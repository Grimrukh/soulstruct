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
    RunCommonEvent(20005500, args=(15000800, 15000000, 5000950, 5001950))
    RegisterBonfire(bonfire_flag=15000001, obj=5001951, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15000002, obj=5001952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15000003, obj=5001953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15000004, obj=5001954, reaction_distance=5.0)
    Event_15005100()
    Event_15005800()
    Event_15005810()
    Event_15005811()
    Event_15005812()
    Event_15005813()
    Event_15005800()
    Event_15005849()
    Event_15005850(0, 5002850, 5003850, 0.5, 1)
    Event_15005850(1, 5002851, 5003851, 0.10000000149011612, 1)
    Event_15005850(2, 5002852, 5003852, 0.0, 1)
    Event_15005850(3, 5002853, 5003853, 0.20000000298023224, 1)
    Event_15005850(4, 5002854, 5003854, 0.0, 1)
    Event_15005850(5, 5002855, 5003855, 0.4000000059604645, 1)
    Event_15005850(6, 5002856, 5003856, 0.5, 1)
    Event_15005850(7, 5002857, 5003857, 0.699999988079071, 1)
    Event_15005850(8, 5002858, 5003858, 0.8999999761581421, 1)
    Event_15005850(9, 5002859, 5003859, 0.800000011920929, 1)
    Event_15005850(10, 5002860, 5003860, 0.10000000149011612, 1)
    Event_15005850(11, 5002861, 5003861, 0.20000000298023224, 1)
    Event_15005850(12, 5002862, 5003862, 0.6000000238418579, 1)
    Event_15005850(13, 5002863, 5003863, 0.9800000190734863, 1)
    Event_15005850(14, 5002864, 5003864, 0.5, 1)
    Event_15005850(15, 5002865, 5003865, 0.6000000238418579, 1)
    Event_15005850(16, 5002866, 5003866, 0.699999988079071, 1)
    Event_15005850(17, 5002867, 5003867, 0.6899999976158142, 1)
    Event_15005850(18, 5002868, 5003868, 0.20000000298023224, 1)
    Event_15005850(19, 5002869, 5003869, 0.4000000059604645, 1)
    Event_15005850(20, 5002870, 5003870, 0.30000001192092896, 1)
    Event_15005850(21, 5002871, 5003871, 1.0, 1)
    Event_15005850(22, 5002872, 5003872, 0.0, 1)
    Event_15005850(23, 5002873, 5003873, 0.8999999761581421, 1)
    Event_15005220(
        0,
        character=5000200,
        flag=15005230,
        flag_1=15005215,
        character_1=5000210,
        special_effect_id=16620,
        special_effect_id_1=16640
    )
    RunCommonEvent(20005203, args=(5000200, 30000, 20000, 5002200, 5002201, 5002202, 0, 0, 0))
    Event_15005210(0, character=5000210, special_effect=16256, character_1=5004200, character_2=5000200, flag=15005215)
    Event_15005250(0, character=5000210, character_1=5000200)
    Event_15005260()
    Event_15005270(0, character=5000200)
    Event_15005290(0, character=5000200)
    Event_15005285(0, flag=15000235, character=5000200, character_1=5000210)
    DisableFlag(15005215)
    Event_15005261()
    Event_15005220(
        1,
        character=5000201,
        flag=15005231,
        flag_1=15005216,
        character_1=5000211,
        special_effect_id=16621,
        special_effect_id_1=16641
    )
    Event_15005240(0, character=5000201, region=5002228, special_effect_id=16255)
    Event_15005210(1, character=5000211, special_effect=16256, character_1=5004201, character_2=5000201, flag=15005216)
    Event_15005250(1, character=5000211, character_1=5000201)
    Event_15005270(1, character=5000201)
    Event_15005266(
        1,
        character=5000211,
        animation_id=20001,
        region=5002220,
        region_1=5002221,
        region_2=5002222,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0
    )
    Event_15005280(0, character=5000201, animation_id=30000, animation_id_1=20000)
    Event_15005290(1, character=5000201)
    Event_15005285(1, flag=15000236, character=5000201, character_1=5000211)
    DisableFlag(15005216)
    Event_15005265(
        0,
        character=5000212,
        animation_id=20000,
        region=5002240,
        region_1=5002241,
        region_2=5002242,
        region_3=5002243,
        region_4=0,
        region_5=0,
        region_6=0
    )
    Event_15005220(
        2,
        character=5000202,
        flag=15005232,
        flag_1=15005217,
        character_1=5000212,
        special_effect_id=16622,
        special_effect_id_1=16642
    )
    Event_15005210(2, character=5000212, special_effect=16256, character_1=5004202, character_2=5000202, flag=15005217)
    Event_15005250(2, character=5000212, character_1=5000202)
    Event_15005270(2, character=5000202)
    Event_15005290(2, character=5000202)
    Event_15005285(2, flag=15000237, character=5000202, character_1=5000212)
    Event_15005460(1, 5000223, 700, 1700, 5002401, 5000222, 16005, 0.30000001192092896, 5000220)
    RunCommonEvent(20005132, args=(5000222, 5.0, 5002400), arg_types="ifi")
    RunCommonEvent(20005210, args=(5000224, 700, 1700, 12.0), arg_types="iiif")
    RunCommonEvent(20005132, args=(5000226, 5.0, 5002402), arg_types="ifi")
    RunCommonEvent(20005206, args=(5000232, 701, 1701, 5002250, 5002251, 5002252, 0, 0, 0))
    RunCommonEvent(20005203, args=(5000233, 701, 1701, 2, 5002253, 5002254, 0, 0, 0))
    RunCommonEvent(20005213, args=(5000236, 700, 1700, 6.0, 5002256), arg_types="iiifi")
    RunCommonEvent(20005213, args=(5000237, 701, 1701, 5.0, 5002257), arg_types="iiifi")
    Event_15005470()
    RunCommonEvent(20005213, args=(5000300, 700, 1700, 2.0, 5002301), arg_types="iiifi")
    RunCommonEvent(20005219, args=(5000301, 700, 1700, 2.0, 5002302, 3.0), arg_types="iiifif")
    RunCommonEvent(20005243, args=(5000400, 700, 1700, 5000300, 16220, 6.5), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000401, 700, 1700, 5000300, 16220, 7.199999809265137), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000402, 700, 1700, 5000300, 16220, 3.9000000953674316), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000403, 700, 1700, 5000300, 16220, 5.800000190734863), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000404, 700, 1700, 5000300, 16220, 4.400000095367432), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000405, 700, 1700, 5000300, 16220, 1.899999976158142), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000406, 700, 1700, 5000300, 16220, 0.800000011920929), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000407, 700, 1700, 5000300, 16220, 0.0), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000408, 700, 1700, 5000300, 16220, 3.799999952316284), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000409, 700, 1700, 5000300, 16220, 2.5), arg_types="iiiiif")
    RunCommonEvent(20005243, args=(5000410, 700, 1700, 5000300, 16220, 1.0), arg_types="iiiiif")
    RunCommonEvent(20005212, args=(5000310, 700, 1700, 5.0, 5002315), arg_types="iiifi")
    RunCommonEvent(20005212, args=(5000311, 700, 1700, 20.0, 5002315), arg_types="iiifi")
    RunCommonEvent(20005219, args=(5000315, 700, 1700, 3.0, 5002317, 1.0), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000420, 700, 1700, 2.0, 5002310, 0.0), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000421, 701, 1701, 1.0, 5002316, 0.0), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000422, 702, 20000, 2.0, 5002311, 0.10000000149011612), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000423, 701, 1701, 2.0, 5002312, 0.0), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000424, 702, 20000, 2.0, 5002312, 0.30000001192092896), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000425, 702, 20000, 2.0, 5002314, 0.0), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000426, 700, 1700, 2.0, 5002312, 0.800000011920929), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000427, 701, 1701, 1.0, 5002318, 1.5), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000428, 700, 1700, 1.0, 5002319, 0.5), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000316, 700, 1700, 2.0, 5002320, 1.2999999523162842), arg_types="iiifif")
    RunCommonEvent(20005219, args=(5000317, 700, 1700, 2.0, 5002320, 0.0), arg_types="iiifif")
    Event_15005410(0, 5000319, 700, 1700, 5002322, 15005392, 0.10000000149011612)
    RunCommonEvent(20005205, args=(5000448, 701, 1701, 5002328, 0.10000000149011612), arg_types="iiiif")
    RunCommonEvent(20005132, args=(5000449, 3.0, 5002329), arg_types="ifi")
    RunCommonEvent(20005205, args=(5000331, 700, 1700, 5002332, 5.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(5000456, 702, 20000, 5002332, 9.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(5000457, 702, 20000, 5002334, 0.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(5000458, 700, 1700, 5002333, 2.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(5000459, 701, 1701, 5002335, 5.0), arg_types="iiiif")
    RunCommonEvent(20005219, args=(5000335, 700, 1700, 2.0, 5002340, 0.0), arg_types="iiifif")
    RunCommonEvent(20005201, args=(5000460, 700, 1700, 5002340, 3.0), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000461, 700, 1700, 5002340, 1.2000000476837158), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000462, 700, 1700, 5002340, 1.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000463, 700, 1700, 5002340, 5.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000464, 700, 1700, 5002340, 5.800000190734863), arg_types="iiiif")
    Event_15005400(0, 5000335, 5000460, 5003340, 5000520, 5003345, 0.0)
    Event_15005400(1, 5000335, 5000461, 5003341, 5000521, 5003346, 0.10000000149011612)
    Event_15005400(2, 5000335, 5000462, 5003342, 5000522, 5003347, 0.30000001192092896)
    RunCommonEvent(20005201, args=(5000337, 700, 1700, 5002356, 0.0), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000475, 700, 1700, 5002355, 3.0), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000476, 700, 1700, 5002355, 3.700000047683716), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000477, 700, 1700, 5002355, 3.799999952316284), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000478, 700, 1700, 5002355, 5.0), arg_types="iiiif")
    RunCommonEvent(20005201, args=(5000479, 700, 1700, 5002355, 5.5), arg_types="iiiif")
    Event_15005340(0, character=5000316, character_1=5000500)
    Event_15005340(1, character=5000319, character_1=5000503)
    Event_15005340(2, character=5000315, character_1=5000501)
    Event_15005340(3, character=5000426, character_1=5000502)
    Event_15005340(4, character=5000337, character_1=5000530)
    Event_15005340(7, character=5000454, character_1=5000506)
    Event_15005340(8, character=5000455, character_1=5000507)
    Event_15005340(9, character=5000457, character_1=5000508)
    Event_15005340(10, character=5000458, character_1=5000509)
    Event_15005340(11, character=5000463, character_1=5000523)
    Event_15005340(12, character=5000464, character_1=5000524)
    Event_15005360(0, character=5000460, character_1=5000520)
    Event_15005360(1, character=5000461, character_1=5000521)
    Event_15005360(2, character=5000462, character_1=5000522)
    Event_15005340(13, character=5000463, character_1=5000523)
    Event_15005340(14, character=5000464, character_1=5000524)
    Event_15005365(0, character=5000520)
    Event_15005365(1, character=5000521)
    Event_15005365(2, character=5000522)
    Event_15005310(12, character=5000335, character_1=5000460)
    Event_15005310(13, character=5000335, character_1=5000461)
    Event_15005310(14, character=5000335, character_1=5000462)
    Event_15005310(15, character=5000336, character_1=5000463)
    Event_15005310(16, character=5000336, character_1=5000464)
    Event_15005390(0, character=5000324, region=5002325, entity=5003320)
    Event_15005390(1, character=5000324, region=5002326, entity=5003321)
    Event_15005390(2, character=5000324, region=5002327, entity=5003322)
    Event_15005390(3, character=5000324, region=5002342, entity=5003323)
    Event_15005390(4, character=5000324, region=5002343, entity=5003324)
    Event_15005390(5, character=5000332, region=5002350, entity=5003350)
    Event_15005390(6, character=5000332, region=5002350, entity=5003351)
    RunCommonEvent(20005114, args=(5000270, 5002270, 1.0), arg_types="iif")
    RunCommonEvent(20005114, args=(5000271, 5002270, 1.5), arg_types="iif")
    RunCommonEvent(20005120, args=(5000272, 12.0), arg_types="if")
    RunCommonEvent(20005331, args=(5000270,))
    RunCommonEvent(20005331, args=(5000271,))
    RunCommonEvent(20005331, args=(5000272,))
    Event_15005444()
    Event_15005447()
    Event_15005448(1, 5000273, 701, 1701, 5002272, 0.5)
    Event_15005448(2, 5000274, 701, 1701, 5002272, 0.0)
    Event_15005448(3, 5000275, 700, 1700, 5002271, 2.0)
    RunCommonEvent(20005132, args=(5000275, 3.0, 5002274), arg_types="ifi")
    RunCommonEvent(20005132, args=(5000279, 3.0, 5002276), arg_types="ifi")
    RunCommonEvent(20005132, args=(5000280, 3.0, 5002277), arg_types="ifi")
    RunCommonEvent(20005132, args=(5000281, 3.0, 5002277), arg_types="ifi")
    RunCommonEvent(20005205, args=(5000283, 701, 1701, 5002279, 0.5), arg_types="iiiif")
    RunCommonEvent(20005205, args=(5000284, 701, 1701, 5002280, 0.5), arg_types="iiiif")
    RunCommonEvent(20005134, args=(5000285, 3006, 3.0, 5002281), arg_types="iifi")
    RunCommonEvent(20005205, args=(5000286, 701, 1701, 5002282, 4.0), arg_types="iiiif")
    RunCommonEvent(20005132, args=(5000287, 5.0, 5002286), arg_types="ifi")
    RunCommonEvent(20005132, args=(5000288, 5.0, 5002286), arg_types="ifi")
    Event_15005440(0, character=5000288, attacker=5000200, region=5002287, region_1=5000287)
    Event_15005500()
    Event_15005502()
    Event_15005510()
    Event_15005520(0, region=5002520, obj=5001520)
    Event_15005520(1, region=5002521, obj=5001521)
    Event_15005530(0, region=5002530)
    Event_15005530(1, region=5002531)
    Event_15005530(2, region=5002532)
    Event_15005530(3, region=5002533)
    Event_15005530(4, region=5002534)
    Event_15005550(0, region=5002550)
    RunEvent(20005640, slot=0, args=(15000580, 5001580, 15000581, 15000582))
    Event_15005590()
    RunCommonEvent(20005650, args=(15000560, 5001560))
    Event_15005120(0, flag=15000120, character=5000120)
    Event_15005120(1, flag=15000121, character=5000121)
    Event_15005120(2, flag=15000122, character=5000122)
    Event_15005120(3, flag=15000123, character=5000123)
    Event_15005120(4, flag=15000124, character=5000124)
    Event_15005120(5, flag=15000125, character=5000125)
    Event_15005120(6, flag=15000126, character=5000126)
    Event_15005120(7, flag=15000127, character=5000127)
    RunCommonEvent(20005701, args=(15000800, 15004170, 15005170, 5000170, 5002170, 70000030))
    RunCommonEvent(20005720, args=(15004170, 15005170, 15000800, 5000170))
    RunCommonEvent(20005716, args=(15004170, 15005805, 5000170, 5002801, 5002805, 15005801))
    RunCommonEvent(20005715, args=(15004170, 15005805, 5000170, 5002806, 15005801, 5002807, 0))
    Event_15005540(0, region=5002534, character=5000170)
    RunCommonEvent(20005701, args=(15000800, 15004174, 15005174, 5000174, 5002174, 0))
    RunCommonEvent(20005720, args=(15004174, 15005174, 15000800, 5000174))
    RunCommonEvent(20005716, args=(15004174, 15005805, 5000174, 5002801, 5002805, 15005801))
    RunCommonEvent(20005715, args=(15004174, 15005805, 5000174, 5002806, 15005801, 5002807, 0))
    Event_15005540(1, region=5002534, character=5000174)
    RunCommonEvent(20005342, args=(15000180, 5000180))
    RunCommonEvent(20005132, args=(5000180, 6.0, 5002270), arg_types="ifi")
    Event_15005480(0, 5000190, 6.0, 5002270, 5000180, 15000180, 5005190)
    RunCommonEvent(20006002, args=(5000700, 1818, 1815, 1819))
    RunCommonEvent(20006002, args=(5000701, 1818, 1815, 1819))
    RunCommonEvent(20006002, args=(5000702, 1818, 1815, 1819))
    RunCommonEvent(
        20006000,
        args=(5000700, 1816, 1817, 75000140, 0.6499999761581421, 1815, 1819, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(
        20006000,
        args=(5000701, 1816, 1817, 75000141, 0.6499999761581421, 1815, 1819, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(
        20006000,
        args=(5000702, 1816, 1817, 75000142, 0.6499999761581421, 1815, 1819, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(5000700, 1816, 1817, 75000140, 3))
    RunCommonEvent(20006001, args=(5000701, 1816, 1817, 75000141, 3))
    RunCommonEvent(20006001, args=(5000702, 1816, 1817, 75000142, 3))
    RunCommonEvent(20006030, args=(5001700, 4000, 0, 66200, 50006620, 50006620, 75000135))
    Event_15005702(0, character=5000701, character_1=5000170, flag=1801, flag_1=1803)
    Event_15005702(1, character=5000702, character_1=5000170, flag=1802, flag_1=1804)
    RunCommonEvent(20006002, args=(5000705, 1878, 1875, 1879))
    RunCommonEvent(20006040, args=(5000705, 5002705, 5450))
    Event_15005721(0, 5000705, 5001705)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_15005200(0, character=5000200, region=5002200, region_1=0, region_2=0)
    Event_15005200(1, character=5000201, region=5002220, region_1=5002221, region_2=5002222)
    Event_15005200(2, character=5000202, region=5002240, region_1=5002241, region_2=5002242)
    Event_15005570()
    Event_15005575()
    DisableSoundEvent(sound_id=5004801)
    DisableSoundEvent(sound_id=5004802)
    Event_15005700(
        0,
        character=5000700,
        character_1=5000701,
        character_2=5000702,
        animation_id=91180,
        animation_id_1=91180,
        animation_id_2=91170
    )
    Event_15005701(0, obj=5001345, character=5000230, obj_1=5001230)
    Event_15005720(0, character=5000705, animation_id=30004, command_id=2160, obj=5001705, destination=5002705)
    Event_15005722(0, 5000203)


@RestartOnRest(15005100)
def Event_15005100():
    """Event 15005100"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(15000800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9380, entity=5001100))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerHasGood(2156))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    DisplayDialog(text=10012800)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetRespawnPoint(respawn_point=5102110)
    SaveRequest()
    PlayCutscene(51000000, cutscene_flags=0, player_id=10000, move_to_region=5102110, game_map=RINGED_CITY)
    WaitFrames(frames=1)
    Restart()


@NeverRestart(15005120)
def Event_15005120(_, flag: int, character: int):
    """Event 15005120"""
    AddSpecialEffect(character, 17500)
    DisableAI(character)
    DisableAnimations(character)
    ForceAnimation(character, 91230, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(flag)
    End()


@RestartOnRest(15005200)
def Event_15005200(_, character: int, region: int, region_1: int, region_2: int):
    """Event 15005200"""
    DisableGravity(character)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(15005210)
def Event_15005210(_, character: int, special_effect: int, character_1: int, character_2: int, flag: int):
    """Event 15005210"""
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_1)
    DisableFlag(flag)
    WaitFrames(frames=1)
    ReplanAI(character_2)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableGravity(character_2)
    Restart()


@RestartOnRest(15005220)
def Event_15005220(
    _,
    character: int,
    flag: int,
    flag_1: int,
    character_1: int,
    special_effect_id: int,
    special_effect_id_1: int,
):
    """Event 15005220"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AND_2.Add(CharacterDead(character))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=3,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    AddSpecialEffect(character_1, special_effect_id)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_3.Add(CharacterAlive(character))
    AND_3.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_3)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AddSpecialEffect(character_1, special_effect_id_1)
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(15005240)
def Event_15005240(_, character: int, region: int, special_effect_id: int):
    """Event 15005240"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect_id)
    SetCharacterEventTarget(character, region=PLAYER)
    Wait(3.0)
    Restart()


@RestartOnRest(15005250)
def Event_15005250(_, character: int, character_1: int):
    """Event 15005250"""
    MAIN.Await(CharacterDead(character))
    
    AddSpecialEffect(character_1, 16258)


@RestartOnRest(15005260)
def Event_15005260():
    """Event 15005260"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5002202))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5002221))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterHasSpecialEffect(5000200, 16259))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    CancelSpecialEffect(5000200, 16259)
    Restart()


@RestartOnRest(15005261)
def Event_15005261():
    """Event 15005261"""
    AND_15.Add(CharacterDead(5000287))
    if AND_15:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002286))
    
    MAIN.Await(AND_1)
    
    Wait(2.9000000953674316)
    AddSpecialEffect(5000200, 16611)
    SetCharacterEventTarget(5000200, region=5000287)
    
    MAIN.Await(CharacterDead(5000287))
    
    CancelSpecialEffect(5000200, 16611)


@RestartOnRest(15005265)
def Event_15005265(
    _,
    character: int,
    animation_id: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
    region_5: int,
    region_6: int,
):
    """Event 15005265"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    EnableFlag(15005217)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    if ValueNotEqual(left=region_5, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    if ValueNotEqual(left=region_6, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_6))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    ForceAnimation(character, animation_id, skip_transition=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(15005266)
def Event_15005266(
    _,
    character: int,
    animation_id: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
    region_5: int,
    region_6: int,
):
    """Event 15005266"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    if ValueNotEqual(left=region_5, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    if ValueNotEqual(left=region_6, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_6))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    ForceAnimation(character, animation_id, skip_transition=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(15005270)
def Event_15005270(_, character: int):
    """Event 15005270"""
    AND_1.Add(PlayerNotInOwnWorld())
    if AND_1:
        return
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    
    MAIN.Await(CharacterDead(character))
    
    Restart()


@RestartOnRest(15005280)
def Event_15005280(_, character: int, animation_id: int, animation_id_1: int):
    """Event 15005280"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_1.Add(CharacterHasSpecialEffect(5000211, 16610))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    AND_8.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    GotoIfConditionTrue(Label.L1, input_condition=AND_8)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20002, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(15005285)
def Event_15005285(_, flag: int, character: int, character_1: int):
    """Event 15005285"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAnimations(character)
    DisableAnimations(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character_1))
    
    EnableFlag(flag)


@RestartOnRest(15005290)
def Event_15005290(_, character: int):
    """Event 15005290"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5031))
    
    ClearTargetList(character)
    Restart()


@RestartOnRest(15005300)
def Event_15005300(_, character: int, character_1: int, character_2: int):
    """Event 15005300"""
    CancelSpecialEffect(character, 16240)
    if ThisEventSlotFlagEnabled():
        AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 16240))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_2)
    WaitFrames(frames=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=8,
        copy_draw_parent=character,
    )
    Restart()


@RestartOnRest(15005310)
def Event_15005310(_, character: int, character_1: int):
    """Event 15005310"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 16245))
    AND_1.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterAlive(character_1))
    if AND_2:
        return RESTART
    AddSpecialEffect(character, 16245)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(15005340)
