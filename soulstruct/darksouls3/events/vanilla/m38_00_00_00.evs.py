"""
Catacombs of Carthus / Smouldering Lake

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
    RegisterBonfire(bonfire_flag=13800001, obj=3801951, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13800002, obj=3801952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13800003, obj=3801953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13800006, obj=3801956, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13800800, bonfire_flag=13800000, character=3800950, obj=3801950)
    CommonFunc_20005500(0, flag=13800830, bonfire_flag=13800004, character=3800954, obj=3801954)
    CommonFunc_20005119(
        0,
        character=3805389,
        region=3802322,
        region_1=3802323,
        region_2=3802324,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3805384,
        region=3802320,
        region_1=3802321,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005110(0, character=3800300, region=3802201)
    CommonFunc_20005110(0, character=3800301, region=3802205)
    Event_13805240(0, character=3800302, character_1=3800305, patrol_information_id=3803240)
    Event_13805240(1, character=3800305, character_1=3800302, patrol_information_id=3803241)
    Event_13805245(0, character=3800311, patrol_information_id=3803250, patrol_information_id_1=3803251)
    Event_13805245(1, character=3800312, patrol_information_id=3803252, patrol_information_id_1=3803253)
    CommonFunc_20005120(0, character=3800320, radius=35.0)
    CommonFunc_20005110(0, character=3800321, region=3802230)
    CommonFunc_20005120(0, character=3800323, radius=3.5)
    CommonFunc_20005140(0, character=3800291, region=3802204, character_1=3800292)
    CommonFunc_20005140(0, character=3800292, region=3802204, character_1=3800291)
    CommonFunc_20005213(0, character=3800200, animation_id=700, animation_id_1=1700, radius=4.0, region=3802291)
    CommonFunc_20005213(0, character=3800201, animation_id=700, animation_id_1=1700, radius=3.0, region=3802291)
    CommonFunc_20005201(
        0,
        character=3800202,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.100000023841858,
    )
    CommonFunc_20005201(
        0,
        character=3800203,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.2999999523162842,
    )
    CommonFunc_20005201(0, character=3800204, animation_id=700, animation_id_1=1700, region=3802291, seconds=1.0)
    CommonFunc_20005201(0, character=3800205, animation_id=700, animation_id_1=1700, region=3802291, seconds=1.5)
    CommonFunc_20005201(0, character=3800206, animation_id=700, animation_id_1=1700, region=3802291, seconds=1.0)
    CommonFunc_20005201(
        0,
        character=3800207,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=2.200000047683716,
    )
    CommonFunc_20005201(
        0,
        character=3800208,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=2.200000047683716,
    )
    CommonFunc_20005201(
        0,
        character=3800209,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=0.6000000238418579,
    )
    CommonFunc_20005201(0, character=3800210, animation_id=700, animation_id_1=1700, region=3802291, seconds=0.5)
    CommonFunc_20005201(
        0,
        character=3800211,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.100000023841858,
    )
    CommonFunc_20005201(
        0,
        character=3800212,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.100000023841858,
    )
    CommonFunc_20005201(
        0,
        character=3800213,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005201(0, character=3800214, animation_id=700, animation_id_1=1700, region=3802291, seconds=1.5)
    CommonFunc_20005201(
        0,
        character=3800215,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.600000023841858,
    )
    CommonFunc_20005201(
        0,
        character=3800216,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=2.299999952316284,
    )
    CommonFunc_20005201(
        0,
        character=3800217,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=2.799999952316284,
    )
    CommonFunc_20005201(
        0,
        character=3800218,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.7000000476837158,
    )
    CommonFunc_20005201(
        0,
        character=3800219,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005201(
        0,
        character=3800220,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=3.200000047683716,
    )
    CommonFunc_20005201(
        0,
        character=3800221,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=3.799999952316284,
    )
    CommonFunc_20005201(
        0,
        character=3800222,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=3.5999999046325684,
    )
    CommonFunc_20005201(
        0,
        character=3800223,
        animation_id=700,
        animation_id_1=1700,
        region=3802291,
        seconds=3.5999999046325684,
    )
    CommonFunc_20005210(0, character=3800224, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=3800225, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005210(0, character=3800228, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=3800229, animation_id=700, animation_id_1=1700, radius=5.5)
    CommonFunc_20005220(0, character=3800240, animation_id=700, animation_id_1=1700)
    CommonFunc_20005222(0, character=3800241, animation_id=700, animation_id_1=1700, radius=8.0, seconds=2.0)
    CommonFunc_20005210(0, character=3800243, animation_id=700, animation_id_1=1700, radius=13.0)
    CommonFunc_20005201(
        0,
        character=3800245,
        animation_id=700,
        animation_id_1=1700,
        region=3802272,
        seconds=0.10000000149011612,
    )
    CommonFunc_20005201(0, character=3800246, animation_id=700, animation_id_1=1700, region=3802272, seconds=0.0)
    CommonFunc_20005200(0, character=3800248, animation_id=700, animation_id_1=1700, region=3802206)
    CommonFunc_20005201(0, character=3800249, animation_id=700, animation_id_1=1700, region=3802202, seconds=6.0)
    CommonFunc_20005210(0, character=3800254, animation_id=700, animation_id_1=1700, radius=6.0)
    CommonFunc_20005201(0, character=3800255, animation_id=700, animation_id_1=1700, region=3802281, seconds=0.0)
    CommonFunc_20005201(0, character=3800256, animation_id=700, animation_id_1=1700, region=3802281, seconds=1.0)
    CommonFunc_20005201(0, character=3800257, animation_id=700, animation_id_1=1700, region=3802281, seconds=2.0)
    CommonFunc_20005320(0, character=3800257, region=3802282, patrol_information_id=3803230)
    CommonFunc_20005200(0, character=3800258, animation_id=700, animation_id_1=1700, region=3802280)
    CommonFunc_20005201(0, character=3800259, animation_id=700, animation_id_1=1700, region=3802290, seconds=8.0)
    CommonFunc_20005210(0, character=3800261, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=3800262, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005132(0, character=3800263, radius=5.0, region=3802202)
    CommonFunc_20005132(0, character=3800264, radius=5.0, region=3802202)
    CommonFunc_20005134(0, character=3800265, animation_id=3026, radius=3.0, region=3802271)
    CommonFunc_20005132(0, character=3800266, radius=3.0, region=3802270)
    CommonFunc_20005132(0, character=3800267, radius=3.0, region=3802270)
    CommonFunc_20005190(0, character=3800269, radius=3.0)
    CommonFunc_20005211(0, character=3800271, animation_id=700, animation_id_1=1700, radius=4.0, seconds=1.0)
    CommonFunc_20005211(
        0,
        character=3800272,
        animation_id=700,
        animation_id_1=1700,
        radius=4.0,
        seconds=0.6000000238418579,
    )
    CommonFunc_20005211(
        0,
        character=3800273,
        animation_id=700,
        animation_id_1=1700,
        radius=4.0,
        seconds=2.4000000953674316,
    )
    CommonFunc_20005211(
        0,
        character=3800274,
        animation_id=700,
        animation_id_1=1700,
        radius=4.0,
        seconds=1.7999999523162842,
    )
    CommonFunc_20005211(0, character=3800275, animation_id=700, animation_id_1=1700, radius=1.0, seconds=1.5)
    CommonFunc_20005210(0, character=3800276, animation_id=700, animation_id_1=1700, radius=0.5)
    CommonFunc_20005210(0, character=3800277, animation_id=700, animation_id_1=1700, radius=0.5)
    CommonFunc_20005210(0, character=3800278, animation_id=700, animation_id_1=1700, radius=6.0)
    CommonFunc_20005210(0, character=3800279, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800280, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800281, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800282, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800283, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800284, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800285, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800286, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800287, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=3800288, animation_id=700, animation_id_1=1700, radius=8.0)
    Event_13805300(0, character=3800200, region=3802292)
    Event_13805300(1, character=3800201, region=3802292)
    Event_13805300(2, character=3800202, region=3802292)
    Event_13805300(3, character=3800203, region=3802292)
    Event_13805300(4, character=3800204, region=3802292)
    Event_13805300(5, character=3800205, region=3802292)
    Event_13805300(6, character=3800206, region=3802292)
    Event_13805300(7, character=3800207, region=3802292)
    Event_13805300(8, character=3800208, region=3802292)
    Event_13805300(9, character=3800209, region=3802292)
    Event_13805300(10, character=3800210, region=3802292)
    Event_13805300(11, character=3800211, region=3802292)
    Event_13805300(12, character=3800212, region=3802292)
    Event_13805300(13, character=3800213, region=3802292)
    Event_13805300(14, character=3800214, region=3802292)
    Event_13805300(15, character=3800215, region=3802292)
    Event_13805300(16, character=3800216, region=3802292)
    Event_13805300(17, character=3800217, region=3802292)
    Event_13805300(18, character=3800218, region=3802292)
    Event_13805300(19, character=3800219, region=3802292)
    Event_13805300(20, character=3800220, region=3802292)
    Event_13805300(21, character=3800221, region=3802292)
    Event_13805300(22, character=3800222, region=3802292)
    Event_13805300(23, character=3800223, region=3802292)
    Event_13805300(24, character=3800224, region=3802292)
    Event_13805300(25, character=3800225, region=3802292)
    Event_13805300(26, character=3800226, region=3802292)
    Event_13805300(27, character=3800227, region=3802292)
    Event_13805300(28, character=3800228, region=3802292)
    Event_13805280()
    Event_13805270(0, character=3800260, region=3802262, region_1=3802263)
    Event_13805272(
        0,
        character=3800270,
        region=3802266,
        region_1=3802260,
        region_2=3802264,
        region_3=3802261,
        region_4=3802265,
    )
    CommonFunc_20005224(0, character=3800350, animation_id=701, animation_id_1=1701)
    CommonFunc_20005223(0, character=3800351, animation_id=701, animation_id_1=1701, seconds=1.0)
    CommonFunc_20005221(0, character=3800360, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005220(0, character=3800364, animation_id=701, animation_id_1=1701)
    CommonFunc_20005223(0, character=3800365, animation_id=701, animation_id_1=1701, seconds=2.0)
    CommonFunc_20005110(0, character=3800366, region=3802360)
    CommonFunc_20005220(0, character=3800367, animation_id=701, animation_id_1=1701)
    Event_13805370()
    Event_13805340(0, character=3800352, animation_id=701, animation_id_1=1701, radius=5.0, region=3802330, seconds=1.0)
    Event_13805340(1, character=3800353, animation_id=701, animation_id_1=1701, radius=5.0, region=3802330, seconds=0.0)
    CommonFunc_20005120(0, character=3800392, radius=3.0)
    CommonFunc_20005110(0, character=3800395, region=3802360)
    CommonFunc_20005202(0, character=3800400, animation_id=700, animation_id_1=1700, region=3802300)
    CommonFunc_20005202(0, character=3800401, animation_id=700, animation_id_1=1700, region=3802301)
    CommonFunc_20005202(0, character=3800402, animation_id=700, animation_id_1=1700, region=3802302)
    CommonFunc_20005202(0, character=3800403, animation_id=700, animation_id_1=1700, region=3802303)
    CommonFunc_20005202(0, character=3800404, animation_id=700, animation_id_1=1700, region=3802304)
    CommonFunc_20005202(0, character=3800405, animation_id=700, animation_id_1=1700, region=3802305)
    CommonFunc_20005202(0, character=3800406, animation_id=700, animation_id_1=1700, region=3802306)
    CommonFunc_20005202(0, character=3800407, animation_id=700, animation_id_1=1700, region=3802307)
    CommonFunc_20005202(0, character=3800408, animation_id=700, animation_id_1=1700, region=3802308)
    CommonFunc_20005202(0, character=3800409, animation_id=700, animation_id_1=1700, region=3802309)
    CommonFunc_20005202(0, character=3800410, animation_id=700, animation_id_1=1700, region=3802310)
    CommonFunc_20005202(0, character=3800411, animation_id=700, animation_id_1=1700, region=3802311)
    CommonFunc_20005202(0, character=3800412, animation_id=700, animation_id_1=1700, region=3802312)
    CommonFunc_20005202(0, character=3800420, animation_id=700, animation_id_1=1700, region=3802340)
    CommonFunc_20005202(0, character=3800421, animation_id=700, animation_id_1=1700, region=3802341)
    CommonFunc_20005202(0, character=3800422, animation_id=700, animation_id_1=1700, region=3802342)
    CommonFunc_20005202(0, character=3800423, animation_id=700, animation_id_1=1700, region=3802343)
    CommonFunc_20005202(0, character=3800424, animation_id=700, animation_id_1=1700, region=3802344)
    CommonFunc_20005202(0, character=3800425, animation_id=700, animation_id_1=1700, region=3802345)
    CommonFunc_20005202(0, character=3800426, animation_id=700, animation_id_1=1700, region=3802346)
    CommonFunc_20005202(0, character=3800432, animation_id=700, animation_id_1=1700, region=3802348)
    CommonFunc_20005120(0, character=3800433, radius=3.0)
    CommonFunc_20005120(0, character=3800434, radius=3.0)
    Event_13805350(0, character=3800427)
    Event_13805350(1, character=3800428)
    Event_13805350(2, character=3800429)
    Event_13805350(3, character=3800430)
    Event_13805350(4, character=3800431)
    Event_13805371()
    CommonFunc_20005111(0, character=3800499, animation_id=3000, region=3802390)
    Event_13805360()
    CommonFunc_20005132(0, character=3800530, radius=2.0, region=3802356)
    CommonFunc_20005120(0, character=3800531, radius=5.5)
    CommonFunc_20005132(0, character=3800532, radius=2.0, region=3802357)
    CommonFunc_20005132(0, character=3800340, radius=5.0, region=3802365)
    CommonFunc_20005440(0, character=3800340, character_1=3800600, tae_event_id=10)
    CommonFunc_20005440(0, character=3800340, character_1=3800601, tae_event_id=20)
    CommonFunc_20005440(0, character=3800340, character_1=3800602, tae_event_id=30)
    CommonFunc_20005440(0, character=3800342, character_1=3800606, tae_event_id=10)
    CommonFunc_20005440(0, character=3800342, character_1=3800607, tae_event_id=20)
    CommonFunc_20005440(0, character=3800342, character_1=3800608, tae_event_id=30)
    CommonFunc_20005440(0, character=3800343, character_1=3800609, tae_event_id=10)
    CommonFunc_20005440(0, character=3800343, character_1=3800610, tae_event_id=20)
    CommonFunc_20005440(0, character=3800343, character_1=3800611, tae_event_id=30)
    CommonFunc_20005440(0, character=3800344, character_1=3800612, tae_event_id=10)
    CommonFunc_20005440(0, character=3800344, character_1=3800613, tae_event_id=20)
    CommonFunc_20005440(0, character=3800344, character_1=3800614, tae_event_id=30)
    CommonFunc_20005441(0, character=3800340, character_1=3805600)
    CommonFunc_20005441(0, character=3800342, character_1=3805606)
    CommonFunc_20005441(0, character=3800343, character_1=3805609)
    CommonFunc_20005441(0, character=3800344, character_1=3805612)
    Event_13805366(0, character=3800342, character_1=3805627)
    Event_13805366(1, character=3800344, character_1=3805629)
    Event_13805366(2, character=3800343, character_1=3805631)
    CommonFunc_20005341(0, flag=13800380, character=3800500, item_lot=30601000)
    Event_13805361()
    CommonFunc_20005341(0, flag=13800381, character=3800499, item_lot=22000000)
    CommonFunc_20005400(0, character=3800550)
    CommonFunc_20000343(0, flag=13800390, character=3800550, flag_1=53800940)
    CommonFunc_20005341(0, flag=13800392, character=3800552, item_lot=21506020)
    CommonFunc_20005341(0, flag=13800393, character=3800553, item_lot=21506030)
    CommonFunc_20005341(0, flag=13800394, character=3800554, item_lot=21506040)
    CommonFunc_20005341(0, flag=13800395, character=3800555, item_lot=21506000)
    CommonFunc_20005341(0, flag=13800396, character=3800556, item_lot=21506010)
    Event_13805809()
    Event_13800800()
    Event_13805810()
    Event_13805811()
    Event_13805829()
    Event_13805824()
    Event_13805812()
    Event_13805813(
        0,
        npc_part_id=40,
        value=0,
        npc_part_id_1=50,
        value_1=0,
        flag=13805812,
        special_effect=12251,
        animation_id=20001,
        animation_id_1=20002,
        animation_id_2=20003,
    )
    Event_13805813(
        1,
        npc_part_id=20,
        value=0,
        npc_part_id_1=30,
        value_1=0,
        flag=13805812,
        special_effect=12253,
        animation_id=20004,
        animation_id_1=20005,
        animation_id_2=20006,
    )
    Event_13805813(
        2,
        npc_part_id=21,
        value=0,
        npc_part_id_1=31,
        value_1=0,
        flag=13804814,
        special_effect=12255,
        animation_id=20007,
        animation_id_1=20008,
        animation_id_2=20009,
    )
    Event_13804814(0, npc_part_id=21, part_health=634, npc_part_id_1=31, part_health_1=282, flag=13805814)
    Event_13805820()
    Event_13804815(0, character=3800810, region=3802820, dummy_id=40)
    Event_13804815(1, character=3800811, region=3802820, dummy_id=41)
    Event_13804815(2, character=3800812, region=3802820, dummy_id=42)
    Event_13804815(3, character=3800813, region=3802820, dummy_id=43)
    Event_13804815(4, character=3800814, region=3802820, dummy_id=44)
    Event_13804815(5, character=3800815, region=3802820, dummy_id=45)
    Event_13804815(6, character=3800820, region=3802820, dummy_id=44)
    Event_13804815(7, character=3800821, region=3802820, dummy_id=45)
    Event_13804815(8, character=3800822, region=3802820, dummy_id=46)
    Event_13804815(9, character=3800823, region=3802820, dummy_id=47)
    Event_13804815(10, character=3800824, region=3802820, dummy_id=48)
    Event_13804815(11, character=3800825, region=3802820, dummy_id=49)
    CommonFunc_20005840(0, other_entity=3801800)
    CommonFunc_20005841(0, other_entity=3801800)
    Event_13805840()
    Event_13800830()
    Event_13805841()
    Event_13805842()
    Event_13805843()
    Event_13805844()
    Event_13805859()
    CommonFunc_20005840(0, other_entity=3801830)
    CommonFunc_20005841(0, other_entity=3801830)
    Event_13800899()
    Event_13805400()
    Event_13805402()
    Event_13805520()
    Event_13800548(0, obj=3801548)
    Event_13805201()
    Event_13805202()
    Event_13805206()
    Event_13805207(0, vibration_id=103, anchor_entity=3802380)
    DisableObject(3801219)
    DisableObject(3801216)
    DisableObject(3801215)
    DisableObject(3801218)
    DisableObject(3801210)
    Event_13805430(
        0,
        owner_entity=3800562,
        entity=3801214,
        region=3802410,
        source_entity=3802411,
        source_entity_1=3802412,
        source_entity_2=3802413,
    )
    Event_13805440(
        0,
        owner_entity=3800560,
        entity=3801210,
        entity_1=3801211,
        region=3802400,
        region_1=3802401,
        source_entity=3802402,
        source_entity_1=3802403,
        source_entity_2=3802404,
    )
    Event_13805440(
        1,
        owner_entity=3800561,
        entity=3801212,
        entity_1=3801213,
        region=3802405,
        region_1=3802406,
        source_entity=3802407,
        source_entity_1=3802408,
        source_entity_2=3802409,
    )
    Event_13805450()
    Event_13805552()
    Event_13805556()
    Event_13804550()
    Event_13805560(0, obj=3801300, source_entity=3801330, owner_entity=3800570)
    Event_13805560(1, obj=3801301, source_entity=3801331, owner_entity=3800570)
    Event_13805560(2, obj=3801302, source_entity=3801332, owner_entity=3800570)
    Event_13805560(3, obj=3801303, source_entity=3801333, owner_entity=3800570)
    Event_13805560(4, obj=3801304, source_entity=3801334, owner_entity=3800571)
    Event_13805560(5, obj=3801305, source_entity=3801335, owner_entity=3800571)
    Event_13805560(6, obj=3801306, source_entity=3801336, owner_entity=3800571)
    Event_13805560(7, obj=3801307, source_entity=3801337, owner_entity=3800571)
    Event_13805560(8, obj=3801308, source_entity=3801338, owner_entity=3800571)
    Event_13805560(9, obj=3801309, source_entity=3801339, owner_entity=3800572)
    Event_13805560(10, obj=3801310, source_entity=3801340, owner_entity=3800572)
    Event_13805560(11, obj=3801311, source_entity=3801341, owner_entity=3800572)
    Event_13805560(12, obj=3801312, source_entity=3801342, owner_entity=3800572)
    Event_13805560(13, obj=3801313, source_entity=3801343, owner_entity=3800573)
    Event_13805560(14, obj=3801314, source_entity=3801344, owner_entity=3800573)
    Event_13805560(15, obj=3801315, source_entity=3801345, owner_entity=3800573)
    Event_13805560(16, obj=3801316, source_entity=3801346, owner_entity=3800573)
    Event_13805560(17, obj=3801317, source_entity=3801347, owner_entity=3800573)
    Event_13805560(18, obj=3801318, source_entity=3801348, owner_entity=3800574)
    Event_13805560(19, obj=3801319, source_entity=3801349, owner_entity=3800574)
    Event_13805560(20, obj=3801320, source_entity=3801350, owner_entity=3800575)
    Event_13805560(21, obj=3801321, source_entity=3801351, owner_entity=3800575)
    Event_13805560(22, obj=3801322, source_entity=3801352, owner_entity=3800575)
    Event_13805560(23, obj=3801323, source_entity=3801353, owner_entity=3800575)
    Event_13805560(24, obj=3801324, source_entity=3801354, owner_entity=3800575)
    Event_13805560(25, obj=3801325, source_entity=3801355, owner_entity=3800575)
    Event_13805540()
    Event_13800500()
    CommonFunc_20005650(0, flag=13800530, obj=3801530)
    CommonFunc_20005650(0, flag=13800531, obj=3801531)
    CommonFunc_20005650(0, flag=13800532, obj=3801532)
    CommonFunc_20005650(0, flag=13800533, obj=3801533)
    CommonFunc_20005650(0, flag=13800534, obj=3801534)
    CommonFunc_20005650(0, flag=13800535, obj=3801535)
    CommonFunc_20005650(0, flag=13800536, obj=3801536)
    CommonFunc_20005780(0, obj=3801974, dummy_id=2)
    Event_13805570()
    CommonFunc_20005510(
        0,
        flag=13800550,
        obj=3801550,
        message=61380000,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13805750,
    )
    CommonFunc_20005510(
        0,
        flag=13800551,
        obj=3801551,
        message=61380010,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13805751,
    )
    CommonFunc_20005510(
        0,
        flag=13800552,
        obj=3801552,
        message=61380020,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13805752,
    )
    CommonFunc_20005510(
        0,
        flag=13800553,
        obj=3801553,
        message=61380030,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13805753,
    )
    CommonFunc_20005510(
        0,
        flag=13800554,
        obj=3801554,
        message=61380040,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13805754,
    )
    CommonFunc_20005520(0, flag=13800580, obj=3801580, obj_act_id=3804580)
    CommonFunc_20005520(0, flag=13800581, obj=3801581, obj_act_id=3804581)
    CommonFunc_20005520(0, flag=13800583, obj=3801583, obj_act_id=3804583)
    CommonFunc_20005520(0, flag=13800584, obj=3801584, obj_act_id=3804584)
    CommonFunc_20005520(0, flag=13800585, obj=3801585, obj_act_id=3804585)
    CommonFunc_20005520(0, flag=13800586, obj=3801586, obj_act_id=3804586)
    CommonFunc_20005520(0, flag=13800587, obj=3801587, obj_act_id=3804587)
    CommonFunc_20005520(0, flag=13800588, obj=3801588, obj_act_id=3804588)
    CommonFunc_20005520(0, flag=13800589, obj=3801589, obj_act_id=3804589)
    CommonFunc_20005520(0, flag=13800590, obj=3801590, obj_act_id=3804590)
    CommonFunc_20005520(0, flag=13800591, obj=3801591, obj_act_id=3804591)
    CommonFunc_20005520(0, flag=13800592, obj=3801592, obj_act_id=3804592)
    CommonFunc_20005523(0, obj=3801570, completion_count=2)
    CommonFunc_20005523(0, obj=3801571, completion_count=1)
    CommonFunc_20005523(0, obj=3801573, completion_count=1)
    CommonFunc_20005523(0, obj=3801574, completion_count=2)
    Event_13805590(0, obj=3801572, flag=13800800, flag_1=53800500)
    CommonFunc_20005701(
        0,
        left=13800830,
        summon_flag=13804193,
        dismissal_flag=13805193,
        character=3800193,
        region=3802193,
        left_1=0,
    )
    CommonFunc_20005720(0, flag=13804193, flag_1=13805193, flag_2=13800830, character=3800193)
    CommonFunc_20005710(0, flag=13804193, flag_1=13805835, character=3800193, region=3802830, region_1=3802835)
    CommonFunc_20005713(0, flag=9482, flag_1=13800830, flag_2=13804193, flag_3=13805193, character=3800193)
    CommonFunc_20005701(
        0,
        left=13800830,
        summon_flag=13804195,
        dismissal_flag=13805195,
        character=3800195,
        region=3802195,
        left_1=13800196,
    )
    CommonFunc_20005720(0, flag=13804195, flag_1=13805195, flag_2=13800830, character=3800195)
    CommonFunc_20005710(0, flag=13804195, flag_1=13805835, character=3800195, region=3802830, region_1=3802835)
    CommonFunc_20005750(
        0,
        flag=13800800,
        flag_1=13800196,
        summon_flag=13804196,
        dismissal_flag=13805196,
        character=3800196,
        region=3802196,
        region_1=3802197,
        seconds=0.0,
        left=0,
    )
    CommonFunc_20005721(0, flag=13804196, flag_1=13805196, flag_2=13800800, character=3800196)
    CommonFunc_20005760(0, flag=13800196, flag_1=13804196, flag_2=13805196, character=3800196)
    CommonFunc_20005341(0, flag=13800196, character=3800196, item_lot=58400)
    CommonFunc_20005320(0, character=3800198, region=3802370, patrol_information_id=3803370)
    CommonFunc_20005342(0, flag=13800398, character=3800198)
    Event_13805372()
    Event_13805595()
    Event_13800702(0, attacked_entity=3800710, collision=3804713)
    Event_13805703(
        0,
        character=3800700,
        character_1=3800705,
        character_2=3800701,
        character_3=3800706,
        character_4=3800702,
        character_5=3800707,
        animation_id=90760,
        command_id=1900,
        character_6=3800710,
        map_piece_id=3804711,
        vfx_id=3804700,
        vfx_id_1=3804701,
        vfx_id_2=3804710,
        collision=3804712,
    )
    CommonFunc_20006001(0, attacked_entity=3800700, flag=1356, flag_1=1357, flag_2=73800130, right=3)
    CommonFunc_20006000(
        0,
        character=3800700,
        flag=1356,
        flag_1=1357,
        flag_2=73800130,
        value=0.6499999761581421,
        first_flag=1355,
        last_flag=1359,
        right=0,
    )
    CommonFunc_20006002(0, character=3800700, flag=1358, first_flag=1355, last_flag=1359)
    CommonFunc_20006001(0, attacked_entity=3800701, flag=1356, flag_1=1357, flag_2=73800132, right=3)
    CommonFunc_20006000(
        0,
        character=3800701,
        flag=1356,
        flag_1=1357,
        flag_2=73800132,
        value=0.6499999761581421,
        first_flag=1355,
        last_flag=1359,
        right=0,
    )
    CommonFunc_20006002(0, character=3800701, flag=1358, first_flag=1355, last_flag=1359)
    CommonFunc_20006002(0, character=3800703, flag=1358, first_flag=1355, last_flag=1359)
    Event_13805704(0, character=3800703)
    CommonFunc_20006001(0, attacked_entity=3800705, flag=1356, flag_1=1357, flag_2=73800131, right=3)
    CommonFunc_20006000(
        0,
        character=3800705,
        flag=1356,
        flag_1=1357,
        flag_2=73800131,
        value=0.6499999761581421,
        first_flag=1355,
        last_flag=1359,
        right=0,
    )
    CommonFunc_20006002(0, character=3800705, flag=1358, first_flag=1355, last_flag=1359)
    CommonFunc_20006001(0, attacked_entity=3800706, flag=1356, flag_1=1357, flag_2=73800133, right=3)
    CommonFunc_20006000(
        0,
        character=3800706,
        flag=1356,
        flag_1=1357,
        flag_2=73800133,
        value=0.6499999761581421,
        first_flag=1355,
        last_flag=1359,
        right=0,
    )
    CommonFunc_20006002(0, character=3800706, flag=1358, first_flag=1355, last_flag=1359)
    CommonFunc_20006002(0, character=3800708, flag=1358, first_flag=1355, last_flag=1359)
    Event_13805704(1, character=3800708)
    CommonFunc_20006002(0, character=3800710, flag=1498, first_flag=1495, last_flag=1499)
    CommonFunc_20005900(0, flag=13800380, flag_1=6330)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13801200()
    Event_13805580()
    Event_13805700(
        0,
        character=3800700,
        character_1=3800705,
        character_2=3800701,
        character_3=3800706,
        character_4=3800702,
        character_5=3800707,
        character_6=3800703,
        character_7=3800708,
        animation_id=90760,
        command_id=1900,
        vfx_id=3804700,
        vfx_id_1=3804701,
    )
    Event_13805706(0, character=3800710, map_piece_id=3804711, vfx_id=3804710, collision=3804712)
    Event_13805707()
    DisableSoundEvent(sound_id=3804801)
    DisableSoundEvent(sound_id=3804802)
    DisableSoundEvent(sound_id=3804831)
    DisableSoundEvent(sound_id=3804832)
    DisableSoundEvent(sound_id=3804861)
    DisableSoundEvent(sound_id=3804862)


@RestartOnRest(13801200)
def Event_13801200():
    """Event 13801200"""
    if ThisEventSlotFlagEnabled():
        return
    SetNetworkConnectedFlagState(flag=13800200, state=FlagSetting.On)


@RestartOnRest(13805201)
def Event_13805201():
    """Event 13805201"""
    DisableGravity(3800100)
    DisableCharacterCollision(3800100)
    DisableAnimations(3800100)
    GotoIfFlagEnabled(Label.L0, flag=13800200)
    ForceAnimation(3801200, 0, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3801200, 10, loop=True, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(13805202)
def Event_13805202():
    """Event 13805202"""
    GotoIfFlagEnabled(Label.L0, flag=13800200)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9321, entity=3801200))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=3801200, destination_type=CoordEntityType.Object, dummy_id=101, short_move=True)
    ForceAnimation(PLAYER, 60230, unknown2=1.0)
    ForceAnimation(3801200, 201, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(3801200, 10, loop=True, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13800200, state=FlagSetting.On)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9320, entity=3801200))
    
    MAIN.Await(AND_2)
    
    Move(PLAYER, destination=3801200, destination_type=CoordEntityType.Object, dummy_id=103, short_move=True)
    ForceAnimation(PLAYER, 60231, unknown2=1.0)
    ForceAnimation(3801200, 210, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(3801200, 0, loop=True, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13800200, state=FlagSetting.Off)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    Restart()


@RestartOnRest(13805203)
def Event_13805203():
    """Event 13805203"""
    DisableAI(3800100)
    ReplanAI(3800100)
    OR_1.Add(FlagEnabled(13800200))
    
    MAIN.Await(OR_1)
    
    EnableAI(3800100)
    ReplanAI(3800100)
    AND_1.Add(FlagDisabled(13800200))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(13805206)
def Event_13805206():
    """Event 13805206"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3802380))
    AND_1.Add(CharacterBackreadEnabled(3800100))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(3800100, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    
    MAIN.Await(AllPlayersOutsideRegion(region=3802380))
    
    SetNetworkUpdateRate(3800100, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    Restart()


@RestartOnRest(13805207)
def Event_13805207(_, vibration_id: int, anchor_entity: int):
    """Event 13805207"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 11213))
    
    SetCameraVibration(vibration_id=vibration_id, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    Wait(1.0)
    Restart()


@RestartOnRest(13805240)
def Event_13805240(_, character: int, character_1: int, patrol_information_id: int):
    """Event 13805240"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(HasAIStatus(character_1, ai_status=AIStatusType.Battle))

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(13805245)
def Event_13805245(_, character: int, patrol_information_id: int, patrol_information_id_1: int):
    """Event 13805245"""
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 4650))
    
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id_1)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 4650))
    
    Wait(10.0)
    Restart()


