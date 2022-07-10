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
    RegisterBonfire(bonfire_flag=13100000, obj=3101950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13100002, obj=3101952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13100003, obj=3101953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13100004, obj=3101954, reaction_distance=5.0)
    RunCommonEvent(20005500, args=(13100800, 13100001, 3100951, 3101951))
    RunCommonEvent(20005781, args=(3101780, 3, 13105161))
    Event_13105810()
    Event_13105812()
    Event_13105820()
    Event_13105811()
    Event_13105813()
    Event_13105815()
    Event_13105814()
    Event_13105840()
    Event_13105841()
    Event_13105880()
    Event_13105825(0, 9, 9, 150, 0.4000000059604645, 9, 3, 13, 11461, 810, 29, 29, 7)
    Event_13105825(1, 10, 10, 270, 0.4000000059604645, 10, 2, 12, 11462, 811, 30, 30, 8)
    Event_13105825(2, 11, 11, 150, 0.4000000059604645, 11, 1, 11, 11463, 812, 31, 31, 9)
    Event_13105830(0, 1, 1, 780, 0.5, 1, 8, 18, 11464, 813, 21, 21, 2)
    Event_13105830(1, 12, 12, 510, 0.4000000059604645, 12, 6, 16, 11465, 814, 32, 32, 3)
    Event_13105830(2, 13, 13, 240, 0.4000000059604645, 13, 4, 14, 11466, 815, 33, 33, 4)
    Event_13105830(3, 14, 14, 150, 0.4000000059604645, 14, 5, 15, 11467, 816, 34, 34, 5)
    Event_13105835(0, 2, 2, 780, 0.5, 2, 7, 17, 11460, 817, 22, 22, 6)
    Event_13100210(0, character=3100730)
    Event_13105212(0, character=3100730)
    Event_13105170()
    Event_13105171()
    Event_13105172()
    Event_13105173()
    Event_13105174()
    Event_13105176()
    Event_13105177()
    RunCommonEvent(20005220, args=(3100200, 700, 1700))
    RunCommonEvent(20005220, args=(3100201, 701, 1701))
    RunCommonEvent(20005111, args=(3100209, 3004, 3102341))
    RunCommonEvent(20005110, args=(3100210, 3102280))
    RunCommonEvent(20005110, args=(3100211, 3102280))
    RunCommonEvent(20005220, args=(3100212, 706, 1706))
    RunCommonEvent(20005220, args=(3100213, 706, 1706))
    RunCommonEvent(20005132, args=(3100213, 3.0, 3102320), arg_types="ifi")
    RunCommonEvent(20005224, args=(3100214, 703, 1703))
    RunCommonEvent(20005330, args=(3100215, 3102611, 13105316))
    RunCommonEvent(20005330, args=(3100216, 3102611, 13105317))
    RunCommonEvent(20005110, args=(3100225, 3102350))
    RunCommonEvent(20005114, args=(3100226, 3102350, 1.5), arg_types="iif")
    RunCommonEvent(20005220, args=(3100227, 700, 1700))
    RunCommonEvent(20005220, args=(3100229, 700, 1700))
    RunCommonEvent(20005110, args=(3100232, 3102314))
    RunCommonEvent(20005220, args=(3100248, 701, 1701))
    RunCommonEvent(20005140, args=(3100200, 0, 3100603))
    RunCommonEvent(20005140, args=(3100201, 0, 3100603))
    RunCommonEvent(20005140, args=(3100227, 0, 3100603))
    RunCommonEvent(20005140, args=(3100228, 0, 3100603))
    RunCommonEvent(20005140, args=(3100231, 0, 3100603))
    RunCommonEvent(20005140, args=(3100240, 0, 3100603))
    RunCommonEvent(20005140, args=(3100241, 0, 3100603))
    RunCommonEvent(20005140, args=(3100242, 0, 3100603))
    RunCommonEvent(20005140, args=(3100243, 0, 3100603))
    RunCommonEvent(20005140, args=(3100244, 0, 3100603))
    RunCommonEvent(20005140, args=(3100245, 0, 3100603))
    RunCommonEvent(20005140, args=(3100246, 0, 3100603))
    RunCommonEvent(20005140, args=(3100247, 0, 3100603))
    RunCommonEvent(20005140, args=(3100248, 0, 3100603))
    RunCommonEvent(20005140, args=(3100602, 0, 3100603))
    RunCommonEvent(20005120, args=(3100200, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100201, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100227, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100228, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100231, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100240, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100241, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100242, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100243, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100244, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100245, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100246, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100247, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100248, 5.0), arg_types="if")
    RunCommonEvent(20005120, args=(3100602, 5.0), arg_types="if")
    RunCommonEvent(20005110, args=(3100236, 3102257))
    Event_13105850(0, 3100250, 700, 1700, 10.0, 3102805, 5.199999809265137)
    Event_13105850(1, 3100251, 701, 1701, 10.0, 3102805, 4.0)
    Event_13105850(2, 3100252, 702, 1702, 10.0, 3102805, 3.200000047683716)
    Event_13105850(3, 3100253, 700, 1700, 10.0, 3102805, 4.800000190734863)
    Event_13105850(4, 3100254, 701, 1701, 10.0, 3102805, 4.400000095367432)
    Event_13105850(5, 3100255, 702, 1702, 10.0, 3102805, 4.5)
    Event_13105850(6, 3100256, 700, 1700, 10.0, 3102805, 4.0)
    Event_13105850(7, 3100257, 701, 1701, 10.0, 3102805, 3.799999952316284)
    Event_13105850(8, 3100258, 702, 1702, 10.0, 3102805, 0.0)
    Event_13105850(9, 3100259, 700, 1700, 10.0, 3102805, 3.299999952316284)
    Event_13105850(10, 3100260, 701, 1701, 10.0, 3102805, 3.799999952316284)
    Event_13105850(11, 3100261, 702, 1702, 10.0, 3102805, 3.9000000953674316)
    Event_13105850(12, 3100262, 700, 1700, 10.0, 3102805, 4.099999904632568)
    Event_13105850(13, 3100263, 701, 1701, 10.0, 3102805, 4.800000190734863)
    Event_13105850(14, 3100264, 702, 1702, 10.0, 3102805, 5.0)
    Event_13105850(15, 3100265, 700, 1700, 10.0, 3102805, 5.5)
    Event_13105850(16, 3100266, 701, 1701, 10.0, 3102805, 5.099999904632568)
    Event_13105870(0, character=3100250, region=3102840)
    Event_13105870(1, character=3100251, region=3102840)
    Event_13105870(2, character=3100252, region=3102840)
    Event_13105870(3, character=3100253, region=3102840)
    Event_13105870(5, character=3100255, region=3102840)
    Event_13105870(6, character=3100256, region=3102840)
    Event_13105870(7, character=3100257, region=3102840)
    Event_13105870(8, character=3100258, region=3102840)
    Event_13105870(9, character=3100259, region=3102840)
    Event_13105870(10, character=3100260, region=3102840)
    Event_13105870(11, character=3100261, region=3102840)
    Event_13105870(13, character=3100263, region=3102840)
    Event_13105870(15, character=3100265, region=3102840)
    Event_13105870(16, character=3100266, region=3102840)
    RunCommonEvent(20005210, args=(3100267, 703, 1703, 6.0), arg_types="iiif")
    RunCommonEvent(20005122, args=(3100268, 3003, 6.5), arg_types="iif")
    RunCommonEvent(20005213, args=(3100269, 703, 1703, 2.0, 3102256), arg_types="iiifi")
    RunCommonEvent(20005111, args=(3100270, 3005, 3102481))
    RunCommonEvent(20005111, args=(3100271, 3005, 3102480))
    Event_13105270()
    RunCommonEvent(20005202, args=(3100300, 30000, 3000, 3102530))
    RunCommonEvent(20005122, args=(3100301, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3100302, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3100303, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3100304, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3100305, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3100306, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005122, args=(3100307, 3000, 2.0), arg_types="iif")
    RunCommonEvent(20005202, args=(3100308, 30000, 3000, 3102530))
    RunCommonEvent(20005122, args=(3100334, 3000, 3.0), arg_types="iif")
    RunCommonEvent(20005202, args=(3100337, 30000, 3000, 3102531))
    Event_13105250(0, 3100329, 0.20000000298023224)
    Event_13105250(1, 3100330, 0.5)
    Event_13105250(2, 3100331, 0.800000011920929)
    Event_13105250(3, 3100332, 0.8999999761581421)
    Event_13105250(4, 3100333, 0.30000001192092896)
    RunCommonEvent(20005119, args=(3100351, 3102370, 3102371, 0, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3100352, 3102560))
    RunCommonEvent(20005110, args=(3100355, 3102811))
    RunCommonEvent(20005330, args=(3100356, 3102811, 13105318))
    RunCommonEvent(20005110, args=(3100357, 3102540))
    RunCommonEvent(20005110, args=(3100358, 3102372))
    RunCommonEvent(20005120, args=(3100359, 3.0), arg_types="if")
    RunCommonEvent(20005330, args=(3100359, 3102811, 13105315))
    Event_13105260(0, character=3100356)
    Event_13105260(1, character=3100358)
    Event_13105260(2, character=3100355)
    Event_13105260(3, character=3100359)
    RunCommonEvent(20005212, args=(3100380, 700, 1700, 4.5, 3102551), arg_types="iiifi")
    RunCommonEvent(20005210, args=(3100383, 700, 1700, 4.5), arg_types="iiif")
    RunCommonEvent(20005212, args=(3100384, 700, 1700, 4.5, 3102551), arg_types="iiifi")
    RunCommonEvent(20005212, args=(3100385, 700, 1700, 7.5, 3102551), arg_types="iiifi")
    RunCommonEvent(20005212, args=(3100386, 700, 1700, 5.5, 3102551), arg_types="iiifi")
    RunCommonEvent(20005212, args=(3100387, 700, 1700, 4.5, 3102551), arg_types="iiifi")
    Event_13105230(0, character=3100388, animation_id=700, animation_id_1=1700, region=3102553)
    Event_13105230(1, character=3100389, animation_id=700, animation_id_1=1700, region=3102553)
    Event_13105230(2, character=3100381, animation_id=700, animation_id_1=1700, region=3102552)
    Event_13105230(3, character=3100382, animation_id=700, animation_id_1=1700, region=3102552)
    RunCommonEvent(20005214, args=(3100400, 702, 1702, 7.5), arg_types="iiif")
    RunCommonEvent(20005119, args=(3100403, 3102301, 3102302, 0, 0, 0, 0, 0))
    RunCommonEvent(20005111, args=(3100403, 3004, 3102301))
    RunCommonEvent(20005119, args=(3100404, 3102301, 3102302, 0, 0, 0, 0, 0))
    RunCommonEvent(20005111, args=(3100404, 3004, 3102301))
    RunCommonEvent(20005202, args=(3100405, 702, 1702, 3102360))
    RunCommonEvent(20005111, args=(3100406, 3004, 3102360))
    RunCommonEvent(20005202, args=(3100407, 701, 1701, 3102361))
    RunCommonEvent(20005205, args=(3100410, 702, 1702, 3102590, 0.699999988079071), arg_types="iiiif")
    RunCommonEvent(20005132, args=(3100411, 2.5, 3102304), arg_types="ifi")
    RunCommonEvent(20005132, args=(3100412, 2.5, 3102304), arg_types="ifi")
    RunCommonEvent(20005205, args=(3100413, 702, 1702, 3102590, 0.5), arg_types="iiiif")
    RunCommonEvent(20005200, args=(3100416, 706, 20002, 3102315))
    RunCommonEvent(20005202, args=(3100417, 701, 1701, 3102304))
    RunCommonEvent(20005202, args=(3100433, 700, 1700, 3102343))
    RunCommonEvent(20005202, args=(3100434, 700, 1700, 3102305))
    RunCommonEvent(20005202, args=(3100435, 701, 1701, 3102305))
    RunCommonEvent(20005110, args=(3100436, 3102320))
    RunCommonEvent(20005290, args=(3100450, -1, -1))
    RunCommonEvent(20005220, args=(3100451, 701, 1701))
    RunCommonEvent(20005290, args=(3100452, -1, -1))
    RunCommonEvent(20005220, args=(3100453, 703, 1703))
    RunCommonEvent(20005220, args=(3100454, 701, 1701))
    RunCommonEvent(20005290, args=(3100455, -1, -1))
    RunCommonEvent(20005290, args=(3100456, -1, -1))
    RunCommonEvent(20005220, args=(3100457, 702, 1702))
    RunCommonEvent(20005220, args=(3100458, 701, 1701))
    RunCommonEvent(20005290, args=(3100460, 703, 1703))
    RunCommonEvent(20005290, args=(3100461, 703, 1703))
    RunCommonEvent(20005290, args=(3100462, 703, 1703))
    RunCommonEvent(20005290, args=(3100463, 703, 1703))
    RunCommonEvent(20005290, args=(3100464, 703, 1703))
    RunCommonEvent(20005290, args=(3100465, 703, 1703))
    RunCommonEvent(20005290, args=(3100466, 703, 1703))
    RunCommonEvent(20005290, args=(3100467, 703, 1703))
    RunCommonEvent(20005290, args=(3100468, 703, 1703))
    RunCommonEvent(20005290, args=(3100469, 703, 1703))
    RunCommonEvent(20005220, args=(3100505, 700, 1700))
    RunCommonEvent(20005220, args=(3100506, 700, 1700))
    RunCommonEvent(20005330, args=(3100507, 3102536, 13105313))
    RunCommonEvent(20005330, args=(3100508, 3102536, 13105314))
    Event_13105340(
        0,
        character=3100462,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104310
    )
    Event_13105340(
        1,
        character=3100463,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104310
    )
    Event_13105340(
        2,
        character=3100465,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104315
    )
    Event_13105340(
        3,
        character=3100466,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104315
    )
    Event_13105340(
        4,
        character=3100467,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104315
    )
    Event_13105340(
        5,
        character=3100468,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104316
    )
    Event_13105340(
        6,
        character=3100469,
        character_1=3100203,
        character_2=3100204,
        region=3102612,
        patrol_information_id=3104316
    )
    RunCommonEvent(20005330, args=(3100550, 3102510, 13105310))
    RunCommonEvent(20005330, args=(3100551, 3102510, 13105311))
    RunCommonEvent(20005330, args=(3100552, 3102510, 13105312))
    RunCommonEvent(20005200, args=(3100601, 700, 1700, 3102450))
    RunCommonEvent(20005210, args=(3100603, 700, 1700, 12.0), arg_types="iiif")
    RunCommonEvent(20005110, args=(3100605, 3102535))
    RunCommonEvent(20005110, args=(3100606, 3102535))
    RunCommonEvent(20005110, args=(3100651, 3102610))
    RunCommonEvent(20005110, args=(3100657, 3102560))
    RunCommonEvent(20005110, args=(3100659, 3102253))
    RunCommonEvent(20005110, args=(3100661, 3102254))
    Event_13105470(0, 3100556, 3102550, 3102570, 0.0)
    Event_13105470(1, 3100557, 3102550, 3102570, 3.0)
    Event_13105470(2, 3100558, 3102551, 3102572, 0.0)
    Event_13105470(3, 3100559, 3102550, 3102570, 1.5)
    Event_13105470(4, 3100560, 3102550, 3102570, 4.5)
    Event_13105470(5, 3100561, 3102550, 3102570, 5.800000190734863)
    Event_13105470(6, 3100562, 3102550, 3102571, 3.5)
    RunCommonEvent(20005350, args=(3100570, 22800000, 53100228))
    Event_13105300()
    Event_13105225(0, character=3100401, region=3102300, region_1=3102313)
    Event_13105320()
    RunCommonEvent(20005341, args=(13100500, 3100831, 30600000))
    RunCommonEvent(20005341, args=(13100501, 3100860, 13102000))
    RunCommonEvent(20005341, args=(13100502, 3100610, 21501000))
    RunCommonEvent(20005341, args=(13100503, 3100611, 21501010))
    Event_13105240()
    RunCommonEvent(20005900, args=(13300901, 13100900))
    RunCommonEvent(20005340, args=(13100900, 3100900))
    RunCommonEvent(20005900, args=(13305910, 13105910))
    RunCommonEvent(20005340, args=(13105910, 3100910))
    Event_13105290(0, character=3100657)
    RunCommonEvent(20005553, args=(3101600, 0, 100, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101601, 0, 110, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101602, 1000000, 1000100, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101603, 1000000, 1000110, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101604, 2000000, 2000100, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101605, 2000000, 2000110, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101607, 3000000, 3000100, 3102380, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101608, 0, 100, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101609, 0, 110, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101610, 1000000, 1000100, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101611, 1000000, 1000110, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101612, 2000000, 2000100, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101613, 2000000, 2000110, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101614, 3000000, 3000100, 3102560, 0.0, 2.0, 0.5, 1.0), arg_types="iiiiffff")
    RunCommonEvent(20005553, args=(3101636, 0, 110, 3102312, 0.0, 2.0, 0.0, 0.30000001192092896), arg_types="iiiiffff")
    RunCommonEvent(
        20005553,
        args=(3101637, 2000000, 2000100, 3102312, 0.0, 2.0, 0.0, 0.30000001192092896),
        arg_types="iiiiffff",
    )
    RunCommonEvent(
        20005553,
        args=(3101638, 2000000, 2000110, 3102253, 0.0, 2.0, 0.0, 0.30000001192092896),
        arg_types="iiiiffff",
    )
    RunCommonEvent(20005553, args=(3101639, 0, 100, 3102312, 0.0, 2.0, 0.0, 0.30000001192092896), arg_types="iiiiffff")
    RunCommonEvent(
        20005553,
        args=(3101640, 1000000, 1000110, 3102312, 0.0, 2.0, 0.0, 0.30000001192092896),
        arg_types="iiiiffff",
    )
    RunCommonEvent(20005553, args=(3101641, 0, 100, 3102312, 0.0, 2.0, 0.0, 0.30000001192092896), arg_types="iiiiffff")
    Event_13105480()
    RegisterLadder(start_climbing_flag=13100260, stop_climbing_flag=13100261, obj=3101400)
    RegisterLadder(start_climbing_flag=13100262, stop_climbing_flag=13100263, obj=3101401)
    RegisterLadder(start_climbing_flag=13100264, stop_climbing_flag=13100265, obj=3101402)
    RegisterLadder(start_climbing_flag=13100266, stop_climbing_flag=13100267, obj=3101404)
    RegisterLadder(start_climbing_flag=13100268, stop_climbing_flag=13100269, obj=3101405)
    RegisterLadder(start_climbing_flag=13100270, stop_climbing_flag=13100271, obj=3101406)
    RegisterLadder(start_climbing_flag=13100272, stop_climbing_flag=13100273, obj=3101408)
    RegisterLadder(start_climbing_flag=13100274, stop_climbing_flag=13100275, obj=3101409)
    RunCommonEvent(20005613, args=(13100440, 3103240, 3101250, 310300, 10010869))
    RunCommonEvent(20005620, args=(13100250, 3101300, 3101300, 3101201, 3101203, 0))
    Event_13105210(
        0,
        flag=13100250,
        entity=3101300,
        obj=3101201,
        obj_act_id=3104201,
        obj_1=3101203,
        obj_act_id_1=3104203,
        obj_2=3101202,
        obj_act_id_2=3104202
    )
    RunCommonEvent(20005614, args=(3101301, 63100420))
    Event_13105510()
    RunCommonEvent(20005610, args=(13100401, 3102215, 3102216))
    RunCommonEvent(20005611, args=(13100401, 3103241, 3101251, 310301))
    RunCommonEvent(20005610, args=(13100402, 3102225, 3102226))
    RunCommonEvent(20005611, args=(13100402, 3104200, 3101240, 310310))
    RunCommonEvent(20005610, args=(13100403, 3102212, 3102213))
    RunCommonEvent(20005611, args=(13100403, 3103260, 3101252, 310301))
    RunCommonEvent(20005611, args=(13100404, 3104210, 3101253, 310311))
    RunCommonEvent(20005614, args=(3101254, 63100432))
    RunCommonEvent(20005520, args=(13100305, 3101330, 3003230))
    RunCommonEvent(20005520, args=(13100306, 3101331, 3003231))
    RunCommonEvent(20005670, args=(31, 0, 3103100), arg_types="BBi")
    RunCommonEvent(20005671, args=(31, 0, 3103101), arg_types="BBi")
    RunCommonEvent(20005672, args=(31, 0, 3103102), arg_types="BBi")
    RunCommonEvent(20005673, args=(31, 0, 3103103), arg_types="BBi")
    Event_13105280(0, flag=13100280, obj=3101282)
    Event_13105281(
        0,
        flag=13100280,
        obj=3101280,
        obj_1=3101281,
        entity=3101282,
        obj_act_id=310500,
        obj_act_id_1=3104230,
        obj_act_id_2=3104231
    )
    Event_13105285(0, obj=3101282)
    Event_13105420(0, flag=53100700, obj=3101570)
    Event_13105420(1, flag=53100710, obj=3101571)
    Event_13105420(2, flag=53100720, obj=3101572)
    Event_13105420(3, flag=53100730, obj=3101573)
    Event_13105420(4, flag=53100740, obj=3101574)
    Event_13105420(5, flag=53100750, obj=3101575)
    Event_13105420(6, flag=53100760, obj=3101576)
    Event_13105420(7, flag=53100770, obj=3101577)
    Event_13105420(9, flag=53100800, obj=3101579)
    RunCommonEvent(20005525, args=(6700, 4200, 3101290, 60))
    RunCommonEvent(20005525, args=(53100630, 3100630, 3101291, 60))
    RunCommonEvent(20005525, args=(53100660, 3100660, 3101292, 60))
    RunCommonEvent(20005524, args=(3101260, 9482))
    Event_13105295()
    RunCommonEvent(20005542, args=(13105351, 3101501, 201, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005542, args=(13105352, 3101502, 201, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005542, args=(13105353, 3101530, 201, 5110, 0.8500000238418579, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005542, args=(13105354, 3101531, 201, 5110, 0.5, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005542, args=(13105355, 3101532, 201, 5110, 0.699999988079071, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005542, args=(13105356, 3101533, 201, 5110, 0.699999988079071, 0.0, 1.0), arg_types="iiiifff")
    RunCommonEvent(20005530, args=(13105380, 3101210))
    RunCommonEvent(20005530, args=(13105381, 3101211))
    RunCommonEvent(20005530, args=(13105382, 3101212))
    RunCommonEvent(20005530, args=(13105383, 3101213))
    RunCommonEvent(20005530, args=(13105384, 3101214))
    RunCommonEvent(20005530, args=(13105385, 3101215))
    RunCommonEvent(20005530, args=(13105386, 3101216))
    RunCommonEvent(20005530, args=(13105387, 3101217))
    RunCommonEvent(20005530, args=(13105388, 3101218))
    RunCommonEvent(20005530, args=(13105389, 3101219))
    RunCommonEvent(20005530, args=(13105390, 3101220))
    RunCommonEvent(20005530, args=(13105391, 3101221))
    RunCommonEvent(20005530, args=(13105392, 3101222))
    RunCommonEvent(20005530, args=(13105393, 3101223))
    RunCommonEvent(20005530, args=(13105394, 3101224))
    RunCommonEvent(20005530, args=(13105395, 3101225))
    RunCommonEvent(20005530, args=(13105396, 3101226))
    RunCommonEvent(20005530, args=(13105397, 3101227))
    RunCommonEvent(20005530, args=(13105398, 3101228))
    RunCommonEvent(20005530, args=(13105399, 3101229))
    RunCommonEvent(20005530, args=(13105400, 3101230))
    RunCommonEvent(20005530, args=(13105401, 3101231))
    RunCommonEvent(20005530, args=(13105402, 3101232))
    RunCommonEvent(20005530, args=(13105403, 3101233))
    RunCommonEvent(20005530, args=(13105404, 3101234))
    RunCommonEvent(20005530, args=(13105405, 3101235))
    RunCommonEvent(20005530, args=(13105406, 3101236))
    RunCommonEvent(20005530, args=(13105407, 3101237))
    RunCommonEvent(20005530, args=(13105408, 3101238))
    RunCommonEvent(20005530, args=(13105409, 3101239))
    RunCommonEvent(20005523, args=(3101270, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3101271, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3101272, 2), arg_types="iB")
    RunCommonEvent(20005060, args=(8220, 8221, 13101180, 13104181, 13105181, 10012030, 9360, 3101180, 30001))
    RunCommonEvent(20005061, args=(8220, 3100741), event_layers=[2, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(20005062, args=(8221, 8222), event_layers=[2, 3, 4, 5, 6, 7, 8, 9])
    Event_13100180()
    RunCommonEvent(20006002, args=(3100705, 1078, 1075, 1079))
    RunCommonEvent(20006003, args=(3100705, 73100180, 1075, 1060, 1061, 1060, 1074))
    Event_13105601(0, character=3100705, animation_id=20000, region=3102705, flag=73100181, special_effect=151)
    RunCommonEvent(20006002, args=(3100700, 1298, 1295, 1299))
    RunCommonEvent(20006003, args=(3100700, 73100130, 1295, 1280, 1281, 1280, 1294))
    RunCommonEvent(20006005, args=(3100700, 73100131, 73100132, 0, 1.0, 90280, 90291, -1), arg_types="iiiifiii")
    RunCommonEvent(20006002, args=(3100710, 1258, 1255, 1259))
    RunCommonEvent(20006003, args=(3100710, 73100212, 1255, 1240, 1241, 1240, 1254))
    RunCommonEvent(20006002, args=(3100715, 1478, 1475, 1479))
    RunCommonEvent(20006001, args=(3100715, 1476, 1477, 73100270, 3))
    RunCommonEvent(20005491, args=(3100195, 3100196, 3102253, 13105667))
    Event_13105665(0, 3100715, 1476, 1477, 73100270, 0.6499999761581421, 1475, 1479)
    RunCommonEvent(20005495, args=(3100195, 3100196, 13100660))
    RunCommonEvent(20005493, args=(3100195, 3100196, 13100660))
    Event_13105663(0, obj=3101190)
    RunCommonEvent(20005496, args=(3101190,))
    RunCommonEvent(20006030, args=(3101715, 4000, 2, 62510, 50006251, 50006251, 1478))
    RunCommonEvent(
        20005490,
        args=(3100196, 3100195, 3101190, 3101190, 10, 5310, 5311, 5312, 5313, 5314, 5315, 5316, 13105668),
    )
    RunCommonEvent(20005492, args=(3102253,))
    RunCommonEvent(20005494)
    RunCommonEvent(20006002, args=(3100720, 1318, 1315, 1319))
    RunCommonEvent(
        20006000,
        args=(3100720, 1316, 1317, 73100330, 0.6499999761581421, 1315, 1319, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3100720, 1316, 1317, 73100330, 3))
    Event_13105681(0, region=3102720)
    Event_13105682(
        0,
        character=3100720,
        flag=1316,
        flag_1=1317,
        flag_2=1280,
        flag_3=1298,
        first_flag=1315,
        last_flag=1319,
        flag_4=1300
    )
    RunCommonEvent(20006040, args=(3100720, 3102721, 159))
    RunCommonEvent(20006002, args=(3100725, 1138, 1135, 1139))
    Event_13105721()
    Event_13105722(0, attacked_entity=3100725)
    RunCommonEvent(20005526, args=(50006083, 60830, 3101700, 61, 8220))
    Event_13105723()
    RunCommonEvent(20006002, args=(3100740, 1598, 1595, 1599))
    RunCommonEvent(
        20006000,
        args=(3100740, 1596, 1597, 73100430, 0.6499999761581421, 1595, 1599, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3100740, 1596, 1597, 73100430, 3))
    Event_13100701(0, character=3100740)
    RunCommonEvent(20006002, args=(3100730, 1398, 1395, 1399))
    RunCommonEvent(
        20006000,
        args=(3100730, 1396, 1397, 73100391, 0.6499999761581421, 1395, 1399, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3100730, 1396, 1397, 73100391, 3))
    RunCommonEvent(20006002, args=(3100731, 1398, 1395, 1399))
    Event_13105741(0, character=3100730, character_1=3100731)
    Event_13105742(0, character=3100731, character_1=3100730)
    Event_13105746()
    Event_13105747()
    Event_13105748()
    RunCommonEvent(20006040, args=(3100731, 3102733, 158))
    RunCommonEvent(
        20006000,
        args=(3100735, 1951, 1952, 13105711, 0.6499999761581421, 1950, 1954, 1),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(3100735, 1951, 1952, 13105711, 3))
    RunCommonEvent(20006002, args=(3100735, 1953, 1950, 1954))
    RunCommonEvent(20006010, args=(73100952, 69003))
    RunCommonEvent(20005900, args=(13100500, 6330))
    Event_13105911()
    Event_13105910()
    Event_13105930(0, obj=3101660, entity=3101661)
    Event_13105912()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13100200()
    Event_13105330()
    Event_13105600(0, character=3100705, animation_id=30000, command_id=2160)
    Event_13105620(0, character=3100700, animation_id=90550)
    Event_13105640(0, character=3100710)
    Event_13105660(0, character=3100715, obj=3101190)
    RunCommonEvent(20005495, args=(3100195, 3100196, 13100660))
    Event_13105680(0, character=3100720, animation_id=90650, destination=3102721, character_1=3100721, command_id=1700)
    Event_13105720(0, character=3100725)
    Event_13105740(0, character=3100730, character_1=3100731)
    Event_13105700(0, character=3100740)
    Event_13105710(0, character=3100735)
    DisableAnimations(3100791)
    DisableCharacterCollision(3100791)
    DisableGravity(3100791)
    DisableAnimations(3100790)
    DisableCharacterCollision(3100790)
    DisableGravity(3100790)
    DisableSoundEvent(sound_id=3103800)
    DisableSoundEvent(sound_id=3103801)
    DisableFlag(13101180)


@RestartOnRest(13105170)
def Event_13105170():
    """Event 13105170"""
    AND_1.Add(FlagEnabled(13105161))
    AND_1.Add(FlagDisabled(13105162))
    AND_1.Add(FlagDisabled(13105163))
    if AND_1:
        return
    DisableCharacter(3100190)
    DisableAnimations(3100190)


@RestartOnRest(13105171)
def Event_13105171():
    """Event 13105171"""
    DisableFlag(13104170)
    DisableFlag(13105170)
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13100800):
        return
    if FlagEnabled(13100720):
        return
    Wait(0.5)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 490))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3102400))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=8.0)
    SetNetworkConnectedFlagState(flag=13105160, state=FlagSetting.On)


@RestartOnRest(13105172)
def Event_13105172():
    """Event 13105172"""
    if FlagEnabled(13100720):
        return
    if FlagEnabled(13105161):
        return
    if FlagEnabled(13105163):
        return
    AND_1.Add(FlagEnabled(13105160))
    AND_1.Add(FlagDisabled(13105161))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012200, display_location_index=1)
    SkipLines(5)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionTrue(2, MAIN)
    DisplayBattlefieldMessage(10012220, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012230, display_location_index=1)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=30310, anchor_entity=3100190, model_point=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(3100190)
    EnableAnimations(3100190)
    SetBackreadStateAlternate(3100190, True)
    ForceAnimation(3100190, 63010, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13105161, state=FlagSetting.On)


@RestartOnRest(13105173)
def Event_13105173():
    """Event 13105173"""
    if FlagEnabled(13100720):
        return
    AND_1.Add(FlagEnabled(13105161))
    AND_1.Add(CharacterDead(3100190))
    
    MAIN.Await(AND_1)
    
    DisplayBanner(BannerType.BlackPhantomDestroyed)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012202, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012222, display_location_index=1)
    Wait(2.0)
    AwardItemLot(4530, host_only=False)
    SetBackreadStateAlternate(3100190, False)
    SetNetworkConnectedFlagState(flag=13105161, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13100720, state=FlagSetting.On)


