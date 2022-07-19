"""
Common

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    if Client():
        return
    DisableFlag(760)
    DisableFlag(762)
    DisableFlag(765)
    Event_260(0, flag=11810000, text=10010600, seconds=0.0)
    Event_260(1, flag=257, text=10010610, seconds=0.0)
    Event_260(2, flag=710, text=10010620, seconds=0.0)
    Event_761()
    Event_763()
    Event_290()
    Event_701()
    Event_702()
    Event_717()
    Event_718()
    Event_706()
    Event_740()
    Event_750()
    Event_752()
    Event_757()
    Event_758()
    Event_759()
    Event_754()
    Event_770()
    Event_772()
    Event_730()
    Event_731()
    Event_766()
    Event_710()
    Event_711(0, item=2500, flag=711)
    Event_711(1, item=2501, flag=712)
    Event_711(2, item=2502, flag=713)
    Event_711(3, item=2504, flag=714)
    Event_715()
    Event_716()
    Event_8131(0, item=202, item_1=203)
    Event_8131(1, item=204, item_1=205)
    Event_8131(2, item=206, item_1=207)
    Event_8131(3, item=208, item_1=209)
    Event_8131(4, item=210, item_1=211)
    Event_8131(5, item=212, item_1=213)
    Event_8131(6, item=214, item_1=215)
    Event_819()
    Event_970(0, flag=2, item_lot_param_id=2500, item_lot_param_id_1=9020, item_lot_param_id_2=9030)
    Event_970(1, flag=11010901, item_lot_param_id=0, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(2, flag=11010902, item_lot_param_id=2510, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(3, flag=3, item_lot_param_id=0, item_lot_param_id_1=9020, item_lot_param_id_2=0)
    Event_970(4, flag=4, item_lot_param_id=2520, item_lot_param_id_1=9020, item_lot_param_id_2=0)
    Event_970(5, flag=11200900, item_lot_param_id=2530, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(6, flag=5, item_lot_param_id=2540, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(7, flag=6, item_lot_param_id=2550, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(8, flag=7, item_lot_param_id=2560, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(9, flag=9, item_lot_param_id=2570, item_lot_param_id_1=9020, item_lot_param_id_2=0)
    Event_970(10, flag=11410900, item_lot_param_id=0, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(11, flag=11410410, item_lot_param_id=0, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(12, flag=11410901, item_lot_param_id=0, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(13, flag=10, item_lot_param_id=2580, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(14, flag=11, item_lot_param_id=2590, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(15, flag=11510900, item_lot_param_id=2600, item_lot_param_id_1=0, item_lot_param_id_2=0)
    Event_970(16, flag=11510902, item_lot_param_id=2610, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(17, flag=11510903, item_lot_param_id=2620, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(18, flag=13, item_lot_param_id=2630, item_lot_param_id_1=9010, item_lot_param_id_2=0)
    Event_970(19, flag=14, item_lot_param_id=2640, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(20, flag=15, item_lot_param_id=2650, item_lot_param_id_1=0, item_lot_param_id_2=0)
    Event_970(21, flag=16, item_lot_param_id=2660, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(22, flag=11810900, item_lot_param_id=0, item_lot_param_id_1=9000, item_lot_param_id_2=9030)
    Event_970(23, flag=11210000, item_lot_param_id=2680, item_lot_param_id_1=9000, item_lot_param_id_2=0)
    Event_970(24, flag=11210001, item_lot_param_id=2690, item_lot_param_id_1=0, item_lot_param_id_2=0)
    Event_970(25, flag=17, item_lot_param_id=2700, item_lot_param_id_1=9040, item_lot_param_id_2=0)
    Event_970(26, flag=11210004, item_lot_param_id=2710, item_lot_param_id_1=0, item_lot_param_id_2=0)
    Event_250(0, item=2600, flag=250)
    Event_250(1, item=2601, flag=251)
    Event_250(2, item=2602, flag=252)
    Event_250(3, item=2603, flag=253)
    Event_250(4, item=2604, flag=254)
    Event_250(5, item=2605, flag=255)
    Event_250(6, item=2606, flag=256)
    Event_250(7, item=2607, flag=257)
    Event_250(8, item=2608, flag=258)
    Event_250(9, item=2609, flag=259)
    Event_350(0, flag=350, item=800)
    Event_350(1, flag=351, item=801)
    Event_350(2, flag=352, item=802)
    Event_350(6, flag=356, item=806)
    Event_350(7, flag=357, item=807)
    Event_350(8, flag=358, item=808)
    Event_350(9, flag=359, item=809)
    Event_350(10, flag=360, item=810)
    Event_350(12, flag=362, item=812)
    Event_350(13, flag=363, item=813)
    Event_780(0, item=1000, flag=780)
    Event_780(1, item=1010, flag=781)
    Event_780(2, item=1020, flag=782)
    Event_780(3, item=1030, flag=783)
    Event_780(4, item=1040, flag=784)
    Event_780(5, item=1050, flag=785)
    Event_780(6, item=1060, flag=786)
    Event_780(7, item=1070, flag=787)
    Event_780(8, item=1080, flag=788)
    Event_780(9, item=1090, flag=789)
    Event_780(10, item=1100, flag=790)
    Event_780(11, item=1110, flag=791)
    Event_780(12, item=1120, flag=792)
    Event_780(13, item=1130, flag=793)
    Event_870(0, covenant=0, flag=850)
    Event_870(1, covenant=1, flag=851)
    Event_870(2, covenant=2, flag=852)
    Event_870(3, covenant=3, flag=853)
    Event_870(4, covenant=4, flag=854)
    Event_870(5, covenant=5, flag=855)
    Event_870(6, covenant=6, flag=856)
    Event_870(7, covenant=7, flag=857)
    Event_870(8, covenant=8, flag=858)
    Event_870(9, covenant=9, flag=859)
    Event_840(0, 840, 7905, 6370, -1)
    Event_840(1, 841, 7905, 6072, -1)
    Event_840(2, 842, 7905, 6080, -1)
    Event_840(3, 843, 7905, 6001, -1)
    Event_840(4, flag=844, animation_id=7898, target_entity=10000, animation_id_1=7896)
    Event_840(5, 845, 7905, 6340, -1)
    Event_840(6, 846, 7905, 6341, -1)
    Event_840(7, flag=847, animation_id=7913, target_entity=10000, animation_id_1=7911)
    Event_840(8, 848, 7905, 6380, -1)
    Event_840(9, 849, 7905, 1400700, -1)
    Event_690(0, flag=600, bit_count=4, max_value=16, flag_1=1175)
    Event_719()
    Event_720()
    Event_721()
    Event_722()
    Event_723()
    Event_724()
    Event_725()
    Event_726()
    Event_727()
    Event_745()
    Event_818()
    Event_810()
    Event_812(0, flag=51400350)
    Event_812(1, flag=51010050)
    Event_822()
    Event_823()
    Event_910(0, flag=11400591, item_lot_param_id=1280)
    Event_911(0, flag=11010591, item_lot_param_id=1000, state=1)
    Event_911(1, flag=11510590, item_lot_param_id=1010, state=1)
    Event_911(2, flag=11700591, item_lot_param_id=1020, state=1)
    Event_911(3, flag=11000591, item_lot_param_id=1030, state=1)
    Event_911(4, flag=11400590, item_lot_param_id=1040, state=1)
    Event_911(5, flag=11410594, item_lot_param_id=1050, state=1)
    Event_911(6, flag=11020594, item_lot_param_id=1060, state=1)
    Event_911(7, flag=11020595, item_lot_param_id=1070, state=1)
    Event_911(8, flag=11810590, item_lot_param_id=1082, state=1)
    Event_911(9, flag=11810591, item_lot_param_id=1080, state=1)
    Event_911(10, flag=11510592, item_lot_param_id=1090, state=1)
    Event_911(11, flag=11600592, item_lot_param_id=1100, state=1)
    Event_911(12, flag=11020602, item_lot_param_id=1110, state=1)
    Event_911(13, flag=11010594, item_lot_param_id=1120, state=1)
    Event_911(14, flag=11010595, item_lot_param_id=1130, state=1)
    Event_911(15, flag=11020599, item_lot_param_id=1140, state=1)
    Event_911(16, flag=11020607, item_lot_param_id=1150, state=1)
    Event_911(17, flag=11200592, item_lot_param_id=1160, state=1)
    Event_911(18, flag=11200593, item_lot_param_id=1170, state=1)
    Event_911(19, flag=11200594, item_lot_param_id=1180, state=1)
    Event_911(20, flag=11300590, item_lot_param_id=1190, state=1)
    Event_911(21, flag=11300591, item_lot_param_id=1200, state=1)
    Event_911(22, flag=11310590, item_lot_param_id=1210, state=1)
    Event_911(23, flag=11310592, item_lot_param_id=1220, state=1)
    Event_911(24, flag=11310593, item_lot_param_id=1230, state=1)
    Event_911(25, flag=11310594, item_lot_param_id=1240, state=1)
    Event_911(26, flag=11320590, item_lot_param_id=1250, state=1)
    Event_911(27, flag=11320581, item_lot_param_id=1260, state=1)
    Event_911(28, flag=11320593, item_lot_param_id=1270, state=1)
    Event_911(29, flag=11400592, item_lot_param_id=1290, state=1)
    Event_911(30, flag=11400594, item_lot_param_id=1300, state=1)
    Event_911(31, flag=11400596, item_lot_param_id=1310, state=1)
    Event_911(32, flag=11400597, item_lot_param_id=1320, state=1)
    Event_911(33, flag=11400598, item_lot_param_id=1330, state=1)
    Event_911(34, flag=11400599, item_lot_param_id=1340, state=1)
    Event_911(35, flag=11510595, item_lot_param_id=1350, state=1)
    Event_911(36, flag=11510596, item_lot_param_id=1360, state=1)
    Event_911(37, flag=11510597, item_lot_param_id=1370, state=1)
    Event_911(38, flag=11600594, item_lot_param_id=1380, state=1)
    Event_911(39, flag=11600595, item_lot_param_id=1390, state=1)
    Event_911(40, flag=11600596, item_lot_param_id=1400, state=1)
    Event_911(41, flag=11010598, item_lot_param_id=1410, state=0)
    Event_911(42, flag=11210590, item_lot_param_id=1500, state=1)
    Event_911(43, flag=11210593, item_lot_param_id=1510, state=1)
    Event_911(44, flag=11210594, item_lot_param_id=1520, state=1)
    Event_911(45, flag=11600580, item_lot_param_id=1401, state=1)
    Event_911(46, flag=11600581, item_lot_param_id=1402, state=1)
    Event_911(47, flag=11600582, item_lot_param_id=1403, state=1)
    Event_911(48, flag=11600583, item_lot_param_id=1404, state=1)
    Event_890(0, flag=11310580, item_lot_param_id=1221, state=1)
    Event_890(1, flag=11510580, item_lot_param_id=1361, state=1)
    Event_890(2, flag=11510581, item_lot_param_id=1371, state=1)
    Event_890(3, flag=11320592, item_lot_param_id=1261, state=1)
    Event_960(0, flag=1322, character=6190, item_lot_param_id=6190)
    Event_960(1, flag=1315, character=6180, item_lot_param_id=1100)
    Event_960(2, flag=1402, character=6230, item_lot_param_id=6230)
    Event_960(3, flag=1402, character=6230, item_lot_param_id=6231)
    Event_8200(0, item_type=3, item=5500, flag=50000120, flag_1=11010594)
    Event_8200(1, item_type=3, item=5510, flag=50000130, flag_1=11010595)
    Event_8200(2, item_type=2, item=103, flag=50000160, flag_1=11200592)
    Event_8200(3, item_type=3, item=240, flag=50000170, flag_1=11200593)
    Event_8200(4, item_type=2, item=124, flag=50000180, flag_1=11200594)
    Event_8200(5, item_type=0, item=453000, flag=50000220, flag_1=11310592)
    Event_8200(6, item_type=3, item=5100, flag=50000225, flag_1=11310580)
    Event_8200(7, item_type=3, item=5110, flag=50000230, flag_1=11310593)
    Event_8200(8, item_type=3, item=114, flag=50000265, flag_1=11320581)
    Event_8200(9, item_type=3, item=377, flag=50000260, flag_1=11320592)
    Event_8200(10, item_type=3, item=378, flag=50000270, flag_1=11320593)
    Event_8200(11, item_type=3, item=4500, flag=50000310, flag_1=11400596)
    Event_8200(12, item_type=3, item=4520, flag=50000320, flag_1=11400597)
    Event_8200(13, item_type=3, item=4510, flag=50000330, flag_1=11400598)
    Event_8200(14, item_type=2, item=130, flag=50000350, flag_1=11510595)
    Event_8200(15, item_type=3, item=113, flag=50000360, flag_1=11510596)
    Event_8200(16, item_type=2, item=102, flag=50000365, flag_1=11510580)
    Event_8200(17, item_type=3, item=5910, flag=50000370, flag_1=11510597)
    Event_8200(18, item_type=0, item=1366000, flag=50000375, flag_1=11510581)
    Event_8200(19, item_type=0, item=904000, flag=50000380, flag_1=11600594)
    Event_8200(20, item_type=3, item=102, flag=50000390, flag_1=11600595)
    Event_8200(21, item_type=0, item=210000, flag=50000400, flag_1=11600596)
    Event_8200(22, item_type=1, item=40000, flag=50000410, flag_1=11600580)
    Event_8200(23, item_type=1, item=41000, flag=50000420, flag_1=11600581)
    Event_8200(24, item_type=1, item=42000, flag=50000430, flag_1=11600582)
    Event_8200(25, item_type=1, item=43000, flag=50000440, flag_1=11600583)
    Event_8300(0, item_type=3, item=100, flag=50000000)
    Event_8300(1, item_type=3, item=101, flag=51100330)
    Event_8300(2, item_type=3, item=102, flag=50000390)
    Event_8300(3, item_type=3, item=106, flag=11017020)
    Event_8300(4, item_type=3, item=108, flag=11607020)
    Event_8300(5, item_type=3, item=112, flag=11407080)
    Event_8300(6, item_type=3, item=2508, flag=11007010)
    Event_8090(0, item_type=3, item=510, flag=11217010)
    Event_8090(1, item_type=3, item=511, flag=11217020)
    Event_8090(2, item_type=3, item=512, flag=11217030)
    Event_8090(3, item_type=3, item=513, flag=11217040)
    Event_8090(4, 3, 514, 11217050)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    SkipLinesIfFlagEnabled(80, 909)
    SkipLinesIfFlagRangeAnyEnabled(1, (1000, 1029))
    EnableFlag(1000)
    SkipLinesIfFlagRangeAnyEnabled(1, (1030, 1059))
    EnableFlag(1030)
    SkipLinesIfFlagRangeAnyEnabled(1, (1060, 1089))
    EnableFlag(1060)
    SkipLinesIfFlagRangeAnyEnabled(1, (1090, 1109))
    EnableFlag(1090)
    SkipLinesIfFlagRangeAnyEnabled(1, (1110, 1119))
    EnableFlag(1110)
    SkipLinesIfFlagRangeAnyEnabled(1, (1120, 1139))
    EnableFlag(1120)
    SkipLinesIfFlagRangeAnyEnabled(1, (1140, 1169))
    EnableFlag(1140)
    SkipLinesIfFlagRangeAnyEnabled(1, (1170, 1189))
    EnableFlag(1170)
    SkipLinesIfFlagRangeAnyEnabled(1, (1190, 1209))
    EnableFlag(1202)
    SkipLinesIfFlagRangeAnyEnabled(1, (1210, 1219))
    EnableFlag(1210)
    SkipLinesIfFlagRangeAnyEnabled(1, (1220, 1229))
    EnableFlag(1220)
    SkipLinesIfFlagRangeAnyEnabled(1, (1230, 1239))
    EnableFlag(1230)
    SkipLinesIfFlagRangeAnyEnabled(1, (1240, 1249))
    EnableFlag(1240)
    SkipLinesIfFlagRangeAnyEnabled(1, (1250, 1259))
    EnableFlag(1250)
    SkipLinesIfFlagRangeAnyEnabled(1, (1270, 1279))
    EnableFlag(1270)
    SkipLinesIfFlagRangeAnyEnabled(1, (1280, 1289))
    EnableFlag(1280)
    SkipLinesIfFlagRangeAnyEnabled(1, (1290, 1309))
    EnableFlag(1290)
    SkipLinesIfFlagRangeAnyEnabled(1, (1310, 1319))
    EnableFlag(1310)
    SkipLinesIfFlagRangeAnyEnabled(1, (1320, 1339))
    EnableFlag(1320)
    SkipLinesIfFlagRangeAnyEnabled(1, (1340, 1359))
    EnableFlag(1340)
    SkipLinesIfFlagRangeAnyEnabled(1, (1360, 1379))
    EnableFlag(1360)
    SkipLinesIfFlagRangeAnyEnabled(1, (1380, 1399))
    EnableFlag(1380)
    SkipLinesIfFlagRangeAnyEnabled(1, (1400, 1409))
    EnableFlag(1400)
    SkipLinesIfFlagRangeAnyEnabled(1, (1410, 1419))
    EnableFlag(1410)
    SkipLinesIfFlagRangeAnyEnabled(1, (1420, 1429))
    EnableFlag(1420)
    SkipLinesIfFlagRangeAnyEnabled(1, (1430, 1459))
    EnableFlag(1430)
    SkipLinesIfFlagRangeAnyEnabled(1, (1460, 1489))
    EnableFlag(1460)
    SkipLinesIfFlagRangeAnyEnabled(1, (1490, 1539))
    EnableFlag(1490)
    SkipLinesIfFlagRangeAnyEnabled(1, (1540, 1569))
    EnableFlag(1540)
    SkipLinesIfFlagRangeAnyEnabled(1, (1570, 1599))
    EnableFlag(1570)
    SkipLinesIfFlagRangeAnyEnabled(1, (1600, 1619))
    EnableFlag(1600)
    SkipLinesIfFlagRangeAnyEnabled(1, (1620, 1639))
    EnableFlag(1620)
    SkipLinesIfFlagRangeAnyEnabled(1, (1640, 1669))
    EnableFlag(1640)
    SkipLinesIfFlagRangeAnyEnabled(1, (1670, 1679))
    EnableFlag(1670)
    SkipLinesIfFlagRangeAnyEnabled(1, (1690, 1699))
    EnableFlag(1690)
    SkipLinesIfFlagRangeAnyEnabled(1, (1700, 1709))
    EnableFlag(1700)
    SkipLinesIfFlagRangeAnyEnabled(1, (1710, 1729))
    EnableFlag(1710)
    SkipLinesIfFlagRangeAnyEnabled(1, (1760, 1769))
    EnableFlag(1760)
    SkipLinesIfFlagRangeAnyEnabled(1, (1770, 1779))
    EnableFlag(1770)
    SkipLinesIfFlagRangeAnyEnabled(1, (1780, 1789))
    EnableFlag(1780)
    SkipLinesIfFlagRangeAnyEnabled(1, (1820, 1839))
    EnableFlag(1820)
    SkipLinesIfFlagRangeAnyEnabled(1, (1840, 1859))
    EnableFlag(1840)
    SkipLinesIfFlagRangeAnyEnabled(1, (1860, 1869))
    EnableFlag(1860)
    SkipLinesIfFlagRangeAnyEnabled(1, (1870, 1889))
    EnableFlag(1870)
    if FlagDisabled(909):
        EnableFlag(11807020)
        EnableFlag(11807030)
        EnableFlag(11807040)
        EnableFlag(11807050)
        EnableFlag(11807060)
        EnableFlag(11807070)
        EnableFlag(11807080)
        EnableFlag(11807090)
        EnableFlag(11807100)
        EnableFlag(11807110)
        EnableFlag(11807120)
        EnableFlag(11807130)
        EnableFlag(11807170)
        EnableFlag(11807180)
        EnableFlag(11807190)
        EnableFlag(11807200)
        EnableFlag(11807210)
        EnableFlag(11807220)
        EnableFlag(11807230)
        EnableFlag(11807240)
        EnableFlag(11217060)
        EnableFlag(11217070)
        EnableFlag(11217080)
        EnableFlag(11217090)
    if FlagDisabled(909):
        EnableFlag(909)
        EnableFlag(814)
        EnableFlag(50006071)
        EnableFlag(50006080)


@NeverRestart(290)
def Event_290():
    """Event 290"""
    if ThisEventFlagEnabled():
        return
    EnableFlagRange((280, 290))
    OR_1.Add(PlayerClass(ClassType.Knight))
    OR_1.Add(PlayerClass(ClassType.Cleric))
    AND_1.Add(OR_1)
    AND_2.Add(not OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    DisableFlag(287)
    End()
    DisableFlag(288)


@NeverRestart(701)
def Event_701():
    """Event 701"""
    if ThisEventFlagEnabled():
        return
    EnableVagrantSpawning()
    
    MAIN.Await(InsideMap(game_map=UNDEAD_ASYLUM))
    
    DisableVagrantSpawning()
    
    MAIN.Await(FlagEnabled(11810000))
    
    EnableVagrantSpawning()


@NeverRestart(702)
def Event_702():
    """Event 702"""
    DisableFlag(702)
    AND_1.Add(FlagDisabled(11800210))
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    
    MAIN.Await(AND_1)
    
    EnableFlag(702)
    OR_1.Add(OutsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_1.Add(FlagEnabled(11800210))
    
    MAIN.Await(OR_1)
    
    DisableFlag(702)
    Restart()


@NeverRestart(717)
def Event_717():
    """Event 717"""
    DisableFlag(717)
    AND_1.Add(FlagDisabled(710))
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    AND_1.Add(PlayerStandingOnCollision(1603300))
    
    MAIN.Await(AND_1)
    
    EnableFlag(717)
    AND_2.Add(PlayerStandingOnCollision(1603300))
    
    MAIN.Await(not AND_2)
    
    DisableFlag(717)
    Restart()


@NeverRestart(718)
def Event_718():
    """Event 718"""
    if FlagDisabled(8120):
        return
    DisplayStatus(10010650)
    DisableFlag(8120)


@NeverRestart(706)
def Event_706():
    """Event 706"""
    MAIN.Await(FlagEnabled(710))
    
    EnableFlag(706)
    OR_1.Add(FlagEnabled(11705170))
    OR_1.Add(InsideMap(game_map=PAINTED_WORLD))
    
    MAIN.Await(OR_1)
    
    DisableFlag(706)
    AND_1.Add(FlagDisabled(11705170))
    AND_1.Add(OutsideMap(game_map=PAINTED_WORLD))
    
    MAIN.Await(AND_1)
    
    Restart()


@NeverRestart(710)
def Event_710():
    """Event 710"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(PlayerHasGood(2510))
    
    EnableFlag(710)


