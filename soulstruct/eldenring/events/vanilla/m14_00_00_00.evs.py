"""
linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=14000002, obj=14001952, unknown=5.0)
    RegisterGrace(grace_flag=14000003, obj=14001953, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(14000800, 14000000, 14000950, 14001950, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(14000850, 14000001, 14000951, 14001951, 5.0), arg_types="IIIIf")
    Event_14002080()
    Event_14002665()
    UnknownCollision_2011_2(unk_0_4=0, unk_4_8=0)
    Event_14002800()
    Event_14002810()
    Event_14002811()
    Event_14002849()
    Event_140028121()
    Event_140028122(0, character=14000800, special_effect=14585, special_effect_1=14575)
    Event_14002606()
    Event_14002689()
    Event_14003500(0, region=14002700, flag=14000800)
    Event_14002850()
    Event_14002860()
    Event_14002889()
    Event_14003801(
        0,
        14003800,
        14000801,
        14005810,
        14000810,
        14000811,
        14000812,
        14000813,
        14000814,
        14000815,
        14000816,
        14000817,
        14000818,
        14000819,
        14000820,
        14000821,
        14000822,
        14000823,
        14000824,
        14000825,
        14000826,
        14000827,
        14000828,
        14000829,
        140008230,
        14000831,
        14000832,
        14000833,
    )
    Event_14003825(0, flag=14003800, character=14000801, character_1=14005810)
    Event_14003805(0, flag=14003806, character=14000801, character_1=14005810, character_2=14005811)
    Event_14003807(0, character=14000801, character_1=14005810)
    Event_14003808(0, flag=14003800, character=14000801)
    Event_14003817(0, character=14005810)
    Event_14003809(0, flag=14003810, character=14000801)
    Event_14003811(
        0,
        14003810,
        14005810,
        14000810,
        14000811,
        14000812,
        14000813,
        14000814,
        14000815,
        14000816,
        14000817,
        14000818,
        14000819,
        14000820,
        14000821,
        14000822,
        14000823,
        14000824,
        14000825,
        14000826,
        14000827,
        14000828,
        14000829,
        140008230,
        14000831,
        14000832,
        14000833,
    )
    Event_14003814(0, destination=14000801, character=14000805)
    Event_14003815(0, character=14000801, anchor_entity=14000805)
    Event_14003892(0, character=14000801, character_1=14005810)
    Event_14003893(0, character=14000801, character_1=14005810)
    Event_14003894(0, character=14000801, character_1=14005810)
    Event_14003820(0, obj=14001820)
    Event_14003820(1, obj=14001821)
    Event_14003820(2, obj=14001822)
    Event_14003820(3, obj=14001823)
    Event_14003820(5, obj=14001825)
    Event_14003820(6, obj=14001826)
    Event_14003820(8, obj=14001828)
    Event_14003820(9, obj=14001829)
    Event_14003950(0, flag=14003820, obj=14001820)
    Event_14003950(1, flag=14003821, obj=14001821)
    Event_14003950(2, flag=14003822, obj=14001822)
    Event_14003950(3, flag=14003823, obj=14001823)
    Event_14003950(4, flag=14003825, obj=14001825)
    Event_14003950(5, flag=14003826, obj=14001826)
    Event_14003950(6, flag=14003828, obj=14001828)
    Event_14003950(7, flag=14003829, obj=14001829)
    Event_14003834(0, obj=14006810)
    Event_14003834(1, obj=14006811)
    Event_14003834(2, obj=14006812)
    Event_14003834(3, obj=14006813)
    Event_14003834(4, obj=14006814)
    Event_14003840(0, character=14000828, left=14001821, left_1=0, left_2=0, flag=14003821, flag_1=0, flag_2=0)
    Event_14003840(1, character=14000829, left=14001822, left_1=0, left_2=0, flag=14003822, flag_1=0, flag_2=0)
    Event_14003840(2, character=14000830, left=14001820, left_1=0, left_2=0, flag=14003820, flag_1=0, flag_2=0)
    Event_14003840(3, character=14000831, left=14001823, left_1=0, left_2=0, flag=14003823, flag_1=0, flag_2=0)
    Event_14003845(0, character=14000828, obj=14001821, obj_1=0, obj_2=0, obj_3=14003821, obj_4=0, obj_5=0)
    Event_14003845(1, character=14000829, obj=14001822, obj_1=0, obj_2=0, obj_3=14003822, obj_4=0, obj_5=0)
    Event_14003845(2, character=14000830, obj=14001820, obj_1=0, obj_2=0, obj_3=14003820, obj_4=0, obj_5=0)
    Event_14003845(3, character=14000831, obj=14001823, obj_1=0, obj_2=0, obj_3=14003823, obj_4=0, obj_5=0)
    Event_14003850(
        0,
        14000832,
        14006810,
        14006811,
        14006812,
        14006813,
        14006814,
        14003834,
        14003835,
        14003836,
        14003837,
        14003838,
        14001810,
        14001811,
        14001812,
        14001813,
        14001814,
        14002815,
        14002816,
        14002817,
        14002818,
        14002819,
    )
    Event_14003850(
        1,
        14000833,
        14006810,
        14006811,
        14006812,
        14006813,
        14006814,
        14003834,
        14003835,
        14003836,
        14003837,
        14003838,
        14001810,
        14001811,
        14001812,
        14001813,
        14001814,
        14002815,
        14002816,
        14002817,
        14002818,
        14002819,
    )
    Event_14003922(0, flag=14003920, character=14000800, character_1=14000840)
    Event_14003923(0, flag=14003920, flag_1=14003921, character=14000840, character_1=14000800)
    Event_14003924(0, flag=14003920, flag_1=14003921, character=14000840)
    Event_14003925(0, flag=14003920, character=14000840)
    Event_14003926(0, character=14000840)
    Event_14003962(0, flag=14003960, character=14000800, character_1=14000845)
    Event_14003963(0, flag=14003960, flag_1=14003961, character=14000845, character_1=14000800)
    Event_14003964(0, flag=14003960, flag_1=14003961, character=14000845)
    Event_14003965(0, flag=14003960, character=14000845)
    Event_14003966(0, character=14000845)
    Event_14003937(
        0,
        flag=14003935,
        character=14000800,
        character_1=14000841,
        character_2=14000842,
        character_3=14000843,
        character_4=14000844
    )
    Event_14003938(
        0,
        flag=14003935,
        flag_1=14003936,
        character=14000841,
        character_1=14000842,
        character_2=14000843,
        character_3=14000844,
        character_4=14000800
    )
    Event_14003939(
        0,
        flag=14003935,
        flag_1=14003936,
        character=14000841,
        character_1=14000842,
        character_2=14000843,
        character_3=14000844
    )
    Event_14003940(0, flag=14003935, character=14000841)
    Event_14003940(1, flag=14003935, character=14000842)
    Event_14003940(2, flag=14003935, character=14000843)
    Event_14003940(3, flag=14003935, character=14000844)
    Event_14003945(0, character=14000841)
    Event_14003945(1, character=14000842)
    Event_14003945(2, character=14000843)
    Event_14003945(3, character=14000844)
    Event_14003972(0, flag=14003970, character=14000800, character_1=14000846)
    Event_14003973(0, flag=14003970, flag_1=14003971, character=14000846, character_1=14000800)
    Event_14003974(0, flag=14003970, flag_1=14003971, character=14000846)
    Event_14003975(0, flag=14003970, character=14000846)
    Event_14003976(0, character=14000846)
    Event_14003977(0, character=14000800, character_1=14005820)
    Event_14003978()
    Event_14003915()
    RunCommonEvent(0, 90005511, args=(14000560, 14001560, 14003560, 257013, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(14000560, 14002550, 14002551), arg_types="III")
    RunCommonEvent(0, 90005511, args=(14000562, 14001562, 14003562, 257013, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(14000562, 14002552, 14002553), arg_types="III")
    RunCommonEvent(0, 90005515, args=(14008550, 14001550), arg_types="II")
    RunCommonEvent(0, 90005515, args=(14008552, 14001552), arg_types="II")
    RunCommonEvent(
        0,
        90005501,
        args=(14000510, 14000511, 0, 14001510, 14001511, 1035461512, 14000512),
        arg_types="IIIIIII",
    )
    Event_14002510()
    RunCommonEvent(
        0,
        90005501,
        args=(14000515, 14000516, 0, 14001515, 14001516, 14001517, 14000517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(14000520, 14000521, 0, 14001520, 14001521, 14001522, 14000522),
        arg_types="IIIIIII",
    )
    Event_14002580()
    RunCommonEvent(0, 90005520, args=(14000546, 14001544, 14000544, 14000545), arg_types="IIII")
    Event_14002498()
    Event_14002590()
    Event_14002592()
    Event_14002594()
    RunCommonEvent(0, 90005300, args=(14000276, 14000276, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(14000277, 14000277, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005525, args=(14000610, 14001610), arg_types="II")
    RunCommonEvent(0, 90005525, args=(14000611, 14001611), arg_types="II")
    RunCommonEvent(0, 90005525, args=(14000612, 14001612), arg_types="II")
    RunCommonEvent(
        0,
        90005605,
        args=(14001660, 60, 37, 46, 0, 1037462650, 14000000, 14002660, 14002661, 14002662, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_14002328(0, character=14000368)
    Event_14002328(1, character=14000369)
    Event_14002328(2, character=14000370)
    Event_14002328(3, character=14000371)
    Event_14002328(4, character=14000372)
    Event_14002328(5, character=14000373)
    Event_14002328(6, character=14000374)
    Event_14002328(7, character=14000375)
    Event_14002328(8, character=14000376)
    Event_14002328(9, character=14000377)
    Event_14002328(10, character=14000378)
    Event_14002328(11, character=14000379)
    Event_14002328(12, character=14000365)
    Event_14002328(13, character=14000366)
    Event_14002328(14, character=14000367)
    Event_14002328(15, character=14000397)
    RunCommonEvent(0, 90005300, args=(14000633, 14000633, 14000005, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(14000634, 14000634, 14000015, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(14000637, 14000637, 14000025, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(14000638, 14000638, 14000035, 0.0, 0), arg_types="IIifi")
    Event_14002491(0, 14000492, 14002492, 15.0, 0.0, 3032)
    Event_14002491(1, 14000493, 14002493, 15.0, 0.0, 3032)
    Event_14002491(2, 14000494, 14002493, 15.0, 0.0, 3032)
    Event_14002490(0, 14000490, 14002490, 0.0, 3032)
    Event_14002490(1, 14000491, 14002491, 0.0, 3032)
    Event_14002490(2, 14000496, 14002496, 0.0, 3032)
    Event_14002490(3, 14000497, 14002496, 1.0, 3032)
    RunCommonEvent(0, 90005300, args=(14000486, 14000486, 40272, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(14000499, 14000499, 14000980, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005780,
        args=(14000850, 14002160, 14002161, 14000730, 20, 14002731, 1034509259, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(14000850, 14002160, 14002161, 14000730), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(14002160, 14002855, 14000730, 14002850, 14002859, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005795,
        args=(7608, 0, 1051369239, 14002141, 14002142, 80609, 9000, 14001705, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=20)
    RunCommonEvent(0, 90005796, args=(7608, 14000713, 5, 14002141), arg_types="IIBI")
    Event_14002145()
    RunCommonEvent(
        0,
        90005795,
        args=(7609, 0, 1034509269, 14002143, 14002144, 80608, 9000, 14001710, 30000),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=30)
    Event_14002155()
    Event_14002165(0, flag=7609, character=14000716, banner_type=7, entity_id=14002151)
    Event_14002495()
    Event_14000700()
    Event_14000701()
    Event_14000702()
    Event_14000703()
    Event_14000710(0, character__obj=14000710, character__obj_1=14000711)
    Event_14000711()
    RunCommonEvent(0, 90005702, args=(14000713, 3463, 3460, 3463), arg_types="IIII")
    RunCommonEvent(0, 90005750, args=(14001711, 4110, 101070, 400107, 400107, 3469, 0), arg_types="IiiIIIi")
    Event_14000712()
    Event_14000713()
    Event_14000714()
    Event_14000720()
    Event_14000730(0, character=14000717)
    RunCommonEvent(0, 90005703, args=(14000717, 3361, 3362, 14009351, 3361, 3360, 3363, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(14000717, 3361, 3360, 14009351, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(14000717, 3363, 3360, 3363), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(14000716, 3363, 3360, 3363), arg_types="IIII")
    Event_14000731()
    Event_14000740(0, character=14000720)
    Event_14000741(0, character=14000721)
    Event_14000742()
    Event_14000750(0, character=14000740, obj=14006700)
    RunCommonEvent(0, 90005750, args=(14001720, 4110, 103600, 400360, 400362, 3806, 0), arg_types="IiiIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(14000700)
    DisableBackread(14000701)
    DisableBackread(14000710)
    DisableBackread(14000711)
    DisableBackread(14000712)
    DisableBackread(14000713)
    DisableBackread(14000715)
    DisableBackread(14000716)
    DisableBackread(14000717)
    DisableBackread(14000720)
    DisableBackread(14000721)
    DisableBackread(14000740)
    DisableObject(14006710)
    Event_14000519()
    RunCommonEvent(0, 90005250, args=(14000200, 14002200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000201, 14002200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(14000210, 30000, 20000, 14002451, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005210, args=(14000228, 30000, 20000, 14002228, 15.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(14000229, 14002228, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005210,
        args=(14000230, 30000, 20000, 14002228, 15.0, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005250, args=(14000231, 14002228, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000221, 14002222, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000233, 14002222, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000250, 14002251, 0.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000251, 14002251, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000252, 14002252, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000260, 14002260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(14000261, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(14000262, 14002260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000263, 14002260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000257, 14002267, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000265, 14002267, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000267, 14002267, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000266, 14002266, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(14000268, 14002268, 3.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(14000269, 14002268, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(14000276, 14002276, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000277, 14002276, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000285, 14002285, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000286, 14002285, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000287, 14002285, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000300, 14002300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(14000305, 30005, 20005, 14002305, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(14000310, 14002310, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(14000311, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(14000312, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(14000315, 30005, 20005, 14002315, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000316, 30000, 20000, 14002315, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000317, 30006, 20006, 14002315, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(14000318, 30000, 20000, 14002315, 0.699999988079071, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(14000319, 30000, 20000, 14002315, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(14000321, 30000, 20000, 14002315, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(14000322, 30000, 20000, 14002315, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(14000323, 14002323, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005200,
        args=(14000325, 30000, 20000, 14002325, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(14000326, 30000, 20000, 14002325, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(14000335, 14002335, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(14000327, 30000, 20000, 14002325, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000328, 30000, 20000, 14002325, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(14000329, 30000, 20000, 14002325, 1.7999999523162842, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(14000340, 30006, 20006, 14002340, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000341, 30000, 20000, 14002340, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000342, 30000, 20000, 14002340, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(14000345, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(14000346, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(14000347, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(14000355, 30000, 20000, 14002355, 5.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(14000356, 30000, 20000, 14002355, 5.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005221, args=(14000360, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(14000361, 30006, 20006, 14002361, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(14000362, 30006, 20006, 14002361, 1.399999976158142, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005251, args=(14000383, 16.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(14000388, 14002345, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(14000392, 30000, 20000, 14002355, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(14000394, 30006, 20006, 14002361, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000396, 30001, 20001, 14002396, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000398, 30001, 20001, 14002396, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000399, 30001, 20001, 14002396, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(14000290, 14002345, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(14000291, 30001, 20001, 14002345, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(14000297, 30001, 20001, 14002345, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(14000299, 30001, 20001, 14002345, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005221, args=(14000417, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(14000418, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(14000419, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(14000420, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(14000421, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(14000438, 30001, 20001, 14002267, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000439, 30001, 20001, 14002267, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(14000440, 30001, 20001, 14002267, 1.7999999523162842, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005221, args=(14000441, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005250, args=(14000443, 14002267, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(14000442, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(14000600, 30000, 20000, 14002228, 10.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000410, 30000, 20000, 14002410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000411, 30000, 20000, 14002410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000412, 30000, 20000, 14002410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000413, 30000, 20000, 14002410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000414, 30000, 20000, 14002410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000415, 30000, 20000, 14002410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000400, 30000, 20000, 14002252, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000402, 30000, 20000, 14002252, 6.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000403, 30000, 20000, 14002252, 7.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000405, 30000, 20000, 14002252, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000406, 30000, 20000, 14002252, 2.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000635, 30001, 20001, 14002635, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000636, 30001, 20001, 14002636, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000450, 30010, 20010, 14002450, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000451, 30010, 20010, 14002451, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000453, 30010, 20010, 14002451, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000452, 30010, 20010, 14002452, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(14000461, 14002461, 20.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(14000474, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(14000477, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005200, args=(14000472, 30010, 20010, 14002472, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(14000473, 30010, 20010, 14002472, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(14000480, 14002487, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000481, 14002487, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(14000495, 30000, 20001, 14002495, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(14000483, 14002396, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000484, 14002396, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000675, 14002675, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000295, 14002276, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000293, 14002293, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000294, 14002294, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(14000499, 14002499, 0.0, -1), arg_types="IIfi")


@NeverRestart(14002080)
def Event_14002080():
    """Event 14002080"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=14002080)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 14307)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetRespawnPoint(respawn_point=16002080)
    SaveRequest()
    EnableFlag(16000540)