@RestartOnRest(13105174)
def Event_13105174():
    """Event 13105174"""
    if FlagEnabled(13100720):
        return
    AND_1.Add(FlagEnabled(13105161))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3100190, radius=20.0))
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=13105162, state=FlagSetting.On)


@RestartOnRest(13105176)
def Event_13105176():
    """Event 13105176"""
    if FlagEnabled(13100720):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(13105161))
    AND_1.Add(FlagEnabled(13105162))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    DisableCharacter(3100190)
    DisableAnimations(3100190)
    SetBackreadStateAlternate(3100190, False)
    SetNetworkConnectedFlagState(flag=13105161, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13105163, state=FlagSetting.On)


@RestartOnRest(13105177)
def Event_13105177():
    """Event 13105177"""
    if FlagEnabled(13100720):
        return
    AND_1.Add(FlagEnabled(13105161))
    OR_1.Add(FlagEnabled(13105805))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102800))
    AND_2.Add(OR_1)
    AND_2.Add(PlayerInOwnWorld())
    AND_1.Add(AND_2)
    AND_1.Add(HealthValueNotEqual(3100190, value=0))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(13105163):
        return
    ForceAnimation(3100190, 91030, unknown2=1.0)
    Wait(1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012203, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012223, display_location_index=1)
    Wait(1.0)
    DisableCharacter(3100190)
    DisableAnimations(3100190)
    SetBackreadStateAlternate(3100190, False)
    SetNetworkConnectedFlagState(flag=13105161, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13105163, state=FlagSetting.On)


