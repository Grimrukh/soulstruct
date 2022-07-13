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
    RegisterGrace(grace_flag=13000003, obj=13001953, unknown=5.0)
    RegisterGrace(grace_flag=13000004, obj=13001954, unknown=5.0)
    RegisterGrace(grace_flag=13000005, obj=13001955, unknown=5.0)
    RegisterGrace(grace_flag=13000006, obj=13001956, unknown=5.0)
    RegisterGrace(grace_flag=13000007, obj=13001957, unknown=5.0)
    RegisterGrace(grace_flag=13000008, obj=13001958, unknown=5.0)
    RegisterGrace(grace_flag=13000009, obj=13001959, unknown=5.0)
    RegisterGrace(grace_flag=13000010, obj=13001960, unknown=5.0)
    Event_13002805()
    RunCommonEvent(0, 9005810, args=(13000830, 13000001, 13000951, 13001951, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(13000850, 13000002, 13000952, 13001952, 5.0), arg_types="IIIIf")
    Event_13002500()
    Event_13002800()
    Event_13002810()
    Event_13002811()
    Event_13002829()
    Event_13002820()
    Event_13002827()
    Event_13002828()
    Event_13002819()
    Event_13002830()
    Event_13002834()
    Event_13002835()
    Event_13002840()
    Event_13002841()
    Event_13002849()
    Event_13002850()
    Event_13002860()
    Event_13002861()
    Event_13002865()
    Event_13002890(0, flag=13002944, character=13000851, character_1=13000852, special_effect_id=15504)
    Event_13002891(
        0,
        flag=13002944,
        character=13003851,
        character_1=13000852,
        special_effect=15506,
        character_2=13000851,
        flag_1=13002873
    )
    Event_13002890(1, flag=13002945, character=13000852, character_1=13000851, special_effect_id=15454)
    Event_13002891(
        1,
        flag=13002945,
        character=13003852,
        character_1=13000851,
        special_effect=15456,
        character_2=13000852,
        flag_1=13002874
    )
    Event_13002892()
    Event_13002236(0, region=13002314, character=13000235)
    RunCommonEvent(0, 90005300, args=(13000340, 13000340, 40770, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000341, 13000341, 40772, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000342, 13000342, 40774, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000343, 13000343, 40776, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000369, 13000369, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000490, 13000490, 13002091, 0.0, 0), arg_types="IIifi")
    Event_13002493(0, character=13000490, region=13002641, region_1=13002640)
    Event_13002646(0, 13000492, 13002492, 13000492, 10.0)
    RunCommonEvent(0, 90005300, args=(13000494, 13000494, 0, 0.0, 0), arg_types="IIifi")
    Event_13002493(2, character=13000494, region=13002645, region_1=13002494)
    Event_13002646(1, 13000494, 13002646, 13000494, 10.0)
    Event_13002610()
    RunCommonEvent(0, 90005300, args=(13000495, 13000495, 13002093, 0.0, 0), arg_types="IIifi")
    Event_13002646(2, 13000495, 13002495, 13000495, 1.0)
    RunCommonEvent(0, 90005300, args=(13000701, 13000701, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000702, 13000702, 0, 0.0, 0), arg_types="IIifi")
    Event_13002493(3, character=13000702, region=13002497, region_1=13002493)
    RunCommonEvent(0, 90005300, args=(13000295, 13000295, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000296, 13000296, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(13000496, 13000496, 13002095, 2.0, 0), arg_types="IIifi")
    Event_13002580()
    Event_13002510()
    RunCommonEvent(
        0,
        90005501,
        args=(13000510, 13000511, 0, 13001510, 13001511, 13001512, 13000512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(13000515, 13000516, 0, 13001515, 13001516, 13001517, 13000517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(13000520, 13000521, 0, 13001520, 13001521, 13001522, 13000522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(13000525, 13000526, 1, 13001525, 13001526, 13001527, 13000527),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(13000530, 13000531, 2, 13001530, 13001531, 13001532, 13000532),
        arg_types="IIIIIII",
    )
    Event_13002600(0, 13000600, 13002600, 13002120, 0.0)
    Event_13002600(1, 13000600, 13002600, 13002121, 1.0)
    Event_13002600(2, 13000600, 13002600, 13002122, 3.0)
    Event_13002600(3, 13000600, 13002600, 13002123, 5.0)
    Event_13002600(4, 13000600, 13002600, 13002124, 6.0)
    Event_13002600(5, 13000600, 13002600, 13002125, 9.0)
    Event_13002600(6, 13000600, 13002600, 13002126, 1.0)
    Event_13002600(7, 13000600, 13002600, 13002127, 2.5)
    Event_13002600(8, 13000600, 13002600, 13002128, 7.0)
    RunCommonEvent(
        0,
        90005620,
        args=(13000570, 13001570, 13001571, 13001572, 13002570, 13002571, 13002572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(13000570, 13001573), arg_types="II")
    RunCommonEvent(
        0,
        90005780,
        args=(13000850, 13002160, 13002161, 13000720, 20, 13002721, 13002720, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(13000850, 13002160, 13002161, 13000720), arg_types="IIII")
    Event_13002859()
    RunCommonEvent(
        0,
        90005780,
        args=(13000850, 13002164, 13002165, 13000725, 20, 13002726, 13002721, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(13000850, 13002164, 13002165, 13000725), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(13002164, 13002855, 13000725, 13002853, 13002869, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 13000180, 13002181, 13002182, 13000710, 22, 13002180, 13002181, 0.0, 13009300, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(13000180, 13002181, 13002182, 13000710), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(13000180, 13002181, 13002182, 13000710, 102920, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        13002660,
        args=(13000180, 13002181, 13002182, 13000710, 13002180, 13002183, 0),
        arg_types="IIIIIIi",
    )
    Event_13003700()
    RunCommonEvent(0, 90005704, args=(13000700, 13009256, 3660, 13009251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(13000700, 3661, 3662, 13009251, 13009256, 3660, 3663, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(13000700, 3663, 3660, 3663), arg_types="IIII")
    Event_13003710(0, character=13000700)
    Event_13003711(0, character=13000700)
    RunCommonEvent(0, 90005750, args=(13001700, 4110, 101740, 400174, 400174, 13009254, 0), arg_types="IiiIIIi")
    Event_13003720()
    Event_13003721()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13000519()
    RunCommonEvent(0, 90005201, args=(13000200, 30003, 20003, 2.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(13000201, 30003, 20003, 2.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(13000202, 30003, 20003, 2.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(13000252, 30003, 20003, 2.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(13000203, 13002203, 20.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(13000204, 13002201, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000250, 13002201, 3.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000217, 13002217, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000218, 30004, 20004, 13002217, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(13000206, 13002205, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(13000209, 13002209, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(13000207, 30003, 20003, 13002207, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(13000210, 13002210, 0.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(13000210, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(13000211, 13002207, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000212, 13002207, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(13000212, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005250, args=(13000213, 13002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000214, 13002215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000215, 13002215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000216, 13002215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000219, 13002214, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000251, 13002214, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000221, 13002220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000222, 13002222, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000223, 13002223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(13000225, 13002225, 20.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005210, args=(13000227, 30004, 20004, 13002227, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(13000228, 13002228, 0.0, 3002), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000230, 13002230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000231, 30004, 20004, 13002231, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000232, 13002230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000234, 13002234, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000233, 30003, 20003, 13002233, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(13000235, 13002235, 20.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(13000236, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(13000237, 30004, 20004, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(13000245, 13002245, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(13000265, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(13000267, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(13000268, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(13000269, 30004, 20004, 13002269, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(13000270, 40.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(13000260, 13002296, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000261, 13002296, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000262, 13002296, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(13000278, 13002278, 30.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(13000275, 13002277, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000276, 13002277, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000277, 13002277, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(13000282, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(13000284, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(13000288, 30004, 20004, 13002289, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000289, 30004, 20004, 13002289, 1.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000290, 30004, 20004, 13002289, 0.5, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000410, 13002412, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000412, 13002412, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000400, 13002412, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000409, 13002408, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000405, 30017, 20017, 13002412, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000408, 30017, 20017, 13002412, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000416, 13002416, 0.0, 3014), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(13000417, 1.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(13000418, 13002418, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000419, 13002418, 0.5, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(13000420, 13002420, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(13000422, 30018, 20018, 13002421, 5.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000423, 30018, 20018, 13002421, 7.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000424, 30018, 20018, 13002421, 8.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000435, 30017, 20017, 13002435, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000441, 13002435, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000446, 30017, 20017, 13002446, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000451, 30014, 20014, 13002446, 3.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000452, 30014, 20014, 13002446, 1.5, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(13000298, 13002323, 35.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(13000299, 13002323, 35.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(13000456, 30017, 20017, 13002456, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000457, 30018, 20018, 13002459, 1.5, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000458, 30018, 20018, 13002459, 2.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005221, args=(13000459, 30018, 20018, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(13000461, 30018, 20018, 13002459, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005221, args=(13000472, 30018, 20018, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(13000473, 30018, 20018, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(13000463, 30018, 20018, 13002463, 3.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000464, 30018, 20018, 13002463, 4.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005221, args=(13000474, 30018, 20018, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005251, args=(13000460, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(13000481, 13002481, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000482, 13002418, 0.5, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000485, 30017, 20017, 13002435, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000487, 30017, 20017, 13002435, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000488, 30017, 20017, 13002488, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(13000489, 13002488, 2.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(13000300, 30001, 20001, 13002300, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(13000310, 30000, 20000, 10.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(13000311, 30000, 20000, 13002311, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000312, 30000, 20000, 13002311, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(13000314, 13002314, 20.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(13000315, 30000, 20000, 20.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(13000315, 30000, 20000, 15.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(13000320, 30001, 20001, 13002456, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000330, 13002355, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000331, 13002355, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000350, 30001, 20001, 13002350, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000351, 30000, 3009, 13002350, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000352, 13002352, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000352, 30000, 20000, 13002352, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000354, 30000, 20000, 13002355, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000355, 30001, 20001, 13002355, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005210, args=(13000356, 30000, 20000, 13002356, 9.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(13000357, 30000, 20000, 13002356, 9.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005210, args=(13000358, 30000, 20000, 13002356, 9.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(13000360, 30000, 20000, 13002356, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000361, 30001, 20001, 13002356, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000362, 30001, 20001, 13002362, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000363, 30001, 20001, 13002362, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000364, 30000, 20000, 13002362, 1.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000365, 30001, 20001, 13002365, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(13000367, 30000, 20000, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(13000381, 13002381, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000382, 13002382, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000384, 13002384, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(13000385, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(13000380, 13002380, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000383, 13002380, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000390, 13002390, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(13000386, 55.0, 6.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(13000388, 13002388, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000389, 13002389, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000392, 13002392, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000395, 13002395, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000396, 13002396, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000398, 13002398, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000371, 30000, 20000, 13002372, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000372, 30000, 20000, 13002372, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000373, 30001, 20001, 13002300, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000376, 30001, 20001, 13002372, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(13000374, 13002374, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(13000375, 30000, 20000, 13002375, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000377, 13002377, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000378, 30000, 20000, 13002369, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000379, 30000, 20000, 13002369, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000369, 30001, 20001, 13002369, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000490, 30019, 20019, 13002490, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(13000494, 30019, 20019, 13002494, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000495, 13002495, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(13000702, 30010, 20010, 13002498, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(13000295, 13002295, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(13000296, 13002296, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(13000496, 13002496, 40.0, 0.0, -1), arg_types="IIffi")


@NeverRestart(13002500)
def Event_13002500():
    """Event 13002500"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(13000500)
    IfInsideMap(AND_1, game_map=CRUMBLING_FARUM_AZULA)
    IfFlagEnabled(AND_1, 110)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=13002502)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    IfPlayerInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, 9000)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(13000500)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)


@RestartOnRest(13002580)
def Event_13002580():
    """Event 13002580"""
    RegisterLadder(start_climbing_flag=13000580, stop_climbing_flag=13000581, obj=13001580)
    RegisterLadder(start_climbing_flag=13000582, stop_climbing_flag=13000583, obj=13001582)
    RegisterLadder(start_climbing_flag=13000584, stop_climbing_flag=13000585, obj=13001584)
    RegisterLadder(start_climbing_flag=13000586, stop_climbing_flag=13000587, obj=13001586)
    RegisterLadder(start_climbing_flag=13000588, stop_climbing_flag=13000589, obj=13001588)
    RegisterLadder(start_climbing_flag=13000590, stop_climbing_flag=13000591, obj=13001590)


@NeverRestart(13002510)
def Event_13002510():
    """Event 13002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            13000510,
            13000511,
            0,
            13001510,
            13001511,
            13003511,
            13001512,
            13003512,
            13002511,
            13002512,
            13000512,
            13000513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            13000515,
            13000516,
            0,
            13001515,
            13001516,
            13003516,
            13001517,
            13003517,
            13002516,
            13002517,
            13000517,
            13000518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            13000520,
            13000521,
            0,
            13001520,
            13001521,
            13003521,
            13001522,
            13003522,
            13002521,
            13002522,
            13000522,
            13000523,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            13000525,
            13000526,
            1,
            13001525,
            13001526,
            13003526,
            13001527,
            13003527,
            13002526,
            13002527,
            13000527,
            13000528,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            13000530,
            13000531,
            2,
            13001530,
            13001531,
            13003531,
            13001532,
            13003532,
            13002531,
            13002532,
            13000532,
            13000533,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(13000519)
def Event_13000519():
    """Event 13000519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(13000510)
    DisableThisSlotFlag()


@RestartOnRest(13002236)
def Event_13002236(_, region: uint, character: uint):
    """Event 13002236"""
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(character)
    Restart()


@RestartOnRest(13002490)
def Event_13002490(_, character: uint, region: uint, animation_id: int, flag: uint):
    """Event 13002490"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, animation_id, unknown2=1.0)


@RestartOnRest(13002493)
def Event_13002493(_, character: uint, region: uint, region_1: uint):
    """Event 13002493"""
    CancelSpecialEffect(character, 18941)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterInsideRegion(AND_1, character=character, region=region_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 18941)
    Wait(4.0)
    Restart()


@RestartOnRest(13002646)
def Event_13002646(_, flag: uint, region: uint, character: uint, seconds: float):
    """Event 13002646"""
    EndIfFlagEnabled(flag)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=region)
    IfHasAIStatus(AND_1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(seconds)
    ForceAnimation(character, 20001, unknown2=1.0)
    Wait(6.0)
    DisableCharacter(character)
    DisableThisSlotFlag()


@RestartOnRest(13002660)
def Event_13002660(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    unk_0_4: uint,
    other_entity: uint,
    region: uint,
    left: int,
):
    """Event 13002660"""
    EndIfFlagEnabled(flag)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_2, flag_1)
    SkipLinesIfUnsignedNotEqual(2, left=region, right=0)
    IfEntityBeyondDistance(AND_2, entity=PLAYER, other_entity=other_entity, radius=110.0)
    SkipLines(1)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=region)
    IfFlagEnabled(AND_3, flag_1)
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=180.0)
    SkipLines(3)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=360.0)
    SkipLines(1)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=720.0)
    IfConditionTrue(OR_10, input_condition=AND_1)
    IfConditionTrue(OR_10, input_condition=AND_2)
    IfConditionTrue(OR_10, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_10)
    EndIfFlagEnabled(flag)
    Unknown_2003_79(unk_0_4=unk_0_4)
    End()
    IfFlagDisabled(OR_11, flag_2)


@RestartOnRest(13002800)
def Event_13002800():
    """Event 13002800"""
    GotoIfFlagDisabled(Label.L0, flag=13000800)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L1, flag=118)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueLessThanOrEqual(MAIN, 13000800, value=0)
    Kill(13000801)
    Kill(13000800)
    Wait(4.0)
    PlaySoundEffect(13008000, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 13000800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 13000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetBackreadStateAlternate(13000800, True)
    KillBossAndDisplayBanner(character=13000800, banner_type=BannerType.HollowArenaWin)
    EnableNetworkFlag(13000800)
    EnableFlag(9116)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61116)
    EndIfPlayerNotInOwnWorld()
    EndIfPlayerInOwnWorld()


@RestartOnRest(13002805)
def Event_13002805():
    """Event 13002805"""
    GotoIfFlagEnabled(Label.L0, flag=13000800)
    DisableCharacter(13000950)
    DisableObject(13001950)
    Wait(1.0)
    IfFlagEnabled(MAIN, 13000800)
    Wait(4.0)
    Wait(7.800000190734863)
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=13001950, model_point=200, anchor_type=CoordEntityType.Object)
    Wait(0.5)
    EnableCharacter(13000950)
    EnableObject(13001950)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(grace_flag=13000000, obj=13001950, reaction_distance=5.0, reaction_angle=180.0, unknown=5.0)


@RestartOnRest(13002810)
def Event_13002810():
    """Event 13002810"""
    GotoIfFlagDisabled(Label.L0, flag=13000800)
    DisableCharacter(13000800)
    DisableCharacter(13000801)
    DisableAnimations(13000800)
    DisableAnimations(13000801)
    Kill(13000800)
    Kill(13000801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(13000801)
    DisableAI(13000800)
    DisableHealthBar(13000800)
    DisableCharacter(13000800)
    DisableGravity(13000800)
    DisableAnimations(13000800)
    GotoIfFlagEnabled(Label.L1, flag=13000801)
    ForceAnimation(13000801, 30018, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_1, 13002805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=13002800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    ForceAnimation(13000801, 20038, loop=True, unknown2=1.0)
    EnableNetworkFlag(13000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 13002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=13002800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(13002803)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(13000800)
    ReferDamageToEntity(13000801, target_entity=13000800)
    EnableAI(13000801)
    SetNetworkUpdateRate(13000801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(13000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(13000801, name=902110000)


@RestartOnRest(13002811)
def Event_13002811():
    """Event 13002811"""
    EndIfFlagEnabled(13000800)
    IfHealthRatioLessThanOrEqual(AND_1, 13000801, value=0.550000011920929)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfHealthValueLessThanOrEqual(OR_15, PLAYER, value=0)
    IfCharacterInsideRegion(OR_15, character=PLAYER, region=13002815)
    EndIfConditionTrue(input_condition=OR_15)
    Unknown_2004_73(entity=13000800, unk_4_8=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=13000040,
        cutscene_flags=0,
        move_to_region=13002820,
        map_base_id=13000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(13000040, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(13002802)
    DisableCharacter(13000801)
    SetNetworkUpdateRate(13000801, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DisableAI(13000801)
    ForceAnimation(13000800, 20015, unknown2=1.0)
    Move(13000800, destination=13002825, destination_type=CoordEntityType.Region, copy_draw_parent=13000800)
    EnableGravity(13000800)
    EnableAnimations(13000800)
    EnableAI(13000800)
    SetNetworkUpdateRate(13000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(13000800, name=902110001)


@RestartOnRest(13002819)
def Event_13002819():
    """Event 13002819"""
    IfCharacterHasSpecialEffect(MAIN, 13000800, 15272)
    Move(13000800, destination=13002825, destination_type=CoordEntityType.Region, copy_draw_parent=13000800)
    Wait(1.0)
    Restart()


@RestartOnRest(13002820)
def Event_13002820():
    """Event 13002820"""
    IfHealthRatioNotEqual(AND_1, 13000800, value=0.0)
    IfFlagEnabled(AND_1, 13002821)
    SkipLinesIfFlagDisabled(1, 13002822)
    SetEventPoint(13000800, region=13002810, reaction_range=200.0)
    SkipLinesIfFlagDisabled(1, 13002823)
    SetEventPoint(13000800, region=13002811, reaction_range=200.0)
    SkipLinesIfFlagDisabled(1, 13002824)
    SetEventPoint(13000800, region=13002812, reaction_range=200.0)
    DisableFlag(13002821)
    Restart()


@RestartOnRest(13002827)
def Event_13002827():
    """Event 13002827"""
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 13000800, 15270)
    IfFlagDisabled(AND_1, 13002826)
    IfCharacterInsideRegion(OR_1, character=13000800, region=13002840)
    IfCharacterInsideRegion(OR_1, character=13000800, region=13002841)
    IfCharacterInsideRegion(OR_1, character=13000800, region=13002842)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(13000800, 15270)
    EnableFlag(13002826)
    Restart()


@RestartOnRest(13002828)
def Event_13002828():
    """Event 13002828"""
    IfFlagEnabled(AND_1, 13002826)
    IfCharacterOutsideRegion(AND_1, character=13000800, region=13002840)
    IfCharacterOutsideRegion(AND_1, character=13000800, region=13002841)
    IfCharacterOutsideRegion(AND_1, character=13000800, region=13002842)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(13002826)
    Restart()


@RestartOnRest(13002829)
def Event_13002829():
    """Event 13002829"""
    RunCommonEvent(
        0,
        9005800,
        args=(13000800, 13001800, 13002800, 13002805, 13005800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(13000800, 13001800, 13002800, 13002805, 13002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(13000800, 13001800, 4, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(13000800, 211000, 13002805, 13002806, 0, 13002802, 1, 1), arg_types="IiIIIIii")


@RestartOnRest(13002830)
def Event_13002830():
    """Event 13002830"""
    EndIfFlagEnabled(13000830)
    IfHealthValueLessThanOrEqual(MAIN, 13000830, value=0)
    Kill(13000830)
    Wait(4.0)
    PlaySoundEffect(13008000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 13000830)
    KillBossAndDisplayBanner(character=13000830, banner_type=BannerType.HollowArenaWin)
    Unknown_2003_68(unknown1=0, unknown2=-1.0, unknown3=0)
    EnableFlag(13000830)
    EnableFlag(9115)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61115)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(71301)


@RestartOnRest(13002834)
def Event_13002834():
    """Event 13002834"""
    EndIfFlagEnabled(13000830)
    GotoIfPlayerInOwnWorld(Label.L0)
    GotoIfFlagDisabled(Label.L0, flag=13002834)
    Unknown_2004_74(
        character=20000,
        unknown1=1,
        region=13002836,
        unknown2=-1,
        character_2=20000,
        unknown3=0,
        unknown4=1,
    )
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown18)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown17)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9740, entity=13001505)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Move(PLAYER, destination=13001505, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    ForceAnimation(PLAYER, 67010, unknown2=1.0)
    Wait(3.0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_12(
        cutscene_id=13000010,
        cutscene_flags=0,
        respawn_point=13002834,
        move_to_region=13000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=0,
        unk_25_26=1,
        unk_26_27=6,
        unk_28_32=-1.0,
        unk_32_36=0,
    )
    SkipLines(1)
    UnknownCutscene_12(
        cutscene_id=13000010,
        cutscene_flags=CutsceneFlags.Unskippable,
        respawn_point=13002836,
        move_to_region=13000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=0,
        unk_25_26=1,
        unk_26_27=6,
        unk_28_32=-1.0,
        unk_32_36=0,
    )
    WaitFramesAfterCutscene(frames=1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)


@RestartOnRest(13002835)
def Event_13002835():
    """Event 13002835"""
    GotoIfFlagDisabled(Label.L3, flag=13000830)
    DisableCharacter(13005830)
    DisableAnimations(13005830)
    Kill(13005830)
    EnableFlag(71301)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableAI(13000830)
    CreateNPCPart(13000830, npc_part_id=0, part_index=NPCPartType.Part1, part_health=9999)
    CreateNPCPart(13000830, npc_part_id=1, part_index=NPCPartType.Part2, part_health=9999)
    SetNPCPartEffects(
        13000830,
        npc_part_id=0,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        13000830,
        npc_part_id=1,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetLockOnPoint(character=13000830, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=13000830, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=13000830, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=13000830, lock_on_model_point=225, state=False)
    SetCharacterEventTarget(13000830, region=13000840)
    SetBackreadStateAlternate(13000830, True)
    ForceAnimation(13000830, 30000, loop=True, unknown2=1.0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=13002831)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=13000830, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=13000830, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=13000830, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=13000830, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=13000830, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=13000830, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    ForceAnimation(13000830, 20000, unknown2=1.0)
    EnableAI(13000830)
    SetNetworkUpdateRate(13000830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(13000830, name=904520000)
    ActivateMultiplayerBuffs(13005830)
    EndIfPlayerNotInOwnWorld()
    EnableNetworkFlag(13002835)
    SetNetworkUpdateAuthority(13005830, authority_level=UpdateAuthority.Unknown8192)
    NotifyBossBattleStart()


@RestartOnRest(13002840)
def Event_13002840():
    """Event 13002840"""
    EndIfFlagEnabled(13000830)
    IfCharacterHasSpecialEffect(AND_1, 13000830, 5029)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Unknown_2003_68(unknown1=3, unknown2=-1.0, unknown3=0)
    EnableFlag(13002832)


@RestartOnRest(13002841)
def Event_13002841():
    """Event 13002841"""
    EndIfFlagEnabled(13000830)
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(AND_1, 13000830, 5025)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4521)
    Wait(1.0)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 13000830, 5025)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)
    Wait(1.0)
    Restart()


@RestartOnRest(13002846)
def Event_13002846(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 13002846"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterWhitePhantom(AND_1, PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(13002849)
def Event_13002849():
    """Event 13002849"""
    Event_13002846(0, flag=13000830, flag_1=13002835, flag_2=13002836)
    RunCommonEvent(0, 9005822, args=(13000830, 452000, 13002835, 13002836, 0, 13002832, 0, 1), arg_types="IiIIIIii")


@RestartOnRest(13002850)
def Event_13002850():
    """Event 13002850"""
    EndIfFlagEnabled(13000850)
    IfHealthValueLessThanOrEqual(MAIN, 13000850, value=0)
    Kill(13000851)
    Kill(13000852)
    EnableFlag(13002854)
    Wait(4.0)
    PlaySoundEffect(13000850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 13000850)
    KillBossAndDisplayBanner(character=13000850, banner_type=BannerType.Unknown)
    EnableFlag(13000850)
    EnableFlag(9114)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61114)


@NeverRestart(13002859)
def Event_13002859():
    """Event 13002859"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 13002160)
    IfFlagEnabled(AND_1, 13002855)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=13002852)
    AICommand(13000720, command_id=10, command_slot=0)
    ReplanAI(13000720)
    SetEventPoint(13000720, region=13002850, reaction_range=0.0)
    IfCharacterInsideRegion(MAIN, character=13000720, region=13002859)
    RotateToFaceEntity(13000720, 13002850, animation=60060, wait_for_completion=True)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfCharacterInsideRegion(OR_5, character=13000720, region=13002850)
    IfConditionTrue(MAIN, input_condition=OR_5)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(13000720, command_id=-1, command_slot=0)
    ReplanAI(13000720)
    SetNetworkUpdateRate(13000720, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(13000720, command_id=10, command_slot=0)
    ReplanAI(13000720)
    SetEventPoint(13000720, region=13002852, reaction_range=0.0)
    IfCharacterInsideRegion(MAIN, character=13000720, region=13002859)
    RotateToFaceEntity(13000720, 13002852, animation=60060, wait_for_completion=True)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfCharacterInsideRegion(OR_5, character=13000720, region=13002852)
    IfConditionTrue(MAIN, input_condition=OR_5)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(13000720, command_id=-1, command_slot=0)
    ReplanAI(13000720)
    SetNetworkUpdateRate(13000720, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13002860)
def Event_13002860():
    """Event 13002860"""
    GotoIfFlagDisabled(Label.L6, flag=13000850)
    DisableCharacter(13000850)
    DisableCharacter(13000851)
    DisableCharacter(13000852)
    DisableAnimations(13000850)
    DisableAnimations(13000851)
    DisableAnimations(13000852)
    Kill(13000850)
    Kill(13000851)
    Kill(13000852)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableAI(13000851)
    DisableAI(13000852)
    DisableCharacter(13000850)
    DisableGravity(13000850)
    DisableAnimations(13000850)
    GotoIfFlagEnabled(Label.L7, flag=13000851)
    DisableCharacter(13000851)
    DisableCharacter(13000852)
    ForceAnimation(13000851, 30001, loop=True, unknown2=1.0)
    ForceAnimation(13000852, 30001, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=13002851)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=13000851, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=13000852, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(13000851)
    EnableCharacter(13000851)
    EnableCharacter(13000852)
    ForceAnimation(13000851, 20001, unknown2=1.0)
    ForceAnimation(13000852, 20001, unknown2=1.0)
    Goto(Label.L8)

    # --- Label 7 --- #
    DefineLabel(7)
    IfFlagEnabled(OR_2, 13002855)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=13002850)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=13002852)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=13002853)
    IfConditionTrue(MAIN, input_condition=OR_2)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(13000850)
    DisableAI(13000850)
    EnableAI(13000851)
    EnableAI(13000852)
    SetNetworkUpdateRate(13000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(13000851, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(13000852, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(13005851, target_entity=13000850)
    EnableBossHealthBar(13000850, name=903575000)


@RestartOnRest(13002861)
def Event_13002861():
    """Event 13002861"""
    EndIfFlagEnabled(13000850)
    IfHealthRatioLessThanOrEqual(OR_1, 13000850, value=0.5)
    IfFlagEnabled(OR_1, 13002873)
    IfFlagEnabled(OR_1, 13002874)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(13002852)


@RestartOnRest(13002890)
def Event_13002890(_, flag: uint, character: uint, character_1: uint, special_effect_id: int):
    """Event 13002890"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(13000850)
    EndIfFlagEnabled(13002854)
    IfFlagDisabled(AND_1, flag)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(20.0)
    IfHealthValueGreaterThan(OR_1, character_1, value=0)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, special_effect_id)
    EnableNetworkFlag(flag)
    Restart()


@RestartOnRest(13002891)
def Event_13002891(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    special_effect: int,
    character_2: uint,
    flag_1: uint,
):
    """Event 13002891"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(13000850)
    EndIfFlagEnabled(13002854)
    IfCharacterHasSpecialEffect(OR_1, character_1, special_effect)
    IfCharacterDead(OR_1, character_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(13000850)
    EndIfFlagEnabled(13002854)
    MakeEnemyAppear(character=character)
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_1)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(13002892)
def Event_13002892():
    """Event 13002892"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(13000850)
    EndIfFlagEnabled(13002854)
    IfCharacterDead(AND_1, 13000851)
    IfCharacterDead(AND_1, 13000852)
    IfFlagDisabled(AND_1, 13002944)
    IfFlagDisabled(AND_1, 13002945)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(13000850)
    Wait(10.0)
    EndIfFlagEnabled(13000850)
    EndIfFlagEnabled(13002854)
    EnableRandomFlagInRange(flag_range=(13002875, 13002876))
    GotoIfFlagEnabled(Label.L0, flag=13002875)
    GotoIfFlagEnabled(Label.L1, flag=13002876)

    # --- Label 0 --- #
    DefineLabel(0)
    MakeEnemyAppear(character=13003851)
    EnableFlag(13002873)
    DisableFlag(13002875)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    MakeEnemyAppear(character=13003852)
    EnableFlag(13002874)
    DisableFlag(13002876)
    Restart()


@RestartOnRest(13002865)
def Event_13002865():
    """Event 13002865"""
    RunCommonEvent(
        0,
        9005800,
        args=(13000850, 13001850, 13002850, 13002855, 13005850, 10000, 13000851, 13002851),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005800,
        args=(13000850, 13001852, 13002852, 13002855, 13005850, 10000, 13000851, 13002851),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005800,
        args=(13000850, 13001853, 13002853, 13002855, 13005850, 10000, 13000851, 13002851),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(13000850, 13001850, 13002850, 13002855, 13002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005801, args=(13000850, 13001852, 13002852, 13002855, 13002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005801, args=(13000850, 13001853, 13002853, 13002855, 13002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(13000850, 13001850, 5, 13000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(13000850, 13001852, 5, 13000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(13000850, 13001853, 5, 13000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(13000850, 13001854, 5, 13000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(13000850, 13001855, 5, 13000851), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(13000850, 356000, 13002855, 13002856, 0, 13002852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(13002600)
def Event_13002600(_, entity: uint, region: uint, anchor_entity: uint, seconds: float):
    """Event 13002600"""
    EndIfFlagEnabled(13000490)
    CreateProjectileOwner(entity=entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.10000000149011612)
    Wait(seconds)
    CreateTemporaryVFX(vfx_id=813600, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    Wait(5.0)
    Restart()


@RestartOnRest(13002610)
def Event_13002610():
    """Event 13002610"""
    ForceAnimation(13000495, 0, unknown2=1.0)
    IfHasAIStatus(OR_15, 13000495, ai_status=AIStatusType.Battle)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_2, 13000495)
    EndIfConditionTrue(input_condition=OR_2)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=13002619)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    ForceAnimation(13000495, 3029, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(13000495, 20002, unknown2=1.0)
    DisableThisSlotFlag()
    Wait(2.0)
    IfCharacterInsideRegion(OR_10, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_10, 13000495)
    EndIfConditionTrue(input_condition=OR_10)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=13000610,
        source_entity=13002610,
        model_point=-1,
        behavior_id=803000070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.5)
    IfCharacterInsideRegion(OR_11, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_11, 13000495)
    EndIfConditionTrue(input_condition=OR_11)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=13000620,
        source_entity=13002620,
        model_point=-1,
        behavior_id=803000070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=13000621,
        source_entity=13002621,
        model_point=-1,
        behavior_id=803000070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.5)
    IfCharacterInsideRegion(OR_12, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_12, 13000495)
    EndIfConditionTrue(input_condition=OR_12)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=13000630,
        source_entity=13002630,
        model_point=-1,
        behavior_id=803000070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=13000631,
        source_entity=13002631,
        model_point=-1,
        behavior_id=803000070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.8999999761581421)
    IfCharacterInsideRegion(OR_13, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_13, 13000495)
    EndIfConditionTrue(input_condition=OR_13)
    ForceAnimation(13000495, 30000, unknown2=1.0)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_3, 13000495)
    GotoIfConditionTrue(Label.L0, input_condition=OR_3)
    Wait(1.0)
    IfCharacterInsideRegion(OR_4, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_4, 13000495)
    GotoIfConditionTrue(Label.L0, input_condition=OR_4)
    Wait(1.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_5, 13000495)
    GotoIfConditionTrue(Label.L0, input_condition=OR_5)
    Wait(1.0)
    IfCharacterInsideRegion(OR_6, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_6, 13000495)
    GotoIfConditionTrue(Label.L0, input_condition=OR_6)
    Wait(1.0)
    IfCharacterInsideRegion(OR_7, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_7, 13000495)
    GotoIfConditionTrue(Label.L0, input_condition=OR_7)
    Wait(1.0)
    IfCharacterInsideRegion(OR_8, character=PLAYER, region=13002495)
    IfFlagEnabled(OR_8, 13000495)
    Wait(1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(13003700)
def Event_13003700():
    """Event 13003700"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 13002805)
    SetCharacterTalkRange(character=13000801, distance=100.0)
    SetCharacterTalkRange(character=13000800, distance=100.0)
    End()


@RestartOnRest(13003710)
def Event_13003710(_, character: uint):
    """Event 13003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3671)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(13000701)
    EnableCharacter(13000702)
    SkipLinesIfFlagDisabled(1, 13000702)
    DisableCharacter(13000702)
    IfFlagEnabled(MAIN, 3671)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(13002710)
    GotoIfFlagEnabled(Label.L4, flag=13009257)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 13009258)
    ForceAnimation(character, 930014, unknown2=1.0)
    DisableCharacter(13000701)
    ForceAnimation(13000701, 10001, unknown2=1.0)
    DisableCharacter(13000702)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableCharacter(13000701)
    DisableCharacter(13000702)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(13000701)
    DisableCharacter(13000702)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3671)
    Restart()


@RestartOnRest(13003711)
def Event_13003711(_, character: uint):
    """Event 13003711"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 3671)
    IfFlagEnabled(AND_1, 13009256)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetCharacterTalkRange(character=character, distance=200.0)
    GotoIfFlagDisabled(Label.L1, flag=13009258)
    IfFlagEnabled(AND_2, 13009258)
    IfFlagDisabled(AND_2, 13009257)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    IfFlagEnabled(AND_3, 13009258)
    IfFlagEnabled(AND_3, 13009257)
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    EnableImmortality(character)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3662)
    EnableFlag(400175)
    IfHealthValueEqual(AND_2, character, value=1)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(13002712)
    ForceAnimation(character, 20035, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3660)
    SetTeamType(character, TeamType.NoTeam)
    IfFlagEnabled(AND_3, 13009257)
    AwaitConditionTrue(AND_3)
    SetTeamType(character, TeamType.FriendlyNPC)
    DisableImmortality(character)
    IfFlagEnabled(OR_1, 13009260)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfCharacterDead(OR_1, character)
    AwaitConditionTrue(OR_1)
    IfCharacterDead(AND_4, character)
    SkipLinesIfConditionTrue(1, AND_4)
    Kill(character, award_souls=True)
    AwardItemLot(101740, host_only=False)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 400174)
    EnableFlag(13009254)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3663)
    End()


@RestartOnRest(13003720)
def Event_13003720():
    """Event 13003720"""
    WaitFrames(frames=1)
    DisableFlag(13009300)
    IfFlagDisabled(AND_1, 16009460)
    IfFlagDisabled(AND_1, 3883)
    EndIfConditionTrue(input_condition=AND_1)
    EnableFlag(13009300)
    End()


@NeverRestart(13003721)
def Event_13003721():
    """Event 13003721"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    IfFlagEnabled(OR_4, 13002720)
    IfFlagEnabled(OR_4, 13002721)
    EndIfConditionTrue(input_condition=OR_4)
    EndIfFlagEnabled(13000850)
    EndIfFlagDisabled(3880)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=13002721, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=13002726, radius=10.0)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13002720)
    DisableFlag(13002721)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(13002720)
    EnableFlag(13002721)
    End()
