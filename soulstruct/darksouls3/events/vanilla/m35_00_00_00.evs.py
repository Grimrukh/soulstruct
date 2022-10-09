"""
Cathedral of the Deep

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
    RegisterBonfire(bonfire_flag=13500000, obj=3501950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13500003, obj=3501953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13500002, obj=3501952, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13500800, bonfire_flag=13500001, character=3500951, obj=3501951)
    CommonFunc_20005211(0, character=3500900, animation_id=700, animation_id_1=1700, radius=1.0, seconds=20.0)
    CommonFunc_20005210(0, character=3500901, animation_id=700, animation_id_1=1700, radius=1.0)
    CommonFunc_20005119(
        0,
        character=3500681,
        region=3502270,
        region_1=3502273,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3500682,
        region=3502260,
        region_1=3502261,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005110(0, character=3500683, region=3502203)
    CommonFunc_20005132(0, character=3500175, radius=3.0, region=3502175)
    CommonFunc_20005132(0, character=3500176, radius=3.0, region=3502176)
    CommonFunc_20005342(0, flag=13500285, character=3500175)
    CommonFunc_20005342(0, flag=13500286, character=3500176)
    Event_13505271()
    CommonFunc_20005132(0, character=3500202, radius=3.0, region=3502290)
    CommonFunc_20005200(0, character=3500204, animation_id=706, animation_id_1=1706, region=3502243)
    CommonFunc_20005215(0, character=3500205, animation_id=710, animation_id_1=1710, radius=4.0, seconds=0.0)
    CommonFunc_20005215(0, character=3500206, animation_id=710, animation_id_1=1710, radius=4.0, seconds=1.0)
    CommonFunc_20005290(0, character=3500207, animation_id=703, animation_id_1=1703)
    CommonFunc_20005220(0, character=3500210, animation_id=706, animation_id_1=1706)
    CommonFunc_20005260(0, character=3500211, animation_id=700, animation_id_1=1700, character_1=3500291)
    CommonFunc_20005260(0, character=3500212, animation_id=701, animation_id_1=1701, character_1=3500291)
    CommonFunc_20005260(0, character=3500213, animation_id=702, animation_id_1=1702, character_1=3500291)
    CommonFunc_20005110(0, character=3500215, region=3502244)
    CommonFunc_20005290(0, character=3500216, animation_id=705, animation_id_1=1705)
    CommonFunc_20005220(0, character=3500220, animation_id=706, animation_id_1=1706)
    CommonFunc_20005290(0, character=3500221, animation_id=705, animation_id_1=1706)
    CommonFunc_20005205(0, character=3500231, animation_id=710, animation_id_1=1710, region=3502264, seconds=4.0)
    CommonFunc_20005200(0, character=3500232, animation_id=703, animation_id_1=1703, region=3502264)
    CommonFunc_20005220(0, character=3500233, animation_id=706, animation_id_1=1706)
    CommonFunc_20005120(0, character=3500234, radius=32.0)
    CommonFunc_20005120(0, character=3500235, radius=22.0)
    CommonFunc_20005120(0, character=3500236, radius=35.0)
    CommonFunc_20005231(0, character=3500248, animation_id=704, animation_id_1=1704, obj=3501242)
    CommonFunc_20005231(0, character=3500249, animation_id=704, animation_id_1=1704, obj=3501243)
    CommonFunc_20005231(0, character=3500250, animation_id=704, animation_id_1=1704, obj=3501244)
    CommonFunc_20005132(0, character=3500255, radius=3.0, region=3502290)
    CommonFunc_20005214(0, character=3500257, animation_id=710, animation_id_1=1710, radius=6.0)
    CommonFunc_20005215(0, character=3500258, animation_id=703, animation_id_1=1703, radius=5.0, seconds=3.0)
    Event_13505240(0, character=3500240, animation_id=701, animation_id_1=1701)
    Event_13505240(1, character=3500241, animation_id=701, animation_id_1=1701)
    Event_13505240(2, character=3500242, animation_id=701, animation_id_1=1701)
    Event_13505240(3, character=3500243, animation_id=701, animation_id_1=1701)
    Event_13505240(4, character=3500244, animation_id=701, animation_id_1=1701)
    Event_13505245(0, character=3500226, animation_id=701, animation_id_1=1701)
    Event_13505245(1, character=3500227, animation_id=701, animation_id_1=1701)
    Event_13505245(2, character=3500228, animation_id=701, animation_id_1=1701)
    Event_13505245(3, character=3500229, animation_id=701, animation_id_1=1701)
    Event_13505245(4, character=3500230, animation_id=701, animation_id_1=1701)
    Event_13505220(0, character=3500213, seconds=3.0)
    Event_13505220(1, character=3500220, seconds=5.0)
    Event_13505220(2, character=3500258, seconds=3.0)
    Event_13505220(3, character=3500204, seconds=5.0)
    Event_13505230(0, character=3500218)
    Event_13505230(1, character=3500219)
    Event_13505230(2, character=3500238)
    CommonFunc_20005132(0, character=3500260, radius=2.0, region=3502280)
    CommonFunc_20005132(0, character=3500262, radius=2.0, region=3502282)
    CommonFunc_20005132(0, character=3500310, radius=5.0, region=3502380)
    CommonFunc_20005231(0, character=3500311, animation_id=700, animation_id_1=1700, obj=3501245)
    CommonFunc_20005231(0, character=3500319, animation_id=700, animation_id_1=1700, obj=3501235)
    Event_13505260()
    Event_13505261()
    CommonFunc_20005110(0, character=3500321, region=3502390)
    CommonFunc_20005119(
        0,
        character=3500326,
        region=3502270,
        region_1=3502273,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005120(0, character=3500340, radius=1.0)
    CommonFunc_20005202(0, character=3500341, animation_id=700, animation_id_1=1700, region=3502341)
    CommonFunc_20005200(0, character=3500342, animation_id=700, animation_id_1=1700, region=3502342)
    CommonFunc_20005202(0, character=3500343, animation_id=700, animation_id_1=1700, region=3502343)
    CommonFunc_20005202(0, character=3500345, animation_id=700, animation_id_1=1700, region=3502345)
    CommonFunc_20005202(0, character=3500346, animation_id=700, animation_id_1=1700, region=3502346)
    CommonFunc_20005202(0, character=3500347, animation_id=700, animation_id_1=1700, region=3502347)
    CommonFunc_20005202(0, character=3500348, animation_id=700, animation_id_1=1700, region=3502348)
    CommonFunc_20005202(0, character=3500349, animation_id=700, animation_id_1=1700, region=3502349)
    CommonFunc_20005205(0, character=3500350, animation_id=700, animation_id_1=1700, region=3502350, seconds=2.0)
    Event_13505255(
        0,
        character=3500344,
        animation_id=700,
        animation_id_1=1700,
        region=3502344,
        flag=53500710,
        flag_1=53500630,
    )
    CommonFunc_20005290(0, character=3500401, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=3500402, animation_id=701, animation_id_1=1701)
    CommonFunc_20005110(0, character=3500403, region=3502202)
    CommonFunc_20005220(0, character=3500404, animation_id=700, animation_id_1=1700)
    CommonFunc_20005210(0, character=3500407, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005201(0, character=3500409, animation_id=702, animation_id_1=1702, region=3502209, seconds=1.0)
    CommonFunc_20005201(0, character=3500410, animation_id=702, animation_id_1=1702, region=3502209, seconds=2.0)
    CommonFunc_20005201(0, character=3500411, animation_id=702, animation_id_1=1702, region=3502209, seconds=1.5)
    CommonFunc_20005220(0, character=3500412, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=3500413, animation_id=700, animation_id_1=1700)
    CommonFunc_20005210(0, character=3500414, animation_id=700, animation_id_1=1700, radius=1.0)
    CommonFunc_20005110(0, character=3500415, region=3502211)
    CommonFunc_20005210(0, character=3500434, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005110(0, character=3500442, region=3502202)
    CommonFunc_20005290(0, character=3500443, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3500444, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500447, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500448, animation_id=700, animation_id_1=1700)
    CommonFunc_20005110(0, character=3500449, region=3502210)
    CommonFunc_20005201(0, character=3500450, animation_id=702, animation_id_1=1702, region=3502209, seconds=2.0)
    CommonFunc_20005201(0, character=3500451, animation_id=702, animation_id_1=1702, region=3502209, seconds=1.5)
    CommonFunc_20005201(0, character=3500492, animation_id=702, animation_id_1=1702, region=3502209, seconds=1.5)
    CommonFunc_20005220(0, character=3500461, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500472, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500471, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500472, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500473, animation_id=700, animation_id_1=1700)
    CommonFunc_20005213(0, character=3500474, animation_id=700, animation_id_1=1700, radius=1.0, region=3502212)
    CommonFunc_20005213(0, character=3500475, animation_id=702, animation_id_1=1702, radius=1.0, region=3502212)
    CommonFunc_20005150(0, character=3500476)
    CommonFunc_20005290(0, character=3500477, animation_id=701, animation_id_1=1701)
    CommonFunc_20005220(0, character=3500478, animation_id=700, animation_id_1=1700)
    CommonFunc_20005210(0, character=3500479, animation_id=700, animation_id_1=1700, radius=6.0)
    CommonFunc_20005290(0, character=3500480, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3500481, animation_id=701, animation_id_1=1701)
    CommonFunc_20005150(0, character=3500482)
    CommonFunc_20005290(0, character=3500484, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3500488, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3500499, animation_id=700, animation_id_1=1700)
    CommonFunc_20005201(
        0,
        character=3500440,
        animation_id=30004,
        animation_id_1=20004,
        region=3502200,
        seconds=1.2999999523162842,
    )
    CommonFunc_20005201(
        0,
        character=3500460,
        animation_id=30004,
        animation_id_1=20004,
        region=3502200,
        seconds=0.30000001192092896,
    )
    CommonFunc_20005201(
        0,
        character=3500424,
        animation_id=30004,
        animation_id_1=20004,
        region=3502200,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005201(
        0,
        character=3500441,
        animation_id=30004,
        animation_id_1=20004,
        region=3502200,
        seconds=2.200000047683716,
    )
    CommonFunc_20005201(
        0,
        character=3500487,
        animation_id=30004,
        animation_id_1=20004,
        region=3502200,
        seconds=1.100000023841858,
    )
    CommonFunc_20005201(0, character=3500427, animation_id=30004, animation_id_1=20004, region=3502200, seconds=3.0)
    CommonFunc_20005201(0, character=3500426, animation_id=30004, animation_id_1=20004, region=3502200, seconds=1.0)
    CommonFunc_20005201(0, character=3500452, animation_id=30004, animation_id_1=20004, region=3502209, seconds=1.0)
    CommonFunc_20005201(0, character=3500453, animation_id=30004, animation_id_1=20004, region=3502209, seconds=2.0)
    CommonFunc_20005201(0, character=3500454, animation_id=30004, animation_id_1=20004, region=3502209, seconds=3.0)
    CommonFunc_20005201(0, character=3500455, animation_id=30004, animation_id_1=20004, region=3502209, seconds=2.5)
    CommonFunc_20005201(0, character=3500456, animation_id=30004, animation_id_1=20004, region=3502209, seconds=1.5)
    CommonFunc_20005201(0, character=3500435, animation_id=30004, animation_id_1=20004, region=3502205, seconds=1.0)
    CommonFunc_20005201(
        0,
        character=3500436,
        animation_id=30004,
        animation_id_1=20004,
        region=3502205,
        seconds=1.399999976158142,
    )
    CommonFunc_20005201(
        0,
        character=3500437,
        animation_id=30004,
        animation_id_1=20004,
        region=3502205,
        seconds=1.7999999523162842,
    )
    CommonFunc_20005201(
        0,
        character=3500438,
        animation_id=30004,
        animation_id_1=20004,
        region=3502205,
        seconds=2.4000000953674316,
    )
    CommonFunc_20005201(0, character=3500439, animation_id=30004, animation_id_1=20004, region=3502205, seconds=3.0)
    CommonFunc_20005201(0, character=3500417, animation_id=30004, animation_id_1=20004, region=3502213, seconds=2.0)
    CommonFunc_20005201(0, character=3500418, animation_id=30004, animation_id_1=20004, region=3502213, seconds=2.0)
    CommonFunc_20005201(0, character=3500419, animation_id=30004, animation_id_1=20004, region=3502213, seconds=1.0)
    CommonFunc_20005201(0, character=3500420, animation_id=30004, animation_id_1=20004, region=3502213, seconds=1.0)
    CommonFunc_20005201(0, character=3500421, animation_id=30004, animation_id_1=20004, region=3502213, seconds=1.0)
    CommonFunc_20005120(0, character=3500280, radius=10.0)
    CommonFunc_20005120(0, character=3500281, radius=10.0)
    CommonFunc_20005120(0, character=3500282, radius=10.0)
    CommonFunc_20005120(0, character=3500283, radius=12.0)
    CommonFunc_20005120(0, character=3500284, radius=10.0)
    CommonFunc_20005110(0, character=3500291, region=3502291)
    CommonFunc_20005322(
        0,
        character=3500600,
        region=3502250,
        patrol_information_id=3504200,
        region_1=3502252,
        patrol_information_id_1=3504201,
    )
    CommonFunc_20005202(0, character=3500601, animation_id=700, animation_id_1=1700, region=3502369)
    CommonFunc_20005214(0, character=3500604, animation_id=701, animation_id_1=1701, radius=7.0)
    CommonFunc_20005202(0, character=3500607, animation_id=701, animation_id_1=1701, region=3502360)
    CommonFunc_20005213(0, character=3500608, animation_id=706, animation_id_1=20002, radius=2.0, region=3502360)
    CommonFunc_20005110(0, character=3500609, region=3502363)
    CommonFunc_20005261(0, character=3500612, animation_id=706, animation_id_1=20002, character_1=3500623)
    CommonFunc_20005261(0, character=3500613, animation_id=706, animation_id_1=20002, character_1=3500623)
    CommonFunc_20005207(
        0,
        character=3500616,
        animation_id=701,
        animation_id_1=1701,
        region=3502372,
        seconds=4.0,
        animation_id_2=1702,
        region_1=3502373,
        seconds_1=0.0,
    )
    CommonFunc_20005207(
        0,
        character=3500617,
        animation_id=701,
        animation_id_1=1701,
        region=3502374,
        seconds=3.0,
        animation_id_2=1702,
        region_1=3502375,
        seconds_1=3.0,
    )
    CommonFunc_20005120(0, character=3500618, radius=3.0)
    CommonFunc_20005205(0, character=3500620, animation_id=701, animation_id_1=1701, region=3502364, seconds=8.0)
    CommonFunc_20005214(0, character=3500622, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005134(0, character=3500623, animation_id=3006, radius=2.0, region=3502240)
    CommonFunc_20005205(0, character=3500627, animation_id=700, animation_id_1=1700, region=3502364, seconds=1.0)
    CommonFunc_20005202(0, character=3500633, animation_id=701, animation_id_1=1701, region=3502367)
    CommonFunc_20005214(0, character=3500636, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005202(0, character=3500637, animation_id=701, animation_id_1=1701, region=3502368)
    CommonFunc_20005207(
        0,
        character=3500638,
        animation_id=701,
        animation_id_1=1701,
        region=3502371,
        seconds=2.0,
        animation_id_2=1703,
        region_1=3502370,
        seconds_1=9.0,
    )
    CommonFunc_20005207(
        0,
        character=3500639,
        animation_id=701,
        animation_id_1=1701,
        region=3502371,
        seconds=4.0,
        animation_id_2=1706,
        region_1=3502370,
        seconds_1=7.0,
    )
    CommonFunc_20005205(0, character=3500640, animation_id=700, animation_id_1=1700, region=3502370, seconds=5.0)
    CommonFunc_20005207(
        0,
        character=3500641,
        animation_id=701,
        animation_id_1=1701,
        region=3502250,
        seconds=0.0,
        animation_id_2=1702,
        region_1=3502251,
        seconds_1=1.0,
    )
    CommonFunc_20005207(
        0,
        character=3500642,
        animation_id=701,
        animation_id_1=1701,
        region=3502250,
        seconds=3.0,
        animation_id_2=1705,
        region_1=3502252,
        seconds_1=1.0,
    )
    CommonFunc_20005210(0, character=3500370, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005341(0, flag=13500290, character=3500370, item_lot=31001000)
    CommonFunc_20005341(0, flag=13500292, character=3500372, item_lot=21503000)
    CommonFunc_20005341(0, flag=13500293, character=3500373, item_lot=21503010)
    Event_13500276(0, character=3500668, item_lot=21800110)
    CommonFunc_20005341(0, flag=13500295, character=3500669, item_lot=21800010)
    Event_13505275()
    CommonFunc_20005150(0, character=3500584)
    CommonFunc_20005150(0, character=3500585)
    CommonFunc_20005350(0, character=3500586, item_lot=52230310, flag=53500970)
    CommonFunc_20005110(0, character=3500589, region=3502257)
    Event_13505270(
        0,
        character=3500292,
        animation_id=700,
        animation_id_1=1700,
        region=3502293,
        seconds=5.0,
        region_1=3502294,
    )
    CommonFunc_20005432(0, character=3500292)
    CommonFunc_20005340(0, flag=13500299, character=3500292)
    CommonFunc_20005400(0, character=3500360)
    CommonFunc_20000343(0, flag=13500298, character=3500360, flag_1=53500980)
    CommonFunc_20005202(0, character=3500651, animation_id=700, animation_id_1=1700, region=3502295)
    CommonFunc_20005202(0, character=3500652, animation_id=700, animation_id_1=1700, region=3502295)
    CommonFunc_20005202(0, character=3500653, animation_id=700, animation_id_1=1700, region=3502295)
    CommonFunc_20005202(0, character=3500654, animation_id=700, animation_id_1=1700, region=3502295)
    CommonFunc_20005205(0, character=3500656, animation_id=700, animation_id_1=1700, region=3502297, seconds=3.0)
    CommonFunc_20005205(0, character=3500657, animation_id=700, animation_id_1=1700, region=3502297, seconds=3.0)
    CommonFunc_20005205(0, character=3500658, animation_id=701, animation_id_1=1701, region=3502297, seconds=0.0)
    CommonFunc_20005205(0, character=3500659, animation_id=700, animation_id_1=1700, region=3502297, seconds=5.0)
    CommonFunc_20005205(0, character=3500661, animation_id=700, animation_id_1=1700, region=3502297, seconds=10.0)
    CommonFunc_20005205(0, character=3500662, animation_id=700, animation_id_1=1700, region=3502297, seconds=10.0)
    CommonFunc_20005202(0, character=3500664, animation_id=700, animation_id_1=1700, region=3502298)
    CommonFunc_20005202(0, character=3500665, animation_id=700, animation_id_1=1700, region=3502298)
    CommonFunc_20005205(0, character=3500666, animation_id=700, animation_id_1=1700, region=3502297, seconds=4.0)
    CommonFunc_20005205(0, character=3500667, animation_id=700, animation_id_1=1700, region=3502297, seconds=10.0)
    CommonFunc_20005205(0, character=3500670, animation_id=701, animation_id_1=1701, region=3502299, seconds=0.0)
    Event_13505210(0, region=3502200, entity=3503400)
    Event_13505210(1, region=3502209, entity=3503408)
    Event_13505210(2, region=3502205, entity=3503411)
    Event_13505300(0, character=3500300)
    Event_13505300(1, character=3500301)
    CommonFunc_20005340(0, flag=13500300, character=3500300)
    CommonFunc_20005340(0, flag=13500301, character=3500301)
    Event_13505310()
    Event_13505311()
    Event_13505312()
    Event_13505320(0, flag=13500320, character=3500300, region=3502330, flag_1=13500405)
    Event_13505322(0, flag=13500320, character=3500300, destination=3502331)
    Event_13505324(0, character=3500300, animation_id=20001, animation_id_1=20002, animation_id_2=30000)
    CommonFunc_20005221(0, character=3500301, animation_id=30000, animation_id_1=20001, radius=26.0)
    Event_13505320(1, flag=13500321, character=3500301, region=3502332, flag_1=13500407)
    Event_13505322(1, flag=13500321, character=3500301, destination=3502333)
    Event_13505324(1, character=3500301, animation_id=20000, animation_id_1=20001, animation_id_2=30000)
    Event_13501800()
    Event_13505810()
    Event_13505899()
    Event_13505812(0, first_flag=13504810, last_flag=13504842)
    Event_13504899()
    Event_13505813()
    Event_13505814()
    Event_13505815()
    Event_13505816(0, character=3500814)
    Event_13505816(1, character=3500815)
    Event_13505816(2, character=3500816)
    Event_13505816(3, character=3500817)
    Event_13505820(0, first_flag=13504810, last_flag=13504842, first_flag_1=13504810, last_flag_1=13504842)
    Event_13505821(0, flag=13504810, flag_1=13504850, character=3500810, special_effect=11560)
    Event_13505821(1, flag=13504811, flag_1=13504851, character=3500811, special_effect=11560)
    Event_13505821(2, flag=13504812, flag_1=13504852, character=3500812, special_effect=11560)
    Event_13505821(3, flag=13504813, flag_1=13504853, character=3500813, special_effect=11560)
    Event_13505821(4, flag=13504814, flag_1=13504854, character=3500814, special_effect=11561)
    Event_13505821(5, flag=13504815, flag_1=13504855, character=3500815, special_effect=11561)
    Event_13505821(6, flag=13504816, flag_1=13504856, character=3500816, special_effect=11561)
    Event_13505821(7, flag=13504817, flag_1=13504857, character=3500817, special_effect=11561)
    Event_13505821(8, flag=13504818, flag_1=13504858, character=3500818, special_effect=11562)
    Event_13505821(9, flag=13504819, flag_1=13504859, character=3500819, special_effect=11562)
    Event_13505821(10, flag=13504820, flag_1=13504860, character=3500820, special_effect=11562)
    Event_13505821(11, flag=13504821, flag_1=13504861, character=3500821, special_effect=11562)
    Event_13505821(12, flag=13504822, flag_1=13504862, character=3500822, special_effect=11562)
    Event_13505821(13, flag=13504823, flag_1=13504863, character=3500823, special_effect=11562)
    Event_13505821(14, flag=13504824, flag_1=13504864, character=3500824, special_effect=11562)
    Event_13505821(15, flag=13504825, flag_1=13504865, character=3500825, special_effect=11562)
    Event_13505821(16, flag=13504826, flag_1=13504866, character=3500826, special_effect=11562)
    Event_13505821(17, flag=13504827, flag_1=13504867, character=3500827, special_effect=11562)
    Event_13505821(18, flag=13504828, flag_1=13504868, character=3500828, special_effect=11562)
    Event_13505821(19, flag=13504829, flag_1=13504869, character=3500829, special_effect=11562)
    Event_13505821(20, flag=13504830, flag_1=13504870, character=3500830, special_effect=11562)
    Event_13505821(21, flag=13504831, flag_1=13504871, character=3500831, special_effect=11562)
    Event_13505821(22, flag=13504832, flag_1=13504872, character=3500832, special_effect=11562)
    Event_13505821(23, flag=13504833, flag_1=13504873, character=3500833, special_effect=11562)
    Event_13505821(24, flag=13504834, flag_1=13504874, character=3500834, special_effect=11562)
    Event_13505821(25, flag=13504835, flag_1=13504875, character=3500835, special_effect=11562)
    Event_13505821(26, flag=13504836, flag_1=13504876, character=3500836, special_effect=11562)
    Event_13505821(27, flag=13504837, flag_1=13504877, character=3500837, special_effect=11562)
    Event_13505821(28, flag=13504838, flag_1=13504878, character=3500838, special_effect=11562)
    Event_13505821(29, flag=13504839, flag_1=13504879, character=3500839, special_effect=11562)
    Event_13505821(30, flag=13504840, flag_1=13504880, character=3500840, special_effect=11562)
    Event_13505821(31, flag=13504841, flag_1=13504881, character=3500841, special_effect=11562)
    Event_13505821(32, flag=13504842, flag_1=13504882, character=3500842, special_effect=11562)
    Event_13505861(0, flag=13504810, flag_1=13504850, attacked_entity=3500810)
    Event_13505861(1, flag=13504811, flag_1=13504851, attacked_entity=3500811)
    Event_13505861(2, flag=13504812, flag_1=13504852, attacked_entity=3500812)
    Event_13505861(3, flag=13504813, flag_1=13504853, attacked_entity=3500813)
    Event_13505861(4, flag=13504814, flag_1=13504854, attacked_entity=3500814)
    Event_13505861(5, flag=13504815, flag_1=13504855, attacked_entity=3500815)
    Event_13505861(6, flag=13504816, flag_1=13504856, attacked_entity=3500816)
    Event_13505861(7, flag=13504817, flag_1=13504857, attacked_entity=3500817)
    Event_13505861(8, flag=13504818, flag_1=13504858, attacked_entity=3500818)
    Event_13505861(9, flag=13504819, flag_1=13504859, attacked_entity=3500819)
    Event_13505861(10, flag=13504820, flag_1=13504860, attacked_entity=3500820)
    Event_13505861(11, flag=13504821, flag_1=13504861, attacked_entity=3500821)
    Event_13505861(12, flag=13504822, flag_1=13504862, attacked_entity=3500822)
    Event_13505861(13, flag=13504823, flag_1=13504863, attacked_entity=3500823)
    Event_13505861(14, flag=13504824, flag_1=13504864, attacked_entity=3500824)
    Event_13505861(15, flag=13504825, flag_1=13504865, attacked_entity=3500825)
    Event_13505861(16, flag=13504826, flag_1=13504866, attacked_entity=3500826)
    Event_13505861(17, flag=13504827, flag_1=13504867, attacked_entity=3500827)
    Event_13505861(18, flag=13504828, flag_1=13504868, attacked_entity=3500828)
    Event_13505861(19, flag=13504829, flag_1=13504869, attacked_entity=3500829)
    Event_13505861(20, flag=13504830, flag_1=13504870, attacked_entity=3500830)
    Event_13505861(21, flag=13504831, flag_1=13504871, attacked_entity=3500831)
    Event_13505861(22, flag=13504832, flag_1=13504872, attacked_entity=3500832)
    Event_13505861(23, flag=13504833, flag_1=13504873, attacked_entity=3500833)
    Event_13505861(24, flag=13504834, flag_1=13504874, attacked_entity=3500834)
    Event_13505861(25, flag=13504835, flag_1=13504875, attacked_entity=3500835)
    Event_13505861(26, flag=13504836, flag_1=13504876, attacked_entity=3500836)
    Event_13505861(27, flag=13504837, flag_1=13504877, attacked_entity=3500837)
    Event_13505861(28, flag=13504838, flag_1=13504878, attacked_entity=3500838)
    Event_13505861(29, flag=13504839, flag_1=13504879, attacked_entity=3500839)
    Event_13505861(30, flag=13504840, flag_1=13504880, attacked_entity=3500840)
    Event_13505861(31, flag=13504841, flag_1=13504881, attacked_entity=3500841)
    Event_13505861(32, flag=13504842, flag_1=13504882, attacked_entity=3500842)
    Event_13504900(0, character=3500810)
    Event_13504900(1, character=3500811)
    Event_13504900(2, character=3500812)
    Event_13504900(3, character=3500813)
    Event_13504900(4, character=3500814)
    Event_13504900(5, character=3500815)
    Event_13504900(6, character=3500816)
    Event_13504900(7, character=3500817)
    Event_13504900(8, character=3500818)
    Event_13504900(9, character=3500819)
    Event_13504900(10, character=3500820)
    Event_13504900(11, character=3500821)
    Event_13504900(12, character=3500822)
    Event_13504900(13, character=3500823)
    Event_13504900(14, character=3500824)
    Event_13504900(15, character=3500825)
    Event_13504900(16, character=3500826)
    Event_13504900(17, character=3500827)
    Event_13504900(18, character=3500828)
    Event_13504900(19, character=3500829)
    Event_13504900(20, character=3500830)
    Event_13504900(21, character=3500831)
    Event_13504900(22, character=3500832)
    Event_13504900(23, character=3500833)
    Event_13504900(24, character=3500834)
    Event_13504900(25, character=3500835)
    Event_13504900(26, character=3500836)
    Event_13504900(27, character=3500837)
    Event_13504900(28, character=3500838)
    Event_13504900(29, character=3500839)
    Event_13504900(30, character=3500840)
    Event_13504900(31, character=3500841)
    Event_13504900(32, character=3500842)
    Event_13504900(33, character=3500843)
    Event_13504900(34, character=3500844)
    Event_13504900(35, character=3500845)
    Event_13504900(36, character=3500846)
    Event_13504900(37, character=3500847)
    Event_13504900(38, character=3500848)
    Event_13504401(0, flag=13500405, flag_1=13501405, obj=3506400, flag_2=13505405)
    Event_13504401(1, flag=13500406, flag_1=13501406, obj=3506401, flag_2=13505406)
    Event_13504401(2, flag=13500407, flag_1=13501407, obj=3506402, flag_2=13505407)
    Event_13504400()
    CommonFunc_20005610(0, flag=13500460, region=3502460, region_1=3502461)
    CommonFunc_20005611(0, flag=13500460, obj_act_id=3503460, obj=3501460, obj_act_id_1=300310)
    CommonFunc_20005610(0, flag=13500462, region=3502462, region_1=3502463)
    CommonFunc_20005611(0, flag=13500462, obj_act_id=3503462, obj=3501462, obj_act_id_1=300310)
    CommonFunc_20005614(0, entity=3501480, flag=63500200)
    CommonFunc_20005614(0, entity=3501481, flag=63500201)
    CommonFunc_20005614(0, entity=3501482, flag=63500202)
    CommonFunc_20005614(0, entity=3501483, flag=63500210)
    CommonFunc_20005614(0, entity=3501487, flag=63500212)
    CommonFunc_20005614(0, entity=3501488, flag=63500213)
    Event_13505480()
    CommonFunc_20005640(0, flag=13500490, obj=3501490, start_climbing_flag=13500484, stop_climbing_flag=13500485)
    CommonFunc_20005523(0, obj=3501530, completion_count=1)
    CommonFunc_20005523(0, obj=3501531, completion_count=2)
    CommonFunc_20005524(0, obj=3501532, flag=9511)
    CommonFunc_20005524(0, obj=3501810, flag=13500800)
    CommonFunc_20005525(0, flag=53500850, item_lot=3500850, obj=3501540, model_point=61)
    CommonFunc_20005525(0, flag=53500860, item_lot=3500860, obj=3501541, model_point=60)
    CommonFunc_20005525(0, flag=53500870, item_lot=3500870, obj=3501542, model_point=60)
    CommonFunc_20005525(0, flag=53500880, item_lot=3500880, obj=3501543, model_point=61)
    CommonFunc_20005525(0, flag=53500890, item_lot=3500890, obj=3501544, model_point=61)
    CommonFunc_20005510(
        0,
        flag=13500500,
        obj=3501500,
        message=61350000,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13505500,
    )
    CommonFunc_20005510(
        0,
        flag=13500501,
        obj=3501501,
        message=61350010,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13505501,
    )
    CommonFunc_20005510(
        0,
        flag=13500502,
        obj=3501502,
        message=61350020,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13505502,
    )
    CommonFunc_20005780(0, obj=3501780, model_point=3)
    CommonFunc_20005780(0, obj=3501781, model_point=3)
    CommonFunc_20005780(0, obj=3501850, model_point=3)
    CommonFunc_20005670(0, area_id=35, block_id=0, vfx_id=3503100)
    CommonFunc_20005671(0, area_id=35, block_id=0, vfx_id=3503101)
    CommonFunc_20005672(0, area_id=35, block_id=0, vfx_id=3503102)
    CommonFunc_20005551(0, obj=3501300, animation_id=17, region=3502400, min_seconds=0.0, max_seconds=0.0, left=1)
    CommonFunc_20005551(0, obj=3501301, animation_id=15, region=3502400, min_seconds=1.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501302, animation_id=10, region=3502400, min_seconds=1.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501303, animation_id=13, region=3502400, min_seconds=1.0, max_seconds=2.5, left=1)
    CommonFunc_20005551(0, obj=3501304, animation_id=10, region=3502400, min_seconds=1.0, max_seconds=2.5, left=1)
    CommonFunc_20005551(0, obj=3501305, animation_id=10, region=3502401, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501306, animation_id=10, region=3502401, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501307, animation_id=10, region=3502401, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501308, animation_id=10, region=3502401, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501309, animation_id=10, region=3502402, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501310, animation_id=10, region=3502402, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501311, animation_id=10, region=3502402, min_seconds=0.0, max_seconds=2.0, left=1)
    CommonFunc_20005551(0, obj=3501312, animation_id=10, region=3502402, min_seconds=1.0, max_seconds=3.0, left=1)
    CommonFunc_20005551(0, obj=3501313, animation_id=10, region=3502402, min_seconds=1.0, max_seconds=3.0, left=1)
    Event_13505500(0, owner_entity=3500380, source_entity=3501380, radius=4.0, model_point=100, seconds=10.0)
    Event_13505500(1, owner_entity=3500381, source_entity=3501381, radius=6.0, model_point=100, seconds=10.0)
    Event_13505500(2, owner_entity=3500382, source_entity=3501382, radius=6.0, model_point=100, seconds=10.0)
    Event_13505500(3, owner_entity=3500383, source_entity=3501383, radius=6.0, model_point=100, seconds=10.0)
    Event_13505500(5, owner_entity=3500385, source_entity=3501385, radius=3.5, model_point=100, seconds=10.0)
    CommonFunc_20005624(0, flag=13500420, flag_1=13501420, entity=3501420, obj=3501421, obj_1=3501422, flag_2=13501421)
    CommonFunc_20005620(0, flag=13500425, flag_1=13501425, entity=3501425, obj=3501426, obj_1=3501427, flag_2=13501426)
    CommonFunc_20005622(0, flag=13500430, flag_1=13501430, entity=3501430, obj=3501431, obj_1=3501432, flag_2=13501431)
    CommonFunc_20005628(0, flag=13500431, obj=3501431, region=3502432)
    Event_13504411()
    DisableGravity(3500296)
    CommonFunc_20005490(
        0,
        owner_entity=3500296,
        character=3500396,
        entity=3501396,
        source_entity=3501396,
        model_point=10,
        behavior_id=5530,
        behavior_id_1=5531,
        behavior_id_2=5532,
        behavior_id_3=5533,
        behavior_id_4=5534,
        behavior_id_5=5535,
        behavior_id_6=5536,
        flag=13505702,
    )
    CommonFunc_20005491(0, character=3500296, character_1=3500396, region=3502396, flag=13505701)
    CommonFunc_20005492(0, anchor_entity=3502396)
    CommonFunc_20005493(0, character=3500296, character_1=3500396, flag=13500700)
    CommonFunc_20005494()
    CommonFunc_20005496(0, obj=3501396)
    Event_13500721(0, character=3500715, animation_id=90710)
    CommonFunc_20006002(0, character=3500715, flag=1158, first_flag=1155, last_flag=1159)
    CommonFunc_20006000(
        0,
        character=3500715,
        flag=1156,
        flag_1=1157,
        flag_2=73500230,
        value=0.6499999761581421,
        first_flag=1155,
        last_flag=1159,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=3500715, flag=1156, flag_1=1157, flag_2=73500230, right=3)
    Event_13505728()
    CommonFunc_20006030(
        0,
        obj=3501715,
        action_button_id=6190,
        right=2,
        item_lot=60920,
        first_flag=50006092,
        last_flag=50006092,
        flag=1152,
    )
    CommonFunc_20006002(0, character=3500700, flag=1358, first_flag=1355, last_flag=1359)
    Event_13505741(0, character=3500700)
    CommonFunc_20006002(0, character=3500701, flag=1358, first_flag=1355, last_flag=1359)
    Event_13505741(1, character=3500701)
    CommonFunc_20006002(0, character=3500720, flag=1378, first_flag=1375, last_flag=1379)
    CommonFunc_20006000(
        0,
        character=3500720,
        flag=1376,
        flag_1=1377,
        flag_2=73500290,
        value=0.6499999761581421,
        first_flag=1375,
        last_flag=1379,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=3500720, flag=1376, flag_1=1377, flag_2=73500290, right=3)
    CommonFunc_20006032(0, character=3500720, obj=3501720)
    CommonFunc_20006002(0, character=3500721, flag=1378, first_flag=1375, last_flag=1379)
    CommonFunc_20006000(
        0,
        character=3500721,
        flag=1376,
        flag_1=1377,
        flag_2=73500291,
        value=0.6499999761581421,
        first_flag=1375,
        last_flag=1379,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=3500721, flag=1376, flag_1=1377, flag_2=73500291, right=3)
    CommonFunc_20006032(0, character=3500721, obj=3501721)
    Event_13500781(0, character=3500720, character_1=3500721, character_2=3500722)
    Event_13500782(0, character=3500720, character_1=3500721, character_2=3500722)
    Event_13500783(0, flag=13500405, flag_1=13500406, flag_2=13500407)
    Event_13505784()
    Event_13505785()
    Event_13500761(0, anchor_entity=3500705)
    Event_13500786()
    Event_13505787()
    Event_13505788()
    Event_13505601(0, entity=3500850, flag=73500160)
    Event_13505602(0, entity=3500850, flag=73500161)
    Event_13505603(0, character=3500850, flag=73500162)
    Event_13505604(0, flag=73500164)
    CommonFunc_20006010(0, flag=73500162, animation_id=69003)
    CommonFunc_20006031(0, flag=73500155, region=3502700)
    CommonFunc_20006011(0, flag=73500163, vfx_id=652120)
    CommonFunc_20005900(0, flag=73500150, flag_1=9250)
    CommonFunc_20005701(
        0,
        left=13500800,
        summon_flag=13504190,
        dismissal_flag=13505190,
        character=3500190,
        region=3502190,
        left_1=70000019,
    )
    CommonFunc_20005720(0, flag=13504190, flag_1=13505190, flag_2=13500800, character=3500190)
    Event_13505370(0, flag=13504190, flag_1=13505805, character=3500190, region=3502800, region_1=3502805)
    CommonFunc_20005701(
        0,
        left=13500800,
        summon_flag=13504191,
        dismissal_flag=13505191,
        character=3500191,
        region=3502191,
        left_1=70000020,
    )
    CommonFunc_20005720(0, flag=13504191, flag_1=13505191, flag_2=13500800, character=3500191)
    Event_13505370(1, flag=13504191, flag_1=13505805, character=3500191, region=3502800, region_1=3502805)
    CommonFunc_20005701(
        0,
        left=13500800,
        summon_flag=13504192,
        dismissal_flag=13505192,
        character=3500192,
        region=3502192,
        left_1=70000021,
    )
    CommonFunc_20005720(0, flag=13504192, flag_1=13505192, flag_2=13500800, character=3500192)
    Event_13505370(2, flag=13504192, flag_1=13505805, character=3500192, region=3502800, region_1=3502805)
    CommonFunc_20005701(
        0,
        left=13500800,
        summon_flag=13504193,
        dismissal_flag=13505193,
        character=3500193,
        region=3502193,
        left_1=70000008,
    )
    CommonFunc_20005720(0, flag=13504193, flag_1=13505193, flag_2=13500800, character=3500193)
    Event_13505370(3, flag=13504193, flag_1=13505805, character=3500193, region=3502800, region_1=3502805)
    CommonFunc_20005750(
        0,
        flag=13500800,
        flag_1=13500194,
        summon_flag=13504194,
        dismissal_flag=13505194,
        character=3500194,
        region=3502194,
        region_1=3502195,
        seconds=2.0,
        left=0,
    )
    CommonFunc_20005721(0, flag=13504194, flag_1=13505194, flag_2=13500800, character=3500194)
    CommonFunc_20005760(0, flag=13500194, flag_1=13504194, flag_2=13505194, character=3500194)
    CommonFunc_20005341(0, flag=13500194, character=3500194, item_lot=58700)
    Event_13505100()
    CommonFunc_20006002(0, character=3500725, flag=1638, first_flag=1635, last_flag=1639)
    Event_13505751(0, character=3500725)
    Event_13505752(0, obj=3501725)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13505600(0, character=3500850, destination=3502852)
    Event_13505700(0, obj=3501396)
    CommonFunc_20005495(0, character=3500396, character_1=3500296, flag=13500700)
    Event_13505720(0, character=3500715, animation_id=90710)
    Event_13505740(0, character=3500700, character_1=3500701)
    Event_13505760(0, character=3500705)
    Event_13505780(0, character=3500720, character_1=3500721, character_2=3500722)
    DisableGravity(3500705)
    DisableCharacterCollision(3500705)
    DisableAnimations(3500705)
    Event_13500410()
    Event_13500400()
    DisableSoundEvent(sound_id=3504801)
    DisableSoundEvent(sound_id=3504802)
    Event_13505750(0, character=3500725, obj=3501725)


@ContinueOnRest(13505100)
def Event_13505100():
    """Event 13505100"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73500339)
    OR_15.Add(FailedToCreateSession())
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(73500339))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3500725, radius=10.0))
    AND_1.Add(not OR_15)
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishPhantoms(unknown=0)
    DisableFlag(73500339)
    OR_1.Add(FlagEnabled(1623))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    PlayCutscene(
        35000050,
        cutscene_flags=0,
        player_id=10000,
        move_to_region=4502100,
        game_map=PAINTED_WORLD_OF_ARIANDEL,
    )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    PlayCutscene(
        35000051,
        cutscene_flags=0,
        player_id=10000,
        move_to_region=4502100,
        game_map=PAINTED_WORLD_OF_ARIANDEL,
    )
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(73500304)
    SetRespawnPoint(respawn_point=4502100)
    EnableFlag(14500001)
    SaveRequest()
    Restart()


