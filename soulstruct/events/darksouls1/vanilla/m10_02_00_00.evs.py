"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11020992, obj=1021960, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=10)
    SkipLinesIfFlagOff(1, 11020108)
    RegisterBonfire(11020992, obj=1021960, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=30)
    SkipLinesIfFlagOff(4, 11020300)
    SkipLinesIfFlagOn(2, 11020302)
    EndOfAnimation(1021000, 11)
    SkipLines(1)
    EndOfAnimation(1021000, 12)
    RunEvent(11020300)
    RunEvent(11025050)
    RunEvent(11020001)
    RunEvent(11020020)
    RunEvent(11020021)
    RunEvent(11020105)
    RunEvent(11020106)
    RunEvent(11020108)
    RunEvent(11020120, slot=0, args=(11020120, 10010874, 1021465, 10010883, 2015))
    RunEvent(11020350)
    RunEvent(11020351)
    RunEvent(11020352)
    RunEvent(11025150)
    RunEvent(11020700, slot=0, args=(1021650, 11020700))
    RunEvent(11020700, slot=1, args=(1021651, 11020701))
    RunEvent(11020700, slot=2, args=(1021652, 11020702))
    RunEvent(11020700, slot=3, args=(1021653, 11020703))
    RunEvent(11025200, slot=0, args=(1020203, 1020203, 4.0, 0.0), arg_types="iiff")
    RunEvent(11025200, slot=1, args=(1020203, 1020204, 4.0, 0.8999999761581421), arg_types="iiff")
    RunEvent(11025200, slot=2, args=(1020205, 1020205, 3.0, 0.0), arg_types="iiff")
    RunEvent(11025200, slot=3, args=(1020205, 1020206, 3.0, 0.699999988079071), arg_types="iiff")
    RunEvent(11025200, slot=6, args=(1020200, 1020200, 11.0, 0.0), arg_types="iiff")
    RunEvent(11025200, slot=7, args=(1020200, 1020201, 11.0, 1.5), arg_types="iiff")
    RunEvent(11025200, slot=8, args=(1020202, 1020202, 7.0, 0.0), arg_types="iiff")
    RunEvent(11025200, slot=9, args=(1020202, 1020214, 7.0, 1.100000023841858), arg_types="iiff")
    RunEvent(11025200, slot=10, args=(1020209, 1020209, 11.0, 0.0), arg_types="iiff")
    RunEvent(11025200, slot=11, args=(1020209, 1020210, 11.0, 0.800000011920929), arg_types="iiff")
    RunEvent(11025200, slot=12, args=(1020209, 1020211, 11.0, 1.5), arg_types="iiff")
    RunEvent(11025200, slot=13, args=(1020209, 1020212, 11.0, 2.200000047683716), arg_types="iiff")
    RunEvent(11025200, slot=14, args=(1020213, 1020213, 3.0, 0.0), arg_types="iiff")


def Event11020899(_, arg_0_3: int, arg_4_7: int):
    """ 11020899: Event 11020899 """
    EndIfClient()
    SkipLinesIfFlagOn(4, 11020898)
    EnableFlag(11020898)
    EndOfAnimation(1021690, 0)
    DisableObjectActivation(1021690, obj_act_id=-1)
    End()
    WaitFrames(1)
    SkipLinesIfFlagOff(20, 11025300)
    IfObjectActivated(0, obj_act_id=11020704)
    WaitFrames(10)
    EnableTreasure(1021700)
    EnableTreasure(1021701)
    EnableTreasure(1021702)
    EnableTreasure(1021703)
    EnableTreasure(1021704)
    EnableTreasure(1021705)
    EnableTreasure(1021706)
    EnableTreasure(1021707)
    EnableTreasureCollection(1021700)
    EnableTreasureCollection(1021701)
    EnableTreasureCollection(1021702)
    EnableTreasureCollection(1021703)
    EnableTreasureCollection(1021704)
    EnableTreasureCollection(1021705)
    EnableTreasureCollection(1021706)
    EnableTreasureCollection(1021707)
    EnableFlagRange((arg_0_3, arg_4_7))
    End()
    EndOfAnimation(1021690, 0)
    DisableObjectActivation(1021690, obj_act_id=-1)


def Event11020800(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_12_15: int, arg_16_19: int):
    """ 11020800: Event 11020800 """
    EndIfClient()
    IfFlagOn(1, arg_0_3)
    IfFlagOff(1, arg_4_7)
    IfPlayerDoesNotHaveItem(1, arg_12_15, item_type=arg_8_8, including_box=True)
    SkipLinesIfNotEqual(1, left=50000082, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 201, including_box=True)
    SkipLinesIfNotEqual(1, left=8131, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 203, including_box=True)
    SkipLinesIfNotEqual(1, left=8132, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 205, including_box=True)
    SkipLinesIfNotEqual(1, left=8133, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 207, including_box=True)
    SkipLinesIfNotEqual(1, left=8134, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 209, including_box=True)
    SkipLinesIfNotEqual(1, left=8135, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 211, including_box=True)
    SkipLinesIfNotEqual(1, left=8136, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 213, including_box=True)
    SkipLinesIfNotEqual(1, left=8137, right=arg_0_3)
    IfPlayerDoesNotHaveGood(1, 215, including_box=True)
    EndIfConditionFalse(1)
    EnableFlag(11025300)
    IfObjectActivated(0, obj_act_id=11020704)
    DisableFlag(arg_16_19)


