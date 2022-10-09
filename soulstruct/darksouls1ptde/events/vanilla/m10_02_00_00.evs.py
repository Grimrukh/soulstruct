"""
Firelink Shrine

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11020992, obj=1021960, reaction_distance=1.0, initial_kindle_level=10)
    if FlagEnabled(11020108):
        RegisterBonfire(bonfire_flag=11020992, obj=1021960, reaction_distance=1.0, initial_kindle_level=30)
    SkipLinesIfFlagDisabled(4, 11020300)
    SkipLinesIfFlagEnabled(2, 11020302)
    EndOfAnimation(obj=1021000, animation_id=11)
    SkipLines(1)
    EndOfAnimation(obj=1021000, animation_id=12)
    Event_11020300()
    Event_11025050()
    Event_11020001()
    Event_11020020()
    Event_11020021()
    Event_11020105()
    Event_11020106()
    Event_11020108()
    Event_11020120(0, obj_act_id=11020120, text=10010874, obj=1021465, text_1=10010883, item=2015)
    Event_11020350()
    Event_11020351()
    Event_11020352()
    Event_11025150()
    Event_11020700(0, obj=1021650, obj_act_id=11020700)
    Event_11020700(1, obj=1021651, obj_act_id=11020701)
    Event_11020700(2, obj=1021652, obj_act_id=11020702)
    Event_11020700(3, obj=1021653, obj_act_id=11020703)
    Event_11025200(0, other_entity=1020203, character=1020203, radius=4.0, seconds=0.0)
    Event_11025200(1, other_entity=1020203, character=1020204, radius=4.0, seconds=0.8999999761581421)
    Event_11025200(2, other_entity=1020205, character=1020205, radius=3.0, seconds=0.0)
    Event_11025200(3, other_entity=1020205, character=1020206, radius=3.0, seconds=0.699999988079071)
    Event_11025200(6, other_entity=1020200, character=1020200, radius=11.0, seconds=0.0)
    Event_11025200(7, other_entity=1020200, character=1020201, radius=11.0, seconds=1.5)
    Event_11025200(8, other_entity=1020202, character=1020202, radius=7.0, seconds=0.0)
    Event_11025200(9, other_entity=1020202, character=1020214, radius=7.0, seconds=1.100000023841858)
    Event_11025200(10, other_entity=1020209, character=1020209, radius=11.0, seconds=0.0)
    Event_11025200(11, other_entity=1020209, character=1020210, radius=11.0, seconds=0.800000011920929)
    Event_11025200(12, other_entity=1020209, character=1020211, radius=11.0, seconds=1.5)
    Event_11025200(13, other_entity=1020209, character=1020212, radius=11.0, seconds=2.200000047683716)
    Event_11025200(14, other_entity=1020213, character=1020213, radius=3.0, seconds=0.0)


@ContinueOnRest(11020899)
def Event_11020899(_, first_flag: int, last_flag: int):
    """Event 11020899"""
    if Client():
        return
    if FlagDisabled(11020898):
        EnableFlag(11020898)
        EndOfAnimation(obj=1021690, animation_id=0)
        DisableObjectActivation(1021690, obj_act_id=-1)
        End()
    WaitFrames(frames=1)
    if FlagEnabled(11025300):
        MAIN.Await(ObjectActivated(obj_act_id=11020704))
    
        WaitFrames(frames=10)
        EnableTreasure(obj=1021700)
        EnableTreasure(obj=1021701)
        EnableTreasure(obj=1021702)
        EnableTreasure(obj=1021703)
        EnableTreasure(obj=1021704)
        EnableTreasure(obj=1021705)
        EnableTreasure(obj=1021706)
        EnableTreasure(obj=1021707)
        EnableTreasureCollection(obj=1021700)
        EnableTreasureCollection(obj=1021701)
        EnableTreasureCollection(obj=1021702)
        EnableTreasureCollection(obj=1021703)
        EnableTreasureCollection(obj=1021704)
        EnableTreasureCollection(obj=1021705)
        EnableTreasureCollection(obj=1021706)
        EnableTreasureCollection(obj=1021707)
        EnableFlagRange((first_flag, last_flag))
        End()
    EndOfAnimation(obj=1021690, animation_id=0)
    DisableObjectActivation(1021690, obj_act_id=-1)


@ContinueOnRest(11020800)
def Event_11020800(_, right: int, flag: int, item_type: uchar, item: int, flag_1: int):
    """Event 11020800"""
    if Client():
        return
    AND_1.Add(FlagEnabled(right))
    AND_1.Add(FlagDisabled(flag))
    IfPlayerDoesNotHaveItem(AND_1, item, item_type=item_type, including_storage=True)
    if ValueEqual(left=50000082, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(201, including_storage=True))
    if ValueEqual(left=8131, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(203, including_storage=True))
    if ValueEqual(left=8132, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(205, including_storage=True))
    if ValueEqual(left=8133, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(207, including_storage=True))
    if ValueEqual(left=8134, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(209, including_storage=True))
    if ValueEqual(left=8135, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(211, including_storage=True))
    if ValueEqual(left=8136, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(213, including_storage=True))
    if ValueEqual(left=8137, right=right):
        AND_1.Add(PlayerDoesNotHaveGood(215, including_storage=True))
    if not AND_1:
        return
    EnableFlag(11025300)
    
    MAIN.Await(ObjectActivated(obj_act_id=11020704))
    
    DisableFlag(flag_1)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    EnableFlagRange((50004000, 50004069))
    Event_11020800(0, right=51010140, flag=703, item_type=3, item=2001, flag_1=50004000)
    Event_11020800(1, right=11017140, flag=703, item_type=3, item=2002, flag_1=50004001)
    Event_11020800(2, right=51500150, flag=703, item_type=3, item=2003, flag_1=50004002)
    Event_11020800(3, right=51700990, flag=703, item_type=3, item=2004, flag_1=50004003)
    Event_11020800(4, right=51700630, flag=703, item_type=3, item=2005, flag_1=50004004)
    Event_11020800(5, right=51700590, flag=703, item_type=3, item=2006, flag_1=50004005)
    Event_11020800(6, right=50001500, flag=703, item_type=3, item=2007, flag_1=50004006)
    Event_11020800(7, right=51400500, flag=703, item_type=3, item=2008, flag_1=50004007)
    Event_11020800(8, right=51100140, flag=703, item_type=3, item=2009, flag_1=50004008)
    Event_11020800(9, right=51810000, flag=703, item_type=3, item=2010, flag_1=50004009)
    Event_11020800(10, right=50001660, flag=703, item_type=3, item=2011, flag_1=50004010)
    Event_11020800(11, right=50000080, flag=703, item_type=3, item=2012, flag_1=50004011)
    Event_11020800(12, right=50000100, flag=703, item_type=3, item=2013, flag_1=50004012)
    Event_11020800(13, right=50001510, flag=703, item_type=3, item=2014, flag_1=50004013)
    Event_11020800(14, right=11027030, flag=11027030, item_type=3, item=2015, flag_1=50004014)
    Event_11020800(15, right=51020210, flag=703, item_type=3, item=2016, flag_1=50004015)
    Event_11020800(16, right=51010000, flag=703, item_type=3, item=2017, flag_1=50004016)
    Event_11020800(17, right=51000240, flag=703, item_type=3, item=2018, flag_1=50004017)
    Event_11020800(18, right=51200140, flag=703, item_type=3, item=2019, flag_1=50004018)
    Event_11020800(19, right=51700210, flag=703, item_type=3, item=2020, flag_1=50004019)
    Event_11020800(20, right=11017030, flag=703, item_type=3, item=2021, flag_1=50004020)
    Event_11020800(21, right=50001560, flag=11800201, item_type=3, item=2500, flag_1=50004021)
    Event_11020800(22, right=50001580, flag=11800202, item_type=3, item=2501, flag_1=50004022)
    Event_11020800(23, right=50001630, flag=11800203, item_type=3, item=2502, flag_1=50004023)
    Event_11020800(24, right=50001640, flag=11800204, item_type=3, item=2503, flag_1=50004024)
    Event_11020800(25, right=50000090, flag=11800100, item_type=3, item=2510, flag_1=50004025)
    Event_11020800(26, right=50001540, flag=703, item_type=2, item=138, flag_1=50004026)
    Event_11020800(27, right=50001670, flag=703, item_type=2, item=139, flag_1=50004027)
    Event_11020800(28, right=50000000, flag=703, item_type=3, item=100, flag_1=50004028)
    Event_11020800(29, right=51100330, flag=703, item_type=3, item=101, flag_1=50004029)
    Event_11020800(30, right=50000390, flag=703, item_type=3, item=102, flag_1=50004030)
    Event_11020800(31, right=200, flag=703, item_type=3, item=103, flag_1=50004031)
    Event_11020800(32, right=11017020, flag=703, item_type=3, item=106, flag_1=50004032)
    Event_11020800(33, right=11607020, flag=703, item_type=3, item=108, flag_1=50004033)
    Event_11020800(34, right=11407080, flag=703, item_type=3, item=112, flag_1=50004034)
    Event_11020800(35, right=50000360, flag=703, item_type=3, item=113, flag_1=50004035)
    Event_11020800(36, right=50000260, flag=703, item_type=3, item=114, flag_1=50004036)
    Event_11020800(37, right=200, flag=703, item_type=3, item=117, flag_1=50004037)
    Event_11020800(38, right=50000082, flag=8131, item_type=3, item=200, flag_1=50004038)
    Event_11020800(39, right=8131, flag=8132, item_type=3, item=202, flag_1=50004039)
    Event_11020800(40, right=8132, flag=8133, item_type=3, item=204, flag_1=50004040)
    Event_11020800(41, right=8133, flag=8134, item_type=3, item=206, flag_1=50004041)
    Event_11020800(42, right=8134, flag=8135, item_type=3, item=208, flag_1=50004042)
    Event_11020800(43, right=8135, flag=8136, item_type=3, item=210, flag_1=50004043)
    Event_11020800(44, right=8136, flag=8137, item_type=3, item=212, flag_1=50004044)
    Event_11020800(45, right=8137, flag=703, item_type=3, item=214, flag_1=50004045)
    Event_11020800(46, right=51810080, flag=703, item_type=3, item=384, flag_1=50004046)
    Event_11020800(47, right=11017150, flag=703, item_type=3, item=2600, flag_1=50004047)
    Event_11020800(48, right=11017160, flag=703, item_type=3, item=2601, flag_1=50004048)
    Event_11020800(49, right=11017170, flag=703, item_type=3, item=2602, flag_1=50004049)
    Event_11020800(50, right=50001550, flag=703, item_type=3, item=2607, flag_1=50004050)
    Event_11020800(51, right=11007010, flag=703, item_type=3, item=2608, flag_1=50004051)
    Event_11020800(52, right=50000360, flag=703, item_type=2, item=102, flag_1=50004052)
    Event_11020800(53, right=50000160, flag=703, item_type=2, item=103, flag_1=50004053)
    Event_11020800(54, right=50000260, flag=703, item_type=3, item=377, flag_1=50004054)
    Event_11020800(55, right=50000270, flag=703, item_type=3, item=378, flag_1=50004055)
    Event_11020800(56, right=51000500, flag=350, item_type=3, item=800, flag_1=50004056)
    Event_11020800(57, right=51600500, flag=351, item_type=3, item=801, flag_1=50004057)
    Event_11020800(58, right=51700600, flag=352, item_type=3, item=802, flag_1=50004058)
    Event_11020800(59, right=51700530, flag=356, item_type=3, item=806, flag_1=50004059)
    Event_11020800(60, right=51200500, flag=357, item_type=3, item=807, flag_1=50004060)
    Event_11020800(61, right=51200141, flag=358, item_type=3, item=808, flag_1=50004061)
    Event_11020800(62, right=51310500, flag=359, item_type=3, item=809, flag_1=50004062)
    Event_11020800(63, right=51100370, flag=360, item_type=3, item=810, flag_1=50004063)
    Event_11020800(64, right=51410100, flag=362, item_type=3, item=812, flag_1=50004064)
    Event_11020800(65, right=51410530, flag=363, item_type=3, item=813, flag_1=50004065)
    Event_11020800(66, right=11007020, flag=703, item_type=3, item=2100, flag_1=50004066)
    Event_11020800(67, right=51210981, flag=703, item_type=3, item=2022, flag_1=50004067)
    Event_11020800(68, right=51700930, flag=703, item_type=3, item=2520, flag_1=50004068)
    Event_11020800(69, right=50001200, flag=703, item_type=3, item=118, flag_1=50004069)
    Event_11020899(0, first_flag=50004000, last_flag=50004069)
    EnableFlag(11020120)
    EnableFlag(61020120)
    HumanityRegistration(6031, event_flag=8334)
    SkipLinesIfFlagEnabled(2, 1092)
    SkipLinesIfFlagEnabled(1, 1096)
    DisableCharacter(6031)
    Event_11020510(0, character=6031, flag=1096)
    Event_11020530(0, character=6031, first_flag=1090, last_flag=1109, flag=1097)
    Event_11020550(0, character=6031, first_flag=1090, last_flag=1109, flag=1092)
    Event_11020551(0, character=6031, first_flag=1090, last_flag=1109, flag=1093)
    HumanityRegistration(6041, event_flag=8342)
    SkipLinesIfFlagRangeAnyEnabled(1, (1112, 1114))
    DisableCharacter(6041)
    Event_11020510(1, character=6041, flag=1114)
    Event_11020530(1, character=6041, first_flag=1110, last_flag=1119, flag=1115)
    Event_11020552(0, character=6041, first_flag=1110, last_flag=1119, flag=1112)
    Event_11020553(0, character=6041, first_flag=1110, last_flag=1119, flag=1113)
    Event_11020554(0, character=6041, first_flag=1110, last_flag=1119, flag=1117)
    Event_11020110()
    Event_11020555(0, character=6060, first_flag=1140, last_flag=1169, flag=1141)
    Event_11020556(0, character=6060, first_flag=1140, last_flag=1169, flag=1146)
    Event_11020557(0, character=6060, first_flag=1140, last_flag=1169, flag=1142)
    Event_11020558(0, character=6060, first_flag=1140, last_flag=1169, flag=1145)
    HumanityRegistration(6070, event_flag=8358)
    if FlagDisabled(1171):
        DisableCharacter(6070)
    Event_11020501()
    Event_11020559()
    Event_11020560()
    Event_11020530(2, character=6070, first_flag=1170, last_flag=1180, flag=1177)
    HumanityRegistration(6080, event_flag=8366)
    SkipLinesIfFlagEnabled(1, 1192)
    SkipLines(1)
    DisableCharacter(6080)
    Event_11020564(0, character=6080, first_flag=1190, last_flag=1209, flag=1193)
    Event_11020565(0, character=6080, first_flag=1190, last_flag=1209, flag=1194)
    Event_11020502(0, character=6080, flag=1197)
    Event_11020503(0, character=6080, flag=1195)
    Event_11020569(0, character=6080, first_flag=1190, last_flag=1209, flag=1198)
    Event_11020567(0, character=6080, first_flag=1190, last_flag=1209, flag=1196)
    HumanityRegistration(6090, event_flag=8374)
    if FlagDisabled(1211):
        DisableCharacter(6090)
    Event_11020530(4, character=6090, first_flag=1210, last_flag=1219, flag=1214)
    HumanityRegistration(6100, event_flag=8382)
    if FlagDisabled(1221):
        DisableCharacter(6100)
    Event_11020530(5, character=6100, first_flag=1220, last_flag=1229, flag=1224)
    HumanityRegistration(6131, event_flag=8390)
    SkipLinesIfFlagEnabled(2, 1252)
    SkipLinesIfFlagEnabled(1, 1253)
    DisableCharacter(6131)
    Event_11020510(6, character=6131, flag=1253)
    Event_11020530(6, character=6131, first_flag=1250, last_flag=1259, flag=1254)
    Event_11020574(0, character=6131, first_flag=1250, last_flag=1259, flag=1252)
    Event_11020575(0, character=6131, first_flag=1250, last_flag=1259, flag=1256)
    HumanityRegistration(6181, event_flag=8406)
    SkipLinesIfFlagEnabled(2, 1314)
    SkipLinesIfFlagEnabled(1, 1313)
    DisableCharacter(6181)
    Event_11020510(7, character=6181, flag=1314)
    Event_11020530(7, character=6181, first_flag=1310, last_flag=1319, flag=1315)
    Event_11020576(0, character=6181, first_flag=1310, last_flag=1319, flag=1313)
    Event_11020504(8, character=6240, flag=1411)
    Event_11020530(8, character=6240, first_flag=1410, last_flag=1413, flag=1412)
    HumanityRegistration(6261, event_flag=8430)
    SkipLinesIfFlagEnabled(2, 1434)
    SkipLinesIfFlagEnabled(1, 1431)
    DisableCharacter(6261)
    Event_11020510(9, character=6261, flag=1434)
    Event_11020413(0, character=6261, flag=1435)
    Event_11020412(0, character=6261, first_flag=1430, last_flag=1459, flag=1431)
    HumanityRegistration(6270, event_flag=8438)
    SkipLinesIfFlagEnabled(2, 1464)
    SkipLinesIfFlagEnabled(1, 1462)
    SkipLines(1)
    DisableCharacter(6270)
    Event_11020510(10, character=6270, flag=1461)
    Event_11020530(10, character=6270, first_flag=1460, last_flag=1464, flag=1462)
    Event_11020577(0, character=6270, first_flag=1460, last_flag=1464, flag=1464)
    HumanityRegistration(6287, event_flag=8446)
    SkipLinesIfFlagEnabled(2, 1512)
    SkipLinesIfFlagEnabled(1, 1497)
    DisableCharacter(6287)
    Event_11020510(11, character=6287, flag=1512)
    Event_11020530(11, character=6287, first_flag=1490, last_flag=1514, flag=1513)
    Event_11020579(0, character=6287, first_flag=1490, last_flag=1514, flag=1497)
    HumanityRegistration(6292, event_flag=8454)
    SkipLinesIfFlagEnabled(3, 1547)
    SkipLinesIfFlagEnabled(2, 1545)
    SkipLinesIfFlagEnabled(1, 1543)
    DisableCharacter(6292)
    Event_11020510(12, character=6292, flag=1547)
    Event_11020530(12, character=6292, first_flag=1540, last_flag=1569, flag=1548)
    Event_11020583(0, character=6292, first_flag=1540, last_flag=1569, flag=1543)
    Event_11020584(0, character=6292, first_flag=1540, last_flag=1569, flag=1544)
    Event_11020585(0, character=6292, first_flag=1540, last_flag=1569, flag=1545)
    Event_11020586(0, character=6292)
    HumanityRegistration(6301, event_flag=8462)
    SkipLinesIfFlagEnabled(3, 1572)
    SkipLinesIfFlagEnabled(2, 1574)
    SkipLinesIfFlagEnabled(1, 1577)
    DisableCharacter(6301)
    Event_11020510(13, character=6301, flag=1574)
    Event_11020530(13, character=6301, first_flag=1570, last_flag=1599, flag=1575)
    Event_11020587(0, character=6301, first_flag=1570, last_flag=1599, flag=1572)
    if FlagEnabled(11020690):
        Event_11020588(0, character=6301, first_flag=1570, last_flag=1599, flag=1573, flag_1=1572, flag_2=1577)
    Event_11020589(0, character=6301, first_flag=1570, last_flag=1599, flag=1577)
    Event_11020410(0, character=6301, first_flag=1570, last_flag=1599, flag=1578)
    HumanityRegistration(6322, event_flag=8478)
    SkipLinesIfFlagEnabled(2, 1627)
    SkipLinesIfFlagEnabled(1, 1626)
    DisableCharacter(6322)
    Event_11020510(14, character=6322, flag=1627)
    Event_11020530(14, character=6322, first_flag=1620, last_flag=1629, flag=1628)
    Event_11020411(0, character=6322, first_flag=1620, last_flag=1629, flag=1626)
    SkipLinesIfFlagDisabled(2, 15)
    DisableCharacter(6330)
    SkipLinesIfFlagEnabled(14, 15)
    EnableImmortality(6330)
    DisableGravity(6330)
    SkipLinesIfFlagEnabled(2, 1647)
    SkipLinesIfFlagEnabled(1, 1640)
    SkipLines(1)
    DisableCharacter(6330)
    Event_11020420(0, character=6330, first_flag=1640, last_flag=1649, flag=1641)
    Event_11020421(0, character=6330, first_flag=1640, last_flag=1649, flag=1642)
    Event_11020422(0, character=6330, first_flag=1640, last_flag=1649, flag=1643)
    Event_11020423(0, character=6330, first_flag=1640, last_flag=1649, flag=1644)
    Event_11020424(0, character=6330, first_flag=1640, last_flag=1649, flag=1647)
    Event_11020425(0, character=6330, first_flag=1640, last_flag=1649, flag=1647)
    Event_11026200()
    Event_11026210()


@ContinueOnRest(11020300)
def Event_11020300():
    """Event 11020300"""
    if ThisEventFlagEnabled():
        Event_11020301()
        End()
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1022003))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11020300)
    EnableFlag(11020302)
    ForceAnimation(1021000, 0, wait_for_completion=True)
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1022001))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1022002))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()


@ContinueOnRest(11020301)
def Event_11020301():
    """Event 11020301"""
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagDisabled(11020302))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1022000))
    AND_2.Add(Singleplayer())
    AND_2.Add(FlagEnabled(11020302))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1022001))
    AND_3.Add(Singleplayer())
    AND_3.Add(FlagEnabled(11020302))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1022002))
    AND_4.Add(Singleplayer())
    AND_4.Add(FlagDisabled(11020302))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1022003))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(7, input_condition=AND_3)
    EnableFlag(11020302)
    ForceAnimation(1021000, 2, wait_for_completion=True)
    AND_5.Add(CharacterOutsideRegion(PLAYER, region=1022001))
    AND_5.Add(CharacterOutsideRegion(PLAYER, region=1022002))
    
    MAIN.Await(AND_5)
    
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()
    DisableFlag(11020302)
    ForceAnimation(1021000, 1, wait_for_completion=True)
    AND_6.Add(CharacterOutsideRegion(PLAYER, region=1022000))
    AND_6.Add(CharacterOutsideRegion(PLAYER, region=1022003))
    
    MAIN.Await(AND_6)
    
    ForceAnimation(1021000, 21, wait_for_completion=True)
    Restart()


@RestartOnRest(11025050)
def Event_11025050():
    """Event 11025050"""
    EnableImmortality(1020100)
    
    MAIN.Await(HealthRatio(1020100) <= 0.30000001192092896)
    
    ForceAnimation(1020100, 7000, wait_for_completion=True)
    DisableCharacter(1020100)


@ContinueOnRest(11020001)
def Event_11020001():
    """Event 11020001"""
    DisableNetworkSync()
    if ThisEventFlagEnabled():
        return
    if OutsideMap(game_map=UNDEAD_ASYLUM):
        MAIN.Await(InsideMap(game_map=FIRELINK_SHRINE))
    
        EnableFlag(11810000)
    DisableBackread(6031)
    DisableBackread(6041)
    DisableBackread(6060)
    DisableBackread(6070)
    DisableBackread(6090)
    DisableBackread(6100)
    DisableBackread(6131)
    DisableBackread(6181)
    DisableBackread(6240)
    DisableBackread(6261)
    DisableBackread(6287)
    DisableBackread(6292)
    DisableBackread(6301)
    DisableBackread(6322)
    DisableBackread(6330)
    DisableSoundEvent(sound_id=1023800)
    
    MAIN.Await(FlagEnabled(11810000))
    
    EnableSoundEvent(sound_id=1023800)
    EnableFlag(11020001)
    Wait(3.0)
    EnableBackread(6031)
    EnableBackread(6041)
    EnableBackread(6060)
    EnableBackread(6070)
    EnableBackread(6090)
    EnableBackread(6100)
    EnableBackread(6131)
    EnableBackread(6181)
    EnableBackread(6240)
    EnableBackread(6261)
    EnableBackread(6287)
    EnableBackread(6292)
    EnableBackread(6301)
    EnableBackread(6322)
    EnableBackread(6330)
    EnableFlag(200)


@RestartOnRest(11025200)
def Event_11025200(_, other_entity: int, character: int, radius: float, seconds: float):
    """Event 11025200"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    
    DisableNetworkSync()
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=9061)