@RestartOnRest(13505210)
def Event_13505210(_, region: int, entity: int):
    """Event 13505210"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableSpawner(entity=entity)
    End()
    DisableSpawner(entity=entity)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=entity)


@RestartOnRest(13505220)
def Event_13505220(_, character: int, seconds: float):
    """Event 13505220"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    Wait(seconds)
    AICommand(character, command_id=-1, command_slot=0)


@RestartOnRest(13505230)
def Event_13505230(_, character: int):
    """Event 13505230"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    Wait(5.0)
    AICommand(character, command_id=-1, command_slot=0)


@RestartOnRest(13505240)
def Event_13505240(_, character: int, animation_id: int, animation_id_1: int):
    """Event 13505240"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    OR_2.Add(HasAIStatus(3500240, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(3500241, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(3500243, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(3500244, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    Wait(1.5)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5450):
        return
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13505245)
def Event_13505245(_, character: int, animation_id: int, animation_id_1: int):
    """Event 13505245"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    OR_2.Add(HasAIStatus(3500227, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(3500228, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(3500229, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(3500230, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    Wait(1.5)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5450):
        return
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13505255)
def Event_13505255(_, character: int, animation_id: int, animation_id_1: int, region: int, flag: int, flag_1: int):
    """Event 13505255"""
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
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(flag_1))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    EnableGravity(character)
    EnableCharacterCollision(character)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13505260)
def Event_13505260():
    """Event 13505260"""
    MAIN.Await(CharacterBackreadEnabled(3500313))
    
    WaitFrames(frames=1)
    AddSpecialEffect(3500313, 5021)


@RestartOnRest(13505261)
def Event_13505261():
    """Event 13505261"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=3500310, other_entity=PLAYER, radius=10.0))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3500310, 5405))
    
    MAIN.Await(AND_1)
    
    AICommand(3500310, command_id=10, command_slot=0)
    Wait(3.0)
    AICommand(3500310, command_id=10, command_slot=0)