def Preconstructor():
    """ 50: Event 50 """
    EnableFlagRange((50004000, 50004070))
    RunEvent(11020800, slot=0, args=(51010140, 703, 3, 2001, 50004000), arg_types="iiBii")
    RunEvent(11020800, slot=1, args=(11017140, 703, 3, 2002, 50004001), arg_types="iiBii")
    RunEvent(11020800, slot=2, args=(51500150, 703, 3, 2003, 50004002), arg_types="iiBii")
    RunEvent(11020800, slot=3, args=(51700990, 703, 3, 2004, 50004003), arg_types="iiBii")
    RunEvent(11020800, slot=4, args=(51700630, 703, 3, 2005, 50004004), arg_types="iiBii")
    RunEvent(11020800, slot=5, args=(51700590, 703, 3, 2006, 50004005), arg_types="iiBii")
    RunEvent(11020800, slot=6, args=(50001500, 703, 3, 2007, 50004006), arg_types="iiBii")
    RunEvent(11020800, slot=7, args=(51400500, 703, 3, 2008, 50004007), arg_types="iiBii")
    RunEvent(11020800, slot=8, args=(51100140, 703, 3, 2009, 50004008), arg_types="iiBii")
    RunEvent(11020800, slot=9, args=(51810000, 703, 3, 2010, 50004009), arg_types="iiBii")
    RunEvent(11020800, slot=10, args=(50001660, 703, 3, 2011, 50004010), arg_types="iiBii")
    RunEvent(11020800, slot=11, args=(50000080, 703, 3, 2012, 50004011), arg_types="iiBii")
    RunEvent(11020800, slot=12, args=(50000100, 703, 3, 2013, 50004012), arg_types="iiBii")
    RunEvent(11020800, slot=13, args=(50001510, 703, 3, 2014, 50004013), arg_types="iiBii")
    RunEvent(11020800, slot=14, args=(11027030, 11027030, 3, 2015, 50004014), arg_types="iiBii")
    RunEvent(11020800, slot=15, args=(51020210, 703, 3, 2016, 50004015), arg_types="iiBii")
    RunEvent(11020800, slot=16, args=(51010000, 703, 3, 2017, 50004016), arg_types="iiBii")
    RunEvent(11020800, slot=17, args=(51000240, 703, 3, 2018, 50004017), arg_types="iiBii")
    RunEvent(11020800, slot=18, args=(51200140, 703, 3, 2019, 50004018), arg_types="iiBii")
    RunEvent(11020800, slot=19, args=(51700210, 703, 3, 2020, 50004019), arg_types="iiBii")
    RunEvent(11020800, slot=20, args=(11017030, 703, 3, 2021, 50004020), arg_types="iiBii")
    RunEvent(11020800, slot=21, args=(50001560, 11800201, 3, 2500, 50004021), arg_types="iiBii")
    RunEvent(11020800, slot=22, args=(50001580, 11800202, 3, 2501, 50004022), arg_types="iiBii")
    RunEvent(11020800, slot=23, args=(50001630, 11800203, 3, 2502, 50004023), arg_types="iiBii")
    RunEvent(11020800, slot=24, args=(50001640, 11800204, 3, 2503, 50004024), arg_types="iiBii")
    RunEvent(11020800, slot=25, args=(50000090, 11800100, 3, 2510, 50004025), arg_types="iiBii")
    RunEvent(11020800, slot=26, args=(50001540, 703, 2, 138, 50004026), arg_types="iiBii")
    RunEvent(11020800, slot=27, args=(50001670, 703, 2, 139, 50004027), arg_types="iiBii")
    RunEvent(11020800, slot=28, args=(50000000, 703, 3, 100, 50004028), arg_types="iiBii")
    RunEvent(11020800, slot=29, args=(51100330, 703, 3, 101, 50004029), arg_types="iiBii")
    RunEvent(11020800, slot=30, args=(50000390, 703, 3, 102, 50004030), arg_types="iiBii")
    RunEvent(11020800, slot=31, args=(200, 703, 3, 103, 50004031), arg_types="iiBii")
    RunEvent(11020800, slot=32, args=(11017020, 703, 3, 106, 50004032), arg_types="iiBii")
    RunEvent(11020800, slot=33, args=(11607020, 703, 3, 108, 50004033), arg_types="iiBii")
    RunEvent(11020800, slot=34, args=(11407080, 703, 3, 112, 50004034), arg_types="iiBii")
    RunEvent(11020800, slot=35, args=(50000360, 703, 3, 113, 50004035), arg_types="iiBii")
    RunEvent(11020800, slot=36, args=(50000260, 703, 3, 114, 50004036), arg_types="iiBii")
    RunEvent(11020800, slot=37, args=(200, 703, 3, 117, 50004037), arg_types="iiBii")
    RunEvent(11020800, slot=38, args=(50000082, 8131, 3, 200, 50004038), arg_types="iiBii")
    RunEvent(11020800, slot=39, args=(8131, 8132, 3, 202, 50004039), arg_types="iiBii")
    RunEvent(11020800, slot=40, args=(8132, 8133, 3, 204, 50004040), arg_types="iiBii")
    RunEvent(11020800, slot=41, args=(8133, 8134, 3, 206, 50004041), arg_types="iiBii")
    RunEvent(11020800, slot=42, args=(8134, 8135, 3, 208, 50004042), arg_types="iiBii")
    RunEvent(11020800, slot=43, args=(8135, 8136, 3, 210, 50004043), arg_types="iiBii")
    RunEvent(11020800, slot=44, args=(8136, 8137, 3, 212, 50004044), arg_types="iiBii")
    RunEvent(11020800, slot=45, args=(8137, 703, 3, 214, 50004045), arg_types="iiBii")
    RunEvent(11020800, slot=46, args=(51810080, 703, 3, 384, 50004046), arg_types="iiBii")
    RunEvent(11020800, slot=47, args=(11017150, 703, 3, 2600, 50004047), arg_types="iiBii")
    RunEvent(11020800, slot=48, args=(11017160, 703, 3, 2601, 50004048), arg_types="iiBii")
    RunEvent(11020800, slot=49, args=(11017170, 703, 3, 2602, 50004049), arg_types="iiBii")
    RunEvent(11020800, slot=50, args=(50001550, 703, 3, 2607, 50004050), arg_types="iiBii")
    RunEvent(11020800, slot=51, args=(11007010, 703, 3, 2608, 50004051), arg_types="iiBii")
    RunEvent(11020800, slot=52, args=(50000360, 703, 2, 102, 50004052), arg_types="iiBii")
    RunEvent(11020800, slot=53, args=(50000160, 703, 2, 103, 50004053), arg_types="iiBii")
    RunEvent(11020800, slot=54, args=(50000260, 703, 3, 377, 50004054), arg_types="iiBii")
    RunEvent(11020800, slot=55, args=(50000270, 703, 3, 378, 50004055), arg_types="iiBii")
    RunEvent(11020800, slot=56, args=(51000500, 350, 3, 800, 50004056), arg_types="iiBii")
    RunEvent(11020800, slot=57, args=(51600500, 351, 3, 801, 50004057), arg_types="iiBii")
    RunEvent(11020800, slot=58, args=(51700600, 352, 3, 802, 50004058), arg_types="iiBii")
    RunEvent(11020800, slot=59, args=(51700530, 356, 3, 806, 50004059), arg_types="iiBii")
    RunEvent(11020800, slot=60, args=(51200500, 357, 3, 807, 50004060), arg_types="iiBii")
    RunEvent(11020800, slot=61, args=(51200141, 358, 3, 808, 50004061), arg_types="iiBii")
    RunEvent(11020800, slot=62, args=(51310500, 359, 3, 809, 50004062), arg_types="iiBii")
    RunEvent(11020800, slot=63, args=(51100370, 360, 3, 810, 50004063), arg_types="iiBii")
    RunEvent(11020800, slot=64, args=(51410100, 362, 3, 812, 50004064), arg_types="iiBii")
    RunEvent(11020800, slot=65, args=(51410530, 363, 3, 813, 50004065), arg_types="iiBii")
    RunEvent(11020800, slot=66, args=(11007020, 703, 3, 2100, 50004066), arg_types="iiBii")
    RunEvent(11020800, slot=67, args=(51210981, 703, 3, 2022, 50004067), arg_types="iiBii")
    RunEvent(11020800, slot=68, args=(51700930, 703, 3, 2520, 50004068), arg_types="iiBii")
    RunEvent(11020800, slot=69, args=(50001200, 703, 3, 118, 50004069), arg_types="iiBii")
    RunEvent(11020800, slot=70, args=(11017210, 703, 3, 385, 50004070), arg_types="iiBii")
    RunEvent(11020899, slot=0, args=(50004000, 50004070))
    EnableFlag(11020120)
    EnableFlag(61020120)
    HumanityRegistration(6031, 8334)
    SkipLinesIfFlagOn(2, 1092)
    SkipLinesIfFlagOn(1, 1096)
    DisableCharacter(6031)
    RunEvent(11020510, slot=0, args=(6031, 1096))
    RunEvent(11020530, slot=0, args=(6031, 1090, 1109, 1097))
    RunEvent(11020550, slot=0, args=(6031, 1090, 1109, 1092))
    RunEvent(11020551, slot=0, args=(6031, 1090, 1109, 1093))
    HumanityRegistration(6041, 8342)
    SkipLinesIfFlagRangeAnyOn(1, (1112, 1114))
    DisableCharacter(6041)
    RunEvent(11020510, slot=1, args=(6041, 1114))
    RunEvent(11020530, slot=1, args=(6041, 1110, 1119, 1115))
    RunEvent(11020552, slot=0, args=(6041, 1110, 1119, 1112))
    RunEvent(11020553, slot=0, args=(6041, 1110, 1119, 1113))
    RunEvent(11020554, slot=0, args=(6041, 1110, 1119, 1117))
    RunEvent(11020110)
    RunEvent(11020555, slot=0, args=(6060, 1140, 1169, 1141))
    RunEvent(11020556, slot=0, args=(6060, 1140, 1169, 1146))
    RunEvent(11020557, slot=0, args=(6060, 1140, 1169, 1142))
    RunEvent(11020558, slot=0, args=(6060, 1140, 1169, 1145))
    HumanityRegistration(6070, 8358)
    SkipLinesIfFlagOn(1, 1171)
    DisableCharacter(6070)
    RunEvent(11020501)
    RunEvent(11020559)
    RunEvent(11020560)
    RunEvent(11020530, slot=2, args=(6070, 1170, 1180, 1177))
    HumanityRegistration(6080, 8366)
    SkipLinesIfFlagOn(1, 1192)
    SkipLines(1)
    DisableCharacter(6080)
    RunEvent(11020564, slot=0, args=(6080, 1190, 1209, 1193))
    RunEvent(11020565, slot=0, args=(6080, 1190, 1209, 1194))
    RunEvent(11020502, slot=0, args=(6080, 1197))
    RunEvent(11020503, slot=0, args=(6080, 1195))
    RunEvent(11020569, slot=0, args=(6080, 1190, 1209, 1198))
    RunEvent(11020567, slot=0, args=(6080, 1190, 1209, 1196))
    HumanityRegistration(6090, 8374)
    SkipLinesIfFlagOn(1, 1211)
    DisableCharacter(6090)
    RunEvent(11020530, slot=4, args=(6090, 1210, 1219, 1214))
    HumanityRegistration(6100, 8382)
    SkipLinesIfFlagOn(1, 1221)
    DisableCharacter(6100)
    RunEvent(11020530, slot=5, args=(6100, 1220, 1229, 1224))
    HumanityRegistration(6131, 8390)
    SkipLinesIfFlagOn(2, 1252)
    SkipLinesIfFlagOn(1, 1253)
    DisableCharacter(6131)
    RunEvent(11020510, slot=6, args=(6131, 1253))
    RunEvent(11020530, slot=6, args=(6131, 1250, 1259, 1254))
    RunEvent(11020574, slot=0, args=(6131, 1250, 1259, 1252))
    RunEvent(11020575, slot=0, args=(6131, 1250, 1259, 1256))
    HumanityRegistration(6181, 8406)
    SkipLinesIfFlagOn(2, 1314)
    SkipLinesIfFlagOn(1, 1313)
    DisableCharacter(6181)
    RunEvent(11020510, slot=7, args=(6181, 1314))
    RunEvent(11020530, slot=7, args=(6181, 1310, 1319, 1315))
    RunEvent(11020576, slot=0, args=(6181, 1310, 1319, 1313))
    RunEvent(11020504, slot=8, args=(6240, 1411))
    RunEvent(11020530, slot=8, args=(6240, 1410, 1413, 1412))
    HumanityRegistration(6261, 8430)
    SkipLinesIfFlagOn(2, 1434)
    SkipLinesIfFlagOn(1, 1431)
    DisableCharacter(6261)
    RunEvent(11020510, slot=9, args=(6261, 1434))
    RunEvent(11020413, slot=0, args=(6261, 1435))
    RunEvent(11020412, slot=0, args=(6261, 1430, 1459, 1431))
    HumanityRegistration(6270, 8438)
    SkipLinesIfFlagOn(2, 1464)
    SkipLinesIfFlagOn(1, 1462)
    SkipLines(1)
    DisableCharacter(6270)
    RunEvent(11020510, slot=10, args=(6270, 1461))
    RunEvent(11020530, slot=10, args=(6270, 1460, 1464, 1462))
    RunEvent(11020577, slot=0, args=(6270, 1460, 1464, 1464))
    HumanityRegistration(6287, 8446)
    SkipLinesIfFlagOn(2, 1512)
    SkipLinesIfFlagOn(1, 1497)
    DisableCharacter(6287)
    RunEvent(11020510, slot=11, args=(6287, 1512))
    RunEvent(11020530, slot=11, args=(6287, 1490, 1514, 1513))
    RunEvent(11020579, slot=0, args=(6287, 1490, 1514, 1497))
    HumanityRegistration(6292, 8454)
    SkipLinesIfFlagOn(3, 1547)
    SkipLinesIfFlagOn(2, 1545)
    SkipLinesIfFlagOn(1, 1543)
    DisableCharacter(6292)
    RunEvent(11020510, slot=12, args=(6292, 1547))
    RunEvent(11020530, slot=12, args=(6292, 1540, 1569, 1548))
    RunEvent(11020583, slot=0, args=(6292, 1540, 1569, 1543))
    RunEvent(11020584, slot=0, args=(6292, 1540, 1569, 1544))
    RunEvent(11020585, slot=0, args=(6292, 1540, 1569, 1545))
    RunEvent(11020586, slot=0, args=(6292,))
    HumanityRegistration(6301, 8462)
    SkipLinesIfFlagOn(3, 1572)
    SkipLinesIfFlagOn(2, 1574)
    SkipLinesIfFlagOn(1, 1577)
    DisableCharacter(6301)
    RunEvent(11020510, slot=13, args=(6301, 1574))
    RunEvent(11020530, slot=13, args=(6301, 1570, 1599, 1575))
    RunEvent(11020587, slot=0, args=(6301, 1570, 1599, 1572))
    SkipLinesIfFlagOff(1, 11020690)
    RunEvent(11020588, slot=0, args=(6301, 1570, 1599, 1573, 1572, 1577))
    RunEvent(11020589, slot=0, args=(6301, 1570, 1599, 1577))
    RunEvent(11020410, slot=0, args=(6301, 1570, 1599, 1578))
    HumanityRegistration(6322, 8478)
    SkipLinesIfFlagOn(2, 1627)
    SkipLinesIfFlagOn(1, 1626)
    DisableCharacter(6322)
    RunEvent(11020510, slot=14, args=(6322, 1627))
    RunEvent(11020530, slot=14, args=(6322, 1620, 1629, 1628))
    RunEvent(11020411, slot=0, args=(6322, 1620, 1629, 1626))
    SkipLinesIfFlagOff(2, 15)
    DisableCharacter(6330)
    SkipLinesIfFlagOn(14, 15)
    EnableImmortality(6330)
    DisableGravity(6330)
    SkipLinesIfFlagOn(2, 1647)
    SkipLinesIfFlagOn(1, 1640)
    SkipLines(1)
    DisableCharacter(6330)
    RunEvent(11020420, slot=0, args=(6330, 1640, 1649, 1641))
    RunEvent(11020421, slot=0, args=(6330, 1640, 1649, 1642))
    RunEvent(11020422, slot=0, args=(6330, 1640, 1649, 1643))
    RunEvent(11020423, slot=0, args=(6330, 1640, 1649, 1644))
    RunEvent(11020424, slot=0, args=(6330, 1640, 1649, 1647))
    RunEvent(11020425, slot=0, args=(6330, 1640, 1649, 1647))
    RunEvent(11026200)
    RunEvent(11026210)