@NeverRestart(711)
def Event_711(_, item: int, flag: int):
    """Event 711"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(PlayerHasGood(item))
    
    EnableFlag(flag)


@NeverRestart(715)
def Event_715():
    """Event 715"""
    DisableFlag(715)
    AND_1.Add(FlagEnabled(11010595))
    AND_1.Add(PlayerHasGood(702))
    AND_1.Add(PlayerDoesNotHaveGood(5520, including_storage=True))
    AND_1.Add(PlayerCovenant(Covenant.WarriorOfSunlight))
    
    MAIN.Await(AND_1)
    
    EnableFlag(715)
    OR_1.Add(PlayerDoesNotHaveGood(702))
    OR_1.Add(PlayerHasGood(5520, including_storage=True))
    AND_2.Add(PlayerCovenant(Covenant.WarriorOfSunlight))
    OR_1.Add(not AND_2)
    
    MAIN.Await(OR_1)
    
    Restart()


@NeverRestart(716)
def Event_716():
    """Event 716"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(50000082))
    
    EnableFlag(716)


@NeverRestart(8131)
def Event_8131(_, item: int, item_1: int):
    """Event 8131"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(PlayerHasGood(item))
    OR_1.Add(PlayerHasGood(item_1))
    
    MAIN.Await(OR_1)
    
    if ValueEqual(left=item, right=202):
        EnableFlag(8131)
    if ValueEqual(left=item, right=204):
        EnableFlagRange((8131, 8132))
    if ValueEqual(left=item, right=206):
        EnableFlagRange((8131, 8133))
    if ValueEqual(left=item, right=208):
        EnableFlagRange((8131, 8134))
    if ValueEqual(left=item, right=210):
        EnableFlagRange((8131, 8135))
    if ValueEqual(left=item, right=212):
        EnableFlagRange((8131, 8136))
    if ValueEqual(left=item, right=214):
        EnableFlagRange((8131, 8137))


@NeverRestart(819)
def Event_819():
    """Event 819"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(11017040))
    OR_1.Add(FlagEnabled(11017170))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11017040)
    EnableFlag(11017170)