@RestartOnRest(13505270)
def Event_13505270(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    region: int,
    seconds: float,
    region_1: int,
):
    """Event 13505270"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
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
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetNest(character, region=region_1)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    Wait(seconds)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()


@RestartOnRest(13505271)
def Event_13505271():
    """Event 13505271"""
    AddSpecialEffect(3500176, 5000)


@RestartOnRest(13505272)
def Event_13505272():
    """Event 13505272"""
    GotoIfFlagDisabled(Label.L0, flag=9250)
    DisableAI(3505650)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9250))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500650, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500651, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500652, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500653, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500654, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(9250):
        return RESTART
    EnableAI(3505650)


@RestartOnRest(13505273)
def Event_13505273():
    """Event 13505273"""
    GotoIfFlagDisabled(Label.L0, flag=9250)
    DisableAI(3505655)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9250))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500655, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500656, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500657, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500658, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500659, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500660, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500661, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500662, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500663, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500664, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500665, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500666, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3500667, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(9250):
        return RESTART
    EnableAI(3505655)


@RestartOnRest(13505275)
def Event_13505275():
    """Event 13505275"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableCharacter(3500669)
    DisableAnimations(3500669)
    DisableBackread(3500669)
    AND_1.Add(FlagEnabled(711))
    AND_1.Add(FlagDisabled(13500295))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(3500669)
    EnableAnimations(3500669)
    EnableBackread(3500669)