@RestartOnRest(13805270)
def Event_13805270(_, character: int, region: int, region_1: int):
    """Event 13805270"""
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    SkipLinesIfConditionTrue(1, AND_3)
    AICommand(character, command_id=-1, command_slot=0)
    SetNest(character, region=region)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region_1)
    AICommand(character, command_id=100, command_slot=0)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    AND_2.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(13805272)
def Event_13805272(_, character: int, region: int, region_1: int, region_2: int, region_3: int, region_4: int):
    """Event 13805272"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    EnableAI(character)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    AICommand(character, command_id=100, command_slot=0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=4.0))
    AND_1.Add(CharacterInsideRegion(character=character, region=region_2))
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region_3)
    AICommand(character, command_id=100, command_slot=0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=4.0))
    AND_1.Add(CharacterInsideRegion(character=character, region=region_4))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(13805280)
def Event_13805280():
    """Event 13805280"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(ObjectDestroyed(3801403))
    
    Wait(5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(3805201, ai_param_id=107021)
    SetAIParamID(3805202, ai_param_id=107022)
    ClearTargetList(3805200)
    ReplanAI(3805200)


@RestartOnRest(13805300)
def Event_13805300(_, character: int, region: int):
    """Event 13805300"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    Kill(character, award_souls=True)


@RestartOnRest(13805340)
def Event_13805340(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    region: int,
    seconds: float,
):
    """Event 13805340"""
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
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    
    MAIN.Await(OR_3)
    
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    Wait(seconds)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13805350)
def Event_13805350(_, character: int):
    """Event 13805350"""
    MAIN.Await(CharacterHasSpecialEffect(character, 4021))
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(character, 4021)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(13805360)
def Event_13805360():
    """Event 13805360"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3802392))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(3805450, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3802392))
    
    SetNetworkUpdateRate(3805450, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    Wait(1.0)
    Restart()


@RestartOnRest(13805361)
def Event_13805361():
    """Event 13805361"""
    AICommand(3800500, command_id=-1, command_slot=0)
    SetNest(3800500, region=3802350)
    
    MAIN.Await(CharacterOutsideRegion(character=3800500, region=3802351))
    
    AICommand(3800500, command_id=100, command_slot=0)
    
    MAIN.Await(CharacterInsideRegion(character=3800500, region=3802351))
    
    Restart()


@RestartOnRest(13805365)
def Event_13805365():
    """Event 13805365"""
    DisableGravity(3805632)


@RestartOnRest(13805366)
def Event_13805366(_, character: int, character_1: int):
    """Event 13805366"""
    DisableGravity(character_1)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(HealthRatio(character) <= 0.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character_1)


@RestartOnRest(13805370)
def Event_13805370():
    """Event 13805370"""
    AddSpecialEffect(3800352, 5000)


@RestartOnRest(13805371)
def Event_13805371():
    """Event 13805371"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(3800480, 5000)
    AddSpecialEffect(3800481, 5000)
    AddSpecialEffect(3800455, 5000)
    AddSpecialEffect(3800456, 5000)
    AddSpecialEffect(3800457, 5000)
    AddSpecialEffect(3800458, 5000)


@RestartOnRest(13805372)
def Event_13805372():
    """Event 13805372"""
    AddSpecialEffect(3800198, 5000)


@RestartOnRest(13805400)
def Event_13805400():
    """Event 13805400"""
    AND_1.Add(ObjectDestroyed(3801403))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_2.Add(PlayerNotInOwnWorld())
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    
    MAIN.Await(ObjectDestroyed(3801403))
    
    ForceAnimation(3806400, 1, unknown2=1.0)
    Wait(6.0)
    DisableObject(3801401)
    Wait(6.0)
    RegisterLadder(start_climbing_flag=13800402, stop_climbing_flag=13800403, obj=3801402)
    Wait(5.329999923706055)
    ForceAnimation(3801400, 2, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=3801400, animation_id=2)
    DisableObject(3801401)
    RegisterLadder(start_climbing_flag=13800402, stop_climbing_flag=13800403, obj=3801402)


@ContinueOnRest(13805402)
def Event_13805402():
    """Event 13805402"""
    AND_1.Add(ObjectDestroyed(3801401))
    if AND_1:
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectBackreadState_Alternate(obj=3806400, state=True))
    
    ForceAnimation(3806400, 0, loop=True, unknown2=1.0)


@RestartOnRest(13805420)
def Event_13805420(_, owner_entity: int, region: int, entity: int, source_entity: int, behavior_id: int):
    """Event 13805420"""
    CreateProjectileOwner(entity=owner_entity)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    ForceAnimation(entity, 0, wait_for_completion=True, unknown2=1.0)
    Wait(1.0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        dummy_id=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        dummy_id=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(4.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(13805430)
def Event_13805430(
    _,
    owner_entity: int,
    entity: int,
    region: int,
    source_entity: int,
    source_entity_1: int,
    source_entity_2: int,
):
    """Event 13805430"""
    CreateProjectileOwner(entity=owner_entity)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    ForceAnimation(entity, 0, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(13805440)
def Event_13805440(
    _,
    owner_entity: int,
    entity: int,
    entity_1: int,
    region: int,
    region_1: int,
    source_entity: int,
    source_entity_1: int,
    source_entity_2: int,
):
    """Event 13805440"""
    CreateProjectileOwner(entity=owner_entity)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    ForceAnimation(entity, 0, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity_1, 0, wait_for_completion=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.20000000298023224)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.5)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5811,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5812,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5813,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5814,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5815,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=5816,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_2)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region_1))
    
    ForceAnimation(entity_1, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 3 --- #
    DefineLabel(3)
    Restart()


@RestartOnRest(13805450)
def Event_13805450():
    """Event 13805450"""
    CreateProjectileOwner(entity=3800560)
    if ObjectNotDestroyed(3801305):
        OR_1.Add(ObjectDestroyed(3801305))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3802430))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(3801217, 0, wait_for_completion=True, unknown2=1.0)
    Wait(0.20000000298023224)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.5)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5821,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5822,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5823,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5824,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5825,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802431,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802432,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802433,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802434,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802435,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802436,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802437,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802438,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=3800560,
            source_entity=3802439,
            dummy_id=-1,
            behavior_id=5826,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(2.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=3802430))
    
    ForceAnimation(3801217, 1, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(13800500)
def Event_13800500():
    """Event 13800500"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=3801501, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ObjectActivated(obj_act_id=3804500))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3801501, 1, unknown2=1.0)
    End()


@RestartOnRest(13805520)
def Event_13805520():
    """Event 13805520"""
    RegisterLadder(start_climbing_flag=13800520, stop_climbing_flag=13800521, obj=3801520)
    RegisterLadder(start_climbing_flag=13800522, stop_climbing_flag=13800523, obj=3801522)
    RegisterLadder(start_climbing_flag=13800524, stop_climbing_flag=13800525, obj=3801524)
    RegisterLadder(start_climbing_flag=13800526, stop_climbing_flag=13800527, obj=3801526)
    RegisterLadder(start_climbing_flag=13800528, stop_climbing_flag=13800529, obj=3801528)


@RestartOnRest(13805540)
def Event_13805540():
    """Event 13805540"""
    if FlagEnabled(13800800):
        return
    if ThisEventSlotFlagEnabled():
        return
    DeleteObjectVFX(3801360, erase_root=False)
    DeleteObjectVFX(3801361, erase_root=False)
    DeleteObjectVFX(3801362, erase_root=False)
    DeleteObjectVFX(3801363, erase_root=False)
    DeleteObjectVFX(3801364, erase_root=False)
    DeleteObjectVFX(3801365, erase_root=False)
    DeleteObjectVFX(3801366, erase_root=False)
    DeleteObjectVFX(3801369, erase_root=False)
    DeleteObjectVFX(3801370, erase_root=False)
    DeleteObjectVFX(3801371, erase_root=False)
    DeleteObjectVFX(3801372, erase_root=False)
    DeleteObjectVFX(3801373, erase_root=False)
    DeleteObjectVFX(3801374, erase_root=False)
    DeleteObjectVFX(3801375, erase_root=False)
    DeleteObjectVFX(3801376, erase_root=False)
    DeleteObjectVFX(3801377, erase_root=False)
    DeleteObjectVFX(3801378, erase_root=False)
    DeleteObjectVFX(3801379, erase_root=False)
    DeleteObjectVFX(3801380, erase_root=False)
    CreateObjectVFX(3801360, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801361, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801362, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801363, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801364, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801365, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801366, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801369, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801370, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801371, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801372, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801373, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801374, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801375, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801376, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801377, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801378, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801379, vfx_id=200, dummy_id=838041)
    CreateObjectVFX(3801380, vfx_id=200, dummy_id=838041)


@RestartOnRest(13800548)
def Event_13800548(_, obj: int):
    """Event 13800548"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(ObjectDestroyed(obj))
    
    MAIN.Await(OR_1)
    
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    End()


@RestartOnRest(13804550)
def Event_13804550():
    """Event 13804550"""
    Event_13805553()
    Event_13805557()


@RestartOnRest(13805550)
def Event_13805550(_, obj: int, animation_id: int, flag: int):
    """Event 13805550"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(ObjectBackreadEnabled(obj=obj))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    ForceAnimation(obj, animation_id, unknown2=1.0)


@RestartOnRest(13805552)
def Event_13805552():
    """Event 13805552"""
    if ObjectDestroyed(3801240):
        return
    if ThisEventSlotFlagEnabled():
        return

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3802520))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(50):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5830,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5831,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5832,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5833,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5834,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5835,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5836,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    ForceAnimation(3801240, 10, unknown2=1.0)
    Wait(9.300000190734863)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)


