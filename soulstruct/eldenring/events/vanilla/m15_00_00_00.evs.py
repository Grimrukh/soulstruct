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
    DisableObject(15001702)
    RunCommonEvent(0, 9005810, args=(15000800, 15000000, 15000950, 15001950, 0.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(15000850, 15000005, 15000955, 15001955, 0.0), arg_types="IIIIf")
    RegisterGrace(grace_flag=15000001, obj=15001951, unknown=8.0)
    RegisterGrace(grace_flag=15000002, obj=15001952, unknown=8.0)
    RegisterGrace(grace_flag=15000003, obj=15001953, unknown=8.0)
    RegisterGrace(grace_flag=15000004, obj=15001954, unknown=8.0)
    RegisterGrace(grace_flag=15000006, obj=15001956, unknown=8.0)
    RegisterGrace(grace_flag=15000007, obj=15001957, unknown=8.0)
    RegisterGrace(grace_flag=15000008, obj=15001958, unknown=8.0)
    Event_15002800()
    Event_15002810()
    Event_15002811()
    Event_15002820(0, character=15000802, animation_id=3030, special_effect=18451)
    Event_15002820(1, character=15000803, animation_id=3031, special_effect=18452)
    Event_15002820(2, character=15000804, animation_id=3032, special_effect=18453)
    Event_15002820(3, character=15000805, animation_id=3033, special_effect=18454)
    Event_15002830(0, special_effect_id=18410, special_effect=18420)
    Event_15002830(1, special_effect_id=18411, special_effect=18421)
    Event_15002830(2, special_effect_id=18412, special_effect=18422)
    Event_15002830(3, special_effect_id=18413, special_effect=18423)
    Event_15002830(4, special_effect_id=18414, special_effect=18424)
    Event_15002830(5, special_effect_id=18415, special_effect=18425)
    Event_15002830(6, special_effect_id=18416, special_effect=18426)
    Event_15002830(7, special_effect_id=18417, special_effect=18427)
    Event_15002830(8, special_effect_id=18418, special_effect=18428)
    Event_15002830(9, special_effect_id=18419, special_effect=18429)
    Event_15002848(0, special_effect=18031, locked_camera_id__normal_camera_id=2122)
    Event_15002849()
    Event_15002850()
    Event_15002860()
    Event_15002861()
    Event_15002899()
    RunCommonEvent(
        0,
        90005795,
        args=(7610, 0, 15009208, 15002141, 15002142, 80610, 9060, 15001705, 30000),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=1, unk_4_8=20)
    RunCommonEvent(0, 90005797, args=(7610, 15005706, 7, 15002142, 4823), arg_types="IIBIi")
    Event_15002145()
    RunCommonEvent(
        0,
        90005795,
        args=(7611, 0, 15009209, 15002151, 15002152, 80611, 9061, 15001706, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=1, unk_4_8=30)
    RunCommonEvent(0, 90005796, args=(7611, 15000702, 5, 15002151), arg_types="IIBI")
    Event_15002155()
    RunCommonEvent(0, 90005300, args=(15000390, 15000390, 15001250, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(15000391, 15000391, 15001260, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(15000392, 15000392, 15001270, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(15000393, 15000393, 15001280, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(15000394, 15000394, 15001290, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(15000398, 15000398, 15001200, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005201, args=(15000495, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005221, args=(15000497, 30001, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(15000498, 30001, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005211, args=(15000400, 30000, 20000, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000401, 30000, 20000, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000402, 30000, 20000, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000418, 30000, 20000, 15002418, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000403, 30000, 20000, 15002403, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000404, 30000, 20000, 15002404, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000405, 30000, 20000, 15002404, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000406, 30000, 20000, 15002404, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000414, 30000, 20000, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000415, 30000, 20000, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000431, 30000, 20000, 15002403, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000360, 15002360, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000361, 30005, 20005, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000362, 30005, 20005, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000363, 30002, 20002, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000364, 15002364, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000365, 30001, 20001, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000366, 15002387, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000367, 15002387, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(15000368, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(15000369, 15002369, 1.0, 0.30000001192092896, 3008), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000371, 15002371, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005201,
        args=(15000372, 30004, 20004, 1.399999976158142, 0.0, 0, 0, 0, 0),
        arg_types="IiiffIIII",
    )
    RunCommonEvent(0, 90005261, args=(15000380, 15002380, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000381, 15002381, 0.10000000149011612, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(15000382, 30005, 20005, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(15000383, 15002383, 0.10000000149011612, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000387, 30001, 20001, 15002387, 1.0, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000340, 15002340, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000450, 15002450, 1.0, 0.0, 3021), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000451, 15002450, 1.0, 0.20000000298023224, 3021), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000452, 15002450, 1.0, 0.20000000298023224, 3021), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000453, 15002450, 1.0, 0.10000000149011612, 3021), arg_types="IIffi")
    RunCommonEvent(0, 90005221, args=(15000454, 30001, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005261, args=(15000455, 15002455, 1.0, 0.0, 3037), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000456, 15002456, 1.0, 0.0, 3037), arg_types="IIffi")
    RunCommonEvent(0, 90005221, args=(15000457, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005211, args=(15000458, 30006, 20006, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000459, 30006, 20006, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000470, 15002470, 1.0, 0.0, 3037), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000471, 15002470, 1.0, 0.5, 3037), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000330, 30000, 20000, 15002330, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000331, 30000, 20000, 15002331, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000332, 30000, 20000, 15002332, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000334, 30000, 20000, 15002334, 1.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000202, 30005, 20005, 15002202, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005213,
        args=(15000203, 30002, 20002, 15002203, 1.0, 0.5, 0, 0, 0, 0, 15000204, 0.5),
        arg_types="IiiIffIIIIIf",
    )
    RunCommonEvent(
        0,
        90005213,
        args=(15000204, 30001, 20001, 15002203, 1.0, 0.0, 1, 1, 1, 0, 15000203, 1.0),
        arg_types="IiiIffIIIIIf",
    )
    RunCommonEvent(0, 90005211, args=(15000205, 30002, 20002, 15002205, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000206, 30002, 20002, 15002206, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000207, 30002, 20002, 15002206, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000208, 30003, 20003, 15002208, 0.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000209, 30001, 20001, 15002208, 1.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000210, 30005, 20005, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000212, 30005, 20005, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000216, 30002, 20002, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005251, args=(15000217, 2.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005211, args=(15000218, 30004, 20004, 15002218, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000219, 30003, 20003, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000221, 15002221, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000222, 15002221, 1.0, 0.10000000149011612, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000226, 15002226, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000227, 15002227, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000228, 30002, 20002, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000229, 30002, 20002, 0, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005251, args=(15000233, 1.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005211, args=(15000234, 30003, 20003, 15002234, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000235, 30005, 20005, 15002235, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000236, 30003, 20003, 15002236, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000238, 30005, 20005, 15002238, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(15000250, 30003, 20003, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(15000251, 30002, 20002, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(15000252, 30002, 20002, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(15000255, 30003, 20003, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(15000256, 30004, 20004, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(15000257, 1.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005211, args=(15000258, 30002, 20002, 15002258, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000259, 30002, 20002, 15002258, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000260, 15002260, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000261, 15002260, 1.0, 0.30000001192092896, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000262, 15002260, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000263, 15002260, 1.0, 0.30000001192092896, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000266, 30010, 20010, 15002266, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000270, 30000, 20000, 15002270, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000272, 30000, 20000, 15002272, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000273, 30000, 20000, 15002273, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000274, 30000, 20000, 15002274, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000275, 15002275, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000276, 15002275, 1.0, 0.0, -1), arg_types="IIffi")
    Event_15002310(0, character=15000310, character_1=15000344)
    Event_15002310(1, character=15000311, character_1=15000345)
    Event_15002310(2, character=15000312, character_1=15000346)
    RunCommonEvent(0, 90005211, args=(15000322, 30000, 20000, 15002322, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000323, 30000, 20000, 15002323, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000324, 30000, 20000, 15002324, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000326, 30001, 20001, 15002326, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000327, 30001, 20001, 15002327, 1.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000328, 30001, 20001, 15002327, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000329, 30001, 20001, 15002327, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000344, 15002344, 1.0, 0.30000001192092896, 30002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000345, 15002345, 1.0, 0.30000001192092896, 30002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000346, 15002346, 1.0, 0.0, 30002), arg_types="IIffi")
    Event_15002344(0, character=15000344, entity=15003344)
    Event_15002344(1, character=15000345, entity=15003345)
    Event_15002344(2, character=15000346, entity=15003346)
    RunCommonEvent(0, 90005261, args=(15000280, 15002280, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000281, 15002281, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000282, 15002282, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000295, 30000, 20001, 0, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000296, 15002296, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000297, 30000, 20001, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000298, 30000, 20001, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000299, 30000, 20001, 0, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000283, 15002283, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000284, 15002284, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000285, 15002285, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000287, 15002280, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000288, 30002, 20005, 15002288, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(15000289, 30000, 20001, 15002288, 1.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(15000290, 30000, 20001, 15002288, 1.0, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(15000291, 30002, 20005, 15002281, 1.0, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(15000292, 15002292, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000293, 15002291, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(15000582, 30001, 20001, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(15000583, 30001, 20001, 15002275, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000584, 30001, 20001, 15002275, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(15000585, 30000, 20000, 15002278, 1.0, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(15000586, 30000, 20000, 15002278, 1.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(15000587, 30000, 20000, 15002278, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(15000589, 30001, 20001, 15002275, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(15000300, 15002300, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000356, 15002356, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000515, 15002356, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000516, 15002356, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000517, 15002356, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(15000392, 15002392, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(15000398, 30002, 20002, 15002398, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005501,
        args=(15000520, 15001520, 0, 15001520, 15001521, 15001522, 15000521),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(15000525, 15001525, 0, 15001525, 15001526, 15001527, 15000526),
        arg_types="IIIIIII",
    )
    Event_15002520()
    RunCommonEvent(
        0,
        90005501,
        args=(15000620, 15001620, 0, 15001620, 15001621, 15001622, 15000621),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(15000625, 15001625, 0, 15001625, 15001626, 15001627, 15000626),
        arg_types="IIIIIII",
    )
    Event_15002620()
    RunCommonEvent(
        0,
        90005620,
        args=(15000570, 15001570, 15001571, 0, 15002570, 15002571, 15002572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(15000570, 15001573), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(15000575, 15001575, 15001576, 0, 15002575, 15002576, 15002577),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(15000575, 15001578), arg_types="II")
    Event_15002580()
    Event_15002680()
    Event_15000700()
    Event_15000701()
    Event_15000702(0, obj=15001702, obj_1=15001703)
    Event_15000710(0, character=15000700)
    RunCommonEvent(0, 90005704, args=(15000700, 4181, 4180, 15002901, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(15000700, 4181, 4182, 15002901, 1059481190, 4180, 4184, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(15000700, 4183, 4180, 4184), arg_types="IIII")
    Event_15000711(0, character=15000703)
    RunCommonEvent(0, 90005708, args=(15000703, 4180, 0), arg_types="III")
    RunCommonEvent(0, 90005702, args=(15000703, 4183, 4180, 4184), arg_types="IIII")
    RunCommonEvent(0, 90005750, args=(15001701, 4350, 103210, 400321, 400321, 4192, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005752, args=(15001704, 200, 120, 3.0), arg_types="Iiif")
    Event_15000712(0, obj=15001700)
    Event_15000713(0, entity=15001703)
    Event_15000715()
    Event_15000716()
    RunCommonEvent(0, 90005774, args=(7611, 103220, 400323), arg_types="IiI")
    RunCommonEvent(0, 90005774, args=(7610, 104800, 400480), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(15000700)
    DisableBackread(15000701)
    DisableBackread(15000702)
    DisableBackread(15000703)
    DisableBackread(15000705)
    DisableBackread(15000706)
    DisableBackread(15000707)
    DisableBackread(15000708)
    DisableBackread(15000709)
    DisableBackread(15000710)
    DisableBackread(15000711)
    DisableBackread(15000712)
    Event_15000050()
    Event_15002200(4, character=15000204, obj=15001204)
    Event_15002200(9, character=15000209, obj=15001209)
    Event_15002550()


@NeverRestart(15000050)
def Event_15000050():
    """Event 15000050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(15000525)
    EnableFlag(15000625)


@RestartOnRest(15002145)
def Event_15002145():
    """Event 15002145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(15000701)
    EnableBackread(15000706)
    EnableBackread(15000708)
    EnableBackread(15000710)
    EnableBackread(15000712)
    SetTeamType(15000701, TeamType.Human)
    SetTeamType(15000706, TeamType.Enemy)
    SetTeamType(15000708, TeamType.Enemy)
    SetTeamType(15000710, TeamType.Enemy)
    SetTeamType(15000712, TeamType.Enemy)
    CreateObjectVFX(15001710, vfx_id=200, model_point=806700)


@RestartOnRest(15002155)
def Event_15002155():
    """Event 15002155"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=30,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(15000702)
    EnableBackread(15000705)
    CreateObjectVFX(15001710, vfx_id=200, model_point=806700)


@RestartOnRest(15002200)
def Event_15002200(_, character: uint, obj: uint):
    """Event 15002200"""
    EndIfThisEventSlotFlagEnabled()
    EnableObjectInvulnerability(obj)
    Wait(0.10000000149011612)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 5080)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableObjectInvulnerability(obj)


@RestartOnRest(15002310)
def Event_15002310(_, character: uint, character_1: uint):
    """Event 15002310"""
    IfCharacterDead(AND_1, character_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Kill(character)


@RestartOnRest(15002344)
def Event_15002344(_, character: uint, entity: uint):
    """Event 15002344"""
    DisableSpawner(entity=entity)
    IfCharacterAlive(AND_1, character)
    IfCharacterHasSpecialEffect(AND_1, character, 15007)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableSpawner(entity=entity)
    IfCharacterAlive(AND_2, character)
    IfCharacterHasSpecialEffect(AND_2, character, 15007)
    IfConditionFalse(MAIN, input_condition=AND_2)
    DisableSpawner(entity=entity)


@NeverRestart(15002520)
def Event_15002520():
    """Event 15002520"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            15000520,
            15001520,
            0,
            15001520,
            15001521,
            15003521,
            15001522,
            15003522,
            15002521,
            15002522,
            15000521,
            15002522,
            15000523,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90015502, args=(15000523, 15001521, 15002522), arg_types="III")
    RunCommonEvent(
        0,
        90005500,
        args=(
            15000525,
            15001525,
            0,
            15001525,
            15001526,
            15003526,
            15001527,
            15003527,
            15002526,
            15002527,
            15000526,
            15002527,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(15002620)
def Event_15002620():
    """Event 15002620"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            15000620,
            15001620,
            0,
            15001620,
            15001621,
            15003621,
            15001622,
            15003622,
            15002621,
            15002622,
            15000621,
            15002622,
            15000623,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005502, args=(15000623, 15001621, 15002622), arg_types="III")
    RunCommonEvent(
        0,
        90005500,
        args=(
            15000625,
            15001625,
            0,
            15001625,
            15001626,
            15003626,
            15001627,
            15003627,
            15002626,
            15002627,
            15000626,
            15002627,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(15002550)
def Event_15002550():
    """Event 15002550"""
    EnableObjectInvulnerability(15001550)
    EnableObjectInvulnerability(15001551)
    EnableObjectInvulnerability(15001552)


@RestartOnRest(15002580)
def Event_15002580():
    """Event 15002580"""
    RegisterLadder(start_climbing_flag=15000580, stop_climbing_flag=15000581, obj=15001580)
    RegisterLadder(start_climbing_flag=15000582, stop_climbing_flag=15000583, obj=15001582)
    RegisterLadder(start_climbing_flag=15000584, stop_climbing_flag=15000585, obj=15001584)
    RegisterLadder(start_climbing_flag=15000586, stop_climbing_flag=15000587, obj=15001586)
    RegisterLadder(start_climbing_flag=15000588, stop_climbing_flag=15000589, obj=15001588)
    RegisterLadder(start_climbing_flag=15000590, stop_climbing_flag=15000591, obj=15001590)


@RestartOnRest(15002680)
def Event_15002680():
    """Event 15002680"""
    RegisterLadder(start_climbing_flag=15000680, stop_climbing_flag=15000681, obj=15001680)
    RegisterLadder(start_climbing_flag=15000682, stop_climbing_flag=15000683, obj=15001682)
    RegisterLadder(start_climbing_flag=15000684, stop_climbing_flag=15000685, obj=15001684)
    RegisterLadder(start_climbing_flag=15000686, stop_climbing_flag=15000687, obj=15001686)
    RegisterLadder(start_climbing_flag=15000688, stop_climbing_flag=15000689, obj=15001688)
    RegisterLadder(start_climbing_flag=15000690, stop_climbing_flag=15000691, obj=15001690)
    RegisterLadder(start_climbing_flag=15000692, stop_climbing_flag=15000693, obj=15001692)
    RegisterLadder(start_climbing_flag=15000694, stop_climbing_flag=15000695, obj=15001694)
    RegisterLadder(start_climbing_flag=15000696, stop_climbing_flag=15000697, obj=15001696)
    RegisterLadder(start_climbing_flag=15000698, stop_climbing_flag=15000699, obj=15001698)


@RestartOnRest(15002800)
def Event_15002800():
    """Event 15002800"""
    EndIfFlagEnabled(15000800)
    IfHealthValueLessThanOrEqual(MAIN, 15000800, value=0)
    Wait(4.0)
    PlaySoundEffect(15008000, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 15000800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 15000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    KillBossAndDisplayBanner(character=15000800, banner_type=BannerType.HollowArenaLoss)
    SkipLinesIfPlayerNotInOwnWorld(1)
    TriggerMultiplayerEvent(event_id=0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableNetworkFlag(15000800)
    EnableFlag(9120)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61120)


@RestartOnRest(15002810)
def Event_15002810():
    """Event 15002810"""
    GotoIfFlagDisabled(Label.L0, flag=15000800)
    DisableCharacter(15005800)
    DisableAnimations(15005800)
    Kill(15005800)
    EnableTreasure(obj=15001810)
    DisableObject(15001820)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(15005800)
    EnableImmortality(15000800)
    DisableCharacter(15000801)
    DisableAnimations(15000801)
    SetLockOnPoint(character=0, lock_on_model_point=-1, state=True)
    DisableCharacter(15000802)
    DisableAnimations(15000802)
    SetLockOnPoint(character=15000802, lock_on_model_point=220, state=True)
    DisableCharacter(15000803)
    DisableAnimations(15000803)
    SetLockOnPoint(character=15000803, lock_on_model_point=220, state=True)
    DisableCharacter(15000804)
    DisableAnimations(15000804)
    SetLockOnPoint(character=15000804, lock_on_model_point=220, state=True)
    DisableCharacter(15000805)
    DisableAnimations(15000805)
    SetLockOnPoint(character=15000805, lock_on_model_point=220, state=True)
    DisableTreasure(obj=15001810)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown18)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown17)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfFlagEnabled(Label.L1, flag=15000801)
    AddSpecialEffect(15000800, 5402)
    DisableAnimations(15000800)
    DisableGravity(15000800)
    SetDisplayMask(15000800, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(15000800, bit_index=12, switch_type=OnOffChange.On)
    SetDisplayMask(15000800, bit_index=13, switch_type=OnOffChange.On)
    ForceAnimation(15000800, 30000, unknown2=1.0)
    IfFlagEnabled(AND_1, 15002805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=15002800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    EnableNetworkFlag(15000801)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=15000000,
        cutscene_flags=0,
        move_to_region=15002811,
        map_base_id=15000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(15000000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=13.069999694824219, unknown2=34.47999954223633)
    AddSpecialEffect(15000800, 5400)
    Move(15000800, destination=15002812, destination_type=CoordEntityType.Region, short_move=True)
    EnableGravity(15000800)
    EnableAnimations(15000800)
    SetDisplayMask(15000800, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(15000800, bit_index=12, switch_type=OnOffChange.Off)
    SetDisplayMask(15000800, bit_index=13, switch_type=OnOffChange.Off)
    DisableObject(15001820)
    ForceAnimation(15000800, 3006, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(15000800, destination=15002814, destination_type=CoordEntityType.Region, short_move=True)
    DisableObject(15001820)
    IfFlagEnabled(AND_2, 15002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=15002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(15005800)
    SetNetworkUpdateRate(15005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(15000800, name=902120000)
    CancelSpecialEffect(15000800, 16141)


@RestartOnRest(15002811)
def Event_15002811():
    """Event 15002811"""
    EndIfFlagEnabled(15000800)
    IfHealthValueLessThanOrEqual(AND_1, 15000800, value=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 15000800, 18480)
    IfAttackedWithDamageType(OR_1, attacked_entity=15000800, attacker=0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=15000010,
        cutscene_flags=0,
        move_to_region=15002815,
        map_base_id=15000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(15000010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(15002802)
    SkipLinesIfPlayerNotInOwnWorld(1)
    ChangeCamera(normal_camera_id=2121, locked_camera_id=2121)
    Move(15000800, destination=15002816, destination_type=CoordEntityType.Region, short_move=True)
    UnknownCamera_4(unknown1=-29.0, unknown2=68.80000305175781)
    EnableBossHealthBar(15000800, name=902120001)
    AddSpecialEffect(15000800, 18000)
    AddSpecialEffect(15000800, 18001)
    AddSpecialEffect(15000800, 18002)
    CancelSpecialEffect(15000800, 18015)
    AddSpecialEffect(15000800, 18016)
    SetDisplayMask(15000800, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(15000800, bit_index=11, switch_type=OnOffChange.Off)
    SetDisplayMask(15000800, bit_index=12, switch_type=OnOffChange.On)
    CreateNPCPart(15000800, npc_part_id=10, part_index=NPCPartType.Part1, part_health=99999)
    SetNPCPartEffects(
        15000800,
        npc_part_id=10,
        material_sfx_id=109,
        material_vfx_id=109,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    CreateNPCPart(15000800, npc_part_id=310, part_index=NPCPartType.WeakPoint, part_health=99999)
    SetNPCPartEffects(
        15000800,
        npc_part_id=310,
        material_sfx_id=110,
        material_vfx_id=110,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    AddSpecialEffect(15000800, 18400)
    AddSpecialEffect(15000801, 18400)
    DisableHealthBar(15000801)
    ForceAnimation(15000800, 20002, unknown2=1.0)
    WaitFrames(frames=1)
    ReplanAI(15000800)
    Wait(3.200000047683716)
    DisableImmortality(15000800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    ChangeCamera(normal_camera_id=2120, locked_camera_id=2120)


@NeverRestart(15002820)
def Event_15002820(_, character: uint, animation_id: int, special_effect: int):
    """Event 15002820"""
    EndIfFlagEnabled(15000800)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    IfFlagDisabled(AND_1, 15002803)
    IfCharacterHasSpecialEffect(AND_1, 15000800, special_effect)
    IfFlagEnabled(AND_2, 15002803)
    IfCharacterHasSpecialEffect(AND_2, 15000801, special_effect)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableCharacter(character)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(2, 15002803)
    Move(
        character,
        destination=15000800,
        destination_type=CoordEntityType.Character,
        model_point=228,
        copy_draw_parent=15000800,
    )
    SkipLines(1)
    Move(
        character,
        destination=15000801,
        destination_type=CoordEntityType.Character,
        model_point=228,
        copy_draw_parent=15000801,
    )
    ForceAnimation(character, animation_id, unknown2=1.0)
    EnableAI(character)
    Wait(0.699999988079071)
    EnableAnimations(character)
    Wait(0.30000001192092896)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5029)
    IfConditionTrue(MAIN, input_condition=AND_5)
    Restart()


@NeverRestart(15002830)
def Event_15002830(_, special_effect_id: int, special_effect: int):
    """Event 15002830"""
    EndIfFlagEnabled(15000800)
    IfPlayerNotInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, special_effect)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    AddSpecialEffect(15000800, special_effect_id)
    Wait(0.20000000298023224)
    Restart()


@NeverRestart(15002840)
def Event_15002840(_, character: uint, character_1: uint, state: uchar):
    """Event 15002840"""
    EndIfFlagEnabled(15000800)
    IfCharacterHasSpecialEffect(AND_1, character, 18037)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    AddSpecialEffect(character_1, 18401)
    WaitFrames(frames=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=228,
        copy_draw_parent=character_1,
    )
    ReplanAI(character)
    ReplanAI(character_1)
    Wait(0.699999988079071)
    EnableAnimations(character_1)
    CancelSpecialEffect(character_1, 18401)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5029)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableCharacter(character)
    DisableAnimations(character)
    SetAbsoluteNetworkFlagState(15002803, state=state)
    Restart()


@NeverRestart(15002842)
def Event_15002842(_, character: uint, special_effect_id: int, special_effect: int):
    """Event 15002842"""
    EndIfFlagEnabled(15000800)
    AddSpecialEffect(character, special_effect_id)
    DisableCharacter(character)
    DisableAnimations(character)
    IfFlagDisabled(AND_1, 15002803)
    IfCharacterHasSpecialEffect(AND_1, 15000800, special_effect)
    IfFlagEnabled(AND_2, 15002803)
    IfCharacterHasSpecialEffect(AND_2, 15000801, special_effect)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableCharacter(character)
    WaitFrames(frames=1)
    EnableAI(character)
    SkipLinesIfFlagEnabled(2, 15002803)
    Move(
        character,
        destination=15000800,
        destination_type=CoordEntityType.Character,
        model_point=228,
        copy_draw_parent=15000800,
    )
    SkipLines(1)
    Move(
        character,
        destination=15000801,
        destination_type=CoordEntityType.Character,
        model_point=228,
        copy_draw_parent=15000801,
    )
    ReplanAI(character)
    Wait(0.699999988079071)
    EnableAnimations(character)
    Wait(2.0)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5029)
    IfConditionTrue(MAIN, input_condition=AND_5)
    Restart()


@NeverRestart(15002848)
def Event_15002848(_, special_effect: int, locked_camera_id__normal_camera_id: int):
    """Event 15002848"""
    DisableNetworkSync()
    EndIfFlagEnabled(15000800)
    IfFlagEnabled(AND_2, 15002810)
    SkipLinesIfPlayerNotInOwnWorld(2)
    IfFlagEnabled(AND_2, 15002805)
    SkipLines(1)
    IfFlagEnabled(AND_2, 15002806)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 15000800, special_effect)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 15000800, 18032)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 15000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EndIfFlagEnabled(15000800)
    ChangeCamera(normal_camera_id=2120, locked_camera_id=2120)
    IfFlagEnabled(AND_1, 15002810)
    IfCharacterHasSpecialEffect(AND_1, 15000800, special_effect)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 15000800, 18032)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, 15000800)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(15000800)
    ChangeCamera(
        normal_camera_id=locked_camera_id__normal_camera_id,
        locked_camera_id=locked_camera_id__normal_camera_id,
    )
    Restart()


@RestartOnRest(15002849)
def Event_15002849():
    """Event 15002849"""
    RunCommonEvent(
        0,
        9005800,
        args=(15000800, 15001800, 15002800, 15002805, 15005800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(15000800, 15001800, 15002800, 15002805, 15002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(15000800, 15001800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(15002800, 212000, 15002805, 15002806, 0, 15002802, 1, 1), arg_types="IiIIIIii")


@RestartOnRest(15002850)
def Event_15002850():
    """Event 15002850"""
    EndIfFlagEnabled(15000850)
    IfHealthValueLessThanOrEqual(MAIN, 15000850, value=0)
    Wait(4.0)
    PlaySoundEffect(15000850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 15000850)
    KillBossAndDisplayBanner(character=15000850, banner_type=BannerType.Unknown)
    EnableFlag(15000850)
    EnableFlag(9119)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61119)


@RestartOnRest(15002860)
def Event_15002860():
    """Event 15002860"""
    GotoIfFlagDisabled(Label.L0, flag=15000850)
    DisableCharacter(15005850)
    DisableAnimations(15005850)
    Kill(15005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(15005850)
    ForceAnimation(15000850, 30001, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=15000851)
    AddSpecialEffect(15000110, 9531)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=15002851)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=15000850, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(15000851)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(15000850, destination=15002860, destination_type=CoordEntityType.Region, copy_draw_parent=15000850)
    IfFlagEnabled(AND_2, 15002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=15002850)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(15000850, 20011, unknown2=1.0)
    ForceAnimation(15000850, 3005, unknown2=1.0)
    EnableAI(15005850)
    SetNetworkUpdateRate(15005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(15000110, 9532)
    Wait(2.0)
    EnableBossHealthBar(15000850, name=903252000)


@RestartOnRest(15002861)
def Event_15002861():
    """Event 15002861"""
    EndIfFlagEnabled(15000850)
    IfHealthRatioLessThanOrEqual(AND_1, 15000850, value=0.550000011920929)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)


@RestartOnRest(15002899)
def Event_15002899():
    """Event 15002899"""
    RunCommonEvent(
        0,
        9005800,
        args=(15000850, 15001850, 15002850, 15002855, 15005850, 10000, 15000851, 15002851),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(15000850, 15001850, 15002850, 15002855, 15002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(15000850, 15001850, 3, 15000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(15000850, 15001851, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(15000850, 920200, 15002855, 15002856, 0, 15002852, 0, 0), arg_types="IiIIIIii")


@NeverRestart(15000700)
def Event_15000700():
    """Event 15000700"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(15000800)
    EndIfFlagEnabled(15002700)
    IfFlagEnabled(MAIN, 15002805)
    SetCharacterTalkRange(character=15000800, distance=100.0)
    IfFlagEnabled(MAIN, 15002701)
    SetCharacterTalkRange(character=15000800, distance=17.0)


@NeverRestart(15000701)
def Event_15000701():
    """Event 15000701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(15000800)
    EndIfFlagEnabled(15002700)
    IfPlayerInOwnWorld(AND_1)
    IfHealthValueEqual(AND_1, 15000800, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(15000800, True)
    IfTimeElapsed(OR_1, seconds=100.0)
    IfFlagEnabled(OR_1, 15002701)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetBackreadStateAlternate(15000800, False)


@RestartOnRest(15000702)
def Event_15000702(_, obj: uint, obj_1: uint):
    """Event 15000702"""
    DisableObject(obj)
    DisableObject(obj_1)
    GotoIfFlagEnabled(Label.L19, flag=9120)
    IfFlagEnabled(AND_1, 9120)
    IfFlagEnabled(AND_1, 9000)
    AwaitConditionTrue(AND_1)
    Wait(1.0)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableObject(obj)
    EnableObject(obj_1)
    EnableNetworkFlag(15009212)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(15000710)
def Event_15000710(_, character: uint):
    """Event 15000710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4190)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4190)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    IfFlagDisabled(MAIN, 4190)
    Restart()


@RestartOnRest(15000711)
def Event_15000711(_, character: uint):
    """Event 15000711"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 4191)
    IfFlagEnabled(OR_1, 4192)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(15001704)
    IfFlagEnabled(OR_2, 4191)
    IfFlagEnabled(OR_2, 4192)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    EnableObject(15001704)
    SkipLinesIfFlagEnabled(3, 4191)
    ForceAnimation(character, 90104, unknown2=1.0)
    SetTeamType(character, TeamType.NoTeam)
    DisableObject(15001704)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    IfFlagDisabled(AND_1, 4191)
    IfFlagDisabled(AND_1, 4192)
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(15000712)
def Event_15000712(_, obj: uint):
    """Event 15000712"""
    DisableObject(obj)
    AwaitFlagEnabled(flag=4194)
    EnableObject(obj)
    End()


@RestartOnRest(15000713)
def Event_15000713(_, entity: uint):
    """Event 15000713"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400324)
    IfPlayerHasGood(AND_2, 8196)
    IfFlagDisabled(AND_2, 400324)
    IfFlagEnabled(AND_2, 15009212)
    IfActionButtonParamActivated(AND_2, action_button_id=6519, entity=entity)
    AwaitConditionTrue(AND_2)
    AwardItemLot(103240, host_only=False)
    RemoveGoodFromPlayer(item=8196, quantity=1)
    End()


@RestartOnRest(15000714)
def Event_15000714():
    """Event 15000714"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400323)
    IfTimeElapsed(AND_2, seconds=2.0)
    IfFlagEnabled(AND_2, 7611)
    AwaitConditionTrue(AND_2)
    AwardItemLot(103220, host_only=False)
    End()


@RestartOnRest(15000715)
def Event_15000715():
    """Event 15000715"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4190)
    IfFlagEnabled(AND_1, 4190)
    IfFlagEnabled(AND_1, 15009206)
    IfEntityWithinDistance(OR_1, entity=15001952, other_entity=20000, radius=5.0)
    IfEntityWithinDistance(OR_1, entity=15001953, other_entity=20000, radius=12.0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(15009213)
    EnableNetworkFlag(4198)
    EnableNetworkFlag(4178)
    End()


@RestartOnRest(15000716)
def Event_15000716():
    """Event 15000716"""
    EndIfFlagEnabled(15000398)
    AwaitFlagEnabled(flag=15000398)
    EnableNetworkFlag(4198)
    End()