@RestartOnRest(14002145)
def Event_14002145():
    """Event 14002145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(14000713)
    EnableBackread(14000715)
    SetTeamType(14000713, TeamType.Human)
    SetTeamType(14000715, TeamType.Enemy)
    DeleteObjectVFX(14006710)
    CreateObjectVFX(14006710, vfx_id=200, model_point=806700)


@RestartOnRest(14002155)
def Event_14002155():
    """Event 14002155"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=30,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(14000716)
    EnableBackread(14000712)
    SetTeamType(14000716, TeamType.Enemy)
    SetTeamType(14000712, TeamType.Human)
    DeleteObjectVFX(14006700)
    CreateObjectVFX(14006700, vfx_id=200, model_point=806700)


@RestartOnRest(14002165)
def Event_14002165(_, flag: uint, character: uint, banner_type: uchar, entity_id: uint):
    """Event 14002165"""
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    EndIfFlagEnabled(flag)
    IfCharacterDrawGroupEnabled(AND_1, character=character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayBanner(banner_type)
    SkipLinesIfUnsignedEqual(1, left=entity_id, right=0)
    Unknown_2003_77(entity_id=entity_id)
    AddSpecialEffect(20000, 4822)
    Unknown_2003_74(unk_0_4=1)


@RestartOnRest(14002580)
def Event_14002580():
    """Event 14002580"""
    RegisterLadder(start_climbing_flag=14000530, stop_climbing_flag=14000531, obj=14001530)
    RegisterLadder(start_climbing_flag=14000532, stop_climbing_flag=14000533, obj=14001532)
    RegisterLadder(start_climbing_flag=14000534, stop_climbing_flag=14000535, obj=14001534)
    RegisterLadder(start_climbing_flag=14000536, stop_climbing_flag=14000537, obj=14001536)
    RegisterLadder(start_climbing_flag=14000538, stop_climbing_flag=14000539, obj=14001538)
    RegisterLadder(start_climbing_flag=14000540, stop_climbing_flag=14000541, obj=14001540)
    RegisterLadder(start_climbing_flag=14000542, stop_climbing_flag=14000543, obj=14001542)


@NeverRestart(14002510)
def Event_14002510():
    """Event 14002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            14000510,
            14001511,
            0,
            14001510,
            14001511,
            14003511,
            1035461512,
            1035463512,
            14002511,
            14002512,
            14000512,
            14000513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            14000515,
            14000516,
            0,
            14001515,
            14001516,
            14003516,
            14001517,
            14003517,
            14002516,
            14002517,
            14000517,
            14000518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            14000520,
            14000521,
            0,
            14001520,
            14001521,
            14003521,
            14001522,
            14003522,
            14002521,
            14002522,
            14000522,
            14000523,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(14000519)
def Event_14000519():
    """Event 14000519"""
    EndIfThisEventSlotFlagEnabled()
    DisableThisSlotFlag()


@RestartOnRest(14002498)
def Event_14002498():
    """Event 14002498"""
    GotoIfFlagEnabled(Label.L0, flag=14000546)
    EnableNavmeshType(navmesh_id=14002498, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(MAIN, 14000546)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=14002498, navmesh_type=NavmeshType.Solid)
    End()


@RestartOnRest(14003500)
def Event_14003500(_, region: uint, flag: uint):
    """Event 14003500"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(PLAYER, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterOutsideRegion(AND_3, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Wait(0.10000000149011612)
    CancelSpecialEffect(PLAYER, 9621)
    Restart()


@RestartOnRest(14002590)
def Event_14002590():
    """Event 14002590"""
    EnableNetworkSync()
    GotoIfFlagRangeAllDisabled(Label.L0, flag_range=(14000276, 14000277))
    DisableObject(14001590)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(14001590)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfFlagEnabled(AND_1, 14002595)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagRangeAllEnabled(flag_range=(14000276, 14000277))
    EnableObject(14001590)
    ForceAnimation(14001590, 1, unknown2=1.0)
    CreateTemporaryVFX(vfx_id=814630, anchor_entity=14001591, model_point=100, anchor_type=CoordEntityType.Object)
    SkipLinesIfFlagDisabled(1, 50)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500000,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500010,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500020,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500030,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500040,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500050,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500060,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    CreateHazard(
        obj_flag=14000590,
        obj=14001590,
        model_point=200,
        behavior_param_id=802500070,
        target_type=DamageTargetType.Character,
        radius=3.799999952316284,
        life=10.0,
        repetition_time=0.0,
    )
    Wait(10.0)
    DisableObject(14001590)
    Restart()


@RestartOnRest(14002592)
def Event_14002592():
    """Event 14002592"""
    DeleteObjectVFX(14001592)
    CreateObjectVFX(14001592, vfx_id=100, model_point=814631)


@RestartOnRest(14002594)
def Event_14002594():
    """Event 14002594"""
    EndIfFlagRangeAllEnabled(flag_range=(14000276, 14000277))
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=14002590)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(14002595)
    Wait(10.0)
    DisableNetworkFlag(14002595)
    Restart()