def Event_15005340(_, character: int, character_1: int):
    """Event 15005340"""
    AND_1.Add(CharacterDead(character_1))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableCharacter(character_1)
    DisableAI(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagDisabled(Label.L1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16247))
    
    EnableCharacter(character_1)
    EnableAI(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=character,
    )
    WaitFrames(frames=1)
    ReplanAI(character_1)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16249))
    
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@RestartOnRest(15005360)
def Event_15005360(_, character: int, character_1: int):
    """Event 15005360"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(character_1)
        DisableAnimations(character_1)
    DisableAI(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, 16247))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    EnableAI(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=character,
    )
    WaitFrames(frames=1)
    ReplanAI(character_1)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    CancelSpecialEffect(character, 16247)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16249))
    
    Move(character, destination=5002390, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Kill(character)
    Wait(1.0)
    Restart()


@RestartOnRest(15005365)
def Event_15005365(_, character: int):
    """Event 15005365"""
    AND_1.Add(HealthValueGreaterThanOrEqual(character, value=1))
    AND_1.Add(CharacterHasSpecialEffect(character, 16901))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    Kill(character)
    Wait(1.0)
    Restart()


@RestartOnRest(15005370)
def Event_15005370(_, character: int, character_1: int, special_effect: int):
    """Event 15005370"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 16229)
    AND_1.Add(CharacterHasSpecialEffect(character_1, special_effect))
    
    MAIN.Await(AND_1)
    
    CancelSpecialEffect(character, 16229)