@RestartOnRest(13105510)
def Event_13105510():
    """Event 13105510"""
    DisableNetworkSync()
    DisableFlag(13105511)
    OR_1.Add(TryingToJoinSession())
    OR_1.Add(TryingToCreateSession())
    OR_1.Add(FlagEnabled(13105161))
    
    MAIN.Await(OR_1)
    
    EnableFlag(13105511)
    AND_1.Add(FlagDisabled(13105161))
    OR_2.Add(TryingToJoinSession())
    OR_2.Add(TryingToCreateSession())
    AND_1.Add(not OR_2)
    
    MAIN.Await(AND_1)
    
    DisableFlag(13105511)
    Restart()


@NeverRestart(13100200)
def Event_13100200():
    """Event 13100200"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    EnableFlag(13100250)


@NeverRestart(13100210)
def Event_13100210(_, character: int):
    """Event 13100210"""
    GotoIfFlagEnabled(Label.L0, flag=13100211)
    DisableMapCollision(collision=3104730)
    DisableAI(character)
    DisableGravity(character)
    EnableInvincibility(character)
    DisableFlag(13100212)
    OR_15.Add(CharacterHuman(PLAYER))
    OR_15.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_15)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3102450))
    AND_1.Add(ObjectBackreadEnabled(obj=3101300))
    
    MAIN.Await(AND_1)
    
    DisableFlag(13100250)
    EnableFlag(13100211)
    SetBackreadStateAlternate(character, True)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(13100212)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=3102731))
    
    Wait(2.0)
    DisableFlag(13100212)
    EnableAI(character)
    SetBackreadStateAlternate(character, False)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    ChangePatrolBehavior(character, patrol_information_id=3104700)
    SetNest(character, region=3102452)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=3102731))
    
    EnableMapCollision(collision=3104730)
    DisableInvincibility(character)
    EnableGravity(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=3102452, destination_type=CoordEntityType.Region, copy_draw_parent=3102452)
    SetNest(character, region=3102452)
    EnableMapCollision(collision=3104730)


@NeverRestart(13105212)
def Event_13105212(_, character: int):
    """Event 13105212"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(13100212))
    
    Move(
        character,
        destination=3101300,
        destination_type=CoordEntityType.Object,
        model_point=803,
        copy_draw_parent=character,
    )
    Restart()