@RestartOnRest(13500276)
def Event_13500276(_, character: int, item_lot: int):
    """Event 13500276"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(6781))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    
    MAIN.Await(CharacterDead(character))
    
    if PlayerNotInOwnWorld():
        return
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(13505300)
def Event_13505300(_, character: int):
    """Event 13505300"""
    DisableNetworkSync()
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.EveryFiveFrames)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    OR_1.Add(CharacterBackreadDisabled(character))
    OR_1.Add(CharacterDead(character))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(13505310)
def Event_13505310():
    """Event 13505310"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagDisabled(13500320):
        ForceAnimation(3500300, 700, loop=True, unknown2=1.0)
    else:
        ForceAnimation(3500300, 30000, loop=True, unknown2=1.0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    GotoIfFlagEnabled(Label.L0, flag=13500320)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3502301))
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(EntityWithinDistance(entity=3500300, other_entity=PLAYER, radius=5.0))
    OR_2.Add(FlagDisabled(13500405))
    AND_1.Add(OR_2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=3500300))
    
    MAIN.Await(OR_3)
    
    RemoveSpecialEffect(3500300, 12341)
    WaitFrames(frames=1)
    ReplanAI(3500300)
    GotoIfFlagEnabled(Label.L2, flag=13500320)
    ForceAnimation(3500300, 1700, wait_for_completion=True, unknown2=1.0)
    End()
    ForceAnimation(3500300, 20002, wait_for_completion=True, unknown2=1.0)
    End()