@RestartOnRest(14002650)
def Event_14002650(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 14002650"""
    EndIfTryingToCreateSession()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfLeavingSession(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(14002328)
def Event_14002328(_, character: uint):
    """Event 14002328"""
    Kill(character)


@RestartOnRest(14002360)
def Event_14002360(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    attacked_entity: uint,
    attacked_entity_1: uint,
    attacked_entity_2: uint,
):
    """Event 14002360"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_3, attacked_entity=attacked_entity, attacker=0)
    IfAttackedWithDamageType(OR_3, attacked_entity=attacked_entity_1, attacker=0)
    IfAttackedWithDamageType(OR_3, attacked_entity=attacked_entity_2, attacker=0)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(14002490)
def Event_14002490(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 14002490"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    DisableGravity(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    EnableAI(character)
    EnableGravity(character)
    Wait(2.799999952316284)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(14002491)
def Event_14002491(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 14002491"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    DisableGravity(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    EnableAI(character)
    EnableGravity(character)
    Wait(2.799999952316284)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(14002495)
def Event_14002495():
    """Event 14002495"""
    DisableNetworkSync()
    IfFlagEnabled(OR_1, 14002140)
    IfFlagEnabled(OR_1, 14002150)
    IfConditionTrue(MAIN, input_condition=OR_1)
    AddSpecialEffect(14000106, 9531)
    IfFlagDisabled(AND_1, 14002140)
    IfFlagDisabled(AND_1, 14002150)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(14000106, 9532)
    Wait(1.0)
    Restart()


@NeverRestart(14002606)
def Event_14002606():
    """Event 14002606"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=14000676)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(AND_1, obj_act_id=14003606)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.10000000149011612)
    DisplayDialog(text=208199, anchor_entity=14001606)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(14001606, obj_act_id=199630)
    End()


@RestartOnRest(14002665)
def Event_14002665():
    """Event 14002665"""
    DisableObject(14006600)


@RestartOnRest(14002689)
def Event_14002689():
    """Event 14002689"""
    GotoIfFlagEnabled(Label.L0, flag=14000801)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=14002689)
    UnknownMap_11(unk_0_4=500, unk_4_8=0.0)
    Wait(0.10000000149011612)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    UnknownMap_12(unk_0_4=0.0)
    End()


@RestartOnRest(14002800)
def Event_14002800():
    """Event 14002800"""
    GotoIfFlagDisabled(Label.L1, flag=14000804)
    EndOfAnimation(obj=14001841, animation_id=0)
    EndOfAnimation(obj=14001842, animation_id=0)
    EndOfAnimation(obj=14001846, animation_id=0)
    MoveRemains(source_region=14002840, destination_region=14002843)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L0, flag=14000800)
    IfHealthValueLessThanOrEqual(MAIN, 14000800, value=0)
    Wait(4.0)
    PlaySoundEffect(14008000, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 14000800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 14000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Kill(14005810)
    KillBossAndDisplayBanner(character=14000800, banner_type=BannerType.HollowArenaWin)
    EnableNetworkFlag(14000800)
    EnableFlag(9118)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61118)
    SetRespawnPoint(respawn_point=14003900)
    SaveRequest()
    Wait(8.0)
    EndIfPlayerNotInOwnWorld()

    # --- Label 0 --- #
    DefineLabel(0)
    WarpToMap(game_map=RAYA_LUCARIA, player_start=14003900)
    SetRespawnPoint(respawn_point=14003900)
    SaveRequest()
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    EnableObjectActivation(14001606, obj_act_id=199630)
    MoveRemains(source_region=14002840, destination_region=14002843)
    EndOfAnimation(obj=14001810, animation_id=0)
    EndOfAnimation(obj=14001811, animation_id=0)
    EndOfAnimation(obj=14001812, animation_id=0)
    EndOfAnimation(obj=14001813, animation_id=0)
    EndOfAnimation(obj=14001814, animation_id=0)
    EndOfAnimation(obj=14001841, animation_id=0)
    EndOfAnimation(obj=14001842, animation_id=0)
    EndOfAnimation(obj=14001846, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    EnableFlag(14000804)
    SetBackreadStateAlternate(35000, False)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)


@RestartOnRest(14002810)
def Event_14002810():
    """Event 14002810"""
    GotoIfFlagDisabled(Label.L0, flag=14000800)
    DisableCharacter(14005800)
    DisableAnimations(14005800)
    Kill(14005800)
    EnableCharacter(14000700)
    EnableAnimations(14000700)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(14005800)
    DisableCharacter(14000700)
    DisableAnimations(14000700)
    DisableCharacter(14000800)
    DisableAnimations(14000800)
    DisableObjectActivation(14001606, obj_act_id=199630)
    MoveRemains(source_region=14002840, destination_region=14002841)
    GotoIfFlagEnabled(Label.L1, flag=14000801)
    DisableCharacter(14005800)
    DisableAnimations(14005800)
    EndOfAnimation(obj=14001810, animation_id=10)
    EndOfAnimation(obj=14001811, animation_id=10)
    EndOfAnimation(obj=14001812, animation_id=10)
    EndOfAnimation(obj=14001813, animation_id=10)
    EndOfAnimation(obj=14001814, animation_id=10)
    EndOfAnimation(obj=14001841, animation_id=1)
    EndOfAnimation(obj=14001842, animation_id=1)
    EndOfAnimation(obj=14001846, animation_id=1)
    DeleteVFX(14002600, erase_root_only=False)
    DeleteVFX(14002601, erase_root_only=False)
    DeleteVFX(14002602, erase_root_only=False)
    DeleteVFX(14002603, erase_root_only=False)
    DeleteVFX(14002604, erase_root_only=False)
    DeleteVFX(14002605, erase_root_only=False)
    DeleteVFX(14002606, erase_root_only=False)
    DeleteVFX(14002607, erase_root_only=False)
    DeleteVFX(14002608, erase_root_only=False)
    DeleteVFX(14002609, erase_root_only=False)
    DeleteVFX(14002610, erase_root_only=False)
    DeleteVFX(14002611, erase_root_only=False)
    DeleteVFX(14002612, erase_root_only=False)
    DeleteVFX(14002613, erase_root_only=False)
    DeleteVFX(14002614, erase_root_only=False)
    DeleteVFX(14002615, erase_root_only=False)
    DeleteVFX(14002616, erase_root_only=False)
    DeleteVFX(14002617, erase_root_only=False)
    DeleteVFX(14002618, erase_root_only=False)
    DeleteVFX(14002619, erase_root_only=False)
    DeleteVFX(14002620, erase_root_only=False)
    DeleteVFX(14002621, erase_root_only=False)
    DeleteVFX(14002622, erase_root_only=False)
    DeleteVFX(14002623, erase_root_only=False)
    DeleteVFX(14002624, erase_root_only=False)
    DeleteVFX(14002625, erase_root_only=False)
    DeleteVFX(14002626, erase_root_only=False)
    DeleteVFX(14002627, erase_root_only=False)
    DeleteVFX(14002628, erase_root_only=False)
    DeleteVFX(14002629, erase_root_only=False)
    DeleteVFX(14002630, erase_root_only=False)
    DeleteVFX(14002631, erase_root_only=False)
    DeleteVFX(14002680, erase_root_only=False)
    DeleteVFX(14002681, erase_root_only=False)
    DeleteVFX(14002682, erase_root_only=False)
    DeleteVFX(14002683, erase_root_only=False)
    DeleteVFX(14002684, erase_root_only=False)
    DeleteVFX(14002685, erase_root_only=False)
    DeleteVFX(14002686, erase_root_only=False)
    DeleteVFX(14002687, erase_root_only=False)
    Unknown_2004_73(entity=14000810, unk_4_8=0)
    Unknown_2004_73(entity=14000811, unk_4_8=0)
    Unknown_2004_73(entity=14000812, unk_4_8=0)
    Unknown_2004_73(entity=14000813, unk_4_8=0)
    Unknown_2004_73(entity=14000814, unk_4_8=0)
    Unknown_2004_73(entity=14000815, unk_4_8=0)
    Unknown_2004_73(entity=14000816, unk_4_8=0)
    Unknown_2004_73(entity=14000817, unk_4_8=0)
    Unknown_2004_73(entity=14000818, unk_4_8=0)
    Unknown_2004_73(entity=14000819, unk_4_8=0)
    Unknown_2004_73(entity=14000820, unk_4_8=0)
    Unknown_2004_73(entity=14000821, unk_4_8=0)
    Unknown_2004_73(entity=14000822, unk_4_8=0)
    Unknown_2004_73(entity=14000823, unk_4_8=0)
    Unknown_2004_73(entity=14000824, unk_4_8=0)
    Unknown_2004_73(entity=14000825, unk_4_8=0)
    Unknown_2004_73(entity=14000826, unk_4_8=0)
    Unknown_2004_73(entity=14000827, unk_4_8=0)
    Unknown_2004_73(entity=14000828, unk_4_8=0)
    Unknown_2004_73(entity=14000829, unk_4_8=0)
    Unknown_2004_73(entity=14000830, unk_4_8=0)
    Unknown_2004_73(entity=14000831, unk_4_8=0)
    Unknown_2004_73(entity=14000832, unk_4_8=0)
    Unknown_2004_73(entity=14000833, unk_4_8=0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=14002801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=14000801, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=14000000,
        cutscene_flags=0,
        move_to_region=14002802,
        map_base_id=14000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(14000000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(14000801)
    EnableCharacter(14000801)
    EnableAnimations(14000801)
    EnableCharacter(14005810)
    EnableAnimations(14005810)
    EndOfAnimation(obj=14001810, animation_id=0)
    EndOfAnimation(obj=14001811, animation_id=0)
    EndOfAnimation(obj=14001812, animation_id=0)
    EndOfAnimation(obj=14001813, animation_id=0)
    EndOfAnimation(obj=14001814, animation_id=0)
    ForceAnimation(14001814, 0, loop=True, unknown2=1.0)
    EndOfAnimation(obj=14001841, animation_id=0)
    EndOfAnimation(obj=14001842, animation_id=0)
    EndOfAnimation(obj=14001846, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=14001810, animation_id=0)
    EndOfAnimation(obj=14001811, animation_id=0)
    EndOfAnimation(obj=14001812, animation_id=0)
    EndOfAnimation(obj=14001813, animation_id=0)
    EndOfAnimation(obj=14001814, animation_id=0)
    EndOfAnimation(obj=14001841, animation_id=0)
    EndOfAnimation(obj=14001842, animation_id=0)
    EndOfAnimation(obj=14001846, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    IfFlagEnabled(AND_2, 14002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=14002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(14005800)
    SetNetworkUpdateRate(14000801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(14005810, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)
    EnableBossHealthBar(14000801, name=902030000)


@RestartOnRest(14002811)
def Event_14002811():
    """Event 14002811"""
    EndIfFlagEnabled(14000800)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterDead(AND_1, 14000801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(14002802)
    Unknown_2004_73(entity=14000800, unk_4_8=0)
    EndOfAnimation(obj=14001810, animation_id=10)
    EndOfAnimation(obj=14001811, animation_id=10)
    EndOfAnimation(obj=14001812, animation_id=10)
    EndOfAnimation(obj=14001813, animation_id=10)
    EndOfAnimation(obj=14001814, animation_id=10)
    EndOfAnimation(obj=14001841, animation_id=1)
    EndOfAnimation(obj=14001842, animation_id=1)
    EndOfAnimation(obj=14001846, animation_id=1)
    DeleteVFX(14002600, erase_root_only=False)
    DeleteVFX(14002601, erase_root_only=False)
    DeleteVFX(14002602, erase_root_only=False)
    DeleteVFX(14002603, erase_root_only=False)
    DeleteVFX(14002604, erase_root_only=False)
    DeleteVFX(14002605, erase_root_only=False)
    DeleteVFX(14002606, erase_root_only=False)
    DeleteVFX(14002607, erase_root_only=False)
    DeleteVFX(14002608, erase_root_only=False)
    DeleteVFX(14002609, erase_root_only=False)
    DeleteVFX(14002610, erase_root_only=False)
    DeleteVFX(14002611, erase_root_only=False)
    DeleteVFX(14002612, erase_root_only=False)
    DeleteVFX(14002613, erase_root_only=False)
    DeleteVFX(14002614, erase_root_only=False)
    DeleteVFX(14002615, erase_root_only=False)
    DeleteVFX(14002616, erase_root_only=False)
    DeleteVFX(14002617, erase_root_only=False)
    DeleteVFX(14002618, erase_root_only=False)
    DeleteVFX(14002619, erase_root_only=False)
    DeleteVFX(14002620, erase_root_only=False)
    DeleteVFX(14002621, erase_root_only=False)
    DeleteVFX(14002622, erase_root_only=False)
    DeleteVFX(14002623, erase_root_only=False)
    DeleteVFX(14002624, erase_root_only=False)
    DeleteVFX(14002625, erase_root_only=False)
    DeleteVFX(14002626, erase_root_only=False)
    DeleteVFX(14002627, erase_root_only=False)
    DeleteVFX(14002628, erase_root_only=False)
    DeleteVFX(14002629, erase_root_only=False)
    DeleteVFX(14002630, erase_root_only=False)
    DeleteVFX(14002631, erase_root_only=False)
    DeleteVFX(14002680, erase_root_only=False)
    DeleteVFX(14002681, erase_root_only=False)
    DeleteVFX(14002682, erase_root_only=False)
    DeleteVFX(14002683, erase_root_only=False)
    DeleteVFX(14002684, erase_root_only=False)
    DeleteVFX(14002685, erase_root_only=False)
    DeleteVFX(14002686, erase_root_only=False)
    DeleteVFX(14002687, erase_root_only=False)
    Unknown_2003_76(
        unk_0_4=917760,
        unk_4_8=0,
        unk_8_12=42.02000045776367,
        unk_12_16=154.1999969482422,
        unk_16_20=-23.889999389648438,
    )
    SetBackreadStateAlternate(14000800, True)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=14000010,
        cutscene_flags=0,
        move_to_region=14002803,
        map_base_id=14000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    UnknownCutscene_11(
        cutscene_id=14000010,
        cutscene_flags=0,
        move_to_region=14002806,
        map_base_id=14000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=4.960000038146973, unknown2=-117.80000305175781)
    EnableFlag(14002803)
    SetBackreadStateAlternate(35000, True)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)
    Move(35000, destination=14002806, destination_type=CoordEntityType.Region, copy_draw_parent=14000800)
    Move(14000106, destination=14002806, destination_type=CoordEntityType.Region, copy_draw_parent=14000800)
    SetCharacterTalkRange(character=14000106, distance=200.0)
    Unknown_2003_68(unknown1=0, unknown2=-1.0, unknown3=0)
    EnableCharacter(14000800)
    EnableAnimations(14000800)
    ForceAnimation(14000800, 20005, unknown2=1.0)
    EnableBossHealthBar(14000800, name=902030001)
    SetNetworkUpdateRate(14000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFramesAfterCutscene(frames=1)
    AttachObjectToCharacter(character=14000106, model_point=10, obj=14001106)


@RestartOnRest(140028121)
def Event_140028121():
    """Event 140028121"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(14000800)
    IfCharacterHasSpecialEffect(OR_1, 14000801, 14350)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(14002707)
    IfFlagDisabled(AND_1, 14002707)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 14000801, 14350)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Restart()


@RestartOnRest(140028122)
def Event_140028122(_, character: uint, special_effect: int, special_effect_1: int):
    """Event 140028122"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(character)
    IfCharacterHasSpecialEffect(OR_1, character, special_effect)
    IfCharacterHasSpecialEffect(OR_1, character, special_effect_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(14002720)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(14002722)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(AND_1, flag_range=(14002720, 14002723))
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, special_effect)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, special_effect_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Restart()


@RestartOnRest(14002849)
def Event_14002849():
    """Event 14002849"""
    RunCommonEvent(
        0,
        9005800,
        args=(14000800, 14001800, 14002800, 14002805, 14005800, 10000, 14000801, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(14000800, 14001800, 14002800, 14002805, 14002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(14000800, 14001800, 3, 14000801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(14000800, 203000, 14002805, 14002806, 0, 14002803, 1, 0), arg_types="IiIIIIii")


@RestartOnRest(14002850)
def Event_14002850():
    """Event 14002850"""
    EndIfFlagEnabled(14000850)
    IfHealthLessThanOrEqual(MAIN, 14000850, value=0.0)
    Wait(2.0)
    PlaySoundEffect(14000850, 77777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 14000850)
    KillBossAndDisplayBanner(character=14000850, banner_type=BannerType.Unknown)
    EnableFlag(14000850)
    EnableFlag(9117)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61117)


@RestartOnRest(14002860)
def Event_14002860():
    """Event 14002860"""
    GotoIfFlagDisabled(Label.L0, flag=14000850)
    DisableCharacter(14000850)
    DisableAnimations(14000850)
    Kill(14000850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(14000850)
    GotoIfFlagEnabled(Label.L1, flag=14000851)
    ForceAnimation(14000850, 30002, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 14002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=14002850)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableNetworkFlag(14000851)
    ForceAnimation(14000850, 20002, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(14000850, destination=14002856, destination_type=CoordEntityType.Region, short_move=True)
    IfFlagEnabled(AND_2, 14002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=14002850)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(14000850)
    SetNetworkUpdateRate(14005850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(14000850, name=903181000)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(14005850, authority_level=UpdateAuthority.Unknown8192)


@RestartOnRest(14002889)
def Event_14002889():
    """Event 14002889"""
    RunCommonEvent(
        0,
        9005800,
        args=(14000850, 14001850, 14002850, 14002855, 14005850, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(14000850, 14001850, 14002850, 14002855, 14002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(14000850, 14001850, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005813, args=(14000850, 14001851, 3, 14000851, 806760), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(14000850, 921400, 14002855, 14002856, 0, 14000852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(14002820)
def Event_14002820(_, character: uint):
    """Event 14002820"""
    DisableAI(character)
    IfCharacterInsideRegion(AND_1, character=20000, region=14002812)
    IfHasAIStatus(AND_1, 14000810, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAI(character)
    DisableObject(14001800)
    DisableObject(14006800)
    SetNetworkUpdateRate(14000801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(character)
    IfFlagEnabled(MAIN, 14002810)
    WaitFrames(frames=1)
    DisableBossHealthBar(14000801)
    EnableBossHealthBar(character)


@RestartOnRest(14002821)
def Event_14002821(_, character: uint):
    """Event 14002821"""
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=character, radius=30.0)
    IfHealthEqual(OR_1, character, value=1.0, target_comparison_type=ComparisonType.NotEqual)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNetworkUpdateRate(14000801, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAI(character)
    EnableBossHealthBar(character)


@RestartOnRest(14002822)
def Event_14002822(_, character: uint):
    """Event 14002822"""
    IfCharacterDead(MAIN, character)
    Wait(1.5)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    EnableFlag(14000899)


@RestartOnRest(14003801)
def Event_14003801(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
    character_10: uint,
    character_11: uint,
    character_12: uint,
    character_13: uint,
    character_14: uint,
    character_15: uint,
    character_16: uint,
    character_17: uint,
    character_18: uint,
    character_19: uint,
    character_20: uint,
    character_21: uint,
    character_22: uint,
    character_23: uint,
    character_24: uint,
    character_25: uint,
):
    """Event 14003801"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_10, 14002805)
    AwaitConditionTrue(AND_10)
    IfFlagEnabled(AND_1, flag)
    IfCharacterHasSpecialEffect(AND_1, character_1, 14394, target_comparison_type=ComparisonType.LessThan)
    IfCharacterHasSpecialEffect(OR_1, character, 14357)
    IfCharacterHasSpecialEffect(OR_1, character, 14361)
    IfCharacterHasSpecialEffect(OR_1, character, 14368)
    IfCharacterHasSpecialEffect(OR_1, character, 14369)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(14003802)
    DisableFlag(14003803)
    DisableFlag(14003804)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(14003802, 14003804))
    SkipLinesIfFlagEnabled(2, 14003804)
    GotoIfFlagEnabled(Label.L0, flag=14003802)
    GotoIfFlagEnabled(Label.L1, flag=14003803)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_2, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_2, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14394)
    ReplanAI(character_2)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_3, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_3, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14394)
    ReplanAI(character_3)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_4, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_4, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14394)
    ReplanAI(character_4)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_5, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_5, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14394)
    ReplanAI(character_5)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_6, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_6, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14394)
    ReplanAI(character_6)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_7, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_7, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14394)
    ReplanAI(character_7)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_8, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_8, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14394)
    ReplanAI(character_8)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_9, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_9, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_9, special_effect=14393)
    AddSpecialEffect(character_9, 14394)
    ReplanAI(character_9)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_10, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_10, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_10, special_effect=14393)
    AddSpecialEffect(character_10, 14394)
    ReplanAI(character_10)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_11, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_11, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_11, special_effect=14393)
    AddSpecialEffect(character_11, 14394)
    ReplanAI(character_11)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_12, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_12, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_12, special_effect=14393)
    AddSpecialEffect(character_12, 14394)
    ReplanAI(character_12)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_13, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_13, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_13, special_effect=14393)
    AddSpecialEffect(character_13, 14394)
    ReplanAI(character_13)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_14, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_14, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_14, special_effect=14393)
    AddSpecialEffect(character_14, 14394)
    ReplanAI(character_14)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_15, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_15, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_15, special_effect=14393)
    AddSpecialEffect(character_15, 14394)
    ReplanAI(character_15)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_16, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_16, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_16, special_effect=14393)
    AddSpecialEffect(character_16, 14394)
    ReplanAI(character_16)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_17, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_17, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_17, special_effect=14393)
    AddSpecialEffect(character_17, 14394)
    ReplanAI(character_17)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_18, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_18, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_18, special_effect=14393)
    AddSpecialEffect(character_18, 14394)
    ReplanAI(character_18)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_19, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_19, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_19, special_effect=14393)
    AddSpecialEffect(character_19, 14394)
    ReplanAI(character_19)
    Restart()
    Goto(Label.L10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_20, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_20, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_20, special_effect=14393)
    AddSpecialEffect(character_20, 14394)
    ReplanAI(character_20)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_21, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_21, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_21, special_effect=14393)
    AddSpecialEffect(character_21, 14394)
    ReplanAI(character_21)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_22, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_22, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_22, special_effect=14393)
    AddSpecialEffect(character_22, 14394)
    ReplanAI(character_22)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_23, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_23, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_23, special_effect=14393)
    AddSpecialEffect(character_23, 14394)
    ReplanAI(character_23)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_24, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_24, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_24, special_effect=14393)
    AddSpecialEffect(character_24, 14394)
    ReplanAI(character_24)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_25, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_25, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_25, special_effect=14393)
    AddSpecialEffect(character_25, 14394)
    ReplanAI(character_25)
    Restart()