@ContinueOnRest(11020020)
def Event_11020020():
    """Event 11020020"""
    MAIN.Await(ActionButton(
        prompt_text=10010506,
        anchor_entity=1022120,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    EnableFlag(11025060)
    WaitFrames(frames=3)
    AND_1.Add(ActionButton(
        prompt_text=10010507,
        anchor_entity=1022120,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1022120))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11025060)
    RestartEvent(event_id=11020021)
    SetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


@ContinueOnRest(11020021)
def Event_11020021():
    """Event 11020021"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11025060))
    
    if FlagDisabled(11020000):
        Wait(20.0)
    PlayCutscene(100230, cutscene_flags=0, player_id=10000, move_to_region=1812110, game_map=UNDEAD_ASYLUM)
    PlayCutscene(180130, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11020000)
    DisableFlag(11025060)
    SetStandbyAnimationSettings(PLAYER)
    Restart()


@ContinueOnRest(11020105)
def Event_11020105():
    """Event 11020105"""
    DisableTreasure(obj=1021300)
    DisableObject(1021961)
    if FlagEnabled(11020108):
        return
    if FlagDisabled(11020101):
        MAIN.Await(FlagEnabled(11020100))
    
        EnableFlag(102)
        EnableTreasure(obj=1021300)
    
        MAIN.Await(FlagEnabled(11020101))
    
        DisableFlag(102)
    
    MAIN.Await(FlagEnabled(11020108))
    
    RegisterBonfire(bonfire_flag=11020992, obj=1021960, reaction_distance=1.0, initial_kindle_level=30)


@ContinueOnRest(11020106)
def Event_11020106():
    """Event 11020106"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11020100))
    AND_1.Add(FlagDisabled(11020101))
    AND_1.Add(ActionButton(
        prompt_text=10010182,
        anchor_entity=1021960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(
        text=10010184,
        anchor_entity=1021960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@ContinueOnRest(11020108)
def Event_11020108():
    """Event 11020108"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(71020022))
    OR_1.Add(FlagEnabled(71020023))
    
    MAIN.Await(OR_1)
    
    End()


@ContinueOnRest(11020120)
def Event_11020120(_, obj_act_id: int, text: int, obj: int, text_1: int, item: int):
    """Event 11020120"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    AND_1.Add(Host())
    AND_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableFlag(obj_act_id)
    SkipLinesIfClient(5)
    AND_1.Add(PlayerHasGood(item))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=text_1, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@ContinueOnRest(11020350)
def Event_11020350():
    """Event 11020350"""
    if ThisEventFlagDisabled():
        DisableObject(1021481)
        DisableMapCollision(collision=1023510)
        AND_1.Add(FlagEnabled(11010700))
        AND_1.Add(FlagEnabled(11400200))
    
        MAIN.Await(AND_1)
    
        EnableObject(1021481)
        EnableMapCollision(collision=1023510)
    DisableObject(1021480)
    DisableMapCollision(collision=1023500)
    DisableMapPiece(map_piece_id=1023501)
    DisableMapCollision(collision=1023502)


@ContinueOnRest(11020351)
def Event_11020351():
    """Event 11020351"""
    if FlagEnabled(0):
        DisableMapCollision(collision=0)
        DisableMapCollision(collision=0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1022111))
    
    if FlagDisabled(710):
        Kill(PLAYER)
        End()
    PlayCutscene(180060, cutscene_flags=0, player_id=10000, move_to_region=1802110, game_map=KILN_OF_THE_FIRST_FLAME)
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(11020352)
def Event_11020352():
    """Event 11020352"""
    MAIN.Await(FlagEnabled(710))
    
    DisableMapCollision(collision=1023600)
    DisableMapCollision(collision=1023601)


@ContinueOnRest(11020700)
def Event_11020700(_, obj: int, obj_act_id: int):
    """Event 11020700"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11025150)
def Event_11025150():
    """Event 11025150"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1022710))
    
    AICommand(1020190, command_id=1, command_slot=3)
    AICommand(1020160, command_id=1, command_slot=3)
    AICommand(1020161, command_id=1, command_slot=3)
    AICommand(1020163, command_id=1, command_slot=3)
    AICommand(1020165, command_id=1, command_slot=3)
    AICommand(1020166, command_id=1, command_slot=3)
    ReplanAI(1020190)
    ReplanAI(1020160)
    ReplanAI(1020161)
    ReplanAI(1020163)
    ReplanAI(1020165)
    ReplanAI(1020166)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1022710))
    
    AICommand(1020190, command_id=-1, command_slot=3)
    AICommand(1020160, command_id=-1, command_slot=3)
    AICommand(1020161, command_id=-1, command_slot=3)
    AICommand(1020163, command_id=-1, command_slot=3)
    AICommand(1020165, command_id=-1, command_slot=3)
    AICommand(1020166, command_id=-1, command_slot=3)
    ReplanAI(1020190)
    ReplanAI(1020160)
    ReplanAI(1020161)
    ReplanAI(1020163)
    ReplanAI(1020165)
    ReplanAI(1020166)
    Restart()


@ContinueOnRest(11020510)
def Event_11020510(_, character: int, flag: int):
    """Event 11020510"""
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventSlotFlagDisabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11020530)
def Event_11020530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020530"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(CharacterInsideRegion(character, region=1022300))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    Kill(character, award_souls=True)
    DisableGravity(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020501)
