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
    RegisterBonfire(bonfire_flag=13410001, obj=3411951, reaction_distance=5.0)
    RunCommonEvent(20005500, args=(13410830, 13410000, 3410950, 3411950))
    RunCommonEvent(20005780, args=(3411750, 2))
    RunCommonEvent(20005780, args=(3411751, 3))
    RunCommonEvent(20005701, args=(13410830, 13414190, 13415190, 3410190, 3412715, 70000008))
    RunCommonEvent(20005711, args=(13414190, 13415835, 3410190, 3412831, 3412810, 13410831))
    RunCommonEvent(20005720, args=(13414190, 13415190, 13410830, 3410190))
    RunCommonEvent(20005714, args=(13414190, 13415835, 3410190, 3412811, 13410831))
    RunCommonEvent(20005701, args=(13410830, 13414191, 13415191, 3410191, 3412720, 70000013))
    RunCommonEvent(20005711, args=(13414191, 13415835, 3410191, 3412831, 3412810, 13410831))
    RunCommonEvent(20005720, args=(13414191, 13415191, 13410830, 3410191))
    RunCommonEvent(20005714, args=(13414191, 13415835, 3410191, 3412811, 13410831))
    RunCommonEvent(20005110, args=(3410220, 3412491))
    RunCommonEvent(20005110, args=(3410221, 3412492))
    RunCommonEvent(20005202, args=(3410250, 30000, 20004, 3412560))
    RunCommonEvent(20005132, args=(3410251, 10.0, 3412561), arg_types="ifi")
    RunCommonEvent(20005202, args=(3410252, 30000, 20003, 3412562))
    RunCommonEvent(20005202, args=(3410253, 30000, 20003, 3412563))
    RunCommonEvent(20005205, args=(3410302, 700, 1700, 3412530, 0.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(3410303, 700, 1700, 3412530, 0.5), arg_types="iiiif")
    RunCommonEvent(20005205, args=(3410304, 701, 1701, 3412430, 0.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(3410305, 701, 1701, 3412430, 0.5), arg_types="iiiif")
    RunCommonEvent(20005202, args=(3410308, 701, 1701, 3412470))
    RunCommonEvent(20005214, args=(3410309, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005214, args=(3410310, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005214, args=(3410311, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005202, args=(3410313, 701, 1701, 3412421))
    RunCommonEvent(20005202, args=(3410314, 701, 1701, 3412405))
    RunCommonEvent(20005202, args=(3410315, 701, 1701, 3412405))
    RunCommonEvent(20005120, args=(3410316, 8.0), arg_types="if")
    RunCommonEvent(20005111, args=(3410350, 3002, 3412580))
    RunCommonEvent(20005202, args=(3410351, 700, 1700, 3412580))
    RunCommonEvent(20005224, args=(3410400, 700, 1700))
    RunCommonEvent(20005224, args=(3410401, 700, 1700))
    RunCommonEvent(20005224, args=(3410402, 702, 1702))
    RunCommonEvent(20005224, args=(3410405, 700, 1700))
    RunCommonEvent(20005224, args=(3410406, 702, 1702))
    RunCommonEvent(20005110, args=(3410420, 3412490))
    RunCommonEvent(20005110, args=(3410421, 3412490))
    RunCommonEvent(20005110, args=(3410422, 3412490))
    RunCommonEvent(20005114, args=(3410423, 3412491, 3.0), arg_types="iif")
    Event_13415450(0, 3410500, 3020, 0.5)
    Event_13415450(1, 3410501, 3020, 0.800000011920929)
    Event_13415450(2, 3410502, 3026, 0.0)
    Event_13410300()
    RunCommonEvent(20005111, args=(3410550, 3000, 3412650))
    RunCommonEvent(20005111, args=(3410551, 3000, 3412651))
    RunCommonEvent(20005111, args=(3410552, 3000, 3412651))
    RunCommonEvent(20005111, args=(3410553, 3000, 3412650))
    RunCommonEvent(20005110, args=(3410554, 3412651))
    RunCommonEvent(20005110, args=(3410555, 3412491))
    RunCommonEvent(20005110, args=(3410556, 3412491))
    RunCommonEvent(20005110, args=(3410557, 3412491))
    RunCommonEvent(20005110, args=(3410558, 3412492))
    RunCommonEvent(20005110, args=(3410559, 3412492))
    RunCommonEvent(20005110, args=(3410600, 3412510))
    RunCommonEvent(20005110, args=(3410601, 3412480))
    RunCommonEvent(20005110, args=(3410603, 3412480))
    Event_13415350(0, character=3410200)
    Event_13415351(
        0,
        character=3410200,
        region=3412780,
        region_1=3412781,
        region_2=3412782,
        region_3=3412783,
        region_4=3412784,
        copy_draw_parent=3412790,
        copy_draw_parent_1=3412791,
        copy_draw_parent_2=3412792,
        copy_draw_parent_3=3412793
    )
    Event_13415355(0, character=3410200)
    RunCommonEvent(20005341, args=(13410200, 3410200, 13210000))
    RunCommonEvent(20005341, args=(13410201, 3410210, 13101000))
    RunCommonEvent(20005342, args=(13410202, 3410198))
    RunCommonEvent(20005342, args=(13410203, 3410199))
    RunCommonEvent(20005342, args=(13410204, 3410196))
    RunCommonEvent(20005341, args=(13410205, 3410370, 21505000))
    RunCommonEvent(20005341, args=(13410206, 3410371, 21505010))
    RunCommonEvent(20005341, args=(13410207, 3410372, 21505020))
    RunCommonEvent(20005120, args=(3410372, 5.0), arg_types="if")
    RunCommonEvent(20005341, args=(13410208, 3410373, 21505030))
    RunCommonEvent(20005341, args=(13410209, 3410374, 21505040))
    RunCommonEvent(20005120, args=(3410374, 5.0), arg_types="if")
    RunCommonEvent(20005341, args=(13410210, 3410375, 21505050))
    RunCommonEvent(20005120, args=(3410375, 5.0), arg_types="if")
    RunCommonEvent(20005341, args=(13410211, 3410376, 21505060))
    RunCommonEvent(20005341, args=(13410212, 3410377, 21505070))
    Event_13415830()
    Event_13415840()
    Event_13415841()
    Event_13415831()
    Event_13410832()
    Event_13415833()
    Event_13415843()
    Event_13415845()
    RunCommonEvent(20005624, args=(13410450, 13410452, 3411450, 3411451, 3411452, 13411450))
    RunCommonEvent(20005628, args=(13410451, 3411452, 3412451))
    Event_13415400()
    RunCommonEvent(20005622, args=(13410460, 13410462, 3411460, 3411461, 3411462, 13411460))
    Event_13415410()
    RunCommonEvent(20005613, args=(13410595, 13411605, 3411400, 340330, 10010874))
    Event_13415490(0, flag=13410510, entity=3411470, obj=3411471, obj_act_id=342200, obj_act_id_1=13411604)
    Event_13415490(1, flag=13410512, entity=3411474, obj=3411475, obj_act_id=342200, obj_act_id_1=13411607)
    Event_13415490(2, flag=13410513, entity=3411476, obj=3411477, obj_act_id=342200, obj_act_id_1=13411608)
    Event_13415495(
        0,
        flag=13410511,
        entity=3411472,
        entity_1=3411478,
        obj=3411473,
        obj_act_id=342200,
        obj_act_id_1=13411606
    )
    RunCommonEvent(20005523, args=(3411270, 1), arg_types="iB")
    RunCommonEvent(20005523, args=(3411272, 2), arg_types="iB")
    RunCommonEvent(20005520, args=(13410500, 3411320, 63411610))
    RunCommonEvent(20005520, args=(13410501, 3411321, 63411611))
    RunCommonEvent(20005520, args=(13410502, 3411322, 63411612))
    RunCommonEvent(20005520, args=(13410503, 3411323, 63411613))
    RunCommonEvent(20005520, args=(13410504, 3411324, 63411614))
    Event_13415250(0, flag=53410600, entity=3411330)
    Event_13415250(1, flag=53410610, entity=3411331)
    Event_13415250(2, flag=53410620, entity=3411332)
    Event_13415440()
    RegisterLadder(start_climbing_flag=13415150, stop_climbing_flag=13415151, obj=3411430)
    RegisterLadder(start_climbing_flag=13415152, stop_climbing_flag=13415153, obj=3411431)
    RegisterLadder(start_climbing_flag=13415154, stop_climbing_flag=13415155, obj=3411432)
    RegisterLadder(start_climbing_flag=13415156, stop_climbing_flag=13415157, obj=3411433)
    RegisterLadder(start_climbing_flag=13415158, stop_climbing_flag=13415159, obj=3411434)
    RegisterLadder(start_climbing_flag=13415164, stop_climbing_flag=13415165, obj=3411437)
    RunCommonEvent(20005640, args=(13410520, 3411435, 13415160, 13415161))
    RunCommonEvent(20005640, args=(13410521, 3411436, 13415162, 13415163))
    Event_13415430()
    Event_13417500(0, 3411650, 3411500, 0, 1, 2, 3, 3.0, 13417300, 13416300)
    Event_13417500(1, 3411650, 3411501, 10, 11, 12, 13, 3.0, 13417301, 13416301)
    Event_13417500(28, 3411650, 3411528, 0, 1, 2, 3, 3.0, 13417328, 13416328)
    Event_13417500(29, 3411650, 3411529, 10, 11, 12, 13, 3.0, 13417329, 13416329)
    Event_13417500(30, 3411650, 3411530, 0, 1, 2, 3, 3.0, 13417330, 13416330)
    Event_13417500(31, 3411650, 3411531, 10, 11, 12, 13, 3.0, 13417331, 13416331)
    Event_13417500(32, 3411650, 3411532, 0, 1, 2, 3, 3.0, 13417332, 13416332)
    Event_13417500(33, 3411650, 3411533, 10, 11, 12, 13, 3.5, 13417333, 13416333)
    Event_13417500(34, 3411650, 3411534, 0, 1, 2, 3, 3.0, 13417334, 13416334)
    Event_13417500(35, 3411650, 3411535, 10, 11, 12, 13, 3.0, 13417335, 13416335)
    Event_13417500(36, 3411650, 3411536, 0, 1, 2, 3, 3.0, 13417336, 13416336)
    Event_13417500(37, 3411650, 3411537, 10, 11, 12, 13, 3.0, 13417337, 13416337)
    Event_13417500(38, 3411650, 3411538, 10, 11, 12, 13, 3.0, 13417338, 13416338)
    Event_13417500(39, 3411650, 3411539, 0, 1, 2, 3, 3.0, 13417339, 13416339)
    Event_13417500(40, 3411650, 3411540, 10, 11, 12, 13, 3.0, 13417340, 13416340)
    Event_13417500(41, 3411650, 3411541, 0, 1, 2, 3, 3.0, 13417341, 13416341)
    Event_13417500(42, 3411650, 3411542, 10, 11, 12, 13, 3.5, 13417342, 13416342)
    Event_13417500(43, 3411650, 3411543, 0, 1, 2, 3, 3.5, 13417343, 13416343)
    Event_13417500(44, 3411650, 3411544, 10, 11, 12, 13, 3.0, 13417344, 13416344)
    Event_13417600(27, 3411650, 3411625, 0, 1, 2, 3, 3.0, 13417427, 13416427)
    Event_13417600(28, 3411650, 3411626, 10, 11, 12, 13, 3.0, 13417428, 13416428)
    Event_13417600(29, 3411650, 3411627, 0, 1, 2, 3, 3.0, 13417429, 13416429)
    Event_13417600(30, 3411650, 3411628, 10, 11, 12, 13, 3.0, 13417430, 13416430)
    Event_13417600(31, 3411650, 3411629, 0, 1, 2, 3, 3.0, 13417431, 13416431)
    Event_13417600(32, 3411650, 3411630, 10, 11, 12, 13, 3.0, 13417432, 13416432)
    Event_13417600(33, 3411650, 3411631, 0, 1, 2, 3, 3.0, 13417433, 13416433)
    Event_13417600(34, 3411650, 3411632, 10, 11, 12, 13, 3.0, 13417434, 13416434)
    Event_13417500(6, 3411652, 3411506, 0, 1, 2, 3, 4.5, 13417306, 13416306)
    Event_13417500(10, 3411652, 3411510, 0, 1, 2, 3, 4.5, 13417310, 13416310)
    Event_13417500(46, 3411652, 3411546, 0, 1, 2, 3, 4.5, 13417346, 13416346)
    Event_13417500(47, 3411652, 3411547, 20, 21, 22, 23, 1.5, 13417347, 13416347)
    Event_13417500(48, 3411652, 3411548, 0, 1, 2, 3, 4.5, 13417348, 13416348)
    Event_13417500(51, 3411652, 3411551, 20, 21, 22, 23, 1.5, 13417351, 13416351)
    Event_13417500(52, 3411652, 3411552, 0, 1, 2, 3, 4.5, 13417352, 13416352)
    Event_13417500(53, 3411652, 3411553, 0, 1, 2, 3, 4.5, 13417353, 13416353)
    Event_13417500(54, 3411652, 3411554, 0, 1, 2, 3, 4.5, 13417354, 13416354)
    Event_13417500(55, 3411652, 3411555, 20, 21, 22, 23, 1.5, 13417355, 13416355)
    Event_13417500(12, 3411653, 3411512, 0, 1, 2, 3, 4.5, 13417312, 13416312)
    Event_13417500(13, 3411653, 3411513, 10, 11, 12, 13, 4.5, 13417313, 13416313)
    Event_13417500(14, 3411653, 3411514, 20, 21, 22, 23, 1.5, 13417314, 13416314)
    Event_13417500(15, 3411653, 3411515, 0, 1, 2, 3, 4.5, 13417315, 13416315)
    Event_13417500(16, 3411653, 3411516, 10, 11, 12, 13, 4.5, 13417316, 13416316)
    Event_13417500(17, 3411653, 3411517, 20, 21, 22, 23, 1.5, 13417317, 13416317)
    Event_13417500(18, 3411653, 3411518, 0, 1, 2, 3, 4.5, 13417318, 13416318)
    Event_13417500(19, 3411653, 3411519, 10, 11, 12, 13, 4.5, 13417319, 13416319)
    Event_13417500(20, 3411653, 3411520, 20, 21, 22, 23, 1.5, 13417320, 13416320)
    Event_13417500(21, 3411653, 3411521, 0, 1, 2, 3, 4.5, 13417321, 13416321)
    Event_13417500(22, 3411653, 3411522, 10, 11, 12, 13, 4.5, 13417322, 13416322)
    Event_13417500(23, 3411653, 3411523, 20, 21, 22, 23, 1.5, 13417323, 13416323)
    Event_13417500(56, 3411653, 3411556, 0, 1, 2, 3, 4.5, 13417356, 13416356)
    Event_13417500(57, 3411653, 3411557, 10, 11, 12, 13, 4.5, 13417357, 13416357)
    Event_13417500(58, 3411653, 3411558, 0, 1, 2, 3, 4.5, 13417358, 13416358)
    Event_13417500(59, 3411653, 3411559, 10, 11, 12, 13, 4.5, 13417359, 13416359)
    Event_13417500(60, 3411653, 3411560, 0, 1, 2, 3, 4.5, 13417360, 13416360)
    Event_13417500(61, 3411653, 3411561, 10, 11, 12, 13, 4.5, 13417361, 13416361)
    Event_13417500(62, 3411653, 3411562, 0, 1, 2, 3, 4.5, 13417362, 13416362)
    Event_13417500(63, 3411653, 3411563, 10, 11, 12, 13, 4.5, 13417363, 13416363)
    Event_13417500(64, 3411653, 3411564, 0, 1, 2, 3, 4.5, 13417364, 13416364)
    Event_13417500(65, 3411653, 3411565, 10, 11, 12, 13, 4.5, 13417365, 13416365)
    Event_13417500(66, 3411653, 3411566, 20, 21, 22, 23, 1.5, 13417366, 13416366)
    Event_13417500(67, 3411653, 3411567, 20, 21, 22, 23, 1.5, 13417367, 13416367)
    Event_13417600(12, 3411653, 3411610, 0, 1, 2, 3, 4.5, 13417412, 13416412)
    Event_13417600(13, 3411653, 3411611, 10, 11, 12, 13, 4.5, 13417413, 13416413)
    Event_13417600(14, 3411653, 3411612, 0, 1, 2, 3, 4.5, 13417414, 13416414)
    Event_13417600(15, 3411653, 3411613, 10, 11, 12, 13, 4.5, 13417415, 13416415)
    Event_13417600(16, 3411653, 3411614, 0, 1, 2, 3, 4.5, 13417416, 13416416)
    Event_13417600(17, 3411653, 3411615, 10, 11, 12, 13, 4.5, 13417417, 13416417)
    Event_13417600(18, 3411653, 3411616, 0, 1, 2, 3, 4.5, 13417418, 13416418)
    Event_13417600(19, 3411653, 3411617, 10, 11, 12, 13, 4.5, 13417419, 13416419)
    Event_13417600(20, 3411653, 3411618, 0, 1, 2, 3, 4.5, 13417420, 13416420)
    Event_13417600(21, 3411653, 3411619, 20, 21, 22, 23, 1.5, 13417421, 13416421)
    Event_13417600(22, 3411653, 3411620, 0, 1, 2, 3, 4.5, 13417422, 13416422)
    Event_13417600(23, 3411653, 3411621, 10, 11, 12, 13, 4.5, 13417423, 13416423)
    Event_13417600(24, 3411653, 3411622, 20, 21, 22, 23, 1.5, 13417424, 13416424)
    Event_13417600(25, 3411653, 3411623, 20, 21, 22, 23, 1.5, 13417425, 13416425)
    Event_13417600(26, 3411653, 3411624, 20, 21, 22, 23, 1.5, 13417426, 13416426)
    Event_13417500(2, 3411651, 3411502, 0, 1, 2, 3, 4.5, 13417302, 13416302)
    Event_13417500(3, 3411651, 3411503, 10, 11, 12, 13, 4.5, 13417303, 13416303)
    Event_13417500(4, 3411651, 3411504, 0, 1, 2, 3, 4.5, 13417304, 13416304)
    Event_13417500(5, 3411651, 3411505, 10, 11, 12, 13, 4.5, 13417305, 13416305)
    Event_13417500(24, 3411651, 3411524, 0, 1, 2, 3, 4.5, 13417324, 13416324)
    Event_13417500(25, 3411651, 3411525, 10, 11, 12, 13, 4.5, 13417325, 13416325)
    Event_13417500(26, 3411651, 3411526, 0, 1, 2, 3, 4.5, 13417326, 13416326)
    Event_13417500(27, 3411651, 3411527, 10, 11, 12, 13, 4.5, 13417327, 13416327)
    Event_13417500(68, 3411651, 3411568, 0, 1, 2, 3, 4.5, 13417368, 13416368)
    Event_13417500(69, 3411651, 3411569, 10, 11, 12, 13, 4.5, 13417369, 13416369)
    Event_13417500(70, 3411651, 3411570, 0, 1, 2, 3, 4.5, 13417370, 13416370)
    Event_13417500(71, 3411651, 3411571, 0, 1, 2, 3, 4.5, 13417371, 13416371)
    Event_13417500(72, 3411651, 3411572, 20, 21, 22, 23, 1.5, 13417372, 13416372)
    Event_13417500(73, 3411651, 3411573, 0, 1, 2, 3, 4.5, 13417373, 13416373)
    Event_13417500(74, 3411651, 3411574, 10, 11, 12, 13, 4.5, 13417374, 13416374)
    Event_13417500(75, 3411651, 3411575, 0, 1, 2, 3, 4.5, 13417375, 13416375)
    Event_13417500(76, 3411651, 3411576, 10, 11, 12, 13, 4.5, 13417376, 13416376)
    Event_13417500(77, 3411651, 3411577, 0, 1, 2, 3, 4.5, 13417377, 13416377)
    Event_13417500(78, 3411651, 3411578, 10, 11, 12, 13, 4.5, 13417378, 13416378)
    Event_13417500(79, 3411651, 3411579, 20, 21, 22, 23, 1.5, 13417379, 13416379)
    Event_13417500(80, 3411651, 3411580, 20, 21, 22, 23, 1.5, 13417380, 13416380)
    Event_13417500(81, 3411651, 3411581, 20, 21, 22, 23, 1.5, 13417381, 13416381)
    Event_13417500(82, 3411651, 3411582, 20, 21, 22, 23, 1.5, 13417382, 13416382)
    Event_13417500(7, 3411651, 3411507, 20, 21, 22, 23, 1.5, 13417307, 13416307)
    Event_13417500(8, 3411651, 3411508, 20, 21, 22, 23, 1.5, 13417308, 13416308)
    Event_13417500(9, 3411651, 3411509, 20, 21, 22, 23, 1.5, 13417309, 13416309)
    Event_13417600(35, 3411651, 3411633, 20, 21, 22, 23, 1.5, 13417435, 13416435)
    Event_13417600(36, 3411651, 3411634, 20, 21, 22, 23, 1.5, 13417436, 13416436)
    Event_13417600(37, 3411651, 3411635, 20, 21, 22, 23, 1.5, 13417437, 13416437)
    Event_13417600(38, 3411651, 3411636, 20, 21, 22, 23, 1.5, 13417438, 13416438)
    Event_13417600(39, 3411651, 3411637, 20, 21, 22, 23, 1.5, 13417439, 13416439)
    Event_13417500(83, 3411654, 3411583, 0, 1, 2, 3, 4.5, 13417383, 13416383)
    Event_13417500(84, 3411654, 3411584, 10, 11, 12, 13, 4.5, 13417384, 13416384)
    Event_13417500(85, 3411654, 3411585, 0, 1, 2, 3, 4.5, 13417385, 13416385)
    Event_13417500(86, 3411654, 3411586, 10, 11, 12, 13, 4.5, 13417386, 13416386)
    Event_13417500(87, 3411654, 3411587, 0, 1, 2, 3, 4.5, 13417387, 13416387)
    Event_13417500(88, 3411654, 3411588, 10, 11, 12, 13, 4.5, 13417388, 13416388)
    Event_13417500(89, 3411654, 3411589, 0, 1, 2, 3, 4.5, 13417389, 13416389)
    Event_13417500(90, 3411654, 3411590, 10, 11, 12, 13, 4.5, 13417390, 13416390)
    Event_13417500(91, 3411654, 3411591, 20, 21, 22, 23, 1.5, 13417391, 13416391)
    Event_13417500(92, 3411654, 3411592, 20, 21, 22, 23, 1.5, 13417392, 13416392)
    Event_13417500(93, 3411654, 3411593, 20, 21, 22, 23, 1.5, 13417393, 13416393)
    Event_13417500(94, 3411654, 3411594, 20, 21, 22, 23, 1.5, 13417394, 13416394)
    Event_13417500(95, 3411654, 3411595, 20, 21, 22, 23, 1.5, 13417395, 13416395)
    Event_13417500(96, 3411654, 3411596, 20, 21, 22, 23, 1.5, 13417396, 13416396)
    Event_13417500(97, 3411654, 3411597, 20, 21, 22, 23, 1.5, 13417397, 13416397)
    Event_13417500(98, 3411654, 3411598, 20, 21, 22, 23, 1.5, 13417398, 13416398)
    Event_13417500(99, 3411654, 3411599, 20, 21, 22, 23, 1.5, 13417399, 13416399)
    Event_13417600(0, 3411654, 3411600, 20, 21, 22, 23, 1.5, 13417400, 13416400)
    Event_13417600(1, 3411654, 3411601, 20, 21, 22, 23, 1.5, 13417401, 13416401)
    Event_13417600(2, 3411654, 3411602, 20, 21, 22, 23, 1.5, 13417402, 13416402)
    Event_13417600(3, 3411654, 3411603, 20, 21, 22, 23, 1.5, 13417403, 13416403)
    Event_13417600(4, 3411654, 3411604, 20, 21, 22, 23, 1.5, 13417404, 13416404)
    Event_13417600(5, 3411654, 3411605, 20, 21, 22, 23, 1.5, 13417405, 13416405)
    Event_13417600(6, 3411654, 3411606, 20, 21, 22, 23, 1.5, 13417406, 13416406)
    Event_13417600(7, 3411654, 3411607, 20, 21, 22, 23, 1.5, 13417407, 13416407)
    Event_13417600(8, 3411654, 3411608, 10, 11, 12, 13, 4.5, 13417408, 13416408)
    Event_13417600(9, 3411654, 3411609, 0, 1, 2, 3, 4.5, 13417409, 13416409)
    Event_13417600(10, 3411654, 3411610, 10, 11, 12, 13, 4.5, 13417410, 13416410)
    Event_13417600(11, 3411654, 3411611, 0, 1, 2, 3, 4.5, 13417411, 13416411)
    Event_13415420(0, obj=3411390, obj_act_id=341020, obj_act_id_1=3414390)
    Event_13415420(1, obj=3411391, obj_act_id=342100, obj_act_id_1=3414470)
    Event_13415420(2, obj=3411392, obj_act_id=342100, obj_act_id_1=3414471)
    RunCommonEvent(20005650, args=(13410490, 3411310))
    RunCommonEvent(20005628, args=(0, -1, 0))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13415600()
    Event_13415620(0, character=3410705, command_id=1300, obj=3411705, destination=3412705)
    Event_13415640(0, character=3410700)
    DisableSoundEvent(sound_id=3412833)
    DisableSoundEvent(sound_id=3412834)
    Event_13415700()


@NeverRestart(13410300)
def Event_13410300():
    """Event 13410300"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterDead(3410500))
    AND_1.Add(CharacterDead(3410501))
    AND_1.Add(CharacterDead(3410502))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(12902200, host_only=False)


@RestartOnRest(13415250)
def Event_13415250(_, flag: int, entity: int):
    """Event 13415250"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1, loop=True, unknown2=1.0)
    
    MAIN.Await(FlagEnabled(flag))

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, 0, unknown2=1.0)


@RestartOnRest(13415270)
def Event_13415270(_, character: int):
    """Event 13415270"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    CancelSpecialEffect(character, 11970)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(OR_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 11970)


@RestartOnRest(13415350)
def Event_13415350(_, character: int):
    """Event 13415350"""
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    if FlagEnabled(13410200):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3412500))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3412781))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3412782))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3412783))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3412784))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 20003, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableAI(character)
    EnableAnimations(character)
    ReplanAI(character)


@RestartOnRest(13415351)
def Event_13415351(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
    copy_draw_parent: int,
    copy_draw_parent_1: int,
    copy_draw_parent_2: int,
    copy_draw_parent_3: int,
):
    """Event 13415351"""
    if FlagEnabled(13410200):
        return
    GotoIfFlagEnabled(Label.L12, flag=13415434)
    GotoIfFlagEnabled(Label.L11, flag=13415433)
    GotoIfFlagEnabled(Label.L10, flag=13415432)
    GotoIfFlagEnabled(Label.L11, flag=13415433)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_2.Add(CharacterInsideRegion(character=character, region=region))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_3.Add(CharacterInsideRegion(character=character, region=region_1))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    AND_4.Add(OR_1)
    AND_4.Add(CharacterInsideRegion(character=character, region=region))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    AND_5.Add(OR_2)
    AND_5.Add(CharacterInsideRegion(character=character, region=region_1))
    AND_6.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_6.Add(CharacterInsideRegion(character=character, region=region_2))
    AND_7.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_7.Add(CharacterInsideRegion(character=character, region=region_3))
    AND_8.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_8.Add(CharacterInsideRegion(character=character, region=region_4))
    AND_14.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_3.Add(AND_14)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    OR_3.Add(CharacterHollow(PLAYER))
    OR_4.Add(AND_1)
    OR_4.Add(AND_2)
    OR_4.Add(AND_3)
    OR_4.Add(AND_4)
    OR_4.Add(AND_5)
    OR_4.Add(AND_6)
    OR_4.Add(AND_7)
    OR_4.Add(AND_8)
    AND_9.Add(OR_3)
    AND_9.Add(OR_4)
    
    MAIN.Await(AND_9)
    
    SetAIParamID(character, ai_param_id=132051)
    WaitFrames(frames=2)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetNetworkConnectedFlagState(flag=13415432, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_10.Add(TimeElapsed(seconds=10.0))
    AND_11.Add(CharacterHasTAEEvent(character, tae_event_id=60))
    OR_5.Add(AND_10)
    OR_5.Add(AND_11)
    
    MAIN.Await(OR_5)
    
    RestartIfFinishedConditionTrue(input_condition=AND_10)
    SetNetworkConnectedFlagState(flag=13415433, state=FlagSetting.On)

    # --- Label 11 --- #
    DefineLabel(11)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=70))
    
    SetNetworkConnectedFlagState(flag=13415434, state=FlagSetting.On)

    # --- Label 12 --- #
    DefineLabel(12)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_5)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_6)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_7)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_8)

    # --- Label 0 --- #
    DefineLabel(0)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=copy_draw_parent,
    )
    SetAIParamID(character, ai_param_id=132051)
    Goto(Label.L4)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(
        character,
        destination=copy_draw_parent_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=copy_draw_parent_2,
    )
    SetAIParamID(character, ai_param_id=132052)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(
        character,
        destination=copy_draw_parent_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=copy_draw_parent_1,
    )
    SetAIParamID(character, ai_param_id=132052)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(
        character,
        destination=copy_draw_parent_3,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=copy_draw_parent_3,
    )
    SetAIParamID(character, ai_param_id=132052)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(character, 20003, wait_for_completion=True, unknown2=1.0)
    ReplanAI(character)
    DisableFlag(13415432)
    DisableFlag(13415433)
    DisableFlag(13415434)
    Restart()


@RestartOnRest(13415355)
def Event_13415355(_, character: int):
    """Event 13415355"""
    if FlagEnabled(13410200):
        return
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3412611))
    
    SetBackreadStateAlternate(character, True)
    ImmediateActivate(character=character, state=True)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3412611))
    
    SetBackreadStateAlternate(character, False)
    ImmediateActivate(character=character, state=False)
    Restart()


@RestartOnRest(13415400)
def Event_13415400():
    """Event 13415400"""
    RunCommonEvent(
        20005625,
        args=(
            13410450,
            13410452,
            3411450,
            3411451,
            3414451,
            3411452,
            3414452,
            3412451,
            3412452,
            13411450,
            13414450,
            13410451,
        ),
    )


@RestartOnRest(13415410)
def Event_13415410():
    """Event 13415410"""
    RunCommonEvent(
        20005623,
        args=(13410460, 13410462, 3411460, 3411461, 3414461, 3411462, 3414462, 3412461, 3412462, 13411460, 13414460, 0),
    )


@RestartOnRest(13415420)
def Event_13415420(_, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 13415420"""
    DisableNetworkSync()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id_1))
    
    Wait(5.0)
    EnableObjectActivation(obj, obj_act_id=obj_act_id)
    Restart()


@RestartOnRest(13415430)
def Event_13415430():
    """Event 13415430"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 12035))
    
    WaitFrames(frames=1)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4600))
    SkipLinesIfConditionTrue(2, AND_1)
    AddSpecialEffect(PLAYER, 4620)
    AddSpecialEffect(PLAYER, 4621)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(13415440)
def Event_13415440():
    """Event 13415440"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(3411680)
    RestoreObject(3411681)
    RestoreObject(3411682)
    RestoreObject(3411683)
    RestoreObject(3411684)
    RestoreObject(3411685)
    RestoreObject(3411686)
    RestoreObject(3411687)
    RestoreObject(3411690)
    RestoreObject(3411691)
    RestoreObject(3411692)
    RestoreObject(3411693)
    RestoreObject(3411694)
    RestoreObject(3411695)
    RestoreObject(3411696)
    RestoreObject(3411697)


@RestartOnRest(13415450)
def Event_13415450(_, character: int, animation_id: int, seconds: float):
    """Event 13415450"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableAI(character)
    AND_14.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_14)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3412522))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    OR_4.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_4.Add(AND_2)
    
    MAIN.Await(OR_4)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(seconds)
    ForceAnimation(character, animation_id, unknown2=1.0)
    Wait(2.200000047683716)
    AddSpecialEffect(character, 4050)
    AddSpecialEffect(character, 4070)
    EnableGravity(character)
    EnableAI(character)
    Wait(2.5)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13417500)
def Event_13417500(
    _,
    obj__state: int,
    obj: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    animation_id_3: int,
    radius: float,
    obj_flag: int,
    flag: int,
):
    """Event 13417500"""
    ForceAnimation(obj, animation_id, loop=True, unknown2=1.0)
    GotoIfObjectDestructionState(Label.L1, obj=1, state=obj__state)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_14.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_14)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterHollow(PLAYER))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj, radius=radius))
    OR_1.Add(ObjectDestroyed(obj__state))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    GotoIfObjectDestructionState(Label.L1, obj=1, state=obj__state)
    ForceAnimation(obj, animation_id_1, unknown2=1.0)
    Wait(0.800000011920929)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=210,
        behavior_param_id=5210,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    EnableFlag(flag)
    Wait(1.2000000476837158)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(obj, animation_id_2, loop=True, unknown2=1.0)
    OR_3.Add(FramesElapsed(frames=210))
    OR_3.Add(ObjectDestroyed(obj__state))
    
    MAIN.Await(OR_3)
    
    if ObjectNotDestroyed(obj__state):
        AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj, radius=radius))
        if AND_3:
            return RESTART
    ForceAnimation(obj, animation_id_3, wait_for_completion=True, unknown2=1.0)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableFlag(flag)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DestroyObject(obj)
    End()


@RestartOnRest(13417600)
def Event_13417600(
    _,
    obj__state: int,
    obj: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    animation_id_3: int,
    radius: float,
    obj_flag: int,
    flag: int,
):
    """Event 13417600"""
    ForceAnimation(obj, animation_id, loop=True, unknown2=1.0)
    GotoIfObjectDestructionState(Label.L1, obj=1, state=obj__state)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_14.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_14)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterHollow(PLAYER))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj, radius=radius))
    OR_1.Add(ObjectDestroyed(obj__state))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    GotoIfObjectDestructionState(Label.L1, obj=1, state=obj__state)
    ForceAnimation(obj, animation_id_1, unknown2=1.0)
    Wait(0.800000011920929)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=210,
        behavior_param_id=5210,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    EnableFlag(flag)
    Wait(1.2000000476837158)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(obj, animation_id_2, loop=True, unknown2=1.0)
    OR_3.Add(FramesElapsed(frames=210))
    OR_3.Add(ObjectDestroyed(obj__state))
    
    MAIN.Await(OR_3)
    
    if ObjectNotDestroyed(obj__state):
        AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj, radius=radius))
        if AND_3:
            return RESTART
    ForceAnimation(obj, animation_id_3, wait_for_completion=True, unknown2=1.0)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableFlag(flag)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DestroyObject(obj)
    End()


@RestartOnRest(13415490)
def Event_13415490(_, flag: int, entity: int, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 13415490"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 2, unknown2=1.0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObjectActivation(obj, obj_act_id=obj_act_id)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id_1))
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    Wait(2.0)
    ForceAnimation(obj, 2, unknown2=1.0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(entity, 2, unknown2=1.0)


@RestartOnRest(13415495)
def Event_13415495(_, flag: int, entity: int, entity_1: int, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 13415495"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 2, unknown2=1.0)
    ForceAnimation(entity_1, 2, unknown2=1.0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObjectActivation(obj, obj_act_id=obj_act_id)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id_1))
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    Wait(2.0)
    ForceAnimation(obj, 2, unknown2=1.0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id)
    ForceAnimation(entity, 1, unknown2=1.0)
    ForceAnimation(entity_1, 1, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(entity, 2, unknown2=1.0)
    ForceAnimation(entity_1, 2, unknown2=1.0)


@RestartOnRest(13415700)
def Event_13415700():
    """Event 13415700"""
    DisableCharacter(3410197)
    DisableAnimations(3410197)
    DisableTreasure(obj=3411350)
    AND_1.Add(FlagEnabled(711))
    AND_1.Add(CharacterBackreadEnabled(3410197))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(3410197)
    DropMandatoryTreasure(3410197)
    EzstateAIRequest(3410197, command_id=1900, command_slot=1)
    EnableTreasure(obj=3411350)


@RestartOnRest(13415830)
def Event_13415830():
    """Event 13415830"""
    DisableAI(3410830)
    DisableAI(3410831)
    DisableAI(3410832)
    DisableCharacter(3410830)
    DisableCharacter(3410831)
    DisableCharacter(3410832)
    DisableAnimations(3410830)
    DisableAnimations(3410831)
    DisableAnimations(3410832)
    DisableSoundEvent(sound_id=3412833)
    DisableObject(3411810)
    if FlagEnabled(13410830):
        return
    EnableObject(3411810)
    EnableCharacter(3410832)
    EnableAnimations(3410832)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(13415830)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=13410831)
    DisableCharacter(3410832)
    DisableAnimations(3410832)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3412846))
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    NotifyBossBattleStart()
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return
    SkipLinesIfFlagEnabled(7, 13410831)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(34010010, cutscene_flags=0, player_id=10000, move_to_region=3412840, game_map=GRAND_ARCHIVES)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        34010010,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3412840,
        game_map=GRAND_ARCHIVES,
    )
    SkipLines(1)
    PlayCutscene(34010010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(3410832)
    EnableAnimations(3410832)
    Move(3410832, destination=3412841, destination_type=CoordEntityType.Region, copy_draw_parent=3412841)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3412830))

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(3410832)
    EnableImmortality(3410832)
    SetNetworkUpdateRate(3410832, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkConnectedFlagState(flag=13410831, state=FlagSetting.On)
    ActivateMultiplayerBuffs(3410832)
    ActivateMultiplayerBuffs(3410831)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=3,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3410830, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3410831, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3410832, authority_level=UpdateAuthority.Forced)
    EnableBossHealthBar(3410832, name=905250)


@RestartOnRest(13415831)
def Event_13415831():
    """Event 13415831"""
    if FlagEnabled(13410830):
        return
    AND_1.Add(HealthLessThan(3410832, value=0.009999999776482582))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3410832, 11602))
    AND_1.Add(FlagEnabled(13415835))
    
    MAIN.Await(AND_1)
    
    DisableObject(3411810)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(34010000, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(34010000, cutscene_flags=CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(34010000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Move(
        3410830,
        destination=3410832,
        destination_type=CoordEntityType.Character,
        model_point=-1,
        copy_draw_parent=3410832,
    )
    DisableCharacter(3410832)
    DisableAnimations(3410832)
    DisableAI(3410832)
    DisableBossHealthBar(3410832, name=905250)
    SetNetworkUpdateRate(3410832, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3410830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3410831, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3410830)
    EnableAI(3410831)
    EnableCharacter(3410830)
    EnableCharacter(3410831)
    EnableAnimations(3410830)
    EnableAnimations(3410831)
    EnableBossHealthBar(3410830, name=905250)
    EnableBossHealthBar(3410831, name=905251, bar_slot=1)


@NeverRestart(13410832)
def Event_13410832():
    """Event 13410832"""
    if FlagEnabled(13410830):
        return
    AND_1.Add(HealthLessThanOrEqual(3410831, value=0.0))
    AND_2.Add(HealthLessThanOrEqual(3410831, value=0.0))
    AND_2.Add(CharacterHasSpecialEffect(3410830, 11607))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    ForceAnimation(3410830, 20001, skip_transition=True, unknown2=1.0)
    Wait(7.5)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(3410830, 20002, skip_transition=True, unknown2=1.0)
    Wait(8.0)

    # --- Label 2 --- #
    DefineLabel(2)
    PlaySoundEffect(3410830, 777777777, sound_type=SoundType.s_SFX)
    Wait(1.0)
    DisableCharacter(3410830)
    DisableCharacter(3410831)
    DisableAnimations(3410830)
    DisableAnimations(3410831)
    Wait(5.0)
    HandleBossDefeatAndDisplayBanner(boss=3410830, banner=BannerType.UnknownBossDefeat)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableFlag(13410830)
    EnableFlag(9309)
    EnableFlag(6309)


@RestartOnRest(13415833)
def Event_13415833():
    """Event 13415833"""
    RunCommonEvent(20005800, args=(13410830, 3411830, 3412831, 13415835, 3411830, 0, 13410831, 0))
    RunCommonEvent(20005801, args=(13410830, 3411830, 3412831, 13415835, 3411830, 13415836))
    RunCommonEvent(20005820, args=(13410830, 3411830, 3, 13410831))
    RunCommonEvent(20001836, args=(13410830, 13415835, 13415836, 13415830, 3412833, 3412834, 13415831))
    RunCommonEvent(20005840, args=(3411830,))
    RunCommonEvent(20005841, args=(3411830,))
    RunCommonEvent(20005810, args=(13410830, 3411830, 3412831, 10000))


@RestartOnRest(13415840)
def Event_13415840():
    """Event 13415840"""
    DisableFlag(13415842)
    
    MAIN.Await(CharacterHasSpecialEffect(3410830, 11601))
    
    EnableFlag(13415842)
    DisableGravity(3410831)
    DisableAnimations(3410831)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(3410830, 11601))
    
    EnableGravity(3410831)
    EnableAnimations(3410831)
    Restart()


@RestartOnRest(13415841)
def Event_13415841():
    """Event 13415841"""
    MAIN.Await(FlagEnabled(13415842))
    
    Move(
        3410831,
        destination=3410830,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=3410830,
    )
    Restart()


@RestartOnRest(13415843)
def Event_13415843():
    """Event 13415843"""
    if FlagEnabled(13410830):
        return
    EnableImmortality(3410830)
    AND_1.Add(HealthLessThan(3410830, value=0.009999999776482582))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3410830, 11603))
    AND_1.Add(CharacterAlive(3410831))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AND_2.Add(HealthLessThanOrEqual(3410831, value=0.0))
    if AND_2:
        return
    EnableFlag(73410100)
    ForceAnimation(3410831, 20000, skip_transition=True, unknown2=1.0)
    ForceAnimation(3410830, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Restart()


@NeverRestart(13415845)
def Event_13415845():
    """Event 13415845"""
    if FlagEnabled(13410830):
        return
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(13415835))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3412830))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=5250, locked_camera_id=5250)


@RestartOnRest(13415600)
def Event_13415600():
    """Event 13415600"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1415, 1419))
    DisableNetworkConnectedFlagRange(flag_range=(1415, 1419))
    SetNetworkConnectedFlagState(flag=1415, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1400, 1414))
    DisableNetworkConnectedFlagRange(flag_range=(1400, 1414))
    SetNetworkConnectedFlagState(flag=1400, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(13410830))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1400, 1419))
    SetNetworkConnectedFlagState(flag=1401, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1418, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1400)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=3410831, distance=80.0)
    End()