@NeverRestart(719)
def Event_719():
    """Event 719"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(PlayerHasGood(3000))
    OR_1.Add(PlayerHasGood(3010))
    OR_1.Add(PlayerHasGood(3020))
    OR_1.Add(PlayerHasGood(3030))
    OR_1.Add(PlayerHasGood(3040))
    OR_1.Add(PlayerHasGood(3050))
    OR_1.Add(PlayerHasGood(3060))
    OR_1.Add(PlayerHasGood(3070))
    OR_1.Add(PlayerHasGood(3100))
    OR_1.Add(PlayerHasGood(3110))
    OR_1.Add(PlayerHasGood(3120))
    OR_1.Add(PlayerHasGood(3300))
    OR_1.Add(PlayerHasGood(3310))
    OR_1.Add(PlayerHasGood(3400))
    OR_1.Add(PlayerHasGood(3410))
    OR_1.Add(PlayerHasGood(3500))
    OR_1.Add(PlayerHasGood(3510))
    OR_1.Add(PlayerHasGood(3520))
    OR_1.Add(PlayerHasGood(3530))
    OR_1.Add(PlayerHasGood(3540))
    OR_1.Add(PlayerHasGood(3550))
    OR_1.Add(PlayerHasGood(3600))
    OR_1.Add(PlayerHasGood(3610))
    OR_1.Add(PlayerHasGood(3700))
    OR_1.Add(PlayerHasGood(4000))
    OR_1.Add(PlayerHasGood(4010))
    OR_1.Add(PlayerHasGood(4020))
    OR_1.Add(PlayerHasGood(4030))
    OR_1.Add(PlayerHasGood(4040))
    OR_1.Add(PlayerHasGood(4050))
    OR_1.Add(PlayerHasGood(4060))
    OR_1.Add(PlayerHasGood(4100))
    OR_1.Add(PlayerHasGood(4110))
    OR_1.Add(PlayerHasGood(4200))
    OR_1.Add(PlayerHasGood(4210))
    OR_1.Add(PlayerHasGood(4220))
    OR_1.Add(PlayerHasGood(4300))
    OR_1.Add(PlayerHasGood(4310))
    OR_1.Add(PlayerHasGood(4360))
    OR_1.Add(PlayerHasGood(4400))
    OR_1.Add(PlayerHasGood(4500))
    OR_1.Add(PlayerHasGood(4510))
    OR_1.Add(PlayerHasGood(4520))
    OR_1.Add(PlayerHasGood(5000))
    OR_1.Add(PlayerHasGood(5010))
    OR_1.Add(PlayerHasGood(5020))
    OR_1.Add(PlayerHasGood(5030))
    OR_1.Add(PlayerHasGood(5040))
    OR_1.Add(PlayerHasGood(5050))
    OR_1.Add(PlayerHasGood(5100))
    OR_1.Add(PlayerHasGood(5110))
    OR_1.Add(PlayerHasGood(5200))
    OR_1.Add(PlayerHasGood(5210))
    OR_1.Add(PlayerHasGood(5300))
    OR_1.Add(PlayerHasGood(5310))
    OR_1.Add(PlayerHasGood(5320))
    OR_1.Add(PlayerHasGood(5400))
    OR_1.Add(PlayerHasGood(5500))
    OR_1.Add(PlayerHasGood(5510))
    OR_1.Add(PlayerHasGood(5520))
    OR_1.Add(PlayerHasGood(5600))
    OR_1.Add(PlayerHasGood(5610))
    OR_1.Add(PlayerHasGood(5700))
    OR_1.Add(PlayerHasGood(5710))
    OR_1.Add(PlayerHasGood(5800))
    OR_1.Add(PlayerHasGood(5810))
    OR_1.Add(PlayerHasGood(5900))
    OR_1.Add(PlayerHasGood(5910))
    OR_1.Add(PlayerHasGood(3710))
    OR_1.Add(PlayerHasGood(3720))
    OR_1.Add(PlayerHasGood(3730))
    OR_1.Add(PlayerHasGood(3740))
    OR_1.Add(PlayerHasGood(4530))
    
    MAIN.Await(OR_1)
    
    EnableFlag(719)


@NeverRestart(720)
def Event_720():
    """Event 720"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(PlayerHasGood(4020))
    OR_1.Add(PlayerHasGood(4030))
    OR_1.Add(PlayerHasGood(4040))
    OR_1.Add(PlayerHasGood(4060))
    OR_1.Add(PlayerHasGood(4110))
    OR_1.Add(PlayerHasGood(4500))
    OR_1.Add(PlayerHasGood(4510))
    OR_1.Add(PlayerHasGood(4520))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11020102)


