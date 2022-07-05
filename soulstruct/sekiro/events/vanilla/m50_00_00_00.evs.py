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


def Constructor():
    """ 0: Event 0 """
    RunCommonEvent(20005500, args=(15000800, 15000000, 5000950, 5001950))
    RegisterBonfire(15000001, obj=5001951, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(15000002, obj=5001952, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(15000003, obj=5001953, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(15000004, obj=5001954, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunEvent(15005100)
    RunEvent(15005800)
    RunEvent(15005810)
    RunEvent(15005811)
    RunEvent(15005812)
    RunEvent(15005813)
    RunEvent(15005800)
    RunEvent(15005849)
    RunEvent(15005850, slot=0, args=(5002850, 5003850, 0.5, 1), arg_types="iifi")
    RunEvent(15005850, slot=1, args=(5002851, 5003851, 0.10000000149011612, 1), arg_types="iifi")
    RunEvent(15005850, slot=2, args=(5002852, 5003852, 0.0, 1), arg_types="iifi")
    RunEvent(15005850, slot=3, args=(5002853, 5003853, 0.20000000298023224, 1), arg_types="iifi")
    RunEvent(15005850, slot=4, args=(5002854, 5003854, 0.0, 1), arg_types="iifi")
    RunEvent(15005850, slot=5, args=(5002855, 5003855, 0.4000000059604645, 1), arg_types="iifi")
    RunEvent(15005850, slot=6, args=(5002856, 5003856, 0.5, 1), arg_types="iifi")
    RunEvent(15005850, slot=7, args=(5002857, 5003857, 0.699999988079071, 1), arg_types="iifi")
    RunEvent(15005850, slot=8, args=(5002858, 5003858, 0.8999999761581421, 1), arg_types="iifi")
    RunEvent(15005850, slot=9, args=(5002859, 5003859, 0.800000011920929, 1), arg_types="iifi")
    RunEvent(15005850, slot=10, args=(5002860, 5003860, 0.10000000149011612, 1), arg_types="iifi")
    RunEvent(15005850, slot=11, args=(5002861, 5003861, 0.20000000298023224, 1), arg_types="iifi")
    RunEvent(15005850, slot=12, args=(5002862, 5003862, 0.6000000238418579, 1), arg_types="iifi")
    RunEvent(15005850, slot=13, args=(5002863, 5003863, 0.9800000190734863, 1), arg_types="iifi")
    RunEvent(15005850, slot=14, args=(5002864, 5003864, 0.5, 1), arg_types="iifi")
    RunEvent(15005850, slot=15, args=(5002865, 5003865, 0.6000000238418579, 1), arg_types="iifi")
    RunEvent(15005850, slot=16, args=(5002866, 5003866, 0.699999988079071, 1), arg_types="iifi")
    RunEvent(15005850, slot=17, args=(5002867, 5003867, 0.6899999976158142, 1), arg_types="iifi")
    RunEvent(15005850, slot=18, args=(5002868, 5003868, 0.20000000298023224, 1), arg_types="iifi")
    RunEvent(15005850, slot=19, args=(5002869, 5003869, 0.4000000059604645, 1), arg_types="iifi")
    RunEvent(15005850, slot=20, args=(5002870, 5003870, 0.30000001192092896, 1), arg_types="iifi")
    RunEvent(15005850, slot=21, args=(5002871, 5003871, 1.0, 1), arg_types="iifi")
    RunEvent(15005850, slot=22, args=(5002872, 5003872, 0.0, 1), arg_types="iifi")
    RunEvent(15005850, slot=23, args=(5002873, 5003873, 0.8999999761581421, 1), arg_types="iifi")
    RunEvent(15005220, slot=0, args=(5000200, 15005230, 15005215, 5000210, 16620, 16640))
    RunCommonEvent(20005203, args=(5000200, 30000, 20000, 5002200, 5002201, 5002202, 0, 0, 0))
    RunEvent(15005210, slot=0, args=(5000210, 16256, 5004200, 5000200, 15005215))
    RunEvent(15005250, slot=0, args=(5000210, 5000200))
    RunEvent(15005260)
    RunEvent(15005270, slot=0, args=(5000200,))
    RunEvent(15005290, slot=0, args=(5000200,))
    RunEvent(15005285, slot=0, args=(15000235, 5000200, 5000210))
    DisableFlag(15005215)
    RunEvent(15005261)
    RunEvent(15005220, slot=1, args=(5000201, 15005231, 15005216, 5000211, 16621, 16641))
    RunEvent(15005240, slot=0, args=(5000201, 5002228, 16255))
    RunEvent(15005210, slot=1, args=(5000211, 16256, 5004201, 5000201, 15005216))
    RunEvent(15005250, slot=1, args=(5000211, 5000201))
    RunEvent(15005270, slot=1, args=(5000201,))
    RunEvent(15005266, slot=1, args=(5000211, 20001, 5002220, 5002221, 5002222, 0, 0, 0, 0))
    RunEvent(15005280, slot=0, args=(5000201, 30000, 20000))
    RunEvent(15005290, slot=1, args=(5000201,))
    RunEvent(15005285, slot=1, args=(15000236, 5000201, 5000211))
    DisableFlag(15005216)
    RunEvent(15005265, slot=0, args=(5000212, 20000, 5002240, 5002241, 5002242, 5002243, 0, 0, 0))
    RunEvent(15005220, slot=2, args=(5000202, 15005232, 15005217, 5000212, 16622, 16642))
    RunEvent(15005210, slot=2, args=(5000212, 16256, 5004202, 5000202, 15005217))
    RunEvent(15005250, slot=2, args=(5000212, 5000202))
    RunEvent(15005270, slot=2, args=(5000202,))
    RunEvent(15005290, slot=2, args=(5000202,))
    RunEvent(15005285, slot=2, args=(15000237, 5000202, 5000212))
    RunEvent(
        15005460,
        slot=1,
        args=(5000223, 700, 1700, 5002401, 5000222, 16005, 0.30000001192092896, 5000220),
        arg_types="iiiiiifi",
    )
    RunCommonEvent(20005132, args=(5000222, 1084227584, 5002400))
    RunCommonEvent(20005210, args=(5000224, 700, 1700, 1094713344))
    RunCommonEvent(20005132, args=(5000226, 1084227584, 5002402))
    RunCommonEvent(20005206, args=(5000232, 701, 1701, 5002250, 5002251, 5002252, 0, 0, 0))
    RunCommonEvent(20005203, args=(5000233, 701, 1701, 2, 5002253, 5002254, 0, 0, 0))
    RunCommonEvent(20005213, args=(5000236, 700, 1700, 1086324736, 5002256))
    RunCommonEvent(20005213, args=(5000237, 701, 1701, 1084227584, 5002257))
    RunEvent(15005470)
    RunCommonEvent(20005213, args=(5000300, 700, 1700, 1073741824, 5002301))
    RunCommonEvent(20005219, args=(5000301, 700, 1700, 1073741824, 5002302, 1077936128))
    RunCommonEvent(20005243, args=(5000400, 700, 1700, 5000300, 16220, 1087373312))
    RunCommonEvent(20005243, args=(5000401, 700, 1700, 5000300, 16220, 1088841318))
    RunCommonEvent(20005243, args=(5000402, 700, 1700, 5000300, 16220, 1081711002))
    RunCommonEvent(20005243, args=(5000403, 700, 1700, 5000300, 16220, 1085905306))
    RunCommonEvent(20005243, args=(5000404, 700, 1700, 5000300, 16220, 1082969293))
    RunCommonEvent(20005243, args=(5000405, 700, 1700, 5000300, 16220, 1072902963))
    RunCommonEvent(20005243, args=(5000406, 700, 1700, 5000300, 16220, 1061997773))
    RunCommonEvent(20005243, args=(5000407, 700, 1700, 5000300, 16220, 0))
    RunCommonEvent(20005243, args=(5000408, 700, 1700, 5000300, 16220, 1081291571))
    RunCommonEvent(20005243, args=(5000409, 700, 1700, 5000300, 16220, 1075838976))
    RunCommonEvent(20005243, args=(5000410, 700, 1700, 5000300, 16220, 1065353216))
    RunCommonEvent(20005212, args=(5000310, 700, 1700, 1084227584, 5002315))
    RunCommonEvent(20005212, args=(5000311, 700, 1700, 1101004800, 5002315))
    RunCommonEvent(20005219, args=(5000315, 700, 1700, 1077936128, 5002317, 1065353216))
    RunCommonEvent(20005219, args=(5000420, 700, 1700, 1073741824, 5002310, 0))
    RunCommonEvent(20005219, args=(5000421, 701, 1701, 1065353216, 5002316, 0))
    RunCommonEvent(20005219, args=(5000422, 702, 20000, 1073741824, 5002311, 1036831949))
    RunCommonEvent(20005219, args=(5000423, 701, 1701, 1073741824, 5002312, 0))
    RunCommonEvent(20005219, args=(5000424, 702, 20000, 1073741824, 5002312, 1050253722))
    RunCommonEvent(20005219, args=(5000425, 702, 20000, 1073741824, 5002314, 0))
    RunCommonEvent(20005219, args=(5000426, 700, 1700, 1073741824, 5002312, 1061997773))
    RunCommonEvent(20005219, args=(5000427, 701, 1701, 1065353216, 5002318, 1069547520))
    RunCommonEvent(20005219, args=(5000428, 700, 1700, 1065353216, 5002319, 1056964608))
    RunCommonEvent(20005219, args=(5000316, 700, 1700, 1073741824, 5002320, 1067869798))
    RunCommonEvent(20005219, args=(5000317, 700, 1700, 1073741824, 5002320, 0))
    RunEvent(15005410, slot=0, args=(5000319, 700, 1700, 5002322, 15005392, 0.10000000149011612), arg_types="iiiiif")
    RunCommonEvent(20005205, args=(5000448, 701, 1701, 5002328, 1036831949))
    RunCommonEvent(20005132, args=(5000449, 1077936128, 5002329))
    RunCommonEvent(20005205, args=(5000331, 700, 1700, 5002332, 1084227584))
    RunCommonEvent(20005205, args=(5000456, 702, 20000, 5002332, 1091567616))
    RunCommonEvent(20005205, args=(5000457, 702, 20000, 5002334, 0))
    RunCommonEvent(20005205, args=(5000458, 700, 1700, 5002333, 1073741824))
    RunCommonEvent(20005205, args=(5000459, 701, 1701, 5002335, 1084227584))
    RunCommonEvent(20005219, args=(5000335, 700, 1700, 1073741824, 5002340, 0))
    RunCommonEvent(20005201, args=(5000460, 700, 1700, 5002340, 1077936128))
    RunCommonEvent(20005201, args=(5000461, 700, 1700, 5002340, 1067030938))
    RunCommonEvent(20005201, args=(5000462, 700, 1700, 5002340, 1069547520))
    RunCommonEvent(20005201, args=(5000463, 700, 1700, 5002340, 1085276160))
    RunCommonEvent(20005201, args=(5000464, 700, 1700, 5002340, 1085905306))
    RunEvent(15005400, slot=0, args=(5000335, 5000460, 5003340, 5000520, 5003345, 0.0), arg_types="iiiiif")
    RunEvent(
        15005400,
        slot=1,
        args=(5000335, 5000461, 5003341, 5000521, 5003346, 0.10000000149011612),
        arg_types="iiiiif",
    )
    RunEvent(
        15005400,
        slot=2,
        args=(5000335, 5000462, 5003342, 5000522, 5003347, 0.30000001192092896),
        arg_types="iiiiif",
    )
    RunCommonEvent(20005201, args=(5000337, 700, 1700, 5002356, 0))
    RunCommonEvent(20005201, args=(5000475, 700, 1700, 5002355, 1077936128))
    RunCommonEvent(20005201, args=(5000476, 700, 1700, 5002355, 1080872141))
    RunCommonEvent(20005201, args=(5000477, 700, 1700, 5002355, 1081291571))
    RunCommonEvent(20005201, args=(5000478, 700, 1700, 5002355, 1084227584))
    RunCommonEvent(20005201, args=(5000479, 700, 1700, 5002355, 1085276160))
    RunEvent(15005340, slot=0, args=(5000316, 5000500))
    RunEvent(15005340, slot=1, args=(5000319, 5000503))
    RunEvent(15005340, slot=2, args=(5000315, 5000501))
    RunEvent(15005340, slot=3, args=(5000426, 5000502))
    RunEvent(15005340, slot=4, args=(5000337, 5000530))
    RunEvent(15005340, slot=7, args=(5000454, 5000506))
    RunEvent(15005340, slot=8, args=(5000455, 5000507))
    RunEvent(15005340, slot=9, args=(5000457, 5000508))
    RunEvent(15005340, slot=10, args=(5000458, 5000509))
    RunEvent(15005340, slot=11, args=(5000463, 5000523))
    RunEvent(15005340, slot=12, args=(5000464, 5000524))
    RunEvent(15005360, slot=0, args=(5000460, 5000520))
    RunEvent(15005360, slot=1, args=(5000461, 5000521))
    RunEvent(15005360, slot=2, args=(5000462, 5000522))
    RunEvent(15005340, slot=13, args=(5000463, 5000523))
    RunEvent(15005340, slot=14, args=(5000464, 5000524))
    RunEvent(15005365, slot=0, args=(5000520,))
    RunEvent(15005365, slot=1, args=(5000521,))
    RunEvent(15005365, slot=2, args=(5000522,))
    RunEvent(15005310, slot=12, args=(5000335, 5000460))
    RunEvent(15005310, slot=13, args=(5000335, 5000461))
    RunEvent(15005310, slot=14, args=(5000335, 5000462))
    RunEvent(15005310, slot=15, args=(5000336, 5000463))
    RunEvent(15005310, slot=16, args=(5000336, 5000464))
    RunEvent(15005390, slot=0, args=(5000324, 5002325, 5003320))
    RunEvent(15005390, slot=1, args=(5000324, 5002326, 5003321))
    RunEvent(15005390, slot=2, args=(5000324, 5002327, 5003322))
    RunEvent(15005390, slot=3, args=(5000324, 5002342, 5003323))
    RunEvent(15005390, slot=4, args=(5000324, 5002343, 5003324))
    RunEvent(15005390, slot=5, args=(5000332, 5002350, 5003350))
    RunEvent(15005390, slot=6, args=(5000332, 5002350, 5003351))
    RunCommonEvent(20005114, args=(5000270, 5002270, 1065353216))
    RunCommonEvent(20005114, args=(5000271, 5002270, 1069547520))
    RunCommonEvent(20005120, args=(5000272, 1094713344))
    RunCommonEvent(20005331, args=(5000270,))
    RunCommonEvent(20005331, args=(5000271,))
    RunCommonEvent(20005331, args=(5000272,))
    RunEvent(15005444)
    RunEvent(15005447)
    RunEvent(15005448, slot=1, args=(5000273, 701, 1701, 5002272, 0.5), arg_types="iiiif")
    RunEvent(15005448, slot=2, args=(5000274, 701, 1701, 5002272, 0.0), arg_types="iiiif")
    RunEvent(15005448, slot=3, args=(5000275, 700, 1700, 5002271, 2.0), arg_types="iiiif")
    RunCommonEvent(20005132, args=(5000275, 1077936128, 5002274))
    RunCommonEvent(20005132, args=(5000279, 1077936128, 5002276))
    RunCommonEvent(20005132, args=(5000280, 1077936128, 5002277))
    RunCommonEvent(20005132, args=(5000281, 1077936128, 5002277))
    RunCommonEvent(20005205, args=(5000283, 701, 1701, 5002279, 1056964608))
    RunCommonEvent(20005205, args=(5000284, 701, 1701, 5002280, 1056964608))
    RunCommonEvent(20005134, args=(5000285, 3006, 1077936128, 5002281))
    RunCommonEvent(20005205, args=(5000286, 701, 1701, 5002282, 1082130432))
    RunCommonEvent(20005132, args=(5000287, 1084227584, 5002286))
    RunCommonEvent(20005132, args=(5000288, 1084227584, 5002286))
    RunEvent(15005440, slot=0, args=(5000288, 5000200, 5002287, 5000287))
    RunEvent(15005500)
    RunEvent(15005502)
    RunEvent(15005510)
    RunEvent(15005520, slot=0, args=(5002520, 5001520))
    RunEvent(15005520, slot=1, args=(5002521, 5001521))
    RunEvent(15005530, slot=0, args=(5002530,))
    RunEvent(15005530, slot=1, args=(5002531,))
    RunEvent(15005530, slot=2, args=(5002532,))
    RunEvent(15005530, slot=3, args=(5002533,))
    RunEvent(15005530, slot=4, args=(5002534,))
    RunEvent(15005550, slot=0, args=(5002550,))
    RunEvent(20005640, slot=0, args=(15000580, 5001580, 15000581, 15000582))
    RunEvent(15005590)
    RunCommonEvent(20005650, args=(15000560, 5001560))
    RunEvent(15005120, slot=0, args=(15000120, 5000120))
    RunEvent(15005120, slot=1, args=(15000121, 5000121))
    RunEvent(15005120, slot=2, args=(15000122, 5000122))
    RunEvent(15005120, slot=3, args=(15000123, 5000123))
    RunEvent(15005120, slot=4, args=(15000124, 5000124))
    RunEvent(15005120, slot=5, args=(15000125, 5000125))
    RunEvent(15005120, slot=6, args=(15000126, 5000126))
    RunEvent(15005120, slot=7, args=(15000127, 5000127))
    RunCommonEvent(20005701, args=(15000800, 15004170, 15005170, 5000170, 5002170, 70000030))
    RunCommonEvent(20005720, args=(15004170, 15005170, 15000800, 5000170))
    RunCommonEvent(20005716, args=(15004170, 15005805, 5000170, 5002801, 5002805, 15005801))
    RunCommonEvent(20005715, args=(15004170, 15005805, 5000170, 5002806, 15005801, 5002807, 0))
    RunEvent(15005540, slot=0, args=(5002534, 5000170))
    RunCommonEvent(20005701, args=(15000800, 15004174, 15005174, 5000174, 5002174, 0))
    RunCommonEvent(20005720, args=(15004174, 15005174, 15000800, 5000174))
    RunCommonEvent(20005716, args=(15004174, 15005805, 5000174, 5002801, 5002805, 15005801))
    RunCommonEvent(20005715, args=(15004174, 15005805, 5000174, 5002806, 15005801, 5002807, 0))
    RunEvent(15005540, slot=1, args=(5002534, 5000174))
    RunCommonEvent(20005342, args=(15000180, 5000180))
    RunCommonEvent(20005132, args=(5000180, 1086324736, 5002270))
    RunEvent(15005480, slot=0, args=(5000190, 6.0, 5002270, 5000180, 15000180, 5005190), arg_types="ifiiii")
    RunCommonEvent(20006002, args=(5000700, 1818, 1815, 1819))
    RunCommonEvent(20006002, args=(5000701, 1818, 1815, 1819))
    RunCommonEvent(20006002, args=(5000702, 1818, 1815, 1819))
    RunCommonEvent(20006000, args=(5000700, 1816, 1817, 75000140, 1059481190, 1815, 1819, 0))
    RunCommonEvent(20006000, args=(5000701, 1816, 1817, 75000141, 1059481190, 1815, 1819, 0))
    RunCommonEvent(20006000, args=(5000702, 1816, 1817, 75000142, 1059481190, 1815, 1819, 0))
    RunCommonEvent(20006001, args=(5000700, 1816, 1817, 75000140, 3))
    RunCommonEvent(20006001, args=(5000701, 1816, 1817, 75000141, 3))
    RunCommonEvent(20006001, args=(5000702, 1816, 1817, 75000142, 3))
    RunCommonEvent(20006030, args=(5001700, 4000, 0, 66200, 50006620, 50006620, 75000135))
    RunEvent(15005702, slot=0, args=(5000701, 5000170, 1801, 1803))
    RunEvent(15005702, slot=1, args=(5000702, 5000170, 1802, 1804))
    RunCommonEvent(20006002, args=(5000705, 1878, 1875, 1879))
    RunCommonEvent(20006040, args=(5000705, 5002705, 5450))
    RunEvent(15005721, slot=0, args=(5000705, 5001705))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(15005200, slot=0, args=(5000200, 5002200, 0, 0))
    RunEvent(15005200, slot=1, args=(5000201, 5002220, 5002221, 5002222))
    RunEvent(15005200, slot=2, args=(5000202, 5002240, 5002241, 5002242))
    RunEvent(15005570)
    RunEvent(15005575)
    DisableSoundEvent(5004801)
    DisableSoundEvent(5004802)
    RunEvent(15005700, slot=0, args=(5000700, 5000701, 5000702, 91180, 91180, 91170))
    RunEvent(15005701, slot=0, args=(5001345, 5000230, 5001230))
    RunEvent(15005720, slot=0, args=(5000705, 30004, 2160, 5001705, 5002705))
    RunEvent(15005722, slot=0, args=(5000203,))


@RestartOnRest
def Event15005100():
    """ 15005100: Event 15005100 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 15000800)
    IfActionButtonParamActivated(1, action_button_id=9380, entity=5001100)
    IfConditionTrue(0, input_condition=1)
    IfPlayerHasGood(2, 2156, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(
        10012800,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    SetRespawnPoint(5102110)
    SaveRequest()
    PlayCutscene(
        51000000,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=5102110,
        move_to_map=RINGED_CITY,
    )
    WaitFrames(1)
    Restart()


def Event15005120(_, arg_0_3: int, arg_4_7: int):
    """ 15005120: Event 15005120 """
    AddSpecialEffect(arg_4_7, 17500)
    DisableAI(arg_4_7)
    DisableAnimations(arg_4_7)
    ForceAnimation(arg_4_7, 91230)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    DisableFlag(arg_0_3)
    End()


@RestartOnRest
def Event15005200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 15005200: Event 15005200 """
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest
def Event15005210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 15005210: Event 15005210 """
    IfCharacterHasSpecialEffect(1, arg_0_3, arg_4_7)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    MakeEnemyAppear(arg_8_11)
    DisableFlag(arg_16_19)
    WaitFrames(1)
    ReplanAI(arg_12_15)
    SetNetworkUpdateRate(arg_12_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableGravity(arg_12_15)
    Restart()


@RestartOnRest
def Event15005220(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 15005220: Event 15005220 """
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    SetNetworkConnectedFlagState(flag=arg_4_7, state=FlagState.Off)
    IfCharacterDead(2, arg_0_3)
    IfPlayerInOwnWorld(2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfClientTypeCountComparison(3, ClientType.Invader, ComparisonType.Equal, 0)
    SetNetworkConnectedFlagState(flag=arg_4_7, state=FlagState.On)
    SetNetworkConnectedFlagState(flag=arg_8_11, state=FlagState.On)
    AddSpecialEffect(arg_12_15, arg_16_19)
    SetNetworkUpdateRate(arg_12_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    IfCharacterAlive(3, arg_0_3)
    IfPlayerInOwnWorld(3)
    IfConditionTrue(0, input_condition=3)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    SetNetworkConnectedFlagState(flag=arg_4_7, state=FlagState.Off)
    AddSpecialEffect(arg_12_15, arg_20_23)
    SetNetworkUpdateRate(arg_12_15, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest
def Event15005240(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005240: Event 15005240 """
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(arg_0_3, arg_8_11)
    SetCharacterEventTarget(arg_0_3, 10000)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event15005250(_, arg_0_3: int, arg_4_7: int):
    """ 15005250: Event 15005250 """
    IfCharacterDead(0, arg_0_3)
    AddSpecialEffect(arg_4_7, 16258)


@RestartOnRest
def Event15005260():
    """ 15005260: Event 15005260 """
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=5002202)
    IfCharacterInsideRegion(-2, PLAYER, region=5002221)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterHasSpecialEffect(1, 5000200, 16259)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(5000200, 16259)
    Restart()


@RestartOnRest
def Event15005261():
    """ 15005261: Event 15005261 """
    IfCharacterDead(15, 5000287)
    EndIfConditionTrue(15)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=5002286)
    IfConditionTrue(0, input_condition=1)
    Wait(2.9000000953674316)
    AddSpecialEffect(5000200, 16611)
    SetCharacterEventTarget(5000200, 5000287)
    IfCharacterDead(0, 5000287)
    CancelSpecialEffect(5000200, 16611)


@RestartOnRest
def Event15005265(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 15005265: Event 15005265 """
    SkipLinesIfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.Equal, 0)
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    EnableFlag(15005217)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_16_19)
    SkipLinesIfEqual(1, left=arg_20_23, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_20_23)
    SkipLinesIfEqual(1, left=arg_24_27, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_24_27)
    SkipLinesIfEqual(1, left=arg_28_31, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_28_31)
    SkipLinesIfEqual(1, left=arg_32_35, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_32_35)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(arg_0_3, arg_4_7, skip_transition=True)
    EnableAI(arg_0_3)


@RestartOnRest
def Event15005266(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 15005266: Event 15005266 """
    SkipLinesIfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.Equal, 0)
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_16_19)
    SkipLinesIfEqual(1, left=arg_20_23, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_20_23)
    SkipLinesIfEqual(1, left=arg_24_27, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_24_27)
    SkipLinesIfEqual(1, left=arg_28_31, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_28_31)
    SkipLinesIfEqual(1, left=arg_32_35, right=0)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_32_35)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(arg_0_3, arg_4_7, skip_transition=True)
    EnableAI(arg_0_3)


@RestartOnRest
def Event15005270(_, arg_0_3: int):
    """ 15005270: Event 15005270 """
    IfPlayerNotInOwnWorld(1)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(2, arg_0_3)
    IfCharacterAlive(2, arg_0_3)
    IfConditionTrue(0, input_condition=2)
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)
    IfCharacterDead(0, arg_0_3)
    Restart()


@RestartOnRest
def Event15005280(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005280: Event 15005280 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfCharacterHasSpecialEffect(1, 5000211, 16610)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5450)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    Wait(0.10000000149011612)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5450)
    EndIfConditionTrue(2)
    IfHasAIStatus(8, arg_0_3, ai_status=AIStatusType.Battle)
    GotoIfConditionTrue(Label.L1, input_condition=8)
    ForceAnimation(arg_0_3, arg_8_11)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 20002)

    # --- 0 --- #
    DefineLabel(0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event15005285(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005285: Event 15005285 """
    GotoIfFlagDisabled(Label.L0, arg_0_3)
    DisableAnimations(arg_4_7)
    DisableAnimations(arg_8_11)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_8_11)
    EnableFlag(arg_0_3)


@RestartOnRest
def Event15005290(_, arg_0_3: int):
    """ 15005290: Event 15005290 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5031)
    ClearTargetList(arg_0_3)
    Restart()


@RestartOnRest
def Event15005300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005300: Event 15005300 """
    CancelSpecialEffect(arg_0_3, 16240)
    SkipLinesIfThisEventSlotFlagDisabled(1)
    IfCharacterDead(1, arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, 16240)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    MakeEnemyAppear(arg_8_11)
    WaitFrames(1)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=8,
        copy_draw_parent=arg_0_3,
    )
    Restart()


@RestartOnRest
def Event15005310(_, arg_0_3: int, arg_4_7: int):
    """ 15005310: Event 15005310 """
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterAlive(1, arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 16245)
    IfCharacterDead(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    IfCharacterAlive(2, arg_4_7)
    RestartIfConditionTrue(2)
    AddSpecialEffect(arg_0_3, 16245)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event15005340(_, arg_0_3: int, arg_4_7: int):
    """ 15005340: Event 15005340 """
    IfCharacterDead(1, arg_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableCharacter(arg_0_3)
    DisableAnimations(arg_0_3)
    DisableAI(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableAI(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagDisabled(Label.L1)
    DisableCharacter(arg_0_3)
    DisableAnimations(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_4_7)
    DisableAnimations(arg_4_7)
    DisableAI(arg_4_7)
    IfCharacterHasSpecialEffect(0, arg_0_3, 16247)
    EnableCharacter(arg_4_7)
    EnableAI(arg_4_7)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=arg_0_3,
    )
    WaitFrames(1)
    ReplanAI(arg_4_7)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    IfCharacterHasSpecialEffect(0, arg_0_3, 16249)
    DisableCharacter(arg_0_3)
    DisableAnimations(arg_0_3)
    End()


@RestartOnRest
def Event15005360(_, arg_0_3: int, arg_4_7: int):
    """ 15005360: Event 15005360 """
    SkipLinesIfThisEventSlotFlagEnabled(2)
    DisableCharacter(arg_4_7)
    DisableAnimations(arg_4_7)
    DisableAI(arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, 16247)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_4_7)
    EnableAI(arg_4_7)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=arg_0_3,
    )
    WaitFrames(1)
    ReplanAI(arg_4_7)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    CancelSpecialEffect(arg_0_3, 16247)
    IfCharacterHasSpecialEffect(0, arg_0_3, 16249)
    Move(arg_0_3, destination=5002390, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    Kill(arg_0_3, award_souls=False)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event15005365(_, arg_0_3: int):
    """ 15005365: Event 15005365 """
    IfHealthValueGreaterThanOrEqual(1, arg_0_3, 1)
    IfCharacterHasSpecialEffect(1, arg_0_3, 16901)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    Kill(arg_0_3, award_souls=False)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event15005370(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005370: Event 15005370 """
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(arg_0_3, 16229)
    IfCharacterHasSpecialEffect(1, arg_4_7, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(arg_0_3, 16229)


@RestartOnRest
def Event15005380(_, arg_0_3: int, arg_4_7: int):
    """ 15005380: Event 15005380 """
    CancelSpecialEffect(arg_0_3, 16240)
    IfCharacterHasSpecialEffect(1, arg_0_3, 16240)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    MakeEnemyAppear(arg_4_7)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event15005390(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005390: Event 15005390 """
    DisableSpawner(arg_8_11)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfCharacterAlive(2, arg_0_3)
    IfConditionTrue(0, input_condition=2)
    EnableSpawner(arg_8_11)
    Wait(0.20000000298023224)
    IfAllPlayersOutsideRegion(3, region=arg_4_7)
    IfConditionTrue(-3, input_condition=3)
    IfCharacterDead(-3, arg_0_3)
    IfConditionTrue(0, input_condition=-3)
    Restart()


@RestartOnRest
def Event15005400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float):
    """ 15005400: Event 15005400 """
    CancelSpecialEffect(arg_0_3, 16240)
    SkipLinesIfThisEventSlotFlagDisabled(1)
    IfCharacterDead(1, arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, 16240)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_20_23)
    IfCharacterAlive(3, arg_4_7)
    SkipLinesIfConditionTrue(1, 3)
    MakeEnemyAppear(arg_8_11)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    IfCharacterAlive(2, arg_12_15)
    SkipLinesIfConditionTrue(1, 2)
    MakeEnemyAppear(arg_16_19)
    WaitFrames(1)
    DisableAI(arg_12_15)
    DisableCharacter(arg_12_15)
    DisableAnimations(arg_12_15)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event15005410(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float):
    """ 15005410: Event 15005410 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_4_7)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5450)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    Wait(arg_20_23)
    ForceAnimation(arg_0_3, arg_8_11)
    ReplanAI(arg_0_3)
    End()


@RestartOnRest
def Event15005440(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 15005440: Event 15005440 """
    SkipLinesIfFlagEnabled(1, 0)
    SkipLinesIfEqual(1, left=0, right=arg_12_15)
    IfAttacked(-1, arg_12_15, attacker=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=arg_4_7)
    IfCharacterInsideRegion(-1, arg_0_3, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_8_11)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    AddSpecialEffect(arg_0_3, 5000)
    IfCharacterInsideRegion(-3, arg_0_3, region=arg_12_15)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(arg_0_3, 5000)


@RestartOnRest
def Event15005444():
    """ 15005444: Event 15005444 """
    GotoIfPlayerInOwnWorld(Label.L9)
    GotoIfFlagEnabled(Label.L0, 15005445)
    Goto(Label.L1)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagDisabled(Label.L0, 15000180)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(5000290)
    DisableAnimations(5000290)
    DisableCharacter(5000291)
    DisableAnimations(5000291)
    DisableCharacter(5000292)
    DisableAnimations(5000292)
    EndIfPlayerNotInOwnWorld()
    SetNetworkConnectedFlagState(flag=15005445, state=FlagState.On)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(5000270)
    DisableAnimations(5000270)
    DisableCharacter(5000271)
    DisableAnimations(5000271)
    DisableCharacter(5000272)
    DisableAnimations(5000272)
    End()


@RestartOnRest
def Event15005447():
    """ 15005447: Event 15005447 """
    EndIfFlagEnabled(15000180)
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(5000272, 16805)
    IfEntityWithinDistance(0, 5000272, 5000180, radius=5.0)
    CancelSpecialEffect(5000272, 16805)


@RestartOnRest
def Event15005448(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 15005448: Event 15005448 """
    EndIfThisEventSlotFlagEnabled()
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5450)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfAttacked(-2, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    Wait(arg_16_19)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, arg_8_11)
    ReplanAI(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)


@RestartOnRest
def Event15005460(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: float,
    arg_28_31: int,
):
    """ 15005460: Event 15005460 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_4_7)
    DisableGravity(arg_0_3)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfCharacterHasSpecialEffect(-2, arg_0_3, arg_20_23)
    IfAttackedWithDamageType(-2, attacked_entity=arg_16_19, attacker=-1)
    IfAttackedWithDamageType(-2, attacked_entity=arg_28_31, attacker=-1)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5450)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, special_effect=arg_20_23)
    Wait(0.5)
    SkipLinesIfFinishedConditionFalse(1, 1)
    Wait(arg_24_27)
    EnableGravity(arg_0_3)
    ForceAnimation(arg_0_3, arg_8_11)
    ReplanAI(arg_0_3)
    End()


@RestartOnRest
def Event15005470():
    """ 15005470: Event 15005470 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(0, 5000236, region=5002260)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=5002261)
    IfEntityBeyondDistance(2, PLAYER, 5000236, radius=3.0)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(5000236, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(5000236, 3011, wait_for_completion=True)
    SetNetworkUpdateRate(5000236, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest
def Event15005480(_, arg_0_3: int, arg_4_7: float, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 15005480: Event 15005480 """
    GotoIfFlagDisabled(Label.L0, arg_16_19)
    DisableAI(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(arg_0_3)
    IfCharacterType(9, PLAYER, CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(9, PLAYER, 3710)
    IfConditionTrue(-1, input_condition=9)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-1)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(3, input_condition=-3)
    IfFlagDisabled(3, arg_16_19)
    IfConditionTrue(0, input_condition=3)

    # --- 1 --- #
    DefineLabel(1)
    EnableAI(arg_0_3)
    SkipLinesIfEqual(1, left=0, right=0)
    AddSpecialEffect(arg_20_23, 5000)
    AICommand(arg_0_3, command_id=100, slot=0)
    SetCharacterEventTarget(arg_0_3, arg_12_15)


@RestartOnRest
def Event15005500():
    """ 15005500: Event 15005500 """
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=False)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=False)
    GotoIfFlagDisabled(Label.L0, 15000500)
    EndOfAnimation(5001500, 2)
    DisableObject(5001501)
    DisableObject(5001502)
    DisableObject(5001503)
    EnableObject(5001504)
    CreateVFX(5003500)
    CreateVFX(5003501)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=True)
    DisableObject(5001504)
    IfCharacterInsideRegion(-1, PLAYER, region=5002500)
    IfCharacterInsideRegion(-1, PLAYER, region=5002501)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerInOwnWorld(1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(15000500)
    EnableFlag(15005500)
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=False)
    ForceAnimation(5001500, 1)
    Wait(1.5)
    CreateHazard(
        15005500,
        5001500,
        model_point=40,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(1.7000000476837158)
    CreateHazard(
        15005501,
        5001500,
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
    RemoveObjectFlag(15005500)
    RemoveObjectFlag(15005501)
    Wait(2.200000047683716)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=True)


@RestartOnRest
def Event15005502():
    """ 15005502: Event 15005502 """
    DisableNetworkSync()
    EndIfFlagEnabled(15000500)
    IfFlagEnabled(0, 15000500)
    IfCharacterInsideRegion(1, PLAYER, region=5002502)
    EndIfConditionFalse(1)
    Wait(0.4000000059604645)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=5002502,
        decay_start_distance=999.0,
        decay_end_distance=999.0,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.600000023841858)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=5002502,
        decay_start_distance=999.0,
        decay_end_distance=999.0,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.600000023841858)
    SetCameraVibration(
        vibration_id=104,
        anchor_entity=5002502,
        decay_start_distance=999.0,
        decay_end_distance=999.0,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest
def Event15005510():
    """ 15005510: Event 15005510 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(5001301, 310, loop=True, skip_transition=True)
    IfCharacterInsideRegion(0, PLAYER, region=5002510)
    DestroyObject_NoSlot(obj=5001510)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    ForceAnimation(5001301, 311, wait_for_completion=True, skip_transition=True)
    ForceAnimation(5001301, 312, loop=True, skip_transition=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(5001510)
    ForceAnimation(5001301, 312, loop=True, skip_transition=True)


@RestartOnRest
def Event15005520(_, arg_0_3: int, arg_4_7: int):
    """ 15005520: Event 15005520 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    DestroyObject_NoSlot(obj=arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(arg_4_7)


@RestartOnRest
def Event15005530(_, arg_0_3: int):
    """ 15005530: Event 15005530 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 4050)
    IfCharacterOutsideRegion(0, PLAYER, region=arg_0_3)
    CancelSpecialEffect(PLAYER, 4050)
    Restart()


@RestartOnRest
def Event15005540(_, arg_0_3: int, arg_4_7: int):
    """ 15005540: Event 15005540 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, arg_4_7, region=arg_0_3)
    AddSpecialEffect(arg_4_7, 4050)
    IfCharacterOutsideRegion(0, arg_4_7, region=arg_0_3)
    CancelSpecialEffect(arg_4_7, 4050)
    Restart()


@RestartOnRest
def Event15005550(_, arg_0_3: int):
    """ 15005550: Event 15005550 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 4070)
    IfCharacterOutsideRegion(0, PLAYER, region=arg_0_3)
    CancelSpecialEffect(PLAYER, 4070)
    Restart()


@RestartOnRest
def Event15005570():
    """ 15005570: Event 15005570 """
    EndIfThisEventSlotFlagEnabled()
    RestoreObject(5001510)
    RestoreObject(5001520)
    RestoreObject(5001521)


@RestartOnRest
def Event15005575():
    """ 15005575: Event 15005575 """
    EnableObjectInvulnerability(5001411)


@RestartOnRest
def Event15005580():
    """ 15005580: Event 15005580 """
    RegisterLadder(start_climbing_flag=15001580, stop_climbing_flag=15001581, obj=5001580)


@RestartOnRest
def Event15005590():
    """ 15005590: Event 15005590 """
    IfCharacterInsideRegion(1, PLAYER, region=5002590)
    IfFlagDisabled(1, 15000590)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAreaWelcomeMessage()
    EnableFlag(15000590)


@RestartOnRest
def Event15005800():
    """ 15005800: Event 15005800 """
    EndIfFlagEnabled(15000800)
    IfFlagEnabled(1, 15005803)
    IfHealthLessThanOrEqual(1, 5000801, 0.0)
    IfFlagEnabled(2, 15005804)
    IfHealthLessThanOrEqual(2, 5000802, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    Wait(3.0)
    PlaySoundEffect(anchor_entity=5000801, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5000801, banner=BannerType.HeirOfFireDestroyed)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(5005803, award_souls=False)
    Wait(3.0)
    PlaySoundEffect(anchor_entity=5000802, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5000802, banner=BannerType.HeirOfFireDestroyed)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(15000800)
    EnableFlag(9324)
    EnableFlag(6324)


@RestartOnRest
def Event15005810():
    """ 15005810: Event 15005810 """
    GotoIfFlagDisabled(Label.L0, 15000800)
    DisableCharacter(5005800)
    DisableAnimations(5005800)
    Kill(5005800, award_souls=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableImmortality(5000800)
    DisableHealthBar(5000800)
    SetLockOnPoint(5000800, lock_on_model_point=220, state=False)
    DisableAI(5005800)
    EnableImmortality(5000801)
    DisableAI(5005801)
    DisableHealthBar(5000801)
    SetCollisionMask(5000801, bit_index=1, switch_type=OnOffChange.Off)
    IfCharacterType(-15, PLAYER, CharacterType.BlackPhantom)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=7)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=21)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=4)
    EndIfConditionTrue(-15)
    IfCharacterInsideRegion(1, PLAYER, region=5002800)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=5000801, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(9, 15005805)
    IfCharacterInsideRegion(9, PLAYER, region=5002800)
    IfConditionTrue(0, input_condition=9)

    # --- 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    BanishInvaders(unknown=0)
    SetNetworkUpdateRate(5005801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(5000801, 5000800)
    Wait(0.30000001192092896)
    EnableAI(5005801)
    SkipLinesIfFlagEnabled(1, 15005810)
    Wait(3.0)
    EnableBossHealthBar(5000801, name=905020)
    EnableBossHealthBar(5000802, name=905021, slot=1)
    EnableFlag(15005810)
    SetNetworkConnectedFlagState(flag=15005801, state=FlagState.On)
    EndIfPlayerNotInOwnWorld()
    Wait(0.0)
    SetNetworkConnectedFlagState(flag=15005809, state=FlagState.On)


@RestartOnRest
def Event15005811():
    """ 15005811: Event 15005811 """
    EndIfFlagEnabled(15000800)
    EnableImmortality(5000802)
    DisableAI(5005802)
    DisableHealthBar(5000802)
    SetCollisionMask(5000802, bit_index=1, switch_type=OnOffChange.Off)
    IfPlayerInOwnWorld(1)
    IfFlagEnabled(1, 15005809)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 15005811)
    IfAttackedWithDamageType(-1, attacked_entity=5000802, attacker=-1)
    IfHealthLessThanOrEqual(-1, 5000801, 0.6499999761581421)
    IfCharacterHasSpecialEffect(-1, 5000801, 15025)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(5005802)
    SetNetworkUpdateRate(5005802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.0)
    EnableBossHealthBar(5000802, name=905021, slot=1)


@RestartOnRest
def Event15005812():
    """ 15005812: Event 15005812 """
    EndIfFlagEnabled(15000800)
    IfCharacterHasSpecialEffect(2, 5000801, 15202)
    IfCharacterHasSpecialEffect(3, 5000802, 15202)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    SetNetworkConnectedFlagState(flag=15005803, state=FlagState.On)
    Wait(6.0)
    DisableBossHealthBar(5000802, name=905023, slot=1)
    Wait(12.0)
    EnableBossHealthBar(5000801, name=905022)
    DisableImmortality(5000801)
    SetCollisionMask(5000801, bit_index=1, switch_type=OnOffChange.On)
    GotoIfPlayerNotInOwnWorld(Label.L11)
    IfAllyPhantomCountComparison(11, comparison_state=True, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    GotoIfConditionTrue(Label.L11, input_condition=11)
    AddSpecialEffect(5000801, 15150)

    # --- 11 --- #
    DefineLabel(11)
    DisableCharacter(5000802)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=15005804, state=FlagState.On)
    Wait(6.0)
    DisableBossHealthBar(5000801, name=905022)
    Wait(12.0)
    EnableBossHealthBar(5000802, name=905023)
    DisableImmortality(5000802)
    SetCollisionMask(5000802, bit_index=1, switch_type=OnOffChange.On)
    GotoIfPlayerNotInOwnWorld(Label.L12)
    IfAllyPhantomCountComparison(12, comparison_state=True, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    GotoIfConditionTrue(Label.L12, input_condition=12)
    AddSpecialEffect(5000802, 15150)

    # --- 12 --- #
    DefineLabel(12)
    DisableCharacter(5000801)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    SetNetworkConnectedFlagState(flag=15005802, state=FlagState.On)


@RestartOnRest
def Event15005813():
    """ 15005813: Event 15005813 """
    EndIfFlagEnabled(15000800)
    IfHealthValueEqual(1, 5000801, 1)
    IfHealthValueEqual(2, 5000802, 1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfPlayerInOwnWorld(3)
    IfConditionTrue(0, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    AddSpecialEffect(5000801, 15100)
    AddSpecialEffect(5000801, 15204)
    AddSpecialEffect(5000802, 15204)
    AddSpecialEffect(5000802, 15201)
    Wait(3.0)
    CancelSpecialEffect(5000801, 15040)
    CancelSpecialEffect(5000801, 15026)
    End()

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect(5000802, 15100)
    AddSpecialEffect(5000802, 15204)
    AddSpecialEffect(5000801, 15204)
    AddSpecialEffect(5000801, 15201)
    Wait(3.0)
    CancelSpecialEffect(5000802, 15040)
    CancelSpecialEffect(5000802, 15026)


@RestartOnRest
def Event15005820(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005820: Event 15005820 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(15000800)
    EndIfFlagEnabled(15005803)
    IfPlayerInOwnWorld(1)
    IfCharacterAlive(1, arg_0_3)
    IfCharacterDead(1, arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagState(flag=arg_8_11, state=FlagState.Off)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event15005825(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 15005825: Event 15005825 """
    EndIfFlagEnabled(15000800)
    EndIfFlagEnabled(15005803)
    DisableGravity(arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, arg_12_15)
    IfFlagDisabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    MakeEnemyAppear(arg_16_19)
    WaitFrames(1)
    SetNetworkUpdateRate(arg_4_7, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_20_23,
        copy_draw_parent=arg_0_3,
    )
    SetNetworkConnectedFlagState(flag=arg_8_11, state=FlagState.On)
    ReplanAI(arg_4_7)
    SkipLinesIfNotEqual(1, left=1, right=arg_24_27)
    SetCharacterEventTarget(arg_4_7, arg_0_3)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event15005830(_, arg_0_3: int):
    """ 15005830: Event 15005830 """
    EndIfFlagEnabled(15000800)
    DisableNetworkSync()
    IfHealthValueLessThanOrEqual(-5, 5000801, 0)
    IfHealthValueLessThanOrEqual(-5, 5000802, 0)
    GotoIfConditionTrue(Label.L9, input_condition=-5)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=18.0)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    IfEntityBeyondDistance(2, PLAYER, arg_0_3, radius=18.0)
    GotoIfConditionTrue(Label.L2, input_condition=2)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(arg_0_3, 15041)
    IfEntityBeyondDistance(-1, PLAYER, arg_0_3, radius=18.0)
    IfConditionTrue(0, input_condition=-1)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(arg_0_3, 15040)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=18.0)
    IfConditionTrue(0, input_condition=-2)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    Restart()

    # --- 9 --- #
    DefineLabel(9)
    IfCharacterHasSpecialEffect(10, arg_0_3, 15042)
    SkipLinesIfConditionTrue(1, 10)
    AddSpecialEffect(arg_0_3, 15040)
    Wait(0.20000000298023224)
    End()


