"""
Common

linked:


strings:

"""
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_200()
    Event_230()
    Event_9570(0, item_lot=4500, special_effect=3740)
    Event_9570(1, item_lot=4510, special_effect=3750)
    if Client():
        return
    if FlagEnabled(2052):
        return
    Event_130(0, area_id=40, block_id=0, collision=4004110, ceremony_id=0, achievement_id=-1)
    Event_130(1, area_id=30, block_id=0, collision=3004110, ceremony_id=0, achievement_id=-1)
    Event_130(2, area_id=31, block_id=0, collision=3104110, ceremony_id=0, achievement_id=-1)
    Event_130(3, area_id=33, block_id=0, collision=3304110, ceremony_id=0, achievement_id=-1)
    Event_130(4, area_id=35, block_id=0, collision=3504110, ceremony_id=0, achievement_id=-1)
    Event_130(5, area_id=33, block_id=0, collision=3304111, ceremony_id=0, achievement_id=-1)
    Event_130(6, area_id=38, block_id=0, collision=3804110, ceremony_id=0, achievement_id=-1)
    Event_130(7, area_id=38, block_id=0, collision=3804111, ceremony_id=0, achievement_id=-1)
    Event_130(8, area_id=37, block_id=0, collision=3704110, ceremony_id=0, achievement_id=-1)
    Event_130(9, area_id=37, block_id=0, collision=3704111, ceremony_id=0, achievement_id=-1)
    Event_130(10, area_id=39, block_id=0, collision=3904110, ceremony_id=0, achievement_id=-1)
    Event_130(11, area_id=32, block_id=0, collision=3204110, ceremony_id=0, achievement_id=26)
    Event_130(12, area_id=30, block_id=0, collision=3004111, ceremony_id=0, achievement_id=-1)
    Event_130(13, area_id=34, block_id=1, collision=3414110, ceremony_id=0, achievement_id=-1)
    Event_130(14, area_id=40, block_id=0, collision=4004111, ceremony_id=10, achievement_id=25)
    Event_130(15, area_id=41, block_id=0, collision=4104110, ceremony_id=0, achievement_id=-1)
    Event_130(16, area_id=45, block_id=0, collision=4504110, ceremony_id=0, achievement_id=-1)
    Event_130(17, area_id=50, block_id=0, collision=5004110, ceremony_id=0, achievement_id=-1)
    Event_130(18, area_id=51, block_id=0, collision=5104110, ceremony_id=0, achievement_id=-1)
    Event_130(19, area_id=51, block_id=1, collision=5114110, ceremony_id=0, achievement_id=-1)
    Event_9004(0, flag=9007)
    Event_9005(0, flag=9008)
    Event_9006(0, flag=9009)
    Event_9000(0, flag=9001, flag_1=9007, flag_2=9008, flag_3=9009)
    Event_9002(0, flag=9003)
    Event_9010()
    Event_970(0, flag=13000800, item_lot=2000, item_lot_1=0, item_lot_2=0)
    Event_970(1, flag=13000890, item_lot=2010, item_lot_1=0, item_lot_2=0)
    Event_970(2, flag=13000830, item_lot=2020, item_lot_1=0, item_lot_2=0)
    Event_970(3, flag=13010800, item_lot=2030, item_lot_1=0, item_lot_2=0)
    Event_970(9, flag=13410830, item_lot=2040, item_lot_1=0, item_lot_2=0)
    Event_970(10, flag=13410860, item_lot=2050, item_lot_1=0, item_lot_2=0)
    Event_970(4, flag=13100800, item_lot=2060, item_lot_1=0, item_lot_2=0)
    Event_970(5, flag=13200800, item_lot=2070, item_lot_1=0, item_lot_2=0)
    Event_970(6, flag=13200850, item_lot=2080, item_lot_1=0, item_lot_2=0)
    Event_970(7, flag=13300850, item_lot=2090, item_lot_1=0, item_lot_2=0)
    Event_970(8, flag=13300800, item_lot=2100, item_lot_1=0, item_lot_2=0)
    Event_970(11, flag=13500800, item_lot=2110, item_lot_1=0, item_lot_2=0)
    Event_970(12, flag=13700850, item_lot=2120, item_lot_1=0, item_lot_2=0)
    Event_970(13, flag=13700800, item_lot=2130, item_lot_1=0, item_lot_2=0)
    Event_970(14, flag=13800800, item_lot=2140, item_lot_1=0, item_lot_2=0)
    Event_970(15, flag=13800830, item_lot=2150, item_lot_1=0, item_lot_2=0)
    Event_970(17, flag=13900800, item_lot=2170, item_lot_1=0, item_lot_2=0)
    Event_970(18, flag=14000800, item_lot=2180, item_lot_1=0, item_lot_2=0)
    Event_970(19, flag=14000830, item_lot=2190, item_lot_1=0, item_lot_2=0)
    Event_970(20, flag=14100800, item_lot=2200, item_lot_1=0, item_lot_2=0)
    Event_970(21, flag=14500800, item_lot=2300, item_lot_1=0, item_lot_2=0)
    Event_970(22, flag=14500860, item_lot=2310, item_lot_1=0, item_lot_2=0)
    Event_970(23, flag=15000800, item_lot=2330, item_lot_1=0, item_lot_2=0)
    Event_970(24, flag=15100800, item_lot=2340, item_lot_1=0, item_lot_2=0)
    Event_970(25, flag=15100850, item_lot=2350, item_lot_1=0, item_lot_2=0)
    Event_970(26, flag=15110800, item_lot=2360, item_lot_1=0, item_lot_2=0)
    Event_250(10, achievement_id=17, flag=6700, seconds=0.0)
    Event_250(11, achievement_id=18, flag=6770, seconds=0.0)
    Event_250(12, achievement_id=19, flag=6740, seconds=0.0)
    Event_250(13, achievement_id=20, flag=6750, seconds=0.0)
    Event_250(14, achievement_id=21, flag=6760, seconds=0.0)
    Event_250(15, achievement_id=22, flag=6710, seconds=0.0)
    Event_250(16, achievement_id=23, flag=6720, seconds=0.0)
    Event_250(17, achievement_id=24, flag=6730, seconds=0.0)
    Event_250(20, achievement_id=4, flag=13300800, seconds=0.0)
    Event_250(21, achievement_id=5, flag=13900800, seconds=0.0)
    Event_250(22, achievement_id=6, flag=13700800, seconds=0.0)
    Event_250(23, achievement_id=7, flag=13410830, seconds=0.0)
    Event_250(24, achievement_id=27, flag=14000800, seconds=0.0)
    Event_250(25, achievement_id=28, flag=13000800, seconds=0.0)
    Event_250(26, achievement_id=29, flag=13100800, seconds=0.0)
    Event_250(27, achievement_id=30, flag=13300850, seconds=0.0)
    Event_250(28, achievement_id=31, flag=13500800, seconds=0.0)
    Event_250(29, achievement_id=32, flag=13800800, seconds=0.0)
    Event_250(30, achievement_id=33, flag=13700850, seconds=0.0)
    Event_250(31, achievement_id=34, flag=13000890, seconds=0.0)
    Event_250(32, achievement_id=35, flag=13010800, seconds=0.0)
    Event_250(33, achievement_id=36, flag=13800830, seconds=0.0)
    Event_250(34, achievement_id=37, flag=13000830, seconds=0.0)
    Event_250(35, achievement_id=38, flag=14000830, seconds=0.0)
    Event_250(36, achievement_id=39, flag=13200800, seconds=0.0)
    Event_250(37, achievement_id=40, flag=13200850, seconds=0.0)
    Event_6099()
    Event_6100(0, flag=6100, flag_1=13300800)
    Event_6100(1, flag=6101, flag_1=13900800)
    Event_6100(2, flag=6102, flag_1=13700800)
    Event_6100(3, flag=6103, flag_1=13410830)
    Event_6100(4, flag=6104, flag_1=14000800)
    Event_6100(5, flag=6105, flag_1=13000800)
    Event_6100(6, flag=6106, flag_1=13300850)
    Event_6100(7, flag=6107, flag_1=13500800)
    Event_6100(8, flag=6108, flag_1=13800800)
    Event_6100(9, flag=6109, flag_1=13700850)
    Event_6100(10, flag=6110, flag_1=13000890)
    Event_6100(11, flag=6111, flag_1=13010800)
    Event_6100(12, flag=6112, flag_1=110)
    Event_702()
    Event_710()
    Event_9510()
    Event_9511()
    Event_9512()
    Event_9520(0, special_effect=4410, gesture_id=8, item_id=9013, flag=6058)
    Event_9525(0, special_effect=4430, gesture_id=4, item_id=9005, flag=6054)
    Event_9530(0, special_effect=4420, gesture_id=18, item_id=9020, flag=6068)
    Event_9540(0, gesture_id=15, item_id=9017, flag=6065)
    Event_9100(0, flag=70000007)
    Event_9101(0, flag=70000008)
    Event_9102(0, flag=70000012)
    Event_9103(0, flag=70000013)
    Event_9104(0, flag=70000017)
    Event_9105(0, flag=70000019, flag_1=70000020, flag_2=70000021)
    Event_9111(0, flag=70000022, flag_1=70000023)
    Event_9106(0, flag=70000000)
    Event_9107(0, flag=70000001)
    Event_9108(0, flag=70000002)
    Event_9109(0, flag=70000003)
    Event_9110(0, flag=70000004)
    Event_9112(0, flag=70000005)
    Event_9113(0, flag=70000030)
    Event_9114(0, flag=70000031)
    Event_9120(
        0,
        flag=74000756,
        flag_1=74000760,
        flag_2=74000760,
        bit_count=1,
        bit_count_1=1,
        max_value__value=1,
        left=0,
    )
    Event_9120(
        1,
        flag=74000591,
        flag_1=74000552,
        flag_2=74000592,
        bit_count=3,
        bit_count_1=3,
        max_value__value=3,
        left=0,
    )
    Event_9120(
        2,
        flag=74000552,
        flag_1=74000553,
        flag_2=74000592,
        bit_count=3,
        bit_count_1=3,
        max_value__value=6,
        left=0,
    )
    Event_9120(
        3,
        flag=74000303,
        flag_1=74000316,
        flag_2=74000316,
        bit_count=1,
        bit_count_1=1,
        max_value__value=1,
        left=1,
    )
    Event_9120(
        4,
        flag=74000306,
        flag_1=74000318,
        flag_2=74000318,
        bit_count=1,
        bit_count_1=1,
        max_value__value=1,
        left=1,
    )
    Event_9120(
        5,
        flag=74000921,
        flag_1=74000925,
        flag_2=74000925,
        bit_count=1,
        bit_count_1=1,
        max_value__value=1,
        left=1,
    )
    Event_9120(
        6,
        flag=74000916,
        flag_1=74000913,
        flag_2=74000913,
        bit_count=1,
        bit_count_1=1,
        max_value__value=1,
        left=1,
    )
    Event_9120(
        7,
        flag=73500265,
        flag_1=73500264,
        flag_2=73500264,
        bit_count=1,
        bit_count_1=1,
        max_value__value=1,
        left=0,
    )
    Event_9016()
    Event_9011(0, flag=74000132)
    Event_9014()
    Event_9018()
    Event_9019(0, flag=74000669)
    Event_9015()
    Event_6900()
    Event_9020(0, flag=73500300, first_flag=1621, last_flag=1634, flag_1=6951, area_id=35, block_id=0)
    Event_9020(1, flag=14100511, first_flag=14100512, last_flag=14100512, flag_1=6952, area_id=41, block_id=0)
    Event_9020(2, flag=14500161, first_flag=14500162, last_flag=14500162, flag_1=6952, area_id=45, block_id=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_231()
    Event_232()
    Event_701()
    Event_700()
    Event_9012()
    Event_741()
    Event_740()
    Event_9080(0, item_type=2, item=10040, flag=6700)
    Event_9080(1, item_type=2, item=10050, flag=6710)
    Event_9080(2, item_type=2, item=10020, flag=6720)
    Event_9080(3, item_type=2, item=10030, flag=6730)
    Event_9080(4, item_type=2, item=10070, flag=6740)
    Event_9080(5, item_type=2, item=10000, flag=6750)
    Event_9080(6, item_type=2, item=10080, flag=6760)
    Event_9080(7, item_type=2, item=10060, flag=6770)
    Event_9080(10, item_type=3, item=520, flag=6790)
    Event_9080(11, item_type=3, item=521, flag=6791)
    Event_9080(12, item_type=3, item=522, flag=6792)
    Event_9080(13, item_type=3, item=523, flag=6793)
    Event_9080(14, item_type=3, item=524, flag=6794)
    Event_9080(15, item_type=3, item=102, flag=6780)
    Event_9080(16, item_type=3, item=101, flag=6781)
    Event_9080(17, item_type=3, item=108, flag=6782)
    Event_9080(18, item_type=2, item=10090, flag=6830)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2052):
        return
    AND_1.Add(FlagEnabled(6400))
    AND_1.Add(FlagDisabled(14000100))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    RemoveGoodFromPlayer(item=115, quantity=1)
    RemoveGoodFromPlayer(item=384, quantity=1)
    RemoveGoodFromPlayer(item=386, quantity=1)
    RemoveGoodFromPlayer(item=390, quantity=1)
    RemoveGoodFromPlayer(item=490, quantity=8)
    RemoveGoodFromPlayer(item=2001, quantity=1)
    RemoveGoodFromPlayer(item=2005, quantity=1)
    RemoveGoodFromPlayer(item=2007, quantity=1)
    RemoveGoodFromPlayer(item=2008, quantity=1)
    RemoveGoodFromPlayer(item=2009, quantity=1)
    RemoveGoodFromPlayer(item=2010, quantity=1)
    RemoveGoodFromPlayer(item=2011, quantity=1)
    RemoveGoodFromPlayer(item=2012, quantity=1)
    RemoveGoodFromPlayer(item=2013, quantity=1)
    RemoveGoodFromPlayer(item=2014, quantity=1)
    RemoveGoodFromPlayer(item=2015, quantity=1)
    RemoveGoodFromPlayer(item=2102, quantity=1)
    RemoveGoodFromPlayer(item=2103, quantity=1)
    RemoveGoodFromPlayer(item=2104, quantity=1)
    RemoveGoodFromPlayer(item=2105, quantity=1)
    RemoveGoodFromPlayer(item=2106, quantity=1)
    RemoveGoodFromPlayer(item=2107, quantity=1)
    RemoveGoodFromPlayer(item=2108, quantity=1)
    RemoveGoodFromPlayer(item=2109, quantity=1)
    RemoveGoodFromPlayer(item=2110, quantity=1)
    RemoveGoodFromPlayer(item=2111, quantity=1)
    RemoveGoodFromPlayer(item=2112, quantity=1)
    RemoveGoodFromPlayer(item=2113, quantity=1)
    RemoveGoodFromPlayer(item=2114, quantity=1)
    RemoveGoodFromPlayer(item=2115, quantity=1)
    RemoveGoodFromPlayer(item=2116, quantity=1)
    RemoveGoodFromPlayer(item=2117, quantity=1)
    RemoveGoodFromPlayer(item=2119, quantity=1)
    RemoveGoodFromPlayer(item=2120, quantity=1)
    RemoveGoodFromPlayer(item=2121, quantity=1)
    RemoveGoodFromPlayer(item=2123, quantity=1)
    RemoveGoodFromPlayer(item=2124, quantity=1)
    RemoveGoodFromPlayer(item=2125, quantity=1)
    RemoveGoodFromPlayer(item=2126, quantity=1)
    RemoveGoodFromPlayer(item=2127, quantity=1)
    RemoveGoodFromPlayer(item=2128, quantity=1)
    RemoveGoodFromPlayer(item=2129, quantity=1)
    RemoveGoodFromPlayer(item=2130, quantity=1)
    RemoveGoodFromPlayer(item=2131, quantity=1)
    RemoveGoodFromPlayer(item=2132, quantity=1)
    RemoveGoodFromPlayer(item=2133, quantity=1)
    RemoveGoodFromPlayer(item=2134, quantity=1)
    RemoveGoodFromPlayer(item=2135, quantity=1)
    RemoveGoodFromPlayer(item=2137, quantity=1)
    RemoveGoodFromPlayer(item=2138, quantity=1)
    RemoveGoodFromPlayer(item=2139, quantity=1)
    RemoveGoodFromPlayer(item=2140, quantity=1)
    RemoveGoodFromPlayer(item=2142, quantity=1)
    RemoveGoodFromPlayer(item=2144, quantity=1)
    RemoveGoodFromPlayer(item=2145, quantity=1)
    RemoveGoodFromPlayer(item=2146, quantity=1)
    RemoveGoodFromPlayer(item=2147, quantity=1)
    RemoveGoodFromPlayer(item=2148, quantity=1)
    RemoveGoodFromPlayer(item=2149, quantity=1)
    RemoveGoodFromPlayer(item=2150, quantity=1)
    RemoveGoodFromPlayer(item=2151, quantity=1)
    RemoveGoodFromPlayer(item=2152, quantity=1)
    RemoveGoodFromPlayer(item=2154, quantity=1)
    RemoveGoodFromPlayer(item=2155, quantity=1)
    RemoveGoodFromPlayer(item=2156, quantity=1)
    RemoveGoodFromPlayer(item=2157, quantity=1)
    RemoveGoodFromPlayer(item=2158, quantity=1)
    DisableFlag(6400)

    # --- Label 0 --- #
    DefineLabel(0)