@NeverRestart(730)
def Event_730():
    """Event 730"""
    AND_1.Add(FlagDisabled(732))
    AND_1.Add(FlagEnabled(8000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(732)
    EnableFlag(735)
    Restart()


@NeverRestart(731)
def Event_731():
    """Event 731"""
    MAIN.Await(FlagDisabled(8000))
    
    DisableFlag(732)
    DisableFlag(735)
    
    MAIN.Await(FlagEnabled(8000))
    
    Restart()


@NeverRestart(250)
def Event_250(_, item: int, flag: int):
    """Event 250"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(PlayerHasGood(item))
    
    EnableFlag(flag)


@NeverRestart(350)
def Event_350(_, flag: int, item: int):
    """Event 350"""
    if ThisEventSlotFlagEnabled():
        AND_1.Add(PlayerHasGood(item))
        if not AND_1:
            return
    
    MAIN.Await(FlagEnabled(flag))
    
    RemoveGoodFromPlayer(item=item, quantity=1)


@NeverRestart(780)
def Event_780(_, item: int, flag: int):
    """Event 780"""
    DisableFlag(flag)
    
    MAIN.Await(PlayerHasGood(item))
    
    EnableFlag(flag)
    
    MAIN.Await(PlayerDoesNotHaveGood(item))
    
    Restart()


@NeverRestart(870)
def Event_870(_, covenant: uchar, flag: int):
    """Event 870"""
    MAIN.Await(PlayerCovenant(covenant))
    
    EnableFlag(flag)
    AND_1.Add(PlayerCovenant(covenant))
    
    MAIN.Await(not AND_1)
    
    DisableFlag(flag)
    Restart()


@NeverRestart(260)
def Event_260(_, flag: int, text: int, seconds: float):
    """Event 260"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(seconds)
    DisplayStatus(text)


@NeverRestart(970)
def Event_970(_, flag: int, item_lot_param_id: int, item_lot_param_id_1: int, item_lot_param_id_2: int):
    """Event 970"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    if ValueNotEqual(left=item_lot_param_id, right=0):
        AwardItemLot(item_lot_param_id, host_only=True)
    DisableNetworkSync()
    Wait(5.0)
    if ValueNotEqual(left=item_lot_param_id_1, right=0):
        AwardItemLot(item_lot_param_id_1, host_only=True)
    if ValueNotEqual(left=item_lot_param_id_2, right=0):
        AwardItemLot(item_lot_param_id_2, host_only=True)


@NeverRestart(911)
def Event_911(_, flag: int, item_lot_param_id: int, state: uchar):
    """Event 911"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(item_lot_param_id, host_only=True)
    SetFlagState(flag, state)
    if FlagEnabled(flag):
        return
    Restart()


@NeverRestart(890)
def Event_890(_, flag: int, item_lot_param_id: int, state: uchar):
    """Event 890"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(item_lot_param_id, host_only=True)
    SetFlagState(flag, state)
    if FlagEnabled(flag):
        return
    Restart()


@NeverRestart(960)
def Event_960(_, flag: int, character: int, item_lot_param_id: int):
    """Event 960"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(item_lot_param_id, host_only=True)


@NeverRestart(8200)
def Event_8200(_, item_type: uchar, item: int, flag: int, flag_1: int):
    """Event 8200"""
    if FlagEnabled(flag):
        return
    AND_1.Add(NewGameCycleGreaterThanOrEqual(completion_count=1))
    if not AND_1:
        return
    IfPlayerHasItem(AND_2, item, item_type=item_type, including_storage=True)
    if not AND_2:
        return
    EnableFlag(flag)
    EnableFlag(flag_1)


@NeverRestart(8300)
def Event_8300(_, item_type: uchar, item: int, flag: int):
    """Event 8300"""
    if FlagEnabled(flag):
        return
    AND_1.Add(NewGameCycleGreaterThanOrEqual(completion_count=1))
    if not AND_1:
        return
    IfPlayerHasItem(AND_2, item, item_type=item_type, including_storage=True)
    if not AND_2:
        return
    EnableFlag(flag)


@NeverRestart(8090)
def Event_8090(_, item_type: uchar, item: int, flag: int):
    """Event 8090"""
    if FlagEnabled(flag):
        return
    AND_1.Add(NewGameCycleGreaterThanOrEqual(completion_count=1))
    if not AND_1:
        return
    IfPlayerHasItem(AND_2, item, item_type=item_type, including_storage=True)
    if not AND_2:
        return
    EnableFlag(flag)


@NeverRestart(910)
def Event_910(_, flag: int, item_lot_param_id: int):
    """Event 910"""
    if FlagDisabled(flag):
        MAIN.Await(FlagEnabled(flag))
    
        AwardItemLot(item_lot_param_id, host_only=True)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@NeverRestart(690)
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


@NeverRestart(721)
def Event_721():
    """Event 721"""
    if FlagEnabled(728):
        return
    AND_1.Add(FlagEnabled(11707000))
    AND_1.Add(FlagEnabled(11707010))
    AND_1.Add(FlagEnabled(11707020))
    AND_1.Add(FlagEnabled(11707030))
    AND_1.Add(FlagEnabled(11707040))
    AND_1.Add(FlagEnabled(11707050))
    AND_1.Add(FlagEnabled(11707060))
    AND_1.Add(FlagEnabled(11707070))
    
    MAIN.Await(AND_1)
    
    EnableFlag(721)
    AND_2.Add(FlagEnabled(11707090))
    AND_2.Add(FlagEnabled(11707100))
    AND_2.Add(FlagEnabled(11707110))
    
    MAIN.Await(AND_2)
    
    EnableFlag(728)


@NeverRestart(722)
def Event_722():
    """Event 722"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11407120))
    AND_1.Add(FlagEnabled(11407130))
    AND_1.Add(FlagEnabled(11407150))
    AND_1.Add(FlagEnabled(11407160))
    AND_1.Add(FlagEnabled(11407170))
    AND_1.Add(FlagEnabled(11407140))
    AND_1.Add(FlagEnabled(11407180))
    AND_1.Add(FlagEnabled(11407190))
    AND_1.Add(FlagEnabled(10))
    AND_1.Add(PlayerHasWeapon(1332500))
    
    MAIN.Await(AND_1)
    
    EnableFlag(722)


@NeverRestart(723)
def Event_723():
    """Event 723"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11027130))
    AND_1.Add(FlagEnabled(11027140))
    AND_1.Add(FlagEnabled(11027150))
    AND_1.Add(FlagEnabled(11027160))
    AND_1.Add(FlagEnabled(11027170))
    AND_1.Add(FlagEnabled(11027180))
    AND_1.Add(FlagEnabled(11027190))
    AND_1.Add(FlagEnabled(11027200))
    AND_1.Add(FlagEnabled(11027210))
    AND_1.Add(FlagEnabled(11027220))
    AND_1.Add(FlagEnabled(11027230))
    AND_1.Add(FlagEnabled(11027240))
    
    MAIN.Await(AND_1)
    
    EnableFlag(723)


@NeverRestart(724)
def Event_724():
    """Event 724"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11017050))
    AND_1.Add(FlagEnabled(11017060))
    AND_1.Add(FlagEnabled(11017070))
    AND_1.Add(FlagEnabled(11017080))
    AND_1.Add(FlagEnabled(11017090))
    AND_1.Add(FlagEnabled(11017100))
    AND_1.Add(FlagEnabled(11017110))
    AND_1.Add(FlagEnabled(11017120))
    AND_1.Add(FlagEnabled(11017130))
    
    MAIN.Await(AND_1)
    
    EnableFlag(724)


@NeverRestart(725)
def Event_725():
    """Event 725"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(11707100, 11707190)) >= 2)
    
    EnableFlag(725)


@NeverRestart(726)
def Event_726():
    """Event 726"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(11607000, 11607090)) >= 2)
    
    EnableFlag(726)


@NeverRestart(727)
def Event_727():
    """Event 727"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11327000))
    AND_1.Add(FlagEnabled(11327010))
    AND_1.Add(FlagEnabled(11327020))
    AND_1.Add(FlagEnabled(11327030))
    AND_1.Add(FlagEnabled(11327040))
    AND_1.Add(FlagEnabled(11327050))
    AND_1.Add(FlagEnabled(11327060))
    AND_1.Add(FlagEnabled(11327070))
    AND_1.Add(FlagEnabled(11327080))
    AND_1.Add(FlagEnabled(11327090))
    
    MAIN.Await(AND_1)
    
    EnableFlag(727)


@NeverRestart(740)
def Event_740():
    """Event 740"""
    MAIN.Await(PlayerClass(ClassType.Pyromancer))
    
    EnableFlag(740)


@NeverRestart(745)
def Event_745():
    """Event 745"""
    AND_7.Add(FlagEnabled(1604))
    AND_7.Add(FlagEnabled(1764))
    SkipLinesIfConditionFalse(1, AND_7)
    
    MAIN.Await(FlagEnabled(703))
    
    if FlagDisabled(1604):
        OR_1.Add(FlagEnabled(1604))
    if FlagDisabled(1764):
        OR_1.Add(FlagEnabled(1764))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    End()


@NeverRestart(754)
def Event_754():
    """Event 754"""
    DisableFlag(754)
    
    MAIN.Await(FlagEnabled(754))
    
    DisableFlag(754)
    AddSpecialEffect(PLAYER, 4600)
    AddSpecialEffect(PLAYER, 4601)
    CreateTemporaryVFX(vfx_id=22715, anchor_entity=PLAYER, model_point=7, anchor_type=CoordEntityType.Character)
    Restart()


@NeverRestart(770)
def Event_770():
    """Event 770"""
    MAIN.Await(FlagEnabled(755))
    
    DisableFlag(755)
    DisableFlag(742)
    DisableFlag(743)
    DisableFlag(744)
    DisableFlag(745)
    DisableFlag(746)
    DisableFlagRange((11000501, 11000519))
    DisableFlagRange((11010501, 11010519))
    DisableFlagRange((11020501, 11020529))
    DisableFlagRange((11100501, 11100519))
    DisableFlagRange((11200501, 11200519))
    DisableFlagRange((11300501, 11300519))
    DisableFlagRange((11310501, 11310519))
    DisableFlagRange((11320501, 11320519))
    DisableFlagRange((11400501, 11400519))
    DisableFlagRange((11410501, 11410519))
    DisableFlagRange((11500501, 11500519))
    DisableFlagRange((11510501, 11510519))
    DisableFlagRange((11600501, 11600519))
    DisableFlagRange((11700501, 11700519))
    DisableFlagRange((11800501, 11800519))
    DisableFlagRange((11810501, 11810519))
    DisableFlagRange((11210501, 11210519))
    DisableFlag(1004)
    DisableFlag(1033)
    DisableFlag(1096)
    DisableFlag(1114)
    DisableFlag(1176)
    DisableFlag(1179)
    DisableFlag(1195)
    DisableFlag(1197)
    DisableFlag(1213)
    DisableFlag(1223)
    DisableFlag(1241)
    DisableFlag(1253)
    DisableFlag(1282)
    DisableFlag(1283)
    DisableFlag(1287)
    DisableFlag(1294)
    DisableFlag(1314)
    DisableFlag(1321)
    DisableFlag(1341)
    DisableFlag(1361)
    DisableFlag(1381)
    DisableFlag(1401)
    DisableFlag(1411)
    DisableFlag(1421)
    DisableFlag(1434)
    DisableFlag(1461)
    DisableFlag(1512)
    DisableFlag(1547)
    DisableFlag(1574)
    DisableFlag(1603)
    DisableFlag(1627)
    DisableFlag(1646)
    DisableFlag(1675)
    DisableFlag(1691)
    EnableFlag(1710)
    DisableFlag(1711)
    DisableFlag(1712)
    DisableFlag(11200596)
    DisableFlag(71200035)
    DisableFlag(71200042)
    DisableFlag(1763)
    DisableFlag(1822)
    DisableFlag(1841)
    DisableFlag(1863)
    DisableFlag(1871)
    SetTeamType(6001, TeamType.Ally)
    SetTeamType(6040, TeamType.Ally)
    SetTeamType(6072, TeamType.Ally)
    SetTeamType(6190, TeamType.Ally)
    SetTeamType(6230, TeamType.Ally)
    SetTeamType(6300, TeamType.Ally)
    Restart()


@NeverRestart(772)
def Event_772():
    """Event 772"""
    MAIN.Await(FlagDisabled(744))
    
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1033))
    OR_1.Add(FlagEnabled(1096))
    OR_1.Add(FlagEnabled(1114))
    OR_1.Add(FlagEnabled(1176))
    OR_1.Add(FlagEnabled(1179))
    OR_1.Add(FlagEnabled(1195))
    OR_1.Add(FlagEnabled(1197))
    OR_1.Add(FlagEnabled(1213))
    OR_1.Add(FlagEnabled(1223))
    OR_1.Add(FlagEnabled(1241))
    OR_1.Add(FlagEnabled(1253))
    OR_1.Add(FlagEnabled(1282))
    OR_1.Add(FlagEnabled(1283))
    OR_1.Add(FlagEnabled(1287))
    OR_1.Add(FlagEnabled(1294))
    OR_1.Add(FlagEnabled(1314))
    OR_1.Add(FlagEnabled(1321))
    OR_1.Add(FlagEnabled(1341))
    OR_1.Add(FlagEnabled(1361))
    OR_1.Add(FlagEnabled(1381))
    OR_1.Add(FlagEnabled(1401))
    OR_1.Add(FlagEnabled(1411))
    OR_1.Add(FlagEnabled(1421))
    OR_1.Add(FlagEnabled(1434))
    OR_1.Add(FlagEnabled(1461))
    OR_1.Add(FlagEnabled(1512))
    OR_1.Add(FlagEnabled(1547))
    OR_1.Add(FlagEnabled(1574))
    OR_1.Add(FlagEnabled(1603))
    OR_1.Add(FlagEnabled(1627))
    OR_1.Add(FlagEnabled(1646))
    OR_1.Add(FlagEnabled(1675))
    OR_1.Add(FlagEnabled(1691))
    OR_1.Add(FlagEnabled(1711))
    OR_1.Add(FlagEnabled(1712))
    OR_1.Add(FlagEnabled(71200035))
    OR_1.Add(FlagEnabled(71200042))
    OR_1.Add(FlagEnabled(1763))
    OR_1.Add(FlagEnabled(1822))
    OR_1.Add(FlagEnabled(1841))
    OR_1.Add(FlagEnabled(1863))
    OR_1.Add(FlagEnabled(1871))
    
    MAIN.Await(OR_1)
    
    EnableFlag(744)
    
    MAIN.Await(FlagDisabled(744))
    
    Restart()