@RestartOnRest(13505311)
def Event_13505311():
    """Event 13505311"""
    AddSpecialEffect(3500300, 5406)
    Wait(1.0)
    AND_1.Add(CharacterBackreadEnabled(3500300))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3500300, 5450))
    AND_1.Add(AllPlayersOutsideRegion(region=3502300))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AddSpecialEffect(3500300, 12341)
    RemoveSpecialEffect(3500300, 5406)
    Wait(1.0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3502300))
    
    Restart()


@ContinueOnRest(13505312)
def Event_13505312():
    """Event 13505312"""
    MAIN.Await(CharacterHasTAEEvent(3500300, tae_event_id=100))
    
    Move(3500300, destination=3502307, destination_type=CoordEntityType.Region, short_move=True)
    RemoveSpecialEffect(3500300, 12341)
    Restart()


@RestartOnRest(13505320)
def Event_13505320(_, flag: int, character: int, region: int, flag_1: int):
    """Event 13505320"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(CharacterOutsideRegion(character=character, region=region))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(13505322)
def Event_13505322(_, flag: int, character: int, destination: int):
    """Event 13505322"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    if ThisEventSlotFlagEnabled():
        return
    if FlagDisabled(flag):
        return
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=flag)


@ContinueOnRest(13505324)
def Event_13505324(_, character: int, animation_id: int, animation_id_1: int, animation_id_2: int):
    """Event 13505324"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 12340))
    AND_1.Add(CharacterHasSpecialEffect(character, 12342))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(character, animation_id_2, wait_for_completion=True, unknown2=1.0)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 12340))
    AND_1.Add(CharacterHasSpecialEffect(character, 12342))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(13505370)
def Event_13505370(_, flag: int, flag_1: int, character: int, region: int, region_1: int):
    """Event 13505370"""
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region_1))
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.5)
    RotateToFaceEntity(character, region, animation=60060, wait_for_completion=True)
    OR_2.Add(CharacterInsideRegion(character=character, region=region))
    OR_1.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_1)
    
    MAIN.Await(OR_2)
    
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ThisEventSlotFlagEnabled())
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(13500400)
def Event_13500400():
    """Event 13500400"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13500405)
    EnableFlag(13500406)
    EnableFlag(13500407)
    EnableFlag(13500400)


@RestartOnRest(13504400)
def Event_13504400():
    """Event 13504400"""
    Event_13505401(
        0,
        flag=13500405,
        flag_1=13501405,
        entity=3506400,
        obj=3501400,
        obj_1=3501410,
        obj_act_id=3503400,
        flag_2=13504405,
        flag_3=13505405,
        obj_act_id_1=350021,
    )
    Event_13505401(
        1,
        flag=13500406,
        flag_1=13501406,
        entity=3506401,
        obj=3501401,
        obj_1=3501411,
        obj_act_id=3503401,
        flag_2=13504406,
        flag_3=13505406,
        obj_act_id_1=350022,
    )
    Event_13505401(
        2,
        flag=13500407,
        flag_1=13501407,
        entity=3506402,
        obj=3501402,
        obj_1=3501412,
        obj_act_id=3503402,
        flag_2=13504407,
        flag_3=13505407,
        obj_act_id_1=350023,
    )


@RestartOnRest(13504401)
def Event_13504401(_, flag: int, flag_1: int, obj: int, flag_2: int):
    """Event 13504401"""
    MAIN.Await(FlagEnabled(13500400))
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(flag_2)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=20)
    DisableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=10)
    EnableFlag(flag_1)
    End()


@ContinueOnRest(13505401)
def Event_13505401(
    _,
    flag: int,
    flag_1: int,
    entity: int,
    obj: int,
    obj_1: int,
    obj_act_id: int,
    flag_2: int,
    flag_3: int,
    obj_act_id_1: int,
):
    """Event 13505401"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagEnabled(Label.L2, flag=flag)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_2.Add(FlagEnabled(flag))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    ForceAnimation(entity, 10, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    Wait(2.0)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    ForceAnimation(entity, 10, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.Off)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(ObjectBackreadEnabled(obj=obj))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.Off)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_2.Add(FlagDisabled(flag))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_3)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    ForceAnimation(entity, 20, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    Wait(2.0)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    ForceAnimation(entity, 20, wait_for_completion=True, skip_transition=True, unknown2=2.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.Off)

    # --- Label 4 --- #
    DefineLabel(4)
    AND_1.Add(ObjectBackreadEnabled(obj=obj))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.Off)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@ContinueOnRest(13500410)
def Event_13500410():
    """Event 13500410"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13500420)
    EnableFlag(13500430)
    EnableFlag(13500410)