@NeverRestart(13415620)
def Event_13415620(_, character: int, command_id: int, obj: int, destination: int):
    """Event 13415620"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1235, 1239))
    DisableNetworkConnectedFlagRange(flag_range=(1235, 1239))
    SetNetworkConnectedFlagState(flag=1235, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1236))
    AND_1.Add(FlagEnabled(70000063))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1235, 1239))
    SetNetworkConnectedFlagState(flag=1235, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1220, 1234))
    DisableNetworkConnectedFlagRange(flag_range=(1220, 1234))
    SetNetworkConnectedFlagState(flag=1220, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1235)
    AND_4.Add(FlagEnabled(1223))
    AND_4.Add(FlagEnabled(9309))
    AND_4.Add(ObjectNotDestroyed(obj))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1220, 1234))
    SetNetworkConnectedFlagState(flag=1224, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1235, 1239))
    SetNetworkConnectedFlagState(flag=1238, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000063)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1224)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(character)
    DisableCharacterCollision(character)
    EzstateAIRequest(character, command_id=command_id, command_slot=1)
    EnableObjectInvulnerability(obj)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(13415640)
def Event_13415640(_, character: int):
    """Event 13415640"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1215, 1219))
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1215, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1200, 1214))
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1200, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1215)
    AND_7.Add(FlagEnabled(1206))
    AND_7.Add(FlagEnabled(74000309))
    SkipLinesIfConditionFalse(6, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1207, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1218, state=FlagSetting.On)
    EnableFlag(70000152)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1207)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DropMandatoryTreasure(character)
    EzstateAIRequest(character, command_id=1200, command_slot=1)
    End()