@RestartOnRest(13105200)
def Event_13105200():
    """Event 13105200"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(3101551)


@RestartOnRest(13105910)
def Event_13105910():
    """Event 13105910"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L0, flag=13100280)
    DisableAI(3100504)
    DisableAI(3100590)
    DisableAI(3100592)
    OR_1.Add(FlagEnabled(13100280))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102462))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(CharacterDead(3100295))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    if FlagDisabled(13100280):
        EnableFlag(13100280)
    Wait(2.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13105913)
    EnableAI(3100592)
    EnableAI(3100504)
    OR_2.Add(FlagDisabled(13100280))
    OR_2.Add(TimeElapsed(seconds=15.0))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDead(3100295))
    if AND_2:
        return
    if FlagEnabled(13100280):
        DisableFlag(13100280)


@RestartOnRest(13105911)
def Event_13105911():
    """Event 13105911"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3100295)
    AND_1.Add(FlagEnabled(13105910))
    AND_1.Add(ObjectActivated(obj_act_id=3104231))
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(EntityWithinDistance(entity=3100295, other_entity=PLAYER, radius=5.0))
    AND_3.Add(OR_1)
    AND_3.Add(AND_2)
    OR_2.Add(AND_1)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    EnableAI(3100295)


@RestartOnRest(13105912)
def Event_13105912():
    """Event 13105912"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(13105913))
    
    GotoIfFlagDisabled(Label.L0, flag=13100280)
    Wait(1.5)
    SetAIParamID(3100590, ai_param_id=110070)
    AddSpecialEffect(3100590, 5000)
    EnableAI(3100590)
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(CharacterInsideRegion(character=3100590, region=3102463))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(3100590, 5000)
    SetAIParamID(3100590, ai_param_id=202101)


@RestartOnRest(13105930)
def Event_13105930(_, obj: int, entity: int):
    """Event 13105930"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    CreateObjectVFX(obj, vfx_id=200, model_point=831023)
    CreateObjectVFX(obj, vfx_id=200, model_point=60)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9600, entity=entity))
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    Wait(0.20000000298023224)
    CreateTemporaryVFX(vfx_id=301002, anchor_entity=PLAYER, model_point=220, anchor_type=CoordEntityType.Character)
    PlaySoundEffect(PLAYER, 999999988, sound_type=SoundType.c_CharacterMotion)
    AddSpecialEffect(PLAYER, 2005)
    DeleteObjectVFX(obj)


@RestartOnRest(13105210)
def Event_13105210(
    _,
    flag: int,
    entity: int,
    obj: int,
    obj_act_id: int,
    obj_1: int,
    obj_act_id_1: int,
    obj_2: int,
    obj_act_id_2: int,
):
    """Event 13105210"""
    GotoIfFlagEnabled(Label.L3, flag=flag)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(ObjectActivated(obj_act_id=obj_act_id_2))
    OR_3.Add(FlagEnabled(flag))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3102201))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=3102202))
    OR_6.Add(OR_1)
    OR_6.Add(OR_2)
    OR_6.Add(OR_3)
    OR_6.Add(OR_4)
    OR_6.Add(OR_5)
    
    MAIN.Await(OR_6)
    
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_2)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(2.0)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(2.0)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_1.Add(AllPlayersOutsideRegion(region=3102202))
    AND_1.Add(AllPlayersOutsideRegion(region=3102203))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(entity, 10, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    OR_7.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_8.Add(ObjectActivated(obj_act_id=obj_act_id_2))
    OR_9.Add(FlagDisabled(flag))
    OR_10.Add(CharacterInsideRegion(character=PLAYER, region=3102202))
    OR_11.Add(CharacterInsideRegion(character=PLAYER, region=3102203))
    OR_12.Add(OR_7)
    OR_12.Add(OR_8)
    OR_12.Add(OR_9)
    OR_12.Add(OR_10)
    OR_12.Add(OR_11)
    
    MAIN.Await(OR_12)
    
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_7)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_8)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L6)

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(2.0)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    Wait(2.0)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    AND_2.Add(AllPlayersOutsideRegion(region=3102201))
    AND_2.Add(AllPlayersOutsideRegion(region=3102202))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(entity, 120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(entity, 20, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    DisableFlag(flag)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    Restart()


@RestartOnRest(13105225)
def Event_13105225(_, character: int, region: int, region_1: int):
    """Event 13105225"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    EnableAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3006, wait_for_completion=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(13105230)
def Event_13105230(_, character: int, animation_id: int, animation_id_1: int, region: int):
    """Event 13105230"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAnimations(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    EnableAnimations(character)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13105240)
def Event_13105240():
    """Event 13105240"""
    DisableNetworkSync()
    SetNetworkUpdateRate(3100657, is_fixed=False, update_rate=CharacterUpdateRate.EveryFiveFrames)
    SetBackreadStateAlternate(3100657, False)
    SetBackreadStateAlternate(3100604, False)
    SetBackreadStateAlternate(3100203, False)
    SetBackreadStateAlternate(3100204, False)
    SetBackreadStateAlternate(3100205, False)
    SetBackreadStateAlternate(3100206, False)
    SetBackreadStateAlternate(3100207, False)
    Wait(1.0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3102500))
    
    SetNetworkUpdateRate(3100657, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    SetBackreadStateAlternate(3100657, True)
    SetBackreadStateAlternate(3100604, True)
    SetBackreadStateAlternate(3100203, True)
    SetBackreadStateAlternate(3100204, True)
    SetBackreadStateAlternate(3100205, True)
    SetBackreadStateAlternate(3100206, True)
    SetBackreadStateAlternate(3100207, True)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3102500))
    
    Wait(1.0)
    Restart()


@RestartOnRest(13105250)
def Event_13105250(_, character: int, seconds: float):
    """Event 13105250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableAI(character)
    ForceAnimation(character, 30000, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L0, flag=13100306)
    OR_1.Add(FlagEnabled(13100306))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3102532))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    SkipLinesIfConditionTrue(2, AND_1)
    Wait(seconds)
    ForceAnimation(character, 3000, loop=True, unknown2=1.0)
    EnableGravity(character)
    EnableAI(character)


@RestartOnRest(13105260)
def Event_13105260(_, character: int):
    """Event 13105260"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    AddSpecialEffect(character, 12230)


@RestartOnRest(13105270)
def Event_13105270():
    """Event 13105270"""
    if ThisEventSlotFlagEnabled():
        return
    SetAIParamID(3100200, ai_param_id=124041)
    SetAIParamID(3100201, ai_param_id=124006)
    SetAIParamID(3100227, ai_param_id=124041)
    SetAIParamID(3100228, ai_param_id=124014)
    SetAIParamID(3100229, ai_param_id=124006)
    SetAIParamID(3100231, ai_param_id=124014)
    SetAIParamID(3100240, ai_param_id=124041)
    SetAIParamID(3100241, ai_param_id=124014)
    SetAIParamID(3100242, ai_param_id=124006)
    SetAIParamID(3100243, ai_param_id=124014)
    SetAIParamID(3100244, ai_param_id=124014)
    SetAIParamID(3100245, ai_param_id=124041)
    SetAIParamID(3100246, ai_param_id=124014)
    SetAIParamID(3100247, ai_param_id=124014)
    SetAIParamID(3100248, ai_param_id=124041)
    SetAIParamID(3100602, ai_param_id=124006)
    
    MAIN.Await(CharacterDead(3100603))
    
    SetAIParamID(3100200, ai_param_id=124040)
    SetAIParamID(3100201, ai_param_id=124000)
    SetAIParamID(3100227, ai_param_id=124040)
    SetAIParamID(3100228, ai_param_id=124010)
    SetAIParamID(3100229, ai_param_id=124000)
    SetAIParamID(3100231, ai_param_id=124010)
    SetAIParamID(3100240, ai_param_id=124040)
    SetAIParamID(3100241, ai_param_id=124010)
    SetAIParamID(3100242, ai_param_id=124010)
    SetAIParamID(3100243, ai_param_id=124010)
    SetAIParamID(3100244, ai_param_id=124010)
    SetAIParamID(3100245, ai_param_id=124040)
    SetAIParamID(3100246, ai_param_id=124010)
    SetAIParamID(3100247, ai_param_id=124010)
    SetAIParamID(3100248, ai_param_id=124040)
    SetAIParamID(3100602, ai_param_id=124000)


@RestartOnRest(13105280)
def Event_13105280(_, flag: int, obj: int):
    """Event 13105280"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=2)
    End()