@ContinueOnRest(13504411)
def Event_13504411():
    """Event 13504411"""
    CommonFunc_20005625(
        0,
        flag=13500420,
        flag_1=13501420,
        obj=3501420,
        obj_1=3501421,
        obj_act_id=3503421,
        obj_2=3501422,
        obj_act_id_1=3503422,
        region=3502421,
        region_1=3502422,
        flag_2=13501421,
        flag_3=13504420,
        left=0,
    )
    CommonFunc_20005621(
        0,
        flag=13500425,
        flag_1=13501425,
        obj=3501425,
        obj_1=3501426,
        obj_act_id=3503426,
        obj_2=3501427,
        obj_act_id_1=3503427,
        region=3502426,
        region_1=3502427,
        flag_2=13501426,
        flag_3=13504425,
        left=0,
    )
    CommonFunc_20005623(
        0,
        flag=13500430,
        flag_1=13501430,
        obj=3501430,
        obj_1=3501431,
        obj_act_id=3503431,
        obj_2=3501432,
        obj_act_id_1=3503432,
        region=3502431,
        region_1=3502432,
        flag_2=13501431,
        flag_3=13504430,
        left=13500431,
    )


@ContinueOnRest(13505480)
def Event_13505480():
    """Event 13505480"""
    RegisterLadder(start_climbing_flag=13500480, stop_climbing_flag=13500481, obj=3501200)
    RegisterLadder(start_climbing_flag=13500482, stop_climbing_flag=13500483, obj=3501201)


@ContinueOnRest(13500490)
def Event_13500490():
    """Event 13500490"""
    GotoIfFlagDisabled(Label.L0, flag=13500490)
    EndOfAnimation(obj=3501490, animation_id=2)
    RegisterLadder(start_climbing_flag=13500484, stop_climbing_flag=13500485, obj=3501490)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9200, entity=3501490))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 3501490, animation=60210)
    Wait(0.009999999776482582)
    ForceAnimation(3501490, 1, wait_for_completion=True, unknown2=1.0)
    RegisterLadder(start_climbing_flag=13500484, stop_climbing_flag=13500485, obj=3501490)
    EnableFlag(13500490)


@RestartOnRest(13505500)
def Event_13505500(_, owner_entity: int, source_entity: int, radius: float, model_point: int, seconds: float):
    """Event 13505500"""
    CreateProjectileOwner(entity=owner_entity)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=radius))
    
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5500,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5501,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5502,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5503,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5504,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5505,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=5506,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(seconds)
    Restart()


@RestartOnRest(13505510)
def Event_13505510(
    _,
    owner_entity: int,
    source_entity: int,
    radius: float,
    behavior_id: int,
    model_point: int,
    seconds: float,
):
    """Event 13505510"""
    CreateProjectileOwner(entity=owner_entity)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=radius))
    
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(seconds)
    Restart()


@ContinueOnRest(13501800)
def Event_13501800():
    """Event 13501800"""
    if FlagEnabled(13500800):
        return
    
    MAIN.Await(HealthRatio(3500800) <= 0.0)
    
    DeleteVFX(3503800)
    DeleteVFX(3503801)
    RemoveSpecialEffect(PLAYER, 11557)
    DisableSpawner(entity=3503830)
    DisableSpawner(entity=3503831)
    DisableSpawner(entity=3503832)
    DisableSpawner(entity=3503833)
    DisableSpawner(entity=3503834)
    DisableSpawner(entity=3503840)
    DisableSpawner(entity=3503841)
    DisableSpawner(entity=3503842)
    DisableSpawner(entity=3503843)
    DisableSpawner(entity=3503844)
    DisableSpawner(entity=3503845)
    DisableSpawner(entity=3503846)
    WaitFrames(frames=2)
    Kill(3505801)
    Kill(3505802)
    Wait(1.0)
    PlaySoundEffect(3800830, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3500800))
    
    KillBoss(game_area_param_id=3500800)
    EnableFlag(13500800)
    EnableFlag(9311)
    EnableFlag(6311)
    ResetOmissionModeCountsToDefault()


@RestartOnRest(13505810)
def Event_13505810():
    """Event 13505810"""
    ResetOmissionModeCountsToDefault()
    GotoIfFlagDisabled(Label.L0, flag=13500800)
    DisableSpawner(entity=3503830)
    DisableSpawner(entity=3503831)
    DisableSpawner(entity=3503832)
    DisableSpawner(entity=3503833)
    DisableSpawner(entity=3503834)
    DisableSpawner(entity=3503840)
    DisableSpawner(entity=3503841)
    DisableSpawner(entity=3503842)
    DisableSpawner(entity=3503843)
    DisableSpawner(entity=3503844)
    DisableSpawner(entity=3503845)
    DisableSpawner(entity=3503846)
    DisableCharacter(3505800)
    Kill(3505800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3505800)
    ForceAnimation(3505801, 700, unknown2=1.0)
    DisableCharacter(3505802)
    DisableAnimations(3505802)
    AND_1.Add(FlagEnabled(13505805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3502800))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=13500801)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13500801)
    SetOmissionModeCounts(level_1_count=15, level_2_count=30)
    EnableAI(3505801)
    SetCharacterEventTarget(3505801, entity=3500800)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3505803, authority_level=UpdateAuthority.Normal)
    ForceAnimation(3505801, 1700, unknown1=1, unknown2=1.0)
    EnableBossHealthBar(3500800, name=905220)
    SetNetworkConnectedFlagState(flag=13504827, state=FlagSetting.On)
    WaitFrames(frames=1)


@RestartOnRest(13505812)
def Event_13505812(_, first_flag: int, last_flag: int):
    """Event 13505812"""
    if FlagEnabled(13500800):
        return
    AND_1.Add(HealthRatio(3500800) <= 0.6499999761581421)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13505802)
    ForceAnimation(3500800, 20001, unknown2=1.0)
    Move(3500800, destination=3502810, destination_type=CoordEntityType.Region, copy_draw_parent=3500800)
    EnableAI(3500800)
    SetCharacterEventTarget(3500800, entity=3500800)
    CreateTemporaryVFX(vfx_id=652231, anchor_entity=3500800, model_point=220, anchor_type=CoordEntityType.Character)
    EnableCharacter(3505802)
    ForceAnimation(3505802, 20000, unknown2=4.0)
    EnableAI(3505802)
    EnableAnimations(3505802)
    SetCharacterEventTarget(3505802, entity=3500800)
    DisableSpawner(entity=3503830)
    DisableSpawner(entity=3503831)
    DisableSpawner(entity=3503832)
    DisableSpawner(entity=3503833)
    DisableSpawner(entity=3503834)
    EnableSpawner(entity=3503840)
    EnableSpawner(entity=3503841)
    EnableSpawner(entity=3503842)
    EnableSpawner(entity=3503843)
    EnableSpawner(entity=3503844)
    EnableSpawner(entity=3503845)


@RestartOnRest(13505813)
def Event_13505813():
    """Event 13505813"""
    if FlagEnabled(13500800):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterAlive(3500800))
    AND_1.Add(CharacterHasSpecialEffect(3500800, 11554))
    
    MAIN.Await(AND_1)
    
    CreateVFX(3503800)
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(3500800, 11554))
    OR_1.Add(CharacterHasSpecialEffect(3500800, 11555))
    OR_1.Add(CharacterHasSpecialEffect(3500800, 11556))
    AND_2.Add(CharacterDead(3500800))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(3500800, 11554)
    DeleteVFX(3503800)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    Restart()


@RestartOnRest(13505814)
def Event_13505814():
    """Event 13505814"""
    if FlagEnabled(13500800):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterAlive(3500800))
    AND_1.Add(CharacterHasSpecialEffect(3500800, 11555))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(3500800, 11554)
    DeleteVFX(3503800)
    CreateVFX(3503801)
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(3500800, 11555))
    OR_1.Add(CharacterHasSpecialEffect(3500800, 11556))
    AND_2.Add(CharacterDead(3500800))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(3500800, 11555)
    DeleteVFX(3503801)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    Restart()


@RestartOnRest(13505815)
def Event_13505815():
    """Event 13505815"""
    if FlagEnabled(13500800):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(3500800, 11556))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3502801))
    AND_1.Add(CharacterAlive(3500800))
    OR_1.Add(CharacterHasSpecialEffect(3500814, 11558))
    OR_1.Add(CharacterHasSpecialEffect(3500815, 11558))
    OR_1.Add(CharacterHasSpecialEffect(3500816, 11558))
    OR_1.Add(CharacterHasSpecialEffect(3500817, 11558))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 11557)
    OR_2.Add(CharacterDoesNotHaveSpecialEffect(3500800, 11556))
    OR_2.Add(CharacterOutsideRegion(character=PLAYER, region=3502801))
    AND_2.Add(CharacterDead(3500800))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(PLAYER, 11557)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    Restart()


@RestartOnRest(13505816)
def Event_13505816(_, character: int):
    """Event 13505816"""
    if FlagEnabled(13500800):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 11543))
    AND_1.Add(CharacterHasSpecialEffect(character, 11559))
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=3500800, special_effect=11556)
    AddSpecialEffect(3500800, 11538)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(3500800, 11537)

    # --- Label 1 --- #
    DefineLabel(1)
    RemoveSpecialEffect(3500800, 11556)
    RemoveSpecialEffect(3500800, 11555)
    RemoveSpecialEffect(3500800, 11554)
    Wait(3.0)
    Restart()