def Event_11020501():
    """Event 11020501"""
    AND_1.Add(FlagEnabled(11010902))
    AND_1.Add(FlagDisabled(11020693))
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagRangeAllDisabled(flag_range=(1193, 1196)))
    AND_2.Add(HealthRatio(6070) <= 0.8999999761581421)
    if FlagDisabled(1177):
        AND_2.Add(Attacked(attacked_entity=6070, attacker=PLAYER))
    AND_3.Add(HealthRatio(6080) <= 0.8999999761581421)
    if FlagDisabled(1198):
        AND_3.Add(Attacked(attacked_entity=6080, attacker=PLAYER))
    AND_4.Add(HealthRatio(6090) <= 0.8999999761581421)
    if FlagDisabled(1214):
        AND_4.Add(Attacked(attacked_entity=6090, attacker=PLAYER))
    AND_5.Add(HealthRatio(6100) <= 0.8999999761581421)
    if FlagDisabled(1224):
        AND_5.Add(Attacked(attacked_entity=6100, attacker=PLAYER))
    AND_6.Add(FlagEnabled(1197))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    AND_1.Add(OR_1)
    AND_7.Add(ThisEventFlagEnabled())
    OR_2.Add(AND_1)
    OR_2.Add(AND_7)
    
    MAIN.Await(OR_2)
    
    if FlagDisabled(1177):
        EnableFlag(1176)
        EnableCharacter(6070)
    SetTeamType(6070, TeamType.HostileAlly)
    if FlagDisabled(1198):
        EnableFlag(1197)
        EnableCharacter(6080)
    SetTeamType(6080, TeamType.HostileAlly)
    if FlagDisabled(1214):
        EnableFlag(1213)
        EnableCharacter(6090)
    SetTeamType(6090, TeamType.HostileAlly)
    if FlagDisabled(1224):
        EnableFlag(1223)
        EnableCharacter(6100)
    SetTeamType(6100, TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11020502)