@RestartOnRest(15005380)
def Event_15005380(_, character: int, character_1: int):
    """Event 15005380"""
    CancelSpecialEffect(character, 16240)
    AND_1.Add(CharacterHasSpecialEffect(character, 16240))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_1)
    Wait(1.0)
    Restart()


@RestartOnRest(15005390)
def Event_15005390(_, character: int, region: int, entity: int):
    """Event 15005390"""
    DisableSpawner(entity=entity)
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    EnableSpawner(entity=entity)
    Wait(0.20000000298023224)
    AND_3.Add(AllPlayersOutsideRegion(region=region))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterDead(character))
    
    MAIN.Await(OR_3)
    
    Restart()


@RestartOnRest(15005400)
def Event_15005400(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    seconds: float,
):
    """Event 15005400"""
    CancelSpecialEffect(character, 16240)
    if ThisEventSlotFlagEnabled():
        AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 16240))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    AND_3.Add(CharacterAlive(character_1))
    SkipLinesIfConditionTrue(1, AND_3)
    MakeEnemyAppear(character=character_2)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    AND_2.Add(CharacterAlive(character_3))
    SkipLinesIfConditionTrue(1, AND_2)
    MakeEnemyAppear(character=character_4)
    WaitFrames(frames=1)
    DisableAI(character_3)
    DisableCharacter(character_3)
    DisableAnimations(character_3)
    Wait(1.0)
    Restart()


