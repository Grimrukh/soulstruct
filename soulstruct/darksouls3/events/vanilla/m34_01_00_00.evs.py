"""
Grand Archives

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
    RegisterBonfire(bonfire_flag=13410001, obj=3411951, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13410830, bonfire_flag=13410000, character=3410950, obj=3411950)
    CommonFunc_20005780(0, obj=3411750, dummy_id=2)
    CommonFunc_20005780(0, obj=3411751, dummy_id=3)
    CommonFunc_20005701(
        0,
        left=13410830,
        summon_flag=13414190,
        dismissal_flag=13415190,
        character=3410190,
        region=3412715,
        left_1=70000008,
    )
    CommonFunc_20005711(
        0,
        flag=13414190,
        flag_1=13415835,
        character=3410190,
        region=3412831,
        region_1=3412810,
        flag_2=13410831,
    )
    CommonFunc_20005720(0, flag=13414190, flag_1=13415190, flag_2=13410830, character=3410190)
    CommonFunc_20005714(0, flag=13414190, flag_1=13415835, character=3410190, region=3412811, flag_2=13410831)
    CommonFunc_20005701(
        0,
        left=13410830,
        summon_flag=13414191,
        dismissal_flag=13415191,
        character=3410191,
        region=3412720,
        left_1=70000013,
    )
    CommonFunc_20005711(
        0,
        flag=13414191,
        flag_1=13415835,
        character=3410191,
        region=3412831,
        region_1=3412810,
        flag_2=13410831,
    )
    CommonFunc_20005720(0, flag=13414191, flag_1=13415191, flag_2=13410830, character=3410191)
    CommonFunc_20005714(0, flag=13414191, flag_1=13415835, character=3410191, region=3412811, flag_2=13410831)
    CommonFunc_20005110(0, character=3410220, region=3412491)
    CommonFunc_20005110(0, character=3410221, region=3412492)
    CommonFunc_20005202(0, character=3410250, animation_id=30000, animation_id_1=20004, region=3412560)
    CommonFunc_20005132(0, character=3410251, radius=10.0, region=3412561)
    CommonFunc_20005202(0, character=3410252, animation_id=30000, animation_id_1=20003, region=3412562)
    CommonFunc_20005202(0, character=3410253, animation_id=30000, animation_id_1=20003, region=3412563)
    CommonFunc_20005205(0, character=3410302, animation_id=700, animation_id_1=1700, region=3412530, seconds=0.0)
    CommonFunc_20005205(0, character=3410303, animation_id=700, animation_id_1=1700, region=3412530, seconds=0.5)
    CommonFunc_20005205(0, character=3410304, animation_id=701, animation_id_1=1701, region=3412430, seconds=0.0)
    CommonFunc_20005205(0, character=3410305, animation_id=701, animation_id_1=1701, region=3412430, seconds=0.5)
    CommonFunc_20005202(0, character=3410308, animation_id=701, animation_id_1=1701, region=3412470)
    CommonFunc_20005214(0, character=3410309, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005214(0, character=3410310, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005214(0, character=3410311, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005202(0, character=3410313, animation_id=701, animation_id_1=1701, region=3412421)
    CommonFunc_20005202(0, character=3410314, animation_id=701, animation_id_1=1701, region=3412405)
    CommonFunc_20005202(0, character=3410315, animation_id=701, animation_id_1=1701, region=3412405)
    CommonFunc_20005120(0, character=3410316, radius=8.0)
    CommonFunc_20005111(0, character=3410350, animation_id=3002, region=3412580)
    CommonFunc_20005202(0, character=3410351, animation_id=700, animation_id_1=1700, region=3412580)
    CommonFunc_20005224(0, character=3410400, animation_id=700, animation_id_1=1700)
    CommonFunc_20005224(0, character=3410401, animation_id=700, animation_id_1=1700)
    CommonFunc_20005224(0, character=3410402, animation_id=702, animation_id_1=1702)
    CommonFunc_20005224(0, character=3410405, animation_id=700, animation_id_1=1700)
    CommonFunc_20005224(0, character=3410406, animation_id=702, animation_id_1=1702)
    CommonFunc_20005110(0, character=3410420, region=3412490)
    CommonFunc_20005110(0, character=3410421, region=3412490)
    CommonFunc_20005110(0, character=3410422, region=3412490)
    CommonFunc_20005114(0, character=3410423, region=3412491, seconds=3.0)
    Event_13415450(0, character=3410500, animation_id=3020, seconds=0.5)
    Event_13415450(1, character=3410501, animation_id=3020, seconds=0.800000011920929)
    Event_13415450(2, character=3410502, animation_id=3026, seconds=0.0)
    Event_13410300()
    CommonFunc_20005111(0, character=3410550, animation_id=3000, region=3412650)
    CommonFunc_20005111(0, character=3410551, animation_id=3000, region=3412651)
    CommonFunc_20005111(0, character=3410552, animation_id=3000, region=3412651)
    CommonFunc_20005111(0, character=3410553, animation_id=3000, region=3412650)
    CommonFunc_20005110(0, character=3410554, region=3412651)
    CommonFunc_20005110(0, character=3410555, region=3412491)
    CommonFunc_20005110(0, character=3410556, region=3412491)
    CommonFunc_20005110(0, character=3410557, region=3412491)
    CommonFunc_20005110(0, character=3410558, region=3412492)
    CommonFunc_20005110(0, character=3410559, region=3412492)
    CommonFunc_20005110(0, character=3410600, region=3412510)
    CommonFunc_20005110(0, character=3410601, region=3412480)
    CommonFunc_20005110(0, character=3410603, region=3412480)
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
        copy_draw_parent_3=3412793,
    )
    Event_13415355(0, character=3410200)
    CommonFunc_20005341(0, flag=13410200, character=3410200, item_lot=13210000)
    CommonFunc_20005341(0, flag=13410201, character=3410210, item_lot=13101000)
    CommonFunc_20005342(0, flag=13410202, character=3410198)
    CommonFunc_20005342(0, flag=13410203, character=3410199)
    CommonFunc_20005342(0, flag=13410204, character=3410196)
    CommonFunc_20005341(0, flag=13410205, character=3410370, item_lot=21505000)
    CommonFunc_20005341(0, flag=13410206, character=3410371, item_lot=21505010)
    CommonFunc_20005341(0, flag=13410207, character=3410372, item_lot=21505020)
    CommonFunc_20005120(0, character=3410372, radius=5.0)
    CommonFunc_20005341(0, flag=13410208, character=3410373, item_lot=21505030)
    CommonFunc_20005341(0, flag=13410209, character=3410374, item_lot=21505040)
    CommonFunc_20005120(0, character=3410374, radius=5.0)
    CommonFunc_20005341(0, flag=13410210, character=3410375, item_lot=21505050)
    CommonFunc_20005120(0, character=3410375, radius=5.0)
    CommonFunc_20005341(0, flag=13410211, character=3410376, item_lot=21505060)
    CommonFunc_20005341(0, flag=13410212, character=3410377, item_lot=21505070)
    Event_13415830()
    Event_13415840()
    Event_13415841()
    Event_13415831()
    Event_13410832()
    Event_13415833()
    Event_13415843()
    Event_13415845()
    CommonFunc_20005624(0, flag=13410450, flag_1=13410452, entity=3411450, obj=3411451, obj_1=3411452, flag_2=13411450)
    CommonFunc_20005628(0, flag=13410451, obj=3411452, region=3412451)
    Event_13415400()
    CommonFunc_20005622(0, flag=13410460, flag_1=13410462, entity=3411460, obj=3411461, obj_1=3411462, flag_2=13411460)
    Event_13415410()
    CommonFunc_20005613(0, flag=13410595, obj_act_id=13411605, obj=3411400, obj_act_id_1=340330, text=10010874)
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
        obj_act_id_1=13411606,
    )
    CommonFunc_20005523(0, obj=3411270, completion_count=1)
    CommonFunc_20005523(0, obj=3411272, completion_count=2)
    CommonFunc_20005520(0, flag=13410500, obj=3411320, obj_act_id=63411610)
    CommonFunc_20005520(0, flag=13410501, obj=3411321, obj_act_id=63411611)
    CommonFunc_20005520(0, flag=13410502, obj=3411322, obj_act_id=63411612)
    CommonFunc_20005520(0, flag=13410503, obj=3411323, obj_act_id=63411613)
    CommonFunc_20005520(0, flag=13410504, obj=3411324, obj_act_id=63411614)
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
    CommonFunc_20005640(0, flag=13410520, obj=3411435, start_climbing_flag=13415160, stop_climbing_flag=13415161)
    CommonFunc_20005640(0, flag=13410521, obj=3411436, start_climbing_flag=13415162, stop_climbing_flag=13415163)
    Event_13415430()
    Event_13417500(
        0,
        obj=3411650,
        obj_1=3411500,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417300,
        flag=13416300,
    )
    Event_13417500(
        1,
        obj=3411650,
        obj_1=3411501,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417301,
        flag=13416301,
    )
    Event_13417500(
        28,
        obj=3411650,
        obj_1=3411528,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417328,
        flag=13416328,
    )
    Event_13417500(
        29,
        obj=3411650,
        obj_1=3411529,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417329,
        flag=13416329,
    )
    Event_13417500(
        30,
        obj=3411650,
        obj_1=3411530,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417330,
        flag=13416330,
    )
    Event_13417500(
        31,
        obj=3411650,
        obj_1=3411531,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417331,
        flag=13416331,
    )
    Event_13417500(
        32,
        obj=3411650,
        obj_1=3411532,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417332,
        flag=13416332,
    )
    Event_13417500(
        33,
        obj=3411650,
        obj_1=3411533,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.5,
        obj_flag=13417333,
        flag=13416333,
    )
    Event_13417500(
        34,
        obj=3411650,
        obj_1=3411534,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417334,
        flag=13416334,
    )
    Event_13417500(
        35,
        obj=3411650,
        obj_1=3411535,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417335,
        flag=13416335,
    )
    Event_13417500(
        36,
        obj=3411650,
        obj_1=3411536,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417336,
        flag=13416336,
    )
    Event_13417500(
        37,
        obj=3411650,
        obj_1=3411537,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417337,
        flag=13416337,
    )
    Event_13417500(
        38,
        obj=3411650,
        obj_1=3411538,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417338,
        flag=13416338,
    )
    Event_13417500(
        39,
        obj=3411650,
        obj_1=3411539,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417339,
        flag=13416339,
    )
    Event_13417500(
        40,
        obj=3411650,
        obj_1=3411540,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417340,
        flag=13416340,
    )
    Event_13417500(
        41,
        obj=3411650,
        obj_1=3411541,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417341,
        flag=13416341,
    )
    Event_13417500(
        42,
        obj=3411650,
        obj_1=3411542,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.5,
        obj_flag=13417342,
        flag=13416342,
    )
    Event_13417500(
        43,
        obj=3411650,
        obj_1=3411543,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.5,
        obj_flag=13417343,
        flag=13416343,
    )
    Event_13417500(
        44,
        obj=3411650,
        obj_1=3411544,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417344,
        flag=13416344,
    )
    Event_13417600(
        27,
        obj=3411650,
        obj_1=3411625,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417427,
        flag=13416427,
    )
    Event_13417600(
        28,
        obj=3411650,
        obj_1=3411626,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417428,
        flag=13416428,
    )
    Event_13417600(
        29,
        obj=3411650,
        obj_1=3411627,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417429,
        flag=13416429,
    )
    Event_13417600(
        30,
        obj=3411650,
        obj_1=3411628,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417430,
        flag=13416430,
    )
    Event_13417600(
        31,
        obj=3411650,
        obj_1=3411629,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417431,
        flag=13416431,
    )
    Event_13417600(
        32,
        obj=3411650,
        obj_1=3411630,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417432,
        flag=13416432,
    )
    Event_13417600(
        33,
        obj=3411650,
        obj_1=3411631,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=3.0,
        obj_flag=13417433,
        flag=13416433,
    )
    Event_13417600(
        34,
        obj=3411650,
        obj_1=3411632,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=3.0,
        obj_flag=13417434,
        flag=13416434,
    )
    Event_13417500(
        6,
        obj=3411652,
        obj_1=3411506,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417306,
        flag=13416306,
    )
    Event_13417500(
        10,
        obj=3411652,
        obj_1=3411510,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417310,
        flag=13416310,
    )
    Event_13417500(
        46,
        obj=3411652,
        obj_1=3411546,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417346,
        flag=13416346,
    )
    Event_13417500(
        47,
        obj=3411652,
        obj_1=3411547,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417347,
        flag=13416347,
    )
    Event_13417500(
        48,
        obj=3411652,
        obj_1=3411548,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417348,
        flag=13416348,
    )
    Event_13417500(
        51,
        obj=3411652,
        obj_1=3411551,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417351,
        flag=13416351,
    )
    Event_13417500(
        52,
        obj=3411652,
        obj_1=3411552,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417352,
        flag=13416352,
    )
    Event_13417500(
        53,
        obj=3411652,
        obj_1=3411553,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417353,
        flag=13416353,
    )
    Event_13417500(
        54,
        obj=3411652,
        obj_1=3411554,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417354,
        flag=13416354,
    )
    Event_13417500(
        55,
        obj=3411652,
        obj_1=3411555,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417355,
        flag=13416355,
    )
    Event_13417500(
        12,
        obj=3411653,
        obj_1=3411512,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417312,
        flag=13416312,
    )
    Event_13417500(
        13,
        obj=3411653,
        obj_1=3411513,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417313,
        flag=13416313,
    )
    Event_13417500(
        14,
        obj=3411653,
        obj_1=3411514,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417314,
        flag=13416314,
    )
    Event_13417500(
        15,
        obj=3411653,
        obj_1=3411515,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417315,
        flag=13416315,
    )
    Event_13417500(
        16,
        obj=3411653,
        obj_1=3411516,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417316,
        flag=13416316,
    )
    Event_13417500(
        17,
        obj=3411653,
        obj_1=3411517,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417317,
        flag=13416317,
    )
    Event_13417500(
        18,
        obj=3411653,
        obj_1=3411518,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417318,
        flag=13416318,
    )
    Event_13417500(
        19,
        obj=3411653,
        obj_1=3411519,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417319,
        flag=13416319,
    )
    Event_13417500(
        20,
        obj=3411653,
        obj_1=3411520,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417320,
        flag=13416320,
    )
    Event_13417500(
        21,
        obj=3411653,
        obj_1=3411521,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417321,
        flag=13416321,
    )
    Event_13417500(
        22,
        obj=3411653,
        obj_1=3411522,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417322,
        flag=13416322,
    )
    Event_13417500(
        23,
        obj=3411653,
        obj_1=3411523,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417323,
        flag=13416323,
    )
    Event_13417500(
        56,
        obj=3411653,
        obj_1=3411556,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417356,
        flag=13416356,
    )
    Event_13417500(
        57,
        obj=3411653,
        obj_1=3411557,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417357,
        flag=13416357,
    )
    Event_13417500(
        58,
        obj=3411653,
        obj_1=3411558,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417358,
        flag=13416358,
    )
    Event_13417500(
        59,
        obj=3411653,
        obj_1=3411559,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417359,
        flag=13416359,
    )
    Event_13417500(
        60,
        obj=3411653,
        obj_1=3411560,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417360,
        flag=13416360,
    )
    Event_13417500(
        61,
        obj=3411653,
        obj_1=3411561,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417361,
        flag=13416361,
    )
    Event_13417500(
        62,
        obj=3411653,
        obj_1=3411562,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417362,
        flag=13416362,
    )
    Event_13417500(
        63,
        obj=3411653,
        obj_1=3411563,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417363,
        flag=13416363,
    )
    Event_13417500(
        64,
        obj=3411653,
        obj_1=3411564,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417364,
        flag=13416364,
    )
    Event_13417500(
        65,
        obj=3411653,
        obj_1=3411565,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417365,
        flag=13416365,
    )
    Event_13417500(
        66,
        obj=3411653,
        obj_1=3411566,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417366,
        flag=13416366,
    )
    Event_13417500(
        67,
        obj=3411653,
        obj_1=3411567,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417367,
        flag=13416367,
    )
    Event_13417600(
        12,
        obj=3411653,
        obj_1=3411610,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417412,
        flag=13416412,
    )
    Event_13417600(
        13,
        obj=3411653,
        obj_1=3411611,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417413,
        flag=13416413,
    )
    Event_13417600(
        14,
        obj=3411653,
        obj_1=3411612,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417414,
        flag=13416414,
    )
    Event_13417600(
        15,
        obj=3411653,
        obj_1=3411613,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417415,
        flag=13416415,
    )
    Event_13417600(
        16,
        obj=3411653,
        obj_1=3411614,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417416,
        flag=13416416,
    )
    Event_13417600(
        17,
        obj=3411653,
        obj_1=3411615,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417417,
        flag=13416417,
    )
    Event_13417600(
        18,
        obj=3411653,
        obj_1=3411616,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417418,
        flag=13416418,
    )
    Event_13417600(
        19,
        obj=3411653,
        obj_1=3411617,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417419,
        flag=13416419,
    )
    Event_13417600(
        20,
        obj=3411653,
        obj_1=3411618,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417420,
        flag=13416420,
    )
    Event_13417600(
        21,
        obj=3411653,
        obj_1=3411619,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417421,
        flag=13416421,
    )
    Event_13417600(
        22,
        obj=3411653,
        obj_1=3411620,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417422,
        flag=13416422,
    )
    Event_13417600(
        23,
        obj=3411653,
        obj_1=3411621,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417423,
        flag=13416423,
    )
    Event_13417600(
        24,
        obj=3411653,
        obj_1=3411622,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417424,
        flag=13416424,
    )
    Event_13417600(
        25,
        obj=3411653,
        obj_1=3411623,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417425,
        flag=13416425,
    )
    Event_13417600(
        26,
        obj=3411653,
        obj_1=3411624,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417426,
        flag=13416426,
    )
    Event_13417500(
        2,
        obj=3411651,
        obj_1=3411502,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417302,
        flag=13416302,
    )
    Event_13417500(
        3,
        obj=3411651,
        obj_1=3411503,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417303,
        flag=13416303,
    )
    Event_13417500(
        4,
        obj=3411651,
        obj_1=3411504,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417304,
        flag=13416304,
    )
    Event_13417500(
        5,
        obj=3411651,
        obj_1=3411505,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417305,
        flag=13416305,
    )
    Event_13417500(
        24,
        obj=3411651,
        obj_1=3411524,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417324,
        flag=13416324,
    )
    Event_13417500(
        25,
        obj=3411651,
        obj_1=3411525,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417325,
        flag=13416325,
    )
    Event_13417500(
        26,
        obj=3411651,
        obj_1=3411526,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417326,
        flag=13416326,
    )
    Event_13417500(
        27,
        obj=3411651,
        obj_1=3411527,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417327,
        flag=13416327,
    )
    Event_13417500(
        68,
        obj=3411651,
        obj_1=3411568,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417368,
        flag=13416368,
    )
    Event_13417500(
        69,
        obj=3411651,
        obj_1=3411569,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417369,
        flag=13416369,
    )
    Event_13417500(
        70,
        obj=3411651,
        obj_1=3411570,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417370,
        flag=13416370,
    )
    Event_13417500(
        71,
        obj=3411651,
        obj_1=3411571,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417371,
        flag=13416371,
    )
    Event_13417500(
        72,
        obj=3411651,
        obj_1=3411572,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417372,
        flag=13416372,
    )
    Event_13417500(
        73,
        obj=3411651,
        obj_1=3411573,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417373,
        flag=13416373,
    )
    Event_13417500(
        74,
        obj=3411651,
        obj_1=3411574,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417374,
        flag=13416374,
    )
    Event_13417500(
        75,
        obj=3411651,
        obj_1=3411575,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417375,
        flag=13416375,
    )
    Event_13417500(
        76,
        obj=3411651,
        obj_1=3411576,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417376,
        flag=13416376,
    )
    Event_13417500(
        77,
        obj=3411651,
        obj_1=3411577,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417377,
        flag=13416377,
    )
    Event_13417500(
        78,
        obj=3411651,
        obj_1=3411578,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417378,
        flag=13416378,
    )
    Event_13417500(
        79,
        obj=3411651,
        obj_1=3411579,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417379,
        flag=13416379,
    )
    Event_13417500(
        80,
        obj=3411651,
        obj_1=3411580,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417380,
        flag=13416380,
    )
    Event_13417500(
        81,
        obj=3411651,
        obj_1=3411581,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417381,
        flag=13416381,
    )
    Event_13417500(
        82,
        obj=3411651,
        obj_1=3411582,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417382,
        flag=13416382,
    )
    Event_13417500(
        7,
        obj=3411651,
        obj_1=3411507,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417307,
        flag=13416307,
    )
    Event_13417500(
        8,
        obj=3411651,
        obj_1=3411508,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417308,
        flag=13416308,
    )
    Event_13417500(
        9,
        obj=3411651,
        obj_1=3411509,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417309,
        flag=13416309,
    )
    Event_13417600(
        35,
        obj=3411651,
        obj_1=3411633,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417435,
        flag=13416435,
    )
    Event_13417600(
        36,
        obj=3411651,
        obj_1=3411634,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417436,
        flag=13416436,
    )
    Event_13417600(
        37,
        obj=3411651,
        obj_1=3411635,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417437,
        flag=13416437,
    )
    Event_13417600(
        38,
        obj=3411651,
        obj_1=3411636,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417438,
        flag=13416438,
    )
    Event_13417600(
        39,
        obj=3411651,
        obj_1=3411637,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417439,
        flag=13416439,
    )
    Event_13417500(
        83,
        obj=3411654,
        obj_1=3411583,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417383,
        flag=13416383,
    )
    Event_13417500(
        84,
        obj=3411654,
        obj_1=3411584,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417384,
        flag=13416384,
    )
    Event_13417500(
        85,
        obj=3411654,
        obj_1=3411585,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417385,
        flag=13416385,
    )
    Event_13417500(
        86,
        obj=3411654,
        obj_1=3411586,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417386,
        flag=13416386,
    )
    Event_13417500(
        87,
        obj=3411654,
        obj_1=3411587,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417387,
        flag=13416387,
    )
    Event_13417500(
        88,
        obj=3411654,
        obj_1=3411588,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417388,
        flag=13416388,
    )
    Event_13417500(
        89,
        obj=3411654,
        obj_1=3411589,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417389,
        flag=13416389,
    )
    Event_13417500(
        90,
        obj=3411654,
        obj_1=3411590,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417390,
        flag=13416390,
    )
    Event_13417500(
        91,
        obj=3411654,
        obj_1=3411591,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417391,
        flag=13416391,
    )
    Event_13417500(
        92,
        obj=3411654,
        obj_1=3411592,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417392,
        flag=13416392,
    )
    Event_13417500(
        93,
        obj=3411654,
        obj_1=3411593,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417393,
        flag=13416393,
    )
    Event_13417500(
        94,
        obj=3411654,
        obj_1=3411594,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417394,
        flag=13416394,
    )
    Event_13417500(
        95,
        obj=3411654,
        obj_1=3411595,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417395,
        flag=13416395,
    )
    Event_13417500(
        96,
        obj=3411654,
        obj_1=3411596,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417396,
        flag=13416396,
    )
    Event_13417500(
        97,
        obj=3411654,
        obj_1=3411597,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417397,
        flag=13416397,
    )
    Event_13417500(
        98,
        obj=3411654,
        obj_1=3411598,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417398,
        flag=13416398,
    )
    Event_13417500(
        99,
        obj=3411654,
        obj_1=3411599,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417399,
        flag=13416399,
    )
    Event_13417600(
        0,
        obj=3411654,
        obj_1=3411600,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417400,
        flag=13416400,
    )
    Event_13417600(
        1,
        obj=3411654,
        obj_1=3411601,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417401,
        flag=13416401,
    )
    Event_13417600(
        2,
        obj=3411654,
        obj_1=3411602,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417402,
        flag=13416402,
    )
    Event_13417600(
        3,
        obj=3411654,
        obj_1=3411603,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417403,
        flag=13416403,
    )
    Event_13417600(
        4,
        obj=3411654,
        obj_1=3411604,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417404,
        flag=13416404,
    )
    Event_13417600(
        5,
        obj=3411654,
        obj_1=3411605,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417405,
        flag=13416405,
    )
    Event_13417600(
        6,
        obj=3411654,
        obj_1=3411606,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417406,
        flag=13416406,
    )
    Event_13417600(
        7,
        obj=3411654,
        obj_1=3411607,
        animation_id=20,
        animation_id_1=21,
        animation_id_2=22,
        animation_id_3=23,
        radius=1.5,
        obj_flag=13417407,
        flag=13416407,
    )
    Event_13417600(
        8,
        obj=3411654,
        obj_1=3411608,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417408,
        flag=13416408,
    )
    Event_13417600(
        9,
        obj=3411654,
        obj_1=3411609,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417409,
        flag=13416409,
    )
    Event_13417600(
        10,
        obj=3411654,
        obj_1=3411610,
        animation_id=10,
        animation_id_1=11,
        animation_id_2=12,
        animation_id_3=13,
        radius=4.5,
        obj_flag=13417410,
        flag=13416410,
    )
    Event_13417600(
        11,
        obj=3411654,
        obj_1=3411611,
        animation_id=0,
        animation_id_1=1,
        animation_id_2=2,
        animation_id_3=3,
        radius=4.5,
        obj_flag=13417411,
        flag=13416411,
    )
    Event_13415420(0, obj=3411390, obj_act_id=341020, obj_act_id_1=3414390)
    Event_13415420(1, obj=3411391, obj_act_id=342100, obj_act_id_1=3414470)
    Event_13415420(2, obj=3411392, obj_act_id=342100, obj_act_id_1=3414471)
    CommonFunc_20005650(0, flag=13410490, obj=3411310)
    CommonFunc_20005628(0, flag=0, obj=-1, region=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13415600()
    Event_13415620(0, character=3410705, command_id=1300, obj=3411705, destination=3412705)
    Event_13415640(0, character=3410700)
    DisableSoundEvent(sound_id=3412833)
    DisableSoundEvent(sound_id=3412834)
    Event_13415700()


@ContinueOnRest(13410300)
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
    RemoveSpecialEffect(character, 11970)
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
    CommonFunc_20005625(
        0,
        flag=13410450,
        flag_1=13410452,
        obj=3411450,
        obj_1=3411451,
        obj_act_id=3414451,
        obj_2=3411452,
        obj_act_id_1=3414452,
        region=3412451,
        region_1=3412452,
        flag_2=13411450,
        flag_3=13414450,
        left=13410451,
    )


@RestartOnRest(13415410)
def Event_13415410():
    """Event 13415410"""
    CommonFunc_20005623(
        0,
        flag=13410460,
        flag_1=13410462,
        obj=3411460,
        obj_1=3411461,
        obj_act_id=3414461,
        obj_2=3411462,
        obj_act_id_1=3414462,
        region=3412461,
        region_1=3412462,
        flag_2=13411460,
        flag_3=13414460,
        left=0,
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
    obj: int,
    obj_1: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    animation_id_3: int,
    radius: float,
    obj_flag: int,
    flag: int,
):
    """Event 13417500"""
    ForceAnimation(obj_1, animation_id, loop=True, unknown2=1.0)
    GotoIfObjectDestroyed(Label.L1, obj=obj)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_14.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_14)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterHollow(PLAYER))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj_1, radius=radius))
    OR_1.Add(ObjectDestroyed(obj))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    GotoIfObjectDestroyed(Label.L1, obj=obj)
    ForceAnimation(obj_1, animation_id_1, unknown2=1.0)
    Wait(0.800000011920929)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        dummy_id=210,
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
    ForceAnimation(obj_1, animation_id_2, loop=True, unknown2=1.0)
    OR_3.Add(FramesElapsed(frames=210))
    OR_3.Add(ObjectDestroyed(obj))
    
    MAIN.Await(OR_3)
    
    if ObjectNotDestroyed(obj):
        AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj_1, radius=radius))
        if AND_3:
            return RESTART
    ForceAnimation(obj_1, animation_id_3, wait_for_completion=True, unknown2=1.0)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableFlag(flag)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DestroyObject(obj_1)
    End()


@RestartOnRest(13417600)
def Event_13417600(
    _,
    obj: int,
    obj_1: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    animation_id_3: int,
    radius: float,
    obj_flag: int,
    flag: int,
):
    """Event 13417600"""
    ForceAnimation(obj_1, animation_id, loop=True, unknown2=1.0)
    GotoIfObjectDestroyed(Label.L1, obj=obj)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_14.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_14)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterHollow(PLAYER))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj_1, radius=radius))
    OR_1.Add(ObjectDestroyed(obj))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    GotoIfObjectDestroyed(Label.L1, obj=obj)
    ForceAnimation(obj_1, animation_id_1, unknown2=1.0)
    Wait(0.800000011920929)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        dummy_id=210,
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
    ForceAnimation(obj_1, animation_id_2, loop=True, unknown2=1.0)
    OR_3.Add(FramesElapsed(frames=210))
    OR_3.Add(ObjectDestroyed(obj))
    
    MAIN.Await(OR_3)
    
    if ObjectNotDestroyed(obj):
        AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=obj_1, radius=radius))
        if AND_3:
            return RESTART
    ForceAnimation(obj_1, animation_id_3, wait_for_completion=True, unknown2=1.0)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableFlag(flag)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DestroyObject(obj_1)
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
    AND_1.Add(HealthRatio(3410832) < 0.009999999776482582)
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
        dummy_id=-1,
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


@ContinueOnRest(13410832)
def Event_13410832():
    """Event 13410832"""
    if FlagEnabled(13410830):
        return
    AND_1.Add(HealthRatio(3410831) <= 0.0)
    AND_2.Add(HealthRatio(3410831) <= 0.0)
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
    CommonFunc_20005800(
        0,
        flag=13410830,
        entity=3411830,
        region=3412831,
        flag_1=13415835,
        action_button_id=3411830,
        character=0,
        left=13410831,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=13410830,
        entity=3411830,
        region=3412831,
        flag_1=13415835,
        action_button_id=3411830,
        flag_2=13415836,
    )
    CommonFunc_20005820(0, flag=13410830, obj=3411830, dummy_id=3, left=13410831)
    CommonFunc_20001836(
        0,
        flag=13410830,
        flag_1=13415835,
        flag_2=13415836,
        flag_3=13415830,
        sound_id=3412833,
        sound_id_1=3412834,
        flag_4=13415831,
    )
    CommonFunc_20005840(0, other_entity=3411830)
    CommonFunc_20005841(0, other_entity=3411830)
    CommonFunc_20005810(0, flag=13410830, entity=3411830, target_entity=3412831, action_button_id=10000)


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
        dummy_id=50,
        copy_draw_parent=3410830,
    )
    Restart()


@RestartOnRest(13415843)
def Event_13415843():
    """Event 13415843"""
    if FlagEnabled(13410830):
        return
    EnableImmortality(3410830)
    AND_1.Add(HealthRatio(3410830) < 0.009999999776482582)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(3410830, 11603))
    AND_1.Add(CharacterAlive(3410831))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AND_2.Add(HealthRatio(3410831) <= 0.0)
    if AND_2:
        return
    EnableFlag(73410100)
    ForceAnimation(3410831, 20000, skip_transition=True, unknown2=1.0)
    ForceAnimation(3410830, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Restart()


@ContinueOnRest(13415845)
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


@ContinueOnRest(13415620)
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


@ContinueOnRest(13415640)
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