@ContinueOnRest(130)
def Event_130(_, area_id: uchar, block_id: uchar, collision: int, ceremony_id: ushort, achievement_id: int):
    """Event 130"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(InsideMap(game_map=(area_id, block_id)))
    AND_1.Add(PlayerStandingOnCollision(collision))
    AND_2.Add(InsideMap(game_map=FIRELINK_SHRINE))
    SkipLinesIfConditionFalse(1, AND_2)
    AND_1.Add(MapInCeremony(game_map=(area_id, block_id), ceremony_id=ceremony_id))
    
    MAIN.Await(AND_1)
    
    if ValueEqual(left=achievement_id, right=-1):
        return
    AwardAchievement(achievement_id=achievement_id)
    End()


@RestartOnRest(200)
def Event_200():
    """Event 200"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    EnableFlag(201)


@RestartOnRest(230)
def Event_230():
    """Event 230"""
    if FlagEnabled(230):
        return
    AND_1.Add(FlagEnabled(9314))
    AND_1.Add(FlagEnabled(9318))
    
    MAIN.Await(AND_1)
    
    SetMapCeremony(game_map=HIGH_WALL_OF_LOTHRIC, ceremony_id=10)
    SetMapCeremony(game_map=LOTHRIC_CASTLE, ceremony_id=10)
    SetMapCeremony(game_map=GRAND_ARCHIVES, ceremony_id=10)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=10)
    SetMapCeremony(game_map=FARRON_KEEP, ceremony_id=10)
    SetMapCeremony(game_map=CATHEDRAL_OF_THE_DEEP, ceremony_id=10)
    EnableFlag(230)