@RestartOnRest(15005410)
def Event_15005410(_, character: int, animation_id: int, animation_id_1: int, region: int, flag: int, seconds: float):
    """Event 15005410"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(FlagEnabled(flag))
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()


@RestartOnRest(15005440)
def Event_15005440(_, character: int, attacker: int, region: int, region_1: int):
    """Event 15005440"""
    SkipLinesIfFlagEnabled(1, 0)
    SkipLinesIfValueEqual(1, left=0, right=region_1)
    OR_1.Add(Attacked(attacked_entity=region_1, attacker=attacker))
    OR_1.Add(Attacked(attacked_entity=character, attacker=attacker))
    OR_1.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_1)
    
    AND_2.Add(CharacterInsideRegion(character=character, region=region))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AddSpecialEffect(character, 5000)
    OR_3.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(OR_3)

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(character, 5000)


@RestartOnRest(15005444)
def Event_15005444():
    """Event 15005444"""
    GotoIfPlayerInOwnWorld(Label.L9)
    GotoIfFlagEnabled(Label.L0, flag=15005445)
    Goto(Label.L1)

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagDisabled(Label.L0, flag=15000180)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(5000290)
    DisableAnimations(5000290)
    DisableCharacter(5000291)
    DisableAnimations(5000291)
    DisableCharacter(5000292)
    DisableAnimations(5000292)
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=15005445, state=FlagSetting.On)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(5000270)
    DisableAnimations(5000270)
    DisableCharacter(5000271)
    DisableAnimations(5000271)
    DisableCharacter(5000272)
    DisableAnimations(5000272)
    End()


@RestartOnRest(15005447)
def Event_15005447():
    """Event 15005447"""
    if FlagEnabled(15000180):
        return
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(5000272, 16805)
    
    MAIN.Await(EntityWithinDistance(entity=5000272, other_entity=5000180, radius=5.0))
    
    CancelSpecialEffect(5000272, 16805)


@RestartOnRest(15005448)
def Event_15005448(_, character: int, animation_id: int, animation_id_1: int, region: int, seconds: float):
    """Event 15005448"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    Wait(seconds)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(15005460)