@RestartOnRest(13805553)
def Event_13805553():
    """Event 13805553"""
    DisableObject(3801390)
    DisableTreasure(obj=3801390)
    GotoIfObjectDestroyed(Label.L9, obj=3801240)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13805554, state=FlagSetting.Off)
    AND_1.Add(FlagEnabled(13805552))
    AND_1.Add(FlagDisabled(13805554))
    
    MAIN.Await(AND_1)
    
    AND_9.Add(CharacterDead(3800270))
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    if ThisEventSlotFlagEnabled():
        Wait(1.0)
    if FlagEnabled(50):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5830,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5831,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5832,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5833,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5834,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5835,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            obj_flag=13800550,
            obj=3801240,
            dummy_id=1,
            behavior_param_id=5836,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13805554, state=FlagSetting.On)
    ForceAnimation(3801240, 11, unknown2=1.0)
    Wait(19.0)
    RemoveObjectFlag(obj_flag=13800550)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(obj_flag=13800550)
    CreateTemporaryVFX(vfx_id=838091, anchor_entity=3801240, dummy_id=200, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(3801240, 381070000, sound_type=SoundType.o_Object)
    DestroyObject(3801240)
    SetNetworkConnectedFlagState(flag=13805555, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableObject(3801390)
    EnableTreasure(obj=3801390)


@RestartOnRest(13805556)
def Event_13805556():
    """Event 13805556"""
    if ObjectDestroyed(3801241):
        return
    if ThisEventSlotFlagEnabled():
        return

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3802523))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3802524))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3802525))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(50):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5830,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5831,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5832,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5833,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5834,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5835,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5836,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    ForceAnimation(3801241, 21, unknown2=1.0)
    Wait(12.5)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)