@RestartOnRest(231)
def Event_231():
    """Event 231"""
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    if AND_1:
        return
    SetMapCeremony(game_map=FIRELINK_SHRINE, ceremony_id=10)
    End()


@ContinueOnRest(232)
def Event_232():
    """Event 232"""
    GotoIfFlagEnabled(Label.L1, flag=8221)
    GotoIfFlagEnabled(Label.L0, flag=230)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=10)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(InsideMap(game_map=HIGH_WALL_OF_LOTHRIC))
    OR_1.Add(InsideMap(game_map=LOTHRIC_CASTLE))
    OR_1.Add(InsideMap(game_map=GRAND_ARCHIVES))
    OR_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L2, flag=230)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=20)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=30)
    Goto(Label.L3)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_1.Add(OutsideMap(game_map=HIGH_WALL_OF_LOTHRIC))
    AND_1.Add(OutsideMap(game_map=LOTHRIC_CASTLE))
    AND_1.Add(OutsideMap(game_map=GRAND_ARCHIVES))
    AND_1.Add(OutsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    Restart()


@ContinueOnRest(250)
def Event_250(_, achievement_id: int, flag: int, seconds: float):
    """Event 250"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    AwardAchievement(achievement_id=achievement_id)


@ContinueOnRest(6100)
def Event_6100(_, flag: int, flag_1: int):
    """Event 6100"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@ContinueOnRest(700)
def Event_700():
    """Event 700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2052):
        return
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(50006020)
    EnableFlag(9215)
    SetPlayerRemainingYoelLevels(level_count=5)
    EnableFlag(70000125)
    EnableFlag(70000128)
    EnableFlag(70000129)
    OR_15.Add(PlayerClass(ClassType.Sorcerer))
    SkipLinesIfConditionFalse(1, OR_15)
    EnableFlag(74000587)
    OR_14.Add(PlayerClass(ClassType.Pyromancer))
    SkipLinesIfConditionFalse(1, OR_14)
    EnableFlag(74000465)
    EnableFlag(50006162)
    EnableFlag(50006163)
    EnableFlag(73501010)
    EnableFlag(73501020)
    EnableFlag(73501030)
    EnableFlag(73501040)
    EnableFlag(73501050)
    OR_13.Add(NewGameCycleGreaterThanOrEqual(completion_count=1))
    SkipLinesIfConditionFalse(1, OR_13)
    EnableFlag(70000900)
    AND_6.Add(NewGameCycleGreaterThanOrEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_6)
    EnableFlag(56)
    End()
    AND_5.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_5)
    EnableFlag(55)
    End()
    AND_4.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_4)
    EnableFlag(54)
    End()
    AND_3.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(53)
    End()
    AND_2.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(52)
    End()
    AND_1.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(51)
    End()
    EnableFlag(50)
    End()


@ContinueOnRest(701)
def Event_701():
    """Event 701"""
    DisableFlag(6000)
    EnableFlag(6001)


@ContinueOnRest(702)
def Event_702():
    """Event 702"""
    if FlagEnabled(6600):
        return
    
    MAIN.Await(FlagEnabled(6600))
    
    EnableFlag(703)


@ContinueOnRest(710)
def Event_710():
    """Event 710"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(PlayerHasGood(2014))
    if AND_15:
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9314))
    AND_1.Add(FlagEnabled(9318))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3702890))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3902890))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4900)
    AddSpecialEffect(PLAYER, 4901)
    GotoIfInsideMap(Label.L0, game_map=IRITHYLL)
    GotoIfInsideMap(Label.L1, game_map=PROFANED_CAPITAL)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    EnableFlag(13700002)
    AND_8.Add(FlagEnabled(13000896))
    AND_8.Add(FlagDisabled(13000890))
    SkipLinesIfConditionTrue(2, AND_8)
    PlayCutsceneAndMoveSpecificPlayer_WithOtherRegion(
        cutscene_id=37000030,
        cutscene_flags=0,
        move_to_region=3002100,
        game_map=HIGH_WALL_OF_LOTHRIC,
        player_id=10000,
        other_region=3002890,
    )
    SkipLines(1)
    PlayCutsceneAndMoveSpecificPlayer_WithOtherRegion(
        cutscene_id=37000030,
        cutscene_flags=0,
        move_to_region=3002890,
        game_map=HIGH_WALL_OF_LOTHRIC,
        player_id=10000,
        other_region=3002890,
    )
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagRangeAllDisabled(Label.L19, flag_range=(1388, 1389))
    OR_2.Add(FlagEnabled(73900164))
    OR_2.Add(FlagEnabled(1398))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=3902890))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)

    # --- Label 19 --- #
    DefineLabel(19)
    Wait(3.0)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(13900001)
    AND_9.Add(FlagEnabled(13000896))
    AND_9.Add(FlagDisabled(13000890))
    SkipLinesIfConditionTrue(2, AND_9)
    PlayCutsceneAndMoveSpecificPlayer_WithOtherRegion(
        cutscene_id=39000030,
        cutscene_flags=0,
        move_to_region=3002100,
        game_map=HIGH_WALL_OF_LOTHRIC,
        player_id=10000,
        other_region=3002890,
    )
    SkipLines(1)
    PlayCutsceneAndMoveSpecificPlayer_WithOtherRegion(
        cutscene_id=39000030,
        cutscene_flags=0,
        move_to_region=3002890,
        game_map=HIGH_WALL_OF_LOTHRIC,
        player_id=10000,
        other_region=3002890,
    )
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(711)
    WaitFrames(frames=0)
    RemoveSpecialEffect(PLAYER, 4900)
    RemoveSpecialEffect(PLAYER, 4901)
    End()