def Event_15005460(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    region: int,
    attacked_entity: int,
    special_effect: int,
    seconds: float,
    attacked_entity_1: int,
):
    """Event 15005460"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, unknown2=1.0)
    DisableGravity(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=special_effect)
    Wait(0.5)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    Wait(seconds)
    EnableGravity(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()


@RestartOnRest(15005470)
def Event_15005470():
    """Event 15005470"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(character=5000236, region=5002260))
    
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=5002261))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000236, radius=3.0))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(5000236, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(5000236, 3011, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(5000236, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(15005480)
def Event_15005480(_, character: int, radius: float, region: int, region_1: int, flag: int, character_1: int):
    """Event 15005480"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(AND_1)
    AND_3.Add(OR_3)
    AND_3.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    if ValueNotEqual(left=0, right=0):
        AddSpecialEffect(character_1, 5000)
    AICommand(character, command_id=100, command_slot=0)
    SetCharacterEventTarget(character, region=region_1)


@RestartOnRest(15005500)
def Event_15005500():
    """Event 15005500"""
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=False)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=False)
    GotoIfFlagDisabled(Label.L0, flag=15000500)
    EndOfAnimation(obj=5001500, animation_id=2)
    DisableObject(5001501)
    DisableObject(5001502)
    DisableObject(5001503)
    EnableObject(5001504)
    CreateVFX(5003500)
    CreateVFX(5003501)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=True)
    DisableObject(5001504)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5002500))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5002501))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(15000500)
    EnableFlag(15005500)
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=False)
    ForceAnimation(5001500, 1, unknown2=1.0)
    Wait(1.5)
    CreateHazard(
        obj_flag=15005500,
        obj=5001500,
        model_point=40,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(1.7000000476837158)
    CreateHazard(
        obj_flag=15005501,
        obj=5001500,
        model_point=41,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.5,
        repetition_time=0.0,
    )
    DestroyObject_NoSlot(obj=5001501)
    DestroyObject_NoSlot(obj=5001502)
    DestroyObject_NoSlot(obj=5001503)
    EnableObject(5001504)
    CreateVFX(5003500)
    CreateVFX(5003501)
    Wait(0.5)
    RemoveObjectFlag(obj_flag=15005500)
    RemoveObjectFlag(obj_flag=15005501)
    Wait(2.200000047683716)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=True)


@RestartOnRest(15005502)
def Event_15005502():
    """Event 15005502"""
    DisableNetworkSync()
    if FlagEnabled(15000500):
        return
    
    MAIN.Await(FlagEnabled(15000500))
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002502))
    if not AND_1:
        return
    Wait(0.4000000059604645)
    SetCameraVibration(vibration_id=105, anchor_entity=5002502, anchor_type=CoordEntityType.Region)
    Wait(1.600000023841858)
    SetCameraVibration(vibration_id=105, anchor_entity=5002502, anchor_type=CoordEntityType.Region)
    Wait(1.600000023841858)
    SetCameraVibration(vibration_id=104, anchor_entity=5002502, anchor_type=CoordEntityType.Region)


@RestartOnRest(15005510)
def Event_15005510():
    """Event 15005510"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(5001301, 310, loop=True, skip_transition=True, unknown2=1.0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=5002510))
    
    DestroyObject_NoSlot(obj=5001510)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    ForceAnimation(5001301, 311, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(5001301, 312, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(5001510)
    ForceAnimation(5001301, 312, loop=True, skip_transition=True, unknown2=1.0)


@RestartOnRest(15005520)
def Event_15005520(_, region: int, obj: int):
    """Event 15005520"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    DestroyObject_NoSlot(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)


@RestartOnRest(15005530)
def Event_15005530(_, region: int):
    """Event 15005530"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4050)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    CancelSpecialEffect(PLAYER, 4050)
    Restart()


@RestartOnRest(15005540)
def Event_15005540(_, region: int, character: int):
    """Event 15005540"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4050)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    CancelSpecialEffect(character, 4050)
    Restart()


@RestartOnRest(15005550)
def Event_15005550(_, region: int):
    """Event 15005550"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4070)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    CancelSpecialEffect(PLAYER, 4070)
    Restart()


@RestartOnRest(15005570)
def Event_15005570():
    """Event 15005570"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(5001510)
    RestoreObject(5001520)
    RestoreObject(5001521)


@RestartOnRest(15005575)
def Event_15005575():
    """Event 15005575"""
    EnableObjectInvulnerability(5001411)


@RestartOnRest(15005580)
def Event_15005580():
    """Event 15005580"""
    RegisterLadder(start_climbing_flag=15001580, stop_climbing_flag=15001581, obj=5001580)


@RestartOnRest(15005590)
def Event_15005590():
    """Event 15005590"""
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002590))
    AND_1.Add(FlagDisabled(15000590))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetAreaWelcomeMessageState(state=False)
    EnableFlag(15000590)


@RestartOnRest(15005800)
def Event_15005800():
    """Event 15005800"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(FlagEnabled(15005803))
    AND_1.Add(HealthRatioLessThanOrEqual(5000801, value=0.0))
    AND_2.Add(FlagEnabled(15005804))
    AND_2.Add(HealthRatioLessThanOrEqual(5000802, value=0.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    Wait(3.0)
    PlaySoundEffect(5000801, 777777777, sound_type=SoundType.s_SFX)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5000801, banner=BannerType.HeirOfFireDestroyed)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(5005803)
    Wait(3.0)
    PlaySoundEffect(5000802, 777777777, sound_type=SoundType.s_SFX)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5000802, banner=BannerType.HeirOfFireDestroyed)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(15000800)
    EnableFlag(9324)
    EnableFlag(6324)


@RestartOnRest(15005810)
def Event_15005810():
    """Event 15005810"""
    GotoIfFlagDisabled(Label.L0, flag=15000800)
    DisableCharacter(5005800)
    DisableAnimations(5005800)
    Kill(5005800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableImmortality(5000800)
    DisableHealthBar(5000800)
    SetLockOnPoint(character=5000800, lock_on_model_point=220, state=False)
    DisableAI(5005800)
    EnableImmortality(5000801)
    DisableAI(5005801)
    DisableHealthBar(5000801)
    SetCollisionMask(5000801, bit_index=1, switch_type=OnOffChange.Off)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    if OR_15:
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002800))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=5000801))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_9.Add(FlagEnabled(15005805))
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=5002800))
    
    MAIN.Await(AND_9)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    SetNetworkUpdateRate(5005801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(5000801, target_entity=5000800)
    Wait(0.30000001192092896)
    EnableAI(5005801)
    if FlagDisabled(15005810):
        Wait(3.0)
    EnableBossHealthBar(5000801, name=905020)
    EnableBossHealthBar(5000802, name=905021, bar_slot=1)
    EnableFlag(15005810)
    SetNetworkConnectedFlagState(flag=15005801, state=FlagSetting.On)
    if PlayerNotInOwnWorld():
        return
    Wait(0.0)
    SetNetworkConnectedFlagState(flag=15005809, state=FlagSetting.On)


@RestartOnRest(15005811)
def Event_15005811():
    """Event 15005811"""
    if FlagEnabled(15000800):
        return
    EnableImmortality(5000802)
    DisableAI(5005802)
    DisableHealthBar(5000802)
    SetCollisionMask(5000802, bit_index=1, switch_type=OnOffChange.Off)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(15005809))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(15005811))
    OR_1.Add(AttackedWithDamageType(attacked_entity=5000802))
    OR_1.Add(HealthRatioLessThanOrEqual(5000801, value=0.6499999761581421))
    OR_1.Add(CharacterHasSpecialEffect(5000801, 15025))
    
    MAIN.Await(OR_1)
    
    EnableAI(5005802)
    SetNetworkUpdateRate(5005802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.0)
    EnableBossHealthBar(5000802, name=905021, bar_slot=1)