@RestartOnRest(13105281)
def Event_13105281(
    _,
    flag: int,
    obj: int,
    obj_1: int,
    entity: int,
    obj_act_id: int,
    obj_act_id_1: int,
    obj_act_id_2: int,
):
    """Event 13105281"""
    AND_1.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id_2))
    AND_3.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_3)
    Wait(2.799999952316284)
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_1)
    ForceAnimation(obj, 3, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(obj_1, 3, unknown2=1.0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id)
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_3)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(entity, 2, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    EnableObjectActivation(obj, obj_act_id=obj_act_id)
    EnableObjectActivation(obj_1, obj_act_id=obj_act_id)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13105284)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(entity, 0, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    EnableObjectActivation(obj, obj_act_id=obj_act_id)
    EnableObjectActivation(obj_1, obj_act_id=obj_act_id)
    Restart()


@RestartOnRest(13105285)
def Event_13105285(_, obj: int):
    """Event 13105285"""
    MAIN.Await(FlagEnabled(13105284))
    
    DisableFlag(13105284)
    Wait(1.2999999523162842)
    CreateHazard(
        obj_flag=13105286,
        obj=obj,
        model_point=40,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13105287,
        obj=obj,
        model_point=41,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13105288,
        obj=obj,
        model_point=42,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13105289,
        obj=obj,
        model_point=43,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    Restart()


@RestartOnRest(13105290)
def Event_13105290(_, character: int):
    """Event 13105290"""
    MAIN.Await(CharacterInsideRegion(character=character, region=3102600))
    
    AddSpecialEffect(3100657, 5002)
    AddSpecialEffect(3100604, 5002)
    AddSpecialEffect(3100203, 5002)
    AddSpecialEffect(3100204, 5002)
    AddSpecialEffect(3100205, 5002)
    AddSpecialEffect(3100206, 5002)
    AddSpecialEffect(3100207, 5002)
    ReplanAI(3100657)
    ReplanAI(3100604)
    ReplanAI(3100203)
    ReplanAI(3100204)
    ReplanAI(3100205)
    ReplanAI(3100206)
    ReplanAI(3100207)


@RestartOnRest(13105295)
def Event_13105295():
    """Event 13105295"""
    GotoIfObjectDestroyed(Label.L0, obj=3101680)
    
    MAIN.Await(ObjectDestroyed(3101680))
    
    WaitFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(3101681)
    DisableObject(3101682)
    DisableObject(3101683)
    DisableObject(3101684)
    DisableObject(3101685)
    DisableObject(3101686)


@RestartOnRest(13105300)
def Event_13105300():
    """Event 13105300"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3100353)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3102240))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=3100353, radius=5.0))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(OR_2)
    OR_3.Add(AND_3)
    OR_3.Add(Attacked(attacked_entity=3100353, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    EnableAI(3100353)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(3100353)
    SetNetworkUpdateRate(3100353, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3100353, 20000, wait_for_completion=True, unknown2=1.0)
    Wait(5.0)
    SetNetworkUpdateRate(3100353, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13105320)
def Event_13105320():
    """Event 13105320"""
    GotoIfFlagEnabled(Label.L0, flag=1598)
    OR_12.Add(HasAIStatus(3100350, ai_status=AIStatusType.Battle))
    OR_12.Add(CharacterDead(3100350))
    GotoIfConditionTrue(Label.L0, input_condition=OR_12)
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterBackreadEnabled(3100350))
    AddSpecialEffect(3100350, 99006)
    GotoIfTryingToCreateSession(Label.L1)
    GotoIfTryingToJoinSession(Label.L1)
    OR_1.Add(ActionButtonParamActivated(action_button_id=3100000, entity=3100350))
    OR_2.Add(Attacked(attacked_entity=3100350, attacker=PLAYER))
    OR_3.Add(TryingToCreateSession())
    OR_3.Add(TryingToJoinSession())
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(OR_3)
    
    MAIN.Await(OR_4)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(3100350, 99006)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_5.Add(LeavingSession())
    OR_5.Add(Attacked(attacked_entity=3100350, attacker=PLAYER))
    
    MAIN.Await(OR_5)
    
    WaitFrames(frames=1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    if PlayerNotInOwnWorld():
        return
    PlayCutscene(31000000, cutscene_flags=0, player_id=10000, move_to_region=3102270, game_map=UNDEAD_SETTLEMENT)


@RestartOnRest(13105330)
def Event_13105330():
    """Event 13105330"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13100330))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3102460))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AddSpecialEffect(PLAYER, 4610)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    DisableFlag(13100330)
    EnableFlag(13100331)


@RestartOnRest(13105340)
def Event_13105340(_, character: int, character_1: int, character_2: int, region: int, patrol_information_id: int):
    """Event 13105340"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character_1, 5000)
    AddSpecialEffect(character_2, 5000)
    AddSpecialEffect(character_1, 5002)
    AddSpecialEffect(character_2, 5002)
    ChangePatrolBehavior(character_1, patrol_information_id=patrol_information_id)
    ChangePatrolBehavior(character_2, patrol_information_id=patrol_information_id)
    ReplanAI(character_1)
    ReplanAI(character_2)
    Wait(5.0)
    CancelSpecialEffect(character_1, 5000)
    CancelSpecialEffect(character_2, 5000)


@RestartOnRest(13105420)
def Event_13105420(_, flag: int, obj: int):
    """Event 13105420"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    DeleteObjectVFX(obj)
    DisableTreasure(obj=obj)
    CreateObjectVFX(obj, vfx_id=90, model_point=60)
    
    MAIN.Await(ObjectDestroyed(obj))
    
    EnableTreasure(obj=obj)
    DeleteObjectVFX(obj, erase_root=False)


@RestartOnRest(13105470)
def Event_13105470(_, character: int, region: int, destination: int, seconds: float):
    """Event 13105470"""
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    
    MAIN.Await(AND_2)
    
    Wait(seconds)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    ForceAnimation(character, 20000, wait_for_completion=True, unknown2=1.0)
    EnableAnimations(character)
    EnableAI(character)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(13105480)
def Event_13105480():
    """Event 13105480"""
    DisableObject(3101615)
    DisableObject(3101616)
    DisableObject(3101617)
    DisableObject(3101618)
    DisableObject(3101619)
    DisableObject(3101620)
    DisableObject(3101621)
    DisableObject(3101622)
    DisableObject(3101623)
    DisableObject(3101624)
    DisableObject(3101625)
    DisableObject(3101626)
    DisableObject(3101627)
    DisableObject(3101628)
    DisableObject(3101629)
    DisableObject(3101630)
    DisableObject(3101631)
    DisableObject(3101632)
    DisableObject(3101633)
    DisableObject(3101634)
    DisableObject(3101635)
    if ThisEventSlotFlagEnabled():
        return
    EnableObject(3101615)
    EnableObject(3101616)
    EnableObject(3101617)
    EnableObject(3101618)
    EnableObject(3101619)
    EnableObject(3101620)
    EnableObject(3101621)
    EnableObject(3101622)
    EnableObject(3101623)
    EnableObject(3101624)
    EnableObject(3101625)
    EnableObject(3101626)
    EnableObject(3101627)
    EnableObject(3101628)
    EnableObject(3101629)
    EnableObject(3101630)
    EnableObject(3101631)
    EnableObject(3101632)
    EnableObject(3101633)
    EnableObject(3101634)
    EnableObject(3101635)
    ForceAnimation(3101615, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101616, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101617, 1000000, loop=True, unknown2=1.0)
    ForceAnimation(3101618, 3000000, loop=True, unknown2=1.0)
    ForceAnimation(3101619, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101620, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101621, 1000000, loop=True, unknown2=1.0)
    ForceAnimation(3101622, 3000000, loop=True, unknown2=1.0)
    ForceAnimation(3101623, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101624, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101625, 1000000, loop=True, unknown2=1.0)
    ForceAnimation(3101626, 3000000, loop=True, unknown2=1.0)
    ForceAnimation(3101627, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101628, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101629, 1000000, loop=True, unknown2=1.0)
    ForceAnimation(3101630, 3000000, loop=True, unknown2=1.0)
    ForceAnimation(3101631, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101632, 0, loop=True, unknown2=1.0)
    ForceAnimation(3101633, 1000000, loop=True, unknown2=1.0)
    ForceAnimation(3101634, 3000000, loop=True, unknown2=1.0)
    ForceAnimation(3101635, 0, loop=True, unknown2=1.0)
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 12035))
    OR_1.Add(CharacterHasSpecialEffect(3100280, 12035))
    OR_1.Add(CharacterHasSpecialEffect(3100281, 12035))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(3101615, 100, unknown2=1.0)
    ForceAnimation(3101616, 110, unknown2=1.0)
    ForceAnimation(3101617, 1000110, unknown2=1.0)
    ForceAnimation(3101618, 3000100, unknown2=1.0)
    ForceAnimation(3101619, 100, unknown2=1.0)
    ForceAnimation(3101620, 110, unknown2=1.0)
    ForceAnimation(3101621, 1000110, unknown2=1.0)
    ForceAnimation(3101622, 3000100, unknown2=1.0)
    ForceAnimation(3101623, 100, unknown2=1.0)
    ForceAnimation(3101624, 110, unknown2=1.0)
    ForceAnimation(3101625, 1000110, unknown2=1.0)
    ForceAnimation(3101626, 3000100, unknown2=1.0)
    ForceAnimation(3101627, 100, unknown2=1.0)
    ForceAnimation(3101628, 110, unknown2=1.0)
    ForceAnimation(3101629, 1000110, unknown2=1.0)
    ForceAnimation(3101630, 3000100, unknown2=1.0)
    ForceAnimation(3101631, 100, unknown2=1.0)
    ForceAnimation(3101632, 110, unknown2=1.0)
    ForceAnimation(3101633, 1000110, unknown2=1.0)
    ForceAnimation(3101634, 3000100, unknown2=1.0)
    ForceAnimation(3101635, 100, unknown2=1.0)


@RestartOnRest(13105810)
def Event_13105810():
    """Event 13105810"""
    DisableCharacter(3100800)
    DisableAI(3100800)
    DisableHealthBar(3100800)
    DisableSpawner(entity=3104810)
    DisableCharacter(3100250)
    DisableCharacter(3100251)
    DisableCharacter(3100252)
    DisableCharacter(3100253)
    DisableCharacter(3100254)
    DisableCharacter(3100255)
    DisableCharacter(3100256)
    DisableCharacter(3100257)
    DisableCharacter(3100258)
    DisableCharacter(3100259)
    DisableCharacter(3100260)
    DisableCharacter(3100261)
    DisableCharacter(3100262)
    DisableCharacter(3100263)
    DisableCharacter(3100264)
    DisableCharacter(3100265)
    DisableCharacter(3100266)
    DisableAnimations(3100250)
    DisableAnimations(3100251)
    DisableAnimations(3100252)
    DisableAnimations(3100253)
    DisableAnimations(3100254)
    DisableAnimations(3100255)
    DisableAnimations(3100256)
    DisableAnimations(3100257)
    DisableAnimations(3100258)
    DisableAnimations(3100259)
    DisableAnimations(3100260)
    DisableAnimations(3100261)
    DisableAnimations(3100262)
    DisableAnimations(3100263)
    DisableAnimations(3100264)
    DisableAnimations(3100265)
    DisableAnimations(3100266)
    if FlagEnabled(13100800):
        return
    EnableCharacter(3100800)
    EnableCharacter(3100250)
    EnableCharacter(3100251)
    EnableCharacter(3100252)
    EnableCharacter(3100253)
    EnableCharacter(3100255)
    EnableCharacter(3100256)
    EnableCharacter(3100257)
    EnableCharacter(3100258)
    EnableCharacter(3100259)
    EnableCharacter(3100260)
    EnableCharacter(3100261)
    EnableCharacter(3100263)
    EnableCharacter(3100265)
    EnableCharacter(3100266)
    EnableAnimations(3100250)
    EnableAnimations(3100251)
    EnableAnimations(3100252)
    EnableAnimations(3100253)
    EnableAnimations(3100255)
    EnableAnimations(3100256)
    EnableAnimations(3100257)
    EnableAnimations(3100258)
    EnableAnimations(3100259)
    EnableAnimations(3100260)
    EnableAnimations(3100261)
    EnableAnimations(3100263)
    EnableAnimations(3100265)
    EnableAnimations(3100266)
    DisableMapCollision(collision=3104801)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(3100800)
    SetNetworkUpdateRate(3100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableHealthBar(3100800)
    EnableInvincibility(3100800)
    SetLockOnPoint(character=3100800, lock_on_model_point=220, state=False)
    SetLockOnPoint(character=3100800, lock_on_model_point=221, state=False)
    ForceAnimation(3100800, 700, loop=True, unknown2=1.0)
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102805))
    
    MAIN.Await(OR_1)
    
    Wait(2.0)
    EnableAI(3100800)
    SetNetworkUpdateRate(3100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3100800, 1700, skip_transition=True, unknown2=1.0)
    DisableInvincibility(3100800)
    EnableAI(3100800)
    SetNetworkUpdateRate(3100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    if FlagDisabled(13105811):
        EnableSpawner(entity=3104810)
    SetLockOnPoint(character=3100800, lock_on_model_point=220, state=True)
    SetLockOnPoint(character=3100800, lock_on_model_point=221, state=True)
    DisableNetworkSync()
    EnableBossHealthBar(3100800, name=905180)
    EnableFlag(13105803)
    EnableFlag(13100801)


@RestartOnRest(13105811)
def Event_13105811():
    """Event 13105811"""
    if FlagEnabled(13100800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3100800, tae_event_id=100))
    
    DisableSpawner(entity=3104810)
    DisableMapPiece(map_piece_id=3104805)
    ForceAnimation(3101802, 0, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(3101802, 1, loop=True, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(13105812)
def Event_13105812():
    """Event 13105812"""
    if FlagEnabled(13100800):
        return
    
    MAIN.Await(HealthLessThanOrEqual(3100800, value=0.0))
    
    Wait(1.0)
    PlaySoundEffect(3100800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3100800))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3100800)
    DisableBossHealthBar(3100800, name=905180)
    EnableFlag(13100800)
    EnableFlag(9303)
    EnableFlag(6303)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(13105813)