@ContinueOnRest(730)
def Event_730():
    """Event 730"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 100))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    RemoveSpecialEffect(PLAYER, 11907)
    Wait(1.0)
    Restart()


@ContinueOnRest(740)
def Event_740():
    """Event 740"""
    DisableNetworkSync()
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@ContinueOnRest(741)
def Event_741():
    """Event 741"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2052):
        return
    DisableFlag(74000013)
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_1.Add(MapInCeremony(game_map=FIRELINK_SHRINE, ceremony_id=10))
    
    MAIN.Await(not AND_1)
    
    EnableFlag(743)
    AND_2.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_2.Add(MapInCeremony(game_map=FIRELINK_SHRINE, ceremony_id=10))
    AND_3.Add(PlayerStandingOnCollision(4004120))
    AND_2.Add(not AND_3)
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(750)
def Event_750():
    """Event 750"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    RemoveGoodFromPlayer(item=10110, quantity=99)
    RemoveGoodFromPlayer(item=10120, quantity=99)
    RemoveGoodFromPlayer(item=10200, quantity=99)
    RemoveGoodFromPlayer(item=10210, quantity=99)
    RemoveGoodFromPlayer(item=10220, quantity=99)
    RemoveGoodFromPlayer(item=10230, quantity=99)


@ContinueOnRest(970)
def Event_970(_, flag: int, item_lot: int, item_lot_1: int, item_lot_2: int):
    """Event 970"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    if ValueNotEqual(left=item_lot, right=0):
        AwardItemLot(item_lot, host_only=True)
    DisableNetworkSync()
    Wait(5.0)
    if ValueNotEqual(left=item_lot_1, right=0):
        AwardItemLot(item_lot_1, host_only=True)
    if ValueNotEqual(left=item_lot_2, right=0):
        AwardItemLot(item_lot_2, host_only=True)


@ContinueOnRest(6099)
def Event_6099():
    """Event 6099"""
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(6050))
    AND_1.Add(FlagEnabled(6051))
    AND_1.Add(FlagEnabled(6054))
    AND_1.Add(FlagEnabled(6056))
    AND_1.Add(FlagEnabled(6057))
    AND_1.Add(FlagEnabled(6058))
    AND_1.Add(FlagEnabled(6059))
    AND_1.Add(FlagEnabled(6062))
    AND_1.Add(FlagEnabled(6065))
    AND_1.Add(FlagEnabled(6066))
    AND_1.Add(FlagEnabled(6067))
    AND_1.Add(FlagEnabled(6068))
    AND_1.Add(FlagEnabled(6069))
    AND_1.Add(FlagEnabled(6072))
    AND_1.Add(FlagEnabled(6073))
    AND_1.Add(FlagEnabled(6074))
    AND_1.Add(FlagEnabled(6075))
    AND_1.Add(FlagEnabled(6076))
    AND_1.Add(FlagEnabled(6077))
    AND_1.Add(FlagEnabled(6078))
    AND_1.Add(FlagEnabled(6079))
    AND_1.Add(FlagEnabled(6080))
    AND_1.Add(FlagEnabled(6081))
    AND_1.Add(FlagEnabled(6082))
    AND_1.Add(FlagEnabled(6083))
    AND_1.Add(FlagEnabled(6084))
    
    MAIN.Await(AND_1)
    
    AwardAchievement(achievement_id=14)
    EnableFlag(6099)


@ContinueOnRest(6900)
def Event_6900():
    """Event 6900"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerDoesNotHaveGood(170))
    AND_1.Add(PlayerDoesNotHaveGood(171))
    if AND_1:
        return
    EnableFlag(6030)


@ContinueOnRest(9510)
def Event_9510():
    """Event 9510"""
    if ThisEventSlotFlagEnabled():
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13500193))
    AND_1.Add(FlagEnabled(8240))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9510)


@ContinueOnRest(9511)
def Event_9511():
    """Event 9511"""
    if ThisEventSlotFlagEnabled():
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13500194))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9511)


@ContinueOnRest(9512)
def Event_9512():
    """Event 9512"""
    if ThisEventSlotFlagEnabled():
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13700194))
    AND_1.Add(FlagEnabled(13300184))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9512)


@RestartOnRest(9520)
def Event_9520(_, special_effect: int, gesture_id: ushort, item_id: int, flag: int):
    """Event 9520"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(13304194))
    
    AICommand(3300194, command_id=99, command_slot=2)
    ReplanAI(3300194)
    
    MAIN.Await(CharacterHasSpecialEffect(3300194, special_effect))
    
    AICommand(3300194, command_id=-1, command_slot=2)
    ReplanAI(3300194)
    if FlagEnabled(flag):
        return
    AwardGestureItem(gesture_id=gesture_id, item_type=ItemType.Good, item_id=item_id)
    EnableFlag(flag)