@RestartOnRest(13805557)
def Event_13805557():
    """Event 13805557"""
    DisableObject(3801391)
    DisableTreasure(obj=3801391)
    DisableCharacter(3800498)
    DisableAnimations(3800498)
    GotoIfObjectDestroyed(Label.L9, obj=3801241)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13805558, state=FlagSetting.Off)
    AND_1.Add(FlagEnabled(13805556))
    AND_1.Add(FlagDisabled(13805558))
    
    MAIN.Await(AND_1)
    
    AND_9.Add(CharacterDead(3800260))
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    if ThisEventSlotFlagEnabled():
        Wait(0.5)
    if FlagEnabled(50):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5830,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5831,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5832,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5833,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5834,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5835,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            obj_flag=13800551,
            obj=3801241,
            dummy_id=1,
            behavior_param_id=5836,
            target_type=DamageTargetType.Character,
            radius=1.7000000476837158,
            life=20.0,
            repetition_time=10.0,
        )
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13805558, state=FlagSetting.On)
    ForceAnimation(3801241, 22, unknown2=1.0)
    Wait(15.800000190734863)
    RemoveObjectFlag(obj_flag=13800551)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(obj_flag=13800551)
    CreateTemporaryVFX(vfx_id=838091, anchor_entity=3801241, dummy_id=200, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(3801241, 381070000, sound_type=SoundType.o_Object)
    DestroyObject(3801241)
    SetNetworkConnectedFlagState(flag=13805559, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)
    EnableObject(3801391)
    EnableTreasure(obj=3801391)
    EnableCharacter(3800498)
    EnableAnimations(3800498)


@RestartOnRest(13805560)
def Event_13805560(_, obj: int, source_entity: int, owner_entity: int):
    """Event 13805560"""
    if ObjectDestroyed(obj):
        return
    
    MAIN.Await(ObjectDestroyed(obj))
    
    CreateTemporaryVFX(vfx_id=610707, anchor_entity=source_entity, dummy_id=10, anchor_type=CoordEntityType.Object)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5840,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5841,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5842,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5843,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5844,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5845,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=10,
            behavior_id=5846,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )


@RestartOnRest(13805580)
def Event_13805580():
    """Event 13805580"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(3801240)
    RestoreObject(3801241)
    RestoreObject(3806300)


@RestartOnRest(13805590)
def Event_13805590(_, obj: int, flag: int, flag_1: int):
    """Event 13805590"""
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)
    DisableTreasure(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(obj)
    EnableTreasure(obj=obj)


@RestartOnRest(13805595)
def Event_13805595():
    """Event 13805595"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(6065):
        return
    OR_1.Add(FlagEnabled(13800196))
    OR_1.Add(FlagEnabled(13800398))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(6065):
        return
    AwardGestureItem(gesture_id=15, item_type=ItemType.Good, item_id=9017)
    EnableFlag(6065)


@RestartOnRest(13800800)
def Event_13800800():
    """Event 13800800"""
    GotoIfFlagDisabled(Label.L0, flag=13801800)
    DisableObjectActivation(3801561, obj_act_id=-1)
    EndOfAnimation(obj=3801561, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=13800800)
    
    MAIN.Await(HealthRatio(3800800) <= 0.0)
    
    RemoveSpecialEffect(3805800, 5830)
    RemoveSpecialEffect(3805800, 5832)
    Kill(3805800)
    Wait(1.0)
    PlaySoundEffect(3800800, 777777777, sound_type=SoundType.s_SFX)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(3800800))
    
    MAIN.Await(AND_1)
    
    KillBoss(game_area_param_id=3800800)
    EnableFlag(13800800)
    EnableFlag(9315)
    EnableFlag(6315)
    AddSpecialEffect(PLAYER, 4900)
    AddSpecialEffect(PLAYER, 4901)
    Wait(5.0)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=3802806))
    GotoIfConditionFalse(Label.L2, input_condition=AND_9)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        38000020,
        cutscene_flags=CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3802804,
        game_map=CATACOMBS_OF_CARTHUS,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        38000020,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3802804,
        game_map=CATACOMBS_OF_CARTHUS,
    )
    SkipLines(1)
    PlayCutscene(
        38000020,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3802807,
        game_map=CATACOMBS_OF_CARTHUS,
    )
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    EndOfAnimation(obj=3801561, animation_id=1)
    EnableFlag(63800561)
    RemoveSpecialEffect(PLAYER, 4900)
    RemoveSpecialEffect(PLAYER, 4901)
    EnableFlag(13801800)