def Event11020300():
    """ 11020300: Event 11020300 """
    SkipLinesIfThisEventOff(2)
    RunEvent(11020301)
    End()
    IfThisEventOff(1)
    IfCharacterInsideRegion(1, PLAYER, region=1022003)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11020300)
    EnableFlag(11020302)
    ForceAnimation(1021000, 0, wait_for_completion=True)
    IfCharacterOutsideRegion(2, PLAYER, region=1022001)
    IfCharacterOutsideRegion(2, PLAYER, region=1022002)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()


def Event11020301():
    """ 11020301: Event 11020301 """
    IfSingleplayer(1)
    IfFlagOff(1, 11020302)
    IfCharacterInsideRegion(1, PLAYER, region=1022000)
    IfSingleplayer(2)
    IfFlagOn(2, 11020302)
    IfCharacterInsideRegion(2, PLAYER, region=1022001)
    IfSingleplayer(3)
    IfFlagOn(3, 11020302)
    IfCharacterInsideRegion(3, PLAYER, region=1022002)
    IfSingleplayer(4)
    IfFlagOff(4, 11020302)
    IfCharacterInsideRegion(4, PLAYER, region=1022003)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(8, 2)
    SkipLinesIfFinishedConditionTrue(7, 3)
    EnableFlag(11020302)
    ForceAnimation(1021000, 2, wait_for_completion=True)
    IfCharacterOutsideRegion(5, PLAYER, region=1022001)
    IfCharacterOutsideRegion(5, PLAYER, region=1022002)
    IfConditionTrue(0, input_condition=5)
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()
    DisableFlag(11020302)
    ForceAnimation(1021000, 1, wait_for_completion=True)
    IfCharacterOutsideRegion(6, PLAYER, region=1022000)
    IfCharacterOutsideRegion(6, PLAYER, region=1022003)
    IfConditionTrue(0, input_condition=6)
    ForceAnimation(1021000, 21, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event11025050():
    """ 11025050: Event 11025050 """
    EnableImmortality(1020100)
    IfHealthLessThanOrEqual(0, 1020100, 0.30000001192092896)
    ForceAnimation(1020100, 7000, wait_for_completion=True)
    DisableCharacter(1020100)


def Event11020001():
    """ 11020001: Event 11020001 """
    DisableNetworkSync()
    EndIfThisEventOn()
    SkipLinesIfInsideMap(2, game_map=UNDEAD_ASYLUM)
    IfInsideMap(0, game_map=FIRELINK_SHRINE)
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
    DisableSoundEvent(1023800)
    IfFlagOn(0, 11810000)
    EnableSoundEvent(1023800)
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


@RestartOnRest
def Event11025200(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 11025200: Event 11025200 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_4_7)
    End()
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=arg_8_11)
    DisableNetworkSync()
    Wait(arg_12_15)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=9061)