def Event_11020502(_, character: int, flag: int):
    """Event 11020502"""
    AND_7.Add(FlagDisabled(11010902))
    AND_7.Add(FlagDisabled(1195))
    AND_7.Add(FlagDisabled(1197))
    AND_7.Add(FlagEnabled(1202))
    AND_6.Add(FlagEnabled(11010902))
    AND_6.Add(FlagDisabled(1195))
    AND_6.Add(FlagDisabled(1197))
    AND_6.Add(FlagEnabled(1193))
    OR_2.Add(AND_7)
    OR_2.Add(AND_6)
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11020503)
def Event_11020503(_, character: int, flag: int):
    """Event 11020503"""
    AND_1.Add(FlagDisabled(1197))
    AND_1.Add(FlagEnabled(1194))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11020504)
def Event_11020504(_, character: int, flag: int):
    """Event 11020504"""
    AND_1.Add(FlagDisabled(1411))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_1)
    Move(character, destination=1022700, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(character, region=1022700)
    End()
    SetTeamType(character, TeamType.Enemy)
    SetNest(character, region=1022700)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=1022700))
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    EnableFlag(flag)


@ContinueOnRest(11020550)
def Event_11020550(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020550"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagDisabled(1099))
    AND_1.Add(FlagEnabled(1091))
    AND_1.Add(FlagEnabled(11500594))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020551)