@RestartOnRest(14003805)
def Event_14003805(_, flag: uint, character: uint, character_1: uint, character_2: uint):
    """Event 14003805"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, 14356)
    IfCharacterHasSpecialEffect(AND_1, character_1, 14396, target_count=0.0)
    IfCharacterHasSpecialEffect(AND_1, character_1, 14394, target_count=0.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=14369)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=14368)
    RestartIfCharacterDoesNotHaveSpecialEffect(character=character, special_effect=14361)
    AddSpecialEffect(character, 14368)
    IfCharacterHasSpecialEffect(OR_15, character_1, 14394, target_comparison_type=ComparisonType.GreaterThanOrEqual)
    AwaitConditionTrue(OR_15)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 14369)
    IfCharacterHasSpecialEffect(OR_15, character_1, 14394, target_comparison_type=ComparisonType.GreaterThanOrEqual)
    AwaitConditionTrue(OR_15)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 14357)
    AddSpecialEffect(character_1, 14384)
    AddSpecialEffect(character, 14578)
    ReplanAI(character)
    EnableFlag(14003816)
    DisableFlag(14003800)
    AddSpecialEffect(character_1, 14388)
    AddSpecialEffect(character_2, 14388)
    Restart()


@RestartOnRest(14003807)
def Event_14003807(_, character: uint, character_1: uint):
    """Event 14003807"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, 14357)
    IfCharacterHasSpecialEffect(AND_1, character, 14358)
    IfCharacterHasSpecialEffect(AND_1, character_1, 14396, target_comparison_type=ComparisonType.GreaterThanOrEqual)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14356)
    AddSpecialEffect(character_1, 14589)
    DisableFlag(14003816)
    Restart()