@RestartOnRest(15005812)
def Event_15005812():
    """Event 15005812"""
    if FlagEnabled(15000800):
        return
    AND_2.Add(CharacterHasSpecialEffect(5000801, 15202))
    AND_3.Add(CharacterHasSpecialEffect(5000802, 15202))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_3)
    SetNetworkConnectedFlagState(flag=15005803, state=FlagSetting.On)
    Wait(6.0)
    DisableBossHealthBar(5000802, name=905023, bar_slot=1)
    Wait(12.0)
    EnableBossHealthBar(5000801, name=905022)
    DisableImmortality(5000801)
    SetCollisionMask(5000801, bit_index=1, switch_type=OnOffChange.On)
    GotoIfPlayerNotInOwnWorld(Label.L11)
    AND_11.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.GreaterThanOrEqual, value=2))
    GotoIfConditionTrue(Label.L11, input_condition=AND_11)
    AddSpecialEffect(5000801, 15150)

    # --- Label 11 --- #
    DefineLabel(11)
    DisableCharacter(5000802)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=15005804, state=FlagSetting.On)
    Wait(6.0)
    DisableBossHealthBar(5000801, name=905022)
    Wait(12.0)
    EnableBossHealthBar(5000802, name=905023)
    DisableImmortality(5000802)
    SetCollisionMask(5000802, bit_index=1, switch_type=OnOffChange.On)
    GotoIfPlayerNotInOwnWorld(Label.L12)
    AND_12.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.GreaterThanOrEqual, value=2))
    GotoIfConditionTrue(Label.L12, input_condition=AND_12)
    AddSpecialEffect(5000802, 15150)

    # --- Label 12 --- #
    DefineLabel(12)
    DisableCharacter(5000801)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    SetNetworkConnectedFlagState(flag=15005802, state=FlagSetting.On)


@RestartOnRest(15005813)
def Event_15005813():
    """Event 15005813"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(HealthValueEqual(5000801, value=1))
    AND_2.Add(HealthValueEqual(5000802, value=1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    AddSpecialEffect(5000801, 15100)
    AddSpecialEffect(5000801, 15204)
    AddSpecialEffect(5000802, 15204)
    AddSpecialEffect(5000802, 15201)
    Wait(3.0)
    CancelSpecialEffect(5000801, 15040)
    CancelSpecialEffect(5000801, 15026)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(5000802, 15100)
    AddSpecialEffect(5000802, 15204)
    AddSpecialEffect(5000801, 15204)
    AddSpecialEffect(5000801, 15201)
    Wait(3.0)
    CancelSpecialEffect(5000802, 15040)
    CancelSpecialEffect(5000802, 15026)


@RestartOnRest(15005820)
def Event_15005820(_, character: int, character_1: int, flag: int):
    """Event 15005820"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(15000800):
        return
    if FlagEnabled(15005803):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterDead(character_1))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(15005825)