def Event_11020551(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020551"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagDisabled(1099))
    AND_1.Add(FlagEnabled(1092))
    AND_1.Add(FlagEnabled(11020603))
    AND_1.Add(OutsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11020694)
    DisableCharacter(character)


@ContinueOnRest(11020552)
def Event_11020552(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020552"""
    AND_1.Add(FlagDisabled(1114))
    AND_1.Add(FlagDisabled(1117))
    AND_1.Add(FlagEnabled(1111))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020553)
def Event_11020553(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020553"""
    AND_1.Add(FlagDisabled(1114))
    AND_1.Add(FlagDisabled(1117))
    AND_1.Add(FlagEnabled(1112))
    AND_1.Add(FlagEnabled(11020694))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020554)
def Event_11020554(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020554"""
    AND_1.Add(FlagDisabled(1114))
    AND_1.Add(FlagDisabled(1117))
    AND_1.Add(FlagEnabled(1113))
    AND_1.Add(FlagEnabled(723))
    AND_1.Add(InsideMap(game_map=SENS_FORTRESS))
    if not AND_1:
        return
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11020555)
def Event_11020555(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020555"""
    AND_1.Add(FlagEnabled(1140))
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(FlagDisabled(1575))
    AND_2.Add(FlagEnabled(812))
    AND_2.Add(FlagEnabled(813))
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(11500200))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020556)
def Event_11020556(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020556"""
    AND_1.Add(FlagEnabled(1141))
    AND_1.Add(FlagEnabled(810))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020557)
def Event_11020557(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020557"""
    AND_1.Add(FlagEnabled(1146))
    AND_1.Add(FlagEnabled(11020609))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020558)