@RestartOnRest(13505820)
def Event_13505820(_, first_flag: int, last_flag: int, first_flag_1: uint, last_flag_1: uint):
    """Event 13505820"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13500800):
        return
    if FlagEnabled(13505802):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthRatio(3500800) > 0.6499999761581421)
    AND_1.Add(FlagEnabled(13505805))
    AND_1.Add(FlagEnabled(13505810))
    AND_1.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(first_flag_1, last_flag_1))
    Restart()


@RestartOnRest(13505821)
def Event_13505821(_, flag: int, flag_1: int, character: int, special_effect: int):
    """Event 13505821"""
    DisableNetworkSync()
    if FlagEnabled(13500800):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(13505802))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    AND_2.Add(HealthValue(character) > 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateTemporaryVFX(vfx_id=652231, anchor_entity=character, model_point=203, anchor_type=CoordEntityType.Character)
    Wait(2.0)
    AddSpecialEffect(character, 11521)
    OR_1.Add(HealthRatio(character) <= 0.0)
    OR_2.Add(TimeElapsed(seconds=25.0))
    OR_2.Add(FlagEnabled(flag_1))
    OR_2.Add(OR_1)
    
    MAIN.Await(OR_2)
    
    GotoIfFinishedConditionFalse(Label.L0, input_condition=OR_1)
    AddSpecialEffect(3500800, special_effect)
    AND_3.Add(HealthRatio(3500800) <= 0.6499999761581421)
    SkipLinesIfConditionTrue(2, AND_3)
    PlaySoundEffect(character, 522008010, sound_type=SoundType.c_CharacterMotion)
    SkipLines(1)
    PlaySoundEffect(character, 522008010, sound_type=SoundType.c_CharacterMotion)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.5)
    AND_4.Add(HealthRatio(3500800) <= 0.6499999761581421)
    SkipLinesIfConditionTrue(2, AND_4)
    CreateTemporaryVFX(vfx_id=652230, anchor_entity=character, model_point=203, anchor_type=CoordEntityType.Character)
    SkipLines(1)
    CreateTemporaryVFX(vfx_id=652232, anchor_entity=character, model_point=203, anchor_type=CoordEntityType.Character)
    RemoveSpecialEffect(character, 11521)
    Wait(2.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.Off)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(13505861)
def Event_13505861(_, flag: int, flag_1: int, attacked_entity: int):
    """Event 13505861"""
    if FlagEnabled(13500800):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    AND_1.Add(FlagDisabled(13505802))
    
    MAIN.Await(AND_1)
    
    Wait(0.5)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_1)
    
    MAIN.Await(OR_2)
    
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    Wait(1.0)
    Restart()


@RestartOnRest(13504899)
def Event_13504899():
    """Event 13504899"""
    if FlagEnabled(13500800):
        return
    
    MAIN.Await(FlagEnabled(13505805))
    
    SetCharacterEventTarget(3505801, entity=3500800)
    ActivateMultiplayerBuffs(3505801)
    if FlagEnabled(13505802):
        SetCharacterEventTarget(3505802, entity=3500800)
        ActivateMultiplayerBuffs(3505802)
    Wait(3.0)
    Restart()


@RestartOnRest(13505899)
def Event_13505899():
    """Event 13505899"""
    CommonFunc_20005800(
        0,
        flag=13500800,
        entity=3501800,
        region=3502800,
        flag_1=13505805,
        action_button_id=3501800,
        character=3505800,
        left=0,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=13500800,
        entity=3501800,
        region=3502800,
        flag_1=13505805,
        action_button_id=3501800,
        flag_2=13505806,
    )
    CommonFunc_20005820(0, flag=13500800, obj=3501800, model_point=2, left=0)
    CommonFunc_20005831(
        0,
        flag=13500800,
        flag_1=13505805,
        flag_2=13505806,
        region=3502800,
        sound_id=3504801,
        sound_id_1=3504802,
        flag_3=13505802,
    )
    CommonFunc_20005810(0, flag=13500800, entity=3501800, target_entity=3502800, action_button_id=10000)


@RestartOnRest(13504900)
def Event_13504900(_, character: int):
    """Event 13504900"""
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterInsideRegion(character=character, region=3502803))
    
    MAIN.Await(AND_1)
    
    Kill(character, award_souls=True)
    Wait(1.0)
    Restart()


@ContinueOnRest(13505600)
def Event_13505600(_, character: int, destination: int):
    """Event 13505600"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(1, (1515, 1519))
    EnableFlag(1515)
    AND_1.Add(FlagDisabled(1501))
    AND_1.Add(FlagEnabled(1518))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1515, 1519))
    SetNetworkConnectedFlagState(flag=1515, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(1, (1500, 1514))
    EnableFlag(1500)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableGravity(character)
    DisableCharacterCollision(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L0, flag=1500)
    GotoIfFlagEnabled(Label.L11, flag=1501)
    GotoIfFlagEnabled(Label.L0, flag=1502)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    GotoIfFlagEnabled(Label.L11, flag=1518)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(character, 30000, unknown2=1.0)
    End()


@ContinueOnRest(13505601)
def Event_13505601(_, entity: int, flag: int):
    """Event 13505601"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 20001, unknown2=1.0)
    DisableNetworkConnectedFlagRange(flag_range=(1515, 1519))
    SetNetworkConnectedFlagState(flag=1515, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1500, 1514))
    SetNetworkConnectedFlagState(flag=1502, state=FlagSetting.On)
    Wait(3.0)
    DisableFlag(flag)


@ContinueOnRest(13505602)
def Event_13505602(_, entity: int, flag: int):
    """Event 13505602"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagDisabled(1501))
    AND_1.Add(FlagDisabled(1518))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 20000, wait_for_completion=True, unknown2=1.0)
    
    MAIN.Await(FlagDisabled(flag))
    
    ForceAnimation(entity, 20002, unknown2=1.0)
    Restart()


@ContinueOnRest(13505603)
def Event_13505603(_, character: int, flag: int):
    """Event 13505603"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    OR_1.Add(FlagEnabled(1501))
    OR_1.Add(HealthRatio(character) == 0.0)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    ForceAnimation(character, 20003, wait_for_completion=True, unknown2=1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(6.0)
    Restart()


@ContinueOnRest(13505604)
def Event_13505604(_, flag: int):
    """Event 13505604"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(13505700)
def Event_13505700(_, obj: int):
    """Event 13505700"""
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

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000075)
    OR_1.Add(PlayerHasGood(462))
    OR_1.Add(PlayerHasGood(463))
    SkipLinesIfConditionTrue(3, OR_1)
    DisableFlag(50006250)
    SetNetworkConnectedFlagState(flag=13500700, state=FlagSetting.Off)
    SkipLines(2)
    EnableFlag(50006250)
    SetNetworkConnectedFlagState(flag=13500700, state=FlagSetting.On)

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


@ContinueOnRest(13505720)
def Event_13505720(_, character: int, animation_id: int):
    """Event 13505720"""
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
    AND_2.Add(FlagEnabled(1146))
    AND_2.Add(FlagEnabled(73500200))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1151, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000059)
    if FlagEnabled(1155):
        DisableFlag(73500220)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=1145)
    GotoIfFlagEnabled(Label.L6, flag=1146)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    AddSpecialEffect(character, 12400)
    DisableGravity(character)
    DisableCharacterCollision(character)
    EnableInvincibility(character)
    DisableAnimations(character)
    Move(character, destination=3502715, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L16, flag=1156)
    GotoIfFlagEnabled(Label.L18, flag=1158)
    ForceAnimation(character, animation_id, unknown2=1.0)
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


@RestartOnRest(13500721)
def Event_13500721(_, character: int, animation_id: int):
    """Event 13500721"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1145))
    AND_1.Add(FlagEnabled(1155))
    AND_1.Add(FlagEnabled(74000853))
    AND_1.Add(FlagEnabled(73500150))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=4,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1146, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=13500721, state=FlagSetting.On)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(character, destination=3502716, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(character, region=3502716)
    EnableGravity(character)
    EnableCharacterCollision(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SaveRequest()
    Wait(0.5)
    RemoveSpecialEffect(character, 12400)
    Wait(1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(13505728)
def Event_13505728():
    """Event 13505728"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1151))
    AND_1.Add(FlagEnabled(1500))
    OR_1.Add(FlagEnabled(13900002))
    OR_1.Add(FlagEnabled(9318))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(3500850) != 0.0)
    if not AND_1:
        return
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1152, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1155, 1159))
    SetNetworkConnectedFlagState(flag=1157, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1500, 1514))
    SetNetworkConnectedFlagState(flag=1501, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1515, 1519))
    SetNetworkConnectedFlagState(flag=1518, state=FlagSetting.On)
    ForceAnimation(3500850, 30000, unknown2=1.0)


@ContinueOnRest(13505740)
def Event_13505740(_, character: int, character_1: int):
    """Event 13505740"""
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
    AND_2.Add(FlagEnabled(1351))
    AND_2.Add(FlagEnabled(50006030))
    AND_2.Add(FlagDisabled(8263))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1352, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1357, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000069)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L12, flag=1352)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 12 --- #
    DefineLabel(12)
    GotoIfFlagEnabled(Label.L18, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAI(character)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAI(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
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


@ContinueOnRest(13505741)
def Event_13505741(_, character: int):
    """Event 13505741"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1352))
    AND_1.Add(FlagDisabled(1358))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=5.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    ReplanAI(character)


@ContinueOnRest(13505750)
def Event_13505750(_, character: int, obj: int):
    """Event 13505750"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1635, 1639))
    DisableNetworkConnectedFlagRange(flag_range=(1635, 1639))
    SetNetworkConnectedFlagState(flag=1635, state=FlagSetting.On)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1620, 1621)))
    AND_1.Add(FlagEnabled(1638))
    AND_1.Add(HealthRatio(character) > 0.0)
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1635, 1639))
    SetNetworkConnectedFlagState(flag=1635, state=FlagSetting.On)
    EnableFlag(73500305)
    AND_2.Add(FlagEnabled(1636))
    AND_2.Add(FlagEnabled(70001051))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1635, 1639))
    SetNetworkConnectedFlagState(flag=1635, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1620, 1634))
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1620, state=FlagSetting.On)
    if FlagDisabled(1623):
        GotoIfFlagDisabled(Label.L9, flag=1635)
    AND_3.Add(FlagEnabled(1620))
    AND_3.Add(FlagEnabled(73500300))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1621, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1621))
    AND_4.Add(FlagEnabled(73500304))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1622, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1621))
    AND_5.Add(FlagEnabled(6952))
    AND_5.Add(FlagEnabled(148))
    SkipLinesIfConditionFalse(4, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1623, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1635, 1639))
    SetNetworkConnectedFlagState(flag=1638, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1623))
    AND_6.Add(FlagEnabled(73500304))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1624, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001051)
    if FlagEnabled(1635):
        DisableFlag(73500320)
    OR_15.Add(FlagDisabled(73500302))
    OR_15.Add(FlagEnabled(73500305))
    SkipLinesIfConditionFalse(1, OR_15)
    DisableFlag(73500301)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L1, flag=1621)
    GotoIfFlagEnabled(Label.L3, flag=1623)
    GotoIfFlagEnabled(Label.L4, flag=1624)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)
    GotoIfFlagEnabled(Label.L18, flag=1638)
    ForceAnimation(character, 91060, unknown2=1.0)
    DisableGravity(character)
    DisableCharacterCollision(character)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(13505751)