def Event_15005825(
    _,
    character__region: int,
    character: int,
    flag: int,
    special_effect: int,
    character_1: int,
    model_point: int,
    right: int,
):
    """Event 15005825"""
    if FlagEnabled(15000800):
        return
    if FlagEnabled(15005803):
        return
    DisableGravity(character)
    AND_1.Add(CharacterHasSpecialEffect(character__region, special_effect))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_1)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=character__region,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    ReplanAI(character)
    if ValueEqual(left=1, right=right):
        SetCharacterEventTarget(character, region=character__region)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(15005830)
def Event_15005830(_, character: int):
    """Event 15005830"""
    if FlagEnabled(15000800):
        return
    DisableNetworkSync()
    OR_5.Add(HealthValueLessThanOrEqual(5000801, value=0))
    OR_5.Add(HealthValueLessThanOrEqual(5000802, value=0))
    GotoIfConditionTrue(Label.L9, input_condition=OR_5)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=18.0))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=18.0))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 15041)
    OR_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=18.0))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 15040)
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=18.0))
    
    MAIN.Await(OR_2)
    
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    AND_10.Add(CharacterHasSpecialEffect(character, 15042))
    SkipLinesIfConditionTrue(1, AND_10)
    AddSpecialEffect(character, 15040)
    Wait(0.20000000298023224)
    End()


@RestartOnRest(15005835)
def Event_15005835():
    """Event 15005835"""
    if FlagEnabled(15000800):
        return
    DisableNetworkSync()
    AND_13.Add(CharacterInsideRegion(character=PLAYER, region=5002800))
    AND_13.Add(FlagEnabled(15005810))
    
    MAIN.Await(AND_13)
    
    AND_14.Add(FlagEnabled(15005803))
    AND_14.Add(CharacterDead(5000801))
    AND_15.Add(FlagEnabled(15005804))
    AND_15.Add(CharacterDead(5000802))
    OR_15.Add(AND_14)
    OR_15.Add(AND_15)
    GotoIfConditionTrue(Label.L20, input_condition=OR_15)
    AND_5.Add(CharacterHasSpecialEffect(5000802, 15100))
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    AND_10.Add(CharacterHasSpecialEffect(5000801, 15100))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterHasSpecialEffect(5000801, 15100))
    OR_3.Add(CharacterHasSpecialEffect(5000802, 15100))
    
    MAIN.Await(OR_3)
    
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    OR_4.Add(CharacterHasSpecialEffect(5000801, 15100))
    OR_4.Add(CharacterHasSpecialEffect(5000802, 15100))
    
    MAIN.Await(OR_4)
    
    Goto(Label.L0)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    GotoIfConditionTrue(Label.L6, input_condition=AND_6)
    AND_7.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    GotoIfConditionTrue(Label.L7, input_condition=AND_7)

    # --- Label 6 --- #
    DefineLabel(6)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    OR_6.Add(CharacterDead(5000801))
    OR_6.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    
    MAIN.Await(OR_6)
    
    Goto(Label.L0)

    # --- Label 7 --- #
    DefineLabel(7)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    OR_7.Add(CharacterDead(5000801))
    OR_7.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    
    MAIN.Await(OR_7)
    
    Goto(Label.L0)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L11, input_condition=AND_11)
    AND_12.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L12, input_condition=AND_12)

    # --- Label 11 --- #
    DefineLabel(11)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    OR_11.Add(CharacterDead(5000802))
    OR_11.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    
    MAIN.Await(OR_11)
    
    Goto(Label.L0)

    # --- Label 12 --- #
    DefineLabel(12)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    OR_12.Add(CharacterDead(5000802))
    OR_12.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    
    MAIN.Await(OR_12)
    
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(3.0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    End()


@RestartOnRest(15005850)
def Event_15005850(_, region: int, vfx_id: int, seconds: float, right: int):
    """Event 15005850"""
    if FlagEnabled(15000800):
        return
    DeleteVFX(vfx_id)
    if ValueNotEqual(left=1, right=right):
        OR_1.Add(CharacterInsideRegion(character=5000801, region=region))
        OR_1.Add(CharacterInsideRegion(character=5000802, region=region))
    else:
        OR_1.Add(CharacterHasSpecialEffect(5000801, 5404))
        OR_1.Add(CharacterHasSpecialEffect(5000802, 5404))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(15005802))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    CreateVFX(vfx_id)


@RestartOnRest(15005849)
def Event_15005849():
    """Event 15005849"""
    RunCommonEvent(20005800, args=(15000800, 5001800, 5002800, 15005805, 5001800, 5005800, 15005801, 0))
    RunCommonEvent(20005801, args=(15000800, 5001800, 5002801, 15005805, 5001800, 15005806))
    if FlagDisabled(15005801):
        RunCommonEvent(20001836, args=(15000800, 15005805, 15005806, 15005810, 5004801, 5004802, 15005802))
    else:
        RunCommonEvent(20005831, args=(15000800, 15005805, 15005806, 5002800, 5004801, 5004802, 15005802))
    RunCommonEvent(20005820, args=(15000800, 5001800, 3, 15005801))
    RunCommonEvent(20005820, args=(15000800, 5001801, 2, 15005801))
    RunCommonEvent(20005810, args=(15000800, 5001800, 5002801, 10000))
    Event_15005820(0, character=5000802, character_1=5000810, flag=15005840)
    Event_15005820(1, character=5000802, character_1=5000811, flag=15005841)
    Event_15005820(2, character=5000802, character_1=5000812, flag=15005842)
    Event_15005820(3, character=5000802, character_1=5000813, flag=15005843)
    Event_15005820(4, character=5000802, character_1=5000814, flag=15005844)
    Event_15005825(
        0,
        character__region=5000802,
        character=5000810,
        flag=15005840,
        special_effect=15020,
        character_1=5004810,
        model_point=100,
        right=0
    )
    Event_15005825(
        1,
        character__region=5000802,
        character=5000811,
        flag=15005841,
        special_effect=15021,
        character_1=5004811,
        model_point=1,
        right=0
    )
    Event_15005825(
        2,
        character__region=5000802,
        character=5000812,
        flag=15005842,
        special_effect=15022,
        character_1=5004812,
        model_point=2,
        right=0
    )
    Event_15005825(
        3,
        character__region=5000802,
        character=5000813,
        flag=15005843,
        special_effect=15027,
        character_1=5004813,
        model_point=1,
        right=1
    )
    Event_15005825(
        4,
        character__region=5000802,
        character=5000814,
        flag=15005844,
        special_effect=15028,
        character_1=5004814,
        model_point=2,
        right=1
    )
    Event_15005835()
    RunCommonEvent(20005840, args=(5001800,))
    RunCommonEvent(20005841, args=(5001800,))