@RestartOnRest(14003808)
def Event_14003808(_, flag: uint, character: uint):
    """Event 14003808"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, 14358)
    IfCharacterHasSpecialEffect(AND_1, character, 14357)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(10.0)
    EnableFlag(flag)
    IfCharacterHasSpecialEffect(OR_15, character, 14356)
    AwaitConditionFalse(OR_15)
    Restart()


@RestartOnRest(14003809)
def Event_14003809(_, flag: uint, character: uint):
    """Event 14003809"""
    IfCharacterHasSpecialEffect(AND_1, character, 14350)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(3.0)
    DisableFlag(flag)
    Restart()


@RestartOnRest(14003811)
def Event_14003811(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
    character_10: uint,
    character_11: uint,
    character_12: uint,
    character_13: uint,
    character_14: uint,
    character_15: uint,
    character_16: uint,
    character_17: uint,
    character_18: uint,
    character_19: uint,
    character_20: uint,
    character_21: uint,
    character_22: uint,
    character_23: uint,
    character_24: uint,
):
    """Event 14003811"""
    IfCharacterHasSpecialEffect(
        OR_1,
        character,
        14351,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    )
    SkipLinesIfConditionFalse(2, OR_1)
    DisableFlag(flag)
    Restart()
    IfFlagEnabled(AND_1, flag)
    IfCharacterHasSpecialEffect(
        AND_1,
        character,
        14351,
        target_comparison_type=ComparisonType.LessThan,
        target_count=5.0,
    )
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(14003802)
    DisableFlag(14003803)
    DisableFlag(14003804)
    EnableRandomFlagInRange(flag_range=(14003802, 14003804))
    SkipLinesIfFlagEnabled(2, 14003804)
    GotoIfFlagEnabled(Label.L0, flag=14003802)
    GotoIfFlagEnabled(Label.L1, flag=14003803)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_1, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_1, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_1, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_1, special_effect=14393)
    AddSpecialEffect(character_1, 14351)
    ReplanAI(character_1)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_2, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_2, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_2, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14351)
    ReplanAI(character_2)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_3, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_3, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_3, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14351)
    ReplanAI(character_3)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_4, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_4, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_4, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14351)
    ReplanAI(character_4)
    SetNetworkUpdateRate(character_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_5, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_5, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_5, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14351)
    ReplanAI(character_5)
    SetNetworkUpdateRate(character_5, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_6, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_6, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_6, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14351)
    ReplanAI(character_6)
    SetNetworkUpdateRate(character_6, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_7, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_7, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_7, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14351)
    ReplanAI(character_7)
    SetNetworkUpdateRate(character_7, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_8, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_8, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_8, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14351)
    ReplanAI(character_8)
    SetNetworkUpdateRate(character_8, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_9, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_9, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_9, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_9, special_effect=14393)
    AddSpecialEffect(character_9, 14351)
    ReplanAI(character_9)
    SetNetworkUpdateRate(character_9, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_10, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_10, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_10, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_10, special_effect=14393)
    AddSpecialEffect(character_10, 14351)
    ReplanAI(character_10)
    SetNetworkUpdateRate(character_10, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_11, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_11, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_11, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_11, special_effect=14393)
    AddSpecialEffect(character_11, 14351)
    ReplanAI(character_11)
    SetNetworkUpdateRate(character_11, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_12, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_12, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_12, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_12, special_effect=14393)
    AddSpecialEffect(character_12, 14351)
    ReplanAI(character_12)
    SetNetworkUpdateRate(character_12, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_13, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_13, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_13, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_13, special_effect=14393)
    AddSpecialEffect(character_13, 14351)
    ReplanAI(character_13)
    SetNetworkUpdateRate(character_13, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_14, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_14, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_14, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_14, special_effect=14393)
    AddSpecialEffect(character_14, 14351)
    ReplanAI(character_14)
    SetNetworkUpdateRate(character_14, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_15, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_15, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_15, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_15, special_effect=14393)
    AddSpecialEffect(character_15, 14351)
    ReplanAI(character_15)
    SetNetworkUpdateRate(character_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_16, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_16, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_16, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_16, special_effect=14393)
    AddSpecialEffect(character_16, 14351)
    ReplanAI(character_16)
    SetNetworkUpdateRate(character_16, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_17, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_17, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_17, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_17, special_effect=14393)
    AddSpecialEffect(character_17, 14351)
    ReplanAI(character_17)
    SetNetworkUpdateRate(character_17, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_18, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_18, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_18, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_18, special_effect=14393)
    AddSpecialEffect(character_18, 14351)
    ReplanAI(character_18)
    SetNetworkUpdateRate(character_18, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    Goto(Label.L10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_19, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_19, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_19, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_19, special_effect=14393)
    AddSpecialEffect(character_19, 14351)
    ReplanAI(character_19)
    SetNetworkUpdateRate(character_19, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_20, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_20, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_20, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_20, special_effect=14393)
    AddSpecialEffect(character_20, 14351)
    ReplanAI(character_20)
    SetNetworkUpdateRate(character_20, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_21, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_21, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_21, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_21, special_effect=14393)
    AddSpecialEffect(character_21, 14351)
    ReplanAI(character_21)
    SetNetworkUpdateRate(character_21, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_22, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_22, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_22, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_22, special_effect=14393)
    AddSpecialEffect(character_22, 14351)
    ReplanAI(character_22)
    SetNetworkUpdateRate(character_22, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=character_23, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=character_23, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_23, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character_23, special_effect=14393)
    AddSpecialEffect(character_23, 14351)
    ReplanAI(character_23)
    SetNetworkUpdateRate(character_23, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=6, character=character_24, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=character_24, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_24, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_24, special_effect=14393)
    AddSpecialEffect(character_24, 14351)
    ReplanAI(character_24)
    SetNetworkUpdateRate(character_24, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(14003814)
def Event_14003814(_, destination: uint, character: uint):
    """Event 14003814"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    DisableGravity(character)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Character,
        model_point=20,
        short_move=True,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(14003815)