def Event_11020558(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020558"""
    AND_1.Add(FlagEnabled(1142))
    AND_1.Add(FlagEnabled(11800200))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020559)
def Event_11020559():
    """Event 11020559"""
    AND_1.Add(FlagEnabled(1170))
    AND_1.Add(FlagEnabled(11010902))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1170, 1189))
    EnableFlag(1171)
    EnableCharacter(6070)
    DisableFlagRange((1210, 1219))
    EnableFlag(1211)
    EnableCharacter(6090)
    DisableFlagRange((1220, 1229))
    EnableFlag(1221)
    EnableCharacter(6100)


@ContinueOnRest(11020560)
def Event_11020560():
    """Event 11020560"""
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1176, 1181)))
    AND_7.Add(FlagEnabled(1171))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1195, 1198)))
    AND_7.Add(FlagEnabled(1202))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1213, 1215)))
    AND_7.Add(FlagEnabled(1211))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1223, 1225)))
    AND_7.Add(FlagEnabled(1221))
    AND_1.Add(AND_7)
    AND_1.Add(FlagEnabled(11020600))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(AND_7)
    AND_2.Add(FlagEnabled(11300005))
    AND_3.Add(AND_7)
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    ClearEventValue(600, bit_count=4)
    EnableFlag(11020693)
    DisableFlagRange((1170, 1189))
    EnableFlag(1173)
    DisableCharacter(6070)
    DisableFlagRange((1190, 1209))
    EnableFlag(1192)
    DisableCharacter(6080)
    DisableFlagRange((1210, 1219))
    EnableFlag(1216)
    DisableCharacter(6090)
    DisableFlagRange((1220, 1229))
    EnableFlag(1226)
    DisableCharacter(6100)


@ContinueOnRest(11020564)
def Event_11020564(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020564"""
    AND_1.Add(FlagDisabled(1195))
    AND_1.Add(FlagDisabled(1197))
    AND_1.Add(FlagEnabled(1192))
    if not AND_1:
        return
    if FlagDisabled(11020692):
        EnableFlag(11020692)
        End()
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020565)
def Event_11020565(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020565"""
    AND_1.Add(FlagDisabled(1195))
    AND_1.Add(FlagDisabled(1197))
    AND_1.Add(FlagEnabled(1193))
    AND_1.Add(FlagEnabled(11020608))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020567)
def Event_11020567(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020567"""
    OR_2.Add(FlagEnabled(1194))
    OR_2.Add(FlagEnabled(1195))
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(1196))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EndIfFinishedConditionTrue(input_condition=AND_1)
    DropMandatoryTreasure(character)


