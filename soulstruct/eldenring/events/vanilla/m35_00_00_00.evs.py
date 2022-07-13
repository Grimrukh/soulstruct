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
    RegisterGrace(grace_flag=35000001, obj=35001951, unknown=5.0)
    RegisterGrace(grace_flag=35000002, obj=35001952, unknown=5.0)
    RegisterGrace(grace_flag=35000003, obj=35001953, unknown=5.0)
    RegisterGrace(grace_flag=35000004, obj=35001954, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(35001150, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 9005810, args=(35000800, 35000000, 35000950, 35001950, 5.0), arg_types="IIIIf")
    Event_35002500()
    Event_35002504()
    Event_35002506()
    Event_35002508()
    RunCommonEvent(0, 90005300, args=(35000800, 35000800, 0, 0.0, 0), arg_types="IIifi")
    Event_35002800()
    Event_35002810()
    Event_35002849()
    Event_35002850()
    Event_35002860()
    Event_35002899()
    Event_35002490(0, flag=35008203, obj=35001490, flag_1=35000800)
    RunCommonEvent(
        0,
        90005501,
        args=(35000510, 35000511, 0, 35001510, 35001511, 35001512, 35000512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(35000515, 35000516, 0, 35001515, 35001516, 35001517, 35000517),
        arg_types="IIIIIII",
    )
    Event_35002510()
    RunCommonEvent(0, 90005525, args=(35000570, 35001570), arg_types="II")
    RunCommonEvent(1, 90005525, args=(35000571, 35001571), arg_types="II")
    RunCommonEvent(2, 90005525, args=(35000572, 35001572), arg_types="II")
    RunCommonEvent(3, 90005525, args=(35000573, 35001573), arg_types="II")
    RunCommonEvent(4, 90005525, args=(35000574, 35001574), arg_types="II")
    RunCommonEvent(0, 90005540, args=(35000530, 35001530, 35001531, 35003531, -1, 1, 2), arg_types="IIIIiii")
    RunCommonEvent(0, 90005540, args=(35000565, 35001532, 35001533, 35003533, -1, 1, 2), arg_types="IIIIiii")
    RunCommonEvent(0, 90005540, args=(35000566, 35001534, 35001535, 35003535, -1, 1, 2), arg_types="IIIIiii")
    RunCommonEvent(0, 90005511, args=(35000560, 35001560, 35003560, 27019, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(35000560, 35002560, 35002561), arg_types="III")
    RunCommonEvent(0, 90005511, args=(35000562, 35001562, 35003562, 27019, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(35000562, 35002562, 35002563), arg_types="III")
    RunCommonEvent(0, 90005510, args=(35000564, 35001564, 35003564, 1027019, 208197, 0), arg_types="IIIiiI")
    RunCommonEvent(0, 90005515, args=(35008542, 35001542), arg_types="II")
    Event_35002580()
    RunCommonEvent(0, 90005520, args=(35000598, 35001598, 35002598, 35002599), arg_types="IIII")
    Event_35002498()
    RunCommonEvent(0, 90005690, args=(35002507,))
    RunCommonEvent(0, 90005691, args=(35002507,))
    Event_35002820()
    RunCommonEvent(0, 90005650, args=(35000640, 35001640, 35001641, 35003641, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(35000640, 35001640), arg_types="II")
    RunCommonEvent(0, 90005680, args=(35000670, 35000671, 35000672, 35000673, 35001670), arg_types="IIIII")
    RunCommonEvent(0, 90005680, args=(35000675, 35000676, 35000677, 35000678, 35001675), arg_types="IIIII")
    Event_35002642()
    Event_35002680()
    RunCommonEvent(
        0,
        90005646,
        args=(35000850, 35002840, 35002841, 35001840, 35002840, 35, 0, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(35002800, 35001695, 5), arg_types="IIi")
    RunCommonEvent(
        0,
        90005780,
        args=(35000800, 35002160, 35002161, 35000720, 20, 35002721, 35009318, 0, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(35000800, 35002160, 35002161, 35000720), arg_types="IIII")
    RunCommonEvent(0, 90005784, args=(35002160, 35002805, 35000720, 35002800, 35002808, 0), arg_types="IIIIIi")
    Event_35000700(0, character=35000700, obj=35001701)
    RunCommonEvent(
        0,
        90005740,
        args=(
            35002705,
            35002706,
            35002707,
            35000700,
            701,
            35001700,
            701,
            0.4000000059604645,
            90202,
            -1,
            -1,
            1.100000023841858,
        ),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(
        0,
        90005741,
        args=(35002708, 35002709, 35002707, 35000700, 90202, 1, -1, 0, 0.0),
        arg_types="IIIIiIiif",
    )
    RunCommonEvent(0, 90005750, args=(35001702, 4110, 100890, 400089, 400089, 35009211, 0), arg_types="IiiIIIi")
    Event_35000703(0, 7.5)
    Event_35003720(0, character=35000715)
    RunCommonEvent(0, 90005704, args=(35000715, 4241, 4240, 35009251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(35000715, 4241, 4242, 35009251, 4241, 4240, 4244, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(35000715, 4243, 4240, 4244), arg_types="IIII")
    Event_35003721(0, character=35000716)
    Event_35003722(0, entity=35000716)
    RunCommonEvent(0, 90005702, args=(35000716, 4243, 4240, 4244), arg_types="IIII")
    Event_35003724(
        0,
        obj=35001705,
        action_button_id=6440,
        item_lot_param_id=4920,
        first_flag=9504,
        last_flag=9504,
        flag=35009333,
        model_point=806782
    )
    Event_35003723()
    RunCommonEvent(0, 90005750, args=(35001706, 4110, 103820, 400381, 400382, 35009336, 0), arg_types="IiiIIIi")
    Event_35003725()
    Event_35003726()
    Event_35003727()
    RunCommonEvent(0, 90005750, args=(35001706, 4110, 113820, 400382, 400382, 35009337, 0), arg_types="IiiIIIi")
    Event_35003730()
    RunCommonEvent(0, 90005771, args=(35000950, 35002730), arg_types="II")
    RunCommonEvent(0, 90005771, args=(35000954, 35002731), arg_types="II")
    Event_35003790()
    Event_35003500(0, region=35002700)
    Event_35002361()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(35000700)
    DisableBackread(35000710)
    DisableBackread(35000711)
    DisableBackread(35000712)
    DisableBackread(35000715)
    DisableBackread(35000716)
    Event_35000050()
    Event_35000519()
    Event_35002600()
    RunCommonEvent(0, 90005261, args=(35000200, 35002200, 2.0, 0.0, -1), arg_types="IIffi")
    Event_35002200()
    RunCommonEvent(0, 90005211, args=(35000201, 30009, 20009, 35002201, 2.5, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000202, 30002, 20002, 35002202, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002203()
    RunCommonEvent(0, 90005211, args=(35000204, 30000, 20000, 35002204, 0.0, 11.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000205, 30004, 20004, 35002205, 2.0, 8.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(35000206, 35002226, 2.0, 0.0, 3006), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000207, 30004, 20004, 35002205, 2.0, 3.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000208, 30002, 20002, 35002208, 1.0, 4.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002208()
    RunCommonEvent(0, 90005211, args=(35000209, 30010, 20010, 35002209, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000210, 30004, 20004, 35002210, 2.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(35000211, 35002211, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000212, 30010, 20010, 35002212, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000213, 30000, 20000, 35002213, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000214, 30010, 20010, 35002214, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000215, 30010, 20010, 35002215, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002215()
    RunCommonEvent(0, 90005211, args=(35000216, 30004, 20004, 35002217, 2.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(35000217, 30004, 20004, 35002217, 2.0, 0.30000001192092896, 1, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(35000218, 30002, 20002, 35002218, 0.5, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000219, 30000, 20000, 35002219, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002220(0, 35000420, 30001, 20001, 2.0, 0.5, 0, 0, 0, 0)
    Event_35002220(1, 35000421, 30000, 20000, 2.0, 0.30000001192092896, 0, 0, 0, 0)
    Event_35002220(2, 35000422, 30000, 20000, 2.0, 0.699999988079071, 0, 0, 0, 0)
    Event_35002220(3, 35000423, 30000, 20000, 2.0, 0.6000000238418579, 0, 0, 0, 0)
    Event_35002220(4, 35000418, 30000, 20000, 3.0, 0.30000001192092896, 0, 0, 0, 0)
    Event_35002226(0, 35000426, 30000, 20000, 1.5, 0.5, 0, 0, 0, 0)
    Event_35002226(1, 35000427, 30000, 20000, 1.5, 1.0, 0, 0, 0, 0)
    Event_35002226(2, 35000428, 30001, 20001, 1.5, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005261, args=(35000385, 35002385, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000386, 30003, 20003, 35002386, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000387, 30004, 20004, 35002387, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(35000230, 35002230, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000231, 35002230, 0.5, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000232, 35002230, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000233, 35002230, 0.5, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000234, 35002230, 0.5, 0.0, 0), arg_types="IIffi")
    Event_35002230(0, 35000230, 10.0)
    Event_35002230(1, 35000231, 15.0)
    Event_35002230(2, 35000232, 12.0)
    Event_35002230(3, 35000233, 16.0)
    Event_35002230(4, 35000234, 17.0)
    RunCommonEvent(0, 90005261, args=(35000235, 35002235, 2.0, 0.0, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000236, 35002236, 2.0, 0.0, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000237, 35002237, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000238, 35002237, 2.0, 0.0, 0), arg_types="IIffi")
    Event_35002239(0, 35000239, 35002239, 0.0, 0.0, 3002)
    RunCommonEvent(0, 90005261, args=(35000240, 35002240, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000243, 35002243, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000248, 35002248, 2.0, 0.0, 0), arg_types="IIffi")
    Event_35002240(0, character=35000243)
    Event_35002240(1, character=35000248)
    RunCommonEvent(0, 90005261, args=(35000285, 0, 1.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000286, 35002286, 0.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000288, 35002288, 0.5, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000260, 35002260, 2.0, 3.0, 3037), arg_types="IIffi")
    Event_35002261(0, 35000261, 35002261, 3.0, 0.0, 3037)
    RunCommonEvent(0, 90005251, args=(35000262, 1.0, 0.0, 0), arg_types="Iffi")
    Event_35002261(1, 35000263, 35002263, 3.0, 0.0, 3022)
    RunCommonEvent(0, 90005261, args=(35000266, 35002380, 4.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000267, 35002267, 4.0, 0.0, 3022), arg_types="IIffi")
    Event_35002261(2, 35000268, 35002268, 3.0, 0.0, 3037)
    RunCommonEvent(0, 90005261, args=(35000269, 35002269, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000271, 35002271, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000272, 35002272, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000275, 35002275, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000276, 35002276, 2.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000277, 35002276, 2.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000278, 30000, 20000, 35002278, 3.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(35000279, 30000, 20000, 35002278, 3.0, 0.800000011920929, 1, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(35000390, 35002390, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000391, 35002390, 2.0, 0.0, 0), arg_types="IIffi")
    Event_35002390(0, character=35000390)
    Event_35002390(1, character=35000391)
    Event_35002392(0, character=35000392, animation_id=30013)
    Event_35002392(1, character=35000393, animation_id=30013)
    Event_35002392(2, character=35000394, animation_id=30013)
    Event_35002392(3, character=35000395, animation_id=30013)
    Event_35002392(4, character=35000396, animation_id=30013)
    Event_35002392(5, character=35000397, animation_id=30013)
    Event_35002392(6, character=35000398, animation_id=30012)
    Event_35002392(7, character=35000399, animation_id=30013)
    RunCommonEvent(0, 90005271, args=(35000399, 0.0, 0), arg_types="Ifi")
    RunCommonEvent(0, 90005261, args=(35000290, 35002290, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000291, 35002290, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000292, 35002290, 3.0, 0.800000011920929, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000293, 35002293, 3.0, 0.0, 3001), arg_types="IIffi")
    Event_35002290(0, character=35000290)
    Event_35002290(1, character=35000291)
    Event_35002290(2, character=35000292)
    RunCommonEvent(0, 90005261, args=(35000296, 35002296, 3.0, 0.0, 0), arg_types="IIffi")
    Event_35002296(0, character=35000296)
    Event_35002297(0, 35000297, 35002297, 4.0, 0.0, 3000)
    RunCommonEvent(0, 90005261, args=(35000298, 35002298, 3.0, 1.5, 0), arg_types="IIffi")
    Event_35002298()
    RunCommonEvent(0, 90005261, args=(35000380, 35002380, 2.0, 0.0, 1800), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000381, 35002380, 2.0, 0.0, 1800), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000382, 35002380, 2.0, 0.0, 1800), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000383, 35002384, 1.0, 0.0, 1800), arg_types="IIffi")
    Event_35002258(0, character=35000382)
    Event_35002258(1, character=35000307)
    RunCommonEvent(0, 90005261, args=(35000370, 35002370, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000371, 0, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000372, 35002372, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005221, args=(35000373, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005261, args=(35000376, 35002275, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005221, args=(35000377, 30005, 20005, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005261, args=(35000378, 0, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000301, 35002301, 2.0, 0.0, 3003), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000307, 35002307, 0.0, 1.5, 3003), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000314, 30000, 20000, 35002314, 2.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(35000327, 35002327, 2.0, 0.0, 3003), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000328, 35002327, 2.0, 0.4000000059604645, 3003), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000329, 35002327, 2.0, 0.6000000238418579, 3003), arg_types="IIffi")
    Event_35002320(0, character=35000300, animation_id=30001)
    Event_35002320(1, character=35000302, animation_id=30001)
    Event_35002320(2, character=35000303, animation_id=30001)
    Event_35002320(3, character=35000304, animation_id=30000)
    Event_35002320(4, character=35000305, animation_id=30001)
    Event_35002320(5, character=35000306, animation_id=30000)
    Event_35002320(6, character=35000308, animation_id=30000)
    Event_35002320(7, character=35000309, animation_id=30000)
    Event_35002320(8, character=35000310, animation_id=30000)
    Event_35002320(9, character=35000311, animation_id=30000)
    Event_35002320(10, character=35000312, animation_id=30001)
    Event_35002320(11, character=35000313, animation_id=30000)
    Event_35002320(12, character=35000315, animation_id=30000)
    Event_35002320(13, character=35000316, animation_id=30000)
    Event_35002320(14, character=35000317, animation_id=30001)
    Event_35002320(15, character=35000318, animation_id=30001)
    Event_35002320(16, character=35000319, animation_id=30000)
    Event_35002320(17, character=35000320, animation_id=30000)
    Event_35002320(18, character=35000321, animation_id=30000)
    Event_35002320(19, character=35000322, animation_id=30001)
    Event_35002320(20, character=35000323, animation_id=30001)
    Event_35002320(21, character=35000324, animation_id=30000)
    Event_35002320(22, character=35000325, animation_id=30000)
    Event_35002320(23, character=35000326, animation_id=30000)
    RunCommonEvent(0, 90005271, args=(35000351, 0.0, 0), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000352, 0.0, 0), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000353, 0.0, 0), arg_types="Ifi")
    RunCommonEvent(0, 90005211, args=(35000250, 30002, 20002, 35002250, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002250()
    Event_35002251()
    Event_35002253()
    RunCommonEvent(0, 90005261, args=(35000495, 35002495, 0.5, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000496, 35002496, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000497, 30003, 20003, 35002497, 1.0, 6.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(35000490, 35002490, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000491, 35002491, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000492, 35002492, 0.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000493, 30003, 20003, 35002493, 1.5, 2.5, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(35000494, 30003, 20003, 35002494, 0.5, 1.5, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005300, args=(35000495, 35000495, 35000970, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000496, 35000496, 35000980, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000497, 35000497, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000490, 35000490, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000491, 35000491, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000492, 35000492, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000493, 35000493, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(35000494, 35000494, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005211, args=(35000360, 30000, 20000, 35002360, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(35000361, 30000, 20000, 35002361, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(35000361, 35002361, 0.20000000298023224, 3005), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(35000362, 35002362, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000363, 35002363, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000366, 35002366, 3.0, 0.0, 3024), arg_types="IIffi")
    Event_35002365(0, 35000364, 35002364, 2.0, 0.5, 1700, 35000367)
    Event_35002365(1, 35000367, 35002364, 2.0, 0.5, 1700, 35000364)
    RunCommonEvent(0, 90005211, args=(35000369, 30000, 20000, 35002369, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(35000280, 35002280, 3.0, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000281, 35002281, 3.0, 1.5, 3001), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000282, 35002282, 3.0, 0.0, 3003), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000284, 35002284, 3.0, 3.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(35000258, 30000, 20000, 35002258, 2.0, 7.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002400()
    RunCommonEvent(0, 90005211, args=(35000401, 30000, 20000, 35002401, 3.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_35002401()
    RunCommonEvent(
        0,
        90005211,
        args=(35000416, 30000, 20000, 35002416, 1.0, 0.699999988079071, 1, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    Event_35002410(0, 35000410, 30005, 20005, 35002410, 5.0, 4.0, 1, 0, 0, 0)
    Event_35002410(1, 35000411, 30005, 20005, 35002410, 5.0, 4.300000190734863, 1, 0, 0, 0)
    Event_35002410(2, 35000412, 30005, 20005, 35002410, 5.0, 5.5, 1, 0, 0, 0)
    Event_35002411()
    Event_35002430(0, 35000432, 0, 3016, 35002431, 3.0, 0.0, 0, 0, 0, 0)
    Event_35002430(1, 35000431, 0, 3016, 35002431, 3.5, 0.0, 0, 0, 0, 0)
    Event_35002430(3, 35000436, 0, 3016, 35002431, 3.0, 0.0, 0, 0, 0, 0)
    Event_35002430(4, 35000435, 0, 3016, 35002431, 3.0, 0.0, 0, 0, 0, 0)
    Event_35002430(5, 35000434, 0, 3016, 35002431, 3.0, 0.0, 0, 0, 0, 0)
    Event_35002430(7, 35000433, 0, 3016, 35002431, 3.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005200, args=(35000476, 30000, 20000, 35002430, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000430, 30000, 20000, 35002430, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_35002440(0, character=35005431)
    Event_35002440(3, character=35000439)
    Event_35002440(4, character=35000440)
    Event_35002430(8, 35000448, 0, 3016, 35002448, 10.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005261, args=(35000454, 35002454, 1.0, 0.0, 3030), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(35000455, 35002454, 1.0, 0.5, 3031), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(35000443, 30001, 20001, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(35000446, 30002, 20002, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(35000445, 30002, 20002, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(35000444, 30001, 20001, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(35005435, 35002614, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005271, args=(35000449, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000439, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000440, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000441, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000442, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000447, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000458, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(35000451, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005200, args=(35000437, 30000, 20000, 35002475, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000475, 30000, 20000, 35002475, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000438, 30000, 20000, 35002475, 2.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000450, 30006, 20006, 35002222, 2.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000452, 30006, 20006, 35002222, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(35000451, 35002222, 0.0, 3023), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(35000449, 35002449, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(35000456, 30001, 20001, 35002456, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000457, 30002, 20002, 35002456, 2.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000458, 30001, 20001, 35002456, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(35000481, 30000, 20000, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(35000484, 35002365, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(35000484, 30000, 20000, 35002365, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(35000366, 30000, 20000, 35002366, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(35000367, 35002366, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(35000483, 35002483, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(35000480, 35002483, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(35000485, 35002483, 0.0, -1), arg_types="IIfi")


@NeverRestart(35000050)
def Event_35000050():
    """Event 35000050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(35000670)
    DisableFlag(35000675)


@RestartOnRest(35002498)
def Event_35002498():
    """Event 35002498"""
    GotoIfFlagEnabled(Label.L0, flag=35000598)
    EnableNavmeshType(navmesh_id=35002498, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(MAIN, 35000598)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=35002498, navmesh_type=NavmeshType.Solid)
    End()


@NeverRestart(35002500)
def Event_35002500():
    """Event 35002500"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L1, flag=35000501)
    GotoIfFlagDisabled(Label.L0, flag=35000500)
    EndOfAnimation(obj=35001500, animation_id=1)
    EnableObject(35001502)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(35001502)
    IfPlayerInOwnWorld(AND_1)
    IfUnknownCondition_34(AND_1, unk_4_8=10000, unk_8_12=-1)
    IfUnknownCondition_34(AND_1, unk_4_8=10100, unk_8_12=-1)
    IfUnknownCondition_34(AND_1, unk_4_8=10200, unk_8_12=-1)
    IfUnknownCondition_34(AND_1, unk_4_8=10300, unk_8_12=-1)
    IfActionButtonParamActivated(AND_1, action_button_id=9640, entity=35001500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(35000500)
    EnableFlag(108)
    SkipLinesIfFlagDisabled(1, 110)
    EnableFlag(109)
    EnableFlag(7500)
    EnableFlag(35000501)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9021)
    UnknownCutscene_11(
        cutscene_id=35000000,
        cutscene_flags=0,
        move_to_region=35002500,
        map_base_id=35000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(35000501)
    EndOfAnimation(obj=35001500, animation_id=1)
    EnableObject(35001502)
    EnableFlag(9431)
    EnableFlag(9430)


@NeverRestart(35002504)
def Event_35002504():
    """Event 35002504"""
    GotoIfFlagDisabled(Label.L0, flag=35000504)
    DisableObject(35001504)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=35002504)
    DeleteObjectVFX(35001504)
    CreateObjectVFX(35001504, vfx_id=101, model_point=1540)
    EnableNetworkFlag(35002504)

    # --- Label 2 --- #
    DefineLabel(2)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9505, entity=35001504)
    IfFlagEnabled(AND_2, 400001)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=20005, anchor_entity=35001504, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(35000504)
    DeleteObjectVFX(35001504)
    DisableObject(35001504)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteObjectVFX(35001504)
    CreateObjectVFX(35001504, vfx_id=101, model_point=1540)
    End()


@RestartOnRest(35002506)
def Event_35002506():
    """Event 35002506"""
    GotoIfFlagDisabled(Label.L0, flag=35000506)
    DisableObject(35001506)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002506)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.15000000596046448)
    IfCharacterDead(OR_2, PLAYER)
    IfHealthValueEqual(OR_2, PLAYER, value=0)
    EndIfConditionTrue(input_condition=OR_2)
    DestroyObject(35001506)
    EnableFlag(35000506)


@RestartOnRest(35002508)
def Event_35002508():
    """Event 35002508"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=35000506)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=35002508)
    AddSpecialEffect(PLAYER, 4080)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=35002508)
    CancelSpecialEffect(PLAYER, 4080)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(35002600)
def Event_35002600():
    """Event 35002600"""
    GotoIfFlagDisabled(Label.L0, flag=300)
    DisableCharacter(35005230)
    DisableAnimations(35005230)
    DisableObject(35001606)
    DisableTreasure(obj=35001606)
    EnableObject(35001607)
    EnableTreasure(obj=35001607)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagEnabled(1, 35008540)
    EnableFlag(35008540)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(35001600)
    EnableObject(35001606)
    EnableTreasure(obj=35001606)
    DisableObject(35001607)
    DisableTreasure(obj=35001607)


@NeverRestart(35002510)
def Event_35002510():
    """Event 35002510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            35000510,
            35000511,
            0,
            35001510,
            35001511,
            35003511,
            35001512,
            35003512,
            35002511,
            35002512,
            35000512,
            35000513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            35000515,
            35000516,
            0,
            35001515,
            35001516,
            35003516,
            35001517,
            35003517,
            35002516,
            35002517,
            35000517,
            35000518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005681, args=(35000670, 35000671, 35000672, 35000673, 35001670), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103370, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103360, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103350, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103340, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103330, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103320, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103310, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(35000672, 35001670, 35002670, 35000670, 801103300, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    RunCommonEvent(0, 90005681, args=(35000675, 35000676, 35000677, 35000678, 35001675), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103370, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103360, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103350, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103340, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103330, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103320, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103310, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(35000677, 35001675, 35002675, 35000675, 801103300, 801103305, 102, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )


@NeverRestart(35000519)
def Event_35000519():
    """Event 35000519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(35000510)
    DisableFlag(35000520)


@NeverRestart(35002679)
def Event_35002679():
    """Event 35002679"""
    RunCommonEvent(0, 90005681, args=(35000670, 35000671, 35000672, 35000672, 35001670), arg_types="IIIII")


@RestartOnRest(35002490)
def Event_35002490(_, flag: uint, obj: uint, flag_1: uint):
    """Event 35002490"""
    EndIfFlagEnabled(flag)
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)


@RestartOnRest(35002200)
def Event_35002200():
    """Event 35002200"""
    IfCharacterDead(OR_15, 35000200)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(35000200, 17155)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=35000200, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000200, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(35000200, 17155)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002203)
def Event_35002203():
    """Event 35002203"""
    IfCharacterDead(OR_15, 35000203)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    ForceAnimation(35000203, 30002, unknown2=1.0)
    DisableAI(35000203)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002203)
    IfCharacterType(AND_10, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_10, PLAYER, 3710)
    IfConditionTrue(OR_2, input_condition=AND_9)
    IfCharacterHuman(OR_2, PLAYER)
    IfCharacterHollow(OR_2, PLAYER)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=35002220)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(35000203, 20002, loop=True, unknown2=1.0)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(35000203, 20004, loop=True, unknown2=1.0)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(35000203)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002208)
def Event_35002208():
    """Event 35002208"""
    IfCharacterDead(OR_15, 35000208)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(35000208, 8081)
    AddSpecialEffect(35000208, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=35000208, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfCharacterInsideRegion(OR_2, character=35000208, region=35002206)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000208, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(35000208, 8081)
    CancelSpecialEffect(35000208, 8082)
    CancelSpecialEffect(35000208, 5000)
    AddSpecialEffect(35000208, 17153)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002215)
def Event_35002215():
    """Event 35002215"""
    IfCharacterDead(OR_15, 35000215)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002216)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000215, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    ForceAnimation(35000215, 3006, unknown2=1.0)
    CancelSpecialEffect(35000215, 8081)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002220)
def Event_35002220(
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
):
    """Event 35002220"""
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
    IfAttackedWithDamageType(OR_2, attacked_entity=35000420, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000421, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000422, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000423, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000418, attacker=0)
    IfHasAIStatus(OR_3, 35000420, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 35000421, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 35000422, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 35000423, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 35000418, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=OR_5)
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


@RestartOnRest(35002226)
def Event_35002226(
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
):
    """Event 35002226"""
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
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=35002426)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=35000426, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000427, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000428, attacker=0)
    IfHasAIStatus(OR_3, 35000426, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 35000427, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_3, 35000428, ai_status=AIStatusType.Battle)
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
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_3)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfConditionTrue(OR_5, input_condition=AND_6)
    IfConditionTrue(OR_5, input_condition=AND_7)
    IfConditionTrue(OR_5, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_5)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
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


@RestartOnRest(35002230)
def Event_35002230(_, character: uint, seconds: float):
    """Event 35002230"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002230)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_5)
    Wait(seconds)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    CancelSpecialEffect(character, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002239)
def Event_35002239(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 35002239"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    EnableCharacter(character)
    EnableAnimations(character)


@RestartOnRest(35002240)
def Event_35002240(_, character: uint):
    """Event 35002240"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    CancelSpecialEffect(character, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002250)
def Event_35002250():
    """Event 35002250"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002380)
    IfConditionTrue(AND_2, input_condition=AND_1)
    IfCharacterHasSpecialEffect(AND_2, 35000250, 15007)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableSpawner(entity=35003380)
    EnableSpawner(entity=35003381)
    EnableSpawner(entity=35003382)
    EnableSpawner(entity=35003383)
    EnableSpawner(entity=35003388)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002251)
def Event_35002251():
    """Event 35002251"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002380)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 35000250, 15007)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfAttackedWithDamageType(OR_5, attacked_entity=35000350, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_5)
    DisableSpawner(entity=35003380)
    DisableSpawner(entity=35003381)
    DisableSpawner(entity=35003382)
    DisableSpawner(entity=35003383)
    DisableSpawner(entity=35003388)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002253)
def Event_35002253():
    """Event 35002253"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterDead(MAIN, 35000250)
    Kill(35000380, award_souls=True)
    Kill(35000381, award_souls=True)
    Kill(35000382, award_souls=True)
    Kill(35000382, award_souls=True)
    Kill(35000383, award_souls=True)
    Kill(35000388, award_souls=True)
    DisableSpawner(entity=35003380)
    DisableSpawner(entity=35003381)
    DisableSpawner(entity=35003382)
    DisableSpawner(entity=35003383)
    DisableSpawner(entity=35003388)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002258)
def Event_35002258(_, character: uint):
    """Event 35002258"""
    IfCharacterDead(OR_15, character)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(character, 8092)
    Restart()


@RestartOnRest(35002261)
def Event_35002261(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 35002261"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(35002290)
def Event_35002290(_, character: uint):
    """Event 35002290"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    CancelSpecialEffect(character, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002296)
def Event_35002296(_, character: uint):
    """Event 35002296"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002297)
def Event_35002297(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 35002297"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(35002298)
def Event_35002298():
    """Event 35002298"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(OR_1, 35000298, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000298, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_1)
    Wait(0.5)
    SkipLinesIfValueEqual(1, left=3001, right=-1)
    ForceAnimation(35000298, 3001, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(35002320)
def Event_35002320(_, character: uint, animation_id: int):
    """Event 35002320"""
    IfCharacterDead(OR_15, character)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    DisableAI(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002361)
def Event_35002361():
    """Event 35002361"""

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002358)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DisableAI(35000361)
    SetNest(35000361, region=35002359)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002357)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableAI(35000361)
    GotoIfFlagEnabled(Label.L0, flag=35002361)


@RestartOnRest(35002365)
def Event_35002365(
    _,
    character: uint,
    region: uint,
    radius: float,
    seconds: float,
    animation_id: int,
    character_1: uint,
):
    """Event 35002365"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(OR_2, attacked_entity=character_1, attacker=0)
    IfHasAIStatus(OR_2, character_1, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_5, attacked_entity=character, attacker=0)
    IfHasAIStatus(OR_5, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_5)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_2)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(35002390)
def Event_35002390(_, character: uint):
    """Event 35002390"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(35002392)
def Event_35002392(_, character: uint, animation_id: int):
    """Event 35002392"""
    DisableAI(character)
    ForceAnimation(character, animation_id, unknown2=1.0)


@RestartOnRest(35002400)
def Event_35002400():
    """Event 35002400"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=35002400)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=35000400, radius=3.0)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000385, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    CancelSpecialEffect(35000400, 8085)


@RestartOnRest(35002401)
def Event_35002401():
    """Event 35002401"""
    AddSpecialEffect(35000401, 8092)


@RestartOnRest(35002410)
def Event_35002410(
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
    """Event 35002410"""
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
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=35000416, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000410, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000411, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000412, attacker=0)
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
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfConditionTrue(OR_5, input_condition=AND_6)
    IfConditionTrue(OR_5, input_condition=AND_7)
    IfConditionTrue(OR_5, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_5)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    DisableCharacterCollision(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(35002411)
def Event_35002411():
    """Event 35002411"""
    EndIfFlagDisabled(11109959)
    DisableCharacter(35000416)
    DisableCharacter(35000410)
    DisableCharacter(35000411)
    DisableCharacter(35000412)


@RestartOnRest(35002430)
def Event_35002430(
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
    """Event 35002430"""
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfCharacterBackreadEnabled(AND_1, character)
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


@RestartOnRest(35002440)
def Event_35002440(_, character: uint):
    """Event 35002440"""
    Kill(character)


@RestartOnRest(35003500)
def Event_35003500(_, region: uint):
    """Event 35003500"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterOutsideRegion(AND_3, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 9621)
    Restart()


@NeverRestart(35002530)
def Event_35002530():
    """Event 35002530"""
    GotoIfFlagEnabled(Label.L0, flag=35000530)
    EndOfAnimation(obj=35001530, animation_id=0)
    DisableObjectActivation(35001531, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(AND_1, obj_act_id=35003531)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(35000350)
    DisableObjectActivation(35001531, obj_act_id=-1)
    ForceAnimation(35001350, 1, unknown2=1.0)


@NeverRestart(35002642)
def Event_35002642():
    """Event 35002642"""
    DisableObjectActivation(35001642, obj_act_id=27041)
    EndOfAnimation(obj=35001642, animation_id=1)
    End()


@RestartOnRest(35002580)
def Event_35002580():
    """Event 35002580"""
    RegisterLadder(start_climbing_flag=35000580, stop_climbing_flag=35000581, obj=35001580)
    RegisterLadder(start_climbing_flag=35000582, stop_climbing_flag=35000583, obj=35001582)
    RegisterLadder(start_climbing_flag=35000584, stop_climbing_flag=35000585, obj=35001584)
    RegisterLadder(start_climbing_flag=35000586, stop_climbing_flag=35000587, obj=35001586)
    RegisterLadder(start_climbing_flag=35000588, stop_climbing_flag=35000589, obj=35001588)
    RegisterLadder(start_climbing_flag=35000590, stop_climbing_flag=35000591, obj=35001590)
    RegisterLadder(start_climbing_flag=35000592, stop_climbing_flag=35000593, obj=35001592)


@RestartOnRest(35002680)
def Event_35002680():
    """Event 35002680"""
    RegisterLadder(start_climbing_flag=35000680, stop_climbing_flag=35000681, obj=35001680)


@RestartOnRest(35002800)
def Event_35002800():
    """Event 35002800"""
    EndIfFlagEnabled(35000800)
    IfHealthValueLessThanOrEqual(MAIN, 35000800, value=0)
    Wait(4.0)
    PlaySoundEffect(35000800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 35000800)
    KillBossAndDisplayBanner(character=35000800, banner_type=BannerType.Unknown)
    EnableObjectActivation(35001660, obj_act_id=-1)
    EnableFlag(35000800)
    EnableFlag(9125)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61125)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002825, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002826, anchor_type=CoordEntityType.Region)


@RestartOnRest(35002810)
def Event_35002810():
    """Event 35002810"""
    GotoIfFlagDisabled(Label.L0, flag=35000800)
    DisableCharacter(35000800)
    DisableAnimations(35000800)
    Kill(35000800)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002825, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002826, anchor_type=CoordEntityType.Region)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(35000800)
    DisableObjectActivation(35001660, obj_act_id=-1)
    GotoIfFlagEnabled(Label.L1, flag=35000801)
    AddSpecialEffect(35000100, 9531)
    ForceAnimation(35000800, 30001, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002802)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=35000800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(35000801)
    DisableHealthBar(35000800)
    ForceAnimation(35000800, 20001, unknown2=1.0)
    Wait(3.0)
    AddSpecialEffect(35000100, 9532)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 35002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=35002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(35000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(35000800, name=904800002, bar_slot=1)
    Wait(1.0)
    EnableAI(35000800)
    EndIfFlagEnabled(35000800)
    IfHealthRatioLessThanOrEqual(AND_1, 35000800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(35002802)


@RestartOnRest(35002820)
def Event_35002820():
    """Event 35002820"""
    GotoIfFlagDisabled(Label.L0, flag=35000820)
    ForceAnimation(35001820, 2, wait_for_completion=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(35001820, 0, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 35002800)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=35002820)
    IfAttackedWithDamageType(AND_1, attacked_entity=35001820, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(35001820, 1, wait_for_completion=True, unknown2=1.0)
    EnableFlag(35000820)
    End()


@RestartOnRest(35002849)
def Event_35002849():
    """Event 35002849"""
    RunCommonEvent(
        0,
        9005800,
        args=(35000800, 35001800, 35002800, 35002805, 35005800, 10000, 35000801, 35002802),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(35000800, 35001800, 35002800, 35002805, 35002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(35000800, 35001800, 5, 35000801), arg_types="IIiI")
    RunCommonEvent(0, 9005812, args=(35000800, 35001801, 5, 35000801, 5), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(35000800, 921600, 35002805, 35002806, 0, 35002802, 0, 1), arg_types="IiIIIIii")


@RestartOnRest(35002850)
def Event_35002850():
    """Event 35002850"""
    EndIfFlagEnabled(35000850)
    IfHealthValueLessThanOrEqual(MAIN, 35000850, value=0)
    Kill(35005850)
    Wait(4.0)
    PlaySoundEffect(35000850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 35000850)
    KillBossAndDisplayBanner(character=35000850, banner_type=BannerType.DutyFulfilled)
    EnableFlag(35000850)
    EnableFlag(9222)
    EnableFlag(61222)


@RestartOnRest(35002860)
def Event_35002860():
    """Event 35002860"""
    GotoIfFlagDisabled(Label.L0, flag=35000850)
    DisableCharacter(35005850)
    DisableAnimations(35005850)
    Kill(35005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(35000850)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 35002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=35002850)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(35000850)
    SetNetworkUpdateRate(35000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(35000850, name=138600)


@RestartOnRest(35002899)
def Event_35002899():
    """Event 35002899"""
    RunCommonEvent(
        0,
        9005800,
        args=(35000850, 35001850, 35002850, 35002855, 35005850, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(35000850, 35001850, 35002850, 35002855, 35002856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(35000850, 35001850, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(35000850, 921700, 35002855, 35002856, 0, 35002852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(35000700)
def Event_35000700(_, character: uint, obj: uint):
    """Event 35000700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DeleteObjectVFX(obj)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3380)
    DisableFlag(1036499202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L12, flag=3392)
    GotoIfFlagEnabled(Label.L13, flag=3393)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3392, 3393))
    Restart()

    # --- Label 12 --- #
    DefineLabel(12)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    SkipLinesIfFlagEnabled(2, 35000701)
    ForceAnimation(character, 90103, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, 90108, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3392)
    Restart()

    # --- Label 13 --- #
    DefineLabel(13)
    DisableCharacter(character)
    DisableBackread(character)
    CreateObjectVFX(obj, vfx_id=100, model_point=600930)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3393)
    Restart()


@RestartOnRest(35000702)
def Event_35000702(_, obj: uint, character: uint):
    """Event 35000702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 35009209)
    MoveObjectToCharacter(obj, character=character)


@RestartOnRest(35000703)
def Event_35000703(_, seconds: float):
    """Event 35000703"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=35009209)
    IfFlagEnabled(MAIN, 35009209)
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(35009211)


@RestartOnRest(35003710)
def Event_35003710(_, character: uint):
    """Event 35003710"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(35003711)
def Event_35003711(_, character: uint):
    """Event 35003711"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(35003712)
def Event_35003712(_, character: uint):
    """Event 35003712"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(35003713)
def Event_35003713(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 35003713"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4705)
    EndIfFlagRangeAnyEnabled(flag_range=(4708, 4710))
    EndIfFlagDisabled(flag_1)
    EnableFlag(flag)
    EnableFlag(4718)
    WaitFrames(frames=1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(35003714)
def Event_35003714(_, region: uint):
    """Event 35003714"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4705)
    EndIfFlagEnabled(4710)
    IfFlagEnabled(OR_1, 35009255)
    IfFlagEnabled(OR_1, 35009254)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(35009261)
    EnableFlag(4718)
    WaitFrames(frames=1)
    EnableFlag(35009250)
    End()


@RestartOnRest(35003715)
def Event_35003715(_, character: uint, flag: uint):
    """Event 35003715"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4703)
    EndIfFlagEnabled(4705)
    IfFlagEnabled(MAIN, flag)
    DisableAnimations(character)
    Wait(2.0)
    Kill(character, award_souls=True)
    End()


@RestartOnRest(35003720)
def Event_35003720(_, character: uint):
    """Event 35003720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagEnabled(1, 4240)
    DisableFlag(35009303)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4246)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 4246)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

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
    IfFlagEnabled(OR_15, 4246)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(35003721)
def Event_35003721(_, character: uint):
    """Event 35003721"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(35001710)
    IfFlagEnabled(OR_1, 4249)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 4249)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L4, flag=35009323)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableObject(35001710)
    ForceAnimation(character, 90102, unknown2=1.0)
    DisableGravity(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableObject(35001710)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(35001710)
    ForceAnimation(character, 90103, unknown2=1.0)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableFlag(4243)
    SkipLinesIfFlagDisabled(2, 35009323)
    EnableFlag(35009333)
    EnableObject(35001711)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 4249)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(35003722)
def Event_35003722(_, entity: uint):
    """Event 35003722"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4243)
    DisableObject(35001711)
    IfFlagEnabled(AND_1, 4249)
    IfFlagEnabled(OR_1, 35002725)
    IfFlagEnabled(OR_1, 35002726)
    IfConditionTrue(AND_1, input_condition=OR_1)
    AwaitConditionTrue(AND_1)
    GotoIfFlagEnabled(Label.L1, flag=35002725)
    GotoIfFlagEnabled(Label.L2, flag=35002726)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(35002725)
    PlayCutscene(35000010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    EnableFlag(35009323)
    DisableFlag(35002726)
    PlayCutscene(35000020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(35009333)
    ForceAnimation(entity, 90103, unknown2=1.0)
    EnableObject(35001711)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableFlag(4243)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EndIfFlagEnabled(4243)
    Restart()


@RestartOnRest(35003723)
def Event_35003723():
    """Event 35003723"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400382)
    EndIfFlagDisabled(9504)
    EnableNetworkFlag(35009336)
    End()


@NeverRestart(35003724)
def Event_35003724(
    _,
    obj: uint,
    action_button_id: int,
    item_lot_param_id: int,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    model_point: int,
):
    """Event 35003724"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagRangeAnyDisabled(AND_1, flag_range=(first_flag, last_flag))
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfValueEqual(2, left=model_point, right=0)
    CreateObjectVFX(obj, vfx_id=90, model_point=model_point)
    SkipLines(1)
    CreateObjectVFX(obj, vfx_id=90, model_point=6101)
    Wait(1.5)
    IfFlagDisabled(OR_2, flag)
    IfFlagRangeAllEnabled(OR_2, flag_range=(first_flag, last_flag))
    IfActionButtonParamActivated(OR_1, action_button_id=action_button_id, entity=obj)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    DeleteObjectVFX(obj)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj)
    Restart()


@RestartOnRest(35003725)
def Event_35003725():
    """Event 35003725"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400382)
    SkipLinesIfFlagEnabled(2, 4243)
    IfHealthRatioLessThan(AND_1, 35000716, value=0.10000000149011612)
    AwaitConditionTrue(AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableFlag(4243)
    Wait(3.0)
    EnableFlag(35009337)
    End()


@RestartOnRest(35003726)
def Event_35003726():
    """Event 35003726"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4247)
    AwaitFlagEnabled(flag=1045520180)
    DisableNetworkFlag(35009317)
    DisableNetworkFlag(35009318)
    End()


@RestartOnRest(35003727)
def Event_35003727():
    """Event 35003727"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4246)
    IfFlagEnabled(AND_1, 4240)
    IfFlagEnabled(AND_1, 35009306)
    IfEntityWithinDistance(AND_1, entity=35001952, other_entity=20000, radius=15.0)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(4258)
    End()


@RestartOnRest(35003730)
def Event_35003730():
    """Event 35003730"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3631)
    EndIfFlagEnabled(3623)
    IfFlagEnabled(MAIN, 35000500)
    EndIfFlagDisabled(3631)
    GotoIfFlagDisabled(Label.L1, flag=3621)
    EnableFlag(1049539212)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()


@RestartOnRest(35003790)
def Event_35003790():
    """Event 35003790"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(35000500)
    IfFlagEnabled(MAIN, 35000500)
    EndIfCharacterOutsideRegion(character=20000, region=35002500)
    ForceAnimation(20000, 67020, unknown2=1.0)
    End()