def Event_13105813():
    """Event 13105813"""
    if FlagEnabled(13100800):
        return
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102802))
    OR_1.Add(CharacterInsideRegion(character=3100800, region=3102802))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4070)
    AddSpecialEffect(3100800, 4070)
    AddSpecialEffect(PLAYER, 4050)
    AddSpecialEffect(3100800, 4050)
    AddSpecialEffect(PLAYER, 4500)
    Wait(3.0)
    Restart()


@RestartOnRest(13105814)
def Event_13105814():
    """Event 13105814"""
    if FlagEnabled(13100800):
        return
    EnableObject(3101801)
    DisableObject(3101802)
    
    MAIN.Await(CharacterHasTAEEvent(3100800, tae_event_id=100))
    
    EnableMapCollision(collision=3104801)
    CreateTemporaryVFX(vfx_id=831110, anchor_entity=3101820, model_point=200, anchor_type=CoordEntityType.Object)
    EnableFlag(13100820)
    WaitFrames(frames=50)
    DisableObject(3101801)
    EnableObject(3101802)
    DisableMapCollision(collision=3104800)
    DisableObject(3106451)
    DisableObject(3106452)
    DisableObject(3106453)
    DisableObject(3106454)
    DisableObject(3106460)
    DisableMapPiece(map_piece_id=3104862)
    DisableMapPiece(map_piece_id=3104859)
    DisableMapPiece(map_piece_id=3104853)
    DisableMapPiece(map_piece_id=3104858)
    DisableMapPiece(map_piece_id=3104852)
    DisableMapPiece(map_piece_id=3104855)
    DisableMapPiece(map_piece_id=3104856)
    DisableMapPiece(map_piece_id=3104857)
    DisableMapPiece(map_piece_id=3104854)
    DisableMapPiece(map_piece_id=3104850)
    DisableMapPiece(map_piece_id=3104851)
    DisableMapPiece(map_piece_id=3104861)
    DisableMapPiece(map_piece_id=3104863)
    DisableMapPiece(map_piece_id=3104864)
    DisableMapPiece(map_piece_id=3104865)
    DisableMapPiece(map_piece_id=3104866)
    DisableMapPiece(map_piece_id=3104867)
    DisableMapPiece(map_piece_id=3104868)
    WaitFrames(frames=5)
    DisableObject(3101810)
    WaitFrames(frames=12)
    DisableObject(3101811)
    WaitFrames(frames=5)
    DisableObject(3101812)
    WaitFrames(frames=2)
    DisableObject(3101813)
    DestroyObject(3101866)
    Wait(0.10000000149011612)
    DestroyObject(3101867)
    Wait(0.10000000149011612)
    DestroyObject(3101868)
    Wait(0.10000000149011612)
    DestroyObject(3101860)
    Wait(0.10000000149011612)
    DestroyObject(3101861)
    Wait(0.10000000149011612)
    DestroyObject(3101862)
    Wait(0.30000001192092896)
    DestroyObject(3101863)
    DestroyObject(3101864)
    DestroyObject(3101865)
    EnableFlag(13105881)


@RestartOnRest(13105815)
def Event_13105815():
    """Event 13105815"""
    if FlagEnabled(13100800):
        return
    CreateNPCPart(3100800, npc_part_id=3, part_index=NPCPartType.Part3, part_health=999999)
    SetNPCPartEffects(3100800, npc_part_id=3, material_sfx_id=110, material_vfx_id=110)
    CreateNPCPart(
        3100800,
        npc_part_id=15,
        part_index=NPCPartType.Part15,
        part_health=999999,
        body_damage_correction=0.10000000149011612,
    )
    SetNPCPartEffects(3100800, npc_part_id=15, material_sfx_id=105, material_vfx_id=105)
    CreateNPCPart(
        3100800,
        npc_part_id=4,
        part_index=NPCPartType.Part4,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=4, material_sfx_id=105, material_vfx_id=105)
    CreateNPCPart(
        3100800,
        npc_part_id=5,
        part_index=NPCPartType.Part5,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=5, material_sfx_id=105, material_vfx_id=105)
    CreateNPCPart(
        3100800,
        npc_part_id=6,
        part_index=NPCPartType.Part6,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=6, material_sfx_id=105, material_vfx_id=105)
    CreateNPCPart(
        3100800,
        npc_part_id=7,
        part_index=NPCPartType.Part7,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=7, material_sfx_id=105, material_vfx_id=105)
    CreateNPCPart(
        3100800,
        npc_part_id=8,
        part_index=NPCPartType.Part8,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=8, material_sfx_id=105, material_vfx_id=105)
    SetDisplayMask(3100800, bit_index=1, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=3, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=4, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=5, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=6, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=7, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=19, switch_type=OnOffChange.Off)


@RestartOnRest(13105820)
def Event_13105820():
    """Event 13105820"""
    RunCommonEvent(20005800, args=(13100800, 3101800, 3102800, 13105805, 3101800, 3100800, 13100801, 0))
    RunCommonEvent(20005801, args=(13100800, 3101800, 3102800, 13105805, 3101800, 13105806))
    RunCommonEvent(20005820, args=(13100800, 3101800, 4, 13100801))
    RunCommonEvent(20001836, args=(13100800, 13105805, 13105806, 13105803, 3103800, 3103801, 13105814))
    RunCommonEvent(20005840, args=(3101800,))
    RunCommonEvent(20005841, args=(3101800,))
    RunCommonEvent(20005837, args=(13100800, 3100800, 16.0, 5180, 5180, 13105805, 13105806), arg_types="iifiiii")
    RunCommonEvent(20005810, args=(13100800, 3101800, 3102800, 10000))


@RestartOnRest(13105825)
def Event_13105825(
    _,
    npc_part_id: short,
    part_index: short,
    part_health: int,
    body_damage_correction: float,
    npc_part_id_1: int,
    bit_index: uchar,
    bit_index_1: uchar,
    special_effect_id: int,
    model_point: int,
    npc_part_id_2: short,
    npc_part_id_3: int,
    bit_index_2: uchar,
):
    """Event 13105825"""
    if FlagEnabled(13100800):
        return
    
    MAIN.Await(FlagEnabled(13105805))
    
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        body_damage_correction=body_damage_correction,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_1, material_sfx_id=110, material_vfx_id=110)
    GotoIfThisEventSlotFlagEnabled(Label.L2)
    
    MAIN.Await(CharacterPartHealthLessThanOrEqual(3100800, npc_part_id=npc_part_id_1, value=0))
    
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(3100800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(3100800, special_effect_id)
    CreateTemporaryVFX(
        vfx_id=651850,
        anchor_entity=3100800,
        model_point=model_point,
        anchor_type=CoordEntityType.Character,
    )
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3100800, 11451))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHasSpecialEffect(3100800, 11451))
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    AddSpecialEffect(3100800, 11452)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3100800, 20002, skip_transition=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id_2,
        part_index=part_index,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=105, material_vfx_id=105)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(3100800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id_2,
        part_index=part_index,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=105, material_vfx_id=105)


@RestartOnRest(13105830)
def Event_13105830(
    _,
    npc_part_id: short,
    part_index: short,
    part_health: int,
    body_damage_correction: float,
    npc_part_id_1: int,
    bit_index: uchar,
    bit_index_1: uchar,
    special_effect_id: int,
    model_point: int,
    npc_part_id_2: short,
    npc_part_id_3: int,
    bit_index_2: uchar,
):
    """Event 13105830"""
    if FlagEnabled(13100800):
        return
    
    MAIN.Await(FlagEnabled(13105805))
    
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    
    MAIN.Await(CharacterHasSpecialEffect(3100800, 5404))
    
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.On)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        body_damage_correction=body_damage_correction,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_1, material_sfx_id=110, material_vfx_id=110)
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=139, material_vfx_id=139)
    
    MAIN.Await(CharacterPartHealthLessThanOrEqual(3100800, npc_part_id=npc_part_id_1, value=0))
    
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(3100800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(3100800, special_effect_id)
    CreateTemporaryVFX(
        vfx_id=651850,
        anchor_entity=3100800,
        model_point=model_point,
        anchor_type=CoordEntityType.Character,
    )
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3100800, 11451))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHasSpecialEffect(3100800, 11451))
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    AddSpecialEffect(3100800, 11452)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3100800, 20002, skip_transition=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id_2,
        part_index=part_index,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=105, material_vfx_id=105)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(3100800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id_2,
        part_index=part_index,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=105, material_vfx_id=105)


@RestartOnRest(13105835)
def Event_13105835(
    _,
    npc_part_id: short,
    part_index: short,
    part_health: int,
    body_damage_correction: float,
    npc_part_id_1: int,
    bit_index: uchar,
    bit_index_1: uchar,
    special_effect_id: int,
    model_point: int,
    npc_part_id_2: short,
    npc_part_id_3: int,
    bit_index_2: uchar,
):
    """Event 13105835"""
    if FlagEnabled(13100800):
        return
    
    MAIN.Await(FlagEnabled(13105805))
    
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        body_damage_correction=body_damage_correction,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_1, material_sfx_id=110, material_vfx_id=110)
    GotoIfThisEventSlotFlagEnabled(Label.L2)
    
    MAIN.Await(CharacterPartHealthLessThanOrEqual(3100800, npc_part_id=npc_part_id_1, value=0))
    
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(3100800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(3100800, special_effect_id)
    CreateTemporaryVFX(
        vfx_id=651850,
        anchor_entity=3100800,
        model_point=model_point,
        anchor_type=CoordEntityType.Character,
    )
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3100800, 11451))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHasSpecialEffect(3100800, 11451))
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    AddSpecialEffect(3100800, 11452)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3100800, 20002, skip_transition=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    AICommand(3100800, command_id=10, command_slot=0)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id_2,
        part_index=part_index,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=105, material_vfx_id=105)
    
    MAIN.Await(CharacterHasSpecialEffect(3100800, 11453))
    
    AddSpecialEffect(3100800, 5840)
    
    MAIN.Await(CharacterHasSpecialEffect(3100800, 5404))
    
    CancelSpecialEffect(3100800, 5840)
    AICommand(3100800, command_id=-1, command_slot=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    SetCollisionMask(3100800, bit_index=bit_index_2, switch_type=OnOffChange.Off)
    SetDisplayMask(3100800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(3100800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    CreateNPCPart(
        3100800,
        npc_part_id=npc_part_id_2,
        part_index=part_index,
        part_health=999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
    )
    SetNPCPartEffects(3100800, npc_part_id=npc_part_id_3, material_sfx_id=105, material_vfx_id=105)


@RestartOnRest(13105840)
def Event_13105840():
    """Event 13105840"""
    if FlagDisabled(13100800):
        return
    DisableObject(3101801)
    DisableObject(3101802)
    DisableMapCollision(collision=3104800)
    EnableMapCollision(collision=3104801)
    DisableObject(3106451)
    DisableObject(3106452)
    DisableObject(3106453)
    DisableObject(3106454)
    DisableObject(3106460)
    DisableMapPiece(map_piece_id=3104805)
    DisableMapPiece(map_piece_id=3104862)
    DisableMapPiece(map_piece_id=3104859)
    DisableMapPiece(map_piece_id=3104853)
    DisableMapPiece(map_piece_id=3104858)
    DisableMapPiece(map_piece_id=3104852)
    DisableMapPiece(map_piece_id=3104855)
    DisableMapPiece(map_piece_id=3104856)
    DisableMapPiece(map_piece_id=3104857)
    DisableMapPiece(map_piece_id=3104854)
    DisableMapPiece(map_piece_id=3104850)
    DisableMapPiece(map_piece_id=3104851)
    DisableMapPiece(map_piece_id=3104861)
    DisableMapPiece(map_piece_id=3104863)
    DisableMapPiece(map_piece_id=3104864)
    DisableMapPiece(map_piece_id=3104865)
    DisableMapPiece(map_piece_id=3104866)
    DisableMapPiece(map_piece_id=3104867)
    DisableMapPiece(map_piece_id=3104868)
    DisableObject(3101810)
    DisableObject(3101811)
    DisableObject(3101812)
    DisableObject(3101813)


@RestartOnRest(13105841)
def Event_13105841():
    """Event 13105841"""
    if FlagDisabled(13100800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3102802))
    
    AddSpecialEffect(PLAYER, 4070)
    AddSpecialEffect(PLAYER, 4050)
    AddSpecialEffect(PLAYER, 4500)
    Wait(5.0)
    Restart()


@RestartOnRest(13105850)
def Event_13105850(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    region: int,
    seconds: float,
):
    """Event 13105850"""
    if FlagEnabled(13100800):
        return
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    SkipLinesIfConditionTrue(1, AND_3)
    Wait(seconds)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_4:
        return
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    CancelSpecialEffect(character, 12091)
    ReplanAI(character)
    End()


@RestartOnRest(13105870)
def Event_13105870(_, character: int, region: int):
    """Event 13105870"""
    if FlagEnabled(13100800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    EnableCharacter(character)
    EnableAnimations(character)
    Wait(3.0)
    Restart()


@RestartOnRest(13105880)
def Event_13105880():
    """Event 13105880"""
    if FlagEnabled(13100800):
        return
    if FlagEnabled(13105881):
        return
    
    MAIN.Await(FlagEnabled(13105805))
    
    ActivateMultiplayerBuffs(3105801)
    Wait(3.0)
    Restart()


@RestartOnRest(13100180)
def Event_13100180():
    """Event 13100180"""
    DisableFlag(13101180)
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(1124))
    OR_1.Add(FlagEnabled(1126))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(9303))
    AND_1.Add(FlagEnabled(9314))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13101180)