@RestartOnRest
def Event15005835():
    """ 15005835: Event 15005835 """
    EndIfFlagEnabled(15000800)
    DisableNetworkSync()
    IfCharacterInsideRegion(13, PLAYER, region=5002800)
    IfFlagEnabled(13, 15005810)
    IfConditionTrue(0, input_condition=13)
    IfFlagEnabled(14, 15005803)
    IfCharacterDead(14, 5000801)
    IfFlagEnabled(15, 15005804)
    IfCharacterDead(15, 5000802)
    IfConditionTrue(-15, input_condition=14)
    IfConditionTrue(-15, input_condition=15)
    GotoIfConditionTrue(Label.L20, input_condition=-15)
    IfCharacterHasSpecialEffect(5, 5000802, 15100)
    GotoIfConditionTrue(Label.L5, input_condition=5)
    IfCharacterHasSpecialEffect(10, 5000801, 15100)
    GotoIfConditionTrue(Label.L10, input_condition=10)
    IfEntityWithinDistance(-1, PLAYER, 5000801, radius=8.0)
    IfEntityWithinDistance(-1, PLAYER, 5000802, radius=8.0)
    GotoIfConditionTrue(Label.L1, input_condition=-1)
    IfEntityBeyondDistance(1, PLAYER, 5000801, radius=8.0)
    IfEntityBeyondDistance(1, PLAYER, 5000802, radius=8.0)
    GotoIfConditionTrue(Label.L2, input_condition=1)

    # --- 1 --- #
    DefineLabel(1)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    IfEntityBeyondDistance(3, PLAYER, 5000801, radius=8.0)
    IfEntityBeyondDistance(3, PLAYER, 5000802, radius=8.0)
    IfConditionTrue(-3, input_condition=3)
    IfCharacterHasSpecialEffect(-3, 5000801, 15100)
    IfCharacterHasSpecialEffect(-3, 5000802, 15100)
    IfConditionTrue(0, input_condition=-3)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    IfEntityWithinDistance(-4, PLAYER, 5000801, radius=8.0)
    IfEntityWithinDistance(-4, PLAYER, 5000802, radius=8.0)
    IfCharacterHasSpecialEffect(-4, 5000801, 15100)
    IfCharacterHasSpecialEffect(-4, 5000802, 15100)
    IfConditionTrue(0, input_condition=-4)
    Goto(Label.L0)

    # --- 5 --- #
    DefineLabel(5)
    IfEntityWithinDistance(6, PLAYER, 5000801, radius=8.0)
    GotoIfConditionTrue(Label.L6, input_condition=6)
    IfEntityBeyondDistance(7, PLAYER, 5000801, radius=8.0)
    GotoIfConditionTrue(Label.L7, input_condition=7)

    # --- 6 --- #
    DefineLabel(6)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    IfCharacterDead(-6, 5000801)
    IfEntityBeyondDistance(-6, PLAYER, 5000801, radius=8.0)
    IfConditionTrue(0, input_condition=-6)
    Goto(Label.L0)

    # --- 7 --- #
    DefineLabel(7)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    IfCharacterDead(-7, 5000801)
    IfEntityWithinDistance(-7, PLAYER, 5000801, radius=8.0)
    IfConditionTrue(0, input_condition=-7)
    Goto(Label.L0)

    # --- 10 --- #
    DefineLabel(10)
    IfEntityWithinDistance(11, PLAYER, 5000802, radius=8.0)
    GotoIfConditionTrue(Label.L11, input_condition=11)
    IfEntityBeyondDistance(12, PLAYER, 5000802, radius=8.0)
    GotoIfConditionTrue(Label.L12, input_condition=12)

    # --- 11 --- #
    DefineLabel(11)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    IfCharacterDead(-11, 5000802)
    IfEntityBeyondDistance(-11, PLAYER, 5000802, radius=8.0)
    IfConditionTrue(0, input_condition=-11)
    Goto(Label.L0)

    # --- 12 --- #
    DefineLabel(12)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    IfCharacterDead(-12, 5000802)
    IfEntityWithinDistance(-12, PLAYER, 5000802, radius=8.0)
    IfConditionTrue(0, input_condition=-12)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    Restart()

    # --- 20 --- #
    DefineLabel(20)
    Wait(3.0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    End()


@RestartOnRest
def Event15005850(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 15005850: Event 15005850 """
    EndIfFlagEnabled(15000800)
    DeleteVFX(arg_4_7, erase_root_only=True)
    SkipLinesIfEqual(3, left=1, right=arg_12_15)
    IfCharacterInsideRegion(-1, 5000801, region=arg_0_3)
    IfCharacterInsideRegion(-1, 5000802, region=arg_0_3)
    SkipLines(2)
    IfCharacterHasSpecialEffect(-1, 5000801, 5404)
    IfCharacterHasSpecialEffect(-1, 5000802, 5404)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 15005802)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_8_11)
    CreateVFX(arg_4_7)


@RestartOnRest
def Event15005849():
    """ 15005849: Event 15005849 """
    RunCommonEvent(20005800, args=(15000800, 5001800, 5002800, 15005805, 5001800, 5005800, 15005801, 0))
    RunCommonEvent(20005801, args=(15000800, 5001800, 5002801, 15005805, 5001800, 15005806))
    SkipLinesIfFlagEnabled(2, 15005801)
    RunCommonEvent(20001836, args=(15000800, 15005805, 15005806, 15005810, 5004801, 5004802, 15005802))
    SkipLines(1)
    RunCommonEvent(20005831, args=(15000800, 15005805, 15005806, 5002800, 5004801, 5004802, 15005802))
    RunCommonEvent(20005820, args=(15000800, 5001800, 3, 15005801))
    RunCommonEvent(20005820, args=(15000800, 5001801, 2, 15005801))
    RunCommonEvent(20005810, args=(15000800, 5001800, 5002801, 10000))
    RunEvent(15005820, slot=0, args=(5000802, 5000810, 15005840))
    RunEvent(15005820, slot=1, args=(5000802, 5000811, 15005841))
    RunEvent(15005820, slot=2, args=(5000802, 5000812, 15005842))
    RunEvent(15005820, slot=3, args=(5000802, 5000813, 15005843))
    RunEvent(15005820, slot=4, args=(5000802, 5000814, 15005844))
    RunEvent(15005825, slot=0, args=(5000802, 5000810, 15005840, 15020, 5004810, 100, 0))
    RunEvent(15005825, slot=1, args=(5000802, 5000811, 15005841, 15021, 5004811, 1, 0))
    RunEvent(15005825, slot=2, args=(5000802, 5000812, 15005842, 15022, 5004812, 2, 0))
    RunEvent(15005825, slot=3, args=(5000802, 5000813, 15005843, 15027, 5004813, 1, 1))
    RunEvent(15005825, slot=4, args=(5000802, 5000814, 15005844, 15028, 5004814, 2, 1))
    RunEvent(15005835)
    RunCommonEvent(20005840, args=(5001800,))
    RunCommonEvent(20005841, args=(5001800,))


def Event15005700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 15005700: Event 15005700 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1815, 1819))
    SetNetworkConnectedFlagRangeState((1815, 1819), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1815, state=FlagState.On)
    IfFlagEnabled(1, 1816)
    IfFlagEnabled(1, 70001073)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1815, 1819), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1815, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1800, 1814))
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1800, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1815)
    IfFlagEnabled(2, 1800)
    IfFlagEnabled(2, 75000101)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1801, state=FlagState.On)
    SkipLinesIfFlagDisabled(2, 1803)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1801, state=FlagState.On)
    IfFlagEnabled(3, 1801)
    IfFlagEnabled(3, 9324)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1805, state=FlagState.On)
    IfFlagEnabled(4, 1801)
    IfFlagEnabled(4, 75000131)
    IfFlagDisabled(4, 55000450)
    IfFlagEnabled(4, 1875)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1802, state=FlagState.On)
    SkipLinesIfFlagDisabled(2, 1804)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1802, state=FlagState.On)
    IfFlagEnabled(5, 1802)
    IfFlagEnabled(5, 9324)
    SkipLinesIfConditionFalse(2, 5)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1806, state=FlagState.On)
    IfFlagEnabled(6, 1805)
    IfFlagEnabled(6, 75000131)
    IfFlagDisabled(6, 55000450)
    IfFlagEnabled(6, 1875)
    SkipLinesIfConditionFalse(2, 6)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1806, state=FlagState.On)
    IfFlagRangeAnyEnabled(7, (1805, 1806))
    IfFlagEnabled(7, 75000104)
    SkipLinesIfConditionFalse(2, 7)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1807, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70001073)
    SkipLinesIfFlagDisabled(1, 1815)
    DisableFlag(75000120)
    IfFlagEnabled(-1, 1802)
    IfFlagEnabled(-1, 1806)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(15000703)
    SkipLinesIfFlagRangeAllDisabled(1, (1807, 1814))
    EnableFlag(75000135)
    IfFlagEnabled(-2, 1801)
    IfFlagEnabled(-2, 1803)
    IfFlagEnabled(-2, 1805)
    IfFlagEnabled(8, 75000130)
    IfFlagDisabled(8, 55000450)
    IfFlagEnabled(8, 1875)
    IfConditionTrue(8, input_condition=-2)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(75000131)
    IfFlagEnabled(-3, 1801)
    IfFlagEnabled(-3, 1803)
    IfFlagEnabled(-3, 1805)
    IfFlagEnabled(9, 75000103)
    IfFlagDisabled(9, 55000450)
    IfFlagEnabled(9, 1875)
    IfConditionTrue(9, input_condition=-3)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(75000130)
    IfPlayerHasGood(-4, 2153, including_box=False)
    IfFlagEnabled(-4, 6500)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(50006623)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1800)
    GotoIfFlagEnabled(Label.L1, 1801)
    GotoIfFlagEnabled(Label.L2, 1802)
    GotoIfFlagEnabled(Label.L5, 1805)
    GotoIfFlagEnabled(Label.L6, 1806)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    GotoIfFlagEnabled(Label.L16, 1816)
    GotoIfFlagEnabled(Label.L18, 1818)
    ForceAnimation(arg_0_3, arg_12_15)
    End()

    # --- 16 --- #
    DefineLabel(16)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)

    # --- 5 --- #
    DefineLabel(5)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    GotoIfFlagEnabled(Label.L16, 1816)
    GotoIfFlagEnabled(Label.L18, 1818)
    ForceAnimation(arg_4_7, arg_16_19)
    End()

    # --- 16 --- #
    DefineLabel(16)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DropMandatoryTreasure(arg_4_7)
    End()

    # --- 2 --- #
    DefineLabel(2)

    # --- 6 --- #
    DefineLabel(6)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    GotoIfFlagEnabled(Label.L16, 1816)
    GotoIfFlagEnabled(Label.L18, 1818)
    ForceAnimation(arg_8_11, arg_20_23)
    End()

    # --- 16 --- #
    DefineLabel(16)
    SetTeamType(arg_8_11, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    DropMandatoryTreasure(arg_8_11)
    End()


@RestartOnRest
def Event15005701(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 15005701: Event 15005701 """
    DisableObject(arg_8_11)
    IfFlagEnabled(0, 15000703)
    DisableTreasure(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    EnableObject(arg_8_11)


def Event15005702(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 15005702: Event 15005702 """
    EndIfFlagRangeAnyEnabled((1805, 1814))
    IfPlayerInOwnWorld(1)
    IfFlagEnabled(1, 1815)
    IfFlagEnabled(1, arg_8_11)
    IfFlagDisabled(1, 9324)
    IfCharacterHasSpecialEffect(1, PLAYER, 490)
    IfEntityWithinDistance(1, PLAYER, arg_4_7, radius=10.0)
    IfCharacterBackreadEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SetNetworkConnectedFlagRangeState((1800, 1814), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_12_15, state=FlagState.On)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)


def Event15005720(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 15005720: Event 15005720 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1875, 1879))
    SetNetworkConnectedFlagRangeState((1875, 1879), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1875, state=FlagState.On)
    IfFlagEnabled(1, 1876)
    IfFlagEnabled(1, 70001076)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1875, 1879), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1875, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1860, 1874))
    SetNetworkConnectedFlagRangeState((1860, 1874), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1860, state=FlagState.On)
    IfFlagEnabled(2, 1860)
    IfFlagEnabled(2, 1878)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1860, 1874), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1861, state=FlagState.On)
    IfFlagEnabled(3, 1860)
    IfFlagEnabled(3, 1875)
    IfFlagEnabled(3, 15100500)
    SkipLinesIfConditionFalse(4, 3)
    SetNetworkConnectedFlagRangeState((1860, 1874), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1862, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1875, 1879), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1878, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70001076)
    DisableFlag(15000721)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1860)
    GotoIfFlagEnabled(Label.L1, 1861)
    GotoIfFlagEnabled(Label.L2, 1862)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, 1878)
    DisableHealthBar(arg_0_3)
    ForceAnimation(arg_0_3, arg_4_7)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    Move(arg_0_3, destination=arg_16_19, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    RestoreObject(arg_12_15)
    EnableObjectInvulnerability(arg_12_15)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    DestroyObject(arg_12_15, slot=0)
    End()

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)
    EzstateAIRequest(arg_0_3, command_id=arg_8_11, slot=1)
    DropMandatoryTreasure(arg_0_3)
    DestroyObject(arg_12_15)
    End()


def Event15005721(_, arg_0_3: int, arg_4_7: int):
    """ 15005721: Event 15005721 """
    GotoIfFlagEnabled(Label.L0, 15000721)
    EndIfFlagDisabled(1860)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    IfPlayerInOwnWorld(1)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5450)
    IfConditionTrue(0, input_condition=1)
    IfPlayerInOwnWorld(2)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5450)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)

    # --- 1 --- #
    DefineLabel(1)
    IfPlayerInOwnWorld(3)
    IfCharacterBackreadEnabled(3, arg_0_3)
    IfPlayerInOwnWorld(4)
    IfCharacterBackreadDisabled(4, arg_0_3)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(4)

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    DisableObjectInvulnerability(arg_4_7)
    DestroyObject_NoSlot(obj=arg_4_7)
    EnableFlag(15000721)


@RestartOnRest
def Event15005722(_, arg_0_3: int):
    """ 15005722: Event 15005722 """
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    IfFlagRangeAnyEnabled(0, (1861, 1862))
    EnableCharacter(arg_0_3)
    EnableBackread(arg_0_3)
    DisableGravity(arg_0_3)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest
def Event15005900():
    """ 15005900: Event 15005900 """
    SetBackreadStateAlternate(5000202, state=True)
    SetBackreadStateAlternate(5000212, state=True)
    SetNetworkUpdateRate(5000212, is_fixed=True, update_rate=CharacterUpdateRate.Always)