def Event_14003815(_, character: uint, anchor_entity: uint):
    """Event 14003815"""
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    TriggerAISound(ai_sound_param_id=203000, anchor_entity=anchor_entity, unk_8_12=2)
    Wait(5.0)
    Restart()


@RestartOnRest(14003817)
def Event_14003817(_, character: uint):
    """Event 14003817"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 14003816)
    IfUnknownCharacterCondition_19(AND_1, character=character, unk_8_12=14385, unk_12_13=1, unk_13_14=4, unk_16_20=1.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14384)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(14003820)
def Event_14003820(_, obj: uint):
    """Event 14003820"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()
    IfThisEventSlotFlagDisabled(MAIN)
    Wait(20.0)
    EnableObject(obj)
    SkipLinesIfObjectNotDestroyed(1, obj)
    RestoreObject(obj)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()


@RestartOnRest(14003825)
def Event_14003825(_, flag: uint, character: uint, character_1: uint):
    """Event 14003825"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterBackreadEnabled(AND_10, character)
    IfCharacterBackreadEnabled(AND_10, 14000810)
    IfCharacterBackreadEnabled(AND_10, 14000818)
    IfCharacterBackreadEnabled(AND_10, 14000826)
    IfFlagEnabled(AND_10, 14002805)
    AwaitConditionTrue(AND_10)
    DisableFlag(14003802)
    DisableFlag(14003803)
    DisableFlag(14003804)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(14003802, 14003804))
    SkipLinesIfFlagDisabled(1, 14003802)
    AddSpecialEffect(14000810, 14394)
    SkipLinesIfFlagDisabled(1, 14003803)
    AddSpecialEffect(14000818, 14394)
    SkipLinesIfFlagDisabled(1, 14003804)
    AddSpecialEffect(14000826, 14394)
    AddSpecialEffect(character, 14361)
    WaitFrames(frames=1)
    EnableFlag(flag)
    DisableThisSlotFlag()
    IfCharacterHasSpecialEffect(OR_1, character_1, 14396, target_comparison_type=ComparisonType.GreaterThanOrEqual)
    AwaitConditionTrue(OR_1)
    EnableFlag(14003806)
    End()


@RestartOnRest(14003950)
def Event_14003950(_, flag: uint, obj: uint):
    """Event 14003950"""
    IfObjectDestroyed(AND_1, obj)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(14003834)
def Event_14003834(_, obj: uint):
    """Event 14003834"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()
    IfThisEventSlotFlagDisabled(MAIN)
    Wait(20.0)
    EnableObject(obj)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    Wait(3.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()


@RestartOnRest(14003840)
def Event_14003840(_, character: uint, left: uint, left_1: uint, left_2: uint, flag: uint, flag_1: uint, flag_2: uint):
    """Event 14003840"""
    WaitFrames(frames=1)
    SkipLinesIfUnsignedEqual(2, left=left_2, right=0)
    SkipLinesIfFlagDisabled(1, flag_2)
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=left_2, radius=10.0)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=0)
    SkipLinesIfFlagDisabled(1, flag_1)
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=left_1, radius=10.0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    SkipLinesIfFlagDisabled(1, flag)
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=left, radius=10.0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14367)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14367)
    ReplanAI(character)
    Wait(8.0)
    Restart()


@RestartOnRest(14003845)
def Event_14003845(_, character: uint, obj: uint, obj_1: uint, obj_2: uint, obj_3: uint, obj_4: uint, obj_5: uint):
    """Event 14003845"""
    IfCharacterHasSpecialEffect(MAIN, character, 14362)
    SkipLinesIfFlagDisabled(1, obj_5)
    CreateObjectVFX(obj_2, vfx_id=200, model_point=814625)
    SkipLinesIfFlagDisabled(1, obj_4)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=814625)
    SkipLinesIfFlagDisabled(1, obj_3)
    CreateObjectVFX(obj, vfx_id=200, model_point=814625)
    Wait(1.5)
    SkipLinesIfFlagDisabled(1, obj_5)
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=obj_2, radius=4.5)
    SkipLinesIfFlagDisabled(1, obj_4)
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=obj_1, radius=4.5)
    SkipLinesIfFlagDisabled(1, obj_3)
    IfEntityWithinDistance(OR_1, entity=20000, other_entity=obj, radius=4.5)
    IfTimeElapsed(OR_1, seconds=5.0)
    AwaitConditionTrue(OR_1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L10, character=character, special_effect=14363)
    ReplanAI(character)
    ForceAnimation(character, 3014, unknown2=1.0)
    Wait(0.699999988079071)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=obj_2, radius=4.5)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=obj_5)
    GotoIfObjectDestroyed(Label.L0, obj=obj_5)
    DisableNetworkFlag(obj_5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj_2,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableObject(obj_2)

    # --- Label 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=obj_1, radius=4.5)
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    GotoIfFlagDisabled(Label.L1, flag=obj_4)
    GotoIfObjectDestroyed(Label.L1, obj=obj_4)
    DisableNetworkFlag(obj_4)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj_1,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableObject(obj_1)

    # --- Label 1 --- #
    DefineLabel(1)
    IfEntityWithinDistance(AND_3, entity=20000, other_entity=obj, radius=4.5)
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    GotoIfFlagDisabled(Label.L2, flag=obj_3)
    GotoIfObjectDestroyed(Label.L2, obj=obj_3)
    DisableNetworkFlag(obj_3)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableObject(obj)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteObjectVFX(obj_2)
    DeleteObjectVFX(obj_1)
    DeleteObjectVFX(obj)
    Restart()


@RestartOnRest(14003850)
def Event_14003850(
    _,
    character: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
    obj_4: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    flag_4: uint,
    obj__obj_flag: uint,
    obj__obj_flag_1: uint,
    obj__obj_flag_2: uint,
    obj__obj_flag_3: uint,
    obj__obj_flag_4: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    region_4: uint,
):
    """Event 14003850"""
    IfCharacterHasSpecialEffect(MAIN, character, 14363)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region)
    SkipLinesIfFlagDisabled(23, flag)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableNetworkFlag(flag)
    ForceAnimation(obj, 1, unknown2=1.0)
    AddSpecialEffect(character, 5032)
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    CreateHazard(
        obj_flag=obj__obj_flag,
        obj=obj__obj_flag,
        model_point=210,
        behavior_param_id=220400150,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=12.0,
        repetition_time=0.0,
    )
    Wait(7.5)
    DisableObject(obj)
    Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_1)
    SkipLinesIfFlagDisabled(23, flag_1)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableNetworkFlag(flag_1)
    ForceAnimation(obj_1, 1, unknown2=1.0)
    AddSpecialEffect(character, 5032)
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_1,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    CreateHazard(
        obj_flag=obj__obj_flag_1,
        obj=obj__obj_flag_1,
        model_point=210,
        behavior_param_id=220400150,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=12.0,
        repetition_time=0.0,
    )
    Wait(7.5)
    DisableObject(obj_1)
    Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_2)
    SkipLinesIfFlagDisabled(23, flag_2)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableNetworkFlag(flag_2)
    ForceAnimation(obj_2, 1, unknown2=1.0)
    AddSpecialEffect(character, 5032)
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_2,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    CreateHazard(
        obj_flag=obj__obj_flag_2,
        obj=obj__obj_flag_2,
        model_point=210,
        behavior_param_id=220400150,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=12.0,
        repetition_time=0.0,
    )
    Wait(7.5)
    DisableObject(obj_2)
    Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_3)
    SkipLinesIfFlagDisabled(23, flag_3)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableNetworkFlag(flag_3)
    ForceAnimation(obj_3, 1, unknown2=1.0)
    AddSpecialEffect(character, 5032)
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_3,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    CreateHazard(
        obj_flag=obj__obj_flag_3,
        obj=obj__obj_flag_3,
        model_point=210,
        behavior_param_id=220400150,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=12.0,
        repetition_time=0.0,
    )
    Wait(7.5)
    DisableObject(obj_3)
    Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_4)
    SkipLinesIfFlagDisabled(23, flag_4)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableNetworkFlag(flag_4)
    ForceAnimation(obj_4, 1, unknown2=1.0)
    AddSpecialEffect(character, 5032)
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=220,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=223,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=225,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=221,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=222,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=obj__obj_flag_4,
        model_point=224,
        behavior_id=220400155,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    CreateHazard(
        obj_flag=obj__obj_flag_4,
        obj=obj__obj_flag_4,
        model_point=210,
        behavior_param_id=220400150,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=12.0,
        repetition_time=0.0,
    )
    Wait(7.5)
    DisableObject(obj_4)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    Restart()