@ContinueOnRest(11020569)
def Event_11020569(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020569"""
    AND_1.Add(FlagDisabled(1194))
    AND_1.Add(FlagDisabled(1195))
    AND_1.Add(FlagDisabled(1196))
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(1198))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EndIfFinishedConditionTrue(input_condition=AND_1)
    DropMandatoryTreasure(character)


@ContinueOnRest(11020574)
def Event_11020574(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020574"""
    AND_1.Add(FlagDisabled(1253))
    AND_1.Add(FlagEnabled(1251))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020575)
def Event_11020575(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020575"""
    AND_1.Add(FlagDisabled(1253))
    AND_1.Add(FlagEnabled(1252))
    AND_1.Add(FlagEnabled(11020102))
    AND_1.Add(FlagEnabled(11020103))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020576)
def Event_11020576(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020576"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1312))
    AND_1.Add(FlagEnabled(11600593))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020577)
def Event_11020577(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020577"""
    AND_1.Add(FlagDisabled(1461))
    AND_1.Add(FlagDisabled(1464))
    AND_1.Add(FlagEnabled(1460))
    AND_1.Add(FlagEnabled(11020597))
    AND_1.Add(OutsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11020579)
def Event_11020579(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020579"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1494))
    AND_1.Add(FlagEnabled(11510590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020583)
def Event_11020583(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020583"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1542))
    AND_1.Add(FlagEnabled(11700593))
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagDisabled(1513))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020584)
def Event_11020584(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020584"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1543))
    AND_1.Add(FlagEnabled(11020605))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1547))
    AND_2.Add(FlagEnabled(1543))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11020585)
def Event_11020585(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020585"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1544))
    AND_1.Add(FlagEnabled(11410593))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020586)
def Event_11020586(_, character: int):
    """Event 11020586"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1545))
    AND_1.Add(FlagEnabled(11020606))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1547))
    AND_2.Add(FlagEnabled(1545))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    DisableCharacter(character)


@ContinueOnRest(11020587)
def Event_11020587(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020587"""
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(FlagDisabled(1578))
    AND_1.Add(FlagEnabled(1571))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableFlag(11020690)
    EnableFlag(11020691)