@RestartOnRest(9525)
def Event_9525(_, special_effect: int, gesture_id: ushort, item_id: int, flag: int):
    """Event 9525"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(13304195))
    OR_1.Add(FlagEnabled(13704192))
    OR_1.Add(FlagEnabled(14104190))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(13304195):
        AICommand(3300195, command_id=99, command_slot=2)
        ReplanAI(3300195)
    if FlagEnabled(13704192):
        AICommand(3700192, command_id=99, command_slot=2)
        ReplanAI(3700192)
    if FlagEnabled(14104190):
        AICommand(4100190, command_id=99, command_slot=2)
        ReplanAI(4100190)
    OR_2.Add(CharacterHasSpecialEffect(3300195, special_effect))
    OR_2.Add(CharacterHasSpecialEffect(3700192, special_effect))
    OR_2.Add(CharacterHasSpecialEffect(4100191, special_effect))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(13304195):
        AICommand(3300195, command_id=-1, command_slot=2)
        ReplanAI(3300195)
    if FlagEnabled(13704192):
        AICommand(3700192, command_id=-1, command_slot=2)
        ReplanAI(3700192)
    if FlagEnabled(14104191):
        AICommand(4100190, command_id=-1, command_slot=2)
        ReplanAI(4100190)
    if FlagEnabled(flag):
        return
    AwardGestureItem(gesture_id=gesture_id, item_type=ItemType.Good, item_id=item_id)
    EnableFlag(flag)


@RestartOnRest(9530)
def Event_9530(_, special_effect: int, gesture_id: ushort, item_id: int, flag: int):
    """Event 9530"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(13304913))
    OR_1.Add(FlagEnabled(13704191))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(13304913):
        AICommand(3300193, command_id=99, command_slot=2)
        ReplanAI(3300193)
    if FlagEnabled(13704191):
        AICommand(3700191, command_id=99, command_slot=2)
        ReplanAI(3700191)
    OR_2.Add(CharacterHasSpecialEffect(3300193, special_effect))
    OR_2.Add(CharacterHasSpecialEffect(3700191, special_effect))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(13304913):
        AICommand(3300193, command_id=-1, command_slot=2)
        ReplanAI(3300193)
    if FlagEnabled(13704191):
        AICommand(3700191, command_id=-1, command_slot=2)
        ReplanAI(3700191)
    if FlagEnabled(flag):
        return
    AwardGestureItem(gesture_id=gesture_id, item_type=ItemType.Good, item_id=item_id)
    EnableFlag(flag)


@RestartOnRest(9540)
def Event_9540(_, gesture_id: ushort, item_id: int, flag: int):
    """Event 9540"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13804196))
    AND_1.Add(FlagDisabled(13805196))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3800196, radius=20.0))
    AND_2.Add(HasAIStatus(3800198, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=3800198, radius=20.0))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(HealthRatio(PLAYER) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_4.Add(OR_1)
    AND_4.Add(AND_3)
    
    MAIN.Await(AND_4)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    AICommand(3800196, command_id=99, command_slot=2)
    ReplanAI(3800196)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_2)
    AICommand(3800198, command_id=99, command_slot=2)
    ReplanAI(3800198)
    Wait(1.0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    AICommand(3800196, command_id=-1, command_slot=2)
    ReplanAI(3800196)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_2)
    AICommand(3800198, command_id=-1, command_slot=2)
    ReplanAI(3800198)
    if FlagEnabled(flag):
        return
    AwardGestureItem(gesture_id=gesture_id, item_type=ItemType.Good, item_id=item_id)
    EnableFlag(flag)


@RestartOnRest(9570)
def Event_9570(_, item_lot: int, special_effect: int):
    """Event 9570"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, special_effect))
    
    AwardItemLot(item_lot, host_only=True)
    Wait(1.5)
    Restart()