@NeverRestart(14003880)
def Event_14003880(
    _,
    character: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
):
    """Event 14003880"""
    DisableNetworkSync()
    EndIfFlagEnabled(14000899)
    GotoIfThisEventSlotFlagDisabled(Label.L10)
    IfCharacterWhitePhantom(OR_14, 20000)
    EndIfConditionFalse(input_condition=OR_14)
    SkipLinesIfFlagEnabled(3, flag)
    EnableFlag(flag)
    Move(20000, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    End()
    SkipLinesIfFlagEnabled(3, flag_1)
    EnableFlag(flag_1)
    Move(20000, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    End()
    SkipLinesIfFlagEnabled(2, flag_2)
    EnableFlag(flag_2)
    Move(20000, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterWhitePhantom(OR_15, 20000)
    IfCharacterType(OR_15, 20000, character_type=CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, OR_15)
    End()
    IfHealthLessThanOrEqual(MAIN, character, value=0.0)
    WaitFrames(frames=1)
    DisableAI(14000800)
    SetNetworkUpdateRate(14005810, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    Wait(4.0)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    DisableBossHealthBar(character)
    Wait(3.0)
    IfCharacterWhitePhantom(AND_10, ProtectedEntities.ClientPlayer1)
    GotoIfConditionFalse(Label.L0, input_condition=AND_10)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag)
    Move(
        ProtectedEntities.ClientPlayer1,
        destination=destination_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_1)
    EnableFlag(flag_1)
    Move(
        ProtectedEntities.ClientPlayer1,
        destination=destination_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_2)
    EnableFlag(flag_2)
    Move(
        ProtectedEntities.ClientPlayer1,
        destination=destination_3,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterWhitePhantom(AND_11, ProtectedEntities.ClientPlayer2)
    GotoIfConditionFalse(Label.L1, input_condition=AND_11)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag)
    Move(
        ProtectedEntities.ClientPlayer2,
        destination=destination_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_1)
    EnableFlag(flag_1)
    Move(
        ProtectedEntities.ClientPlayer2,
        destination=destination_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_2)
    EnableFlag(flag_2)
    Move(
        ProtectedEntities.ClientPlayer2,
        destination=destination_3,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(AND_12, ProtectedEntities.ClientPlayer3)
    GotoIfConditionFalse(Label.L2, input_condition=AND_12)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag)
    Move(
        ProtectedEntities.ClientPlayer3,
        destination=destination_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_1)
    EnableFlag(flag_1)
    Move(
        ProtectedEntities.ClientPlayer3,
        destination=destination_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_2)
    EnableFlag(flag_2)
    Move(
        ProtectedEntities.ClientPlayer3,
        destination=destination_3,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    EndIfFlagEnabled(flag_2)
    IfCharacterWhitePhantom(AND_13, ProtectedEntities.ClientPlayer4)
    GotoIfConditionFalse(Label.L3, input_condition=AND_13)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag)
    Move(
        ProtectedEntities.ClientPlayer4,
        destination=destination_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_1)
    EnableFlag(flag_1)
    Move(
        ProtectedEntities.ClientPlayer4,
        destination=destination_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_2)
    EnableFlag(flag_2)
    Move(
        ProtectedEntities.ClientPlayer4,
        destination=destination_3,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    EndIfFlagEnabled(flag_2)
    IfCharacterWhitePhantom(AND_14, ProtectedEntities.ClientPlayer5)
    GotoIfConditionFalse(Label.L4, input_condition=AND_14)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag)
    Move(
        ProtectedEntities.ClientPlayer5,
        destination=destination_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_1)
    EnableFlag(flag_1)
    Move(
        ProtectedEntities.ClientPlayer5,
        destination=destination_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )
    SkipLinesIfFlagEnabled(2, flag_2)
    EnableFlag(flag_2)
    Move(
        ProtectedEntities.ClientPlayer5,
        destination=destination_3,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)


@RestartOnRest(14003885)
def Event_14003885(
    _,
    character: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 14003885"""
    IfCharacterHasSpecialEffect(MAIN, character, 14372)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_1)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_2)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_3)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(14003886)
def Event_14003886(_, character: uint, region: uint, special_effect__special_effect_id: int):
    """Event 14003886"""
    IfCharacterInsideRegion(AND_1, character=character, region=region)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect__special_effect_id, target_count=0.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, special_effect__special_effect_id)
    Restart()


@RestartOnRest(14003892)
def Event_14003892(_, character: uint, character_1: uint):
    """Event 14003892"""
    IfCharacterHasSpecialEffect(MAIN, character, 14378)
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    Restart()


@RestartOnRest(14003893)
def Event_14003893(_, character: uint, character_1: uint):
    """Event 14003893"""
    IfCharacterHasSpecialEffect(MAIN, character, 5028)
    AddSpecialEffect(character_1, 14353)
    Wait(1.0)
    Restart()


@RestartOnRest(14003894)
def Event_14003894(_, character: uint, character_1: uint):
    """Event 14003894"""
    IfCharacterHasSpecialEffect(MAIN, character, 5029)
    AddSpecialEffect(character_1, 14355)
    Wait(1.0)
    Restart()


@RestartOnRest(14003898)
def Event_14003898(
    _,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
):
    """Event 14003898"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Normal, target_comparison_type=ComparisonType.NotEqual)
    Wait(40.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_1, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_1, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_1, special_effect=14393)
    AddSpecialEffect(character_1, 14367)
    ReplanAI(character_1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_2, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_2, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14367)
    ReplanAI(character_2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_3, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_3, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14367)
    ReplanAI(character_3)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_4, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_4, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14367)
    ReplanAI(character_4)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_5, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_5, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14367)
    ReplanAI(character_5)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_6, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_6, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14367)
    ReplanAI(character_6)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_7, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_7, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14367)
    ReplanAI(character_7)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_8, special_effect=14351)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_8, special_effect=14394)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14367)
    ReplanAI(character_8)
    DisableThisSlotFlag()
    Restart()


@RestartOnRest(14003900)
def Event_14003900(_, owner_entity: uint, source_entity: uint):
    """Event 14003900"""
    WaitRandomSeconds(min_seconds=3.0, max_seconds=10.0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=220400180,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(14003915)
def Event_14003915():
    """Event 14003915"""
    IfFlagEnabled(MAIN, 14000800)
    Kill(14005810)
    End()


@RestartOnRest(14003922)
def Event_14003922(_, flag: uint, character: uint, character_1: uint):
    """Event 14003922"""
    IfCharacterHasSpecialEffect(AND_1, character, 14580)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=230,
        copy_draw_parent=character,
    )
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CancelSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    ReplanAI(character_1)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20010, unknown2=1.0)
    Wait(0.800000011920929)
    EnableAnimations(character_1)
    Restart()


@RestartOnRest(14003923)
def Event_14003923(_, flag: uint, flag_1: uint, character: uint, character_1: uint):
    """Event 14003923"""
    IfFlagDisabled(AND_1, flag_1)
    IfFlagEnabled(AND_1, flag)
    IfCharacterHasSpecialEffect(OR_1, character, 14572)
    IfCharacterHasSpecialEffect(OR_1, character, 14573)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_1)
    CancelSpecialEffect(character_1, 14590)
    ReplanAI(character_1)
    Wait(3.0)
    Restart()


@RestartOnRest(14003924)
def Event_14003924(_, flag: uint, flag_1: uint, character: uint):
    """Event 14003924"""
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    CancelSpecialEffect(character, 14573)
    Restart()


@RestartOnRest(14003925)
def Event_14003925(_, flag: uint, character: uint):
    """Event 14003925"""
    IfHealthValueLessThanOrEqual(AND_1, character, value=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14573)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 20011, unknown2=1.0)
    Wait(5.0)
    Restart()


@RestartOnRest(14003926)
def Event_14003926(_, character: uint):
    """Event 14003926"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14574)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    CancelSpecialEffect(character, 14572)
    CancelSpecialEffect(character, 14573)
    CancelSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003937)
def Event_14003937(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
):
    """Event 14003937"""
    IfCharacterHasSpecialEffect(AND_1, character, 14595)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=71,
        copy_draw_parent=character,
    )
    ReplanAI(character_2)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_1, 20015, unknown2=1.0)
    CancelSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    Wait(0.10000000149011612)
    EnableCharacter(character_2)
    EnableAnimations(character_2)
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=72,
        copy_draw_parent=character,
    )
    ReplanAI(character_2)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_2, 20015, unknown2=1.0)
    CancelSpecialEffect(character_2, 14574)
    Wait(0.20000000298023224)
    EnableCharacter(character_3)
    EnableAnimations(character_3)
    Move(
        character_3,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=73,
        copy_draw_parent=character,
    )
    ReplanAI(character_3)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_3, 20015, unknown2=1.0)
    CancelSpecialEffect(character_3, 14574)
    Wait(0.10000000149011612)
    EnableCharacter(character_4)
    EnableAnimations(character_4)
    Move(
        character_4,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=70,
        copy_draw_parent=character,
    )
    ReplanAI(character_4)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character_4, 20015, unknown2=1.0)
    CancelSpecialEffect(character_4, 14574)
    Restart()


@RestartOnRest(14003938)
def Event_14003938(
    _,
    flag: uint,
    flag_1: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
):
    """Event 14003938"""
    IfFlagDisabled(AND_1, flag_1)
    IfFlagEnabled(AND_1, flag)
    IfCharacterHasSpecialEffect(OR_1, character, 14572)
    IfCharacterHasSpecialEffect(OR_1, character, 14573)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterHasSpecialEffect(OR_2, character_1, 14572)
    IfCharacterHasSpecialEffect(OR_2, character_1, 14573)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfCharacterHasSpecialEffect(OR_3, character_2, 14572)
    IfCharacterHasSpecialEffect(OR_3, character_2, 14573)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfCharacterHasSpecialEffect(OR_4, character_3, 14572)
    IfCharacterHasSpecialEffect(OR_4, character_3, 14573)
    IfConditionTrue(AND_1, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_1)
    CancelSpecialEffect(character_4, 14590)
    ReplanAI(character_4)
    Restart()


@RestartOnRest(14003939)
def Event_14003939(
    _,
    flag: uint,
    flag_1: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
):
    """Event 14003939"""
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfCharacterHasSpecialEffect(AND_1, character_1, 14573)
    IfCharacterHasSpecialEffect(AND_1, character_2, 14573)
    IfCharacterHasSpecialEffect(AND_1, character_3, 14573)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    CancelSpecialEffect(character, 14573)
    CancelSpecialEffect(character_1, 14573)
    CancelSpecialEffect(character_2, 14573)
    CancelSpecialEffect(character_3, 14573)
    Restart()


@RestartOnRest(14003940)
def Event_14003940(_, flag: uint, character: uint):
    """Event 14003940"""
    IfHealthValueLessThanOrEqual(AND_1, character, value=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14573)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableAnimations(character)
    ForceAnimation(character, 3035, unknown2=1.0)
    Wait(5.0)
    Restart()


@RestartOnRest(14003945)
def Event_14003945(_, character: uint):
    """Event 14003945"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14574)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    CancelSpecialEffect(character, 14572)
    CancelSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003962)