@NeverRestart(13105182)
def Event_13105182():
    """Event 13105182"""
    DisableNetworkSync()
    if FlagEnabled(8222):
        return
    if FlagDisabled(8221):
        return
    
    MAIN.Await(FlagEnabled(8221))
    
    EnableFlag(8222)


@NeverRestart(13105600)
def Event_13105600(_, character: int, animation_id: int, command_id: int):
    """Event 13105600"""
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
    AND_3.Add(FlagEnabled(1060))
    AND_3.Add(FlagEnabled(138))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1063, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000055)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1060)
    GotoIfFlagEnabled(Label.L2, flag=1063)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1078)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EzstateAIRequest(character, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(13105601)
def Event_13105601(_, character: int, animation_id: int, region: int, flag: int, special_effect: int):
    """Event 13105601"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    OR_15.Add(CharacterHasSpecialEffect(character, special_effect))
    if not OR_15:
        return RESTART
    ForceAnimation(character, animation_id, unknown2=1.0)
    SetNest(character, region=region)
    Restart()


@NeverRestart(13105620)
def Event_13105620(_, character: int, animation_id: int):
    """Event 13105620"""
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
    GotoIfFlagDisabled(Label.L10, flag=1295)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000066)
    DisableFlagRange((73100131, 73100133))

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1280)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, flag=1298)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(13105640)
def Event_13105640(_, character: int):
    """Event 13105640"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1255, 1259))
    DisableNetworkConnectedFlagRange(flag_range=(1255, 1259))
    SetNetworkConnectedFlagState(flag=1255, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(70000064))
    AND_1.Add(FlagEnabled(1256))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1255, 1259))
    SetNetworkConnectedFlagState(flag=1255, state=FlagSetting.On)
    DisableFlag(74000460)
    SkipLinesIfFlagRangeAnyEnabled(2, (1240, 1254))
    DisableNetworkConnectedFlagRange(flag_range=(1240, 1254))
    SetNetworkConnectedFlagState(flag=1240, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1255)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(73100211)
    DisableFlag(70000064)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1240)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1258)
    SetTeamType(character, TeamType.FriendlyNPC)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(13105660)
def Event_13105660(_, character: int, obj: int):
    """Event 13105660"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1475, 1479))
    DisableNetworkConnectedFlagRange(flag_range=(1475, 1479))
    SetNetworkConnectedFlagState(flag=1475, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(70000075))
    AND_1.Add(FlagEnabled(1476))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1475, 1479))
    SetNetworkConnectedFlagState(flag=1475, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1475)
    SkipLinesIfFlagRangeAnyEnabled(2, (1460, 1474))
    DisableNetworkConnectedFlagRange(flag_range=(1460, 1474))
    SetNetworkConnectedFlagState(flag=1460, state=FlagSetting.On)
    if FlagEnabled(1462):
        DisableNetworkConnectedFlagRange(flag_range=(1460, 1474))
        SetNetworkConnectedFlagState(flag=1463, state=FlagSetting.On)
        DisableNetworkConnectedFlagRange(flag_range=(1475, 1479))
        SetNetworkConnectedFlagState(flag=1478, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000075)
    OR_1.Add(PlayerHasGood(462))
    OR_1.Add(PlayerHasGood(463))
    SkipLinesIfConditionTrue(3, OR_1)
    DisableFlag(50006250)
    SetNetworkConnectedFlagState(flag=13100660, state=FlagSetting.Off)
    SkipLines(2)
    EnableFlag(50006250)
    SetNetworkConnectedFlagState(flag=13100660, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L0, flag=1460)
    GotoIfFlagEnabled(Label.L0, flag=1462)
    GotoIfFlagEnabled(Label.L1, flag=1463)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L10, flag=1476)
    GotoIfFlagEnabled(Label.L11, flag=1478)
    ForceAnimation(character, 30002, loop=True, skip_transition=True, unknown2=1.0)
    SetTeamType(character, TeamType.FriendlyNPC)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 30004, loop=True, skip_transition=True, unknown2=1.0)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Change)
    DisableObject(obj)
    End()


@NeverRestart(13105663)
def Event_13105663(_, obj: int):
    """Event 13105663"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(1478):
        return
    
    MAIN.Await(ObjectBackreadEnabled(obj=obj))
    
    WaitFrames(frames=1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3102460))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    ForceAnimation(obj, 10, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)
    DisableFlagRange((13105675, 13105676))
    EnableRandomFlagInRange(flag_range=(13105675, 13105676))
    if FlagDisabled(13105675):
        Wait(4.0)
    if TryingToCreateSession():
        return
    ForceAnimation(obj, 10, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)
    DisableFlagRange((13105675, 13105676))
    EnableRandomFlagInRange(flag_range=(13105675, 13105676))
    if FlagDisabled(13105675):
        Wait(4.0)
    if TryingToCreateSession():
        return
    ForceAnimation(obj, 10, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3102290))
    
    if FlagEnabled(1478):
        return
    EnableFlag(13105663)
    if TryingToCreateSession():
        return
    ForceAnimation(obj, 10, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)
    DisableFlagRange((13105675, 13105676))
    EnableRandomFlagInRange(flag_range=(13105675, 13105676))
    if FlagDisabled(13105675):
        Wait(4.0)
    if TryingToCreateSession():
        return
    ForceAnimation(obj, 10, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)
    DisableFlagRange((13105675, 13105676))
    EnableRandomFlagInRange(flag_range=(13105675, 13105676))
    if FlagDisabled(13105675):
        Wait(4.0)
    if TryingToCreateSession():
        return
    ForceAnimation(obj, 10, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(obj, 0, loop=True, unknown2=1.0)


@NeverRestart(13105665)
def Event_13105665(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    value: float,
    first_flag: int,
    last_flag: int,
):
    """Event 13105665"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(HealthGreaterThan(character, value=0.0))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(HealthLessThan(character, value=value))
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(flag_2))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    SaveRequest()
    ForceAnimation(character, 0, unknown2=1.0)
    Restart()


@RestartOnRest(13105666)
def Event_13105666(_, obj: int):
    """Event 13105666"""
    if FlagEnabled(1478):
        return
    
    MAIN.Await(FlagEnabled(1478))
    
    DisableObject(obj)


@RestartOnRest(13105670)
def Event_13105670():
    """Event 13105670"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 12035))
    
    SetCameraVibration(vibration_id=104, anchor_entity=3102253, anchor_type=CoordEntityType.Region)
    Wait(1.5)
    Restart()


@NeverRestart(13105680)
def Event_13105680(_, character: int, animation_id: int, destination: int, character_1: int, command_id: int):
    """Event 13105680"""
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
    AND_3.Add(FlagEnabled(1302))
    AND_3.Add(FlagEnabled(74000650))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1303, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1303))
    AND_4.Add(FlagEnabled(9308))
    AND_4.Add(FlagDisabled(73101740))
    AND_4.Add(FlagDisabled(73101750))
    AND_4.Add(FlagDisabled(73101760))
    AND_4.Add(FlagDisabled(73101770))
    AND_4.Add(FlagDisabled(73101780))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1305, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1315, 1319))
    SetNetworkConnectedFlagState(flag=1318, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000067)
    if FlagEnabled(1315):
        DisableFlag(73100320)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1300)
    GotoIfFlagEnabled(Label.L3, flag=1305)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L1, flag=1316)
    GotoIfFlagEnabled(Label.L1, flag=1317)
    GotoIfFlagEnabled(Label.L2, flag=1318)
    ForceAnimation(character, animation_id, unknown2=1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
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

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    EzstateAIRequest(character_1, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character_1)
    End()


@NeverRestart(13105681)
def Event_13105681(_, region: int):
    """Event 13105681"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(73100301):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    EnableFlag(73100301)


@NeverRestart(13105682)
def Event_13105682(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    first_flag: int,
    last_flag: int,
    flag_4: int,
):
    """Event 13105682"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_4))
    OR_1.Add(FlagEnabled(first_flag))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SaveRequest()
    WaitFrames(frames=1)
    AND_2.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(character, 0, unknown2=1.0)


@NeverRestart(13105700)
def Event_13105700(_, character: int):
    """Event 13105700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1595, 1599))
    DisableNetworkConnectedFlagRange(flag_range=(1595, 1599))
    SetNetworkConnectedFlagState(flag=1595, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1596))
    AND_1.Add(FlagEnabled(70000081))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1595, 1599))
    SetNetworkConnectedFlagState(flag=1595, state=FlagSetting.On)
    AND_2.Add(FlagDisabled(1598))
    AND_2.Add(FlagEnabled(13100820))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1595, 1599))
    SetNetworkConnectedFlagState(flag=1598, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1580, 1594))
    DisableNetworkConnectedFlagRange(flag_range=(1580, 1594))
    SetNetworkConnectedFlagState(flag=1580, state=FlagSetting.On)
    GotoIfFlagEnabled(Label.L9, flag=1595)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000081)
    if FlagEnabled(1595):
        DisableFlag(73100420)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1580)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L16, flag=1596)
    GotoIfFlagEnabled(Label.L18, flag=1598)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(13100701)
def Event_13100701(_, character: int):
    """Event 13100701"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagDisabled(1598))
    AND_1.Add(FlagEnabled(13100820))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    ForceAnimation(character, 90670, loop=True, skip_transition=True, unknown2=1.0)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)