@RestartOnRest(13805809)
def Event_13805809():
    """Event 13805809"""
    GotoIfFlagDisabled(Label.L0, flag=13800800)
    DisableCharacter(3800800)
    Kill(3800800)
    DisableCharacter(3805800)
    Kill(3805800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(3801561, obj_act_id=1000371)
    DisableAI(3805800)
    DisableAI(3800800)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=13805805)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(13800800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9322, entity=3801810))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        38000000,
        cutscene_flags=CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3802802,
        game_map=CATACOMBS_OF_CARTHUS,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        38000000,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3802802,
        game_map=CATACOMBS_OF_CARTHUS,
    )
    SkipLines(1)
    PlayCutscene(
        38000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3802803,
        game_map=CATACOMBS_OF_CARTHUS,
    )
    WaitFrames(frames=1)
    DeleteObjectVFX(3801360, erase_root=False)
    DeleteObjectVFX(3801361, erase_root=False)
    DeleteObjectVFX(3801362, erase_root=False)
    DeleteObjectVFX(3801363, erase_root=False)
    DeleteObjectVFX(3801364, erase_root=False)
    DeleteObjectVFX(3801365, erase_root=False)
    DeleteObjectVFX(3801366, erase_root=False)
    DeleteObjectVFX(3801367, erase_root=False)
    DeleteObjectVFX(3801368, erase_root=False)
    DeleteObjectVFX(3801369, erase_root=False)
    DeleteObjectVFX(3801370, erase_root=False)
    DeleteObjectVFX(3801371, erase_root=False)
    DeleteObjectVFX(3801372, erase_root=False)
    DeleteObjectVFX(3801373, erase_root=False)
    DeleteObjectVFX(3801374, erase_root=False)
    DeleteObjectVFX(3801375, erase_root=False)
    DeleteObjectVFX(3801376, erase_root=False)
    DeleteObjectVFX(3801377, erase_root=False)
    DeleteObjectVFX(3801378, erase_root=False)
    DeleteObjectVFX(3801379, erase_root=False)
    DeleteObjectVFX(3801380, erase_root=False)
    if FlagDisabled(13800801):
        return
    AddSpecialEffect(3800800, 5300)
    AddSpecialEffect(3800800, 5400)
    AddSpecialEffect(3800800, 5441)
    AddSpecialEffect(3800800, 7060)
    AddSpecialEffect(3800800, 30000)
    AddSpecialEffect(3800800, 30010)
    AddSpecialEffect(3800800, 30020)
    AddSpecialEffect(3800800, 30030)
    AddSpecialEffect(3800800, 30040)
    AddSpecialEffect(3800800, 30100)
    WaitFrames(frames=1)
    AddSpecialEffect(3800800, 10507)
    AddSpecialEffect(3800800, 10508)
    AddSpecialEffect(3800800, 12250)
    AddSpecialEffect(3800800, 12252)
    AddSpecialEffect(3800800, 12254)
    AddSpecialEffect(3800800, 12256)
    AddSpecialEffect(3800800, 12610)
    AddSpecialEffect(3800800, 12611)
    AddSpecialEffect(3800800, 12612)
    AddSpecialEffect(3800800, 12617)
    AddSpecialEffect(3800800, 12618)
    DisableMapCollision(collision=3804810)
    EnableAI(3800800)
    EnableAI(3805800)
    EnableBossHealthBar(3800800, name=905160)
    SetNetworkUpdateRate(3800800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ActivateMultiplayerBuffs(3800800)
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=13805805, state=FlagSetting.On)
    SetNetworkUpdateAuthority(3800800, authority_level=UpdateAuthority.Forced)
    NotifyBossBattleStart()


@RestartOnRest(13805810)
def Event_13805810():
    """Event 13805810"""
    if FlagEnabled(13800800):
        return
    if FlagEnabled(13800801):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableMapCollision(collision=3804810)
    OR_1.Add(AttackedWithDamageType(attacked_entity=3800800))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3800800, radius=27.0))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(3800800, 5300)
    AddSpecialEffect(3800800, 5400)
    AddSpecialEffect(3800800, 5441)
    AddSpecialEffect(3800800, 7060)
    AddSpecialEffect(3800800, 30000)
    AddSpecialEffect(3800800, 30010)
    AddSpecialEffect(3800800, 30020)
    AddSpecialEffect(3800800, 30030)
    AddSpecialEffect(3800800, 30040)
    AddSpecialEffect(3800800, 30100)
    WaitFrames(frames=1)
    AddSpecialEffect(3800800, 10507)
    AddSpecialEffect(3800800, 10508)
    AddSpecialEffect(3800800, 12250)
    AddSpecialEffect(3800800, 12252)
    AddSpecialEffect(3800800, 12254)
    AddSpecialEffect(3800800, 12256)
    AddSpecialEffect(3800800, 12610)
    AddSpecialEffect(3800800, 12611)
    AddSpecialEffect(3800800, 12612)
    AddSpecialEffect(3800800, 12617)
    AddSpecialEffect(3800800, 12618)
    EnableAI(3800800)
    EnableAI(3805800)
    EnableBossHealthBar(3800800, name=905160)
    SetNetworkUpdateRate(3800800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ActivateMultiplayerBuffs(3800800)
    DisableMapCollision(collision=3804810)
    EnableFlag(13800801)
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=13805805, state=FlagSetting.On)
    SetNetworkUpdateAuthority(3800800, authority_level=UpdateAuthority.Forced)
    NotifyBossBattleStart()


@RestartOnRest(13805811)
def Event_13805811():
    """Event 13805811"""
    if FlagEnabled(13800800):
        return
    
    MAIN.Await(HealthRatio(3800800) <= 0.800000011920929)
    
    EnableFlag(13805802)


@RestartOnRest(13805812)
def Event_13805812():
    """Event 13805812"""
    if FlagEnabled(13800800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterBackreadEnabled(3800800))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(13805814):
        CreateNPCPart(3800800, npc_part_id=20, part_index=NPCPartType.Part2, part_health=634)
        CreateNPCPart(3800800, npc_part_id=30, part_index=NPCPartType.Part3, part_health=282)
        IncrementCharacterNewGameCycle(character=3800800)
    if FlagDisabled(13805813):
        CreateNPCPart(3800800, npc_part_id=40, part_index=NPCPartType.Part4, part_health=423)
        CreateNPCPart(3800800, npc_part_id=50, part_index=NPCPartType.Part5, part_health=211)
        IncrementCharacterNewGameCycle(character=3800800)
    WaitFrames(frames=1)
    End()


@RestartOnRest(13805813)
def Event_13805813(
    _,
    npc_part_id: int,
    value: int,
    npc_part_id_1: int,
    value_1: int,
    flag: int,
    special_effect: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
):
    """Event 13805813"""
    if FlagEnabled(13800800):
        return
    WaitFrames(frames=1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3802806))
    OR_1.Add(CharacterPartHealth(3800800, npc_part_id=npc_part_id) <= value)
    OR_1.Add(CharacterPartHealth(3800800, npc_part_id=npc_part_id_1) <= value_1)
    AND_1.Add(OR_1)
    OR_2.Add(CharacterDead(3800800))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    AND_9.Add(CharacterDead(3800800))
    if AND_9:
        return
    AND_2.Add(EventValue(flag=13805816, bit_count=2) == 1)
    AND_3.Add(EventValue(flag=13805816, bit_count=2) == 2)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_3)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(3800800, 12616)
    ForceAnimation(3800800, animation_id, wait_for_completion=True, unknown2=1.0)
    ReplanAI(3800800)
    IncrementEventValue(13805816, bit_count=2, max_value=3)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(3800800, 12616)
    ForceAnimation(3800800, animation_id_1, wait_for_completion=True, unknown2=1.0)
    ReplanAI(3800800)
    IncrementEventValue(13805816, bit_count=2, max_value=3)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3800800, 12615)
    ForceAnimation(3800800, animation_id_2, wait_for_completion=True, unknown2=1.0)
    ReplanAI(3800800)
    IncrementEventValue(13805816, bit_count=2, max_value=3)
    End()
    AddSpecialEffect(3800800, special_effect)