def Event_14003962(_, flag: uint, character: uint, character_1: uint):
    """Event 14003962"""
    IfCharacterHasSpecialEffect(AND_1, character, 14585)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=243,
        copy_draw_parent=character,
    )
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CancelSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    ReplanAI(character_1)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20026, unknown2=1.0)
    DisableAnimations(character_1)
    Wait(4.0)
    EnableAnimations(character_1)
    Restart()


@RestartOnRest(14003963)
def Event_14003963(_, flag: uint, flag_1: uint, character: uint, character_1: uint):
    """Event 14003963"""
    IfFlagDisabled(AND_1, flag_1)
    IfFlagEnabled(AND_1, flag)
    IfCharacterHasSpecialEffect(OR_1, character, 14572)
    IfCharacterHasSpecialEffect(OR_1, character, 14573)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_1)
    CancelSpecialEffect(character_1, 14590)
    ReplanAI(character_1)
    Restart()


@RestartOnRest(14003964)
def Event_14003964(_, flag: uint, flag_1: uint, character: uint):
    """Event 14003964"""
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    CancelSpecialEffect(character, 14573)
    Restart()


@RestartOnRest(14003965)
def Event_14003965(_, flag: uint, character: uint):
    """Event 14003965"""
    IfHealthValueLessThanOrEqual(AND_1, character, value=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14573)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 20025, unknown2=1.0)
    Wait(5.0)
    Restart()


@RestartOnRest(14003966)
def Event_14003966(_, character: uint):
    """Event 14003966"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14574)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    CancelSpecialEffect(character, 14572)
    CancelSpecialEffect(character, 14573)
    CancelSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003972)
def Event_14003972(_, flag: uint, character: uint, character_1: uint):
    """Event 14003972"""
    IfCharacterHasSpecialEffect(AND_1, character, 14575)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=65,
        copy_draw_parent=character,
    )
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CancelSpecialEffect(character_1, 14574)
    EnableFlag(flag)
    ReplanAI(character_1)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20026, unknown2=1.0)
    Wait(0.800000011920929)
    EnableAnimations(character_1)
    Restart()


@RestartOnRest(14003973)
def Event_14003973(_, flag: uint, flag_1: uint, character: uint, character_1: uint):
    """Event 14003973"""
    IfFlagDisabled(AND_1, flag_1)
    IfFlagEnabled(AND_1, flag)
    IfCharacterHasSpecialEffect(OR_1, character, 14572)
    IfCharacterHasSpecialEffect(OR_1, character, 14573)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_1)
    CancelSpecialEffect(character_1, 14590)
    ReplanAI(character_1)
    Restart()


@RestartOnRest(14003974)
def Event_14003974(_, flag: uint, flag_1: uint, character: uint):
    """Event 14003974"""
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    CancelSpecialEffect(character, 14573)
    Restart()


@RestartOnRest(14003975)
def Event_14003975(_, flag: uint, character: uint):
    """Event 14003975"""
    IfHealthValueLessThanOrEqual(AND_1, character, value=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14573)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 20027, unknown2=1.0)
    Wait(5.0)
    Restart()


@RestartOnRest(14003976)
def Event_14003976(_, character: uint):
    """Event 14003976"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterHasSpecialEffect(AND_1, character, 14573)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 14574)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 14571)
    AddSpecialEffect(character, 14574)
    CancelSpecialEffect(character, 14572)
    CancelSpecialEffect(character, 14573)
    CancelSpecialEffect(character, 14576)
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(14003977)
def Event_14003977(_, character: uint, character_1: uint):
    """Event 14003977"""
    IfHealthValueEqual(MAIN, character, value=0)
    AddSpecialEffect(character_1, 14572)
    ReplanAI(character_1)


@RestartOnRest(14003978)
def Event_14003978():
    """Event 14003978"""
    IfFlagEnabled(MAIN, 14000800)
    DisableSpawner(entity=14003810)
    DisableSpawner(entity=14003811)
    DisableSpawner(entity=14003812)
    DisableSpawner(entity=14003813)
    DisableSpawner(entity=14003814)
    DisableSpawner(entity=14003815)
    DisableSpawner(entity=14003816)
    DisableSpawner(entity=14003817)
    DisableSpawner(entity=14003818)


@RestartOnRest(14000700)
def Event_14000700():
    """Event 14000700"""
    EndIfFlagEnabled(14009205)
    SetCharacterTalkRange(character=14000700, distance=30.0)
    IfFlagEnabled(AND_1, 14000800)
    IfFlagDisabled(AND_1, 3468)
    IfEntityWithinDistance(AND_1, entity=14000700, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(14002705)
    End()


@RestartOnRest(14000701)
def Event_14000701():
    """Event 14000701"""
    EndIfFlagEnabled(14009210)
    SetCharacterTalkRange(character=14000700, distance=30.0)
    IfFlagEnabled(AND_1, 14000800)
    IfFlagEnabled(AND_1, 3468)
    IfEntityWithinDistance(AND_1, entity=14000701, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(14002706)
    End()


@RestartOnRest(14000702)
def Event_14000702():
    """Event 14000702"""
    WaitFrames(frames=1)
    DisableCharacter(14000700)
    DisableBackread(14000700)
    DisableCharacter(14000701)
    DisableBackread(14000701)
    AwaitFlagEnabled(flag=9118)
    IfFlagEnabled(OR_1, 3468)
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(14000700)
    EnableBackread(14000700)
    ForceAnimation(14000700, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(14000701)
    EnableBackread(14000701)
    ForceAnimation(14000701, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(14000703)
def Event_14000703():
    """Event 14000703"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9614)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9615)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 60540, unknown2=1.0)
    Wait(0.20000000298023224)
    Restart()


@RestartOnRest(14000710)
def Event_14000710(_, character__obj: uint, character__obj_1: uint):
    """Event 14000710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3460)
    IfFlagEnabled(AND_1, 14009253)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(14009253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableCharacter(character__obj_1)
    DisableBackread(character__obj_1)
    IfFlagEnabled(OR_1, 3468)
    IfFlagEnabled(OR_1, 3469)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3468)
    IfFlagEnabled(OR_2, 3469)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3462)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(3, 3468)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 90100, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 14002713)
    Move(character__obj, destination=14002701, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 3469)
    EnableCharacter(character__obj_1)
    EnableBackread(character__obj_1)
    SetTeamType(character__obj_1, TeamType.FriendlyNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagDisabled(3, 3468)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    SetTeamType(character__obj, TeamType.HostileNPC)
    SkipLinesIfFlagDisabled(3, 3469)
    EnableCharacter(character__obj_1)
    EnableBackread(character__obj_1)
    SetTeamType(character__obj_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagDisabled(4, 3468)
    DropMandatoryTreasure(character__obj)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    SkipLinesIfFlagDisabled(4, 3469)
    DropMandatoryTreasure(character__obj_1)
    DisableCharacter(character__obj_1)
    DisableBackread(character__obj_1)
    DisableObject(character__obj_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3468)
    IfFlagEnabled(OR_15, 3469)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(14000711)
def Event_14000711():
    """Event 14000711"""
    EndIfFlagEnabled(3463)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfHealthValueEqual(AND_1, 14000710, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(14000710, True)
    IfTimeElapsed(AND_2, seconds=20.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetBackreadStateAlternate(14000710, False)
    End()


@RestartOnRest(14000712)
def Event_14000712():
    """Event 14000712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400401)
    IfTimeElapsed(AND_2, seconds=2.0)
    IfFlagEnabled(AND_2, 7609)
    AwaitConditionTrue(AND_2)
    EnableFlag(14002713)
    AwardItemLot(104010, host_only=False)
    End()


@RestartOnRest(14000713)
def Event_14000713():
    """Event 14000713"""
    AwaitFlagEnabled(flag=7609)
    AwaitFlagEnabled(flag=14002713)
    Move(14000710, destination=14002701, destination_type=CoordEntityType.Region, short_move=True)
    End()


@RestartOnRest(14000714)
def Event_14000714():
    """Event 14000714"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3461, 3463))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034509259)
    End()


@RestartOnRest(14000720)
def Event_14000720():
    """Event 14000720"""
    EndIfFlagEnabled(14009300)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=14002080)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 14307)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(14009300)
    End()


@RestartOnRest(14000730)
def Event_14000730(_, character: uint):
    """Event 14000730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3360)
    DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3371)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3371)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3371)
    Restart()


@RestartOnRest(14000731)
def Event_14000731():
    """Event 14000731"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400106)
    IfTimeElapsed(AND_2, seconds=2.0)
    IfFlagEnabled(AND_2, 7608)
    AwaitConditionTrue(AND_2)
    AwardItemLot(101060, host_only=False)
    End()


@RestartOnRest(14000740)
def Event_14000740(_, character: uint):
    """Event 14000740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3948)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3948)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3948)
    Restart()


@RestartOnRest(14000741)
def Event_14000741(_, character: uint):
    """Event 14000741"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3949)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3949)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930025, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3949)
    Restart()


@RestartOnRest(14000742)
def Event_14000742():
    """Event 14000742"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3943)
    IfFlagEnabled(AND_1, 3948)
    IfFlagDisabled(AND_1, 11109306)
    IfEntityWithinDistance(AND_1, entity=14000720, other_entity=20000, radius=4.0)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109306)
    End()


@RestartOnRest(14000750)
def Event_14000750(_, character: uint, obj: uint):
    """Event 14000750"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3806)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(obj)
    IfFlagEnabled(MAIN, 3806)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    DisableGravity(character)
    DisableAnimations(character)
    Unknown_2004_81(character=character)
    EnableObject(obj)
    EnableObjectInvulnerability(obj)
    ForceAnimation(character, 90103, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3806)
    Restart()