def Event11020020():
    """ 11020020: Event 11020020 """
    IfActionButton(0, prompt_text=10010506, anchor_entity=1022120, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    EnableFlag(11025060)
    WaitFrames(3)
    IfActionButton(1, prompt_text=10010507, anchor_entity=1022120, anchor_type=CoordEntityType.Region)
    IfCharacterOutsideRegion(2, PLAYER, region=1022120)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11025060)
    RestartEvent(11020021, slot=0)
    ResetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


def Event11020021():
    """ 11020021: Event 11020021 """
    DisableNetworkSync()
    IfFlagOn(0, 11025060)
    SkipLinesIfFlagOn(1, 11020000)
    Wait(20.0)
    PlayCutscene(
        100230, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1812110, move_to_map=UNDEAD_ASYLUM
    )
    PlayCutscene(180130, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11020000)
    DisableFlag(11025060)
    ResetStandbyAnimationSettings(PLAYER)
    Restart()


def Event11020105():
    """ 11020105: Event 11020105 """
    DisableTreasure(1021300)
    DisableObject(1021961)
    EndIfFlagOn(11020108)
    SkipLinesIfFlagOn(5, 11020101)
    IfFlagOn(0, 11020100)
    EnableFlag(102)
    EnableTreasure(1021300)
    IfFlagOn(0, 11020101)
    DisableFlag(102)
    IfFlagOn(0, 11020108)
    RegisterBonfire(11020992, obj=1021960, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=30)


