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
    RegisterGrace(grace_flag=11000002, obj=11001952, unknown=5.0)
    RegisterGrace(grace_flag=11000003, obj=11001953, unknown=5.0)
    RegisterGrace(grace_flag=11000004, obj=11001954, unknown=5.0)
    RegisterGrace(grace_flag=11000005, obj=11001955, unknown=5.0)
    RegisterGrace(grace_flag=11000006, obj=11001956, unknown=5.0)
    RegisterGrace(grace_flag=11000007, obj=11001957, unknown=5.0)
    RegisterGrace(grace_flag=11000008, obj=11001958, unknown=5.0)
    RegisterGrace(grace_flag=11000009, obj=11001959, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(11000500, 11000000, 11000950, 11001950, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(11000850, 11000001, 11000951, 11001951, 5.0), arg_types="IIIIf")
    Event_11002800()
    Event_11002810()
    Event_11002811()
    Event_11002829()
    Event_11002850()
    Event_11002860()
    Event_11002859()
    Event_11002500()
    Event_11002501()
    Event_11002502()
    Event_11002503()
    RunCommonEvent(
        0,
        90005501,
        args=(11000510, 11000511, 0, 11001510, 11001511, 11001512, 11000512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11000515, 11000516, 0, 11001515, 11001516, 11001517, 11000517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11000520, 11000521, 0, 11001520, 11001521, 11001522, 11000522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11000525, 11000526, 0, 11001525, 11001526, 11001527, 11000527),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11000530, 11000531, 0, 11001530, 11001531, 11001532, 11000532),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11000535, 11000536, 1, 11001535, 11001536, 11001537, 11000537),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11000610, 11000611, 2, 11001610, 11001611, 11001612, 11000612),
        arg_types="IIIIIII",
    )
    Event_11002510()
    Event_11000602()
    RunCommonEvent(0, 90005513, args=(11000540, 11001540, 11001541, 11003541, 1227050, 1, 2), arg_types="IIIIiii")
    Event_11002546(
        0,
        flag=11000546,
        obj=11001546,
        obj_1=11001547,
        obj_act_id=11003547,
        obj_act_id_1=1227050,
        animation_id=1,
        animation_id_1=2
    )
    Event_11002547()
    RunCommonEvent(0, 90005511, args=(11000560, 11001560, 11003560, 227010, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(11000560, 11002560, 11002561), arg_types="III")
    RunCommonEvent(0, 90005511, args=(11000562, 11001562, 11003562, 227010, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(11000562, 11002562, 11002563), arg_types="III")
    RunCommonEvent(0, 90005511, args=(11000564, 11001564, 11003564, 227070, 0), arg_types="IIIiI")
    Event_11002540()
    Event_11000600()
    Event_11002601()
    Event_11002603()
    Event_11002580()
    RunCommonEvent(0, 90005520, args=(11000576, 11001576, 11002576, 11002577), arg_types="IIII")
    RunCommonEvent(0, 90005520, args=(11000578, 11001578, 11002578, 11002579), arg_types="IIII")
    Event_11002690()
    Event_11002691(0, obj=11001691)
    RunCommonEvent(
        0,
        90005605,
        args=(11001692, 34, 15, 0, 0, 34152692, 11000000, 11002692, 11002693, 11002694, 11000600, 30040, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(0, 90005632, args=(580050, 11001695, 80050), arg_types="IIi")
    RunCommonEvent(0, 90005570, args=(60822, 52, 11001391, 0, 1, 0), arg_types="IiIiii")
    Event_11002203(0, character=11000203, region=11002216)
    Event_11002205(0, character=11000203, region=11002215)
    Event_11002207(0, character=11000203, flag=11002216)
    Event_11002209(0, character=11000203, flag=11002215)
    Event_11002203(1, character=11000205, region=11002218)
    Event_11002205(1, character=11000205, region=11002217)
    Event_11002207(1, character=11000205, flag=11002218)
    Event_11002209(1, character=11000205, flag=11002217)
    Event_11002260(5, 11000265, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(6, 11000266, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(7, 11000267, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(8, 11000268, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(9, 11000269, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(10, 11000270, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(11, 11000271, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(12, 11000272, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(13, 11000273, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(14, 11000274, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(15, 11000275, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(16, 11000276, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(17, 11000277, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(18, 11000278, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(19, 11000279, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(20, 11000280, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(21, 11000281, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(22, 11000282, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(23, 11000283, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(24, 11000284, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(25, 11000285, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(26, 11000286, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(27, 11000287, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(28, 11000288, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    Event_11002260(29, 11000289, 30000, 20000, 0.0, 0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005300, args=(11000393, 11000393, 11001187, 2.0, 0), arg_types="IIifi")
    Event_11002402(2, 11000252, 30000, 20000, 11002243, 0.0, 0, 1, 0, 0, 1)
    Event_11002402(0, 11000254, 30000, 20000, 11002254, 2.0, 0, 1, 0, 0, 1)
    Event_11002402(1, 11000259, 30000, 20000, 11002259, 0.0, 0, 1, 1, 1, 1)
    Event_11002317(0, 11000408, 11002359, 0.0, 5.0)
    Event_11002317(1, 11000420, 11002359, 0.0, 10.0)
    RunCommonEvent(0, 90005300, args=(11000389, 11000389, 11001198, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000399, 11000399, 11000185, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000495, 11000495, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000496, 11000496, 0, 0.0, 0), arg_types="IIifi")
    Event_11002497(0, 11000497, 11002497, 0.0)
    RunCommonEvent(0, 90005300, args=(11000497, 11000497, 11001193, 0.0, 0), arg_types="IIifi")
    Event_11002402(4, 11000397, 30001, 20001, 11002625, 0.0, 0, 1, 1, 1, 1)
    RunCommonEvent(0, 90005300, args=(11000498, 11000498, 0, 2.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000499, 11000499, 11000195, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000484, 11000484, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000665, 11000665, 40370, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000666, 11000666, 40372, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000667, 11000667, 40374, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(11000299, 11000299, 11001000, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 9005811, args=(11000850, 11001930, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001931, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001932, 5, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        90005795,
        args=(7605, 0, 11009500, 11002141, 11002142, 80605, 9000, 11001710, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=20)
    Event_11002155(0, flag=7605, character=11000740, character_1=11000745, banner_type=5, entity_id=11002141)
    Event_11002145()
    RunCommonEvent(
        0,
        90005780,
        args=(11000800, 11002164, 11002165, 11000730, 20, 11002164, 0, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(11000800, 11002164, 11002165, 11000730), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(11002164, 11002805, 11000730, 11002800, 11002809, 20029), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005780,
        args=(11000800, 11002168, 11002169, 11000760, 20, 11002761, 35009317, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(11000800, 11002168, 11002169, 11000760), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(11002168, 11002805, 11000760, 11002800, 11002809, 0), arg_types="IIIIIi")
    RunCommonEvent(0, 90005703, args=(11000710, 3941, 3942, 1039409251, 3941, 3940, 3943, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(11000710, 3941, 3940, 1039409251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(11000710, 3943, 3940, 3944), arg_types="IIII")
    Event_11003710(0, character=11000710)
    Event_11003711(0, entity=11000710)
    Event_11003715(0, character=11000720)
    Event_11003720(0, character=11000725)
    RunCommonEvent(0, 90005704, args=(11000725, 4201, 4200, 11009451, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(11000725, 4201, 4202, 11009451, 4201, 4200, 4204, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(11000725, 4203, 4200, 4204), arg_types="IIII")
    Event_11003721(0, character=11000715)
    Event_11003722(0, character=11000715)
    Event_11003723(0, other_entity=11000716)
    Event_11003724()
    Event_11003725(0, character=11000705)
    RunCommonEvent(0, 90005701, args=(11000705, 4701, 4702, 11009301, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005700,
        args=(11000705, 4701, 4702, 11009301, 0.6499999761581421, 4700, 4704, -1),
        arg_types="IIIIfIIi",
    )
    RunCommonEvent(0, 90005702, args=(11000705, 4703, 4700, 4704), arg_types="IIII")
    Event_11003730()
    RunCommonEvent(0, 90005774, args=(7605, 11001985, 11001985), arg_types="IiI")
    Event_11003740()
    Event_11003741()
    RunCommonEvent(0, 90005771, args=(11000957, 11002740), arg_types="II")
    RunCommonEvent(0, 90005771, args=(11000952, 11002741), arg_types="II")
    RunCommonEvent(0, 90005771, args=(11000953, 11002742), arg_types="II")
    RunCommonEvent(0, 90005771, args=(11000954, 11002743), arg_types="II")
    RunCommonEvent(0, 90005771, args=(11000955, 11002744), arg_types="II")
    RunCommonEvent(0, 90005775, args=(85495300, 11109687, -1.0), arg_types="iIf")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(11000705)
    DisableBackread(11000710)
    DisableBackread(11000715)
    DisableBackread(11000720)
    DisableBackread(11000725)
    DisableBackread(11000735)
    DisableBackread(11000740)
    DisableBackread(11000745)
    DisableHealthBar(11000750)
    Event_11000519()
    RunCommonEvent(0, 90005201, args=(11000200, 30000, 20000, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(11000201, 30000, 20000, 11002202, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11000202, 30000, 20000, 11002202, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005221, args=(11000204, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005250, args=(11000206, 11002208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000207, 11002208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(11000208, 30000, 20000, 11002208, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(11000220, 30010, 20010, 11002220, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000221, 30010, 20010, 11002220, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000222, 11002222, 0.0, 3004), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000223, 30010, 20010, 11002223, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000224, 30010, 20010, 11002224, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000225, 30010, 20010, 11002224, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000226, 30010, 20010, 11002226, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000227, 30002, 20002, 11002227, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000209, 30000, 20000, 11002393, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000210, 30000, 20000, 11002393, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000211, 30000, 20000, 11002393, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000212, 11002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000213, 11002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000214, 11002212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000240, 11002240, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000246, 11002246, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005210, args=(11000242, 30000, 20000, 11002242, 10.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(11000243, 11002243, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000244, 11002244, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000247, 11002247, 0.0, 3012), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000248, 11002248, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000250, 30000, 20000, 11002250, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000252, 11002243, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000253, 11002243, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000255, 11002255, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000256, 30002, 20002, 11002256, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000257, 30002, 20002, 11002625, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000258, 11002625, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000345, 30000, 20000, 11002345, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(11000346, 11002496, 9.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(11000341, 30000, 20000, 11002340, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000342, 30000, 20000, 11002340, 2.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000343, 30000, 20000, 11002340, 1.5, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000291, 11002330, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000292, 11002330, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000293, 11002330, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(11000375, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000376, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000377, 30001, 20001, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000378, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(11000390, 30000, 20000, 11002390, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(11000391, 11002206, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(11000392, 11002230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000393, 30000, 20000, 11002393, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000394, 11002394, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000300, 30010, 20010, 11002401, 1.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000301, 30010, 20010, 11002353, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000302, 11002353, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000303, 30010, 20010, 11002358, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000304, 30010, 20010, 11002358, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000311, 11002407, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000312, 11002407, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000313, 11002259, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000314, 30010, 20010, 11002259, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000320, 30010, 20010, 11002410, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000321, 11002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000322, 11002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000323, 11002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000324, 11002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000325, 11002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000326, 11002326, 0.0, 3026), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000327, 11002327, 0.0, 3012), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000350, 30002, 20002, 11002350, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000351, 11002350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000352, 30002, 20002, 11002259, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000353, 11002353, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000354, 11002354, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000355, 11002354, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(11000356, 30003, 20003, 0, 10.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11000357, 30004, 20004, 0, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(11000358, 11002358, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(11000359, 30004, 20004, 11002359, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(11000360, 11002360, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000361, 30003, 20003, 11002359, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000364, 11002405, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000365, 11002405, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000367, 11002407, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(11000400, 30000, 20000, 15.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(11000401, 11002401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000404, 11002404, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000416, 11002405, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000406, 11002406, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000407, 11002407, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000409, 11002405, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000410, 11002410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000411, 30000, 20000, 11002411, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000412, 11002412, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000413, 11002413, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000414, 11002414, 0.0, 3029), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000415, 11002415, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000405, 11002416, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000417, 11002416, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005210, args=(11000389, 30000, 20000, 11002389, 35.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(11000493, 11002493, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000494, 11002494, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000495, 11002495, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000496, 11002496, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000430, 11002430, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000431, 30000, 20000, 11002431, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000433, 30001, 20001, 11002433, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000434, 30002, 20002, 11002433, 6.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000436, 30002, 20002, 11002435, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(11000437, 30005, 20005, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(11000439, 30001, 20001, 11002435, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000440, 30005, 20005, 11002295, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(11000443, 30005, 20005, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005221, args=(11000444, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(11000295, 30017, 20017, 11002295, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000296, 30017, 20017, 11002295, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000297, 30018, 20018, 11002297, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000450, 11002455, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000451, 11002455, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000455, 11002471, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000459, 11002471, 0.0, 3009), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000469, 11002469, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(11000425, 30000, 20000, 11002425, 3.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(11000426, 30005, 20005, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(11000427, 30004, 20004, 11002425, 3.0, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11000428, 30006, 20006, 11002425, 3.0, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11000464, 30000, 20000, 11002464, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11000465, 30004, 20004, 11002464, 2.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(11000470, 30003, 20003, 11002470, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000471, 30002, 20002, 11002471, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000472, 30003, 20003, 11002466, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000473, 30003, 20003, 11002466, 2.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000475, 30005, 20005, 11002480, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000476, 30003, 20003, 11002476, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000477, 30005, 20005, 11002476, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000478, 30005, 20005, 11002480, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000480, 30003, 20003, 11002480, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000620, 30001, 20001, 11002620, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000621, 30001, 20001, 11002620, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000625, 30003, 20003, 11002625, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000626, 30002, 20002, 11002625, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000627, 11002625, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(11000630, 11002630, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(11000631, 30000, 20000, 11002631, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000632, 30000, 20000, 11002631, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005221, args=(11000636, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000637, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000638, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000639, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000640, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000641, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11000642, 30006, 20006, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(11000645, 30001, 20001, 11002645, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000395, 30000, 20000, 11002631, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005221, args=(11000396, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(11000398, 30000, 20000, 11002398, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000650, 30000, 20000, 11002650, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000651, 11002650, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000481, 30000, 20000, 11002650, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(11000653, 30000, 20000, 10.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(11000654, 30000, 20000, 10.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(11000656, 30000, 20000, 11002645, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(11000657, 11002645, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(11000658, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005200, args=(11000482, 30001, 20001, 11002398, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(11000663, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(11000482, 11002488, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(11000670, 30000, 20000, 1.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(11000671, 30000, 20000, 1.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(11000672, 30000, 20000, 11002672, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(11000675, 30000, 20000, 1.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(11000676, 30000, 20000, 1.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(11000681, 30001, 20001, 11002681, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(11000682, 30001, 20001, 11002682, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(11000683, 30001, 20001, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(11000685, 30000, 20000, 1.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(11000486, 11002486, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000488, 11002488, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000489, 11002499, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000498, 11002498, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(11000399, 30000, 20000, 11002256, 0.0, 0, 1, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(11000499, 11002499, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(11000484, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(11000665, 11002496, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(11000666, 11002425, 0.0, -1), arg_types="IIfi")
    EnableFlag(11008542)
    SkipLinesIfFlagEnabled(1, 11008544)
    EnableFlag(11008544)


@NeverRestart(11002500)
def Event_11002500():
    """Event 11002500"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9500, entity=11001500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=20000, anchor_entity=11001500, button_type=ButtonType.Yes_or_No)
    EnableFlag(11000500)
    Wait(3.0)
    Restart()


@NeverRestart(11002501)
def Event_11002501():
    """Event 11002501"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11000501)
    IfFlagEnabled(AND_1, 11000800)
    IfFlagDisabled(AND_1, 11000501)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    IfFlagEnabled(AND_2, 11000800)
    IfFlagEnabled(AND_2, 11000500)
    IfFlagEnabled(AND_2, 9000)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    EnableFlag(11000501)
    Restart()


@NeverRestart(11002502)
def Event_11002502():
    """Event 11002502"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11000500)
    IfFlagEnabled(AND_1, 11002802)
    IfFlagEnabled(AND_2, 11000800)
    IfInsideMap(AND_2, game_map=LEYNDELL_ROYAL_CAPITAL)
    IfConditionTrue(OR_9, input_condition=AND_1)
    IfConditionTrue(OR_9, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_9)
    Unknown_2003_68(unknown1=1, unknown2=-1.0, unknown3=0)
    Wait(3.0)
    IfFlagEnabled(AND_1, 11002802)
    IfFlagEnabled(AND_2, 11000800)
    IfInsideMap(AND_2, game_map=LEYNDELL_ROYAL_CAPITAL)
    IfConditionTrue(OR_9, input_condition=AND_1)
    IfConditionTrue(OR_9, input_condition=AND_2)
    IfConditionFalse(MAIN, input_condition=OR_9)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    Wait(3.0)
    Restart()


@NeverRestart(11002503)
def Event_11002503():
    """Event 11002503"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11000501)
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, 11000800)
    IfFlagDisabled(AND_10, 11000501)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=11001800)
    IfTryingToCreateSession(OR_10)
    IfTryingToJoinSession(OR_10)
    IfConditionFalse(AND_10, input_condition=OR_10)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, 11002800, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@NeverRestart(11000519)
def Event_11000519():
    """Event 11000519"""
    SkipLinesIfFlagDisabled(1, 300)
    EnableFlag(11000530)
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(11000510)
    EnableFlag(11000520)
    EnableFlag(11000525)


@NeverRestart(11000602)
def Event_11000602():
    """Event 11000602"""
    EndIfFlagDisabled(300)
    DisableObjectActivation(11001531, obj_act_id=-1)
    IfFlagEnabled(AND_1, 300)
    IfActionButtonParamActivated(AND_1, action_button_id=8320, entity=11001530)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=99995010, anchor_entity=11001530, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@RestartOnRest(11002145)
def Event_11002145():
    """Event 11002145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(11000740)
    EnableBackread(11000745)
    EnableBackread(11000735)
    SetTeamType(11000740, TeamType.Human)
    SetTeamType(11000745, TeamType.Human)
    SetTeamType(11000735, TeamType.Enemy)
    DeleteObjectVFX(11006700)
    CreateObjectVFX(11006700, vfx_id=200, model_point=806700)


@RestartOnRest(11002155)
def Event_11002155(_, flag: uint, character: uint, character_1: uint, banner_type: uchar, entity_id: uint):
    """Event 11002155"""
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    EndIfFlagEnabled(flag)
    IfCharacterDead(AND_1, character)
    IfCharacterDead(AND_1, character_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayBanner(banner_type)
    SkipLinesIfUnsignedEqual(1, left=entity_id, right=0)
    Unknown_2003_77(entity_id=entity_id)
    AddSpecialEffect(20000, 4821)
    Unknown_2003_74(unk_0_4=1)


@RestartOnRest(11002203)
def Event_11002203(_, character: uint, region: uint):
    """Event 11002203"""
    EndIfPlayerNotInOwnWorld()
    IfHealthValueLessThanOrEqual(AND_15, character, value=0)
    EndIfConditionTrue(input_condition=AND_15)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=character, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(region)
    Wait(8.0)
    DisableNetworkFlag(region)
    Restart()


@RestartOnRest(11002205)
def Event_11002205(_, character: uint, region: uint):
    """Event 11002205"""
    EndIfPlayerNotInOwnWorld()
    IfHealthValueLessThanOrEqual(AND_15, character, value=0)
    EndIfConditionTrue(input_condition=AND_15)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=character, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(region)
    Wait(8.0)
    DisableNetworkFlag(region)
    Restart()


@RestartOnRest(11002207)
def Event_11002207(_, character: uint, flag: uint):
    """Event 11002207"""
    EndIfPlayerNotInOwnWorld()
    IfHealthValueLessThanOrEqual(AND_15, character, value=0)
    EndIfConditionTrue(input_condition=AND_15)
    IfFlagEnabled(MAIN, flag)
    Wait(0.8999999761581421)
    ForceAnimation(character, 30002, loop=True, unknown2=1.0)
    Wait(8.0)
    Restart()


@RestartOnRest(11002209)
def Event_11002209(_, character: uint, flag: uint):
    """Event 11002209"""
    EndIfPlayerNotInOwnWorld()
    IfHealthValueLessThanOrEqual(AND_15, character, value=0)
    EndIfConditionTrue(input_condition=AND_15)
    IfFlagEnabled(MAIN, flag)
    Wait(0.8999999761581421)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    Wait(8.0)
    Restart()


@RestartOnRest(11002260)
def Event_11002260(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    left_4: uint,
):
    """Event 11002260"""
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
    IfCharacterHasSpecialEffect(OR_3, character, 14405)
    IfCharacterHasSpecialEffect(OR_3, character, 14406)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
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


@RestartOnRest(11002317)
def Event_11002317(_, character: uint, region: uint, seconds: float, radius: float):
    """Event 11002317"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterHasSpecialEffect(OR_3, PLAYER, 10004)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=AND_3)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(11002360)
def Event_11002360(
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
    """Event 11002360"""
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


@RestartOnRest(11002370)
def Event_11002370(_, character: uint):
    """Event 11002370"""
    Kill(character)


@RestartOnRest(11002397)
def Event_11002397(_, character: uint, region: uint, seconds: float):
    """Event 11002397"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfHasAIStatus(OR_3, 11000257, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 11000258, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 11000625, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 11000626, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 11000627, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_2, input_condition=OR_3)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=AND_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Search)
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
    EnableAI(character)
    ForceAnimation(character, 20001, unknown2=1.0)
    ChangePatrolBehavior(character, patrol_information_id=11003397)
    AddSpecialEffect(character, 5000)


@RestartOnRest(11002402)
def Event_11002402(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    left_4: uint,
):
    """Event 11002402"""
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
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
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


@RestartOnRest(11002497)
def Event_11002497(_, character: uint, region: uint, seconds: float):
    """Event 11002497"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 30002, unknown2=1.0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_3, entity=character, other_entity=PLAYER, radius=20.0)
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


@NeverRestart(11002510)
def Event_11002510():
    """Event 11002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            11000510,
            11000511,
            0,
            11001510,
            11001511,
            11003511,
            11001512,
            11003512,
            11002511,
            11002512,
            11000512,
            11000513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            11000515,
            11000516,
            0,
            11001515,
            11001516,
            11003516,
            11001517,
            11003517,
            11002516,
            11002517,
            11000517,
            11000518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            11000520,
            11000521,
            0,
            11001520,
            11001521,
            11003521,
            11001522,
            11003522,
            11002521,
            11002522,
            11000522,
            11000523,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            11000525,
            11000526,
            0,
            11001525,
            11001526,
            11003526,
            11001527,
            11003527,
            11002526,
            11002527,
            11000527,
            11000528,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    SkipLinesIfFlagEnabled(1, 300)
    RunCommonEvent(
        0,
        90005505,
        args=(11000530, 11000531, 0, 11001530, 11001531, 11003531, 11001532, 11003532, 11000532, 11000533, 0),
        arg_types="IIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005505,
        args=(11000535, 11000536, 1, 11001535, 11001536, 11003536, 11001537, 11003537, 11000537, 11000538, 0),
        arg_types="IIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            11000610,
            11000611,
            2,
            11001610,
            11001611,
            11003611,
            11001612,
            11003612,
            11002611,
            11002612,
            11000612,
            11000613,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(11002540)
def Event_11002540():
    """Event 11002540"""
    EndOfAnimation(obj=11001542, animation_id=2)
    EndOfAnimation(obj=11001571, animation_id=2)
    EndOfAnimation(obj=11001572, animation_id=2)
    EndOfAnimation(obj=11001570, animation_id=2)


@RestartOnRest(11002546)
def Event_11002546(
    _,
    flag: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 11002546"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(obj=obj, animation_id=animation_id_1)
    DisableObjectActivation(obj, obj_act_id=227012)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(AND_1, flag)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    ForceAnimation(obj, animation_id, unknown2=1.0)
    DisableObjectActivation(obj, obj_act_id=227012)


@RestartOnRest(11002547)
def Event_11002547():
    """Event 11002547"""
    EndIfFlagEnabled(11000546)
    IfFlagEnabled(MAIN, 11008546)
    EnableNetworkFlag(11000546)
    DisableObjectActivation(11001547, obj_act_id=1227050)


@RestartOnRest(11002580)
def Event_11002580():
    """Event 11002580"""
    RegisterLadder(start_climbing_flag=11000580, stop_climbing_flag=11000581, obj=11001580)
    RegisterLadder(start_climbing_flag=11000582, stop_climbing_flag=11000583, obj=11001582)
    RegisterLadder(start_climbing_flag=11000584, stop_climbing_flag=11000585, obj=11001584)
    RegisterLadder(start_climbing_flag=11000586, stop_climbing_flag=11000587, obj=11001586)
    RegisterLadder(start_climbing_flag=11000588, stop_climbing_flag=11000589, obj=11001588)
    RegisterLadder(start_climbing_flag=11000590, stop_climbing_flag=11000591, obj=11001590)
    RegisterLadder(start_climbing_flag=11000592, stop_climbing_flag=11000593, obj=11001592)
    RegisterLadder(start_climbing_flag=11000594, stop_climbing_flag=11000595, obj=11001594)
    RegisterLadder(start_climbing_flag=11000596, stop_climbing_flag=11000597, obj=11001596)


@RestartOnRest(11000600)
def Event_11000600():
    """Event 11000600"""
    DisableNetworkSync()
    EndIfThisEventSlotFlagEnabled()
    WaitFrames(frames=2)
    DisableObjectActivation(11001536, obj_act_id=-1)
    IfFlagEnabled(AND_1, 11000535)
    IfFlagDisabled(AND_1, 11000537)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfThisEventSlotFlagEnabled()
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(11002601)
def Event_11002601():
    """Event 11002601"""
    IfFlagEnabled(MAIN, 11000601)
    ForceAnimation(PLAYER, 60131, unknown2=1.0)
    EnableFlag(9080)
    DisableFlag(11000601)


@NeverRestart(11002603)
def Event_11002603():
    """Event 11002603"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(11000603)
    IfFlagEnabled(AND_1, 11000603)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=11002500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownCamera_4(unknown1=11.899999618530273, unknown2=1.1100000143051147)
    DisableFlag(11000603)


@RestartOnRest(11002690)
def Event_11002690():
    """Event 11002690"""
    DisableNetworkSync()
    SkipLinesIfThisEventSlotFlagEnabled(1)
    DeleteVFX(11003690, erase_root_only=False)
    IfInsideMap(AND_1, game_map=LEYNDELL_ROYAL_CAPITAL)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=11002690)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateVFX(11003690)
    Wait(1.0)
    IfOutsideMap(OR_1, game_map=LEYNDELL_ROYAL_CAPITAL)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=11002690)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DeleteVFX(11003690)
    Wait(1.0)
    Restart()


@RestartOnRest(11002691)
def Event_11002691(_, obj: uint):
    """Event 11002691"""
    EnableObjectInvulnerability(obj)


@RestartOnRest(11002696)
def Event_11002696():
    """Event 11002696"""
    EndIfFlagEnabled(11007992)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9531, entity=11001696)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AwardItemLot(11001010, host_only=False)
    End()


@RestartOnRest(11002800)
def Event_11002800():
    """Event 11002800"""
    EndIfFlagEnabled(11000800)
    IfHealthValueLessThanOrEqual(MAIN, 11000800, value=0)
    Wait(4.0)
    PlaySoundEffect(11008000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 11000800)
    KillBossAndDisplayBanner(character=11000800, banner_type=BannerType.HollowArenaLoss)
    SkipLinesIfPlayerNotInOwnWorld(1)
    TriggerMultiplayerEvent(event_id=0)
    DisableObject(11001820)
    EnableMapCollision(collision=11004821)
    WaitFrames(frames=1)
    DisableMapCollision(collision=11004820)
    EnableFlag(11000800)
    EnableFlag(9104)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61104)
    SkipLinesIfFlagEnabled(1, 10000850)
    EnableFlag(10000850)
    SkipLinesIfFlagEnabled(1, 9100)
    EnableFlag(9100)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SkipLinesIfFlagEnabled(1, 61100)
    EnableFlag(61100)
    SkipLinesIfFlagEnabled(3, 10000850)
    DisableCharacter(10000850)
    DisableAnimations(10000850)
    Kill(10000850)
    EndIfPlayerNotInOwnWorld()
    SetRespawnPoint(respawn_point=11002020)
    SaveRequest()


@RestartOnRest(11002810)
def Event_11002810():
    """Event 11002810"""
    GotoIfFlagDisabled(Label.L0, flag=11000800)
    DisableCharacter(11005800)
    DisableAnimations(11005800)
    Kill(11005800)
    DisableObject(11001820)
    DisableMapCollision(collision=11004820)
    DisableObject(11006830)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(11005800)
    DisableObject(11001820)
    DisableMapCollision(collision=11004820)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown18)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown17)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfFlagEnabled(Label.L1, flag=11000801)
    Move(11000800, destination=11002810, destination_type=CoordEntityType.Region, copy_draw_parent=11000800)
    ForceAnimation(11000800, 30000, unknown2=1.0)
    IfFlagEnabled(AND_1, 11002805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=11002800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=11000040,
        cutscene_flags=0,
        move_to_region=11002812,
        map_base_id=11000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(11000040, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(11000801)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=14.420000076293945, unknown2=-37.689998626708984)
    DisableObject(11006830)
    Move(11000800, destination=11002811, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(11000800, 20000, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(11006830)
    IfFlagEnabled(AND_2, 11002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=11002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(11005800)
    SetNetworkUpdateRate(11005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(11000800, name=902130002)


@RestartOnRest(11002811)
def Event_11002811():
    """Event 11002811"""
    EndIfFlagEnabled(11000800)
    IfCharacterHasSpecialEffect(AND_1, 11000800, 16205)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(11002802)
    EnableObject(11001820)
    EnableMapCollision(collision=11004820)
    WaitFrames(frames=1)
    DisableMapCollision(collision=11004821)
    EnableBossHealthBar(11000800, name=902130003)


@RestartOnRest(11002829)
def Event_11002829():
    """Event 11002829"""
    RunCommonEvent(
        0,
        9005800,
        args=(11000800, 11001800, 11002800, 11002805, 11005800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(11000800, 11001800, 11002800, 11002805, 11002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(11000501, 11001800, 17, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000800, 11001801, 18, 11000801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(11000800, 213001, 11002805, 11002806, 0, 11002802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(11002850)
def Event_11002850():
    """Event 11002850"""
    EndIfFlagEnabled(11000850)
    IfHealthValueLessThanOrEqual(MAIN, 11000850, value=0)
    Wait(4.0)
    PlaySoundEffect(11008050, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 11000850)
    KillBossAndDisplayBanner(character=11000850, banner_type=BannerType.Unknown)
    EnableFlag(11000850)
    EnableFlag(9105)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61105)


@RestartOnRest(11002860)
def Event_11002860():
    """Event 11002860"""
    GotoIfFlagDisabled(Label.L0, flag=11000850)
    DisableCharacter(11005850)
    DisableAnimations(11005850)
    Kill(11005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(11005850)
    GotoIfFlagEnabled(Label.L1, flag=11000851)
    ForceAnimation(11000850, 30000, loop=True, unknown2=1.0)
    DisableCharacter(11000850)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=11000850, other_entity=PLAYER, radius=25.0)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=10000850, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(11000851)
    ForceAnimation(11000850, 20000, unknown2=1.0)
    EnableCharacter(11000850)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 11002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=11002850)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(11000850)
    SetNetworkUpdateRate(11005850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(11000850, name=904720002)


@RestartOnRest(11002861)
def Event_11002861():
    """Event 11002861"""
    EndIfFlagEnabled(11000850)
    IfHealthLessThanOrEqual(AND_1, 11000850, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(11002852)


@RestartOnRest(11002859)
def Event_11002859():
    """Event 11002859"""
    RunCommonEvent(
        0,
        9005800,
        args=(11000850, 11001850, 11002850, 11002855, 11005850, 10000, 11000851, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(11000850, 11001850, 11002850, 11002855, 11002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(11000850, 11001850, 4, 11000851), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001851, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001852, 4, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001853, 4, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001854, 19, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001857, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11000850, 11001858, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(11000850, 472001, 11002855, 11002856, 0, 11002852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(11002910)
def Event_11002910():
    """Event 11002910"""
    IfFlagEnabled(AND_1, 11000800)
    IfFlagEnabled(AND_1, 130)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(11001920)
    CreateObjectVFX(11001920, vfx_id=100, model_point=30)


@NeverRestart(11002920)
def Event_11002920(_, flag: uint, anchor_entity: uint):
    """Event 11002920"""
    DisableNetworkSync()
    IfActionButtonParamActivated(OR_1, action_button_id=7100, entity=anchor_entity)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(flag)
    DisplayDialog(text=10010170, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(11003710)
def Event_11003710(_, character: uint):
    """Event 11003710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SkipLinesIfFlagDisabled(1, 3940)
    DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3947)
    IfFlagEnabled(MAIN, 3947)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3957)
    SkipLinesIfFlagEnabled(3, 11109819)
    IfFlagEnabled(AND_6, 71102)
    IfFlagEnabled(AND_6, 9000)
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    EnableNetworkFlag(11109819)
    EnableNetworkFlag(3957)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
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
    IfFlagDisabled(MAIN, 3947)
    Restart()


@RestartOnRest(11003711)
def Event_11003711(_, entity: uint):
    """Event 11003711"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 3943)
    IfFlagDisabled(OR_1, 3947)
    IfFlagEnabled(OR_1, 1039409259)
    EndIfConditionTrue(input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=20000, radius=4.0)
    IfCharacterHasSpecialEffect(AND_1, 20000, 9690)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()


@RestartOnRest(11003715)
def Event_11003715(_, character: uint):
    """Event 11003715"""
    DisableCharacter(character)
    DisableBackread(character)
    SetCharacterTalkRange(character=character, distance=17.0)
    GotoIfFlagEnabled(Label.L0, flag=11000800)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=character, distance=120.0)
    EnableCharacter(character)
    EnableBackread(character)
    Move(character, destination=11002721, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 930000, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 11009405)
    ForceAnimation(character, 930002, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AwaitFlagEnabled(flag=11000800)
    SetCharacterTalkRange(character=character, distance=120.0)
    EnableCharacter(character)
    EnableBackread(character)
    Move(character, destination=11000800, destination_type=CoordEntityType.Character, model_point=900, short_move=True)
    ForceAnimation(character, 930000, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 11009405)
    ForceAnimation(character, 930002, unknown2=1.0)
    End()


@RestartOnRest(11003720)
def Event_11003720(_, character: uint):
    """Event 11003720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4200)
    DisableFlag(1040529253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4208)
    IfFlagEnabled(AND_1, 4209)
    IfFlagEnabled(AND_1, 11009554)
    IfConditionTrue(OR_1, input_condition=AND_1)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 4208)
    IfFlagEnabled(AND_2, 4209)
    IfFlagEnabled(AND_2, 11009554)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

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
    IfFlagEnabled(OR_3, 4208)
    IfFlagEnabled(AND_3, 4209)
    IfFlagEnabled(AND_3, 11009554)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionFalse(MAIN, input_condition=OR_3)
    Restart()


@RestartOnRest(11003721)
def Event_11003721(_, character: uint):
    """Event 11003721"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagDisabled(AND_1, 4203)
    IfFlagEnabled(AND_1, 4208)
    IfFlagEnabled(AND_2, 4203)
    IfFlagDisabled(AND_2, 4217)
    IfFlagDisabled(AND_2, 1051569454)
    IfFlagDisabled(AND_2, 11059304)
    IfFlagDisabled(AND_3, 4217)
    IfFlagEnabled(AND_3, 11009554)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930007, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 11009555)
    ForceAnimation(character, 930009, unknown2=1.0)
    DisableNetworkFlag(1040549254)
    EnableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    IfFlagDisabled(AND_5, 4203)
    IfFlagEnabled(AND_5, 4208)
    IfFlagEnabled(AND_6, 4203)
    IfFlagDisabled(AND_6, 4217)
    IfFlagDisabled(AND_6, 1051569454)
    IfFlagDisabled(AND_6, 11059304)
    IfFlagDisabled(AND_7, 4217)
    IfFlagEnabled(AND_7, 11009554)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfConditionTrue(OR_5, input_condition=AND_6)
    IfConditionTrue(OR_5, input_condition=AND_7)
    IfConditionFalse(MAIN, input_condition=OR_5)
    Restart()


@RestartOnRest(11003722)
def Event_11003722(_, character: uint):
    """Event 11003722"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EnableImmortality(character)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    EnableNetworkFlag(1040542710)
    SkipLinesIfFlagDisabled(1, 11009555)
    ForceAnimation(character, 20014, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SkipLinesIfFlagEnabled(1, 11009555)
    ForceAnimation(character, 20013, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(11003723)
def Event_11003723(_, other_entity: uint):
    """Event 11003723"""
    SkipLinesIfFlagDisabled(2, 11009556)
    DisableObject(11001715)
    End()
    DisableObject(11001705)
    EnableNetworkFlag(11009468)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=4.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, 20000, 1673014)
    AwaitConditionTrue(AND_1)
    CreateTemporaryVFX(vfx_id=811630, anchor_entity=11001706, anchor_type=CoordEntityType.Object)
    ForceAnimation(11001715, 1, unknown2=1.0)
    EnableObject(11001705)
    ForceAnimation(11001705, 1, unknown2=1.0)
    EnableNetworkFlag(11009556)
    EnableNetworkFlag(11009469)
    DisableNetworkFlag(11009468)
    End()


@RestartOnRest(11003724)
def Event_11003724():
    """Event 11003724"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=11000725, distance=17.0)
    EndIfFlagEnabled(11009460)
    SetCharacterTalkRange(character=11000725, distance=160.0)
    IfFlagEnabled(AND_1, 4208)
    IfFlagDisabled(AND_1, 11009460)
    IfFlagDisabled(AND_1, 11002734)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=11002740)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11002733)
    End()


@RestartOnRest(11003725)
def Event_11003725(_, character: uint):
    """Event 11003725"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4700)
    DisableFlag(1042369283)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4707)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 4707)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4700)
    GotoIfFlagEnabled(Label.L2, flag=4701)
    GotoIfFlagEnabled(Label.L3, flag=4702)
    GotoIfFlagEnabled(Label.L4, flag=4703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 30003, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
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
    IfFlagEnabled(OR_4, 4707)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(11003730)
def Event_11003730():
    """Event 11003730"""
    WaitFrames(frames=1)
    DisableFlag(11009500)
    EndIfFlagDisabled(16009458)
    EndIfFlagDisabled(3886)
    EnableFlag(11009500)
    End()


@RestartOnRest(11003740)
def Event_11003740():
    """Event 11003740"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4247)
    AwaitFlagEnabled(flag=1045520180)
    DisableNetworkFlag(35009317)
    DisableNetworkFlag(35009318)
    End()


@RestartOnRest(11003741)
def Event_11003741():
    """Event 11003741"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4246)
    IfFlagEnabled(AND_1, 4240)
    IfFlagEnabled(AND_1, 35009306)
    IfEntityWithinDistance(AND_1, entity=11001957, other_entity=20000, radius=13.0)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(4258)
    End()