@ContinueOnRest(9000)
def Event_9000(_, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 9000"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    OR_2.Add(FlagEnabled(flag_1))
    OR_2.Add(FlagEnabled(flag_2))
    OR_2.Add(FlagEnabled(flag_3))
    
    MAIN.Await(not OR_2)
    
    Restart()


@ContinueOnRest(9002)
def Event_9002(_, flag: int):
    """Event 9002"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableFlag(flag)
    EnableFlag(70000050)
    EnableFlag(70000051)
    EnableFlag(70000052)
    EnableFlag(70000053)
    EnableFlag(70000054)
    EnableFlag(70000055)
    EnableFlag(70000056)
    EnableFlag(70000057)
    EnableFlag(70000058)
    EnableFlag(70000059)
    EnableFlag(70000060)
    EnableFlag(70000061)
    EnableFlag(70000062)
    EnableFlag(70000063)
    EnableFlag(70000064)
    EnableFlag(70000065)
    EnableFlag(70000066)
    EnableFlag(70000067)
    EnableFlag(70000068)
    EnableFlag(70000069)
    EnableFlag(70000070)
    EnableFlag(70000071)
    EnableFlag(70000072)
    EnableFlag(70000073)
    EnableFlag(70000074)
    EnableFlag(70000075)
    EnableFlag(70000076)
    EnableFlag(70000077)
    EnableFlag(70000078)
    EnableFlag(70000079)
    EnableFlag(70000080)
    EnableFlag(70000081)
    EnableFlag(70000082)
    EnableFlag(70000083)
    EnableFlag(70000084)
    EnableFlag(70000085)
    EnableFlag(70000086)
    EnableFlag(70000087)
    EnableFlag(70000088)
    EnableFlag(70000089)
    EnableFlag(70000090)
    EnableFlag(70000091)
    EnableFlag(70000092)
    EnableFlag(70000093)
    EnableFlag(70000094)
    EnableFlag(70000095)
    EnableFlag(70000096)
    EnableFlag(70000097)
    EnableFlag(70000098)
    EnableFlag(70000099)
    EnableFlag(70001073)
    Restart()


@ContinueOnRest(9004)
def Event_9004(_, flag: int):
    """Event 9004"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1016))
    AND_1.Add(FlagDisabled(70000052))
    AND_2.Add(FlagEnabled(1036))
    AND_2.Add(FlagDisabled(70000053))
    AND_3.Add(FlagEnabled(1056))
    AND_3.Add(FlagDisabled(70000054))
    AND_4.Add(FlagEnabled(1076))
    AND_4.Add(FlagDisabled(70000055))
    AND_5.Add(FlagEnabled(1096))
    AND_5.Add(FlagDisabled(70000056))
    AND_6.Add(FlagEnabled(1116))
    AND_6.Add(FlagDisabled(70000057))
    AND_7.Add(FlagEnabled(1136))
    AND_7.Add(FlagDisabled(70000058))
    AND_8.Add(FlagEnabled(1156))
    AND_8.Add(FlagDisabled(70000059))
    AND_9.Add(FlagEnabled(1176))
    AND_9.Add(FlagDisabled(70000060))
    AND_10.Add(FlagEnabled(1196))
    AND_10.Add(FlagDisabled(70000061))
    AND_11.Add(FlagEnabled(1216))
    AND_11.Add(FlagDisabled(70000062))
    AND_12.Add(FlagEnabled(1236))
    AND_12.Add(FlagDisabled(70000063))
    AND_13.Add(FlagEnabled(1256))
    AND_13.Add(FlagDisabled(70000064))
    AND_14.Add(FlagEnabled(1276))
    AND_14.Add(FlagDisabled(70000065))
    AND_15.Add(FlagEnabled(1296))
    AND_15.Add(FlagDisabled(70000066))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_10)
    OR_1.Add(AND_11)
    OR_1.Add(AND_12)
    OR_1.Add(AND_13)
    OR_1.Add(AND_14)
    OR_1.Add(AND_15)
    
    MAIN.Await(OR_1)
    
    ClearMainCondition()
    EnableFlag(flag)
    AND_1.Add(FlagEnabled(1016))
    AND_1.Add(FlagDisabled(70000052))
    AND_2.Add(FlagEnabled(1036))
    AND_2.Add(FlagDisabled(70000053))
    AND_3.Add(FlagEnabled(1056))
    AND_3.Add(FlagDisabled(70000054))
    AND_4.Add(FlagEnabled(1076))
    AND_4.Add(FlagDisabled(70000055))
    AND_5.Add(FlagEnabled(1096))
    AND_5.Add(FlagDisabled(70000056))
    AND_6.Add(FlagEnabled(1116))
    AND_6.Add(FlagDisabled(70000057))
    AND_7.Add(FlagEnabled(1136))
    AND_7.Add(FlagDisabled(70000058))
    AND_8.Add(FlagEnabled(1156))
    AND_8.Add(FlagDisabled(70000059))
    AND_9.Add(FlagEnabled(1176))
    AND_9.Add(FlagDisabled(70000060))
    AND_10.Add(FlagEnabled(1196))
    AND_10.Add(FlagDisabled(70000061))
    AND_11.Add(FlagEnabled(1216))
    AND_11.Add(FlagDisabled(70000062))
    AND_12.Add(FlagEnabled(1236))
    AND_12.Add(FlagDisabled(70000063))
    AND_13.Add(FlagEnabled(1256))
    AND_13.Add(FlagDisabled(70000064))
    AND_14.Add(FlagEnabled(1276))
    AND_14.Add(FlagDisabled(70000065))
    AND_15.Add(FlagEnabled(1296))
    AND_15.Add(FlagDisabled(70000066))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_10)
    OR_1.Add(AND_11)
    OR_1.Add(AND_12)
    OR_1.Add(AND_13)
    OR_1.Add(AND_14)
    OR_1.Add(AND_15)
    
    MAIN.Await(not OR_1)
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(9005)
def Event_9005(_, flag: int):
    """Event 9005"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1316))
    AND_1.Add(FlagDisabled(70000067))
    AND_2.Add(FlagEnabled(1336))
    AND_2.Add(FlagDisabled(70000068))
    AND_3.Add(FlagEnabled(1356))
    AND_3.Add(FlagDisabled(70000069))
    AND_4.Add(FlagEnabled(1376))
    AND_4.Add(FlagDisabled(70000070))
    AND_5.Add(FlagEnabled(1396))
    AND_5.Add(FlagDisabled(70000071))
    AND_6.Add(FlagEnabled(1416))
    AND_6.Add(FlagDisabled(70000072))
    AND_7.Add(FlagEnabled(1436))
    AND_7.Add(FlagDisabled(70000073))
    AND_8.Add(FlagEnabled(1456))
    AND_8.Add(FlagDisabled(70000074))
    AND_9.Add(FlagEnabled(1476))
    AND_9.Add(FlagDisabled(70000075))
    AND_10.Add(FlagEnabled(1496))
    AND_10.Add(FlagDisabled(70000076))
    AND_11.Add(FlagEnabled(1516))
    AND_11.Add(FlagDisabled(70000077))
    AND_12.Add(FlagEnabled(1536))
    AND_12.Add(FlagDisabled(70000078))
    AND_13.Add(FlagEnabled(1556))
    AND_13.Add(FlagDisabled(70000079))
    AND_14.Add(FlagEnabled(1576))
    AND_14.Add(FlagDisabled(70000080))
    AND_15.Add(FlagEnabled(1596))
    AND_15.Add(FlagDisabled(70000081))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_10)
    OR_1.Add(AND_11)
    OR_1.Add(AND_12)
    OR_1.Add(AND_13)
    OR_1.Add(AND_14)
    OR_1.Add(AND_15)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    ClearMainCondition()
    AND_1.Add(FlagEnabled(1316))
    AND_1.Add(FlagDisabled(70000067))
    AND_2.Add(FlagEnabled(1336))
    AND_2.Add(FlagDisabled(70000068))
    AND_3.Add(FlagEnabled(1356))
    AND_3.Add(FlagDisabled(70000069))
    AND_4.Add(FlagEnabled(1376))
    AND_4.Add(FlagDisabled(70000070))
    AND_5.Add(FlagEnabled(1396))
    AND_5.Add(FlagDisabled(70000071))
    AND_6.Add(FlagEnabled(1416))
    AND_6.Add(FlagDisabled(70000072))
    AND_7.Add(FlagEnabled(1436))
    AND_7.Add(FlagDisabled(70000073))
    AND_8.Add(FlagEnabled(1456))
    AND_8.Add(FlagDisabled(70000074))
    AND_9.Add(FlagEnabled(1476))
    AND_9.Add(FlagDisabled(70000075))
    AND_10.Add(FlagEnabled(1496))
    AND_10.Add(FlagDisabled(70000076))
    AND_11.Add(FlagEnabled(1516))
    AND_11.Add(FlagDisabled(70000077))
    AND_12.Add(FlagEnabled(1536))
    AND_12.Add(FlagDisabled(70000078))
    AND_13.Add(FlagEnabled(1556))
    AND_13.Add(FlagDisabled(70000079))
    AND_14.Add(FlagEnabled(1576))
    AND_14.Add(FlagDisabled(70000080))
    AND_15.Add(FlagEnabled(1596))
    AND_15.Add(FlagDisabled(70000081))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_10)
    OR_1.Add(AND_11)
    OR_1.Add(AND_12)
    OR_1.Add(AND_13)
    OR_1.Add(AND_14)
    OR_1.Add(AND_15)
    
    MAIN.Await(not OR_1)
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(9006)
def Event_9006(_, flag: int):
    """Event 9006"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1816))
    AND_1.Add(FlagDisabled(70001073))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    ClearMainCondition()
    AND_1.Add(FlagEnabled(1816))
    AND_1.Add(FlagDisabled(70001073))
    OR_1.Add(AND_1)
    
    MAIN.Await(not OR_1)
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(9010)
def Event_9010():
    """Event 9010"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(70000061))
    
    if FlagEnabled(74000295):
        DisableFlag(74000295)
        Goto(Label.L20)
    if FlagEnabled(74000294):
        DisableFlag(74000294)
        Goto(Label.L20)
    if FlagEnabled(74000293):
        DisableFlag(74000293)
        Goto(Label.L20)
    if FlagEnabled(74000292):
        DisableFlag(74000292)
        Goto(Label.L20)
    if FlagEnabled(74000291):
        DisableFlag(74000291)
        Goto(Label.L20)
    if FlagEnabled(74000290):
        DisableFlag(74000290)
        DisableNetworkConnectedFlagRange(flag_range=(1195, 1199))
        SetNetworkConnectedFlagState(flag=1195, state=FlagSetting.On)
        Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(70000061)
    Restart()


@ContinueOnRest(9011)
def Event_9011(_, flag: int):
    """Event 9011"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(700))
    AND_1.Add(FlagDisabled(50006020))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=14000110)
    AND_2.Add(FlagEnabled(9307))
    AND_2.Add(FlagEnabled(9309))
    AND_2.Add(FlagEnabled(9314))
    AND_2.Add(FlagEnabled(9318))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    if FlagDisabled(9307):
        OR_1.Add(FlagEnabled(9307))
    if FlagDisabled(9309):
        OR_1.Add(FlagEnabled(9309))
    if FlagDisabled(9314):
        OR_1.Add(FlagEnabled(9314))
    if FlagDisabled(9318):
        OR_1.Add(FlagEnabled(9318))
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(14000110))
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(FlagEnabled(50006020))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=OR_2)
    DisableFlag(flag)
    Restart()
    EnableFlag(flag)
    Restart()


@ContinueOnRest(9012)
def Event_9012():
    """Event 9012"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2052):
        return
    
    MAIN.Await(PlayerGender(gender=Gender.Male))
    
    SetNetworkConnectedFlagState(flag=9013, state=FlagSetting.On)
    
    MAIN.Await(PlayerGender(gender=Gender.Female))
    
    SetNetworkConnectedFlagState(flag=9013, state=FlagSetting.Off)
    Restart()


@RestartOnRest(9014)
def Event_9014():
    """Event 9014"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=9014)
    GotoIfFlagDisabled(Label.L0, flag=13300761)
    DisplayDialog(text=13007000, anchor_entity=PLAYER, display_distance=0.0, number_buttons=NumberButtons.OneButton)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(9014))
    
    EnableFlag(9014)