@ContinueOnRest(13804814)
def Event_13804814(_, npc_part_id: short, part_health: int, npc_part_id_1: short, part_health_1: int, flag: int):
    """Event 13804814"""
    if FlagEnabled(13800800):
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    CreateNPCPart(3800800, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=part_health)
    CreateNPCPart(3800800, npc_part_id=npc_part_id_1, part_index=NPCPartType.Part3, part_health=part_health_1)
    IncrementCharacterNewGameCycle(character=3800800)
    WaitFrames(frames=1)
    End()


@ContinueOnRest(13805820)
def Event_13805820():
    """Event 13805820"""
    if FlagEnabled(13800800):
        return
    AND_1.Add(CharacterHasTAEEvent(3800800, tae_event_id=30))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(EventValue(flag=13805816, bit_count=2) == 1)
    AND_3.Add(EventValue(flag=13805816, bit_count=2) == 2)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_3)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceSpawnerToSpawn(spawner=3803810)
    SetNetworkConnectedFlagState(flag=13804810, state=FlagSetting.On)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceSpawnerToSpawn(spawner=3803811)
    SetNetworkConnectedFlagState(flag=13804811, state=FlagSetting.On)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceSpawnerToSpawn(spawner=3803812)
    SetNetworkConnectedFlagState(flag=13804812, state=FlagSetting.On)
    Goto(Label.L3)

    # --- Label 3 --- #
    DefineLabel(3)
    SetNetworkConnectedFlagState(flag=13804813, state=FlagSetting.Off)
    AICommand(3800800, command_id=-1, command_slot=0)
    Wait(1.0)
    Restart()


@RestartOnRest(13804815)
def Event_13804815(_, character: int, region: int, dummy_id: int):
    """Event 13804815"""
    if FlagEnabled(13800800):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(character)
    DisableHealthBar(character)
    Kill(character)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(AND_1)
    
    DisableInvincibility(character)
    EnableGravity(character)
    EnableHealthBar(character)
    Move(
        character,
        destination=3800800,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id,
        copy_draw_parent=character,
    )
    ActivateMultiplayerBuffs(character)
    Restart()


@ContinueOnRest(13805824)
def Event_13805824():
    """Event 13805824"""
    SetNetworkConnectedFlagState(flag=13804813, state=FlagSetting.On)
    AICommand(3800800, command_id=10, command_slot=0)
    AND_1.Add(FlagEnabled(13804810))
    AND_1.Add(CharacterDrawGroupEnabled(character=3805810))
    OR_1.Add(AND_1)
    AND_2.Add(FlagEnabled(13804811))
    AND_2.Add(CharacterDrawGroupEnabled(character=3805811))
    OR_1.Add(AND_2)
    AND_3.Add(FlagEnabled(13804812))
    AND_3.Add(CharacterDrawGroupEnabled(character=3805812))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SetNetworkConnectedFlagState(flag=13804810, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13804811, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13804812, state=FlagSetting.Off)
    Restart()


@ContinueOnRest(13805828)
def Event_13805828(_, flag: int, region: int, flag_1: int, flag_2: int):
    """Event 13805828"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_2)
    Restart()


@ContinueOnRest(13804829)
def Event_13804829(_, flag: int, obj: int, dummy_id: int):
    """Event 13804829"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    OR_1.Add(PlayerNotInOwnWorld())
    OR_3.Add(TryingToCreateSession())
    OR_3.Add(TryingToJoinSession())
    AND_2.Add(OR_3)
    AND_2.Add(FlagEnabled(flag))
    OR_4.Add(OR_1)
    OR_4.Add(AND_2)
    
    MAIN.Await(OR_4)
    
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, dummy_id=dummy_id)
    OR_5.Add(PlayerNotInOwnWorld())
    OR_7.Add(TryingToCreateSession())
    OR_7.Add(TryingToJoinSession())
    AND_4.Add(OR_7)
    AND_4.Add(FlagEnabled(flag))
    AND_5.Add(not OR_5)
    AND_5.Add(not AND_4)
    
    MAIN.Await(AND_5)
    
    Restart()


@RestartOnRest(13805829)
def Event_13805829():
    """Event 13805829"""
    Event_13805828(0, flag=13800800, region=3802821, flag_1=13805805, flag_2=13805806)
    Event_13804829(0, flag=13800800, obj=3801800, dummy_id=2)
    if FlagEnabled(13800801):
        CommonFunc_20005831(
            0,
            flag=13800800,
            flag_1=13805805,
            flag_2=13805806,
            region=3802806,
            sound_id=3804801,
            sound_id_1=3804802,
            flag_3=13805802,
        )
    else:
        CommonFunc_20001836(
            0,
            flag=13800800,
            flag_1=13805805,
            flag_2=13805806,
            flag_3=13800801,
            sound_id=3804801,
            sound_id_1=3804802,
            flag_4=13805802,
        )
    CommonFunc_20005810(0, flag=13800800, entity=3801800, target_entity=3802800, action_button_id=10000)


@ContinueOnRest(13800830)
def Event_13800830():
    """Event 13800830"""
    if FlagEnabled(13800830):
        return
    
    MAIN.Await(HealthRatio(3800830) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(3800830, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3800830))
    
    KillBoss(game_area_param_id=3800830)
    EnableFlag(13800830)
    EnableFlag(9317)
    EnableFlag(6317)


@RestartOnRest(13805840)
def Event_13805840():
    """Event 13805840"""
    GotoIfFlagDisabled(Label.L0, flag=13800830)
    DisableCharacter(3800830)
    Kill(3800830)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3800830)
    GotoIfFlagEnabled(Label.L1, flag=13800831)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=3800830, other_entity=PLAYER, radius=22.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3800830, attacker=PLAYER))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    SetNetworkConnectedFlagState(flag=13800831, state=FlagSetting.On)
    ForceAnimation(3800830, 1700, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(13805835))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3802830))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3800830, 10575)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(3800830)
    EnableBossHealthBar(3800830, name=903050)
    SetNetworkUpdateRate(3800830, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13805841)
def Event_13805841():
    """Event 13805841"""
    if FlagEnabled(13800830):
        return
    
    MAIN.Await(HealthRatio(3800830) <= 0.5)
    
    EnableFlag(13805832)


@RestartOnRest(13805842)
def Event_13805842():
    """Event 13805842"""
    if FlagEnabled(13800830):
        return
    if FlagEnabled(13800831):
        return
    ForceAnimation(3800830, 700, unknown2=1.0)


@RestartOnRest(13805843)
def Event_13805843():
    """Event 13805843"""
    if FlagEnabled(13800830):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(HealthRatio(3800830) <= 0.15000000596046448)
    AND_1.Add(AttackedWithDamageType(attacked_entity=3800830, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3800830, 20002, skip_transition=True, unknown2=1.0)


@RestartOnRest(13805844)
def Event_13805844():
    """Event 13805844"""
    if FlagEnabled(13805830):
        return
    CreateNPCPart(3800830, npc_part_id=10, part_index=NPCPartType.Part1, part_health=282)
    AND_1.Add(CharacterPartHealth(3800830, npc_part_id=10) <= 0)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3800830, 5404))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3800830, 20000, unknown2=1.0)
    SetNPCPartHealth(3800830, npc_part_id=10, desired_health=282, overwrite_max=True)
    Restart()


@RestartOnRest(13805857)
def Event_13805857(_, flag: int, entity: int, region: int, flag_1: int, action_button_id: int, character: int):
    """Event 13805857"""
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        ActivateMultiplayerBuffs(character)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagDisabled(flag))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_3)
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    RestartIfFinishedConditionTrue(input_condition=OR_3)
    
    MAIN.Await(FlagEnabled(13800831))

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    Restart()


@RestartOnRest(13805859)
def Event_13805859():
    """Event 13805859"""
    Event_13805857(
        0,
        flag=13800830,
        entity=3801830,
        region=3802830,
        flag_1=13805835,
        action_button_id=3801830,
        character=3800830,
    )
    CommonFunc_20005801(
        0,
        flag=13800830,
        entity=3801830,
        region=3802830,
        flag_1=13805835,
        action_button_id=3801830,
        flag_2=13805836,
    )
    CommonFunc_20005820(0, flag=13800830, obj=3801830, dummy_id=4, left=0)
    if FlagDisabled(13800831):
        CommonFunc_20001836(
            0,
            flag=13800830,
            flag_1=13805835,
            flag_2=13805836,
            flag_3=13800831,
            sound_id=3804831,
            sound_id_1=3804832,
            flag_4=13805832,
        )
    else:
        CommonFunc_20005831(
            0,
            flag=13800830,
            flag_1=13805835,
            flag_2=13805836,
            region=3802830,
            sound_id=3804831,
            sound_id_1=3804832,
            flag_3=13805832,
        )
    CommonFunc_20005837(
        0,
        flag=13800830,
        entity=3800830,
        radius=12.0,
        normal_camera_id=5290,
        locked_camera_id=5290,
        flag_1=13805835,
        flag_2=13805836,
    )
    CommonFunc_20005810(0, flag=13800830, entity=3801830, target_entity=3802830, action_button_id=10000)