def Event11020106():
    """ 11020106: Event 11020106 """
    DisableNetworkSync()
    IfFlagOn(1, 11020100)
    IfFlagOff(1, 11020101)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=1021960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010184,
        anchor_entity=1021960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11020108():
    """ 11020108: Event 11020108 """
    EndIfThisEventOn()
    IfFlagOn(-1, 71020022)
    IfFlagOn(-1, 71020023)
    IfConditionTrue(0, input_condition=-1)
    End()


def Event11020120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11020120: Event 11020120 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfHost(1)
    IfObjectActivated(1, obj_act_id=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    SkipLinesIfClient(5)
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(1)
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11020350():
    """ 11020350: Event 11020350 """
    SkipLinesIfThisEventOn(7)
    DisableObject(1021481)
    DisableCollision(1023510)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    EnableObject(1021481)
    EnableCollision(1023510)
    DisableObject(1021480)
    DisableCollision(1023500)
    DisableMapPiece(1023501)
    DisableCollision(1023502)


def Event11020351():
    """ 11020351: Event 11020351 """
    SkipLinesIfFlagOff(2, 0)
    DisableCollision(0)
    DisableCollision(0)
    IfCharacterInsideRegion(0, PLAYER, region=1022111)
    SkipLinesIfFlagOn(2, 710)
    Kill(PLAYER, award_souls=False)
    End()
    PlayCutscene(
        180060,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1802110,
        move_to_map=KILN_OF_THE_FIRST_FLAME,
    )
    WaitFrames(1)
    Restart()


def Event11020352():
    """ 11020352: Event 11020352 """
    IfFlagOn(0, 710)
    DisableCollision(1023600)
    DisableCollision(1023601)


def Event11020700(_, arg_0_3: int, arg_4_7: int):
    """ 11020700: Event 11020700 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event11025150():
    """ 11025150: Event 11025150 """
    IfCharacterInsideRegion(0, PLAYER, region=1022710)
    AICommand(1020190, command_id=1, slot=3)
    AICommand(1020160, command_id=1, slot=3)
    AICommand(1020161, command_id=1, slot=3)
    AICommand(1020163, command_id=1, slot=3)
    AICommand(1020165, command_id=1, slot=3)
    AICommand(1020166, command_id=1, slot=3)
    ReplanAI(1020190)
    ReplanAI(1020160)
    ReplanAI(1020161)
    ReplanAI(1020163)
    ReplanAI(1020165)
    ReplanAI(1020166)
    IfCharacterOutsideRegion(0, PLAYER, region=1022710)
    AICommand(1020190, command_id=-1, slot=3)
    AICommand(1020160, command_id=-1, slot=3)
    AICommand(1020161, command_id=-1, slot=3)
    AICommand(1020163, command_id=-1, slot=3)
    AICommand(1020165, command_id=-1, slot=3)
    AICommand(1020166, command_id=-1, slot=3)
    ReplanAI(1020190)
    ReplanAI(1020160)
    ReplanAI(1020161)
    ReplanAI(1020163)
    ReplanAI(1020165)
    ReplanAI(1020166)
    Restart()


def Event11020510(_, arg_0_3: int, arg_4_7: int):
    """ 11020510: Event 11020510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11020530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020530: Event 11020530 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfCharacterInsideRegion(2, arg_0_3, region=1022300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    Kill(arg_0_3, award_souls=True)
    DisableGravity(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020501():
    """ 11020501: Event 11020501 """
    IfFlagOn(1, 11010902)
    IfFlagOff(1, 11020693)
    IfFlagOff(1, 1176)
    IfFlagRangeAllOff(1, (1193, 1196))
    IfHealthLessThanOrEqual(2, 6070, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1177)
    IfAttacked(2, 6070, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(3, 6080, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1198)
    IfAttacked(3, 6080, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(4, 6090, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1214)
    IfAttacked(4, 6090, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(5, 6100, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1224)
    IfAttacked(5, 6100, attacking_character=PLAYER)
    IfFlagOn(6, 1197)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(1, input_condition=-1)
    IfThisEventOn(7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFlagOn(2, 1177)
    EnableFlag(1176)
    EnableCharacter(6070)
    SetTeamType(6070, TeamType.HostileAlly)
    SkipLinesIfFlagOn(2, 1198)
    EnableFlag(1197)
    EnableCharacter(6080)
    SetTeamType(6080, TeamType.HostileAlly)
    SkipLinesIfFlagOn(2, 1214)
    EnableFlag(1213)
    EnableCharacter(6090)
    SetTeamType(6090, TeamType.HostileAlly)
    SkipLinesIfFlagOn(2, 1224)
    EnableFlag(1223)
    EnableCharacter(6100)
    SetTeamType(6100, TeamType.HostileAlly)
    SaveRequest()


def Event11020502(_, arg_0_3: int, arg_4_7: int):
    """ 11020502: Event 11020502 """
    IfFlagOff(7, 11010902)
    IfFlagOff(7, 1195)
    IfFlagOff(7, 1197)
    IfFlagOn(7, 1202)
    IfFlagOn(6, 11010902)
    IfFlagOff(6, 1195)
    IfFlagOff(6, 1197)
    IfFlagOn(6, 1193)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11020503(_, arg_0_3: int, arg_4_7: int):
    """ 11020503: Event 11020503 """
    IfFlagOff(1, 1197)
    IfFlagOn(1, 1194)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11020504(_, arg_0_3: int, arg_4_7: int):
    """ 11020504: Event 11020504 """
    IfFlagOff(1, 1411)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 1)
    Move(arg_0_3, destination=1022700, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(arg_0_3, 1022700)
    End()
    SetTeamType(arg_0_3, TeamType.Enemy)
    SetNest(arg_0_3, 1022700)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=1022700)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    EnableFlag(arg_4_7)


def Event11020550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020550: Event 11020550 """
    IfFlagOff(1, 1096)
    IfFlagOff(1, 1099)
    IfFlagOn(1, 1091)
    IfFlagOn(1, 11500594)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020551(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020551: Event 11020551 """
    IfFlagOff(1, 1096)
    IfFlagOff(1, 1099)
    IfFlagOn(1, 1092)
    IfFlagOn(1, 11020603)
    IfOutsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11020694)
    DisableCharacter(arg_0_3)


def Event11020552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020552: Event 11020552 """
    IfFlagOff(1, 1114)
    IfFlagOff(1, 1117)
    IfFlagOn(1, 1111)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020553(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020553: Event 11020553 """
    IfFlagOff(1, 1114)
    IfFlagOff(1, 1117)
    IfFlagOn(1, 1112)
    IfFlagOn(1, 11020694)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020554(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020554: Event 11020554 """
    IfFlagOff(1, 1114)
    IfFlagOff(1, 1117)
    IfFlagOn(1, 1113)
    IfFlagOn(1, 723)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    EndIfConditionFalse(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020555(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020555: Event 11020555 """
    IfFlagOn(1, 1140)
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1575)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-1, input_condition=2)
    IfFlagOn(-1, 11500200)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020556(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020556: Event 11020556 """
    IfFlagOn(1, 1141)
    IfFlagOn(1, 810)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020557(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020557: Event 11020557 """
    IfFlagOn(1, 1146)
    IfFlagOn(1, 11020609)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020558(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020558: Event 11020558 """
    IfFlagOn(1, 1142)
    IfFlagOn(1, 11800200)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020559():
    """ 11020559: Event 11020559 """
    IfFlagOn(1, 1170)
    IfFlagOn(1, 11010902)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1170, 1189))
    EnableFlag(1171)
    EnableCharacter(6070)
    DisableFlagRange((1210, 1219))
    EnableFlag(1211)
    EnableCharacter(6090)
    DisableFlagRange((1220, 1229))
    EnableFlag(1221)
    EnableCharacter(6100)


def Event11020560():
    """ 11020560: Event 11020560 """
    IfFlagRangeAllOff(7, (1176, 1181))
    IfFlagOn(7, 1171)
    IfFlagRangeAllOff(7, (1195, 1198))
    IfFlagOn(7, 1202)
    IfFlagRangeAllOff(7, (1213, 1215))
    IfFlagOn(7, 1211)
    IfFlagRangeAllOff(7, (1223, 1225))
    IfFlagOn(7, 1221)
    IfConditionTrue(1, input_condition=7)
    IfFlagOn(1, 11020600)
    IfThisEventOff(1)
    IfConditionTrue(2, input_condition=7)
    IfFlagOn(2, 11300005)
    IfConditionTrue(3, input_condition=7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
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


def Event11020564(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020564: Event 11020564 """
    IfFlagOff(1, 1195)
    IfFlagOff(1, 1197)
    IfFlagOn(1, 1192)
    EndIfConditionFalse(1)
    SkipLinesIfFlagOn(2, 11020692)
    EnableFlag(11020692)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020565(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020565: Event 11020565 """
    IfFlagOff(1, 1195)
    IfFlagOff(1, 1197)
    IfFlagOn(1, 1193)
    IfFlagOn(1, 11020608)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020567(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020567: Event 11020567 """
    IfFlagOn(-2, 1194)
    IfFlagOn(-2, 1195)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1196)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11020569(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020569: Event 11020569 """
    IfFlagOff(1, 1194)
    IfFlagOff(1, 1195)
    IfFlagOff(1, 1196)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1198)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11020574(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020574: Event 11020574 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1251)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020575(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020575: Event 11020575 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1252)
    IfFlagOn(1, 11020102)
    IfFlagOn(1, 11020103)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020576(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020576: Event 11020576 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1312)
    IfFlagOn(1, 11600593)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020577(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020577: Event 11020577 """
    IfFlagOff(1, 1461)
    IfFlagOff(1, 1464)
    IfFlagOn(1, 1460)
    IfFlagOn(1, 11020597)
    IfOutsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020579(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020579: Event 11020579 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1494)
    IfFlagOn(1, 11510590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020583(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020583: Event 11020583 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1542)
    IfFlagOn(1, 11700593)
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1513)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020584(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020584: Event 11020584 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1543)
    IfFlagOn(1, 11020605)
    IfThisEventOff(1)
    IfFlagOff(2, 1547)
    IfFlagOn(2, 1543)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020585(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020585: Event 11020585 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1544)
    IfFlagOn(1, 11410593)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020586(_, arg_0_3: int):
    """ 11020586: Event 11020586 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1545)
    IfFlagOn(1, 11020606)
    IfThisEventOff(1)
    IfFlagOff(2, 1547)
    IfFlagOn(2, 1545)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableCharacter(arg_0_3)


def Event11020587(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020587: Event 11020587 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(1, 1571)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(11020690)
    EnableFlag(11020691)


def Event11020588(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11020588: Event 11020588 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(1, 1572)
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(2, 1577)
    IfFlagOff(3, 1574)
    IfFlagOff(3, 1578)
    IfFlagOn(3, 1573)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(6, 3)
    EnableRandomFlagInRange((11025120, 11025122))
    IfFlagOn(0, 11025120)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    End()
    SkipLinesIfFlagOff(4, 11020691)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    EnableCharacter(arg_0_3)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_20_23)
    EnableCharacter(arg_0_3)


def Event11020589(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020589: Event 11020589 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(-1, 1570)
    IfFlagOn(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 3)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(11020690)


def Event11020410(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020410: Event 11020410 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfFlagOn(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11500200)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020411(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020411: Event 11020411 """
    IfFlagOff(1, 1622)
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1624)
    IfFlagOn(1, 7)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020412(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020412: Event 11020412 """
    IfFlagOff(1, 1434)
    IfFlagOff(1, 1435)
    IfFlagOn(1, 1430)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020413(_, arg_0_3: int, arg_4_7: int):
    """ 11020413: Event 11020413 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlag(1434)
    EnableFlag(arg_4_7)


def Event11020420(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020420: Event 11020420 """
    IfFlagOn(1, 1640)
    IfFlagOn(1, 11010700)
    IfFlagOn(2, 1640)
    IfFlagOn(2, 11400200)
    IfFlagOn(3, 1641)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)


def Event11020421(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020421: Event 11020421 """
    IfFlagOn(1, 1641)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7003)


def Event11020422(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020422: Event 11020422 """
    IfFlagOn(1, 1642)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020423(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020423: Event 11020423 """
    IfFlagOn(1, 1643)
    IfFlagOn(1, 820)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020424(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020424: Event 11020424 """
    IfFlagOn(1, 1649)
    IfFlagOn(1, 11020598)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11020425(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020425: Event 11020425 """
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfFlagOn(-1, 11020598)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(2, arg_0_3, 0.0)
    IfAttacked(2, arg_0_3, attacking_character=PLAYER)
    IfEntityBeyondDistance(2, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11026200():
    """ 11026200: Event 11026200 """
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfFlagOn(1, 820)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(820)
    EnableFlag(830)
    EnableCharacter(6331)
    PlayCutscene(
        100240,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1802110,
        move_to_map=KILN_OF_THE_FIRST_FLAME,
    )
    PlayCutscene(180040, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(822)
    Restart()


def Event11026210():
    """ 11026210: Event 11026210 """
    DisableFlag(1650)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfEntityBeyondDistance(1, 6330, PLAYER, radius=30.0)
    IfFlagOff(1, 830)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    EndIfConditionFalse(-1)
    DisableFlagRange((11026211, 11026213))
    EnableRandomFlagInRange((11026211, 11026213))
    EndIfFlagOn(11026211)
    EnableFlag(1650)
    SetStandbyAnimationSettings(6330, standby_animation=9001)
    IfAttacked(0, 6330, attacking_character=PLAYER)
    AddSpecialEffect(6330, 5450)
    SetStandbyAnimationSettings(6330, standby_animation=7003)
    ForceAnimation(6330, 9061, wait_for_completion=True)
    DisableFlag(1650)


def Event11020110():
    """ 11020110: Event 11020110 """
    EnableImmortality(6060)
    EndIfFlagOn(11020101)
    SkipLinesIfFlagOn(1, 11020100)
    IfFlagOn(0, 1141)
    EzstateAIRequest(6060, command_id=1702, slot=0)
    EnableFlag(11020100)
    SkipLinesIfFlagOn(4, 11020111)
    IfFlagOn(0, 11020609)
    EzstateAIRequest(6060, command_id=1701, slot=0)
    EnableFlag(11020111)
    IfHasTAEEvent(0, 6060, tae_event_id=1701)
    EnableFlag(11020101)