@NeverRestart(761)
def Event_761():
    """Event 761"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(760))
    
    WaitFrames(frames=200)
    DisableFlag(760)
    Restart()


@NeverRestart(763)
def Event_763():
    """Event 763"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(762))
    
    ForceAnimation(PLAYER, 7697)
    Wait(3.5)
    DisableFlag(762)
    Wait(2.799999952316284)
    DisableFlag(764)
    ForceAnimation(PLAYER, 7701, loop=True)
    Restart()


@NeverRestart(750)
def Event_750():
    """Event 750"""
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 71))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 72))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 73))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 74))
    OR_1.Add(FlagEnabled(751))
    
    MAIN.Await(OR_1)
    
    EnableFlag(751)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 71))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 72))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 73))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 74))
    
    MAIN.Await(AND_1)
    
    DisableFlag(751)
    Restart()


@NeverRestart(752)
def Event_752():
    """Event 752"""
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 5213))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 5214))
    OR_1.Add(FlagEnabled(753))
    
    MAIN.Await(OR_1)
    
    EnableFlag(753)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 5213))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 5214))
    
    MAIN.Await(AND_1)
    
    DisableFlag(753)
    DisableFlag(11400591)
    Restart()


@NeverRestart(757)
def Event_757():
    """Event 757"""
    if FlagEnabled(757):
        DisplayStatus(10010660)
    DisableFlag(757)
    AND_1.Add(Host())
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 71))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 72))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 73))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 74))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 33))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 34))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    End()