@ContinueOnRest(11020588)
def Event_11020588(_, character: int, first_flag: int, last_flag: int, flag: int, flag_1: int, flag_2: int):
    """Event 11020588"""
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(FlagDisabled(1578))
    AND_1.Add(FlagEnabled(1572))
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(FlagDisabled(1578))
    AND_2.Add(FlagEnabled(1577))
    AND_3.Add(FlagDisabled(1574))
    AND_3.Add(FlagDisabled(1578))
    AND_3.Add(FlagEnabled(1573))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(6, input_condition=AND_3)
    EnableRandomFlagInRange(flag_range=(11025120, 11025122))
    
    MAIN.Await(FlagEnabled(11025120))
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    End()
    if FlagEnabled(11020691):
        DisableFlagRange((first_flag, last_flag))
        EnableFlag(flag_1)
        EnableCharacter(character)
        End()
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_2)
    EnableCharacter(character)


@ContinueOnRest(11020589)
def Event_11020589(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020589"""
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(FlagDisabled(1578))
    OR_1.Add(FlagEnabled(1570))
    OR_1.Add(FlagEnabled(1577))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(3))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableFlag(11020690)


@ContinueOnRest(11020410)
def Event_11020410(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020410"""
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(FlagDisabled(1578))
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    OR_1.Add(FlagEnabled(1577))
    AND_1.Add(OR_1)
    AND_2.Add(FlagEnabled(812))
    AND_2.Add(FlagEnabled(813))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11500200))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11020411)
def Event_11020411(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020411"""
    AND_1.Add(FlagDisabled(1622))
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_1.Add(FlagEnabled(1624))
    AND_1.Add(FlagEnabled(7))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020412)
def Event_11020412(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020412"""
    AND_1.Add(FlagDisabled(1434))
    AND_1.Add(FlagDisabled(1435))
    AND_1.Add(FlagEnabled(1430))
    AND_1.Add(FlagEnabled(11010700))
    AND_1.Add(FlagEnabled(11400200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11020413)
def Event_11020413(_, character: int, flag: int):
    """Event 11020413"""
    if ThisEventFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlag(1434)
    EnableFlag(flag)


@ContinueOnRest(11020420)
def Event_11020420(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020420"""
    AND_1.Add(FlagEnabled(1640))
    AND_1.Add(FlagEnabled(11010700))
    AND_2.Add(FlagEnabled(1640))
    AND_2.Add(FlagEnabled(11400200))
    AND_3.Add(FlagEnabled(1641))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    SetStandbyAnimationSettings(character, standby_animation=9000)


@ContinueOnRest(11020421)
def Event_11020421(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020421"""
    AND_1.Add(FlagEnabled(1641))
    AND_1.Add(FlagEnabled(11010700))
    AND_1.Add(FlagEnabled(11400200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    SetStandbyAnimationSettings(character, standby_animation=7003)


@ContinueOnRest(11020422)
def Event_11020422(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020422"""
    AND_1.Add(FlagEnabled(1642))
    AND_1.Add(FlagEnabled(710))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020423)
def Event_11020423(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020423"""
    AND_1.Add(FlagEnabled(1643))
    AND_1.Add(FlagEnabled(820))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11020424)
def Event_11020424(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020424"""
    AND_1.Add(FlagEnabled(1649))
    AND_1.Add(FlagEnabled(11020598))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11020425)
def Event_11020425(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11020425"""
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    OR_1.Add(FlagEnabled(11020598))
    AND_2.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(character) > 0.0)
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=15.0))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11026200)
def Event_11026200():
    """Event 11026200"""
    OR_1.Add(FlagEnabled(1643))
    OR_1.Add(FlagEnabled(1644))
    OR_1.Add(FlagEnabled(1645))
    AND_1.Add(OR_1)
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_1.Add(FlagEnabled(820))
    
    MAIN.Await(AND_1)
    
    DisableFlag(820)
    EnableFlag(830)
    EnableCharacter(6331)
    PlayCutscene(100240, cutscene_flags=0, player_id=10000, move_to_region=1802110, game_map=KILN_OF_THE_FIRST_FLAME)
    PlayCutscene(180040, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(822)
    Restart()


@ContinueOnRest(11026210)
def Event_11026210():
    """Event 11026210"""
    DisableFlag(1650)
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_1.Add(EntityBeyondDistance(entity=6330, other_entity=PLAYER, radius=30.0))
    AND_1.Add(FlagDisabled(830))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(FlagEnabled(1643))
    OR_1.Add(FlagEnabled(1644))
    OR_1.Add(FlagEnabled(1645))
    if not OR_1:
        return
    DisableFlagRange((11026211, 11026213))
    EnableRandomFlagInRange(flag_range=(11026211, 11026213))
    if FlagEnabled(11026211):
        return
    EnableFlag(1650)
    SetStandbyAnimationSettings(6330, standby_animation=9001)
    
    MAIN.Await(Attacked(attacked_entity=6330, attacker=PLAYER))
    
    AddSpecialEffect(6330, 5450)
    SetStandbyAnimationSettings(6330, standby_animation=7003)
    ForceAnimation(6330, 9061, wait_for_completion=True)
    DisableFlag(1650)


@ContinueOnRest(11020110)
def Event_11020110():
    """Event 11020110"""
    EnableImmortality(6060)
    if FlagEnabled(11020101):
        return
    if FlagDisabled(11020100):
        MAIN.Await(FlagEnabled(1141))
    EzstateAIRequest(6060, command_id=1702, command_slot=0)
    EnableFlag(11020100)
    if FlagDisabled(11020111):
        MAIN.Await(FlagEnabled(11020609))
    
        EzstateAIRequest(6060, command_id=1701, command_slot=0)
        EnableFlag(11020111)
    
        MAIN.Await(CharacterHasTAEEvent(6060, tae_event_id=1701))
    EnableFlag(11020101)