@ContinueOnRest(9015)
def Event_9015():
    """Event 9015"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(70000118):
        return
    OR_1.Add(FlagEnabled(1124))
    OR_1.Add(FlagEnabled(1126))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(9303))
    AND_1.Add(FlagEnabled(9314))
    
    MAIN.Await(AND_1)
    
    EnableFlag(70000118)


@RestartOnRest(9016)
def Event_9016():
    """Event 9016"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(9017)
    
    MAIN.Await(PlayerClass(ClassType.Cleric))
    
    EnableFlag(9017)
    AND_1.Add(PlayerClass(ClassType.Cleric))
    
    MAIN.Await(not AND_1)
    
    Restart()


@RestartOnRest(9018)
def Event_9018():
    """Event 9018"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(73300202):
        return
    OR_1.Add(FlagEnabled(13204190))
    OR_1.Add(FlagEnabled(13005710))
    
    MAIN.Await(OR_1)
    
    EnableFlag(73300202)


@RestartOnRest(9019)
def Event_9019(_, flag: int):
    """Event 9019"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(13304192))
    OR_1.Add(FlagEnabled(13014192))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)


@ContinueOnRest(9020)
def Event_9020(_, flag: int, first_flag: int, last_flag: int, flag_1: int, area_id: uchar, block_id: uchar):
    """Event 9020"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag))
    DisableFlag(flag)
    OR_1.Add(OutsideMap(game_map=(area_id, block_id)))
    OR_1.Add(FlagEnabled(74000013))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_2.Add(OutsideMap(game_map=(area_id, block_id)))
    OR_2.Add(FlagEnabled(74000013))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(OR_2)
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9080)
def Event_9080(_, item_type: uchar, item: int, flag: int):
    """Event 9080"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2052):
        return
    if ThisEventSlotFlagEnabled():
        return
    IfPlayerHasItem(AND_1, item, item_type=item_type, including_storage=True)
    if AND_1:
        return
    DisableFlag(flag)


@ContinueOnRest(9100)
def Event_9100(_, flag: int):
    """Event 9100"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(1103))
    
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(1103))
    
    Restart()


@ContinueOnRest(9101)
def Event_9101(_, flag: int):
    """Event 9101"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(InsideMap(game_map=GRAND_ARCHIVES))
    OR_1.Add(InsideMap(game_map=LOTHRIC_CASTLE))
    OR_1.Add(InsideMap(game_map=FARRON_KEEP))
    OR_1.Add(InsideMap(game_map=CATHEDRAL_OF_THE_DEEP))
    
    MAIN.Await(OR_1)
    
    GotoIfInsideMap(Label.L0, game_map=GRAND_ARCHIVES)
    GotoIfInsideMap(Label.L1, game_map=LOTHRIC_CASTLE)
    GotoIfInsideMap(Label.L2, game_map=FARRON_KEEP)
    GotoIfInsideMap(Label.L3, game_map=CATHEDRAL_OF_THE_DEEP)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(FlagEnabled(1128))
    AND_1.Add(OR_2)
    AND_1.Add(FlagDisabled(73500150))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    
    MAIN.Await(OutsideMap(game_map=GRAND_ARCHIVES))
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(FlagEnabled(1128))
    AND_2.Add(OR_3)
    AND_2.Add(FlagDisabled(73500150))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    
    MAIN.Await(OutsideMap(game_map=LOTHRIC_CASTLE))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    OR_4.Add(FlagEnabled(1124))
    OR_4.Add(FlagEnabled(1126))
    OR_4.Add(FlagEnabled(1128))
    AND_3.Add(OR_4)
    AND_3.Add(FlagDisabled(73500150))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag)
    
    MAIN.Await(OutsideMap(game_map=FARRON_KEEP))
    
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    OR_5.Add(FlagEnabled(1124))
    OR_5.Add(FlagEnabled(1126))
    OR_5.Add(FlagEnabled(1128))
    AND_4.Add(OR_5)
    AND_4.Add(FlagDisabled(73500150))
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag)
    
    MAIN.Await(OutsideMap(game_map=CATHEDRAL_OF_THE_DEEP))
    
    Restart()


@ContinueOnRest(9102)
def Event_9102(_, flag: int):
    """Event 9102"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(InsideMap(game_map=UNDEAD_SETTLEMENT))
    OR_1.Add(InsideMap(game_map=IRITHYLL))
    
    MAIN.Await(OR_1)
    
    GotoIfInsideMap(Label.L0, game_map=UNDEAD_SETTLEMENT)
    GotoIfInsideMap(Label.L1, game_map=IRITHYLL)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1202):
        EnableFlag(flag)
    
    MAIN.Await(OutsideMap(game_map=UNDEAD_SETTLEMENT))
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1204):
        EnableFlag(flag)
    
    MAIN.Await(OutsideMap(game_map=IRITHYLL))
    
    Restart()


@ContinueOnRest(9103)
def Event_9103(_, flag: int):
    """Event 9103"""
    if PlayerNotInOwnWorld():
        return RESTART
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(1223))
    
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(1223))
    
    Restart()


@ContinueOnRest(9104)
def Event_9104(_, flag: int):
    """Event 9104"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(1301))
    OR_1.Add(FlagEnabled(1303))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1295))
    AND_1.Add(FlagDisabled(73101710))
    AND_1.Add(FlagDisabled(73101720))
    AND_1.Add(FlagDisabled(73101730))
    AND_1.Add(FlagDisabled(73101740))
    AND_1.Add(FlagDisabled(73101750))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    OR_2.Add(FlagEnabled(1301))
    OR_2.Add(FlagEnabled(1303))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1295))
    AND_2.Add(FlagDisabled(73101710))
    AND_2.Add(FlagDisabled(73101720))
    AND_2.Add(FlagDisabled(73101730))
    AND_2.Add(FlagDisabled(73101740))
    AND_2.Add(FlagDisabled(73101750))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9105)
def Event_9105(_, flag: int, flag_1: int, flag_2: int):
    """Event 9105"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    AND_1.Add(FlagEnabled(1341))
    AND_1.Add(FlagDisabled(9311))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L10, flag=9013)
    EnableFlag(flag)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(flag_2)
    AND_2.Add(FlagEnabled(1341))
    AND_2.Add(FlagDisabled(9311))
    
    MAIN.Await(not AND_2)
    
    Restart()


@RestartOnRest(9106)
def Event_9106(_, flag: int):
    """Event 9106"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1130))
    AND_1.Add(FlagDisabled(1138))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(1130))
    AND_2.Add(FlagDisabled(1138))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9107)
def Event_9107(_, flag: int):
    """Event 9107"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1042))
    AND_1.Add(FlagEnabled(1055))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(1042))
    AND_2.Add(FlagEnabled(1055))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9108)
def Event_9108(_, flag: int):
    """Event 9108"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    AND_1.Add(FlagEnabled(1055))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    AND_2.Add(FlagEnabled(1055))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9109)
def Event_9109(_, flag: int):
    """Event 9109"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1042))
    AND_1.Add(FlagEnabled(1055))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(1042))
    AND_2.Add(FlagEnabled(1055))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9110)
def Event_9110(_, flag: int):
    """Event 9110"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    OR_2.Add(FlagEnabled(1058))
    OR_2.Add(FlagEnabled(1056))
    AND_2.Add(OR_2)
    OR_1.Add(AND_2)
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(1043, 1044)))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    OR_4.Add(FlagEnabled(1058))
    OR_4.Add(FlagEnabled(1056))
    AND_4.Add(OR_4)
    OR_3.Add(AND_4)
    OR_3.Add(FlagRangeAnyEnabled(flag_range=(1043, 1044)))
    
    MAIN.Await(not OR_3)
    
    Restart()