def Event_13505751(_, character: int):
    """Event 13505751"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73500331)
    
    MAIN.Await(FlagEnabled(73500331))
    
    WaitFrames(frames=1)
    if CharacterHasSpecialEffect(character=character, special_effect=151):
        ForceAnimation(character, 91140, unknown2=1.0)
    Restart()


@ContinueOnRest(13505752)
def Event_13505752(_, obj: int):
    """Event 13505752"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(1623):
        return
    CreateObjectVFX(obj, vfx_id=200, model_point=735504)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=6600, entity=obj))
    
    DeleteObjectVFX(obj)
    EnableFlag(73500339)


@ContinueOnRest(13505760)
def Event_13505760(_, character: int):
    """Event 13505760"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1395, 1399))
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    AND_15.Add(FlagEnabled(1396))
    AND_15.Add(FlagEnabled(70000071))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1395, 1399))
    SetNetworkConnectedFlagState(flag=1395, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1380, 1394))
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1380, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1395)
    OR_1.Add(FlagEnabled(1380))
    OR_1.Add(FlagEnabled(1382))
    OR_1.Add(FlagEnabled(1394))
    AND_1.Add(OR_1)
    OR_2.Add(FlagEnabled(73100350))
    OR_2.Add(FlagEnabled(73100360))
    OR_2.Add(FlagEnabled(73100363))
    AND_1.Add(OR_2)
    AND_1.Add(FlagDisabled(1378))
    AND_1.Add(FlagEnabled(63500201))
    SkipLinesIfConditionFalse(8, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1383, state=FlagSetting.On)
    EnableFlag(70000403)
    DisableFlag(73501010)
    DisableFlag(73501020)
    DisableFlag(73501030)
    DisableFlag(73501040)
    DisableFlag(73501050)
    AND_2.Add(FlagEnabled(1383))
    AND_2.Add(FlagEnabled(73500102))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1385, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000071)
    if FlagEnabled(1395):
        DisableFlag(73500149)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1383)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, flag=1398)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1396, 1397))
    DisableGravity(character)
    DisableCharacterCollision(character)
    DisableAnimations(character)
    DisableCharacter(3500238)
    DisableBackread(3500238)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 17 --- #
    DefineLabel(17)
    SetTeamType(character, TeamType.HostileNPC)
    End()


@RestartOnRest(13500761)
def Event_13500761(_, anchor_entity: int):
    """Event 13500761"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13500761):
        return
    
    MAIN.Await(FlagEnabled(73500105))
    
    PlaySoundEffect(anchor_entity, 350100000, sound_type=SoundType.a_Ambient)


@ContinueOnRest(13505780)
def Event_13505780(_, character: int, character_1: int, character_2: int):
    """Event 13505780"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    if FlagEnabled(50006200):
        DisableFlag(73500267)
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
    AND_1.Add(FlagEnabled(1360))
    OR_1.Add(FlagEnabled(1380))
    OR_1.Add(FlagEnabled(1382))
    OR_1.Add(FlagEnabled(1394))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1395))
    OR_2.Add(FlagEnabled(73100350))
    OR_2.Add(FlagEnabled(73100360))
    OR_2.Add(FlagEnabled(73100363))
    AND_1.Add(OR_2)
    AND_1.Add(FlagEnabled(63500201))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1361, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1361))
    AND_2.Add(FlagEnabled(13500783))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1362, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1361))
    AND_3.Add(FlagEnabled(63500202))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1363, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000070)
    if FlagEnabled(1375):
        DisableFlag(73500299)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1361)
    GotoIfFlagEnabled(Label.L1, flag=1362)
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
    DisableCharacter(3505651)
    DisableBackread(3505651)
    if FlagEnabled(1378):
        DropMandatoryTreasure(character)
        GotoIfFlagEnabled(Label.L18, flag=1378)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1376, 1377))
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=13500406, state=FlagSetting.Off)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(3505651)
    DisableBackread(3505651)
    if FlagEnabled(1378):
        DropMandatoryTreasure(character_1)
        GotoIfFlagEnabled(Label.L18, flag=1378)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1376, 1377))
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    End()

    # --- Label 17 --- #
    DefineLabel(17)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()


@RestartOnRest(13500781)
def Event_13500781(_, character: int, character_1: int, character_2: int):
    """Event 13500781"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3502720))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3502721))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3502723))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1361))
    AND_1.Add(FlagEnabled(1375))
    AND_1.Add(FlagEnabled(13500783))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1362, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)


@RestartOnRest(13500782)
def Event_13500782(_, character: int, character_1: int, character_2: int):
    """Event 13500782"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3502721))
    AND_1.Add(FlagDisabled(13500783))
    OR_1.Add(FlagEnabled(1360))
    OR_1.Add(FlagEnabled(1361))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1375))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1363, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)


@RestartOnRest(13500783)
def Event_13500783(_, flag: int, flag_1: int, flag_2: int):
    """Event 13500783"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3502722))
    AND_1.Add(FlagEnabled(1361))
    AND_1.Add(FlagEnabled(1375))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionTrue(1, AND_2)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    if FlagDisabled(9017):
        PlayCutscene(35000000, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(35000001, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagDisabled(9017):
        PlayCutscene(
            35000000,
            cutscene_flags=0,
            player_id=10000,
            move_to_region=3502725,
            game_map=CATHEDRAL_OF_THE_DEEP,
        )
    else:
        PlayCutscene(
            35000001,
            cutscene_flags=0,
            player_id=10000,
            move_to_region=3502725,
            game_map=CATHEDRAL_OF_THE_DEEP,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableCharacter(3500720)
    DisableBackread(3500720)
    EnableCharacter(3500722)
    EnableBackread(3500722)
    SetCharacterTalkRange(character=3500722, distance=50.0)
    EnableFlag(73500271)
    DisableAnimations(3500722)
    Move(3500300, destination=3502335, destination_type=CoordEntityType.Region, copy_draw_parent=3500300)
    ForceAnimation(3500300, 0, loop=True, skip_transition=True, unknown2=1.0)
    SetNest(3500300, region=3502335)
    SetAIParamID(3500300, ai_param_id=302101)
    ReplanAI(3500300)
    AddSpecialEffect(3500300, 12345)
    AddSpecialEffect(3500300, 12346)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)


@RestartOnRest(13505784)
def Event_13505784():
    """Event 13505784"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(73500255)
    AND_1.Add(CharacterDead(3500300))
    AND_1.Add(CharacterDead(3500301))
    
    MAIN.Await(AND_1)
    
    EnableFlag(73500255)


@RestartOnRest(13505785)
def Event_13505785():
    """Event 13505785"""
    if PlayerInOwnWorld():
        return
    DisableFlag(13500785)
    AND_1.Add(FlagEnabled(1361))
    AND_1.Add(FlagEnabled(1375))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13500785)
    ClearMainCondition()
    AND_1.Add(FlagEnabled(1361))
    AND_1.Add(FlagEnabled(1375))
    
    MAIN.Await(not AND_1)
    
    Restart()


@RestartOnRest(13500786)
def Event_13500786():
    """Event 13500786"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(1360))
    AND_1.Add(FlagEnabled(1375))
    OR_1.Add(FlagEnabled(1380))
    OR_1.Add(FlagEnabled(1382))
    OR_1.Add(FlagEnabled(1394))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1395))
    OR_2.Add(FlagEnabled(73100350))
    OR_2.Add(FlagEnabled(73100360))
    OR_2.Add(FlagEnabled(73100363))
    AND_1.Add(OR_2)
    AND_1.Add(FlagEnabled(63500201))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableFlagRange((1360, 1374))
    EnableFlag(1361)
    SetNetworkConnectedFlagState(flag=13500406, state=FlagSetting.Off)
    DisableFlagRange((1380, 1394))
    EnableFlag(1383)
    EnableFlag(70000403)
    DisableFlag(73501010)
    DisableFlag(73501020)
    DisableFlag(73501030)
    DisableFlag(73501040)
    DisableFlag(73501050)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(3500720)
    EnableBackread(3500720)
    DisableCharacter(3505651)
    DisableBackread(3505651)
    EnableCharacter(3500705)
    EnableBackread(3500705)
    DisableGravity(3500705)
    DisableCharacterCollision(3500705)
    DisableAnimations(3500705)
    Kill(3500238)


@RestartOnRest(13505787)
def Event_13505787():
    """Event 13505787"""
    OR_1.Add(FlagEnabled(1361))
    OR_1.Add(FlagEnabled(1362))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1375))
    if not AND_1:
        return
    DisableCharacter(3505651)
    DisableBackread(3505651)


@RestartOnRest(13505788)
def Event_13505788():
    """Event 13505788"""
    if FlagDisabled(1383):
        return
    DisableGravity(3500705)
    DisableCharacterCollision(3500705)
    DisableAnimations(3500705)
    DisableCharacter(3500238)
    DisableBackread(3500238)


@RestartOnRest(13505900)
def Event_13505900():
    """Event 13505900"""
    Move(PLAYER, destination=3302900, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)


@RestartOnRest(13505910)
def Event_13505910():
    """Event 13505910"""
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=3500300, radius=10.0))
    
    DisplayDialog(text=10010170, number_buttons=NumberButtons.OneButton)
    Wait(3.0)
    Restart()


@ContinueOnRest(13505930)
def Event_13505930(_, flag: int, flag_1: int):
    """Event 13505930"""
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