@NeverRestart(758)
def Event_758():
    """Event 758"""
    if ThisEventFlagEnabled():
        DisplayStatus(10010670)
    DisableFlag(758)
    AND_1.Add(Host())
    AND_1.Add(HealthRatio(PLAYER) <= 0.0)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2130))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(Host())
    AND_2.Add(CharacterDead(PLAYER))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2130))
    
    MAIN.Await(AND_2)
    
    End()


@NeverRestart(759)
def Event_759():
    """Event 759"""
    if ThisEventFlagEnabled():
        DisplayStatus(10010680)
    DisableFlag(759)
    AND_1.Add(Host())
    AND_1.Add(HealthRatio(PLAYER) <= 0.0)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2131))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(Host())
    AND_2.Add(CharacterDead(PLAYER))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2131))
    
    MAIN.Await(AND_2)
    
    End()


@NeverRestart(818)
def Event_818():
    """Event 818"""
    if FlagDisabled(11510150):
        MAIN.Await(FlagEnabled(11510150))
    
        DisplayStatus(10010690)
    AND_1.Add(FlagEnabled(11510150))
    AND_1.Add(OutsideMap(game_map=ANOR_LONDO))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11510150)
    Restart()


@NeverRestart(810)
def Event_810():
    """Event 810"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(50001031))
    
    EnableFlag(810)


@NeverRestart(812)
def Event_812(_, flag: int):
    """Event 812"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    End()