@NeverRestart(13105710)
def Event_13105710(_, character: int):
    """Event 13105710"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1950, 1954))
    DisableNetworkConnectedFlagRange(flag_range=(1950, 1954))
    SetNetworkConnectedFlagState(flag=1950, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1952)
    GotoIfFlagEnabled(Label.L1, flag=1953)
    SetTeamType(character, TeamType.FriendlyNPC)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(13105720)
def Event_13105720(_, character: int):
    """Event 13105720"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1135, 1139))
    DisableNetworkConnectedFlagRange(flag_range=(1135, 1139))
    SetNetworkConnectedFlagState(flag=1135, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1120, 1134))
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1120, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1135)
    AND_1.Add(FlagEnabled(1127))
    AND_1.Add(FlagEnabled(74000760))
    AND_1.Add(FlagEnabled(74000756))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1139))
    SetNetworkConnectedFlagState(flag=1130, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1137, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)

    # --- Label 20 --- #
    DefineLabel(20)
    if FlagDisabled(1138):
        GotoIfFlagEnabled(Label.L0, flag=1130)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 69001, unknown2=1.0)
    End()


@RestartOnRest(13105721)
def Event_13105721():
    """Event 13105721"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(6710):
        return
    
    MAIN.Await(FlagEnabled(8220))
    
    AwardItemLot(4210, host_only=False)


@RestartOnRest(13105722)
def Event_13105722(_, attacked_entity: int):
    """Event 13105722"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(1130):
        return
    if FlagEnabled(1138):
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacked_entity, radius=6.0))
    OR_2.Add(Attacked(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(attacked_entity, 69002, unknown2=1.0)


@RestartOnRest(13105723)
def Event_13105723():
    """Event 13105723"""
    if FlagEnabled(8220):
        return
    
    MAIN.Await(FlagEnabled(8221))
    
    SetCharacterTalkRange(character=3100726, distance=90.0)


@NeverRestart(13105740)
def Event_13105740(_, character: int, character_1: int):
    """Event 13105740"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    DisableFlag(13100212)
    SkipLinesIfFlagRangeAnyEnabled(2, (1395, 1399))
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    AND_14.Add(FlagEnabled(1396))
    AND_14.Add(FlagEnabled(70000071))
    AND_14.Add(FlagEnabled(13100500))
    SkipLinesIfConditionFalse(4, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1399))
    SetNetworkConnectedFlagState(flag=1394, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    EnableFlag(73100350)
    AND_15.Add(FlagEnabled(1396))
    AND_15.Add(FlagEnabled(70000071))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1380, 1394))
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1380, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1395)
    AND_1.Add(FlagEnabled(1382))
    AND_1.Add(FlagEnabled(73100365))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1394, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000071)
    if FlagEnabled(1395):
        DisableFlag(73100390)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1380)
    GotoIfFlagEnabled(Label.L2, flag=1382)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    if FlagEnabled(1398):
        Move(character, destination=3102452, destination_type=CoordEntityType.Region, copy_draw_parent=3102452)
        WaitFrames(frames=1)
        DropMandatoryTreasure(character)
        GotoIfFlagEnabled(Label.L18, flag=1398)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1396, 1397))
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    EnableFlag(73100370)
    GotoIfFlagEnabled(Label.L16, flag=13100500)
    DisableFlag(73100369)
    SkipLinesIfFlagRangeAnyEnabled(5, (1396, 1398))
    ForceAnimation(character_1, 90840, loop=True, skip_transition=True, unknown2=1.0)
    Event_13105743(
        0,
        character=3100731,
        flag=1396,
        flag_1=1397,
        flag_2=73100390,
        first_flag=1395,
        last_flag=1399,
        flag_3=73100370
    )
    Event_13105744(0, attacked_entity=3100731, flag=1396, flag_1=1397, flag_2=73100390, flag_3=73100370)
    DisableAI(character_1)
    SetCharacterTalkRange(character=character_1, distance=30.0)
    if FlagEnabled(1398):
        Move(character_1, destination=3102732, destination_type=CoordEntityType.Region, copy_draw_parent=3102732)
        WaitFrames(frames=1)
        DropMandatoryTreasure(character_1)
        GotoIfFlagEnabled(Label.L18, flag=1398)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1396, 1397))
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    Move(character_1, destination=3102729, destination_type=CoordEntityType.Region, copy_draw_parent=3102729)
    SkipLinesIfFlagRangeAnyEnabled(5, (1396, 1398))
    Event_13105743(
        0,
        character=3100731,
        flag=1396,
        flag_1=1397,
        flag_2=73100390,
        first_flag=1395,
        last_flag=1399,
        flag_3=73100370
    )
    Event_13105744(0, attacked_entity=3100731, flag=1396, flag_1=1397, flag_2=73100390, flag_3=73100370)
    AICommand(3100731, command_id=20, command_slot=1)
    ReplanAI(3100731)
    Event_13105745()
    if FlagEnabled(1398):
        WaitFrames(frames=1)
        DropMandatoryTreasure(character_1)
        GotoIfFlagEnabled(Label.L18, flag=1398)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1396, 1397))
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 17 --- #
    DefineLabel(17)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Move(character_1, destination=3102729, destination_type=CoordEntityType.Region, copy_draw_parent=3102729)
    End()


@RestartOnRest(13105741)
def Event_13105741(_, character: int, character_1: int):
    """Event 13105741"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102725))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102726))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(1380):
        return
    if FlagEnabled(1398):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(1396, 1397))
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1382, state=FlagSetting.On)
    EnableFlag(73100370)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    DisableAI(character_1)
    ForceAnimation(character_1, 90840, loop=True, skip_transition=True, unknown2=1.0)
    SetCharacterTalkRange(character=character_1, distance=30.0)
    Event_13105743(
        0,
        character=3100731,
        flag=1396,
        flag_1=1397,
        flag_2=73100390,
        first_flag=1395,
        last_flag=1399,
        flag_3=73100370
    )
    Event_13105744(0, 3100731, 1396, 1397, 73100390, 73100370)


@RestartOnRest(13105742)
def Event_13105742(_, character: int, character_1: int):
    """Event 13105742"""
    if FlagEnabled(13100500):
        return
    OR_1.Add(HasAIStatus(3100831, ai_status=AIStatusType.Battle))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3102727))
    
    MAIN.Await(OR_1)
    
    EndIfFlagRangeAllDisabled(flag_range=(1380, 1382))
    if FlagEnabled(1398):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(1396, 1397))
    GotoIfFlagEnabled(Label.L0, flag=1382)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1382, state=FlagSetting.On)
    EnableCharacter(character)
    EnableBackread(character)
    DisableCharacter(character_1)
    EnableBackread(character_1)
    Move(character, destination=3102728, destination_type=CoordEntityType.Region, copy_draw_parent=3102728)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)
    SetCharacterEventTarget(character, region=3100831)
    DisableFlag(73100370)
    SetCharacterTalkRange(character=character, distance=50.0)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(character, True)
    ForceAnimation(character, 90841, loop=True, skip_transition=True, unknown2=1.0)
    
    MAIN.Await(HealthEqual(3100831, value=0.0))
    
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(character, False)
    AICommand(3100731, command_id=20, command_slot=1)
    ReplanAI(3100731)
    SetTeamType(3100731, TeamType.FriendlyNPC)
    EnableFlag(73100370)
    Wait(4.0)
    Event_13105743(
        0,
        character=3100731,
        flag=1396,
        flag_1=1397,
        flag_2=73100390,
        first_flag=1395,
        last_flag=1399,
        flag_3=73100370
    )
    Event_13105744(0, attacked_entity=3100731, flag=1396, flag_1=1397, flag_2=73100390, flag_3=73100370)
    Event_13105745()


@RestartOnRest(13105743)
def Event_13105743(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    first_flag: int,
    last_flag: int,
    flag_3: int,
):
    """Event 13105743"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AND_2.Add(HealthGreaterThan(character, value=0.8999999761581421))
    SkipLinesIfConditionFalse(2, AND_2)
    AND_1.Add(HealthLessThan(character, value=0.699999988079071))
    Goto(Label.L20)
    AND_3.Add(HealthGreaterThan(character, value=0.699999988079071))
    SkipLinesIfConditionFalse(2, AND_3)
    AND_1.Add(HealthLessThan(character, value=0.6000000238418579))
    Goto(Label.L20)
    AND_4.Add(HealthGreaterThan(character, value=0.6000000238418579))
    SkipLinesIfConditionFalse(2, AND_4)
    AND_1.Add(HealthLessThan(character, value=0.5))
    Goto(Label.L20)
    AND_5.Add(HealthGreaterThan(character, value=0.5))
    SkipLinesIfConditionFalse(2, AND_5)
    AND_1.Add(HealthLessThan(character, value=0.4000000059604645))
    Goto(Label.L20)
    AND_6.Add(HealthGreaterThan(character, value=0.4000000059604645))
    SkipLinesIfConditionFalse(2, AND_6)
    AND_1.Add(HealthLessThan(character, value=0.30000001192092896))
    Goto(Label.L20)
    AND_7.Add(HealthGreaterThan(character, value=0.30000001192092896))
    SkipLinesIfConditionFalse(2, AND_7)
    AND_1.Add(HealthLessThan(character, value=0.20000000298023224))
    Goto(Label.L20)
    AND_8.Add(HealthGreaterThan(character, value=0.20000000298023224))
    SkipLinesIfConditionFalse(2, AND_8)
    AND_1.Add(HealthLessThan(character, value=0.10000000149011612))
    Goto(Label.L20)
    AND_9.Add(HealthGreaterThan(character, value=0.10000000149011612))
    SkipLinesIfConditionFalse(2, AND_9)
    AND_1.Add(HealthLessThan(character, value=0.5))
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag_2)
    AND_15.Add(FlagDisabled(flag))
    AND_15.Add(FlagDisabled(flag_1))
    AND_15.Add(HealthNotEqual(character, value=0.0))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag_2))
    AND_15.Add(OR_2)
    OR_1.Add(AND_15)
    OR_1.Add(FlagDisabled(flag_3))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableFlag(flag_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    AICommand(3100731, command_id=0, command_slot=1)
    SaveRequest()


@RestartOnRest(13105744)
def Event_13105744(_, attacked_entity: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 13105744"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    OR_15.Add(CharacterHuman(PLAYER))
    OR_15.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_15)
    
    MAIN.Await(AND_1)
    
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(FlagDisabled(flag_3))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        return
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_2.Add(FlagDisabled(flag_3))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        return
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_3.Add(FlagDisabled(flag_3))
    
    MAIN.Await(OR_3)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        return
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(13105745)
def Event_13105745():
    """Event 13105745"""
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(3100731, 150))
    OR_1.Add(FlagEnabled(1396))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1396):
        return
    EzstateAIRequest(3100731, command_id=2100, command_slot=1)
    OR_2.Add(FlagEnabled(1396))
    OR_2.Add(CharacterHasSpecialEffect(3100731, 150))
    OR_2.Add(TimeElapsed(seconds=0.5))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(1396):
        AICommand(3100731, command_id=0, command_slot=1)
        End()
    Restart()


@RestartOnRest(13105746)
def Event_13105746():
    """Event 13105746"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1396):
        return
    
    MAIN.Await(FlagEnabled(73100366))
    
    ForceAnimation(3100731, 90860, loop=True, skip_transition=True, unknown2=1.0)
    WaitFrames(frames=1)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(3100731, 152))
    
    DisableFlag(73100366)
    Restart()


@RestartOnRest(13105747)
def Event_13105747():
    """Event 13105747"""
    if PlayerNotInOwnWorld():
        return
    EnableFlag(73100374)
    AND_1.Add(FlagEnabled(13100500))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3100731, 153))
    
    MAIN.Await(AND_1)
    
    DisableFlag(73100374)
    AND_2.Add(FlagEnabled(13100500))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(3100731, 153))
    
    MAIN.Await(not AND_2)
    
    Restart()


@RestartOnRest(13105748)
def Event_13105748():
    """Event 13105748"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73100368)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3102730))
    
    EnableFlag(73100368)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3102730))
    
    Restart()
