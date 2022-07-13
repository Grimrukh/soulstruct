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
    RegisterGrace(grace_flag=1039540000, obj=1039541950, unknown=5.0)
    RegisterGrace(grace_flag=1039540001, obj=1039541951, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(1039540800, 1039540002, 1039540952, 1039541952, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 90005632, args=(580020, 1039541400, 80020), arg_types="IIi")
    RunCommonEvent(0, 900005610, args=(1039541200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1039541201, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1039541202, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005261, args=(1039540213, 1039542213, 1.0, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1039540257, 30001, 20001, 1039542657, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540558, 1039542610, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(1039540214, 1039542559, 0.0, 0.0, 3037), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1039540615, 30001, 20001, 1039542615, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540616, 30001, 20001, 1039542615, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540609, 30001, 20001, 1039542615, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540613, 30001, 20001, 1039542615, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540614, 30001, 20001, 1039542615, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540619, 30001, 20001, 1039542615, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540633, 30001, 20001, 1039542615, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540630, 30000, 20000, 1039542272, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540631, 30000, 20000, 1039542272, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540632, 30000, 20000, 1039542272, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540272, 30000, 20000, 1039542616, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540273, 30000, 20000, 1039542616, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540212, 30000, 20000, 1039542616, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540667, 1039542667, 0.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540668, 1039542668, 0.5, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540669, 1039542668, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1039540670, 30001, 20001, 1039542670, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540672, 30001, 20001, 1039542672, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540671, 1039542671, 0.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540551, 1039542551, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540552, 1039542552, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540206, 1039542206, 0.0, 3035), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540203, 1039542203, 0.0, 3036), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540553, 1039542553, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540209, 1039542209, 0.0, 3016), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005211,
        args=(1039540211, 30001, 20001, 1039542226, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1039540224, 30002, 20002, 1039542226, 2.0, 0.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1039540226, 30001, 20001, 1039542226, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(1039540303, 30000, 20000, 1039542303, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540504, 1039542504, 2.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(1039540221, 1039542618, 1.0, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540222, 1039542617, 1.0, 0.4000000059604645, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540230, 1039542619, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540231, 1039542619, 1.0, 0.800000011920929, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540232, 1039542619, 1.0, 0.800000011920929, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1039540310, 30001, 20001, 1039542310, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(1039540250, 1039542250, 1.0, 0.0, 3036), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540227, 1039542227, 1.0, 0.0, 3038), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540351, 1039542679, 1.0, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1039540218, 30005, 20005, 1039542350, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1039540219, 30005, 20005, 1039542350, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1039540220, 30005, 20005, 1039542350, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1039540350, 30006, 20006, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1039540207, 30002, 20002, 1039542207, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005250, args=(1039540296, 1039542296, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1039540365, 30000, 20000, 1039542207, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540366, 30000, 20000, 1039542207, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540367, 30000, 20000, 1039542207, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540368, 30000, 20000, 1039542207, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540301, 30000, 20000, 1039542298, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540555, 1039542555, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1039540331, 30002, 20002, 1039542330, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540330, 30002, 20002, 1039542330, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540337, 1039542330, 0.0, 3005), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540341, 1039542341, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540340, 1039542340, 0.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540320, 1039542320, 0.0, 3009), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540342, 1039542342, 1.0, 3000), arg_types="IIfi")
    Event_1039542200(0, 1039540361, 1039542311, 0.0, 3005)
    RunCommonEvent(0, 90005250, args=(1039540311, 1039542311, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540338, 1039542338, 0.0, 3000), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540343, 1039542343, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540321, 1039542322, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540312, 1039542312, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(1039540370, 1039542636, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540371, 1039542636, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540372, 1039542636, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540400, 1039542654, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540401, 1039542654, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540402, 1039542654, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540403, 1039542654, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540404, 1039542860, 1.0, 10.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540680, 1039542860, 1.0, 2.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540681, 1039542860, 1.0, 4.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540682, 1039542860, 1.0, 0.0, -1), arg_types="IIffi")
    AddSpecialEffect(1039540680, 4801)
    AddSpecialEffect(1039540681, 4801)
    RunCommonEvent(0, 90005261, args=(1039540420, 1039542639, 1.0, 0.30000001192092896, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540430, 1039542615, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540431, 1039542615, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540440, 1039542641, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540441, 1039542641, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540442, 1039542641, 1.0, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540443, 1039542641, 1.0, 0.6000000238418579, 3017), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540444, 1039542641, 1.0, 0.0, 3017), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540445, 1039542641, 1.0, 4.0, 3017), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540446, 1039542641, 1.0, 0.20000000298023224, 3017), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540447, 1039542641, 1.0, 0.6000000238418579, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540448, 1039542641, 1.0, 0.4000000059604645, 3016), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540449, 1039542641, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540440, 1039542642, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540441, 1039542642, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540442, 1039542642, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540443, 1039542642, 1.0, 0.4000000059604645, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540444, 1039542642, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540445, 1039542642, 1.0, 1.2000000476837158, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540446, 1039542642, 1.0, 0.4000000059604645, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540447, 1039542642, 1.0, 0.6000000238418579, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540448, 1039542642, 1.0, 0.4000000059604645, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540449, 1039542642, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540470, 1039542658, 1.0, 3.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540471, 1039542680, 1.0, 0.0, 3002), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540690, 1039542658, 1.0, 0.0, 5012), arg_types="IIffi")
    AddSpecialEffect(1039540453, 8081)
    RunCommonEvent(0, 90005261, args=(1039540650, 1039542706, 1.0, 5.0, 3009), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540651, 1039542706, 1.0, 1.0, 3009), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540690, 1039542706, 1.0, 0.0, 5012), arg_types="IIffi")
    AddSpecialEffect(1039540515, 4801)
    AddSpecialEffect(1039540650, 5000)
    AddSpecialEffect(1039540650, 4801)
    AddSpecialEffect(1039540650, 8081)
    AddSpecialEffect(1039540655, 4801)
    AddSpecialEffect(1039540655, 5000)
    AddSpecialEffect(1039540655, 8081)
    AddSpecialEffect(1039540655, 8087)
    AddSpecialEffect(1039540690, 4801)
    RunCommonEvent(0, 90005261, args=(1039540655, 1039542655, 1.0, 0.0, 20), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540656, 1039542655, 1.0, 0.0, 3008), arg_types="IIffi")
    AddSpecialEffect(1039540655, 4801)
    AddSpecialEffect(1039540656, 4801)
    RunCommonEvent(0, 90005261, args=(1039540555, 1039542704, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039540556, 1039542704, 20.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005501,
        args=(1039540510, 1039540511, 5, 1039541510, 1039541511, 1039541512, 1039540512),
        arg_types="IIIIIII",
    )
    Event_1039542510()
    Event_1039542800()
    Event_1039542810()
    Event_1039542849()
    Event_1039542811()
    RunCommonEvent(0, 90005261, args=(1039544680, 1039546680, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544681, 1039546680, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544650, 1039546680, 1.0, 0.0, -1), arg_types="IIffi")
    AddSpecialEffect(1039544680, 8087)
    AddSpecialEffect(1039544681, 8087)
    AddSpecialEffect(1039544680, 5000)
    AddSpecialEffect(1039544681, 5000)
    AddSpecialEffect(1039544600, 8033)
    AddSpecialEffect(1039544601, 8033)
    AddSpecialEffect(1039544602, 8033)
    AddSpecialEffect(1039544603, 8033)
    AddSpecialEffect(1039544604, 8033)
    AddSpecialEffect(1039544605, 8033)
    AddSpecialEffect(1039544606, 8033)
    AddSpecialEffect(1039544600, 8035)
    AddSpecialEffect(1039544601, 8035)
    AddSpecialEffect(1039544602, 8035)
    AddSpecialEffect(1039544603, 8035)
    AddSpecialEffect(1039544604, 8035)
    AddSpecialEffect(1039544605, 8035)
    AddSpecialEffect(1039544606, 8035)
    RunCommonEvent(0, 90005261, args=(1039544252, 1039546250, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544253, 1039546250, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544254, 1039546250, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544550, 1039546550, 1.0, 0.0, 3010), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544551, 1039546550, 1.0, 0.0, 3010), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544552, 1039546550, 1.0, 0.0, 3010), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544553, 1039546550, 1.0, 0.0, 3010), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039544695, 1039546695, 1.0, 0.0, 3008), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1039540380, 1039542380, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1039540383, 30000, 20000, 1039542393, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039540393, 30000, 20000, 1039542393, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1039540627, 1039542627, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540628, 1039542627, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540629, 1039542627, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540607, 1039542607, 3.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540623, 1039542607, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1039540624, 1039542607, 8.0, 0), arg_types="IIfi")
    Event_1039542283(0, character=1039540283)
    Event_1039542520(0, obj_flag=1039542650, obj=1039541260)
    Event_1039542520(1, obj_flag=1039542651, obj=1039541261)
    Event_1039542520(2, obj_flag=1039545650, obj=1039546260)
    Event_1039542520(3, obj_flag=1039545651, obj=1039546261)
    Event_1039542580()
    RunCommonEvent(0, 90005520, args=(1039540592, 1039541592, 1039540593, 1039540863), arg_types="IIII")
    RunCommonEvent(0, 90005520, args=(1039540594, 1039541594, 1039540595, 1039540865), arg_types="IIII")
    Event_1039542498()
    Event_1039542499()
    Event_1039542283(0, character=1039540236)
    Event_1039542283(1, character=1039540238)
    Event_1039542283(2, character=1039540241)
    Event_1039542283(3, character=1039540242)
    Event_1039542283(4, character=1039540244)
    Event_1039542283(5, character=1039540245)
    Event_1039543700(0, character=1039540700)
    Event_1039543702(0, character=1039540700, flag=1039549206)
    RunCommonEvent(0, 90005702, args=(1039540700, 3683, 3680, 3684), arg_types="IIII")
    RunCommonEvent(0, 90005706, args=(1039540701, 930025, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039540700)
    DisableBackread(1039540701)


@RestartOnRest(1039542498)
def Event_1039542498():
    """Event 1039542498"""
    GotoIfFlagDisabled(Label.L0, flag=1039540592)
    DisableNavmeshType(navmesh_id=1039542498, navmesh_type=NavmeshType.Solid)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNavmeshType(navmesh_id=1039542498, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(MAIN, 1039540592)
    DisableNavmeshType(navmesh_id=1039542498, navmesh_type=NavmeshType.Solid)
    End()


@RestartOnRest(1039542811)
def Event_1039542811():
    """Event 1039542811"""
    EndIfFlagEnabled(1039540800)
    IfHealthRatioLessThanOrEqual(AND_1, 1039540800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1039542802)


@RestartOnRest(1039542499)
def Event_1039542499():
    """Event 1039542499"""
    GotoIfFlagDisabled(Label.L0, flag=1039540594)
    DisableNavmeshType(navmesh_id=1039542499, navmesh_type=NavmeshType.Solid)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNavmeshType(navmesh_id=1039542499, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(MAIN, 1039540594)
    DisableNavmeshType(navmesh_id=1039542499, navmesh_type=NavmeshType.Solid)
    End()


@RestartOnRest(1039542290)
def Event_1039542290(_, character: uint):
    """Event 1039542290"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 90000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(1039542283)
def Event_1039542283(_, character: uint):
    """Event 1039542283"""
    Kill(character)
    End()


@NeverRestart(1039542580)
def Event_1039542580():
    """Event 1039542580"""
    RegisterLadder(start_climbing_flag=1039540580, stop_climbing_flag=1039540851, obj=1039541580)
    RegisterLadder(start_climbing_flag=1039540582, stop_climbing_flag=1039540853, obj=1039541582)
    RegisterLadder(start_climbing_flag=1039540584, stop_climbing_flag=1039540855, obj=1039541584)
    RegisterLadder(start_climbing_flag=1039540586, stop_climbing_flag=1039540857, obj=1039541586)
    RegisterLadder(start_climbing_flag=1039540588, stop_climbing_flag=1039540859, obj=1039541588)
    RegisterLadder(start_climbing_flag=1039540590, stop_climbing_flag=1039540861, obj=1039541590)
    RegisterLadder(start_climbing_flag=1039540598, stop_climbing_flag=1039540869, obj=1039541598)
    RegisterLadder(start_climbing_flag=1039540596, stop_climbing_flag=1039540863, obj=1039541596)


@RestartOnRest(1039542200)
def Event_1039542200(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 1039542200"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    Wait(5.0)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)


@RestartOnRest(1039542849)
def Event_1039542849():
    """Event 1039542849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1039540800, 1039541800, 1039542800, 1039542805, 1039545800, 10000, 0, 1039542800),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1039540800, 1039541800, 1039542800, 1039542805, 1039542806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1039540800, 1039541800, 5, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1039540800, 921000, 1039542805, 1039542806, 0, 1039542802, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(1039542800)
def Event_1039542800():
    """Event 1039542800"""
    EndIfFlagEnabled(1039540800)
    IfHealthRatioLessThanOrEqual(MAIN, 1039540800, value=0.0)
    CreateVFX(1039540820)
    CreateVFX(1039540821)
    CreateVFX(1039540822)
    Wait(4.0)
    PlaySoundEffect(1039540800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1039540800)
    KillBossAndDisplayBanner(character=1039540800, banner_type=BannerType.Unknown)
    EnableFlag(1039540800)
    EnableFlag(9182)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61182)


@RestartOnRest(1039542810)
def Event_1039542810():
    """Event 1039542810"""
    GotoIfFlagDisabled(Label.L0, flag=1039540800)
    DisableCharacter(1039540800)
    DisableAnimations(1039540800)
    Kill(1039540800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1039540800)
    IfFlagEnabled(AND_2, 1039542805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1039542800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetNetworkUpdateRate(1039540800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1039540800, name=903100500)
    Wait(1.75)
    EnableAI(1039540800)


@RestartOnRest(1039542720)
def Event_1039542720(_, character: uint, region: uint, seconds: float):
    """Event 1039542720"""
    IfCharacterInsideRegion(AND_5, character=PLAYER, region=region)
    GotoIfConditionTrue(Label.L1, input_condition=AND_5)
    AddSpecialEffect(character, 530)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(seconds)
    CancelSpecialEffect(character, 530)
    End()


@NeverRestart(1039542510)
def Event_1039542510():
    """Event 1039542510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1039540510,
            1039540511,
            5,
            1039541510,
            1039541511,
            1039543511,
            1039541512,
            1039543512,
            1039542511,
            1039542512,
            1039540512,
            1039540513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(1039542520)
def Event_1039542520(_, obj_flag: uint, obj: uint):
    """Event 1039542520"""
    WaitFrames(frames=1)
    EndIfObjectDestroyed(obj)
    IfAttackedWithDamageType(OR_1, attacked_entity=obj, attacker=0, damage_type=DamageType.Fire)
    IfConditionTrue(MAIN, input_condition=OR_1)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=800140, anchor_entity=obj, model_point=200, anchor_type=CoordEntityType.Object)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=200,
        behavior_param_id=200100,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=0.800000011920929,
        repetition_time=0.0,
    )


@RestartOnRest(1039543700)
def Event_1039543700(_, character: uint):
    """Event 1039543700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3690)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3690)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90103, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 1039549206)
    ForceAnimation(character, 90104, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3690)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1039543702)
def Event_1039543702(_, character: uint, flag: uint):
    """Event 1039543702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3690)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    IfFlagEnabled(MAIN, flag)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 9705)
    End()


@RestartOnRest(1039543709)
def Event_1039543709(_, character: uint):
    """Event 1039543709"""
    DisableCharacter(character)
    DisableBackread(character)
    End()