@NeverRestart(15005700)
def Event_15005700(
    _,
    character: int,
    character_1: int,
    character_2: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
):
    """Event 15005700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1815, 1819))
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1815, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1816))
    AND_1.Add(FlagEnabled(70001073))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1815, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1800, 1814))
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1800, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1815)
    AND_2.Add(FlagEnabled(1800))
    AND_2.Add(FlagEnabled(75000101))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1801, state=FlagSetting.On)
    if FlagEnabled(1803):
        DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
        SetNetworkConnectedFlagState(flag=1801, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1801))
    AND_3.Add(FlagEnabled(9324))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1805, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1801))
    AND_4.Add(FlagEnabled(75000131))
    AND_4.Add(FlagDisabled(55000450))
    AND_4.Add(FlagEnabled(1875))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1802, state=FlagSetting.On)
    if FlagEnabled(1804):
        DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
        SetNetworkConnectedFlagState(flag=1802, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1802))
    AND_5.Add(FlagEnabled(9324))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1806, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1805))
    AND_6.Add(FlagEnabled(75000131))
    AND_6.Add(FlagDisabled(55000450))
    AND_6.Add(FlagEnabled(1875))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1806, state=FlagSetting.On)
    AND_7.Add(FlagRangeAnyEnabled(flag_range=(1805, 1806)))
    AND_7.Add(FlagEnabled(75000104))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1807, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001073)
    if FlagEnabled(1815):
        DisableFlag(75000120)
    OR_1.Add(FlagEnabled(1802))
    OR_1.Add(FlagEnabled(1806))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(15000703)
    SkipLinesIfFlagRangeAllDisabled(1, (1807, 1814))
    EnableFlag(75000135)
    OR_2.Add(FlagEnabled(1801))
    OR_2.Add(FlagEnabled(1803))
    OR_2.Add(FlagEnabled(1805))
    AND_8.Add(FlagEnabled(75000130))
    AND_8.Add(FlagDisabled(55000450))
    AND_8.Add(FlagEnabled(1875))
    AND_8.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_8)
    EnableFlag(75000131)
    OR_3.Add(FlagEnabled(1801))
    OR_3.Add(FlagEnabled(1803))
    OR_3.Add(FlagEnabled(1805))
    AND_9.Add(FlagEnabled(75000103))
    AND_9.Add(FlagDisabled(55000450))
    AND_9.Add(FlagEnabled(1875))
    AND_9.Add(OR_3)
    SkipLinesIfConditionFalse(1, AND_9)
    EnableFlag(75000130)
    OR_4.Add(PlayerHasGood(2153))
    OR_4.Add(FlagEnabled(6500))
    SkipLinesIfConditionFalse(1, OR_4)
    EnableFlag(50006623)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1800)
    GotoIfFlagEnabled(Label.L1, flag=1801)
    GotoIfFlagEnabled(Label.L2, flag=1802)
    GotoIfFlagEnabled(Label.L5, flag=1805)
    GotoIfFlagEnabled(Label.L6, flag=1806)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character_2, animation_id_2, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character_2, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DropMandatoryTreasure(character_2)
    End()


@RestartOnRest(15005701)
def Event_15005701(_, obj: int, character: int, obj_1: int):
    """Event 15005701"""
    DisableObject(obj_1)
    
    MAIN.Await(FlagEnabled(15000703))
    
    DisableTreasure(obj=obj)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(obj_1)


@NeverRestart(15005702)
def Event_15005702(_, character: int, character_1: int, flag: int, flag_1: int):
    """Event 15005702"""
    EndIfFlagRangeAnyEnabled(flag_range=(1805, 1814))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(9324))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 490))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=10.0))
    AND_1.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)


@NeverRestart(15005720)
def Event_15005720(_, character: int, animation_id: int, command_id: int, obj: int, destination: int):
    """Event 15005720"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1875, 1879))
    DisableNetworkConnectedFlagRange(flag_range=(1875, 1879))
    SetNetworkConnectedFlagState(flag=1875, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1876))
    AND_1.Add(FlagEnabled(70001076))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1875, 1879))
    SetNetworkConnectedFlagState(flag=1875, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1860, 1874))
    DisableNetworkConnectedFlagRange(flag_range=(1860, 1874))
    SetNetworkConnectedFlagState(flag=1860, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1860))
    AND_2.Add(FlagEnabled(1878))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1860, 1874))
    SetNetworkConnectedFlagState(flag=1861, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1860))
    AND_3.Add(FlagEnabled(1875))
    AND_3.Add(FlagEnabled(15100500))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1860, 1874))
    SetNetworkConnectedFlagState(flag=1862, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1875, 1879))
    SetNetworkConnectedFlagState(flag=1878, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001076)
    DisableFlag(15000721)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1860)
    GotoIfFlagEnabled(Label.L1, flag=1861)
    GotoIfFlagEnabled(Label.L2, flag=1862)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, flag=1878)
    DisableHealthBar(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    DisableCharacterCollision(character)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    DestroyObject(obj, request_slot=0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EzstateAIRequest(character, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character)
    DestroyObject(obj)
    End()


@NeverRestart(15005721)
def Event_15005721(_, character: int, obj: int):
    """Event 15005721"""
    GotoIfFlagEnabled(Label.L0, flag=15000721)
    if FlagDisabled(1860):
        return
    GotoIfPlayerNotInOwnWorld(Label.L1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableObjectInvulnerability(obj)
    DestroyObject_NoSlot(obj=obj)
    EnableFlag(15000721)


@RestartOnRest(15005722)
def Event_15005722(_, character: int):
    """Event 15005722"""
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(1861, 1862)))
    
    EnableCharacter(character)
    EnableBackread(character)
    DisableGravity(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(15005900)
def Event_15005900():
    """Event 15005900"""
    SetBackreadStateAlternate(5000202, True)
    SetBackreadStateAlternate(5000212, True)
    SetNetworkUpdateRate(5000212, is_fixed=True, update_rate=CharacterUpdateRate.Always)
