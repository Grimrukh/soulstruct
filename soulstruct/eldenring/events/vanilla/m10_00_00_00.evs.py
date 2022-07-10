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
    RegisterGrace(grace_flag=10000002, obj=10001952, unknown=5.0)
    RegisterGrace(grace_flag=10000003, obj=10001953, unknown=5.0)
    RegisterGrace(grace_flag=10000004, obj=10001954, unknown=5.0)
    RegisterGrace(grace_flag=10000005, obj=10001955, unknown=5.0)
    RegisterGrace(grace_flag=10000006, obj=10001956, unknown=5.0)
    RegisterGrace(grace_flag=10000007, obj=10001957, unknown=5.0)
    RegisterGrace(grace_flag=10000008, obj=10001958, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(71001, 71002, 10001982, 77100, 4, 78100, 78101, 78102, 78103, 78104, 78105, 78106, 78107, 78108, 78109),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 9005810, args=(10000800, 10000000, 10000950, 10001950, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(10000850, 10000001, 10000951, 10001951, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 90005511, args=(10000560, 10001560, 10003560, 219000, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(10000560, 10002560, 10002561), arg_types="III")
    RunCommonEvent(0, 90005511, args=(10000562, 10001562, 10003562, 1219000, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005511, args=(10000566, 10001566, 10003566, 219000, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(10000566, 10002566, 10002567), arg_types="III")
    RunCommonEvent(0, 90005510, args=(10000564, 10001564, 10003564, 219003, 208010, 0), arg_types="IIIiiI")
    Event_10002580()
    Event_10002500()
    Event_10002501()
    Event_10002510()
    RunCommonEvent(
        0,
        90005501,
        args=(10000510, 10000511, 0, 10001510, 10001511, 10001512, 10000512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(10000515, 10000516, 1, 10001515, 10001516, 10001517, 10000517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(10000520, 10000521, 0, 10001520, 10001521, 10001522, 10000522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005502, args=(10000514, 10001511, 10002512), arg_types="III")
    RunCommonEvent(0, 90005502, args=(10000524, 10001521, 10002522), arg_types="III")
    RunCommonEvent(0, 90005690, args=(10002610,))
    RunCommonEvent(0, 90005691, args=(10002610,))
    RunCommonEvent(0, 900005610, args=(10001680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(10001682, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005632, args=(580040, 10001681, 80040), arg_types="IIi")
    RunCommonEvent(0, 90005570, args=(60836, 94, 10001349, 0, 1, 0), arg_types="IiIiii")
    RunCommonEvent(0, 90005560, args=(10000698, 10001698, 0), arg_types="IIi")
    Event_10002690()
    RunCommonEvent(
        0,
        90005620,
        args=(10000570, 10001570, 10001571, 0, 10002570, 10002571, 10002572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(10000570, 10001573), arg_types="II")
    RunCommonEvent(0, 90005621, args=(10000570, 10001574), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(10000575, 10001575, 10001576, 0, 10002575, 10002576, 10002577),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(10000575, 10001578), arg_types="II")
    RunCommonEvent(0, 90005621, args=(10000575, 10001579), arg_types="II")
    Event_10002800()
    Event_10002810()
    Event_10002811()
    Event_10002849()
    Event_10002820(0, region=10002820, special_effect_id=14790, special_effect_id_1=14791)
    Event_10002821(0, region=10002821, special_effect_id=14792, special_effect_id_1=14793)
    Event_10002824(0, region=10002824, special_effect_id=14794, special_effect_id_1=14795)
    Event_10002825(0, region=10002825, special_effect_id=14796, special_effect_id_1=14797)
    Event_10002850()
    Event_10002860()
    Event_10002861()
    Event_10002870()
    Event_10002889()
    Event_10002350(0, 10000430, 10002430, 0.0, 10002350)
    Event_10002350(10, 10000207, 10002234, 0.0, 10002360)
    Event_10002350(1, 10000603, 10002263, 0.0, 10002351)
    Event_10002350(2, 10005680, 10002205, 0.0, 10002352)
    Event_10002350(3, 10000607, 10002206, 0.0, 10002353)
    Event_10002350(4, 10000550, 10002202, 0.0, 10002354)
    Event_10002350(5, 10000555, 10002202, 1.0, 10002355)
    Event_10002350(8, 10000280, 10002280, 0.0, 10002358)
    Event_10002350(9, 10005370, 10002217, 0.0, 10002359)
    Event_10002350(11, 10005360, 10002219, 0.0, 10002361)
    Event_1002200()
    Event_10002330(0, character=10000470, obj=10001600)
    Event_10002330(1, character=10000471, obj=10001601)
    Event_10002330(2, character=10000472, obj=10001602)
    Event_10002330(3, character=10000473, obj=10001603)
    Event_10002340(0, character=10000470, obj=10001600)
    Event_10002340(1, character=10000471, obj=10001601)
    Event_10002340(2, character=10000472, obj=10001602)
    Event_10002340(3, character=10000473, obj=10001603)
    Event_10002290(0, character=10000530)
    Event_10002290(1, character=10000531)
    Event_10002290(2, character=10000532)
    Event_10002290(3, character=10000533)
    Event_10002290(4, character=10000534)
    Event_10002290(5, character=10000535)
    Event_10002290(6, character=10000536)
    Event_10002310()
    Event_10002480()
    Event_10002423(0, character=10000423)
    Event_10002423(1, character=10000424)
    Event_10002423(2, character=10000425)
    Event_10002423(3, character=10000426)
    Event_10002311(0, 10000315, 30006, 20006, 10002311, 3.0, 0.0, 0, 0, 0, 0)
    Event_10002311(1, 10000316, 30006, 20006, 10002311, 3.0, 0.0, 0, 0, 0, 0)
    Event_10002311(2, 10000317, 30006, 20006, 10002311, 3.0, 0.0, 0, 0, 0, 0)
    Event_10002311(3, 10000318, 30007, 20007, 10002311, 3.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005300, args=(10000280, 10000280, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(10000289, 10000289, 10001085, 1.0, 0), arg_types="IIifi")
    Event_11002291(0, 10000291, 10002291, 3.0)
    RunCommonEvent(0, 90005300, args=(10000291, 10000291, 10001095, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(10000498, 10000498, 10001295, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(10000495, 10000495, 40170, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(10000496, 10000496, 40172, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(10000497, 10000497, 40174, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005780,
        args=(10000800, 10002160, 10002161, 10000733, 20, 10002730, 10009709, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(10000800, 10002160, 10002161, 10000733), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(10002160, 10002805, 10000733, 10002805, 10002809, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005780,
        args=(10000850, 10002164, 10002165, 10000716, 20, 10002722, 10009614, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(10000850, 10002164, 10002165, 10000716), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(10002164, 10002855, 10000716, 10002855, 10002859, 0), arg_types="IIIIIi")
    RunCommonEvent(0, 90005785, args=(10000850, 10002164, 10002165, 10000716, 10002722, 0, 75.0), arg_types="IIIIIIf")
    Event_10002910()
    RunCommonEvent(0, 90005703, args=(10000700, 3261, 3262, 10009504, 3261, 3260, 3263, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005703, args=(10000701, 3261, 3262, 10009385, 3261, 3260, 3263, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005703, args=(10000702, 3261, 3262, 10009386, 3261, 3260, 3263, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005703, args=(10000703, 3261, 3262, 10009387, 3261, 3260, 3263, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005703, args=(10000704, 3261, 3262, 10009388, 3261, 3260, 3263, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005703, args=(10000706, 3261, 3262, 10009505, 3261, 3260, 3263, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(10000700, 3261, 3260, 10009504, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005704, args=(10000701, 3261, 3260, 10009385, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005704, args=(10000702, 3261, 3260, 10009386, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005704, args=(10000703, 3261, 3260, 10009387, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005704, args=(10000704, 3261, 3260, 10009388, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005704, args=(10000706, 3261, 3260, 10009505, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(10000700, 3263, 3260, 3263), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(10000701, 3263, 3260, 3263), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(10000702, 3263, 3260, 3263), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(10000703, 3263, 3260, 3263), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(10000704, 3263, 3260, 3263), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(10000706, 3263, 3260, 3263), arg_types="IIII")
    Event_10003724()
    Event_10003726()
    Event_10003728(0, region=10002716)
    RunCommonEvent(0, 10003710)
    Event_10003711(0, first_flag=10002732, last_flag=10002735, flag=10002732, region=10002700)
    Event_10003711(1, first_flag=10002732, last_flag=10002735, flag=10002733, region=10002702)
    Event_10003711(2, first_flag=10002732, last_flag=10002735, flag=10002734, region=10002704)
    Event_10003711(3, first_flag=10002732, last_flag=10002735, flag=10002735, region=10002706)
    Event_10003715(
        0,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002732,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002736,
        region=10002701
    )
    Event_10003715(
        1,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002733,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002737,
        region=10002703
    )
    Event_10003715(
        2,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002734,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002738,
        region=10002705
    )
    Event_10003715(
        3,
        first_flag=10002732,
        last_flag=10002735,
        flag=10002735,
        first_flag_1=10002736,
        last_flag_1=10002739,
        flag_1=10002739,
        region=10002707
    )
    Event_10003720(0, flag=10009510, flag_1=10009390)
    Event_10003720(1, flag=10009511, flag_1=10009391)
    Event_10003720(2, flag=10009512, flag_1=10009392)
    Event_10003720(3, flag=10009513, flag_1=10009393)
    Event_10003729(0, region=10002701)
    Event_10003730()
    Event_10003734()
    Event_10003731()
    Event_10003732()
    Event_10003733()
    Event_10003738()
    Event_10000739()
    Event_10003736()
    Event_10003737()
    Event_10003775(0, character=10000730, character_1=10000731)
    RunCommonEvent(0, 90005704, args=(10000730, 4221, 4220, 10009701, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(10000730, 4221, 4222, 10009701, 4221, 4220, 4224, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(10000730, 4223, 4220, 4224), arg_types="IIII")
    Event_10003776(0, character=10000732)
    RunCommonEvent(0, 90005704, args=(10000732, 4221, 4220, 10009701, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(10000732, 4221, 4222, 10009701, 4221, 4220, 4224, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(10000732, 4223, 4220, 4224), arg_types="IIII")
    Event_10003777()
    Event_10003778()
    Event_10003779()
    Event_10003780()
    Event_10003790(0, character=10000725)
    Event_10000760(0, character=10000715)
    Event_10000761()
    Event_10000762()
    Event_10000763(0, 10001740, 15.0)
    Event_10000764(0, character=10000740, entity=10001740)
    Event_10003770(0, flag=78104, other_entity=10000952, flag_1=10009650)
    Event_10003771(0, other_entity=10000952, flag=10009650)
    Event_10003772(0, other_entity=10000952, flag=10009651)
    Event_10003773(0, other_entity=10000952, flag=10009651)
    Event_10003740(0, 10000800, 9600, 10009204, 0.5)
    Event_10003741(0, 10000800, 9601, 10009201, 0.5)
    Event_10003742(0, 10000800, 9602, 10009202, 0.5)
    Event_10003743(0, 10000800, 9603, 10009203, 0.5)
    Event_10003744(0, 10000800, 0, 9101, 10002805, 105.0)
    Event_10003745(0, character=10000720)
    RunCommonEvent(0, 90005706, args=(10000735, 930018, 0), arg_types="IiI")
    Event_10003500(0, region=10002740)
    Event_10003500(1, 10002741)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(10000700)
    DisableBackread(10000701)
    DisableBackread(10000702)
    DisableBackread(10000703)
    DisableBackread(10000704)
    DisableBackread(10000706)
    DisableBackread(10000707)
    DisableBackread(10000715)
    DisableBackread(10000720)
    DisableBackread(10000725)
    DisableBackread(10000730)
    DisableBackread(10000731)
    DisableBackread(10000732)
    DisableBackread(10000735)
    Event_10000519()
    RunCommonEvent(0, 90005260, args=(10000705, 0, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000200, 10002218, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000202, 10002218, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000203, 10002233, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000204, 10002204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000205, 10002233, 3.0, 3.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000206, 10002204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000207, 10002231, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000208, 10002236, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000209, 10002209, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000210, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000211, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(10000220, 30001, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000221, 30002, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000222, 30001, 20003, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000223, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000224, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000225, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000226, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005261, args=(10000227, 10002255, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000228, 10002255, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000229, 10002255, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000230, 10002255, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000231, 10002255, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000232, 10002255, 1.0, 0.0, -1), arg_types="IIffi")
    Event_10002240(0, 10000240, 30000, 20000, 10.0, 0.0, 0, 1, 0, 0, 0)
    Event_10002240(1, 10000241, 30000, 20000, 10.0, 0.0, 0, 1, 0, 0, 0)
    Event_10002240(2, 10000242, 30001, 20001, 10.0, 0.0, 0, 0, 0, 0, 1)
    RunCommonEvent(0, 90005251, args=(10000243, 2.0, 1.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(10000262, 10002208, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000263, 10002208, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000264, 10002208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000265, 10002208, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000266, 10002208, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000267, 10002208, 3.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000268, 10002208, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000269, 10002208, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000300, 10002300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000301, 10002300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000303, 10002301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000306, 10002306, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000307, 10002306, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000311, 10002311, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000312, 10002313, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000313, 10002313, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(10000325, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(10000335, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(10000323, 10002323, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(10000327, 4.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(10005334, 10002230, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000330, 10002330, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000332, 10002330, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000334, 10002334, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000350, 10002351, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000351, 10002351, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000352, 10002351, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000353, 10002351, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000354, 10002351, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000355, 10002351, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1000393, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1000394, 5.0, 1.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(10000372, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(10000373, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005221, args=(10000405, 30000, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000406, 30000, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(10000407, 30000, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005201, args=(10000415, 30006, 20006, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(10000416, 10002416, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000417, 10002416, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000418, 10002416, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000420, 10002425, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000422, 10002214, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(10000415, 30006, 20006, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(10000411, 10002616, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000435, 10002238, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(10000436, 30006, 20006, 10002207, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(10000437, 30006, 20006, 10002207, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005210, args=(10000446, 30006, 20006, 10002446, 6.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005251, args=(10000448, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(10000450, 10002214, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000600, 10002260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000281, 10002710, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000607, 10002267, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000609, 10002609, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000610, 10002609, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000615, 10002274, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000616, 10002616, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000460, 10002460, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000461, 10002461, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(10000462, 10002461, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000463, 10002463, 0.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000464, 10002463, 0.0, 3009), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000465, 10002463, 3.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000470, 10002470, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000471, 10002471, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000472, 10002471, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000473, 10002473, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000475, 10002475, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000476, 10002475, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000477, 10002477, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000481, 10002274, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(10000486, 30010, 20010, 10002486, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(10000630, 10002285, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(10000285, 10002285, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(10000544, 10002544, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000620, 10002213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000289, 10002220, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000498, 10002498, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000580, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000581, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000582, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000583, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000584, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000585, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000586, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000587, 10002211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000588, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000589, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000590, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000591, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000592, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000593, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000594, 10002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(10000595, 10002212, 0.0, -1), arg_types="IIfi")
    Event_10003700(0, character=10000700, obj=10001700)
    Event_10003702(0, character=10000706)
    Event_10003703(0, character=10000707)
    Event_10003701(0, character=10000701, obj=10001701, flag=10009510, flag_1=10009390)
    Event_10003701(1, character=10000702, obj=10001702, flag=10009511, flag_1=10009391)
    Event_10003701(2, character=10000703, obj=10001703, flag=10009512, flag_1=10009392)
    Event_10003701(3, character=10000704, obj=10001704, flag=10009513, flag_1=10009393)
    Event_10003705(0, entity=10000700)
    Event_10003705(1, entity=10000701)
    Event_10003705(2, entity=10000702)
    Event_10003705(3, entity=10000703)
    Event_10003705(4, entity=10000704)
    Event_10003705(5, entity=10000706)
    Event_10003705(6, 10000707)


@RestartOnRest(10002281)
def Event_10002281(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 10002281"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    EnableInvincibility(character)
    AddSpecialEffect(character, 16296)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    DisableInvincibility(character)


@NeverRestart(10002580)
def Event_10002580():
    """Event 10002580"""
    RegisterLadder(start_climbing_flag=10000580, stop_climbing_flag=10000581, obj=10001580)
    RegisterLadder(start_climbing_flag=10000582, stop_climbing_flag=10000583, obj=10001582)
    RegisterLadder(start_climbing_flag=10000584, stop_climbing_flag=10000585, obj=10001584)
    RegisterLadder(start_climbing_flag=10000586, stop_climbing_flag=10000587, obj=10001586)
    RegisterLadder(start_climbing_flag=10000588, stop_climbing_flag=10000589, obj=10001588)
    SkipLinesIfFlagEnabled(1, 2001)
    RegisterLadder(start_climbing_flag=10000590, stop_climbing_flag=10000591, obj=10001590)
    RegisterLadder(start_climbing_flag=10000592, stop_climbing_flag=10000593, obj=10001592)
    RegisterLadder(start_climbing_flag=10000594, stop_climbing_flag=10000595, obj=10001594)
    RegisterLadder(start_climbing_flag=10000596, stop_climbing_flag=10000597, obj=10001596)
    RegisterLadder(start_climbing_flag=10000598, stop_climbing_flag=10000599, obj=10001598)


@NeverRestart(10002500)
def Event_10002500():
    """Event 10002500"""
    IfFlagDisabled(AND_1, 10000500)
    IfFlagDisabled(AND_1, 10000501)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    EndOfAnimation(obj=10001500, animation_id=1)
    EndOfAnimation(obj=10001501, animation_id=1)
    DisableObjectActivation(10001501, obj_act_id=219030)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObjectActivation(10001501, obj_act_id=219030)
    IfFlagEnabled(MAIN, 10009355)
    EnableNetworkFlag(10000500)
    EnableFlag(10009355)
    Wait(2.0)
    DisableObjectActivation(10001501, obj_act_id=219030)
    Wait(2.0)
    ForceAnimation(10001501, 1, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(10001500, 1, unknown2=1.0)


@NeverRestart(10002501)
def Event_10002501():
    """Event 10002501"""
    IfFlagDisabled(AND_1, 10000500)
    IfFlagDisabled(AND_1, 10000501)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    EndOfAnimation(obj=10001500, animation_id=1)
    DisableObjectActivation(10001501, obj_act_id=219030)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObjectActivation(10001501, obj_act_id=219030)
    IfPlayerInOwnWorld(AND_2)
    IfObjectActivated(AND_2, obj_act_id=10003501)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableNetworkFlag(10000501)
    EnableFlag(10009354)
    Wait(3.0)
    DisableObjectActivation(10001501, obj_act_id=219030)
    ForceAnimation(10001500, 1, unknown2=1.0)


@NeverRestart(10002510)
def Event_10002510():
    """Event 10002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            10000510,
            10000511,
            0,
            10001510,
            10001511,
            10003511,
            10001512,
            10003512,
            10002511,
            10002512,
            10000512,
            10000513,
            10000514,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            10000515,
            10000516,
            1,
            10001515,
            10001516,
            10003516,
            10001517,
            10003517,
            10002516,
            10002517,
            10000517,
            10000518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            10000520,
            10000521,
            0,
            10001520,
            10001521,
            10003521,
            10001522,
            10003522,
            10002521,
            10002522,
            10000522,
            10000523,
            10000524,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(10000519)
def Event_10000519():
    """Event 10000519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(10000515)
    DisableThisSlotFlag()


@RestartOnRest(1002200)
def Event_1002200():
    """Event 1002200"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHasSpecialEffect(MAIN, 10000376, 10180)
    Wait(1.0)
    ForceAnimation(10000389, 3010, unknown2=1.0)
    DisableThisSlotFlag()


@RestartOnRest(10002240)
def Event_10002240(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    left_4: uint,
):
    """Event 10002240"""
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
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    IfUnsignedEqual(AND_9, left=left_4, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    SkipLinesIfUnsignedEqual(1, left=left_4, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Search)
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


@RestartOnRest(10002290)
def Event_10002290(_, character: uint):
    """Event 10002290"""
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)


@RestartOnRest(11002291)
def Event_11002291(_, character: uint, region: uint, seconds: float):
    """Event 11002291"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 30002, unknown2=1.0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=AND_3)
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
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20002, unknown2=1.0)


@RestartOnRest(10002310)
def Event_10002310():
    """Event 10002310"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(10000520)
    ForceAnimation(10000520, 30000, loop=True, unknown2=1.0)
    IfHasAIStatus(AND_1, 10005231, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10002222, min_target_count=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAI(10000520)
    DisableThisSlotFlag()
    ForceAnimation(10000520, 20000, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(10000520, 3004, unknown2=1.0)


@RestartOnRest(10002311)
def Event_10002311(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 10002311"""
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
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterHasSpecialEffect(OR_3, PLAYER, 10000)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=AND_3)
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


@RestartOnRest(10002320)
def Event_10002320():
    """Event 10002320"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(10000294)
    DisableAI(10000294)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10002294)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=10000294, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=10000294, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=10000294, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=10000294, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=10000294, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=10000294, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableCharacter(10000294)
    EnableAI(10000294)
    ForceAnimation(10000294, 20000, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(10002330)
def Event_10002330(_, character: uint, obj: uint):
    """Event 10002330"""
    EndIfThisEventSlotFlagEnabled()
    EnableNetworkSync()
    EnableObject(obj)
    AttachObjectToCharacter(character=character, model_point=50, obj=obj)
    IfCharacterHasSpecialEffect(MAIN, character, 10941)
    DisableObject(obj)
    DestroyObject(obj, request_slot=0)
    DisableThisSlotFlag()


@RestartOnRest(10002340)
def Event_10002340(_, character: uint, obj: uint):
    """Event 10002340"""
    EndIfThisEventSlotFlagEnabled()
    EnableNetworkSync()
    AddSpecialEffect(character, 10940)
    AddSpecialEffect(character, 10943)
    IfObjectDestroyed(MAIN, obj)
    CancelSpecialEffect(character, 10940)
    CancelSpecialEffect(character, 10943)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=character, special_effect=10941)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=10936)
    ForceAnimation(character, 20005, unknown2=1.0)


@RestartOnRest(10002350)
def Event_10002350(_, character: uint, region: uint, seconds: float, flag: uint):
    """Event 10002350"""
    EndIfFlagEnabled(flag)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
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
    Wait(seconds)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)


@RestartOnRest(10002423)
def Event_10002423(_, character: uint):
    """Event 10002423"""
    Kill(character)


@RestartOnRest(10002460)
def Event_10002460():
    """Event 10002460"""
    IfTimeOfDay(MAIN, earliest=(19, 0, 0), latest=(5, 59, 0))
    AddSpecialEffect(10005460, 10930)
    WaitUntilRandomTimeOfDay(earliest=(6, 0, 0), latest=(18, 59, 0))
    CancelSpecialEffect(10005460, 10930)
    Restart()


@RestartOnRest(10002480)
def Event_10002480():
    """Event 10002480"""
    Kill(10000480)


@NeverRestart(1002700)
def Event_1002700(_, character: uint, flag: uint, flag_1: uint):
    """Event 1002700"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(1002680)
def Event_1002680():
    """Event 1002680"""
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=10002680)
    IfInsideMap(AND_1, game_map=STORMVEIL_CASTLE)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(10002681)
    Wait(2.0)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=10002680)
    IfInsideMap(AND_2, game_map=STORMVEIL_CASTLE)
    IfConditionFalse(MAIN, input_condition=AND_2)
    DisableFlag(10002681)
    Wait(2.0)
    Restart()


@RestartOnRest(10002670)
def Event_10002670(_, tutorial_param_id: int, flag: uint):
    """Event 10002670"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfPlayerHasWeapon(OR_15, 33000000, including_storage=True)
    IfPlayerHasWeapon(OR_15, 33210000, including_storage=True)
    IfPlayerHasWeapon(OR_15, 34000000, including_storage=True)
    IfPlayerHasWeapon(OR_15, 34040000, including_storage=True)
    EndIfConditionTrue(input_condition=OR_15)
    IfPlayerHasWeapon(OR_1, 33000000, including_storage=True)
    IfPlayerHasWeapon(OR_1, 33210000, including_storage=True)
    IfPlayerHasWeapon(OR_1, 34000000, including_storage=True)
    IfPlayerHasWeapon(OR_1, 34040000, including_storage=True)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=STORMVEIL_CASTLE)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    Wait(1.0)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9101, flag=flag, bit_count=1)


@RestartOnRest(10002671)
def Event_10002671(_, tutorial_param_id: int, flag: uint):
    """Event 10002671"""
    EndIfTryingToCreateSession()
    IfPlayerHasGood(OR_1, 215000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 240000, including_storage=True)
    IfPlayerHasGood(OR_1, 243000, including_storage=True)
    IfPlayerHasGood(OR_1, 234000, including_storage=True)
    IfPlayerHasGood(OR_1, 244000, including_storage=True)
    IfPlayerHasGood(OR_1, 236000, including_storage=True)
    IfPlayerHasGood(OR_1, 232000, including_storage=True)
    IfPlayerHasGood(OR_1, 212000, including_storage=True)
    IfPlayerHasGood(OR_1, 241000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 233000, including_storage=True)
    IfPlayerHasGood(OR_1, 245000, including_storage=True)
    IfLeavingSession(AND_1)
    IfPlayerDoesNotHaveGood(AND_1, 9111, including_storage=True)
    IfInsideMap(AND_1, game_map=STORMVEIL_CASTLE)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(10002672)
def Event_10002672(_, tutorial_param_id: int, flag: uint):
    """Event 10002672"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfPlayerHasGood(AND_1, 9500)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=STORMVEIL_CASTLE)
    IfPlayerDoesNotHaveGood(AND_1, 9114)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9114, flag=flag, bit_count=1)


@RestartOnRest(10002673)
def Event_10002673(_, tutorial_param_id: int, flag: uint, flag_1: uint, tutorial_param_id_1: int):
    """Event 10002673"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=STORMVEIL_CASTLE)
    IfPlayerDoesNotHaveGood(AND_1, 9116, including_storage=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag_1)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=flag, bit_count=1)


@RestartOnRest(10002680)
def Event_10002680():
    """Event 10002680"""
    CreateObjectVFX(10001680, vfx_id=100, model_point=800)


@RestartOnRest(10002690)
def Event_10002690():
    """Event 10002690"""
    EndIfFlagDisabled(2001)
    DisableNetworkSync()
    IfFlagEnabled(AND_1, 2001)
    IfActionButtonParamActivated(AND_1, action_button_id=9980, entity=10001690)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=90000, anchor_entity=10001690)
    Wait(1.0)
    Restart()


@RestartOnRest(10002691)
def Event_10002691():
    """Event 10002691"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(10007490)
    IfFlagState(MAIN, FlagSetting.On, FlagType.RelativeToThisEventSlot, 10007490)
    Unknown_2003_71(unk_0_4=94)


@RestartOnRest(10003500)
def Event_10003500(_, region: uint):
    """Event 10003500"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_1, character=20000, region=region)
    IfFailedToCreateSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(OR_2, character=20000, region=region)
    IfFailedToCreateSession(OR_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 9621)
    Restart()


@NeverRestart(10002800)
def Event_10002800():
    """Event 10002800"""
    EndIfFlagEnabled(10000800)
    IfHealthLessThanOrEqual(MAIN, 10000800, value=0.0)
    Kill(10005810)
    Kill(10005820)
    CreateVFX(10003820)
    CreateVFX(10003821)
    CreateVFX(10003822)
    Wait(4.0)
    PlaySoundEffect(10000800, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 10000800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 10000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    KillBossAndDisplayBanner(character=10000800, banner_type=BannerType.HollowArenaLoss)
    SkipLinesIfPlayerNotInOwnWorld(1)
    TriggerMultiplayerEvent(event_id=0)
    EnableNetworkFlag(10000800)
    EnableFlag(9101)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61101)
    SkipLinesIfFlagDisabled(1, 10002802)
    EnableFlag(10000802)
    Unknown_2003_68(unknown1=0, unknown2=1000.0, unknown3=0)
    DeleteVFX(10003810)
    DeleteVFX(10003811)
    EnableObjectActivation(10001540, obj_act_id=219001)
    IfPlayerStandingOnCollision(AND_9, 10003840)
    IfConditionFalse(MAIN, input_condition=AND_9)
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=False)


@RestartOnRest(10002810)
def Event_10002810():
    """Event 10002810"""
    GotoIfFlagDisabled(Label.L0, flag=10000800)
    DisableCharacter(10000800)
    DisableAnimations(10000800)
    Kill(10000800)
    DisableObject(10001870)
    EnableObject(10001871)
    DisableObject(10001820)
    GotoIfFlagEnabled(Label.L10, flag=10000802)
    EnableObject(10001890)
    DisableObject(10001891)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableObject(10001890)
    EnableObject(10001891)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(10001540, obj_act_id=219001)
    DisableAI(10000800)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown18)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown17)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfFlagEnabled(Label.L1, flag=10000801)
    ForceAnimation(10000800, 30000, loop=True, unknown2=1.0)
    EnableObject(10001870)
    DisableObject(10001871)
    EnableObject(10001890)
    DisableObject(10001891)
    IfFlagEnabled(AND_2, 10002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=10002800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DeleteVFX(10003830)
    DeleteVFX(10003831)
    DeleteVFX(10003832)
    DeleteVFX(10003833)
    DeleteVFX(10003834)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=10000020,
        cutscene_flags=0,
        move_to_region=10002810,
        map_base_id=10000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(10000020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=19.0, unknown2=137.8300018310547)
    CreateVFX(10003830)
    CreateVFX(10003831)
    CreateVFX(10003832)
    CreateVFX(10003833)
    CreateVFX(10003834)
    DisableObject(10001870)
    EnableObject(10001871)
    Move(10000800, destination=10001895, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    DisableObject(10001820)
    ForceAnimation(10000800, 20000, unknown2=1.0)
    EnableNetworkFlag(10000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(10001870)
    EnableObject(10001871)
    EnableObject(10001890)
    DisableObject(10001891)
    DisableObject(10001820)
    Move(10000800, destination=10001895, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    IfFlagEnabled(AND_2, 10002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=10002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(10000800)
    SetNetworkUpdateRate(10005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(10000800, name=904750000)


@RestartOnRest(10002811)
def Event_10002811():
    """Event 10002811"""
    EndIfFlagEnabled(10000800)
    IfCharacterHasSpecialEffect(OR_1, 10000800, 14785)
    IfFlagEnabled(OR_1, 10000800)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(10000800)
    IfHealthValueLessThanOrEqual(AND_14, PLAYER, value=0)
    IfCharacterOutsideRegion(AND_14, character=PLAYER, region=10002156)
    EndIfConditionTrue(input_condition=AND_14)
    IfHealthValueLessThanOrEqual(AND_15, PLAYER, value=0)
    IfCharacterInsideRegion(AND_15, character=PLAYER, region=10002156)
    GotoIfConditionTrue(Label.L15, input_condition=AND_15)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=10000030,
        cutscene_flags=0,
        move_to_region=10002811,
        map_base_id=10000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(10000030, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(10002802)
    Move(10000800, destination=10001895, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    AddSpecialEffect(10000800, 14750)
    SetDisplayMask(10000800, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=20, switch_type=OnOffChange.Off)
    SetDisplayMask(10000800, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=29, switch_type=OnOffChange.Off)
    SetDisplayMask(10000800, bit_index=30, switch_type=OnOffChange.Off)
    DisableObject(10001890)
    EnableObject(10001891)
    ForceAnimation(10000800, 20011, wait_for_completion=True, unknown2=1.0)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    SkipLinesIfPlayerNotInOwnWorld(2)
    PlayCutscene(10000030, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(10000030, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(10002802)
    AddSpecialEffect(10000800, 14750)
    SetDisplayMask(10000800, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=20, switch_type=OnOffChange.Off)
    SetDisplayMask(10000800, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(10000800, bit_index=29, switch_type=OnOffChange.Off)
    SetDisplayMask(10000800, bit_index=30, switch_type=OnOffChange.Off)
    DisableObject(10001890)
    EnableObject(10001891)
    ForceAnimation(10000800, 20011, wait_for_completion=True, unknown2=1.0)
    End()


@RestartOnRest(10002820)
def Event_10002820(_, region: uint, special_effect_id: int, special_effect_id_1: int):
    """Event 10002820"""
    EndIfFlagEnabled(10000800)
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(AND_1, character=10000800, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(10000800, special_effect_id)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_2, character=10000800, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(0.10000000149011612)
    AddSpecialEffect(10000800, special_effect_id_1)
    Restart()


@RestartOnRest(10002821)
def Event_10002821(_, region: uint, special_effect_id: int, special_effect_id_1: int):
    """Event 10002821"""
    EndIfFlagEnabled(10000800)
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, special_effect_id)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_2, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(0.10000000149011612)
    AddSpecialEffect(20000, special_effect_id_1)
    Restart()


@RestartOnRest(10002824)
def Event_10002824(_, region: uint, special_effect_id: int, special_effect_id_1: int):
    """Event 10002824"""
    EndIfFlagEnabled(10000800)
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(AND_1, character=10000800, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(10000800, special_effect_id)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_2, character=10000800, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(0.10000000149011612)
    AddSpecialEffect(10000800, special_effect_id_1)
    Restart()


@RestartOnRest(10002825)
def Event_10002825(_, region: uint, special_effect_id: int, special_effect_id_1: int):
    """Event 10002825"""
    EndIfFlagEnabled(10000800)
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, special_effect_id)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_2, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(0.10000000149011612)
    AddSpecialEffect(20000, special_effect_id_1)
    Restart()


@RestartOnRest(10002849)
def Event_10002849():
    """Event 10002849"""
    RunCommonEvent(
        0,
        9005800,
        args=(10000800, 10001800, 10002800, 10002805, 10005800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(10000800, 10001800, 10002800, 10002805, 10002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(10000800, 10001800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(10000800, 475000, 10002805, 10002806, 0, 10002802, 1, 1), arg_types="IiIIIIii")


@NeverRestart(10002850)
def Event_10002850():
    """Event 10002850"""
    EndIfFlagEnabled(10000850)
    IfHealthValueLessThanOrEqual(MAIN, 10000850, value=0)
    Wait(2.0)
    PlaySoundEffect(10000850, 77777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 10000850)
    Kill(10000850)
    KillBossAndDisplayBanner(character=10000850, banner_type=BannerType.Unknown)
    EnableFlag(10000850)
    EnableFlag(9100)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61100)


@RestartOnRest(10002860)
def Event_10002860():
    """Event 10002860"""
    GotoIfFlagDisabled(Label.L0, flag=10000850)
    DisableCharacter(10000850)
    DisableAnimations(10000850)
    Kill(10000850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(10000850)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableThisSlotFlag()
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfUnknownCharacterCondition_31(OR_15, character=PLAYER, unk_4_8=7, unk_8_12=1.0)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfThisEventSlotFlagEnabled(Label.L2)
    GotoIfFlagEnabled(Label.L1, flag=10000851)
    DisableCharacter(10000850)
    Unknown_2004_73(entity=10000850, unk_4_8=0)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=10000850, other_entity=PLAYER, radius=25.0)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=10000850, attacker=0)
    IfConditionTrue(AND_10, input_condition=OR_1)
    IfFlagDisabled(AND_10, 10000850)
    IfConditionTrue(MAIN, input_condition=AND_10)
    Unknown_2004_73(entity=10000850, unk_4_8=0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=10000010,
        cutscene_flags=0,
        move_to_region=10002852,
        map_base_id=10000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(10000010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableCharacter(10000850)
    ForceAnimation(10000850, 20000, unknown2=1.0)
    EnableNetworkFlag(10000851)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 10002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=10002850)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(10000850)
    SetNetworkUpdateRate(10000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(10000850, name=902130000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(10002861)
def Event_10002861():
    """Event 10002861"""
    EndIfFlagEnabled(10000850)
    IfCharacterHasSpecialEffect(AND_1, 10000850, 16205)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(10002852)


@RestartOnRest(10002870)
def Event_10002870():
    """Event 10002870"""
    EndIfFlagEnabled(10000850)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfHealthValueEqual(AND_1, 10000850, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(10000850, True)
    IfFlagEnabled(AND_2, 10002705)
    IfTimeElapsed(AND_2, seconds=50.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetBackreadStateAlternate(10000850, False)


@RestartOnRest(10002889)
def Event_10002889():
    """Event 10002889"""
    RunCommonEvent(
        0,
        9005800,
        args=(10000850, 10001850, 10002850, 10002855, 10000850, 10000, 10000851, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(10000850, 10001850, 10002850, 10002855, 10002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(10000850, 10001850, 3, 10000851), arg_types="IIiI")
    RunCommonEvent(0, 9005813, args=(10000850, 10001851, 3, 10000851, 806760), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(10000850, 213000, 10002855, 10002856, 0, 10002852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(10003700)
def Event_10003700(_, character: uint, obj: uint):
    """Event 10003700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    DisableNetworkFlag(10009350)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3260)
    DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3265, 3268))
    IfFlagEnabled(AND_1, 10009514)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    IfFlagRangeAnyEnabled(AND_2, flag_range=(3265, 3268))
    IfFlagEnabled(AND_2, 10009514)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAnyEnabled(AND_10, flag_range=(3265, 3268))
    IfFlagEnabled(AND_10, 10009514)
    IfConditionFalse(MAIN, input_condition=AND_10)
    Restart()


@RestartOnRest(10003701)
def Event_10003701(_, character: uint, obj: uint, flag: uint, flag_1: uint):
    """Event 10003701"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3260)
    DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3265, 3268))
    IfFlagEnabled(AND_1, flag)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    IfFlagRangeAnyEnabled(AND_2, flag_range=(3265, 3268))
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_5, flag_1)
    IfFlagEnabled(AND_5, 9000)
    GotoIfConditionTrue(Label.L20, input_condition=AND_5)
    SkipLinesIfFlagDisabled(1, 10009510)
    EnableFlag(10009390)
    SkipLinesIfFlagDisabled(1, 10009511)
    EnableFlag(10009391)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930014, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 10009512)
    ForceAnimation(character, 930015, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAnyEnabled(AND_10, flag_range=(3265, 3268))
    IfFlagEnabled(AND_10, flag)
    IfConditionFalse(MAIN, input_condition=AND_10)
    Restart()


@RestartOnRest(10003702)
def Event_10003702(_, character: uint):
    """Event 10003702"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3260)
    DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3269)
    IfFlagEnabled(OR_1, 3269)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930020, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(OR_10, 3269)
    IfConditionTrue(MAIN, input_condition=OR_10)
    Restart()


@RestartOnRest(10003703)
def Event_10003703(_, character: uint):
    """Event 10003703"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3260)
    DisableFlag(10009398)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3270)
    IfFlagEnabled(OR_1, 3270)
    AwaitConditionTrue(OR_1)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3260)
    GotoIfFlagEnabled(Label.L2, flag=3261)
    GotoIfFlagEnabled(Label.L4, flag=3263)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20019, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(OR_10, 3270)
    AwaitConditionTrue(OR_10)
    Restart()
    End()


@RestartOnRest(10003705)
def Event_10003705(_, entity: uint):
    """Event 10003705"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3263)
    IfFlagEnabled(MAIN, 3261)
    ForceAnimation(entity, 20019, unknown2=1.0)


@RestartOnRest(10003710)
def Event_10003710():
    """Event 10003710"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=10002709)
    EnableNetworkFlag(10002765)
    EnableNetworkFlag(3278)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=10002709)
    Restart()


@RestartOnRest(10003711)
def Event_10003711(_, first_flag: uint, last_flag: uint, flag: uint, region: uint):
    """Event 10003711"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3261)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    IfFlagEnabled(MAIN, 10009397)
    SkipLinesIfCharacterInsideRegion(line_count=1, character=PLAYER, region=10002704)
    EndIfFlagEnabled(10009360)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=region)
    Restart()


@RestartOnRest(10003715)
def Event_10003715(
    _,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    first_flag_1: uint,
    last_flag_1: uint,
    flag_1: uint,
    region: uint,
):
    """Event 10003715"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3261)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    IfFlagEnabled(MAIN, 10009397)
    SkipLinesIfFlagDisabled(4, flag)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    DisableNetworkConnectedFlagRange(flag_range=(first_flag_1, last_flag_1))
    EnableNetworkFlag(flag_1)
    EnableNetworkFlag(3278)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=region)
    Restart()


@RestartOnRest(10003720)
def Event_10003720(_, flag: uint, flag_1: uint):
    """Event 10003720"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkFlag(10009389)
    SkipLinesIfFlagDisabled(1, flag)
    EnableNetworkFlag(flag_1)
    IfFlagEnabled(MAIN, 10009389)
    Restart()


@RestartOnRest(10003724)
def Event_10003724():
    """Event 10003724"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3260)
    EndIfFlagEnabled(10009351)
    EndIfFlagEnabled(10002722)
    GotoIfFlagDisabled(Label.L0, flag=10002720)
    GotoIfFlagEnabled(Label.L1, flag=10002720)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=10002715)
    EnableFlag(10002769)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(10002769)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    IfTimeElapsed(OR_1, seconds=18.0)
    IfFlagEnabled(OR_2, 10009351)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10002716)
    IfTimeElapsed(AND_1, seconds=8.0)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfCharacterInsideRegion(OR_4, character=PLAYER, region=10002716)
    IfConditionTrue(OR_15, input_condition=OR_1)
    IfConditionTrue(OR_15, input_condition=OR_2)
    IfConditionTrue(OR_15, input_condition=OR_3)
    IfConditionTrue(OR_15, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=OR_15)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=OR_4)

    # --- Label 3 --- #
    DefineLabel(3)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(10002721)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(10002722)
    End()


@RestartOnRest(10003726)
def Event_10003726():
    """Event 10003726"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10000755)
    IfFlagEnabled(AND_1, 3260)
    IfFlagDisabled(AND_1, 3261)
    IfFlagEnabled(AND_1, 10002731)
    IfFlagDisabled(AND_1, 10009354)
    IfFlagDisabled(AND_1, 10009355)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(10009500)


@RestartOnRest(10003728)
def Event_10003728(_, region: uint):
    """Event 10003728"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(10009502)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfFlagEnabled(AND_1, 10009351)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(10009502)
    End()


@RestartOnRest(10003729)
def Event_10003729(_, region: uint):
    """Event 10003729"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    EnableNetworkFlag(10009356)
    End()


@RestartOnRest(10003730)
def Event_10003730():
    """Event 10003730"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    GotoIfFlagEnabled(Label.L20, flag=10009373)
    DisableNetworkFlag(10009370)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=10000703, radius=24.0)
    IfFlagEnabled(AND_3, 10009512)
    IfFlagEnabled(AND_3, 3260)
    IfFlagDisabled(AND_3, 3261)
    IfConditionTrue(MAIN, input_condition=AND_3)
    EnableNetworkFlag(10009370)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(10003731)
def Event_10003731():
    """Event 10003731"""
    IfFlagDisabled(AND_1, 10009374)
    IfFlagDisabled(AND_1, 10009377)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    IfFlagEnabled(AND_2, 10009374)
    IfFlagDisabled(AND_2, 10009377)
    GotoIfConditionTrue(Label.L5, input_condition=AND_2)
    EndIfFlagEnabled(10009377)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_1, 10009374)
    IfFlagEnabled(OR_2, 10009377)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    EndIfFinishedConditionTrue(input_condition=OR_2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkFlag(10000562)
    DisableNetworkFlag(10008562)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=10000050,
        cutscene_flags=0,
        move_to_region=10002712,
        map_base_id=10000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    Goto(Label.L2)
    IfUnknownCharacterCondition_31(OR_1, character=PLAYER, unk_4_8=1, unk_8_12=1.0)
    IfUnknownCharacterCondition_31(OR_1, character=PLAYER, unk_4_8=7, unk_8_12=1.0)
    SkipLinesIfConditionFalse(2, OR_1)
    UnknownCutscene_11(
        cutscene_id=10000050,
        cutscene_flags=0,
        move_to_region=10002713,
        map_base_id=10000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    Goto(Label.L2)
    PlayCutsceneToAll(cutscene_id=10000050, cutscene_flags=0)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(10009374)
    DisableNetworkFlag(10000562)
    DisableNetworkFlag(10008562)
    SkipLinesIfPlayerNotInOwnWorld(4)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=0)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=1)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=2)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=3)
    EndOfAnimation(obj=10001562, animation_id=1)
    Wait(3.0)
    DisableNetworkFlag(10000562)
    DisableNetworkFlag(10008562)
    EndOfAnimation(obj=10001562, animation_id=1)
    IfCharacterOutsideRegion(AND_5, character=PLAYER, region=10002711)
    IfCharacterHuman(AND_5, PLAYER)
    IfCharacterDead(OR_5, 10000281)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfConditionTrue(MAIN, input_condition=OR_5)
    EnableNetworkFlag(10009377)
    EnableObjectActivation(10001562, obj_act_id=1219000, relative_index=0)
    EnableObjectActivation(10001562, obj_act_id=1219000, relative_index=1)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=2)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=3)
    IfObjectActivated(MAIN, obj_act_id=10003562)
    EnableFlag(10000562)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=0)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=1)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=2)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=3)
    End()


@RestartOnRest(10003732)
def Event_10003732():
    """Event 10003732"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L1, flag=10009374)
    IfFlagEnabled(AND_1, 10009374)
    IfFlagDisabled(AND_1, 10009377)
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    EndIfFlagEnabled(10009377)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(OR_1, 10009374)
    IfFlagEnabled(OR_2, 10009377)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_1)
    EndIfFinishedConditionTrue(input_condition=OR_2)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    IfActionButtonParamActivated(OR_4, action_button_id=9000, entity=10001562)
    IfFlagEnabled(OR_4, 10009377)
    IfConditionTrue(MAIN, input_condition=OR_4)
    EndIfFlagEnabled(10009377)
    SkipLinesIfFlagEnabled(2, 10009377)
    DisplayDialog(text=4001, anchor_entity=10001562, display_distance=1.0, number_buttons=NumberButtons.OneButton)
    Restart()
    End()


@RestartOnRest(10003733)
def Event_10003733():
    """Event 10003733"""
    GotoIfFlagDisabled(Label.L0, flag=10009374)
    IfFlagEnabled(AND_1, 10009374)
    IfFlagDisabled(AND_1, 10009377)
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    EndIfFlagEnabled(10009377)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_1, 10009374)
    IfCharacterDead(OR_2, 10000281)
    IfFlagEnabled(OR_3, 3263)
    IfFlagRangeAllDisabled(OR_4, flag_range=(3265, 3268))
    IfConditionTrue(OR_5, input_condition=OR_1)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_3)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_1)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(10009377)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    IfCharacterOutsideRegion(AND_6, character=PLAYER, region=10002711)
    IfCharacterHuman(AND_6, PLAYER)
    IfCharacterDead(OR_6, 10000281)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfConditionTrue(MAIN, input_condition=OR_6)
    EnableNetworkFlag(10009377)
    DisableNetworkFlag(10000562)
    EnableObjectActivation(10001562, obj_act_id=1219000, relative_index=0)
    EnableObjectActivation(10001562, obj_act_id=1219000, relative_index=1)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=2)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=3)
    IfObjectActivated(MAIN, obj_act_id=10003562)
    EnableFlag(10000562)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=0)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=1)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=2)
    DisableObjectActivation(10001562, obj_act_id=1219000, relative_index=3)
    End()


@RestartOnRest(10003734)
def Event_10003734():
    """Event 10003734"""
    IfFlagDisabled(AND_1, 3263)
    IfFlagEnabled(AND_1, 10009397)
    IfFlagDisabled(AND_1, 10009374)
    IfCharacterDead(AND_1, 10000651, target_comparison_type=ComparisonType.NotEqual)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10002710)
    IfCharacterHuman(AND_1, PLAYER)
    IfFlagDisabled(AND_1, 10009377)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(10009374)
    End()


@RestartOnRest(10003735)
def Event_10003735():
    """Event 10003735"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, 10009374)
    IfFlagDisabled(AND_1, 10009377)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    IfFlagEnabled(AND_2, 10009374)
    IfFlagDisabled(AND_2, 10009377)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_1, 10009374)
    IfFlagEnabled(OR_1, 10009377)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, PLAYER, 4283)
    AddSpecialEffect(PLAYER, 4282)
    IfFlagDisabled(OR_2, 10009374)
    IfFlagEnabled(OR_2, 10009377)
    IfConditionTrue(MAIN, input_condition=OR_2)
    AddSpecialEffect(PLAYER, 4283)
    Restart()


@RestartOnRest(10003736)
def Event_10003736():
    """Event 10003736"""
    EndIfPlayerNotInOwnWorld()
    IfInsideMap(MAIN, game_map=STORMVEIL_CASTLE)
    Unknown_2003_72(unk_0_4=0.0, unk_4_8=-1)
    IfFlagRangeAnyEnabled(OR_1, flag_range=(10009510, 10009513))
    IfFlagEnabled(AND_1, 10009360)
    IfFlagEnabled(AND_1, 10009362)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, 3263)
    IfFlagRangeAllDisabled(OR_2, flag_range=(3265, 3268))
    IfOutsideMap(OR_3, game_map=STORMVEIL_CASTLE)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_2)
    Unknown_2003_72(unk_0_4=0.0, unk_4_8=-1)
    End()
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_3)
    Unknown_2003_72(unk_0_4=0.0, unk_4_8=-1)
    Restart()
    Unknown_2003_72(unk_0_4=0.30000001192092896, unk_4_8=0)
    IfFlagRangeAllDisabled(OR_5, flag_range=(10009510, 10009513))
    IfFlagEnabled(AND_5, 10009360)
    IfFlagEnabled(AND_5, 10009362)
    IfConditionTrue(OR_6, input_condition=AND_5)
    IfFlagEnabled(OR_6, 3263)
    IfFlagRangeAllDisabled(OR_6, flag_range=(3265, 3268))
    IfOutsideMap(OR_7, game_map=STORMVEIL_CASTLE)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(OR_8, input_condition=OR_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    Unknown_2003_72(unk_0_4=0.0, unk_4_8=-1)
    EndIfFinishedConditionTrue(input_condition=OR_6)
    Restart()


@RestartOnRest(10003737)
def Event_10003737():
    """Event 10003737"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3263)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(2600, 2629))
    Unknown_2003_73(unk_4_8=10000700, unk_8_12=0, unk_12_16=0)
    Unknown_2003_73(unk_4_8=10000701, unk_8_12=0, unk_12_16=0)
    Unknown_2003_73(unk_4_8=10000702, unk_8_12=0, unk_12_16=0)
    Unknown_2003_73(unk_4_8=10000703, unk_8_12=0, unk_12_16=0)
    Unknown_2003_73(unk_4_8=10000704, unk_8_12=0, unk_12_16=0)
    End()


@RestartOnRest(10003738)
def Event_10003738():
    """Event 10003738"""
    DisableObject(10001710)
    IfFlagEnabled(OR_1, 10009377)
    IfFlagEnabled(OR_1, 10003738)
    EndIfConditionTrue(input_condition=OR_1)
    SkipLinesIfHost(2)
    EnableObject(10001710)
    CreateObjectVFX(10001710, vfx_id=101, model_point=3)
    IfCharacterOutsideRegion(AND_5, character=PLAYER, region=10002711)
    IfCharacterHuman(AND_5, PLAYER)
    IfFlagEnabled(AND_6, 10009377)
    IfConditionTrue(AND_6, input_condition=AND_5)
    IfConditionTrue(MAIN, input_condition=AND_6)
    DisableObject(10001710)
    DeleteObjectVFX(10001710)
    End()


@RestartOnRest(10000739)
def Event_10000739():
    """Event 10000739"""
    EnableInvincibility(10000281)
    IfFlagEnabled(OR_1, 10009374)
    IfFlagEnabled(OR_1, 10009377)
    IfFlagEnabled(OR_1, 10000379)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableInvincibility(10000281)
    End()


@RestartOnRest(10003740)
def Event_10003740(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003740"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    IfTimeElapsed(OR_1, seconds=seconds)
    IfFlagDisabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003741)
def Event_10003741(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003741"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    IfTimeElapsed(OR_1, seconds=seconds)
    IfFlagDisabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003742)
def Event_10003742(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003742"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    IfTimeElapsed(OR_1, seconds=seconds)
    IfFlagDisabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003743)
def Event_10003743(_, character: uint, special_effect: int, flag: uint, seconds: float):
    """Event 10003743"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    IfTimeElapsed(OR_1, seconds=seconds)
    IfFlagDisabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(10003744)
def Event_10003744(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 10003744"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=character, distance=17.0)
    SkipLinesIfUnsignedEqual(1, left=0, right=character_1)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    EndIfFlagEnabled(flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, flag_1)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    SkipLinesIfUnsignedEqual(1, left=0, right=character_1)
    SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(10003745)
def Event_10003745(_, character: uint):
    """Event 10003745"""
    DisableCharacter(character)
    DisableBackread(character)
    EndIfFlagDisabled(10000800)
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    ForceAnimation(character, 930000, unknown2=1.0)
    End()


@RestartOnRest(10000760)
def Event_10000760(_, character: uint):
    """Event 10000760"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 3905)
    IfFlagDisabled(AND_1, 10002164)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_2, 3905)
    IfFlagDisabled(AND_2, 10002164)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3900)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(AND_3, 3905)
    IfFlagDisabled(AND_3, 10002164)
    IfConditionFalse(MAIN, input_condition=AND_3)
    Restart()


@RestartOnRest(10000761)
def Event_10000761():
    """Event 10000761"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(9101)
    IfFlagEnabled(MAIN, 9101)
    EnableFlag(3918)


@RestartOnRest(10000762)
def Event_10000762():
    """Event 10000762"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11109528)
    IfFlagEnabled(MAIN, 10000291)
    EnableFlag(11109528)


@NeverRestart(10000763)
def Event_10000763(_, obj: uint, radius: float):
    """Event 10000763"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=10009610)
    IfFlagEnabled(OR_1, 10009617)
    IfFlagRangeAnyEnabled(OR_1, flag_range=(3907, 3917))
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=obj, radius=radius)
    IfFlagDisabled(AND_1, 10002164)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(10009610)
    EnableFlag(3918)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=100, model_point=42)


@RestartOnRest(10000764)
def Event_10000764(_, character: uint, entity: uint):
    """Event 10000764"""
    DisableNetworkSync()
    DisableCharacter(character)
    DisableBackread(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5005)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=10009610)
    IfFlagEnabled(MAIN, 10009610)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    IfActionButtonParamActivated(MAIN, action_button_id=6511, entity=entity)
    EnableCharacter(character)
    EnableBackread(character)
    IfCharacterBackreadEnabled(MAIN, character)
    ResetAnimation(character, disable_interpolation=True)
    Wait(0.6000000238418579)
    ForceAnimation(character, 90203, unknown2=1.0)
    Wait(8.0)
    Unknown_2004_81(character=character)
    DisableCharacter(character)
    DisableBackread(character)
    Restart()


@RestartOnRest(10003770)
def Event_10003770(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 10003770"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372701)
    IfFlagDisabled(OR_1, flag)
    IfEntityBeyondDistance(OR_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(10003771)
def Event_10003771(_, other_entity: uint, flag: uint):
    """Event 10003771"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4680)
    IfFlagEnabled(MAIN, 4680)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(10003772)
def Event_10003772(_, other_entity: uint, flag: uint):
    """Event 10003772"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(MAIN, 1042379203)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(10003773)
def Event_10003773(_, other_entity: uint, flag: uint):
    """Event 10003773"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379207)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372702)
    IfEntityBeyondDistance(MAIN, entity=20000, other_entity=other_entity, radius=5.0)
    DisableFlag(1042372702)
    Restart()


@RestartOnRest(10003775)
def Event_10003775(_, character: uint, character_1: uint):
    """Event 10003775"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4220)
    DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 4225)
    IfFlagDisabled(OR_1, 10002160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(AND_2, 4225)
    IfFlagDisabled(OR_2, 10002160)
    IfConditionTrue(AND_2, input_condition=OR_2)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 30015, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    EnableCharacter(10000731)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(10000731)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(10000731)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(OR_15, 4225)
    IfFlagEnabled(OR_15, 10002160)
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(10003776)
def Event_10003776(_, character: uint):
    """Event 10003776"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4220)
    DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4229)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4229)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

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
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4229)
    Restart()
    End()


@RestartOnRest(10003777)
def Event_10003777():
    """Event 10003777"""
    EndIfFlagEnabled(9101)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 10002160)
    IfFlagEnabled(AND_1, 9101)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(10009707)
    End()


@RestartOnRest(10003778)
def Event_10003778():
    """Event 10003778"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=10000730, distance=17.0)
    EndIfFlagEnabled(10009705)
    SetCharacterTalkRange(character=10000730, distance=40.0)
    IfFlagEnabled(AND_1, 4225)
    IfFlagDisabled(AND_1, 10009705)
    IfFlagDisabled(AND_1, 10002785)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10002735)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(10002784)
    End()


@RestartOnRest(10003779)
def Event_10003779():
    """Event 10003779"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(4221, 4223))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(10009709)
    End()


@RestartOnRest(10003780)
def Event_10003780():
    """Event 10003780"""
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagEnabled(2, 9101)
    AwaitFlagEnabled(flag=9101)
    EnableNetworkFlag(10002786)
    IfFlagEnabled(OR_1, 4229)
    IfFlagDisabled(OR_1, 9101)
    IfFlagDisabled(OR_1, 9104)
    IfFlagDisabled(OR_1, 11109921)
    IfFlagEnabled(OR_1, 10009722)
    IfFlagEnabled(OR_1, 10002786)
    EndIfConditionTrue(input_condition=OR_1)
    SkipLinesIfFlagEnabled(2, 10009720)
    EnableNetworkFlag(10009720)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 10009721)
    EnableNetworkFlag(10009721)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 10009722)
    EnableNetworkFlag(10009722)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableNetworkFlag(10002786)
    End()


@RestartOnRest(10003790)
def Event_10003790(_, character: uint):
    """Event 10003790"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3580)
    DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3587)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_1, 3587)
    AwaitConditionTrue(AND_1)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3580)
    GotoIfFlagEnabled(Label.L2, flag=3581)
    GotoIfFlagEnabled(Label.L4, flag=3583)

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
    IfFlagDisabled(AND_15, 3587)
    AwaitConditionTrue(AND_15)
    Restart()
    End()


@RestartOnRest(10002910)
def Event_10002910():
    """Event 10002910"""
    EndIfFlagEnabled(10000800)
    IfFlagEnabled(OR_1, 10002160)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableMapCollision(collision=10004910)