@ContinueOnRest(9111)
def Event_9111(_, flag: int, flag_1: int):
    """Event 9111"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(1347))
    AND_1.Add(FlagEnabled(1355))
    AND_1.Add(FlagEnabled(13700651))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L10, flag=9013)
    EnableFlag(flag)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_2.Add(FlagEnabled(1347))
    AND_2.Add(FlagEnabled(1355))
    AND_2.Add(FlagEnabled(13700651))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(9112)
def Event_9112(_, flag: int):
    """Event 9112"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(8200))
    
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(8200))
    
    Restart()


@ContinueOnRest(9113)
def Event_9113(_, flag: int):
    """Event 9113"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(InsideMap(game_map=DREG_HEAP))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1803, 1804)))
    AND_2.Add(InsideMap(game_map=RINGED_CITY))
    AND_2.Add(FlagEnabled(1811))
    AND_3.Add(InsideMap(game_map=(51, 1)))
    AND_3.Add(FlagEnabled(1811))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    AND_4.Add(InsideMap(game_map=DREG_HEAP))
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1803, 1804)))
    AND_5.Add(InsideMap(game_map=RINGED_CITY))
    AND_5.Add(FlagEnabled(1811))
    AND_6.Add(InsideMap(game_map=(51, 1)))
    AND_6.Add(FlagEnabled(1811))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    
    MAIN.Await(not OR_2)
    
    Restart()


@ContinueOnRest(9114)
def Event_9114(_, flag: int):
    """Event 9114"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(1821))
    
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(1821))
    
    Restart()


@RestartOnRest(9120)
def Event_9120(
    _,
    flag: int,
    flag_1: int,
    flag_2: int,
    bit_count: uint,
    bit_count_1: uchar,
    max_value__value: uint,
    left: int,
):
    """Event 9120"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(MapNotInCeremony(game_map=FIRELINK_SHRINE, ceremony_id=0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(FlagDisabled(flag))
    if FlagDisabled(9300):
        OR_1.Add(FlagEnabled(9300))
    if FlagDisabled(9301):
        OR_1.Add(FlagEnabled(9301))
    if FlagDisabled(9302):
        OR_1.Add(FlagEnabled(9302))
    if FlagDisabled(9303):
        OR_1.Add(FlagEnabled(9303))
    if FlagDisabled(9304):
        OR_1.Add(FlagEnabled(9304))
    if FlagDisabled(9305):
        OR_1.Add(FlagEnabled(9305))
    if FlagDisabled(9306):
        OR_1.Add(FlagEnabled(9306))
    if FlagDisabled(9307):
        OR_1.Add(FlagEnabled(9307))
    if FlagDisabled(9308):
        OR_1.Add(FlagEnabled(9308))
    if FlagDisabled(9309):
        OR_1.Add(FlagEnabled(9309))
    if FlagDisabled(9311):
        OR_1.Add(FlagEnabled(9311))
    if FlagDisabled(9313):
        OR_1.Add(FlagEnabled(9313))
    if FlagDisabled(9314):
        OR_1.Add(FlagEnabled(9314))
    if FlagDisabled(9315):
        OR_1.Add(FlagEnabled(9315))
    if FlagDisabled(9317):
        OR_1.Add(FlagEnabled(9317))
    if FlagDisabled(9318):
        OR_1.Add(FlagEnabled(9318))
    if FlagDisabled(9319):
        OR_1.Add(FlagEnabled(9319))
    if FlagDisabled(9320):
        OR_1.Add(FlagEnabled(9320))
    if FlagDisabled(9321):
        OR_1.Add(FlagEnabled(9321))
    if FlagDisabled(9322):
        OR_1.Add(FlagEnabled(9322))
    if FlagDisabled(9323):
        OR_1.Add(FlagEnabled(9323))
    if FlagDisabled(9324):
        OR_1.Add(FlagEnabled(9324))
    if FlagDisabled(9325):
        OR_1.Add(FlagEnabled(9325))
    if FlagDisabled(9326):
        OR_1.Add(FlagEnabled(9326))
    if FlagDisabled(9327):
        OR_1.Add(FlagEnabled(9327))
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.NotEqual, left=left, right=1)
    AND_2.Add(FlagRangeAllEnabled(flag_range=(9300, 9309)))
    AND_2.Add(FlagEnabled(9311))
    AND_2.Add(FlagRangeAllEnabled(flag_range=(9313, 9315)))
    AND_2.Add(FlagRangeAllEnabled(flag_range=(9317, 9321)))
    if FlagEnabled(6951):
        AND_2.Add(FlagRangeAllEnabled(flag_range=(9322, 9323)))
    if FlagEnabled(6952):
        AND_2.Add(FlagRangeAllEnabled(flag_range=(9324, 9327)))
    OR_1.Add(AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(flag):
        return RESTART
    IncrementEventValue(flag_2, bit_count=bit_count, max_value=max_value__value)
    OR_2.Add(EventValue(flag=flag_2, bit_count=bit_count_1) == max_value__value)
    if not OR_2:
        return RESTART
    EnableFlag(flag_1)


@ContinueOnRest(690)
def Event_690(_, flag: int, bit_count: uint, max_value: uint, flag_1: int):
    """Event 690"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(FlagEnabled(flag_1))
    if FlagDisabled(2):
        OR_1.Add(FlagEnabled(2))
    if FlagDisabled(3):
        OR_1.Add(FlagEnabled(3))
    if FlagDisabled(4):
        OR_1.Add(FlagEnabled(4))
    if FlagDisabled(5):
        OR_1.Add(FlagEnabled(5))
    if FlagDisabled(6):
        OR_1.Add(FlagEnabled(6))
    if FlagDisabled(7):
        OR_1.Add(FlagEnabled(7))
    if FlagDisabled(8):
        OR_1.Add(FlagEnabled(8))
    if FlagDisabled(9):
        OR_1.Add(FlagEnabled(9))
    if FlagDisabled(10):
        OR_1.Add(FlagEnabled(10))
    if FlagDisabled(11):
        OR_1.Add(FlagEnabled(11))
    if FlagDisabled(12):
        OR_1.Add(FlagEnabled(12))
    if FlagDisabled(13):
        OR_1.Add(FlagEnabled(13))
    if FlagDisabled(14):
        OR_1.Add(FlagEnabled(14))
    if FlagDisabled(15):
        OR_1.Add(FlagEnabled(15))
    
    MAIN.Await(OR_1)
    
    IncrementEventValue(flag, bit_count=bit_count, max_value=max_value)
    Restart()


@ContinueOnRest(840)
def Event_840(_, flag: int, animation_id: int, target_entity: int, animation_id_1: int):
    """Event 840"""
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    SkipLinesIfFlagEnabled(2, 844)
    SkipLinesIfFlagEnabled(1, 847)
    FaceEntity(PLAYER, target_entity)
    ForceAnimation(PLAYER, animation_id, unknown2=1.0)
    Wait(1.0)
    PlaySoundEffect(PLAYER, 123456789, sound_type=SoundType.s_SFX)
    Wait(4.0)
    if ValueNotEqual(left=animation_id_1, right=-1):
        ForceAnimation(PLAYER, animation_id_1, loop=True, unknown2=1.0)
    Restart()


@ContinueOnRest(870)
def Event_870(_, covenant: uchar, flag: int):
    """Event 870"""
    MAIN.Await(PlayerCovenant(covenant))
    
    EnableFlag(flag)
    AND_1.Add(PlayerCovenant(covenant))
    
    MAIN.Await(not AND_1)
    
    DisableFlag(flag)
    Restart()