@NeverRestart(822)
def Event_822():
    """Event 822"""
    MAIN.Await(FlagEnabled(830))
    
    AND_1.Add(TimeElapsed(seconds=0.5))
    AND_1.Add(OutsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    
    MAIN.Await(AND_1)
    
    DisableFlag(830)
    Restart()


@NeverRestart(823)
def Event_823():
    """Event 823"""
    MAIN.Await(FlagEnabled(831))
    
    AND_1.Add(TimeElapsed(seconds=0.5))
    AND_1.Add(OutsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    
    MAIN.Await(AND_1)
    
    DisableFlag(831)
    Restart()


@NeverRestart(840)
def Event_840(_, flag: int, animation_id: int, target_entity: int, animation_id_1: int):
    """Event 840"""
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    SkipLinesIfFlagEnabled(2, 844)
    SkipLinesIfFlagEnabled(1, 847)
    RotateToFaceEntity(PLAYER, target_entity=target_entity)
    ForceAnimation(PLAYER, animation_id)
    Wait(1.0)
    PlaySoundEffect(PLAYER, 123456789, sound_type=SoundType.s_SFX)
    Wait(4.0)
    if ValueNotEqual(left=animation_id_1, right=-1):
        ForceAnimation(PLAYER, animation_id_1, loop=True)
    Restart()


@NeverRestart(766)
def Event_766():
    """Event 766"""
    AND_1.Add(Online())
    if AND_1:
        return
    EnableFlag(765)