@ContinueOnRest(13800899)
def Event_13800899():
    """Event 13800899"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(13800800))
    AND_1.Add(FlagEnabled(13800800))
    AND_1.Add(FlagEnabled(13800800))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13800899)


@ContinueOnRest(13805570)
def Event_13805570():
    """Event 13805570"""
    DisableObject(3801975)
    End()


@ContinueOnRest(13805700)
def Event_13805700(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    character_7: int,
    animation_id: int,
    command_id: int,
    vfx_id: int,
    vfx_id_1: int,
):
    """Event 13805700"""
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
    AND_2.Add(FlagEnabled(1342))
    AND_2.Add(FlagEnabled(74000700))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1344, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1344))
    OR_3.Add(FlagEnabled(73800100))
    OR_3.Add(FlagEnabled(73800134))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1345, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1345))
    AND_4.Add(FlagEnabled(73800101))
    AND_4.Add(FlagEnabled(73800102))
    AND_4.Add(FlagEnabled(1497))
    AND_4.Add(FlagEnabled(9315))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1346, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1358, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1345))
    AND_5.Add(FlagEnabled(73800101))
    AND_5.Add(FlagEnabled(73800102))
    AND_5.Add(FlagEnabled(1498))
    AND_5.Add(FlagEnabled(9315))
    SkipLinesIfConditionFalse(5, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1347, state=FlagSetting.On)
    EnableFlag(8263)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1561, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1345))
    AND_6.Add(FlagEnabled(73800101))
    AND_6.Add(FlagDisabled(73800102))
    AND_6.Add(FlagEnabled(9315))
    SkipLinesIfConditionFalse(4, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1347, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1561, state=FlagSetting.On)
    AND_7.Add(FlagEnabled(1351))
    AND_7.Add(FlagEnabled(50006030))
    AND_7.Add(FlagEnabled(8263))
    SkipLinesIfConditionFalse(4, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1353, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1357, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000069)
    if FlagEnabled(1355):
        DisableFlag(73800120)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L3, flag=1344)
    GotoIfFlagEnabled(Label.L4, flag=1345)
    GotoIfFlagEnabled(Label.L5, flag=1346)
    GotoIfFlagRangeAnyEnabled(Label.L6, flag_range=(1347, 1352))
    GotoIfFlagEnabled(Label.L13, flag=1353)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    GotoIfFlagEnabled(Label.L16, flag=1356)
    GotoIfFlagEnabled(Label.L18, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    ForceAnimation(character_1, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
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

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    DeleteVFX(vfx_id_1)
    GotoIfFlagEnabled(Label.L16, flag=1356)
    GotoIfFlagEnabled(Label.L18, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    ForceAnimation(character_2, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    ForceAnimation(character_3, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    SetTeamType(character_2, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    SetTeamType(character_3, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DropMandatoryTreasure(character_2)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DropMandatoryTreasure(character_3)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    EzstateAIRequest(character_4, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character_4)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    EzstateAIRequest(character_5, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character_5)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    End()

    # --- Label 13 --- #
    DefineLabel(13)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    GotoIfFlagEnabled(Label.L18, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    DisableAI(character_6)
    SetTeamType(character_6, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DisableAI(character_7)
    SetTeamType(character_7, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    DropMandatoryTreasure(character_6)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_6)
    DisableBackread(character_6)
    DropMandatoryTreasure(character_7)
    DisableCharacter(character_7)
    DisableBackread(character_7)
    End()


@ContinueOnRest(13805701)
def Event_13805701(_, character: int, character_1: int, animation_id: int, character_2: int):
    """Event 13805701"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(1343))
    AND_1.Add(FlagEnabled(1355))
    AND_1.Add(FlagEnabled(1483))
    AND_1.Add(FlagEnabled(1495))
    AND_1.Add(FlagEnabled(136))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L1)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1344, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1484, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1495, 1499))
    SetNetworkConnectedFlagState(flag=1497, state=FlagSetting.On)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L10, flag=9013)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    SetTeamType(character_2, TeamType.HostileNPC)
    if PlayerNotInOwnWorld():
        return
    SaveRequest()


@ContinueOnRest(13800702)
def Event_13800702(_, attacked_entity: int, collision: int):
    """Event 13800702"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(1484))
    AND_1.Add(PlayerStandingOnCollision(collision))
    AND_2.Add(HealthRatio(PLAYER) > 0.0)
    AND_2.Add(EntityWithinDistance(entity=attacked_entity, other_entity=PLAYER, radius=30.0))
    OR_1.Add(AND_2)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(73800134)


@ContinueOnRest(13805703)
def Event_13805703(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    animation_id: int,
    command_id: int,
    character_6: int,
    map_piece_id: int,
    vfx_id: int,
    vfx_id_1: int,
    vfx_id_2: int,
    collision: int,
):
    """Event 13805703"""
    DisableFlag(13800703)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    EndIfFlagRangeAnyEnabled(flag_range=(1346, 1354))
    AND_2.Add(FlagEnabled(1355))
    AND_2.Add(FlagEnabled(1344))
    OR_2.Add(FlagEnabled(73800100))
    OR_2.Add(FlagEnabled(73800134))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterBackreadDisabled(character))
    AND_2.Add(CharacterBackreadDisabled(character_1))
    OR_1.Add(AND_2)
    AND_3.Add(FlagEnabled(1355))
    AND_3.Add(FlagEnabled(1345))
    AND_3.Add(FlagEnabled(73800101))
    AND_3.Add(FlagEnabled(9315))
    AND_3.Add(CharacterBackreadDisabled(character_2))
    AND_3.Add(CharacterBackreadDisabled(character_3))
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    AND_4.Add(FlagEnabled(1355))
    AND_4.Add(FlagEnabled(1344))
    OR_4.Add(FlagEnabled(73800100))
    OR_4.Add(FlagEnabled(73800134))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1345, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1355))
    AND_5.Add(FlagEnabled(1345))
    AND_5.Add(FlagEnabled(73800101))
    AND_5.Add(FlagEnabled(73800102))
    AND_5.Add(FlagDisabled(1498))
    AND_5.Add(FlagEnabled(9315))
    SkipLinesIfConditionFalse(4, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1346, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1358, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1355))
    AND_6.Add(FlagEnabled(1345))
    AND_6.Add(FlagEnabled(73800101))
    AND_6.Add(FlagEnabled(73800102))
    AND_6.Add(FlagEnabled(1498))
    AND_6.Add(FlagEnabled(9315))
    SkipLinesIfConditionFalse(7, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1347, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1485, state=FlagSetting.On)
    EnableFlag(8263)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1561, state=FlagSetting.On)
    AND_7.Add(FlagEnabled(1355))
    AND_7.Add(FlagEnabled(1345))
    AND_7.Add(FlagEnabled(73800101))
    AND_7.Add(FlagDisabled(73800102))
    AND_7.Add(FlagEnabled(9315))
    SkipLinesIfConditionFalse(4, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1347, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1560, 1574))
    SetNetworkConnectedFlagState(flag=1561, state=FlagSetting.On)
    SaveRequest()
    SetNetworkConnectedFlagState(flag=13800703, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(13800703))
    
    GotoIfFlagEnabled(Label.L5, flag=1345)
    GotoIfFlagEnabled(Label.L6, flag=1346)
    GotoIfFlagEnabled(Label.L7, flag=1347)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    CreateVFX(vfx_id)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    ForceAnimation(character_2, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    ForceAnimation(character_3, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    CreateVFX(vfx_id)
    CreateVFX(vfx_id_1)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    EnableCharacter(character_4)
    EnableBackread(character_4)
    EzstateAIRequest(character_4, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character_4)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    EnableCharacter(character_5)
    EnableBackread(character_5)
    EzstateAIRequest(character_5, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character_5)
    End()

    # --- Label 7 --- #
    DefineLabel(7)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    DisableCharacter(character_5)
    DisableBackread(character_5)
    CreateVFX(vfx_id)
    CreateVFX(vfx_id_1)
    if FlagDisabled(1485):
        return
    DisableCharacter(character_6)
    DisableBackread(character_6)
    EnableMapPiece(map_piece_id=map_piece_id)
    CreateVFX(vfx_id_2)
    EnableMapCollision(collision=collision)
    End()


@ContinueOnRest(13805704)
def Event_13805704(_, character: int):
    """Event 13805704"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1353))
    AND_1.Add(FlagDisabled(1358))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=5.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    ReplanAI(character)


@ContinueOnRest(13805706)
def Event_13805706(_, character: int, map_piece_id: int, vfx_id: int, collision: int):
    """Event 13805706"""
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
    AND_2.Add(FlagEnabled(1482))
    AND_2.Add(FlagEnabled(74000700))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1484, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1495, 1499))
    SetNetworkConnectedFlagState(flag=1497, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1484))
    AND_3.Add(FlagEnabled(1498))
    OR_4.Add(FlagEnabled(1347))
    AND_4.Add(FlagEnabled(1345))
    OR_5.Add(FlagEnabled(1355))
    AND_5.Add(FlagEnabled(1356))
    AND_5.Add(FlagEnabled(70000069))
    OR_5.Add(AND_5)
    AND_4.Add(OR_5)
    OR_4.Add(AND_4)
    AND_3.Add(OR_4)
    AND_3.Add(FlagEnabled(73800101))
    AND_3.Add(FlagEnabled(73800102))
    AND_3.Add(FlagEnabled(9315))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(8263))
    SkipLinesIfConditionFalse(2, OR_3)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1485, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000076)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1484)
    GotoIfFlagEnabled(Label.L2, flag=1485)
    DisableCharacter(character)
    DisableBackread(character)
    DisableMapPiece(map_piece_id=map_piece_id)
    DeleteVFX(vfx_id)
    DisableMapCollision(collision=collision)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=map_piece_id)
    DeleteVFX(vfx_id)
    DisableMapCollision(collision=collision)
    GotoIfFlagEnabled(Label.L1, flag=1498)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(13805707)
def Event_13805707():
    """Event 13805707"""
    if PlayerNotInOwnWorld():
        return
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
    if FlagDisabled(1055):
        return
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
