"""
Common

linked:


strings:

"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_701()
    Event_705()
    Event_900()
    Event_901()
    Event_902()
    Event_910()
    Event_1040()
    Event_1030()
    Event_1050()
    Event_930(
        0,
        cutscene_id=60380000,
        cutscene_id_1=60380001,
        entity=1038501500,
        action_button_id=9700,
        item=8105,
        item_1=8106,
        map_id=60385000,
        move_to_region=1038502500,
        move_to_region_1=0,
        unk_20_24=62001,
    )
    Event_930(
        1,
        cutscene_id=60380010,
        cutscene_id_1=60380011,
        entity=1038501502,
        action_button_id=9700,
        item=8105,
        item_1=8106,
        map_id=60385000,
        move_to_region=1038502502,
        move_to_region_1=0,
        unk_20_24=63000,
    )
    Event_930(
        3,
        cutscene_id=60490010,
        cutscene_id_1=60490011,
        entity=1049531502,
        action_button_id=9700,
        item=8107,
        item_1=0,
        map_id=60495300,
        move_to_region=1049532502,
        move_to_region_1=0,
        unk_20_24=65000,
    )
    Event_930(
        5,
        cutscene_id=60490030,
        cutscene_id_1=60490031,
        entity=1049531506,
        action_button_id=9701,
        item=8175,
        item_1=8176,
        map_id=60495300,
        move_to_region=1049532506,
        move_to_region_1=0,
        unk_20_24=65002,
    )
    Event_936(
        0,
        cutscene_id=60490000,
        cutscene_id_1=60490001,
        flag=1049532500,
        map_id=60495300,
        move_to_region=1049532500,
        unk_20_24=63003,
        change_weather=0,
        weather=0,
        weather_duration=-1.0,
    )
    Event_936(
        1,
        cutscene_id=60490020,
        cutscene_id_1=60490021,
        flag=1049532504,
        map_id=60485400,
        move_to_region=1049532504,
        unk_20_24=63003,
        change_weather=0,
        weather=0,
        weather_duration=-1.0,
    )
    Event_970()
    Event_9820(0, right=8820, item_lot_param_id=4820, special_effect=3600)
    Event_1020()
    Event_9945()
    Event_1400()
    Event_1401()
    Event_1410(0, flag=60804, command_id__gesture_param_id=4, special_effect=1000, character=11100785, flag_1=11102180)
    Event_1411(
        0,
        flag=60808,
        command_id__gesture_param_id=8,
        special_effect=1001,
        character=39200700,
        flag_1=39202160,
        character_1=1052380260,
        flag_2=1252382699,
        character_2=1045520730,
        flag_3=1045522170,
    )
    Event_1412(
        0,
        flag=60823,
        command_id__gesture_param_id=53,
        special_effect=1002,
        character=1050560700,
        flag_1=1050562140,
    )
    Event_1600(0, flag=62010, flag_1=63010, asset=1042371690, asset_1=1042371691)
    Event_1600(1, flag=62011, flag_1=63011, asset=1044321690, asset_1=1044321691)
    Event_1600(2, flag=62012, flag_1=63012, asset=1045371690, asset_1=1045371691)
    Event_1600(3, flag=62020, flag_1=63020, asset=1038411690, asset_1=1038411691)
    Event_1600(4, flag=62021, flag_1=63021, asset=1037441690, asset_1=1037441691)
    Event_1600(5, flag=62022, flag_1=63022, asset=1034481690, asset_1=1034481691)
    Event_1600(6, flag=62030, flag_1=63030, asset=1040521690, asset_1=1040521691)
    Event_1600(7, flag=62031, flag_1=63031, asset=1042511690, asset_1=1042511691)
    Event_1600(8, flag=62032, flag_1=63032, asset=1036541690, asset_1=1036541691)
    Event_1600(9, flag=62040, flag_1=63040, asset=1049371690, asset_1=1049371691)
    Event_1600(10, flag=62041, flag_1=63041, asset=1049401690, asset_1=1049401691)
    Event_1600(11, flag=62050, flag_1=63050, asset=1049531690, asset_1=1049531691)
    Event_1600(12, flag=62051, flag_1=63051, asset=1052541690, asset_1=1052541691)
    Event_1600(13, flag=62052, flag_1=63052, asset=1048561690, asset_1=1048561691)
    Event_1600(14, flag=62060, flag_1=63060, asset=0, asset_1=0)
    Event_1600(15, flag=62061, flag_1=63061, asset=0, asset_1=0)
    Event_1600(16, flag=62063, flag_1=63063, asset=0, asset_1=0)
    Event_1600(17, flag=62062, flag_1=63062, asset=0, asset_1=0)
    Event_1600(18, flag=62064, flag_1=63064, asset=0, asset_1=0)
    Event_1630(
        0,
        flag=62004,
        flag_1=62010,
        right=62012,
        right_1=62020,
        right_2=62030,
        right_3=62031,
        right_4=62041,
        right_5=62050,
        right_6=0,
    )
    Event_1630(
        1,
        flag=62005,
        flag_1=62010,
        right=62011,
        right_1=62022,
        right_2=0,
        right_3=0,
        right_4=0,
        right_5=0,
        right_6=0,
    )
    Event_1630(
        2,
        flag=62006,
        flag_1=62022,
        right=62032,
        right_1=0,
        right_2=0,
        right_3=0,
        right_4=0,
        right_5=0,
        right_6=0,
    )
    Event_1630(
        3,
        flag=62007,
        flag_1=62011,
        right=62040,
        right_1=62041,
        right_2=0,
        right_3=0,
        right_4=0,
        right_5=0,
        right_6=0,
    )
    Event_1630(
        4,
        flag=62008,
        flag_1=62050,
        right=62051,
        right_1=0,
        right_2=0,
        right_3=0,
        right_4=0,
        right_5=0,
        right_6=0,
    )
    Event_1630(
        5,
        flag=62009,
        flag_1=62050,
        right=62052,
        right_1=0,
        right_2=0,
        right_3=0,
        right_4=0,
        right_5=0,
        right_6=0,
    )
    if PlayerNotInOwnWorld():
        return
    Event_945()
    Event_920()
    Event_921()
    Event_922()
    Event_130(2, collision=14004100)
    Event_9300(4, achievement_id=4, flag=10000800, seconds=0.0)
    Event_9300(5, achievement_id=5, flag=9130, seconds=0.0)
    Event_9300(6, achievement_id=6, flag=11000800, seconds=0.0)
    Event_9300(7, achievement_id=7, flag=16000800, seconds=0.0)
    Event_9300(8, achievement_id=8, flag=15000800, seconds=0.0)
    Event_9300(9, achievement_id=9, flag=12050800, seconds=0.0)
    Event_9300(10, achievement_id=10, flag=13000800, seconds=0.0)
    Event_9300(11, achievement_id=11, flag=11050800, seconds=0.0)
    Event_9300(12, achievement_id=12, flag=13000830, seconds=0.0)
    Event_9300(18, achievement_id=18, flag=14000800, seconds=0.0)
    Event_9300(19, achievement_id=19, flag=12030850, seconds=0.0)
    Event_9300(20, achievement_id=20, flag=13000850, seconds=0.0)
    Event_9300(21, achievement_id=21, flag=1052520800, seconds=0.0)
    Event_9300(22, achievement_id=22, flag=12010800, seconds=0.0)
    Event_9300(23, achievement_id=23, flag=12090800, seconds=0.0)
    Event_9300(24, achievement_id=24, flag=12020800, seconds=0.0)
    Event_9300(25, achievement_id=25, flag=10000850, seconds=0.0)
    Event_9300(26, achievement_id=26, flag=14000850, seconds=0.0)
    Event_9300(27, achievement_id=27, flag=16000850, seconds=0.0)
    Event_9300(28, achievement_id=28, flag=39200800, seconds=0.0)
    Event_9300(29, achievement_id=29, flag=11000850, seconds=0.0)
    Event_9300(30, achievement_id=30, flag=35000800, seconds=0.0)
    Event_9300(31, achievement_id=31, flag=12020850, seconds=0.0)
    Event_9300(32, achievement_id=32, flag=15000850, seconds=0.0)
    Event_9300(33, achievement_id=33, flag=12040800, seconds=0.0)
    Event_9300(34, achievement_id=34, flag=1043300800, seconds=0.0)
    Event_9300(35, achievement_id=35, flag=1035500800, seconds=0.0)
    Event_9300(36, achievement_id=36, flag=1039540800, seconds=0.0)
    Event_9300(37, achievement_id=37, flag=12080800, seconds=0.0)
    Event_9300(38, achievement_id=38, flag=1051570800, seconds=0.0)
    Event_9300(39, achievement_id=39, flag=105, seconds=0.0)
    Event_9300(41, achievement_id=41, flag=110, seconds=0.0)
    Event_9360(0, activity_id=0, flag=100, seconds=0.0)
    Event_9360(1, activity_id=1, flag=9390, seconds=0.0)
    Event_9360(2, activity_id=2, flag=9392, seconds=0.0)
    Event_9360(3, activity_id=3, flag=11000801, seconds=0.0)
    Event_9360(4, activity_id=4, flag=1252520801, seconds=0.0)
    Event_9360(5, activity_id=5, flag=13000801, seconds=0.0)
    Event_9360(6, activity_id=6, flag=19000802, seconds=0.0)
    Event_9375(0, activity_id=0, flag=120, seconds=0.0)
    Event_9375(1, activity_id=1, flag=9391, seconds=0.0)
    Event_9375(2, activity_id=2, flag=9393, seconds=0.0)
    Event_9375(3, activity_id=3, flag=11000800, seconds=0.0)
    Event_9375(4, activity_id=4, flag=1252520800, seconds=0.0)
    Event_9375(5, activity_id=5, flag=13000800, seconds=0.0)
    Event_9375(6, activity_id=6, flag=19000800, seconds=0.0)
    Event_9390(0, flag=6001, right=10000801, right_1=1252380801, right_2=16000801, right_3=12050801, right_4=0)
    Event_9390(1, flag=6001, right=10000800, right_1=1252380800, right_2=16000800, right_3=12050800, right_4=0)
    Event_9390(2, flag=9390, right=10000801, right_1=1252380801, right_2=16000801, right_3=12050801, right_4=11000801)
    Event_9390(3, flag=9391, right=10000800, right_1=1252380800, right_2=16000800, right_3=12050800, right_4=11000800)
    Event_1800()
    Event_1801()
    Event_1450(0, flag=65610, right=65620, right_1=65630, right_2=0)
    Event_1450(1, flag=65640, right=65650, right_1=0, right_2=0)
    Event_1450(2, flag=65660, right=65670, right_1=0, right_2=0)
    Event_1450(4, flag=65680, right=65690, right_1=0, right_2=0)
    Event_1450(3, flag=65720, right=65700, right_1=65710, right_2=0)
    Event_1460()
    Event_1461()
    Event_1462()
    Event_1700()
    Event_1701()
    Event_1703()
    Event_1704()
    Event_1705()
    Event_1750()
    Event_1751()
    Event_1752()
    Event_1720(0, flag=69170, flag_1=710610, tutorial_param_id=1610, item=9117)
    Event_1720(1, flag=69180, flag_1=710620, tutorial_param_id=1620, item=9118)
    Event_1720(2, flag=69190, flag_1=710630, tutorial_param_id=1630, item=9119)
    Event_1720(3, flag=69010, flag_1=710060, tutorial_param_id=1060, item=9101)
    Event_1720(4, flag=69020, flag_1=710130, tutorial_param_id=1130, item=9102)
    Event_1720(5, flag=69110, flag_1=710550, tutorial_param_id=1550, item=9111)
    Event_1720(6, flag=69340, flag_1=710560, tutorial_param_id=1560, item=9134)
    Event_1720(9, flag=69360, flag_1=710750, tutorial_param_id=1750, item=9136)
    Event_1720(10, flag=69200, flag_1=710640, tutorial_param_id=1640, item=9120)
    Event_1720(11, flag=69260, flag_1=710690, tutorial_param_id=1690, item=9126)
    Event_1720(12, flag=69270, flag_1=710710, tutorial_param_id=1710, item=9127)
    Event_1720(13, flag=69210, flag_1=710650, tutorial_param_id=1650, item=9121)
    Event_1720(14, flag=69390, flag_1=710810, tutorial_param_id=1810, item=9141)
    Event_1720(15, flag=69420, flag_1=710820, tutorial_param_id=1820, item=9142)
    Event_1790()
    Event_1770(0, flag=700800, flag_1=710800, tutorial_param_id=1800)
    Event_950()
    Event_960(0, flag=76100)
    Event_960(1, flag=76108)
    Event_960(2, flag=76104)
    Event_960(3, flag=76102)
    Event_960(4, flag=76106)
    Event_960(6, flag=76111)
    Event_960(7, flag=76157)
    Event_960(8, flag=76113)
    Event_720(0, flag=160, value=0)
    Event_720(1, flag=161, value=1)
    Event_720(2, flag=162, value=2)
    Event_720(3, flag=163, value=3)
    Event_720(4, flag=164, value=4)
    Event_720(5, flag=165, value=5)
    Event_720(6, flag=166, value=6)
    Event_720(7, flag=167, value=7)
    Event_730(0, flag=180, value=0)
    Event_730(1, flag=181, value=1)
    Event_730(2, flag=182, value=2)
    Event_730(3, flag=183, value=3)
    Event_730(4, flag=184, value=4)
    Event_730(5, flag=185, value=5)
    Event_730(6, flag=186, value=6)
    Event_730(7, flag=187, value=7)
    Event_1100(0, flag=9100, item_lot__item_lot_param_id=10000, item_lot_param_id=0, flag_1=60510)
    Event_1100(1, flag=9101, item_lot__item_lot_param_id=10010, item_lot_param_id=0, flag_1=510010)
    Event_1100(2, flag=9102, item_lot__item_lot_param_id=10020, item_lot_param_id=0, flag_1=510020)
    Event_1100(3, flag=9103, item_lot__item_lot_param_id=10030, item_lot_param_id=0, flag_1=510030)
    Event_1100(4, flag=9104, item_lot__item_lot_param_id=10040, item_lot_param_id=0, flag_1=510040)
    Event_1100(5, flag=9105, item_lot__item_lot_param_id=10050, item_lot_param_id=0, flag_1=60520)
    Event_1100(6, flag=9106, item_lot__item_lot_param_id=10060, item_lot_param_id=0, flag_1=510060)
    Event_1100(7, flag=9107, item_lot__item_lot_param_id=10070, item_lot_param_id=0, flag_1=510070)
    Event_1100(8, flag=9108, item_lot__item_lot_param_id=10080, item_lot_param_id=0, flag_1=510080)
    Event_1100(9, flag=9109, item_lot__item_lot_param_id=10090, item_lot_param_id=0, flag_1=510090)
    Event_1100(10, flag=9110, item_lot__item_lot_param_id=10100, item_lot_param_id=0, flag_1=510100)
    Event_1100(11, flag=9111, item_lot__item_lot_param_id=10110, item_lot_param_id=0, flag_1=510110)
    Event_1100(12, flag=9112, item_lot__item_lot_param_id=10120, item_lot_param_id=0, flag_1=510120)
    Event_1100(13, flag=9113, item_lot__item_lot_param_id=10130, item_lot_param_id=0, flag_1=510130)
    Event_1100(14, flag=9114, item_lot__item_lot_param_id=10140, item_lot_param_id=0, flag_1=510140)
    Event_1100(15, flag=9115, item_lot__item_lot_param_id=10150, item_lot_param_id=0, flag_1=510150)
    Event_1100(16, flag=9116, item_lot__item_lot_param_id=10160, item_lot_param_id=0, flag_1=510160)
    Event_1100(17, flag=9117, item_lot__item_lot_param_id=10170, item_lot_param_id=0, flag_1=60440)
    Event_1100(18, flag=9118, item_lot__item_lot_param_id=10180, item_lot_param_id=0, flag_1=197)
    Event_1100(19, flag=9119, item_lot__item_lot_param_id=10190, item_lot_param_id=0, flag_1=510190)
    Event_1100(20, flag=9120, item_lot__item_lot_param_id=10200, item_lot_param_id=0, flag_1=510200)
    Event_1100(21, flag=9121, item_lot__item_lot_param_id=10210, item_lot_param_id=0, flag_1=510210)
    Event_1100(22, flag=9122, item_lot__item_lot_param_id=10220, item_lot_param_id=0, flag_1=510220)
    Event_1100(23, flag=9123, item_lot__item_lot_param_id=10230, item_lot_param_id=0, flag_1=510230)
    Event_1100(24, flag=9124, item_lot__item_lot_param_id=10240, item_lot_param_id=0, flag_1=510240)
    Event_1100(25, flag=9125, item_lot__item_lot_param_id=10250, item_lot_param_id=0, flag_1=510250)
    Event_1100(26, flag=9126, item_lot__item_lot_param_id=10260, item_lot_param_id=0, flag_1=510260)
    Event_1100(27, flag=9127, item_lot__item_lot_param_id=10270, item_lot_param_id=0, flag_1=510270)
    Event_1100(28, flag=9128, item_lot__item_lot_param_id=10280, item_lot_param_id=0, flag_1=510280)
    Event_1100(29, flag=9129, item_lot__item_lot_param_id=10290, item_lot_param_id=0, flag_1=510290)
    Event_1100(30, flag=9130, item_lot__item_lot_param_id=10300, item_lot_param_id=0, flag_1=510300)
    Event_1100(31, flag=9131, item_lot__item_lot_param_id=10310, item_lot_param_id=0, flag_1=510310)
    Event_1100(32, flag=9132, item_lot__item_lot_param_id=10320, item_lot_param_id=0, flag_1=510320)
    Event_1100(33, flag=9133, item_lot__item_lot_param_id=10330, item_lot_param_id=0, flag_1=510330)
    Event_1100(34, flag=9134, item_lot__item_lot_param_id=10340, item_lot_param_id=0, flag_1=510340)
    Event_1100(35, flag=9135, item_lot__item_lot_param_id=10350, item_lot_param_id=0, flag_1=510350)
    Event_1100(73, flag=9173, item_lot__item_lot_param_id=10730, item_lot_param_id=0, flag_1=510730)
    Event_1100(74, flag=9174, item_lot__item_lot_param_id=10740, item_lot_param_id=0, flag_1=510740)
    Event_1100(80, flag=9180, item_lot__item_lot_param_id=10800, item_lot_param_id=0, flag_1=510800)
    Event_1100(81, flag=9181, item_lot__item_lot_param_id=10810, item_lot_param_id=0, flag_1=510810)
    Event_1100(82, flag=9182, item_lot__item_lot_param_id=10820, item_lot_param_id=0, flag_1=510820)
    Event_1100(83, flag=9183, item_lot__item_lot_param_id=10830, item_lot_param_id=0, flag_1=510830)
    Event_1100(84, flag=9184, item_lot__item_lot_param_id=10840, item_lot_param_id=0, flag_1=510840)
    Event_1200(0, flag=9200, item_lot__item_lot_param_id=20000, item_lot_param_id=0, flag_1=520000)
    Event_1200(1, flag=9201, item_lot__item_lot_param_id=20010, item_lot_param_id=0, flag_1=520010)
    Event_1200(2, flag=9202, item_lot__item_lot_param_id=20020, item_lot_param_id=0, flag_1=520020)
    Event_1200(3, flag=9203, item_lot__item_lot_param_id=20030, item_lot_param_id=0, flag_1=520030)
    Event_1200(4, flag=9204, item_lot__item_lot_param_id=20040, item_lot_param_id=0, flag_1=520040)
    Event_1200(5, flag=9205, item_lot__item_lot_param_id=20050, item_lot_param_id=0, flag_1=520050)
    Event_1200(6, flag=9206, item_lot__item_lot_param_id=20060, item_lot_param_id=0, flag_1=520060)
    Event_1200(7, flag=9207, item_lot__item_lot_param_id=20070, item_lot_param_id=0, flag_1=520070)
    Event_1200(8, flag=9208, item_lot__item_lot_param_id=20080, item_lot_param_id=0, flag_1=520080)
    Event_1200(9, flag=9209, item_lot__item_lot_param_id=20090, item_lot_param_id=0, flag_1=520090)
    Event_1200(10, flag=9210, item_lot__item_lot_param_id=20100, item_lot_param_id=0, flag_1=520100)
    Event_1200(11, flag=9211, item_lot__item_lot_param_id=20110, item_lot_param_id=0, flag_1=520110)
    Event_1200(12, flag=9212, item_lot__item_lot_param_id=20120, item_lot_param_id=0, flag_1=520120)
    Event_1200(13, flag=9213, item_lot__item_lot_param_id=20130, item_lot_param_id=0, flag_1=520130)
    Event_1200(14, flag=9214, item_lot__item_lot_param_id=20140, item_lot_param_id=0, flag_1=520140)
    Event_1200(15, flag=9215, item_lot__item_lot_param_id=20150, item_lot_param_id=0, flag_1=520150)
    Event_1200(16, flag=9216, item_lot__item_lot_param_id=20160, item_lot_param_id=0, flag_1=520160)
    Event_1200(17, flag=9217, item_lot__item_lot_param_id=20170, item_lot_param_id=0, flag_1=520170)
    Event_1200(18, flag=9218, item_lot__item_lot_param_id=20180, item_lot_param_id=0, flag_1=520180)
    Event_1200(19, flag=9219, item_lot__item_lot_param_id=20190, item_lot_param_id=0, flag_1=520190)
    Event_1200(20, flag=9220, item_lot__item_lot_param_id=20200, item_lot_param_id=0, flag_1=520200)
    Event_1200(21, flag=9221, item_lot__item_lot_param_id=20210, item_lot_param_id=0, flag_1=520210)
    Event_1200(22, flag=9222, item_lot__item_lot_param_id=20220, item_lot_param_id=0, flag_1=520220)
    Event_1200(30, flag=9230, item_lot__item_lot_param_id=20300, item_lot_param_id=0, flag_1=520300)
    Event_1200(31, flag=9231, item_lot__item_lot_param_id=20310, item_lot_param_id=0, flag_1=520310)
    Event_1200(32, flag=9232, item_lot__item_lot_param_id=20320, item_lot_param_id=0, flag_1=520320)
    Event_1200(33, flag=9233, item_lot__item_lot_param_id=20330, item_lot_param_id=0, flag_1=520330)
    Event_1200(34, flag=9234, item_lot__item_lot_param_id=20340, item_lot_param_id=0, flag_1=520340)
    Event_1200(35, flag=9235, item_lot__item_lot_param_id=20350, item_lot_param_id=0, flag_1=520350)
    Event_1200(36, flag=9236, item_lot__item_lot_param_id=20360, item_lot_param_id=0, flag_1=520360)
    Event_1200(37, flag=9237, item_lot__item_lot_param_id=20370, item_lot_param_id=0, flag_1=520370)
    Event_1200(38, flag=9238, item_lot__item_lot_param_id=20380, item_lot_param_id=0, flag_1=520380)
    Event_1200(39, flag=9239, item_lot__item_lot_param_id=20390, item_lot_param_id=0, flag_1=520390)
    Event_1200(40, flag=9240, item_lot__item_lot_param_id=20400, item_lot_param_id=0, flag_1=520400)
    Event_1200(41, flag=9241, item_lot__item_lot_param_id=20410, item_lot_param_id=0, flag_1=520410)
    Event_1200(42, flag=9242, item_lot__item_lot_param_id=20420, item_lot_param_id=0, flag_1=520420)
    Event_1200(43, flag=9243, item_lot__item_lot_param_id=20430, item_lot_param_id=0, flag_1=520430)
    Event_1200(44, flag=9244, item_lot__item_lot_param_id=20440, item_lot_param_id=0, flag_1=520440)
    Event_1200(45, flag=9245, item_lot__item_lot_param_id=20450, item_lot_param_id=0, flag_1=520450)
    Event_1200(46, flag=9246, item_lot__item_lot_param_id=20460, item_lot_param_id=0, flag_1=520460)
    Event_1200(47, flag=9247, item_lot__item_lot_param_id=20470, item_lot_param_id=0, flag_1=520470)
    Event_1200(48, flag=9248, item_lot__item_lot_param_id=20480, item_lot_param_id=0, flag_1=520480)
    Event_1200(49, flag=9249, item_lot__item_lot_param_id=20490, item_lot_param_id=0, flag_1=520490)
    Event_1200(60, flag=9260, item_lot__item_lot_param_id=20600, item_lot_param_id=0, flag_1=520600)
    Event_1200(61, flag=9261, item_lot__item_lot_param_id=20610, item_lot_param_id=0, flag_1=520610)
    Event_1200(62, flag=9262, item_lot__item_lot_param_id=20620, item_lot_param_id=0, flag_1=520620)
    Event_1200(63, flag=9263, item_lot__item_lot_param_id=20630, item_lot_param_id=0, flag_1=520630)
    Event_1200(64, flag=9264, item_lot__item_lot_param_id=20640, item_lot_param_id=0, flag_1=520640)
    Event_1200(65, flag=9265, item_lot__item_lot_param_id=20650, item_lot_param_id=0, flag_1=520650)
    Event_1200(66, flag=9266, item_lot__item_lot_param_id=20660, item_lot_param_id=0, flag_1=520660)
    Event_1200(67, flag=9267, item_lot__item_lot_param_id=20670, item_lot_param_id=0, flag_1=520670)
    Event_1200(68, flag=9268, item_lot__item_lot_param_id=20680, item_lot_param_id=0, flag_1=520680)
    Event_65810(0, flag=65810, flag_1=100750, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(1, flag=65811, flag_1=400163, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(2, flag=65812, flag_1=100760, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(3, flag=65813, flag_1=1043377400, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(4, flag=65814, flag_1=540418, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(5, flag=65815, flag_1=540112, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(6, flag=65816, flag_1=540238, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(8, flag=65818, flag_1=100770, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(9, flag=65819, flag_1=1052417100, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(10, flag=65820, flag_1=1047387700, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(11, flag=65821, flag_1=100780, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(12, flag=65822, flag_1=540120, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(13, flag=65823, flag_1=540104, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(14, flag=65824, flag_1=540304, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(15, flag=65825, flag_1=100790, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(16, flag=65826, flag_1=540116, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(17, flag=65827, flag_1=290150, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(18, flag=65828, flag_1=540224, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(19, flag=65829, flag_1=100800, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(20, flag=65830, flag_1=1051537600, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(21, flag=65831, flag_1=400309, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(22, flag=65832, flag_1=100810, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(23, flag=65833, flag_1=540202, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(24, flag=65834, flag_1=540630, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(25, flag=65835, flag_1=1036487400, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(26, flag=65836, flag_1=400061, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(27, flag=65837, flag_1=540170, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(28, flag=65838, flag_1=540172, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(29, flag=65839, flag_1=100830, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(30, flag=65840, flag_1=510100, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(31, flag=65841, flag_1=1042377110, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(32, flag=65842, flag_1=540108, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(33, flag=65843, flag_1=16007020, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(34, flag=65844, flag_1=540516, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(35, flag=65845, flag_1=100840, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(36, flag=65846, flag_1=540408, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(37, flag=65847, flag_1=510140, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(38, flag=65848, flag_1=540410, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(39, flag=65849, flag_1=540372, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(40, flag=65850, flag_1=540318, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(41, flag=65851, flag_1=540310, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(42, flag=65852, flag_1=510810, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(43, flag=65853, flag_1=120000, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(44, flag=65854, flag_1=400358, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(45, flag=65855, flag_1=120010, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(46, flag=65856, flag_1=1043357500, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(47, flag=65857, flag_1=1035507090, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(48, flag=65858, flag_1=120020, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(49, flag=65859, flag_1=290290, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(50, flag=65860, flag_1=540414, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(51, flag=65861, flag_1=540118, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(52, flag=65862, flag_1=540314, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(53, flag=65863, flag_1=540660, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(54, flag=65864, flag_1=540404, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(55, flag=65865, flag_1=540308, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(56, flag=65866, flag_1=1043397500, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(57, flag=65867, flag_1=540300, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(58, flag=65868, flag_1=1039517200, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(59, flag=65869, flag_1=400235, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(60, flag=65870, flag_1=1048517700, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(61, flag=65871, flag_1=540272, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(62, flag=65872, flag_1=1035467700, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(63, flag=65873, flag_1=540524, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(64, flag=65874, flag_1=1049377100, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(65, flag=65875, flag_1=540406, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(66, flag=65876, flag_1=540686, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(67, flag=65877, flag_1=1046367700, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(68, flag=65878, flag_1=540402, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(69, flag=65879, flag_1=540306, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(70, flag=65880, flag_1=100850, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(71, flag=65881, flag_1=540510, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(72, flag=65882, flag_1=1039437400, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(73, flag=65883, flag_1=540200, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(74, flag=65884, flag_1=540204, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(75, flag=65885, flag_1=100860, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(76, flag=65886, flag_1=540210, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(77, flag=65887, flag_1=540302, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(78, flag=65888, flag_1=1044327410, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(79, flag=65889, flag_1=100820, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(80, flag=65890, flag_1=130340, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(81, flag=65891, flag_1=540100, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(82, flag=65892, flag_1=540316, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(83, flag=65893, flag_1=540206, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(84, flag=65894, flag_1=30107100, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(85, flag=65895, flag_1=540208, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(86, flag=65896, flag_1=540332, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(87, flag=65897, flag_1=540140, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(88, flag=65898, flag_1=540412, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(89, flag=65899, flag_1=540334, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(90, flag=65900, flag_1=540646, right=0, right_1=0, right_2=0, right_3=0)
    Event_65810(91, flag=65901, flag_1=580360, right=0, right_1=0, right_2=0, right_3=0)
    Event_1080()
    Event_841()
    Event_9910(0, flag=3005)
    Event_750()
    Event_9941()
    Event_9943()
    Event_9940()
    Event_1700()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_700()
    Event_710()
    Event_711()
    Event_715()
    Event_716()
    DisableFlag(6000)
    EnableFlag(6001)
    DisableFlag(9000)
    DisableFlag(9001)
    Event_740()
    Event_810()
    Event_820(0, flag=550, weather=5)
    Event_820(1, flag=551, weather=0)
    Event_820(2, flag=552, weather=6)
    Event_820(3, flag=553, weather=7)
    Event_820(4, flag=554, weather=1)
    Event_820(5, flag=555, weather=8)
    Event_820(6, flag=556, weather=3)
    Event_820(7, flag=557, weather=9)
    Event_820(8, flag=558, weather=2)
    Event_820(9, flag=559, weather=10)
    Event_820(10, flag=560, weather=4)
    Event_820(11, flag=561, weather=11)
    Event_820(12, flag=562, weather=15)
    Event_820(13, flag=563, weather=12)
    Event_839()
    Event_840()
    Event_980()
    DisableFlag(909)
    Event_3040()
    Event_3041()
    Event_3042()
    Event_3043()
    Event_3044()
    Event_3045()
    Event_3046()
    Event_3056()
    Event_3080()
    Event_3179()
    Event_3499()
    Event_3659()
    Event_3239()
    Event_3619()
    Event_3559()
    Event_3679()
    Event_3959()
    Event_3779()
    Event_3839()
    Event_3859()
    Event_4119()
    Event_3119()
    Event_3199()
    Event_3279()
    Event_3299()
    Event_3579()
    Event_3699()
    Event_3399()
    Event_3419()
    Event_3379()
    Event_3439()
    Event_3459()
    Event_3479()
    Event_3639()
    Event_3719()
    Event_3599()
    Event_4259()
    Event_3979()
    Event_3919()
    Event_3899()
    Event_3739()
    Event_4159()
    Event_3799()
    Event_3819()
    Event_4239()
    Event_3879()
    Event_4199()
    Event_4179()
    Event_4219()
    Event_4719()
    Event_4739()
    Event_4059()
    Event_4139()
    Event_4079()
    Event_3759()
    Event_3049()
    Event_3050()
    Event_3051()
    Event_3052()
    Event_3053()
    Event_3054()
    Event_3055()
    Event_3058()
    Event_3059()
    Event_3089()
    Event_4612()
    Event_60701(0, flag=11109751, flag_1=60701)
    Event_60701(1, flag=11109752, flag_1=60702)
    Event_60701(2, flag=11109753, flag_1=60703)
    Event_60701(3, flag=11109754, flag_1=60704)
    Event_60701(4, flag=11109755, flag_1=60705)
    Event_60701(5, flag=11109756, flag_1=60706)
    Event_60701(6, flag=11109757, flag_1=60707)
    Event_60701(7, flag=11109758, flag_1=60708)
    Event_60701(8, flag=11109759, flag_1=60709)
    Event_60701(9, flag=11109760, flag_1=60710)
    Event_60701(10, flag=11109761, flag_1=60711)
    Event_60701(11, flag=11109762, flag_1=60712)
    Event_60701(12, flag=11109763, flag_1=60713)
    Event_60701(13, flag=11109764, flag_1=60714)
    Event_60701(14, flag=11109765, flag_1=60715)
    Event_60701(29, flag=11109745, flag_1=60730)
    Event_60701(30, flag=11109746, flag_1=60731)
    Event_60701(31, flag=11109747, flag_1=60732)
    Event_60701(32, flag=11109748, flag_1=60733)
    Event_3081(
        0,
        flag=1037429202,
        flag_1=1038519202,
        flag_2=1038509202,
        flag_3=16009302,
        flag_4=16009312,
        flag_5=16009322,
        flag_6=16009313,
    )
    Event_3082(0, flag=1042369202, flag_1=1035449202, flag_2=12059163)
    Event_3083(0, flag=16009202, flag_1=16009252)
    Event_3084(0, flag=1036419202, flag_1=1036419213, flag_2=1047589202)
    Event_3085(0, flag=1037549202, flag_1=1039549203)
    Event_3086(0, flag=1044389202, flag_1=1043359252, flag_2=1035469202, flag_3=1039529202)
    Event_3087(0, flag=1042389252, flag_1=1042389263, flag_2=16009452)
    Event_3088(0, flag=1036439202, flag_1=1036439218, flag_2=1044529252, flag_3=1044529253)
    Event_3090(0, flag=1034449200, flag_1=11059400)
    Event_3091(0, flag=1034509400)
    Event_3092(0, flag=1034499200)
    Event_3093(0, flag=1034509300)
    Event_3094(0, flag=12039150)
    Event_3095(0, flag=1045399200)
    Event_3096(0, flag=1038439200, flag_1=35009200)
    Event_3097(0, flag=1051369222)
    Event_4600(0, flag=10009549, flag_1=10009506)
    Event_4601(0, flag=14009202)
    Event_4602(0, flag=1037449202, flag_1=16009412, flag_2=1039449302)
    Event_4603(0, flag=35009302)
    Event_4604(0, flag=1050389252, flag_1=1050389262, flag_2=1038519252)
    Event_4606(0, flag=1050389202)
    Event_4607(0, flag=1043399302, flag_1=1039449202, flag_2=1035539202, flag_3=13009262)
    Event_4608(0, flag=1039449252)
    Event_4609(0, flag=1039409252, flag_1=1036489202, flag_2=1039519202, flag_3=11109802)
    Event_4611(0, flag=11009452, flag_1=1040549202)
    Event_3098()
    Event_3099()
    AND_1.Add(FlagEnabled(6010))
    AND_1.Add(FlagDisabled(100))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableFlag(6010)

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerNotInOwnWorld():
        return
    Event_6901()
    Event_6902()
    Event_6903()
    Event_6904()
    Event_6905()
    Event_6906()
    Event_6907()
    Event_6908()
    End()


@ContinueOnRest(130)
def Event_130(_, collision: uint):
    """Event 130"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerStandingOnCollision(collision))
    
    MAIN.Await(AND_1)
    
    DisableThisSlotFlag()


@ContinueOnRest(700)
def Event_700():
    """Event 700"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(62000)
    EnableFlag(710580)
    EnableFlag(720000)
    EnableFlag(720010)
    EnableFlag(720020)
    EnableFlag(720030)
    EnableFlag(720040)
    EnableFlag(720050)
    EnableFlag(720060)
    EnableFlag(720090)
    EnableFlag(720100)
    EnableFlag(720110)
    EnableFlag(720120)
    EnableFlag(720130)
    EnableFlag(720140)
    EnableFlag(720150)
    EnableFlag(720160)
    EnableFlag(720170)
    EnableFlag(720180)
    EnableFlag(720190)
    EnableFlag(720200)
    EnableFlag(720210)
    EnableFlag(720220)
    GotoIfFlagEnabled(Label.L1, flag=2001)
    GotoIfFlagEnabled(Label.L0, flag=2000)
    EnableFlag(60200)
    EnableFlag(60210)
    EnableFlag(60220)
    EnableFlag(60230)
    EnableFlag(60240)
    EnableFlag(60250)
    EnableFlag(60260)
    EnableFlag(60270)
    EnableFlag(60280)
    EnableFlag(60290)
    EnableFlag(60300)
    EnableFlag(60310)
    DisableFlag(1650)
    EnableFlag(1651)
    DisableFlag(1652)
    EnableFlag(1653)
    EnableFlag(1650)
    EnableFlag(1651)
    DisableFlag(1652)
    DisableFlag(1653)
    DisableFlag(1654)
    EnableFlag(1655)
    EnableFlag(1656)
    EnableFlag(65600)
    EnableFlag(65610)
    EnableFlag(65620)
    EnableFlag(65630)
    EnableFlag(65640)
    EnableFlag(65650)
    EnableFlag(65660)
    EnableFlag(65670)
    EnableFlag(65680)
    EnableFlag(65690)
    EnableFlag(65700)
    EnableFlag(65710)
    EnableFlag(65720)
    EnableFlag(65730)
    EnableFlag(65740)
    EnableFlag(65750)
    EnableFlag(65760)
    EnableFlag(65770)
    EnableFlag(65780)
    EnableFlag(65790)
    EnableFlag(6500)
    EnableFlag(60120)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(60200)
    EnableFlag(60210)
    EnableFlag(60220)
    EnableFlag(60240)
    EnableFlag(60260)
    EnableFlag(60270)
    EnableFlag(60280)
    EnableFlag(60290)
    EnableFlag(60300)
    EnableFlag(60310)
    EnableFlag(1650)
    EnableFlag(1651)
    DisableFlag(1652)
    DisableFlag(1653)
    DisableFlag(1654)
    EnableFlag(1655)
    EnableFlag(1656)
    EnableFlag(82102)
    EnableFlag(65600)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(65600)
    EnableFlag(60800)
    EnableFlag(60807)
    EnableFlag(60811)
    EnableFlag(60820)
    EnableFlag(60827)
    EnableFlag(60834)
    EnableFlag(60806)
    EnableFlag(60812)
    EnableFlag(60813)
    EnableFlag(60814)
    EnableFlag(60815)
    EnableFlag(60831)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_7.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_7)
    EnableFlag(57)
    End()
    AND_6.Add(NewGameCycleEqual(completion_count=6))
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
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L1, flag=2001)
    GotoIfFlagEnabled(Label.L0, flag=2000)
    if FlagDisabled(50):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=106, flag=60210, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=100, flag=60220, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=109, flag=60230, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=101, flag=60240, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=110, flag=60250, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=112, flag=60260, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=102, flag=60270, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=104, flag=60280, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=105, flag=60290, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=108, flag=60300, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=103, flag=60310, bit_count=1)
    AND_10.Add(PlayerHasGood(150))
    SkipLinesIfConditionTrue(1, AND_10)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=150, flag=1650, bit_count=4)
    AND_11.Add(PlayerHasGood(111))
    SkipLinesIfConditionTrue(1, AND_11)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=111, flag=1660, bit_count=8)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(50):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=106, flag=60210, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=100, flag=60220, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=109, flag=60230, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=101, flag=60240, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=110, flag=60250, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=112, flag=60260, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=102, flag=60270, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=104, flag=60280, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=105, flag=60290, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=108, flag=60300, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=103, flag=60310, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=150, flag=1650, bit_count=8)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8500, flag=60120, bit_count=1)
    SetRespawnPoint(respawn_point=18002020)
    SaveRequest()
    EnableFlag(100)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagDisabled(50):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=106, flag=60210, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=100, flag=60220, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=109, flag=60230, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=101, flag=60240, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=110, flag=60250, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=112, flag=60260, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=102, flag=60270, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=104, flag=60280, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=105, flag=60290, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=108, flag=60300, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=103, flag=60310, bit_count=1)
    AwardGesture(gesture_param_id=6)
    AwardGesture(gesture_param_id=21)
    AwardGesture(gesture_param_id=22)
    AwardGesture(gesture_param_id=23)
    AwardGesture(gesture_param_id=24)
    AwardGesture(gesture_param_id=80)
    EnableFlag(100)
    Wait(3.0)


@ContinueOnRest(702)
def Event_702():
    """Event 702"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L0, flag=2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=True)
    
    MAIN.Await(FlagEnabled(1042368540))
    
    SetWeather(weather=Weather.Default, duration=3600.0, immediate_change=True)
    UnfreezeTime()
    EnableFlag(101)


@ContinueOnRest(703)
def Event_703():
    """Event 703"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(101):
        return
    AND_1.Add(FlagEnabled(100))
    
    MAIN.Await(AND_1)
    
    EnableFlag(101)
    if FlagEnabled(9990):
        SetWeather(weather=Weather.Default, duration=6000.0, immediate_change=False)
    SetCurrentTime(
        time=(23, 45, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )


@RestartOnRest(705)
def Event_705():
    """Event 705"""
    DisableFlag(9290)
    DisableFlag(9291)
    if PlayerNotInOwnWorld():
        return


@RestartOnRest(710)
def Event_710():
    """Event 710"""
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L0)
    EnableFlag(200)
    DisableFlag(201)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(200)
    EnableFlag(201)
    End()


@RestartOnRest(711)
def Event_711():
    """Event 711"""
    DisableNetworkSync()
    DisableFlag(202)
    OR_1.Add(MultiplayerPending())
    OR_1.Add(Multiplayer())
    
    MAIN.Await(OR_1)
    
    EnableFlag(202)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    
    MAIN.Await(not OR_2)
    
    DisableFlag(202)
    Restart()


@ContinueOnRest(715)
def Event_715():
    """Event 715"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        DisableNetworkFlag(210)
    DisableFlag(211)
    OR_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    OR_1.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_1.Add(InsideMap(game_map=(12, 0, 0, 0)))
    OR_1.Add(InsideMap(game_map=CRUMBLING_FARUM_AZULA))
    OR_1.Add(InsideMap(game_map=RAYA_LUCARIA))
    OR_1.Add(InsideMap(game_map=HALIGTREE))
    OR_1.Add(InsideMap(game_map=VOLCANO_MANOR))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(210)
    EnableFlag(211)
    OR_2.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    OR_2.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_2.Add(InsideMap(game_map=(12, 0, 0, 0)))
    OR_2.Add(InsideMap(game_map=CRUMBLING_FARUM_AZULA))
    OR_2.Add(InsideMap(game_map=RAYA_LUCARIA))
    OR_2.Add(InsideMap(game_map=HALIGTREE))
    OR_2.Add(InsideMap(game_map=VOLCANO_MANOR))
    
    MAIN.Await(not OR_2)
    
    Restart()


@ContinueOnRest(716)
def Event_716():
    """Event 716"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        DisableNetworkFlag(220)
    DisableFlag(221)
    OR_1.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    OR_1.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_1.Add(InsideMap(game_map=(12, 0, 0, 0)))
    OR_1.Add(InsideMap(game_map=CRUMBLING_FARUM_AZULA))
    OR_1.Add(InsideMap(game_map=RAYA_LUCARIA))
    OR_1.Add(InsideMap(game_map=HALIGTREE))
    OR_1.Add(InsideMap(game_map=VOLCANO_MANOR))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(220)
    EnableFlag(221)
    OR_2.Add(InsideMap(game_map=STORMVEIL_CASTLE))
    OR_2.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_2.Add(InsideMap(game_map=(12, 0, 0, 0)))
    OR_2.Add(InsideMap(game_map=CRUMBLING_FARUM_AZULA))
    OR_2.Add(InsideMap(game_map=RAYA_LUCARIA))
    OR_2.Add(InsideMap(game_map=HALIGTREE))
    OR_2.Add(InsideMap(game_map=VOLCANO_MANOR))
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(720)
def Event_720(_, flag: uint, value: int):
    """Event 720"""
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(190, 199)) >= value)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(730)
def Event_730(_, flag: uint, value: int):
    """Event 730"""
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(170, 179)) >= value)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@ContinueOnRest(740)
def Event_740():
    """Event 740"""
    DisableNetworkSync()
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@ContinueOnRest(750)
def Event_750():
    """Event 750"""
    DisableNetworkSync()
    if FlagDisabled(9295):
        return
    DisableFlag(9295)
    ForceAnimation(PLAYER, 60456)


@RestartOnRest(810)
def Event_810():
    """Event 810"""
    OR_1.Add(TimeOfDayInRange(earliest=(5, 30, 0), latest=(11, 59, 59)))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    OR_2.Add(TimeOfDayInRange(earliest=(12, 0, 0), latest=(19, 59, 59)))
    GotoIfConditionTrue(Label.L2, input_condition=OR_2)
    OR_3.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 29, 59)))
    GotoIfConditionTrue(Label.L3, input_condition=OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(530)
    DisableFlag(531)
    DisableFlag(532)
    AND_1.Add(TimeOfDayInRange(earliest=(6, 0, 0), latest=(11, 59, 59)))
    
    MAIN.Await(not AND_1)
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(530)
    EnableFlag(531)
    DisableFlag(532)
    AND_2.Add(TimeOfDayInRange(earliest=(12, 0, 0), latest=(19, 59, 59)))
    
    MAIN.Await(not AND_2)
    
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(530)
    DisableFlag(531)
    EnableFlag(532)
    AND_3.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 59, 59)))
    
    MAIN.Await(not AND_3)
    
    Restart()


@ContinueOnRest(820)
def Event_820(_, flag: uint, weather: char):
    """Event 820"""
    DisableNetworkSync()
    DisableFlag(flag)
    AND_1.Add(WeatherState(weather=weather, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    EnableFlag(flag)
    AND_2.Add(WeatherState(weather=weather, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not AND_2)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(839)
def Event_839():
    """Event 839"""
    DisableNetworkSync()
    OR_1.Add(WeatherState(weather=Weather.Cloudless, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(WeatherState(weather=Weather.Default, unk_4_8=0.0, unk_8_12=0.0))
    OR_2.Add(WeatherState(weather=Weather.FlatClouds, unk_4_8=0.0, unk_8_12=0.0))
    OR_2.Add(WeatherState(weather=Weather.PuffyClouds, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L1, input_condition=OR_2)
    OR_3.Add(WeatherState(weather=Weather.Rain, unk_4_8=0.0, unk_8_12=0.0))
    OR_3.Add(WeatherState(weather=Weather.RainyClouds, unk_4_8=0.0, unk_8_12=0.0))
    OR_3.Add(WeatherState(weather=Weather.WindyRain, unk_4_8=0.0, unk_8_12=0.0))
    OR_3.Add(WeatherState(weather=Weather.RainyHeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L2, input_condition=OR_3)
    OR_4.Add(WeatherState(weather=Weather.Snow, unk_4_8=0.0, unk_8_12=0.0))
    OR_4.Add(WeatherState(weather=Weather.HeavySnow, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L3, input_condition=OR_4)
    OR_5.Add(WeatherState(weather=Weather.Fog, unk_4_8=0.0, unk_8_12=0.0))
    OR_5.Add(WeatherState(weather=Weather.HeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L4, input_condition=OR_5)
    OR_6.Add(WeatherState(weather=Weather.WindyFog, unk_4_8=0.0, unk_8_12=0.0))
    OR_6.Add(WeatherState(weather=Weather.WindyPuffyClouds, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L5, input_condition=OR_6)
    DisableFlag(570)
    DisableFlag(571)
    DisableFlag(572)
    DisableFlag(573)
    DisableFlag(574)
    DisableFlag(575)
    Wait(3.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(570)
    DisableFlag(571)
    DisableFlag(572)
    DisableFlag(573)
    DisableFlag(574)
    DisableFlag(575)
    OR_10.Add(WeatherState(weather=Weather.Cloudless, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not OR_10)
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(570)
    EnableFlag(571)
    DisableFlag(572)
    DisableFlag(573)
    DisableFlag(574)
    DisableFlag(575)
    OR_11.Add(WeatherState(weather=Weather.Default, unk_4_8=0.0, unk_8_12=0.0))
    OR_11.Add(WeatherState(weather=Weather.FlatClouds, unk_4_8=0.0, unk_8_12=0.0))
    OR_11.Add(WeatherState(weather=Weather.PuffyClouds, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not OR_11)
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(570)
    DisableFlag(571)
    EnableFlag(572)
    DisableFlag(573)
    DisableFlag(574)
    DisableFlag(575)
    OR_12.Add(WeatherState(weather=Weather.Rain, unk_4_8=0.0, unk_8_12=0.0))
    OR_12.Add(WeatherState(weather=Weather.RainyClouds, unk_4_8=0.0, unk_8_12=0.0))
    OR_12.Add(WeatherState(weather=Weather.WindyRain, unk_4_8=0.0, unk_8_12=0.0))
    OR_12.Add(WeatherState(weather=Weather.RainyHeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not OR_12)
    
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(570)
    DisableFlag(571)
    DisableFlag(572)
    EnableFlag(573)
    DisableFlag(574)
    DisableFlag(575)
    OR_13.Add(WeatherState(weather=Weather.Snow, unk_4_8=0.0, unk_8_12=0.0))
    OR_13.Add(WeatherState(weather=Weather.HeavySnow, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not OR_13)
    
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableFlag(570)
    DisableFlag(571)
    DisableFlag(572)
    DisableFlag(573)
    EnableFlag(574)
    DisableFlag(575)
    OR_14.Add(WeatherState(weather=Weather.Fog, unk_4_8=0.0, unk_8_12=0.0))
    OR_14.Add(WeatherState(weather=Weather.HeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not OR_14)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableFlag(570)
    DisableFlag(571)
    DisableFlag(572)
    DisableFlag(573)
    DisableFlag(574)
    EnableFlag(575)
    OR_15.Add(WeatherState(weather=Weather.WindyFog, unk_4_8=0.0, unk_8_12=0.0))
    OR_15.Add(WeatherState(weather=Weather.WindyPuffyClouds, unk_4_8=0.0, unk_8_12=0.0))
    
    MAIN.Await(not OR_15)
    
    Restart()


@ContinueOnRest(840)
def Event_840():
    """Event 840"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 8998))
    
    DeactivateGparamOverride(change_duration=3.0)
    SetWeather(weather=Weather.Default, duration=1.0, immediate_change=False)
    RemoveSpecialEffect(PLAYER, 8998)
    Wait(1.2000000476837158)
    Restart()


@RestartOnRest(841)
def Event_841():
    """Event 841"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 8990))
    
    SetWeather(weather=Weather.Fog, duration=-1.0, immediate_change=False)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 8990))
    
    Restart()


@ContinueOnRest(900)
def Event_900():
    """Event 900"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L0, flag=9116)
    GotoIfFlagDisabled(Label.L1, flag=118)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9116))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    SetRespawnPoint(respawn_point=13002020)
    SaveRequest()
    Wait(5.199999809265137)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(CharacterDead(PLAYER))
    if AND_2:
        return
    SetBackreadStateAlternate(13000800, False)
    EnableFlag(300)
    EnableFlag(301)
    DisableFlag(302)
    EnableFlag(71300)
    DisableFlagRange((71100, 71110))
    DisableLoadingScreenText()
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=13000050,
        cutscene_flags=0,
        move_to_region=11052010,
        map_id=11050000,
        player_id=10000,
        unk_20_24=13000,
        unk_24_25=True,
    )
    WaitFramesAfterCutscene(frames=1)
    SetRespawnPoint(respawn_point=11052010)
    SaveRequest()
    EnableFlag(118)


@RestartOnRest(901)
def Event_901():
    """Event 901"""
    if FlagEnabled(110):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1054539205))
    OR_1.Add(FlagEnabled(1054539200))
    OR_1.Add(FlagEnabled(1054539201))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    EnableFlag(9001)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=13002500)
    SaveRequest()
    EnableFlag(110)
    EnableFlag(302)
    EnableFlag(9021)
    GotoIfFlagEnabled(Label.L1, flag=1054539201)
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=150000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=640000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=910000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=760000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=440000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=470000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=820000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1010000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1760000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1770000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1780000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=2010000))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=330100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1810100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1811100))
    SkipLinesIfConditionTrue(3, OR_10)
    EnableFlag(780010)
    DisableFlag(780011)
    SkipLines(2)
    DisableFlag(780010)
    EnableFlag(780011)
    EnableFlag(111)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=60540000,
        cutscene_flags=0,
        move_to_region=13002500,
        map_id=13000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
        change_weather=True,
        weather_duration=300.0,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=60540010,
        cutscene_flags=CutsceneFlags.Unknown16,
        player_id=10000,
        change_weather=True,
        weather_duration=300.0,
        change_time=True,
        time=(6, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(9001)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(9000)
    EnableFlag(112)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=60540001,
        cutscene_flags=0,
        move_to_region=13002500,
        map_id=13000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
        change_weather=True,
        weather_duration=200.0,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=60540011,
        cutscene_flags=CutsceneFlags.Unknown16,
        player_id=10000,
        change_weather=True,
        weather_duration=300.0,
        change_time=True,
        time=(6, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(9001)
    End()


@RestartOnRest(902)
def Event_902():
    """Event 902"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1054539206))
    AND_1.Add(FlagEnabled(110))
    AND_1.Add(InsideMap(game_map=SOUTHEAST_MOUNTAINTOPS_SE_NW))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9001)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=13002500)
    SaveRequest()
    DisableFlag(1054539206)
    EnableFlag(302)
    EnableFlag(9021)
    GotoIfFlagEnabled(Label.L1, flag=112)
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=150000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=640000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=910000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=760000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=440000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=470000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=820000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1010000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1760000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1770000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=1780000))
    OR_10.Add(PlayerHasHeadArmorEquipped(armor=2010000))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=330100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1810100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1811100))
    SkipLinesIfConditionTrue(3, OR_10)
    EnableFlag(780010)
    DisableFlag(780011)
    SkipLines(2)
    DisableFlag(780010)
    EnableFlag(780011)
    EnableFlag(111)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=60540000,
        cutscene_flags=0,
        move_to_region=13002500,
        map_id=13000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
        change_weather=True,
        weather_duration=300.0,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=60540010,
        cutscene_flags=CutsceneFlags.Unknown16,
        player_id=10000,
        change_weather=True,
        weather_duration=300.0,
        change_time=True,
        time=(6, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(9001)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(9000)
    EnableFlag(112)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=60540001,
        cutscene_flags=0,
        move_to_region=13002500,
        map_id=13000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
        change_weather=True,
        weather_duration=200.0,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=60540011,
        cutscene_flags=CutsceneFlags.Unknown16,
        player_id=10000,
        change_weather=True,
        weather_duration=300.0,
        change_time=True,
        time=(6, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(9001)
    End()


@ContinueOnRest(910)
def Event_910():
    """Event 910"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9415):
        return
    GotoIfFlagDisabled(Label.L0, flag=310)
    if FlagDisabled(9416):
        SetAreaWelcomeMessageState(state=False)
        EnableFlag(9416)
    SetCurrentTime(
        time=(22, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )
    SetWeather(weather=Weather.Cloudless, duration=-1.0, immediate_change=True)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    if FlagDisabled(9417):
        Wait(0.5)
        DisplayDialog(text=30140, anchor_entity=0, display_distance=5.0, number_buttons=NumberButtons.OneButton)
        EnableFlag(9417)
    OR_13.Add(FlagEnabled(76422))
    OR_13.Add(FlagEnabled(73016))
    
    MAIN.Await(OR_13)
    
    SetWeather(weather=Weather.Cloudless, duration=15000.0, immediate_change=False)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    EnableFlag(9415)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9130))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    SetRespawnPoint(respawn_point=1052382020)
    SaveRequest()
    if FlagDisabled(9414):
        EnableFlag(9414)
        Wait(10.0)
    AND_2.Add(CharacterDead(PLAYER))
    if AND_2:
        return
    OR_9.Add(MapLoaded(game_map=SOUTHEAST_CAELID_NW_NW))
    OR_9.Add(MapLoaded(game_map=SOUTH_CAELID_NE_SE))
    GotoIfConditionTrue(Label.L9, input_condition=OR_9)
    WarpToMap(game_map=SOUTH_CAELID_NE_SE, player_start=1051382020)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(9001)
    WaitFrames(frames=1)
    DisableLoadingScreenText()
    OR_10.Add(MapLoaded(game_map=SOUTHEAST_CAELID_NW_NW))
    SkipLinesIfConditionTrue(2, OR_10)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=60510011,
        cutscene_flags=0,
        player_id=10000,
        change_weather=True,
        weather=Weather.Cloudless,
        change_time=True,
        time=(22, 30, 0),
    )
    SkipLines(1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=60510010,
        cutscene_flags=0,
        player_id=10000,
        change_weather=True,
        weather=Weather.Cloudless,
        change_time=True,
        time=(22, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)
    FadeToBlack(strength=1.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)
    EnableFlag(310)
    SetNetworkInteractionState(state=False)
    End()


@RestartOnRest(920)
def Event_920():
    """Event 920"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(116):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 502190))
    
    MAIN.Await(AND_1)
    
    EnableFlag(116)
    DisableFlag(7500)
    DisableFlag(9431)


@RestartOnRest(921)
def Event_921():
    """Event 921"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(116):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(108))
    AND_1.Add(FlagEnabled(9120))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002050))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4230)


@RestartOnRest(922)
def Event_922():
    """Event 922"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 502160))
    
    MAIN.Await(AND_1)
    
    WarpToMap(game_map=MOHGWYN_PALACE, player_start=12052021)


@ContinueOnRest(930)
def Event_930(
    _,
    cutscene_id: int,
    cutscene_id_1: int,
    entity: uint,
    action_button_id: int,
    item: int,
    item_1: int,
    map_id: int,
    move_to_region: uint,
    move_to_region_1: uint,
    unk_20_24: int,
):
    """Event 930"""
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(PlayerInOwnWorld())
    if ValueNotEqual(left=item, right=0):
        AND_1.Add(PlayerHasGood(item))
    if ValueNotEqual(left=item_1, right=0):
        AND_1.Add(PlayerHasGood(item_1))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9021)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=cutscene_id,
        cutscene_flags=0,
        move_to_region=move_to_region,
        map_id=map_id,
        player_id=10000,
        unk_20_24=unk_20_24,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutscene(cutscene_id_1, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Restart()
    SkipLinesIfPlayerNotInOwnWorld(2)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=cutscene_id,
        cutscene_flags=0,
        move_to_region=move_to_region,
        map_id=map_id,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    SkipLines(4)
    if UnsignedNotEqual(left=move_to_region_1, right=0):
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=cutscene_id,
            cutscene_flags=0,
            move_to_region=move_to_region_1,
            map_id=map_id,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=cutscene_id,
            cutscene_flags=0,
            move_to_region=move_to_region,
            map_id=map_id,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=cutscene_id_1,
        cutscene_flags=CutsceneFlags.Unknown16,
        move_to_region=move_to_region,
        map_id=map_id,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    SkipLines(4)
    if UnsignedNotEqual(left=move_to_region_1, right=0):
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=cutscene_id_1,
            cutscene_flags=CutsceneFlags.Unknown16,
            move_to_region=move_to_region_1,
            map_id=map_id,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=cutscene_id_1,
            cutscene_flags=CutsceneFlags.Unknown16,
            move_to_region=move_to_region,
            map_id=map_id,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    Restart()


@ContinueOnRest(936)
def Event_936(
    _,
    cutscene_id: int,
    cutscene_id_1: int,
    flag: uint,
    map_id: int,
    move_to_region: uint,
    unk_20_24: int,
    change_weather: uchar,
    weather: char,
    weather_duration: float,
):
    """Event 936"""
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    EnableFlag(9021)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=cutscene_id,
        cutscene_flags=0,
        move_to_region=move_to_region,
        map_id=map_id,
        player_id=10000,
        unk_20_24=unk_20_24,
        unk_24_25=False,
        change_weather=change_weather,
        weather=weather,
        weather_duration=weather_duration,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutscene(cutscene_id_1, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Restart()


@ContinueOnRest(945)
def Event_945():
    """Event 945"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(105):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(104))
    
    MAIN.Await(AND_1)
    
    WarpToMap(game_map=ROUNDTABLE_HOLD, player_start=11100980, unk_8_12=61000)
    DisableThisSlotFlag()


@RestartOnRest(950)
def Event_950():
    """Event 950"""
    if FlagEnabled(951):
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1042361950, radius=2.0))
    OR_11.Add(AND_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=1043371950, radius=2.0))
    OR_11.Add(AND_2)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=1046381950, radius=2.0))
    OR_11.Add(AND_3)
    AND_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=1041381950, radius=2.0))
    OR_11.Add(AND_4)
    AND_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=1044351950, radius=2.0))
    OR_11.Add(AND_5)
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=1042371950, radius=2.0))
    OR_11.Add(AND_6)
    AND_7.Add(EntityWithinDistance(entity=PLAYER, other_entity=1044341950, radius=2.0))
    OR_11.Add(AND_7)
    AND_8.Add(EntityWithinDistance(entity=PLAYER, other_entity=1043351950, radius=2.0))
    OR_11.Add(AND_8)
    AND_11.Add(OR_11)
    AND_11.Add(FlagEnabled(9000))
    AND_12.Add(EventValue(flag=955, bit_count=3) == 2)
    AND_13.Add(EventValue(flag=955, bit_count=3) >= 3)
    AND_14.Add(AND_10)
    AND_14.Add(AND_11)
    OR_14.Add(AND_12)
    OR_14.Add(AND_13)
    OR_14.Add(AND_2)
    OR_14.Add(AND_6)
    AND_14.Add(OR_14)
    OR_15.Add(AND_14)
    OR_15.Add(TimeElapsed(seconds=3.0))
    
    MAIN.Await(OR_15)
    
    EndIfFinishedConditionFalse(input_condition=AND_14)
    EnableFlag(9001)
    WaitFrames(frames=1)
    EnableFlag(951)
    EnableFlag(953)
    EnableFlag(9021)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=AND_8)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=AND_7)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=AND_6)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=AND_5)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=AND_4)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    Goto(Label.L10)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    PlayCutscene(60420000, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1042362980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=-150.6300048828125)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    PlayCutscene(60420001, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1043372980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=108.81999969482422)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    PlayCutscene(60420002, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1046382980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=-155.69000244140625)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    PlayCutscene(60420003, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1041382980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=49.130001068115234)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    PlayCutscene(60420004, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1044352980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=-144.17999267578125)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 6 --- #
    DefineLabel(6)
    PlayCutscene(60420005, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1042372980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=4.019999980926514, y_angle=18.700000762939453)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 7 --- #
    DefineLabel(7)
    PlayCutscene(60420006, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1044342980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=17.420000076293945)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 8 --- #
    DefineLabel(8)
    PlayCutscene(60420007, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Move(PLAYER, destination=1043352980, destination_type=CoordEntityType.Region, short_move=True)
    SetCameraAngle(x_angle=5.0, y_angle=-126.7699966430664)
    SetWeather(weather=Weather.Default, duration=300.0, immediate_change=True)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(9001)


@ContinueOnRest(960)
def Event_960(_, flag: uint):
    """Event 960"""
    if FlagEnabled(951):
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(951))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(951):
        return
    IncrementEventValue(955, bit_count=3, max_value=7)


@ContinueOnRest(970)
def Event_970():
    """Event 970"""
    DisableNetworkSync()
    if FlagEnabled(82001):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(InsideMap(game_map=(12, -1, -1, -1)))
    
    MAIN.Await(AND_1)
    
    EnableFlag(82001)


@RestartOnRest(980)
def Event_980():
    """Event 980"""
    if FlagEnabled(1099002980):
        return
    DisableFlagRange((9800, 9809))
    EnableRandomFlagInRange(flag_range=(9800, 9809))
    EnableFlag(1099002980)


@ContinueOnRest(1020)
def Event_1020():
    """Event 1020"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=9021)
    GotoIfFlagEnabled(Label.L1, flag=1099002100)
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=False)
    OR_1.Add(FlagEnabled(1099002100))
    OR_1.Add(FlagEnabled(9021))
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=True)
    DisableFlag(9021)
    OR_2.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(FlagEnabled(1099002100))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L2, flag=1099002100)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=True)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(FlagDisabled(1099002100))
    
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(1030)
def Event_1030():
    """Event 1030"""
    DisableNetworkSync()
    OR_1.Add(WeatherLotActive(weather_lot_param_id=1000))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=2000))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=2010))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=2020))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=3000))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=3010))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=3020))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=3021))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=3022))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=4000))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=4001))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=4010))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=4020))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=5000))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=5010))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=5011))
    OR_1.Add(WeatherLotActive(weather_lot_param_id=6000))
    OR_2.Add(WeatherLotActive(weather_lot_param_id=620000100))
    OR_2.Add(WeatherLotActive(weather_lot_param_id=620000101))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(9840))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    OR_5.Add(WeatherLotInactive(weather_lot_param_id=1000))
    GotoIfConditionTrue(Label.L1, input_condition=OR_5)
    SetWeather(weather=Weather.Cloudless, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=1000))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_6.Add(WeatherLotInactive(weather_lot_param_id=2000))
    GotoIfConditionTrue(Label.L1, input_condition=OR_6)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=2000))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_7.Add(WeatherLotInactive(weather_lot_param_id=2010))
    GotoIfConditionTrue(Label.L1, input_condition=OR_7)
    SetWeather(weather=Weather.FlatClouds, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=2010))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_8.Add(WeatherLotInactive(weather_lot_param_id=2020))
    GotoIfConditionTrue(Label.L1, input_condition=OR_8)
    SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=2020))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_10.Add(WeatherLotInactive(weather_lot_param_id=3000))
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    SetWeather(weather=Weather.Rain, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=3000))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_11.Add(WeatherLotInactive(weather_lot_param_id=3010))
    GotoIfConditionTrue(Label.L1, input_condition=OR_11)
    SetWeather(weather=Weather.RainyClouds, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=3010))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_12.Add(WeatherLotInactive(weather_lot_param_id=3020))
    GotoIfConditionTrue(Label.L1, input_condition=OR_12)
    SetWeather(weather=Weather.WindyRain, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=3020))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_13.Add(WeatherLotInactive(weather_lot_param_id=3021))
    GotoIfConditionTrue(Label.L1, input_condition=OR_13)
    SetWeather(weather=Weather.WindyFog, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=3021))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_14.Add(WeatherLotInactive(weather_lot_param_id=3022))
    GotoIfConditionTrue(Label.L1, input_condition=OR_14)
    SetWeather(weather=Weather.ScatteredRain, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=3022))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_5.Add(WeatherLotInactive(weather_lot_param_id=4000))
    GotoIfConditionTrue(Label.L1, input_condition=AND_5)
    SetWeather(weather=Weather.Snow, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=4000))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_6.Add(WeatherLotInactive(weather_lot_param_id=4001))
    GotoIfConditionTrue(Label.L1, input_condition=AND_6)
    SetWeather(weather=Weather.Unknown18, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=4001))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_7.Add(WeatherLotInactive(weather_lot_param_id=4010))
    GotoIfConditionTrue(Label.L1, input_condition=AND_7)
    SetWeather(weather=Weather.HeavySnow, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=4010))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_8.Add(WeatherLotInactive(weather_lot_param_id=4020))
    GotoIfConditionTrue(Label.L1, input_condition=AND_8)
    SetWeather(weather=Weather.SnowyHeavyFog, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=4020))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_10.Add(WeatherLotInactive(weather_lot_param_id=5000))
    GotoIfConditionTrue(Label.L1, input_condition=AND_10)
    SetWeather(weather=Weather.Fog, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=5000))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_11.Add(WeatherLotInactive(weather_lot_param_id=5010))
    GotoIfConditionTrue(Label.L1, input_condition=AND_11)
    SetWeather(weather=Weather.HeavyFog, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=5010))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_12.Add(WeatherLotInactive(weather_lot_param_id=5011))
    GotoIfConditionTrue(Label.L1, input_condition=AND_12)
    SetWeather(weather=Weather.RainyHeavyFog, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=5011))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_14.Add(WeatherLotInactive(weather_lot_param_id=6000))
    GotoIfConditionTrue(Label.L1, input_condition=AND_14)
    SetWeather(weather=Weather.WindyPuffyClouds, duration=-1.0, immediate_change=False)
    Wait(1.0)
    
    MAIN.Await(WeatherLotInactive(weather_lot_param_id=6000))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_15.Add(WeatherLotInactive(weather_lot_param_id=620000100))
    AND_15.Add(WeatherLotInactive(weather_lot_param_id=620000101))
    GotoIfConditionTrue(Label.L1, input_condition=AND_15)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    Wait(1.0)
    AND_15.Add(WeatherLotInactive(weather_lot_param_id=620000100))
    AND_15.Add(WeatherLotInactive(weather_lot_param_id=620000101))
    
    MAIN.Await(AND_15)
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    EnableFlag(9840)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()


@RestartOnRest(1040)
def Event_1040():
    """Event 1040"""
    DisableNetworkSync()
    DeleteAssetVFX(1060001500)
    RemoveSpecialEffect(PLAYER, 4200)
    RemoveSpecialEffect(PLAYER, 4201)
    SetWindVFX(wind_vfx_id=-1)
    AND_1.Add(TimeOfDayInRange(earliest=(0, 0, 0), latest=(2, 59, 59)))
    AND_1.Add(WeatherState(weather=Weather.Default, unk_4_8=0.0, unk_8_12=0.0))
    AND_1.Add(InsideMap(game_map=(60, -1, -1, -1)))
    OR_1.Add(AND_1)
    AND_2.Add(InsideMap(game_map=CHAPEL_OF_ANTICIPATION))
    AND_2.Add(FlagDisabled(102))
    AND_2.Add(PlayerInOwnWorld())
    OR_1.Add(AND_2)
    OR_2.Add(MultiplayerEvent(event_id=0))
    OR_3.Add(MultiplayerEvent(event_id=10))
    OR_4.Add(MultiplayerEvent(event_id=20))
    OR_5.Add(MultiplayerEvent(event_id=30))
    OR_6.Add(MultiplayerEvent(event_id=40))
    OR_7.Add(MultiplayerEvent(event_id=50))
    OR_8.Add(MultiplayerEvent(event_id=60))
    OR_9.Add(MultiplayerEvent(event_id=70))
    OR_10.Add(MultiplayerEvent(event_id=80))
    OR_15.Add(OR_2)
    OR_15.Add(OR_3)
    OR_15.Add(OR_4)
    OR_15.Add(OR_5)
    OR_15.Add(OR_6)
    OR_15.Add(OR_7)
    OR_15.Add(OR_8)
    OR_15.Add(OR_9)
    OR_15.Add(OR_10)
    OR_1.Add(OR_15)
    OR_1.Add(FlagEnabled(9989))
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_15)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    SetWindVFX(wind_vfx_id=808004)
    Wait(5.0)
    CreateAssetVFX(1060001500, vfx_id=200, model_point=806800)
    Wait(14.0)
    AddSpecialEffect(PLAYER, 4200)
    AddSpecialEffect(PLAYER, 4201)
    AND_10.Add(TimeOfDayInRange(earliest=(0, 0, 0), latest=(3, 29, 59)))
    AND_10.Add(WeatherState(weather=Weather.Default, unk_4_8=0.0, unk_8_12=0.0))
    AND_10.Add(InsideMap(game_map=(60, -1, -1, -1)))
    AND_11.Add(not AND_10)
    AND_11.Add(FlagDisabled(9989))
    OR_10.Add(AND_11)
    OR_10.Add(TimeElapsed(seconds=300.0))
    
    MAIN.Await(OR_10)
    
    SetWindVFX(wind_vfx_id=-1)
    DeleteAssetVFX(1060001500)
    RemoveSpecialEffect(PLAYER, 4200)
    RemoveSpecialEffect(PLAYER, 4201)
    Wait(120.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SetWindVFX(wind_vfx_id=808004)
    AddSpecialEffect(PLAYER, 4200)
    AND_12.Add(InsideMap(game_map=CHAPEL_OF_ANTICIPATION))
    AND_12.Add(FlagDisabled(102))
    AND_12.Add(PlayerInOwnWorld())
    
    MAIN.Await(not AND_12)
    
    SetWindVFX(wind_vfx_id=-1)
    RemoveSpecialEffect(PLAYER, 4200)
    Wait(10.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_15.Add(InsideMap(game_map=(60, -1, -1, -1)))
    GotoIfConditionFalse(Label.L2, input_condition=AND_15)
    SetWindVFX(wind_vfx_id=808004)
    Wait(5.0)
    CreateAssetVFX(1060001500, vfx_id=200, model_point=806800)
    Wait(14.0)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4200)
    AddSpecialEffect(PLAYER, 4201)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_2)
    DisplayNetworkMessage(text=3000201, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_3)
    DisplayNetworkMessage(text=3000211, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_4)
    DisplayNetworkMessage(text=3000221, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_5)
    DisplayNetworkMessage(text=3000231, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_6)
    DisplayNetworkMessage(text=3000241, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_7)
    DisplayNetworkMessage(text=3000251, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_8)
    DisplayNetworkMessage(text=3000261, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_9)
    DisplayNetworkMessage(text=3000271, unk_4_5=False)
    Goto(Label.L15)
    SkipLinesIfFinishedConditionFalse(2, input_condition=OR_10)
    DisplayNetworkMessage(text=3000281, unk_4_5=False)
    Goto(Label.L15)

    # --- Label 15 --- #
    DefineLabel(15)
    Wait(300.0)
    SetWindVFX(wind_vfx_id=-1)
    DeleteAssetVFX(1060001500)
    RemoveSpecialEffect(PLAYER, 4200)
    RemoveSpecialEffect(PLAYER, 4201)
    Wait(150.0)
    Restart()


@RestartOnRest(1050)
def Event_1050():
    """Event 1050"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(7500))
    AND_2.Add(FlagDisabled(7500))
    AND_2.Add(CharacterHasSpecialEffect(20000, 503315))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    AddSpecialEffect(20000, 503315)
    Wait(0.10000000149011612)
    AND_10.Add(FlagDisabled(7500))
    
    MAIN.Await(AND_10)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(20000, 503316)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(1080)
def Event_1080():
    """Event 1080"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9080))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4286)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(9000))
    AND_2.Add(FlagEnabled(9080))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 4286))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(9080))
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(PLAYER, 4287)
    DisableFlag(9080)
    WaitFramesAfterCutscene(frames=1)
    Restart()


@ContinueOnRest(1100)
def Event_1100(_, flag: uint, item_lot__item_lot_param_id: int, item_lot_param_id: int, flag_1: uint):
    """Event 1100"""
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    if ValueNotEqual(left=item_lot__item_lot_param_id, right=0):
        AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    Wait(5.0)
    if ValueNotEqual(left=item_lot_param_id, right=0):
        AwardItemLot(item_lot_param_id, host_only=True)


@ContinueOnRest(1200)
def Event_1200(_, flag: uint, item_lot__item_lot_param_id: int, item_lot_param_id: int, flag_1: uint):
    """Event 1200"""
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    if ValueNotEqual(left=item_lot__item_lot_param_id, right=0):
        AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    Wait(5.0)
    if ValueNotEqual(left=item_lot_param_id, right=0):
        AwardItemLot(item_lot_param_id, host_only=True)


@ContinueOnRest(1400)
def Event_1400():
    """Event 1400"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=6950)
    if FlagDisabled(60849):
        return
    RemoveGesture(gesture_param_id=108)
    DisableFlag(60849)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(60849):
        return
    AwardGesture(gesture_param_id=108)
    EnableFlag(60849)


@ContinueOnRest(1401)
def Event_1401():
    """Event 1401"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L0, flag=6950)
    GotoIfFlagDisabled(Label.L15, flag=60850)
    RemoveGesture(gesture_param_id=109)
    DisableFlag(60850)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(7680)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L16, flag=60850)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(7680))
    
    MAIN.Await(AND_1)
    
    AwardGesture(gesture_param_id=109)
    EnableFlag(60850)

    # --- Label 16 --- #
    DefineLabel(16)
    DisableFlag(7680)


@RestartOnRest(1410)
def Event_1410(_, flag: uint, command_id__gesture_param_id: int, special_effect: int, character: uint, flag_1: uint):
    """Event 1410"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=80, command_slot=0)
    AICommand(character, command_id=command_id__gesture_param_id, command_slot=1)
    ReplanAI(character)
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_2.Add(AND_2)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AICommand(character, command_id=-1, command_slot=0)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    EndIfFinishedConditionFalse(input_condition=AND_2)
    if FlagEnabled(flag):
        return
    AwardGesture(gesture_param_id=command_id__gesture_param_id)
    EnableFlag(flag)


@RestartOnRest(1411)
def Event_1411(
    _,
    flag: uint,
    command_id__gesture_param_id: int,
    special_effect: int,
    character: uint,
    flag_1: uint,
    character_1: uint,
    flag_2: uint,
    character_2: uint,
    flag_3: uint,
):
    """Event 1411"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag_1):
        AICommand(character, command_id=80, command_slot=0)
        AICommand(character, command_id=command_id__gesture_param_id, command_slot=1)
        ReplanAI(character)
    if FlagEnabled(flag_2):
        AICommand(character_1, command_id=80, command_slot=0)
        AICommand(character_1, command_id=command_id__gesture_param_id, command_slot=1)
        ReplanAI(character_1)
    if FlagEnabled(flag_3):
        AICommand(character_2, command_id=80, command_slot=0)
        AICommand(character_2, command_id=command_id__gesture_param_id, command_slot=1)
        ReplanAI(character_2)
    OR_2.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_2.Add(CharacterHasSpecialEffect(character_1, special_effect))
    OR_2.Add(CharacterHasSpecialEffect(character_2, special_effect))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag_1):
        AICommand(character, command_id=-1, command_slot=0)
        AICommand(character, command_id=-1, command_slot=1)
        ReplanAI(character)
    if FlagEnabled(flag_2):
        AICommand(character_1, command_id=-1, command_slot=0)
        AICommand(character_1, command_id=-1, command_slot=1)
        ReplanAI(character_1)
    if FlagEnabled(flag_3):
        AICommand(character_2, command_id=-1, command_slot=0)
        AICommand(character_2, command_id=-1, command_slot=1)
        ReplanAI(character_2)
    if FlagEnabled(flag):
        return
    AwardGesture(gesture_param_id=command_id__gesture_param_id)
    EnableFlag(flag)


@RestartOnRest(1412)
def Event_1412(_, flag: uint, command_id__gesture_param_id: int, special_effect: int, character: uint, flag_1: uint):
    """Event 1412"""
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=18.0))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=80, command_slot=0)
    AICommand(character, command_id=command_id__gesture_param_id, command_slot=1)
    ReplanAI(character)
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_2.Add(AND_2)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AICommand(character, command_id=-1, command_slot=0)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    EndIfFinishedConditionFalse(input_condition=AND_2)
    if FlagEnabled(flag):
        return
    AwardGesture(gesture_param_id=command_id__gesture_param_id)
    EnableFlag(flag)


@RestartOnRest(1450)
def Event_1450(_, flag: uint, right: uint, right_1: uint, right_2: uint):
    """Event 1450"""
    DisableNetworkSync()
    AND_9.Add(PlayerInOwnWorld())
    AND_9.Add(FlagEnabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_9.Add(FlagEnabled(right))
    if UnsignedNotEqual(left=0, right=right_1):
        AND_9.Add(FlagEnabled(right_1))
    if UnsignedNotEqual(left=0, right=right_2):
        AND_9.Add(FlagEnabled(right_2))
    if AND_9:
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if UnsignedNotEqual(left=0, right=right):
        EnableFlag(right)
    if UnsignedNotEqual(left=0, right=right_1):
        EnableFlag(right_1)
    if UnsignedNotEqual(left=0, right=right_2):
        EnableFlag(right_2)


@RestartOnRest(1460)
def Event_1460():
    """Event 1460"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66000))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66010))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66020))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66030))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66040))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66050))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66060))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66070))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66080))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66090))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66100))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66110))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66120))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66130))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66140))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66150))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66160))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66170))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66180))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66190))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9500, flag=9560, bit_count=5)
    AND_10.Add(EventValue(flag=9560, bit_count=5) == 20)
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    WaitFrames(frames=1)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if FlagDisabled(6902):
        EnableFlag(6902)


@RestartOnRest(1461)
def Event_1461():
    """Event 1461"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66400))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66410))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66420))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66430))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66440))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66450))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66460))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66470))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66480))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66490))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9501, flag=9565, bit_count=5)
    AND_10.Add(EventValue(flag=9565, bit_count=5) == 10)
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    WaitFrames(frames=1)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if FlagDisabled(6903):
        EnableFlag(6903)


@RestartOnRest(1462)
def Event_1462():
    """Event 1462"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66700))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66710))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66720))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66730))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66740))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66750))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66760))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66770))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66780))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 66790))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9510, flag=9570, bit_count=5)
    AND_10.Add(EventValue(flag=9570, bit_count=5) == 10)
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    WaitFrames(frames=1)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if FlagDisabled(6904):
        EnableFlag(6904)


@ContinueOnRest(1600)
def Event_1600(_, flag: uint, flag_1: uint, asset: uint, asset_1: uint):
    """Event 1600"""
    DisableNetworkSync()
    GotoIfPlayerInOwnWorld(Label.L0)
    if UnsignedEqual(left=0, right=asset):
        return
    DisableAsset(asset_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag)
    if UnsignedEqual(left=0, right=asset):
        return
    DisableAsset(asset_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if UnsignedNotEqual(left=0, right=asset):
        CreateAssetVFX(asset, vfx_id=200, model_point=803220)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    DisplayBanner(BannerType.MapFound)
    EnableFlag(flag_1)
    Wait(1.0)
    if UnsignedNotEqual(left=0, right=asset):
        ForceAnimation(asset_1, 1)
    if UnsignedNotEqual(left=0, right=asset):
        DeleteAssetVFX(asset)
    End()


@RestartOnRest(1630)
def Event_1630(
    _,
    flag: uint,
    flag_1: uint,
    right: uint,
    right_1: uint,
    right_2: uint,
    right_3: uint,
    right_4: uint,
    right_5: uint,
    right_6: uint,
):
    """Event 1630"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    if UnsignedNotEqual(left=0, right=right_1):
        AND_1.Add(FlagEnabled(right_1))
    if UnsignedNotEqual(left=0, right=right_2):
        AND_1.Add(FlagEnabled(right_2))
    if UnsignedNotEqual(left=0, right=right_3):
        AND_1.Add(FlagEnabled(right_3))
    if UnsignedNotEqual(left=0, right=right_4):
        AND_1.Add(FlagEnabled(right_4))
    if UnsignedNotEqual(left=0, right=right_5):
        AND_1.Add(FlagEnabled(right_5))
    if UnsignedNotEqual(left=0, right=right_6):
        AND_1.Add(FlagEnabled(right_6))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(1700)
def Event_1700():
    """Event 1700"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(710530):
        return
    if FlagEnabled(69100):
        return
    AND_1.Add(FlagEnabled(710530))
    AND_1.Add(TimeElapsed(seconds=2.0))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=1530, unk_4_5=True, unk_5_6=True)
    EnableFlag(700530)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9110, flag=700530, bit_count=1)
    EnableFlag(69100)


@RestartOnRest(1701)
def Event_1701():
    """Event 1701"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(18000020))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710530)


@RestartOnRest(1702)
def Event_1702():
    """Event 1702"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(700550):
        return
    if FlagEnabled(69110):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(710550))
    AND_1.Add(FlagEnabled(60110))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=1550, unk_4_5=True, unk_5_6=True)
    EnableFlag(700550)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=710550, bit_count=1)
    EnableFlag(69110)


@RestartOnRest(1703)
def Event_1703():
    """Event 1703"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(710570):
        return
    if FlagEnabled(69130):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(60120))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=1570, unk_4_5=True, unk_5_6=True)
    EnableFlag(710570)
    if ValueNotEqual(left=9113, right=0):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9113, flag=710570, bit_count=1)
    EnableFlag(69130)


@RestartOnRest(1704)
def Event_1704():
    """Event 1704"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(69350):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(60120))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    Wait(0.30000001192092896)
    DisplayTutorialMessage(tutorial_param_id=1580, unk_4_5=True, unk_5_6=True)
    EnableFlag(69350)
    if ValueNotEqual(left=9135, right=0):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9135, flag=710580, bit_count=1)


@RestartOnRest(1705)
def Event_1705():
    """Event 1705"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(69160):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(710600))
    AND_1.Add(FlagDisabled(69160))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=1600, unk_4_5=True, unk_5_6=True)
    EnableFlag(69160)
    EnableFlag(710750)
    if ValueNotEqual(left=9116, right=0):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=710600, bit_count=1)


@RestartOnRest(1720)
def Event_1720(_, flag: uint, flag_1: uint, tutorial_param_id: int, item: int):
    """Event 1720"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EnableFlag(flag)
    if ValueNotEqual(left=item, right=0):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag_1, bit_count=1)


@RestartOnRest(1750)
def Event_1750():
    """Event 1750"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(710060):
        return
    OR_1.Add(PlayerHasWeapon(33000000))
    OR_1.Add(PlayerHasWeapon(33040000))
    OR_1.Add(PlayerHasWeapon(33050000))
    OR_1.Add(PlayerHasWeapon(33060000))
    OR_1.Add(PlayerHasWeapon(33090000))
    OR_1.Add(PlayerHasWeapon(33120000))
    OR_1.Add(PlayerHasWeapon(33130000))
    OR_1.Add(PlayerHasWeapon(33170000))
    OR_1.Add(PlayerHasWeapon(33180000))
    OR_1.Add(PlayerHasWeapon(33190000))
    OR_1.Add(PlayerHasWeapon(33200000))
    OR_1.Add(PlayerHasWeapon(33210000))
    OR_1.Add(PlayerHasWeapon(33230000))
    OR_1.Add(PlayerHasWeapon(33240000))
    OR_1.Add(PlayerHasWeapon(33250000))
    OR_1.Add(PlayerHasWeapon(33260000))
    OR_1.Add(PlayerHasWeapon(33270000))
    OR_1.Add(PlayerHasWeapon(33280000))
    OR_1.Add(PlayerHasWeapon(34000000))
    OR_1.Add(PlayerHasWeapon(34010000))
    OR_1.Add(PlayerHasWeapon(34020000))
    OR_1.Add(PlayerHasWeapon(34030000))
    OR_1.Add(PlayerHasWeapon(34040000))
    OR_1.Add(PlayerHasWeapon(34060000))
    OR_1.Add(PlayerHasWeapon(34070000))
    OR_1.Add(PlayerHasWeapon(34080000))
    OR_1.Add(PlayerHasWeapon(34090000))
    AND_1.Add(OR_1)
    AND_1.Add(OutsideMap(game_map=CHAPEL_OF_ANTICIPATION))
    AND_1.Add(OutsideMap(game_map=STRANDED_GRAVEYARD))
    AND_1.Add(PlayerTargeted(min_npc_threat_level=1, max_npc_threat_level=31, ai_status=AIStatusType.Battle))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(710060)


@RestartOnRest(1751)
def Event_1751():
    """Event 1751"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(710130):
        return
    OR_1.Add(PlayerHasWeapon(40000000))
    OR_1.Add(PlayerHasWeapon(40010000))
    OR_1.Add(PlayerHasWeapon(40020000))
    OR_1.Add(PlayerHasWeapon(40030000))
    OR_1.Add(PlayerHasWeapon(40050000))
    OR_1.Add(PlayerHasWeapon(41000000))
    OR_1.Add(PlayerHasWeapon(41010000))
    OR_1.Add(PlayerHasWeapon(41020000))
    OR_1.Add(PlayerHasWeapon(41030000))
    OR_1.Add(PlayerHasWeapon(41040000))
    OR_1.Add(PlayerHasWeapon(41060000))
    OR_1.Add(PlayerHasWeapon(41070000))
    OR_1.Add(PlayerHasWeapon(42000000))
    OR_1.Add(PlayerHasWeapon(42000000))
    OR_1.Add(PlayerHasWeapon(42030000))
    OR_1.Add(PlayerHasWeapon(42040000))
    OR_1.Add(PlayerHasWeapon(43000000))
    OR_1.Add(PlayerHasWeapon(43020000))
    OR_1.Add(PlayerHasWeapon(43030000))
    OR_1.Add(PlayerHasWeapon(43050000))
    OR_1.Add(PlayerHasWeapon(43060000))
    OR_1.Add(PlayerHasWeapon(43080000))
    OR_1.Add(PlayerHasWeapon(43100000))
    OR_1.Add(PlayerHasWeapon(43110000))
    AND_1.Add(OR_1)
    AND_1.Add(OutsideMap(game_map=CHAPEL_OF_ANTICIPATION))
    AND_1.Add(OutsideMap(game_map=STRANDED_GRAVEYARD))
    AND_1.Add(PlayerTargeted(min_npc_threat_level=1, max_npc_threat_level=31, ai_status=AIStatusType.Battle))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(710130)


@RestartOnRest(1752)
def Event_1752():
    """Event 1752"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(710710):
        return
    AND_1.Add(FlagEnabled(60110))
    AND_1.Add(FlagEnabled(700550))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9530))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(710710)


@RestartOnRest(1770)
def Event_1770(_, flag: uint, flag_1: uint, tutorial_param_id: int):
    """Event 1770"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EnableFlag(flag)


@RestartOnRest(1790)
def Event_1790():
    """Event 1790"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(710600):
        return
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 81))
    
    MAIN.Await(AND_1)
    
    Wait(1.5)
    EnableFlag(710800)


@RestartOnRest(1800)
def Event_1800():
    """Event 1800"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2001):
        return
    AND_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9431))
    AND_1.Add(FlagEnabled(9431))
    AND_11.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9431))
    AND_11.Add(FlagDisabled(9431))
    AND_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9432))
    AND_2.Add(FlagEnabled(9432))
    AND_3.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9433))
    AND_3.Add(FlagEnabled(9433))
    OR_9.Add(AND_1)
    OR_9.Add(AND_2)
    OR_9.Add(AND_3)
    OR_9.Add(AND_11)
    AND_9.Add(OR_9)
    AND_9.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_9)
    
    EnableFlag(9420)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_3)
    GotoIfFinishedConditionTrue(Label.L11, input_condition=AND_11)

    # --- Label 11 --- #
    DefineLabel(11)
    GotoIfFlagEnabled(Label.L2, flag=9432)
    GotoIfFlagEnabled(Label.L3, flag=9433)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=0, face_param_id=-1)
    DisableFlag(9420)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=0, face_param_id=81000)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L9, flag=9431)
    GotoIfFlagEnabled(Label.L9, flag=9434)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=0, face_param_id=81001)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L9, flag=9431)
    GotoIfFlagEnabled(Label.L9, flag=9432)
    GotoIfFlagEnabled(Label.L9, flag=9434)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=0, face_param_id=81002)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagEnabled(Label.L9, flag=9431)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(1801)
def Event_1801():
    """Event 1801"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2001):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9430))
    AND_1.Add(FlagEnabled(9430))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9421)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=1, face_param_id=80000)


@ContinueOnRest(6901)
def Event_6901():
    """Event 6901"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    AND_1.Add(FlagDisabled(68000))
    AND_1.Add(FlagDisabled(68020))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(68000))
    AND_2.Add(FlagDisabled(68020))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    RemoveGoodFromPlayer(item=9402, quantity=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9400, flag=68000, bit_count=1)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(FlagDisabled(68000))
    AND_3.Add(FlagEnabled(68020))
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_4.Add(FlagEnabled(68000))
    AND_4.Add(FlagEnabled(68020))
    GotoIfConditionFalse(Label.L4, input_condition=AND_4)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9400, flag=68000, bit_count=1)
    Goto(Label.L0)

    # --- Label 4 --- #
    DefineLabel(4)

    # --- Label 0 --- #
    DefineLabel(0)
    ClearMainCondition()
    if FlagEnabled(66040):
        EnableFlag(66000)
        DisableFlag(66040)
    if FlagEnabled(66080):
        EnableFlag(66130)
        DisableFlag(66080)
    AND_5.Add(FlagEnabled(10019200))
    AND_5.Add(FlagEnabled(66150))
    AND_5.Add(FlagEnabled(66181))
    SkipLinesIfConditionFalse(4, AND_5)
    EnableFlag(66150)
    EnableFlag(66170)
    EnableFlag(66180)
    SkipLines(1)
    DisableFlag(66180)
    DisableFlag(66100)
    DisableFlag(66101)
    DisableFlag(66102)
    DisableFlag(66130)
    DisableFlag(66131)
    DisableFlag(66160)
    DisableFlag(66161)
    DisableFlag(66181)
    DisableFlag(66200)
    if FlagEnabled(66420):
        DisableFlag(66400)
        EnableFlag(66410)
        DisableFlag(66420)
    else:
        DisableFlag(66400)
        DisableFlag(66410)
        DisableFlag(66420)
    DisableFlag(66470)
    DisableFlag(66471)
    DisableFlag(66480)
    if FlagEnabled(66710):
        EnableFlag(66760)
        DisableFlag(66710)
    DisableFlag(66730)
    DisableFlag(66731)
    DisableFlag(66750)
    DisableFlag(66751)
    DisableFlag(66780)
    DisableFlag(66781)
    DisableFlag(66104)
    DisableFlag(66202)
    DisableFlag(66204)
    DisableFlag(66300)
    DisableFlag(66302)
    DisableFlag(66304)
    DisableFlag(66402)
    DisableFlag(66404)
    DisableFlag(66502)
    DisableFlag(66510)
    ClearMainCondition()
    DisableFlag(11000389)
    DisableFlag(15000392)
    DisableFlag(15000393)
    DisableFlag(15001270)
    DisableFlag(15001280)
    DisableFlag(1043370340)
    DisableFlag(1044320342)
    DisableFlag(1044327410)
    DisableFlag(1036480340)
    DisableFlag(1036487400)
    DisableFlag(1036480340)
    DisableFlag(1039510451)
    DisableFlag(1049370290)
    DisableFlag(1052410290)
    DisableFlag(1048510300)
    DisableFlag(1248550380)
    DisableFlag(1248550381)
    DisableFlag(1042380340)
    DisableFlag(1044320340)
    DisableFlag(1037420340)
    DisableFlag(1036450340)
    DisableFlag(1044530300)
    DisableFlag(1049370292)
    DisableFlag(1048570320)
    DisableFlag(1043520506)
    DisableFlag(1043520505)
    DisableFlag(1043527500)
    DisableFlag(1038540400)
    DisableFlag(1038547100)
    DisableFlag(1042510300)
    DisableFlag(11000393)
    DisableFlag(13000490)
    DisableFlag(13000495)
    DisableFlag(12020431)
    DisableFlag(10000289)
    DisableFlag(1049370299)
    DisableFlag(1051360291)
    DisableFlag(1051360292)
    DisableFlag(1051570310)
    DisableFlag(1051570311)
    DisableFlag(12010240)
    DisableFlag(12030240)
    DisableFlag(12030241)
    DisableFlag(12030256)
    DisableFlag(12030257)
    DisableFlag(12030297)
    DisableFlag(12030201)
    DisableFlag(1051360290)
    DisableFlag(530140)
    ClearMainCondition()
    if FlagEnabled(82135):
        EnableFlag(62135)
        DisableFlag(82135)
    if FlagEnabled(82137):
        EnableFlag(62137)
        DisableFlag(82137)
    if FlagEnabled(82138):
        EnableFlag(62138)
        DisableFlag(82138)
    if FlagEnabled(95600):
        EnableFlag(78600)
        DisableFlag(95600)
    DisableFlag(82195)
    DisableFlag(82196)
    DisableFlag(82197)
    DisableFlag(82198)
    ClearMainCondition()
    AND_15.Add(FlagDisabled(15000800))
    AND_15.Add(CharacterInsideRegion(character=PLAYER, region=15002845))
    SkipLinesIfConditionFalse(1, AND_15)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=15002950,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    ClearMainCondition()
    if FlagDisabled(11109213):
        EnableFlag(10007452)
    else:
        EnableFlag(10007450)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6902)
def Event_6902():
    """Event 6902"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(6902))
    
    MAIN.Await(AND_1)
    
    EnableFlag(66000)
    EnableFlag(66010)
    EnableFlag(66020)
    EnableFlag(66030)
    EnableFlag(66031)
    EnableFlag(66060)
    EnableFlag(66070)
    EnableFlag(66080)
    EnableFlag(66090)
    EnableFlag(66100)
    EnableFlag(66110)
    EnableFlag(66120)
    EnableFlag(66130)
    EnableFlag(66140)
    EnableFlag(66150)
    EnableFlag(66160)
    EnableFlag(66170)
    EnableFlag(66180)
    EnableFlag(66190)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6903)
def Event_6903():
    """Event 6903"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(6903))
    
    MAIN.Await(AND_1)
    
    EnableFlag(66400)
    EnableFlag(66410)
    EnableFlag(66420)
    EnableFlag(66430)
    EnableFlag(66440)
    EnableFlag(66450)
    EnableFlag(66460)
    EnableFlag(66470)
    EnableFlag(66480)
    EnableFlag(66490)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6904)
def Event_6904():
    """Event 6904"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(6904))
    
    MAIN.Await(AND_1)
    
    EnableFlag(66700)
    EnableFlag(66710)
    EnableFlag(66720)
    EnableFlag(66730)
    EnableFlag(66740)
    EnableFlag(66750)
    EnableFlag(66760)
    EnableFlag(66770)
    EnableFlag(66780)
    EnableFlag(66790)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6905)
def Event_6905():
    """Event 6905"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    if FlagEnabled(510010):
        EnableFlag(171)
    if FlagEnabled(510300):
        EnableFlag(172)
    if FlagEnabled(510040):
        EnableFlag(173)
    if FlagEnabled(510220):
        EnableFlag(174)
    if FlagEnabled(510120):
        EnableFlag(175)
    if FlagEnabled(510200):
        EnableFlag(176)
    if FlagEnabled(197):
        EnableFlag(177)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6906)
def Event_6906():
    """Event 6906"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    if FlagEnabled(69390):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9141, flag=69390, bit_count=1)
    if FlagEnabled(520040):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=202000, flag=520040, bit_count=1)
    SkipLinesIfFlagDisabled(4, 1039418600)
    EnableFlag(1039418540)
    EndOfAnimation(asset=1039411540, animation_id=2)
    DisableAssetActivation(1039411540, obj_act_id=-1)
    SkipLines(4)
    if FlagEnabled(73006):
        EnableFlag(1039418540)
        EndOfAnimation(asset=1039411540, animation_id=2)
        DisableAssetActivation(1039411540, obj_act_id=-1)
    SkipLinesIfFlagDisabled(4, 1047408600)
    EnableFlag(1047408540)
    EndOfAnimation(asset=1047401540, animation_id=2)
    DisableAssetActivation(1047401540, obj_act_id=-1)
    SkipLines(4)
    if FlagEnabled(73014):
        EnableFlag(1047408540)
        EndOfAnimation(asset=1047401540, animation_id=2)
        DisableAssetActivation(1047401540, obj_act_id=-1)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6907)
def Event_6907():
    """Event 6907"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    if FlagEnabled(102):
        EnableFlag(71801)
    SkipLinesIfFlagDisabled(4, 1050558600)
    EnableFlag(1050558540)
    EndOfAnimation(asset=1050551540, animation_id=2)
    DisableAssetActivation(1050551540, obj_act_id=-1)
    SkipLines(4)
    if FlagEnabled(73019):
        EnableFlag(1050558540)
        EndOfAnimation(asset=1050551540, animation_id=2)
        DisableAssetActivation(1050551540, obj_act_id=-1)
    SkipLinesIfFlagDisabled(4, 1039488600)
    EnableFlag(1039488540)
    EndOfAnimation(asset=1039481540, animation_id=2)
    DisableAssetActivation(1039481540, obj_act_id=-1)
    SkipLines(4)
    if FlagEnabled(73005):
        EnableFlag(1039488540)
        EndOfAnimation(asset=1039481540, animation_id=2)
        DisableAssetActivation(1039481540, obj_act_id=-1)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(6908)
def Event_6908():
    """Event 6908"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfPlayerNotInOwnWorld(Label.L15)
    if FlagEnabled(73207):
        EnableFlag(73257)
    DisableThisSlotFlag()
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@RestartOnRest(9300)
def Event_9300(_, achievement_id: int, flag: uint, seconds: float):
    """Event 9300"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    AwardAchievement(achievement_id=achievement_id)


@RestartOnRest(9360)
def Event_9360(_, activity_id: int, flag: uint, seconds: float):
    """Event 9360"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    StartPS5Activity(activity_id=activity_id)


@RestartOnRest(9375)
def Event_9375(_, activity_id: int, flag: uint, seconds: float):
    """Event 9375"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    EndPS5Activity(activity_id=activity_id)


@RestartOnRest(9390)
def Event_9390(_, flag: uint, right: uint, right_1: uint, right_2: uint, right_3: uint, right_4: uint):
    """Event 9390"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfUnsignedEqual(2, left=0, right=right)
    SkipLinesIfFlagEnabled(1, right)
    OR_2.Add(FlagEnabled(right))
    SkipLinesIfUnsignedEqual(2, left=0, right=right_1)
    SkipLinesIfFlagEnabled(1, right_1)
    OR_2.Add(FlagEnabled(right_1))
    SkipLinesIfUnsignedEqual(2, left=0, right=right_2)
    SkipLinesIfFlagEnabled(1, right_2)
    OR_2.Add(FlagEnabled(right_2))
    SkipLinesIfUnsignedEqual(2, left=0, right=right_3)
    SkipLinesIfFlagEnabled(1, right_3)
    OR_2.Add(FlagEnabled(right_3))
    SkipLinesIfUnsignedEqual(2, left=0, right=right_4)
    SkipLinesIfFlagEnabled(1, right_4)
    OR_2.Add(FlagEnabled(right_4))
    
    MAIN.Await(OR_2)
    
    DisableThisSlotFlag()


@RestartOnRest(9820)
def Event_9820(_, right: uint, item_lot_param_id: int, special_effect: int):
    """Event 9820"""
    DisableNetworkSync()
    if UnsignedNotEqual(left=0, right=right):
        if FlagEnabled(right):
            return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    
    MAIN.Await(AND_1)
    
    EnableFlag(right)
    AwardItemLot(item_lot_param_id, host_only=True)
    Wait(1.2000000476837158)
    Restart()


@ContinueOnRest(65810)
def Event_65810(_, flag: uint, flag_1: uint, right: uint, right_1: uint, right_2: uint, right_3: uint):
    """Event 65810"""
    GotoIfPlayerNotInOwnWorld(Label.L15)
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(FlagEnabled(flag_1))
    if UnsignedNotEqual(left=0, right=right):
        OR_1.Add(FlagEnabled(right))
    if UnsignedNotEqual(left=0, right=right_1):
        OR_1.Add(FlagEnabled(right_1))
    if UnsignedNotEqual(left=0, right=right_2):
        OR_1.Add(FlagEnabled(right_2))
    if UnsignedNotEqual(left=0, right=right_3):
        OR_1.Add(FlagEnabled(right_3))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    if FlagDisabled(65800):
        EnableFlag(65800)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    Wait(1.0)


@ContinueOnRest(1910)
def Event_1910(_, npc_threat_level: uint, flag: uint):
    """Event 1910"""
    MAIN.Await(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    
    EnableFlag(flag)
    
    MAIN.Await(FieldBattleMusicDisabled(npc_threat_level=npc_threat_level))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(9910)
def Event_9910(_, flag: uint):
    """Event 9910"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    DisableFlagRange((1042330101, 1042330102))
    DisableFlagRange((1043330101, 1043330101))
    DisableFlagRange((1044330101, 1044330101))
    DisableFlagRange((1045330101, 1045330102))
    DisableFlagRange((1042320101, 1042320102))
    DisableFlagRange((1043320101, 1043320101))
    DisableFlagRange((1044320101, 1044320101))
    DisableFlagRange((1043360101, 1043360102))
    DisableFlagRange((1042370101, 1042370101))
    DisableFlagRange((1043370101, 1043370101))
    DisableFlagRange((1044370101, 1044370102))
    DisableFlagRange((1042390101, 1042390103))
    DisableFlagRange((1042350101, 1042350102))
    DisableFlagRange((1040370101, 1040370101))
    DisableFlagRange((1045350101, 1045350101))
    DisableFlagRange((1040370111, 1040370111))
    DisableFlagRange((1044370111, 1044370112))
    DisableFlagRange((1043390101, 1043390102))
    Restart()


@ContinueOnRest(3040)
def Event_3040():
    """Event 3040"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9413):
        return
    GotoIfFlagEnabled(Label.L2, flag=9412)
    GotoIfFlagDisabled(Label.L20, flag=9411)
    GotoIfFlagEnabled(Label.L20, flag=9130)
    GotoIfCharacterInsideRegion(Label.L20, character=PLAYER, region=1051362220)
    DisableNetworkFlag(9411)
    UnfreezeTime()
    DisableNetworkFlag(1051362702)
    EnableFlag(3618)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L1, flag=9411)
    GotoIfFlagEnabled(Label.L0, flag=9410)
    OR_1.Add(FlagEnabled(1044369223))
    OR_1.Add(FlagEnabled(1034499224))
    OR_1.Add(FlagEnabled(3063))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    EnableNetworkFlag(9410)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(1051362702))
    
    MAIN.Await(AND_2)
    
    GotoIfPlayerNotInOwnWorld(Label.L1)
    EnableNetworkFlag(9411)
    EnableFlag(3618)

    # --- Label 1 --- #
    DefineLabel(1)
    FreezeTime()
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(310))
    
    MAIN.Await(AND_3)
    
    UnfreezeTime()
    GotoIfPlayerNotInOwnWorld(Label.L2)
    EnableNetworkFlag(9411)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(9130))
    AND_4.Add(FlagDisabled(1051369360))
    AND_4.Add(PlayerInOwnWorld())
    AND_5.Add(CharacterInsideRegion(character=PLAYER, region=1051362220))
    OR_4.Add(AND_4)
    OR_4.Add(AND_5)
    
    MAIN.Await(OR_4)
    
    EndIfFinishedConditionTrue(input_condition=AND_5)
    EnableNetworkFlag(9413)


@RestartOnRest(3041)
def Event_3041():
    """Event 3041"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(9000):
        return
    if FlagDisabled(11109657):
        return
    if FlagEnabled(3002):
        return
    EnableFlag(9001)
    WaitFrames(frames=1)
    PlayCutscene(15000020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(9001)
    EnableFlag(3002)


@RestartOnRest(3042)
def Event_3042():
    """Event 3042"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAllDisabled(2, (76100, 76199))
    EnableFlag(3061)
    End()
    DisableFlag(3061)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(76100, 76199)))
    
    EnableFlag(3061)
    End()


@RestartOnRest(3043)
def Event_3043():
    """Event 3043"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAllDisabled(2, (76200, 76299))
    EnableFlag(3062)
    End()
    DisableFlag(3062)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(76200, 76299)))
    
    EnableFlag(3062)
    End()


@RestartOnRest(3044)
def Event_3044():
    """Event 3044"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAllDisabled(2, (76300, 76399))
    EnableFlag(3063)
    End()
    DisableFlag(3063)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(76300, 76399)))
    
    EnableFlag(3063)
    End()


@RestartOnRest(3045)
def Event_3045():
    """Event 3045"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAllDisabled(2, (76400, 76499))
    EnableFlag(3064)
    End()
    DisableFlag(3064)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(76400, 76499)))
    
    EnableFlag(3064)
    End()


@RestartOnRest(3046)
def Event_3046():
    """Event 3046"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAllDisabled(2, (76500, 76599))
    EnableFlag(3065)
    End()
    DisableFlag(3065)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(76500, 76599)))
    
    EnableFlag(3065)
    End()


@RestartOnRest(3049)
def Event_3049():
    """Event 3049"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3740, 3748)))
    AND_1.Add(FlagEnabled(3741))
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(3765, 3767)))
    AND_2.Add(FlagEnabled(3761))
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(3565, 3568)))
    AND_3.Add(FlagEnabled(3561))
    OR_2.Add(FlagEnabled(3601))
    OR_2.Add(FlagEnabled(3603))
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(3605, 3616)))
    AND_4.Add(OR_2)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    EnableFlag(1034509403)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    EnableFlag(1034499202)
    EnableFlag(1034499204)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_3)
    EnableFlag(1034509302)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_4)
    EnableFlag(1045379209)
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(3740, 3748)))
    AND_5.Add(FlagEnabled(3740))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3740, 3743))
    EnableNetworkFlag(3741)
    AND_6.Add(FlagRangeAnyEnabled(flag_range=(3765, 3767)))
    AND_6.Add(FlagEnabled(3760))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3760, 3763))
    EnableNetworkFlag(3761)
    AND_7.Add(FlagRangeAnyEnabled(flag_range=(3565, 3568)))
    AND_7.Add(FlagEnabled(3560))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3560, 3563))
    EnableNetworkFlag(3561)
    AND_8.Add(FlagRangeAnyEnabled(flag_range=(3605, 3616)))
    AND_8.Add(FlagEnabled(3600))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(3600, 3603))
    EnableNetworkFlag(3601)
    AND_9.Add(FlagRangeAnyEnabled(flag_range=(3740, 3748)))
    AND_9.Add(FlagEnabled(3741))
    AND_10.Add(FlagRangeAnyEnabled(flag_range=(3765, 3767)))
    AND_10.Add(FlagEnabled(3761))
    AND_10.Add(FlagRangeAnyEnabled(flag_range=(3565, 3568)))
    AND_10.Add(FlagEnabled(3561))
    OR_4.Add(FlagEnabled(3601))
    OR_4.Add(FlagEnabled(3603))
    AND_11.Add(FlagRangeAnyEnabled(flag_range=(3605, 3616)))
    AND_11.Add(OR_4)
    OR_3.Add(AND_9)
    OR_3.Add(AND_10)
    OR_3.Add(AND_11)
    OR_3.Add(AND_12)
    
    MAIN.Await(not OR_3)
    
    Restart()


@RestartOnRest(3050)
def Event_3050():
    """Event 3050"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400159):
        return
    AND_1.Add(FlagEnabled(12019280))
    AND_1.Add(FlagDisabled(12012716))
    
    MAIN.Await(AND_1)
    
    RemoveGoodFromPlayer(item=8146, quantity=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8187, flag=12019280, bit_count=1)
    AwardItemLot(101590, host_only=False)
    End()


@RestartOnRest(3051)
def Event_3051():
    """Event 3051"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400033):
        return
    if FlagEnabled(3383):
        return
    AND_1.Add(FlagEnabled(400031))
    AND_1.Add(FlagEnabled(3383))
    AND_1.Add(FlagDisabled(35009209))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(400033):
        return
    RemoveGoodFromPlayer(item=8154, quantity=1)
    AwardItemLot(100330, host_only=False)
    End()


@RestartOnRest(3052)
def Event_3052():
    """Event 3052"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400410):
        return
    if FlagEnabled(4103):
        return
    AND_1.Add(FlagEnabled(1036419209))
    AND_1.Add(FlagDisabled(1036412703))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(104100, host_only=False)
    End()


@RestartOnRest(3053)
def Event_3053():
    """Event 3053"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(60818):
        return
    if FlagEnabled(3683):
        return
    OR_1.Add(FlagEnabled(31009218))
    OR_1.Add(FlagEnabled(1038419267))
    OR_1.Add(FlagEnabled(1037549213))
    
    MAIN.Await(OR_1)
    
    EnableFlag(60818)
    AwardGesture(gesture_param_id=40)
    End()


@RestartOnRest(3054)
def Event_3054():
    """Event 3054"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(60830):
        return
    AND_1.Add(FlagEnabled(4703))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(60830):
        return
    EnableFlag(60830)
    AwardGesture(gesture_param_id=73)
    End()


@RestartOnRest(3055)
def Event_3055():
    """Event 3055"""
    DisableNetworkSync()
    GotoIfCharacterHasSpecialEffect(Label.L0, character=PLAYER, special_effect=503360)
    
    MAIN.Await(PlayerHasGood(3360))
    
    AddSpecialEffect(PLAYER, 503360)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerDoesNotHaveGood(3360))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 503355))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 503356))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 503359)
    Restart()


@RestartOnRest(3056)
def Event_3056():
    """Event 3056"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(1051587800))
    OR_1.Add(FlagEnabled(400130))
    OR_2.Add(FlagEnabled(110))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagDisabled(1035429213):
        EnableFlag(1035429211)
        EnableFlag(1035429213)
    
    MAIN.Await(FlagEnabled(110))

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(1035429211)
    End()


@RestartOnRest(3058)
def Event_3058():
    """Event 3058"""
    if PlayerInOwnWorld():
        return
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(20000, 9721))
    
    EnableFlag(7700)


@RestartOnRest(3059)
def Event_3059():
    """Event 3059"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(7700))
    
    DisableFlag(7700)
    GotoIfFlagEnabled(Label.L0, flag=1035449235)
    GotoIfFlagDisabled(Label.L0, flag=1035449207)
    IncrementEventValue(1035449230, bit_count=3, max_value=5)
    AND_1.Add(EventValue(flag=1035449230, bit_count=5) >= 3)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    EnableFlag(1035449235)
    EnableFlag(3198)

    # --- Label 0 --- #
    DefineLabel(0)
    SaveRequest()
    End()


@RestartOnRest(3080)
def Event_3080():
    """Event 3080"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9433):
        return
    
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(290500, 290999)) >= 4)
    
    EnableFlag(9433)
    End()


@RestartOnRest(3081)
def Event_3081(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, flag_4: uint, flag_5: uint, flag_6: uint):
    """Event 3081"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    AND_1.Add(FlagEnabled(3425))
    OR_1.Add(FlagEnabled(1037429207))
    OR_1.Add(FlagEnabled(1037429209))
    OR_1.Add(FlagEnabled(1037429205))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(3426))
    OR_2.Add(FlagEnabled(1038519205))
    OR_2.Add(FlagEnabled(1038519206))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1038519207))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_1)
    AND_3.Add(FlagEnabled(3426))
    OR_3.Add(FlagEnabled(1038519205))
    OR_3.Add(FlagEnabled(1038519206))
    AND_3.Add(OR_3)
    AND_3.Add(FlagEnabled(1038509205))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_2)
    AND_4.Add(FlagEnabled(3427))
    AND_4.Add(FlagEnabled(16009305))
    AND_4.Add(FlagDisabled(16009306))
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag_3)
    AND_5.Add(FlagEnabled(3427))
    AND_5.Add(FlagEnabled(16009305))
    AND_5.Add(FlagEnabled(16009306))
    SkipLinesIfConditionFalse(1, AND_5)
    EnableFlag(flag_4)
    AND_6.Add(FlagEnabled(3428))
    SkipLinesIfConditionFalse(1, AND_6)
    EnableFlag(flag_4)
    AND_7.Add(FlagEnabled(3430))
    AND_7.Add(FlagEnabled(16009335))
    SkipLinesIfConditionFalse(1, AND_7)
    EnableFlag(flag_4)
    AND_8.Add(FlagEnabled(3431))
    AND_8.Add(FlagEnabled(16009335))
    SkipLinesIfConditionFalse(1, AND_8)
    EnableFlag(flag_4)
    AND_9.Add(FlagEnabled(3429))
    OR_9.Add(FlagEnabled(16009326))
    OR_9.Add(FlagEnabled(16009327))
    AND_9.Add(OR_9)
    SkipLinesIfConditionFalse(1, AND_9)
    EnableFlag(flag_5)
    AND_10.Add(FlagEnabled(3431))
    AND_10.Add(FlagDisabled(16009327))
    AND_10.Add(FlagEnabled(16009328))
    SkipLinesIfConditionFalse(1, AND_10)
    EnableFlag(flag_5)
    AND_11.Add(FlagEnabled(3431))
    AND_11.Add(FlagDisabled(16009319))
    SkipLinesIfConditionFalse(1, AND_11)
    EnableFlag(flag_6)
    AND_12.Add(FlagEnabled(3431))
    AND_12.Add(FlagEnabled(400091))
    SkipLinesIfConditionFalse(1, AND_12)
    EnableFlag(flag_6)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3425))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1037429205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1037429207))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1037429209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3426))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038519205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038519206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038519207))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038509205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3427))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009305))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009306))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3428))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3430))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009335))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3431))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009335))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3429))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009326))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009327))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009328))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009319))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400091))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3082)
def Event_3082(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 3082"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    OR_1.Add(FlagEnabled(3185))
    OR_1.Add(FlagEnabled(3187))
    OR_1.Add(FlagEnabled(3191))
    OR_2.Add(FlagEnabled(1042369206))
    OR_2.Add(FlagEnabled(1042369225))
    OR_2.Add(FlagEnabled(1042369226))
    OR_2.Add(FlagEnabled(1042369235))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_4.Add(FlagEnabled(3188))
    OR_4.Add(FlagEnabled(1035449205))
    OR_4.Add(FlagEnabled(1035449206))
    AND_4.Add(OR_4)
    OR_5.Add(AND_4)
    OR_5.Add(FlagEnabled(3189))
    OR_5.Add(FlagEnabled(3190))
    SkipLinesIfConditionFalse(1, OR_5)
    EnableFlag(flag_1)
    OR_6.Add(FlagEnabled(3183))
    OR_6.Add(FlagEnabled(12059166))
    OR_6.Add(AND_6)
    AND_6.Add(FlagEnabled(400036))
    AND_6.Add(FlagEnabled(400037))
    SkipLinesIfConditionFalse(1, AND_6)
    EnableFlag(flag_2)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3185))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1042369206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3187))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1042369225))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1042369226))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3191))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1042369235))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3188))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1035449205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1035449206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3189))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3190))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3183))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 12059166))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400036))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400037))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3083)
def Event_3083(_, flag: uint, flag_1: uint):
    """Event 3083"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(3105))
    OR_1.Add(FlagEnabled(16009208))
    OR_1.Add(FlagEnabled(16009206))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(3106))
    OR_2.Add(FlagEnabled(3107))
    OR_2.Add(FlagEnabled(3108))
    SkipLinesIfConditionFalse(1, OR_2)
    EnableFlag(flag)
    OR_4.Add(FlagEnabled(3109))
    OR_4.Add(FlagEnabled(3110))
    OR_4.Add(FlagEnabled(3111))
    OR_5.Add(FlagEnabled(16009255))
    OR_5.Add(FlagEnabled(16009256))
    OR_5.Add(FlagEnabled(16009258))
    AND_4.Add(OR_4)
    AND_4.Add(OR_5)
    AND_6.Add(FlagDisabled(16009208))
    AND_6.Add(FlagEnabled(71600))
    AND_6.Add(FlagEnabled(3109))
    OR_6.Add(AND_4)
    OR_6.Add(AND_6)
    SkipLinesIfConditionFalse(1, OR_6)
    EnableFlag(flag_1)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3105))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009208))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3106))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3107))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3108))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3109))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3110))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3111))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009255))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009256))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009258))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009208))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 71600))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3084)
def Event_3084(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 3084"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    AND_1.Add(FlagEnabled(4105))
    OR_1.Add(FlagEnabled(1036419205))
    OR_1.Add(FlagEnabled(1036419206))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    OR_2.Add(FlagEnabled(1036419209))
    AND_2.Add(FlagEnabled(4103))
    AND_2.Add(FlagEnabled(400412))
    OR_3.Add(OR_2)
    OR_3.Add(AND_2)
    SkipLinesIfConditionFalse(1, OR_3)
    EnableFlag(flag_1)
    AND_4.Add(FlagEnabled(4106))
    OR_4.Add(FlagEnabled(1047589206))
    OR_4.Add(FlagEnabled(1047582700))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag_2)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4105))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1036419205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1036419206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1036419209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4103))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400412))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4106))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1047589206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1047582700))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3085)
def Event_3085(_, flag: uint, flag_1: uint):
    """Event 3085"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    OR_1.Add(FlagEnabled(3688))
    OR_1.Add(FlagEnabled(3693))
    OR_2.Add(FlagEnabled(1037549206))
    OR_2.Add(FlagEnabled(1037549207))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_3.Add(FlagEnabled(400181))
    AND_3.Add(FlagEnabled(400189))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_1)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3688))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3693))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1037549206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1037549207))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400181))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400189))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3086)
def Event_3086(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 3086"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    OR_1.Add(FlagEnabled(3625))
    AND_1.Add(FlagEnabled(3631))
    AND_1.Add(FlagEnabled(1044389209))
    OR_1.Add(AND_1)
    AND_2.Add(FlagEnabled(1044389206))
    AND_2.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    OR_3.Add(FlagEnabled(3626))
    AND_3.Add(FlagEnabled(3631))
    AND_3.Add(FlagEnabled(1043359259))
    OR_3.Add(AND_3)
    OR_4.Add(FlagEnabled(1043359255))
    OR_4.Add(FlagEnabled(1043359256))
    OR_4.Add(FlagEnabled(1043359257))
    AND_4.Add(OR_3)
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag_1)
    OR_5.Add(FlagEnabled(3627))
    AND_5.Add(FlagEnabled(3631))
    AND_5.Add(FlagEnabled(1035469209))
    OR_5.Add(AND_5)
    AND_6.Add(FlagEnabled(1035469208))
    AND_6.Add(OR_5)
    SkipLinesIfConditionFalse(1, AND_6)
    EnableFlag(flag_2)
    OR_7.Add(FlagEnabled(3630))
    AND_7.Add(FlagEnabled(3631))
    AND_7.Add(FlagEnabled(1039529209))
    OR_7.Add(AND_7)
    AND_8.Add(FlagEnabled(1039529205))
    AND_8.Add(OR_7)
    SkipLinesIfConditionFalse(1, AND_8)
    EnableFlag(flag_3)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3625))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3631))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1044389209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1044389206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3626))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1043359259))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1043359255))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1043359256))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1043359257))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3627))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1035469209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1035469208))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3630))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039529209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039529205))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3087)
def Event_3087(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 3087"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    AND_1.Add(FlagEnabled(3885))
    OR_2.Add(FlagEnabled(1042389255))
    OR_2.Add(FlagEnabled(1042389256))
    AND_1.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_3.Add(FlagEnabled(400293))
    AND_3.Add(FlagEnabled(400294))
    AND_3.Add(FlagEnabled(400299))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_1)
    AND_4.Add(FlagEnabled(3886))
    OR_4.Add(FlagEnabled(16009455))
    OR_4.Add(FlagEnabled(16009456))
    OR_4.Add(FlagEnabled(16009460))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag_2)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3885))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1042389255))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1042389256))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400293))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400294))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400299))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3886))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009455))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009456))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009460))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3088)
def Event_3088(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 3088"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    AND_1.Add(FlagEnabled(4145))
    OR_2.Add(FlagEnabled(1036439205))
    OR_2.Add(FlagEnabled(1036439206))
    AND_1.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_3.Add(FlagEnabled(400300))
    AND_3.Add(FlagEnabled(400309))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_1)
    OR_4.Add(FlagEnabled(4146))
    OR_4.Add(FlagEnabled(4147))
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(1044529256))
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag_2)
    AND_5.Add(FlagEnabled(400308))
    AND_5.Add(FlagEnabled(400309))
    SkipLinesIfConditionFalse(1, AND_5)
    EnableFlag(flag_3)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4145))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1036439205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1036439206))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400300))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400309))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4146))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4147))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1044529256))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400308))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3089)
def Event_3089():
    """Event 3089"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(34149201):
        return
    OR_1.Add(FlagEnabled(62528))
    OR_1.Add(FlagEnabled(34149200))
    
    MAIN.Await(OR_1)
    
    EnableFlag(34149201)
    End()


@RestartOnRest(3090)
def Event_3090(_, flag: uint, flag_1: uint):
    """Event 3090"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(62022))
    AND_1.Add(FlagEnabled(3409))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(62031))
    AND_2.Add(FlagEnabled(118))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_1)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 62022))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3409))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 62031))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 118))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3091)
def Event_3091(_, flag: uint):
    """Event 3091"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(1051369358))
    AND_1.Add(FlagEnabled(9410))
    AND_1.Add(FlagDisabled(9412))
    AND_1.Add(FlagEnabled(3747))
    OR_1.Add(FlagEnabled(1034509405))
    OR_1.Add(FlagEnabled(1034509431))
    AND_2.Add(not AND_1)
    AND_2.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1051369358))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9410))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9412))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3747))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034509405))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034509431))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3092)
def Event_3092(_, flag: uint):
    """Event 3092"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(1034499205))
    OR_1.Add(FlagEnabled(1034499238))
    OR_1.Add(FlagEnabled(1034499233))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034499205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034499238))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034499233))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3093)
def Event_3093(_, flag: uint):
    """Event 3093"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(1034509310))
    OR_1.Add(FlagEnabled(1034509312))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034509310))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1034509312))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3094)
def Event_3094(_, flag: uint):
    """Event 3094"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(12039155))
    OR_1.Add(FlagEnabled(12039156))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 12039155))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 12039156))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3095)
def Event_3095(_, flag: uint):
    """Event 3095"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(1045399205))
    OR_1.Add(FlagEnabled(1045399206))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1045399205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1045399206))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3096)
def Event_3096(_, flag: uint, flag_1: uint):
    """Event 3096"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_1)
    OR_1.Add(FlagEnabled(1038439205))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_2.Add(FlagEnabled(35009205))
    OR_2.Add(FlagEnabled(35009206))
    SkipLinesIfConditionFalse(1, OR_2)
    EnableFlag(flag_1)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038439205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 35009205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 35009206))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(3097)
def Event_3097(_, flag: uint):
    """Event 3097"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(1051369227))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1051369227))
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(3098)
def Event_3098():
    """Event 3098"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1051369204))
    if AND_1:
        return
    
    MAIN.Await(FlagEnabled(3367))
    
    if FlagDisabled(9118):
        OR_1.Add(FlagEnabled(9118))
    if FlagDisabled(9101):
        OR_1.Add(FlagEnabled(9101))
    if FlagDisabled(9104):
        OR_1.Add(FlagEnabled(9104))
    if FlagDisabled(9122):
        OR_1.Add(FlagEnabled(9122))
    if FlagDisabled(9120):
        OR_1.Add(FlagEnabled(9120))
    if FlagDisabled(9112):
        OR_1.Add(FlagEnabled(9112))
    OR_1.Add(FlagEnabled(6000))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(1051369204)
    EnableFlag(3378)
    End()


@RestartOnRest(3099)
def Event_3099():
    """Event 3099"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(11109304))
    if AND_1:
        return
    AwaitFlagEnabled(flag=11109806)
    GotoIfFlagEnabled(Label.L1, flag=11109303)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(9130):
        EnableNetworkFlag(11109309)
    if FlagEnabled(9101):
        EnableNetworkFlag(11109310)
    if FlagEnabled(9104):
        EnableNetworkFlag(11109311)
    if FlagEnabled(9122):
        EnableNetworkFlag(11109312)
    if FlagEnabled(9120):
        EnableNetworkFlag(11109313)
    if FlagEnabled(9112):
        EnableNetworkFlag(11109314)
    EnableNetworkFlag(11109303)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(11109309):
        OR_1.Add(FlagEnabled(9130))
    if FlagDisabled(11109310):
        OR_1.Add(FlagEnabled(9101))
    if FlagDisabled(11109311):
        OR_1.Add(FlagEnabled(9104))
    if FlagDisabled(11109312):
        OR_1.Add(FlagEnabled(9122))
    if FlagDisabled(11109313):
        OR_1.Add(FlagEnabled(9120))
    if FlagDisabled(11109314):
        OR_1.Add(FlagEnabled(9112))
    AND_5.Add(FlagEnabled(11109309))
    AND_5.Add(FlagEnabled(11109310))
    AND_5.Add(FlagEnabled(11109311))
    AND_5.Add(FlagEnabled(11109312))
    AND_5.Add(FlagEnabled(11109313))
    AND_5.Add(FlagEnabled(11109314))
    OR_1.Add(AND_5)
    OR_1.Add(FlagEnabled(6000))
    AwaitConditionTrue(OR_1)
    EnableNetworkFlag(11109304)
    End()


@RestartOnRest(4600)
def Event_4600(_, flag: uint, flag_1: uint):
    """Event 4600"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3265, 3268)))
    OR_1.Add(FlagEnabled(10009351))
    OR_1.Add(FlagEnabled(10009353))
    OR_1.Add(FlagEnabled(10009397))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    OR_2.Add(FlagEnabled(10009399))
    OR_2.Add(FlagEnabled(10002768))
    SkipLinesIfConditionFalse(1, OR_2)
    EnableFlag(flag_1)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3265))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3266))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3267))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3268))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 10009351))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 10009353))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 10009397))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 10009399))
    AND_15.Add(FlagEnabled(10002768))
    AND_15.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_15)
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4601)
def Event_4601(_, flag: uint):
    """Event 4601"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(14009205))
    OR_1.Add(FlagEnabled(14002705))
    OR_1.Add(FlagEnabled(14002706))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagEnabled(14009205))
    OR_14.Add(FlagEnabled(14002705))
    OR_14.Add(FlagEnabled(14002706))
    AND_14.Add(OR_14)
    AND_14.Add(FlagDisabled(flag))
    OR_15.Add(AND_14)
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4602)
def Event_4602(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 4602"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagEnabled(1, 16002731)
    SkipLinesIfFlagRangeAnyEnabled(1, (3448, 3449))
    DisableFlag(flag_1)
    OR_1.Add(FlagEnabled(1037449205))
    OR_1.Add(FlagEnabled(1037442700))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(3448, 3449)))
    AND_2.Add(FlagDisabled(16002731))
    OR_2.Add(FlagEnabled(16009405))
    OR_2.Add(FlagEnabled(16009415))
    OR_2.Add(FlagEnabled(16009416))
    AND_2.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_1)
    OR_3.Add(FlagEnabled(1039449305))
    OR_3.Add(FlagEnabled(1039442721))
    SkipLinesIfConditionFalse(1, OR_3)
    EnableFlag(flag_2)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1037449205))
    AND_13.Add(FlagEnabled(1037442700))
    AND_13.Add(FlagDisabled(flag))
    OR_15.Add(AND_13)
    OR_15.Add(FlagEnabled(3448))
    OR_15.Add(FlagEnabled(3449))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009405))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16009415))
    AND_14.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 16002731))
    AND_14.Add(FlagEnabled(16009416))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039449305))
    AND_15.Add(FlagEnabled(1039442721))
    AND_15.Add(FlagDisabled(flag_2))
    OR_15.Add(AND_15)
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4603)
def Event_4603(_, flag: uint):
    """Event 4603"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(35009306))
    OR_1.Add(FlagEnabled(35009307))
    OR_1.Add(FlagEnabled(35002724))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 35009306))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 35009307))
    AND_15.Add(FlagEnabled(35002724))
    AND_15.Add(FlagDisabled(flag))
    OR_15.Add(AND_15)
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4604)
def Event_4604(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 4604"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    OR_1.Add(FlagEnabled(1050389256))
    OR_1.Add(FlagEnabled(1050382713))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    AND_1.Add(FlagEnabled(1050389265))
    AND_1.Add(FlagEnabled(1050389266))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag_1)
    AND_2.Add(FlagEnabled(1038519255))
    AND_2.Add(FlagEnabled(1038519256))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_2)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1050389256))
    AND_15.Add(FlagEnabled(1050382713))
    AND_15.Add(FlagDisabled(flag))
    OR_15.Add(AND_15)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1050389265))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1050389266))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038519255))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1038519256))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4606)
def Event_4606(_, flag: uint):
    """Event 4606"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagDisabled(7611))
    AND_1.Add(FlagDisabled(1050389265))
    OR_1.Add(FlagEnabled(1050389205))
    OR_1.Add(FlagEnabled(1050389206))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 7611))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1050389265))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1050389205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1050389206))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4607)
def Event_4607(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 4607"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1035539204):
        DisableFlag(flag_1)
    OR_1.Add(FlagEnabled(1043399305))
    OR_1.Add(FlagEnabled(1043392713))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    AND_2.Add(FlagDisabled(1035539204))
    OR_2.Add(FlagEnabled(1039449205))
    OR_2.Add(FlagEnabled(1039442703))
    AND_2.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_1)
    OR_3.Add(FlagEnabled(1035539205))
    OR_3.Add(FlagEnabled(1035532703))
    SkipLinesIfConditionFalse(2, OR_3)
    EnableFlag(flag_2)
    OR_4.Add(FlagEnabled(400173))
    OR_4.Add(FlagEnabled(400174))
    OR_4.Add(FlagEnabled(400175))
    SkipLinesIfConditionFalse(1, OR_4)
    EnableFlag(flag_3)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1043399305))
    AND_13.Add(FlagEnabled(1043392713))
    AND_13.Add(FlagDisabled(flag))
    OR_15.Add(AND_13)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1035539204))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039449205))
    AND_14.Add(FlagEnabled(1039442703))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3669))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3670))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1035539205))
    AND_15.Add(FlagEnabled(1035532703))
    AND_15.Add(FlagDisabled(flag_2))
    OR_15.Add(AND_15)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400173))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400174))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 400175))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4608)
def Event_4608(_, flag: uint):
    """Event 4608"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3825, 3829)))
    AND_1.Add(FlagRangeAllDisabled(flag_range=(3821, 3822)))
    OR_1.Add(FlagEnabled(1039449255))
    OR_1.Add(FlagEnabled(1039449256))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3825))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3826))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3827))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3828))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3829))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3821))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3822))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039449255))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039449256))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4609)
def Event_4609(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 4609"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    AND_1.Add(FlagEnabled(3947))
    AND_1.Add(FlagEnabled(1039409255))
    AND_1.Add(FlagEnabled(1039409264))
    AND_1.Add(FlagDisabled(1036489213))
    AND_1.Add(FlagDisabled(1039519209))
    AND_1.Add(FlagDisabled(11109819))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(3947))
    AND_2.Add(FlagEnabled(1039409255))
    AND_2.Add(FlagEnabled(1036489213))
    AND_2.Add(FlagDisabled(1039519209))
    AND_2.Add(FlagDisabled(11109819))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_1)
    AND_3.Add(FlagEnabled(3947))
    AND_3.Add(FlagEnabled(1039409255))
    AND_3.Add(FlagEnabled(1039519209))
    AND_3.Add(FlagDisabled(11109819))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_2)
    AND_4.Add(FlagEnabled(3947))
    AND_4.Add(FlagEnabled(1039409255))
    AND_4.Add(FlagEnabled(11109819))
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(flag_3)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3947))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039409255))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039409264))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1036489213))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1039519209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 11109819))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(4611)
def Event_4611(_, flag: uint, flag_1: uint):
    """Event 4611"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4208, 4209)))
    OR_1.Add(FlagEnabled(11009554))
    AND_5.Add(FlagDisabled(11009555))
    AND_5.Add(FlagEnabled(118))
    OR_1.Add(AND_5)
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11009460))
    AND_1.Add(FlagDisabled(1051569454))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(4207, 4208)))
    AND_2.Add(FlagEnabled(1040549254))
    AND_2.Add(FlagEnabled(1040549205))
    AND_2.Add(FlagDisabled(11009554))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_1)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4207))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4208))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 4209))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 11009554))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 11009555))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 118))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 11009460))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1040549254))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1040549205))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 1051569454))
    
    MAIN.Await(OR_15)
    
    Restart()


@ContinueOnRest(4612)
def Event_4612():
    """Event 4612"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1051579201):
        return
    EnableFlag(1051579201)
    if FlagDisabled(1051579200):
        return
    GotoIfFlagEnabled(Label.L0, flag=1251570400)
    GotoIfFlagEnabled(Label.L1, flag=1247580400)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(1051579200)
    DisableFlag(1047589250)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(1051579200)
    EnableFlag(1047589250)
    End()


@RestartOnRest(3179)
def Event_3179():
    """Event 3179"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (3160, 3164))
    DisableNetworkConnectedFlagRange(flag_range=(3160, 3164))
    EnableNetworkFlag(3160)
    SkipLinesIfFlagRangeAnyEnabled(2, (3165, 3178))
    DisableNetworkConnectedFlagRange(flag_range=(3165, 3178))
    EnableNetworkFlag(3165)
    GotoIfFlagDisabled(Label.L0, flag=3160)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3239)
def Event_3239():
    """Event 3239"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3238)
    SkipLinesIfFlagRangeAnyEnabled(2, (3220, 3224))
    DisableNetworkConnectedFlagRange(flag_range=(3220, 3224))
    EnableNetworkFlag(3220)
    AND_10.Add(FlagEnabled(3221))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3220, 3224))
    EnableNetworkFlag(3220)
    SkipLinesIfFlagRangeAnyEnabled(2, (3225, 3228))
    DisableNetworkConnectedFlagRange(flag_range=(3225, 3228))
    EnableNetworkFlag(3225)
    GotoIfFlagDisabled(Label.L0, flag=3220)
    if FlagEnabled(110):
        DisableNetworkConnectedFlagRange(flag_range=(3225, 3228))
        EnableNetworkFlag(3226)
    if FlagEnabled(9116):
        DisableNetworkConnectedFlagRange(flag_range=(3225, 3228))
        EnableNetworkFlag(3227)
    if FlagEnabled(11109246):
        DisableNetworkConnectedFlagRange(flag_range=(3225, 3228))
        EnableNetworkFlag(3228)
    
    MAIN.Await(FlagEnabled(3238))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4719)
def Event_4719():
    """Event 4719"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4718)
    SkipLinesIfFlagRangeAnyEnabled(2, (4700, 4704))
    DisableNetworkConnectedFlagRange(flag_range=(4700, 4704))
    EnableNetworkFlag(4700)
    AND_10.Add(FlagEnabled(4701))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4700, 4704))
    EnableNetworkFlag(4700)
    SkipLinesIfFlagRangeAnyEnabled(2, (4705, 4719))
    DisableNetworkConnectedFlagRange(flag_range=(4705, 4719))
    EnableNetworkFlag(4705)
    GotoIfFlagDisabled(Label.L0, flag=4700)
    AND_14.Add(FlagEnabled(4717))
    SkipLinesIfConditionFalse(2, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(4705, 4719))
    EnableNetworkFlag(4705)
    AND_15.Add(FlagEnabled(4705))
    AND_15.Add(FlagEnabled(1042369414))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(4705, 4719))
    EnableNetworkFlag(4717)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(1042369414)
    
    MAIN.Await(FlagEnabled(4718))
    
    Restart()


@RestartOnRest(4739)
def Event_4739():
    """Event 4739"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (4720, 4723))
    DisableNetworkConnectedFlagRange(flag_range=(4720, 4723))
    EnableNetworkFlag(4720)
    SkipLinesIfFlagRangeAnyEnabled(2, (4725, 4728))
    DisableNetworkConnectedFlagRange(flag_range=(4725, 4728))
    EnableNetworkFlag(4725)
    SkipLinesIfFlagRangeAnyEnabled(2, (4730, 4733))
    DisableNetworkConnectedFlagRange(flag_range=(4730, 4733))
    EnableNetworkFlag(4730)
    SkipLinesIfFlagRangeAnyEnabled(2, (4735, 4738))
    DisableNetworkConnectedFlagRange(flag_range=(4735, 4738))
    EnableNetworkFlag(4735)
    SkipLinesIfFlagRangeAnyEnabled(2, (4740, 4743))
    DisableNetworkConnectedFlagRange(flag_range=(4740, 4743))
    EnableNetworkFlag(4740)
    SkipLinesIfFlagRangeAnyEnabled(2, (4745, 4748))
    DisableNetworkConnectedFlagRange(flag_range=(4745, 4748))
    EnableNetworkFlag(4745)
    SkipLinesIfFlagRangeAnyEnabled(2, (4750, 4753))
    DisableNetworkConnectedFlagRange(flag_range=(4750, 4753))
    EnableNetworkFlag(4750)
    SkipLinesIfFlagRangeAnyEnabled(2, (4755, 4758))
    DisableNetworkConnectedFlagRange(flag_range=(4755, 4758))
    EnableNetworkFlag(4755)
    SkipLinesIfFlagRangeAnyEnabled(2, (4760, 4763))
    DisableNetworkConnectedFlagRange(flag_range=(4760, 4763))
    EnableNetworkFlag(4760)
    SkipLinesIfFlagRangeAnyEnabled(2, (4765, 4768))
    DisableNetworkConnectedFlagRange(flag_range=(4765, 4768))
    EnableNetworkFlag(4765)
    SkipLinesIfFlagRangeAnyEnabled(2, (4770, 4773))
    DisableNetworkConnectedFlagRange(flag_range=(4770, 4773))
    EnableNetworkFlag(4770)
    SkipLinesIfFlagRangeAnyEnabled(2, (4775, 4778))
    DisableNetworkConnectedFlagRange(flag_range=(4775, 4778))
    EnableNetworkFlag(4775)
    SkipLinesIfFlagRangeAnyEnabled(2, (4780, 4783))
    DisableNetworkConnectedFlagRange(flag_range=(4780, 4783))
    EnableNetworkFlag(4780)
    SkipLinesIfFlagRangeAnyEnabled(2, (4785, 4788))
    DisableNetworkConnectedFlagRange(flag_range=(4785, 4788))
    EnableNetworkFlag(4785)
    SkipLinesIfFlagRangeAnyEnabled(2, (4790, 4793))
    DisableNetworkConnectedFlagRange(flag_range=(4790, 4793))
    EnableNetworkFlag(4790)
    SkipLinesIfFlagRangeAnyEnabled(2, (4795, 4798))
    DisableNetworkConnectedFlagRange(flag_range=(4795, 4798))
    EnableNetworkFlag(4795)
    SkipLinesIfFlagRangeAnyEnabled(2, (4800, 4803))
    DisableNetworkConnectedFlagRange(flag_range=(4800, 4803))
    EnableNetworkFlag(4800)
    SkipLinesIfFlagRangeAnyEnabled(2, (4805, 4808))
    DisableNetworkConnectedFlagRange(flag_range=(4805, 4808))
    EnableNetworkFlag(4805)
    SkipLinesIfFlagRangeAnyEnabled(2, (4810, 4813))
    DisableNetworkConnectedFlagRange(flag_range=(4810, 4813))
    EnableNetworkFlag(4810)
    End()


@RestartOnRest(4759)
def Event_4759():
    """Event 4759"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (4740, 4744))
    DisableNetworkConnectedFlagRange(flag_range=(4740, 4744))
    EnableNetworkFlag(4740)
    AND_10.Add(FlagEnabled(4741))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4740, 4744))
    EnableNetworkFlag(4740)
    SkipLinesIfFlagRangeAnyEnabled(2, (4745, 4758))
    DisableNetworkConnectedFlagRange(flag_range=(4745, 4758))
    EnableNetworkFlag(4745)
    GotoIfFlagDisabled(Label.L0, flag=4740)
    AND_1.Add(FlagEnabled(1041369201))
    AND_1.Add(FlagDisabled(1041369202))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4745, 4758))
    EnableNetworkFlag(4746)
    AND_2.Add(FlagEnabled(1041369201))
    AND_2.Add(FlagEnabled(1041369202))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4745, 4758))
    EnableNetworkFlag(4747)
    AND_5.Add(FlagDisabled(1041369226))
    AND_5.Add(FlagDisabled(1044349221))
    AND_5.Add(FlagDisabled(1045369221))
    AND_5.Add(FlagDisabled(1043399221))
    SkipLinesIfConditionFalse(4, AND_5)
    EnableFlag(1041369226)
    EnableFlag(1044349221)
    EnableFlag(1045369221)
    EnableFlag(1043399221)
    AND_6.Add(FlagDisabled(1041369225))
    AND_6.Add(FlagDisabled(1044349220))
    AND_6.Add(FlagDisabled(1045369220))
    AND_6.Add(FlagDisabled(1043399220))
    GotoIfConditionTrue(Label.L0, input_condition=AND_6)
    EnableNetworkFlag(1041369226)
    EnableNetworkFlag(1044349221)
    EnableNetworkFlag(1045369221)
    EnableNetworkFlag(1043399221)
    if FlagEnabled(1041369225):
        DisableNetworkFlag(1041369226)
        Goto(Label.L10)
    if FlagEnabled(1044349220):
        DisableNetworkFlag(1044349221)
        Goto(Label.L10)
    if FlagEnabled(1045369220):
        DisableNetworkFlag(1045369221)
        Goto(Label.L10)
    if FlagEnabled(1043399220):
        DisableNetworkFlag(1043399221)
        Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableNetworkFlag(1041369225)
    DisableNetworkFlag(1044349220)
    DisableNetworkFlag(1045369220)
    DisableNetworkFlag(1043399220)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4979)
def Event_4979():
    """Event 4979"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (4960, 4964))
    DisableNetworkConnectedFlagRange(flag_range=(4960, 4964))
    EnableNetworkFlag(4960)
    AND_10.Add(FlagEnabled(4961))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4960, 4964))
    EnableNetworkFlag(4960)
    SkipLinesIfFlagRangeAnyEnabled(2, (4965, 4979))
    DisableNetworkConnectedFlagRange(flag_range=(4965, 4979))
    EnableNetworkFlag(4965)
    GotoIfFlagDisabled(Label.L0, flag=4960)
    AND_1.Add(FlagEnabled(1043379201))
    AND_1.Add(FlagDisabled(1043379202))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4965, 4979))
    EnableNetworkFlag(4966)
    AND_2.Add(FlagEnabled(1043379201))
    AND_2.Add(FlagEnabled(1043379202))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4965, 4979))
    EnableNetworkFlag(4967)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(4999)
def Event_4999():
    """Event 4999"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (4980, 4984))
    DisableNetworkConnectedFlagRange(flag_range=(4980, 4984))
    EnableNetworkFlag(4980)
    DisableNetworkConnectedFlagRange(flag_range=(4982, 4983))
    if FlagEnabled(4703):
        IncrementEventValue(4982, bit_count=2, max_value=2)
    if FlagEnabled(4723):
        IncrementEventValue(4982, bit_count=2, max_value=2)
    if FlagEnabled(4743):
        IncrementEventValue(4982, bit_count=2, max_value=2)
    if FlagEnabled(4982):
        DisableNetworkConnectedFlagRange(flag_range=(4980, 4984))
        EnableNetworkFlag(4982)
    if FlagEnabled(4983):
        DisableNetworkConnectedFlagRange(flag_range=(4980, 4984))
        EnableNetworkFlag(4983)
    OR_5.Add(FlagEnabled(1043379201))
    OR_5.Add(FlagEnabled(1042389201))
    OR_5.Add(FlagEnabled(1041369201))
    SkipLinesIfConditionFalse(1, OR_5)
    EnableNetworkFlag(4985)
    OR_6.Add(FlagEnabled(1043379206))
    OR_6.Add(FlagEnabled(1042389206))
    OR_6.Add(FlagEnabled(1041369206))
    SkipLinesIfConditionFalse(1, OR_6)
    EnableNetworkFlag(4986)
    End()


@RestartOnRest(3679)
def Event_3679():
    """Event 3679"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3678)
    SkipLinesIfFlagRangeAnyEnabled(2, (3660, 3663))
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3660)
    AND_2.Add(FlagEnabled(3661))
    AND_2.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3660)
    SkipLinesIfFlagRangeAnyEnabled(2, (3665, 3671))
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3665)
    GotoIfFlagDisabled(Label.L0, flag=3660)
    AND_3.Add(FlagEnabled(3665))
    OR_3.Add(FlagEnabled(1043399307))
    OR_3.Add(FlagEnabled(32009203))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3666)
    OR_4.Add(FlagEnabled(3665))
    OR_4.Add(FlagEnabled(3666))
    AND_4.Add(FlagEnabled(9410))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3667)
    EnableFlag(1051369259)
    EnableFlag(1051369361)
    AND_5.Add(FlagEnabled(3667))
    AND_5.Add(FlagEnabled(9130))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3668)
    AND_6.Add(FlagEnabled(3668))
    AND_6.Add(FlagEnabled(1051369266))
    SkipLinesIfConditionFalse(4, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3669)
    DisableFlag(1051369361)
    EnableFlag(1035539208)
    AND_7.Add(FlagEnabled(3669))
    AND_7.Add(FlagEnabled(1051369266))
    AND_7.Add(FlagEnabled(1035539204))
    SkipLinesIfConditionFalse(3, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3670)
    EnableFlag(1035539208)
    AND_9.Add(FlagDisabled(1052520800))
    AND_9.Add(FlagEnabled(1035539205))
    SkipLinesIfConditionFalse(1, AND_9)
    EnableNetworkFlag(1035539209)
    AND_10.Add(FlagEnabled(3670))
    AND_10.Add(FlagEnabled(1052520800))
    AND_10.Add(FlagEnabled(1035539205))
    SkipLinesIfConditionFalse(3, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3665, 3671))
    EnableNetworkFlag(3671)
    DisableFlag(1035539208)
    
    MAIN.Await(FlagEnabled(3678))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3199)
def Event_3199():
    """Event 3199"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3198)
    SkipLinesIfFlagRangeAnyEnabled(2, (3180, 3184))
    DisableNetworkConnectedFlagRange(flag_range=(3180, 3184))
    EnableNetworkFlag(3180)
    AND_10.Add(FlagEnabled(3181))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3180, 3184))
    EnableNetworkFlag(3180)
    SkipLinesIfFlagRangeAnyEnabled(2, (3185, 3199))
    DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
    EnableNetworkFlag(3185)
    GotoIfFlagDisabled(Label.L0, flag=3180)
    if FlagEnabled(105):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3187)
    if FlagEnabled(181):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3191)
    if FlagEnabled(11109358):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3188)
    if FlagEnabled(1035449235):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3189)
    if FlagEnabled(400033):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3190)
    if FlagEnabled(1035449226):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3192)
    if FlagEnabled(7601):
        DisableNetworkConnectedFlagRange(flag_range=(3185, 3199))
        EnableNetworkFlag(3193)
    if FlagEnabled(12059166):
        DisableNetworkConnectedFlagRange(flag_range=(3180, 3184))
        EnableNetworkFlag(3183)
        SaveRequest()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3198))
    
    Restart()


@RestartOnRest(3279)
def Event_3279():
    """Event 3279"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3278)
    SkipLinesIfFlagRangeAnyEnabled(2, (3260, 3264))
    DisableNetworkConnectedFlagRange(flag_range=(3260, 3264))
    EnableNetworkFlag(3260)
    AND_10.Add(FlagEnabled(3261))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3260, 3264))
    EnableNetworkFlag(3260)
    SkipLinesIfFlagRangeAnyEnabled(2, (3265, 3269))
    DisableNetworkConnectedFlagRange(flag_range=(3265, 3269))
    EnableNetworkFlag(3265)
    GotoIfFlagDisabled(Label.L20, flag=3260)
    AND_1.Add(FlagEnabled(10009360))
    AND_1.Add(FlagDisabled(10009362))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3265, 3269))
    EnableNetworkFlag(3266)
    AND_2.Add(FlagEnabled(10009360))
    AND_2.Add(FlagEnabled(10009362))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3265, 3269))
    EnableFlag(3268)
    AND_4.Add(FlagEnabled(4229))
    SkipLinesIfConditionFalse(3, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3265, 3270))
    EnableFlag(3270)
    Goto(Label.L20)
    AND_3.Add(FlagEnabled(10000800))
    SkipLinesIfConditionFalse(3, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3265, 3270))
    EnableFlag(3269)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfFlagRangeAnyEnabled(2, (10009510, 10009514))
    DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
    EnableNetworkFlag(10009514)
    OR_10.Add(FlagDisabled(3260))
    OR_10.Add(FlagEnabled(3268))
    OR_10.Add(FlagEnabled(3269))
    OR_10.Add(FlagEnabled(3270))
    GotoIfConditionTrue(Label.L19, input_condition=OR_10)
    AND_5.Add(FlagEnabled(10002736))
    AND_5.Add(FlagDisabled(10009390))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
    EnableNetworkFlag(10009510)
    AND_6.Add(FlagEnabled(10002737))
    AND_6.Add(FlagDisabled(10009391))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
    EnableNetworkFlag(10009511)
    AND_7.Add(FlagEnabled(10002738))
    AND_7.Add(FlagDisabled(10009392))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
    EnableNetworkFlag(10009512)
    AND_8.Add(FlagEnabled(10002739))
    AND_8.Add(FlagDisabled(10009393))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
    EnableNetworkFlag(10009513)
    if FlagEnabled(10002765):
        DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
        EnableNetworkFlag(10009514)
        Goto(Label.L15)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableNetworkConnectedFlagRange(flag_range=(10002736, 10002739))
    DisableNetworkFlag(10002765)
    Goto(Label.L20)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableNetworkConnectedFlagRange(flag_range=(10002732, 10002739))
    DisableNetworkConnectedFlagRange(flag_range=(10009510, 10009514))
    DisableNetworkFlag(10002765)
    EnableNetworkFlag(10009514)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableNetworkFlag(10009350)
    
    MAIN.Await(FlagEnabled(3278))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3299)
def Event_3299():
    """Event 3299"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (3280, 3284))
    DisableNetworkConnectedFlagRange(flag_range=(3280, 3284))
    EnableNetworkFlag(3280)
    SkipLinesIfFlagRangeAnyEnabled(2, (3285, 3298))
    DisableNetworkConnectedFlagRange(flag_range=(3285, 3298))
    EnableNetworkFlag(3285)
    GotoIfFlagDisabled(Label.L0, flag=3280)
    AND_1.Add(FlagEnabled(1043359201))
    AND_1.Add(FlagEnabled(1044350800))
    AND_1.Add(FlagDisabled(1043359247))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3285, 3298))
    EnableNetworkFlag(3286)
    OR_1.Add(FlagEnabled(4703))
    OR_1.Add(FlagEnabled(4723))
    OR_1.Add(FlagEnabled(4743))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3285, 3298))
    EnableNetworkFlag(3295)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(3259)
def Event_3259(_, first_flag: uint, last_flag: uint, first_flag_1: uint, last_flag_1: uint):
    """Event 3259"""
    if FlagRangeAllDisabled((first_flag, last_flag)):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        EnableNetworkFlag(first_flag)
    if FlagRangeAllDisabled((first_flag_1, last_flag_1)):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag_1, last_flag_1))
        EnableNetworkFlag(first_flag_1)
    GotoIfFlagDisabled(Label.L0, flag=first_flag)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(3119)
def Event_3119():
    """Event 3119"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3118)
    SkipLinesIfFlagRangeAnyEnabled(2, (3100, 3104))
    DisableNetworkConnectedFlagRange(flag_range=(3100, 3104))
    EnableNetworkFlag(3100)
    AND_10.Add(FlagEnabled(3101))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3100, 3104))
    EnableNetworkFlag(3100)
    SkipLinesIfFlagRangeAnyEnabled(2, (3105, 3119))
    DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
    EnableNetworkFlag(3105)
    GotoIfFlagDisabled(Label.L0, flag=3100)
    if FlagEnabled(400073):
        DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
        EnableFlag(3106)
    AND_1.Add(EventValue(flag=16009260, bit_count=4) >= 3)
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
    EnableFlag(3107)
    AND_2.Add(FlagEnabled(16000800))
    AND_2.Add(FlagEnabled(16009208))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
    EnableFlag(3108)
    AND_3.Add(FlagEnabled(16000800))
    AND_3.Add(FlagDisabled(16009208))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(16009246))
    SkipLinesIfConditionFalse(2, OR_3)
    DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
    EnableFlag(3109)
    if FlagEnabled(16009265):
        DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
        EnableFlag(3110)
    if FlagEnabled(16009264):
        DisableNetworkConnectedFlagRange(flag_range=(3105, 3119))
        EnableFlag(3111)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3118))
    
    Restart()


@RestartOnRest(3399)
def Event_3399():
    """Event 3399"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3398)
    SkipLinesIfFlagRangeAnyEnabled(2, (3380, 3383))
    DisableNetworkConnectedFlagRange(flag_range=(3380, 3383))
    EnableNetworkFlag(3380)
    SkipLinesIfFlagRangeAnyEnabled(2, (3385, 3397))
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3385)
    GotoIfFlagDisabled(Label.L0, flag=3380)
    OR_1.Add(FlagEnabled(1043319206))
    OR_1.Add(FlagEnabled(3403))
    OR_1.Add(FlagEnabled(3062))
    OR_1.Add(FlagEnabled(9101))
    AND_1.Add(FlagEnabled(3385))
    AND_1.Add(FlagEnabled(1045349207))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3386)
    AND_2.Add(FlagEnabled(3386))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3387)
    AND_3.Add(FlagEnabled(3387))
    AND_3.Add(FlagEnabled(1039409206))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3388)
    AND_4.Add(FlagEnabled(3388))
    AND_4.Add(FlagEnabled(1038419205))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3389)
    AND_5.Add(FlagEnabled(3389))
    AND_5.Add(FlagEnabled(1038439206))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3390)
    AND_6.Add(FlagEnabled(3390))
    AND_6.Add(FlagEnabled(1038439209))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3391)
    AND_7.Add(FlagEnabled(3391))
    AND_7.Add(FlagEnabled(1036499207))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3392)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_14.Add(FlagEnabled(3392))
    AND_14.Add(FlagEnabled(35009209))
    SkipLinesIfConditionFalse(4, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(3385, 3397))
    EnableNetworkFlag(3393)
    DisableNetworkConnectedFlagRange(flag_range=(3380, 3383))
    EnableNetworkFlag(3383)
    
    MAIN.Await(FlagEnabled(3398))
    
    Restart()


@RestartOnRest(3419)
def Event_3419():
    """Event 3419"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3418)
    SkipLinesIfFlagRangeAnyEnabled(2, (3400, 3403))
    DisableNetworkConnectedFlagRange(flag_range=(3400, 3403))
    EnableNetworkFlag(3400)
    AND_15.Add(FlagEnabled(3402))
    AND_15.Add(FlagDisabled(1045349256))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(3400, 3403))
    EnableNetworkFlag(3400)
    SkipLinesIfFlagRangeAnyEnabled(2, (3405, 3417))
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3405)
    GotoIfFlagDisabled(Label.L0, flag=3400)
    AND_14.Add(FlagEnabled(3408))
    AND_14.Add(FlagDisabled(1045349256))
    SkipLinesIfConditionFalse(2, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3407)
    AND_1.Add(FlagEnabled(3405))
    AND_1.Add(FlagEnabled(1043319206))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3406)
    EnableFlag(1043319209)
    AND_2.Add(FlagEnabled(3406))
    AND_2.Add(FlagEnabled(1043300800))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3407)
    DisableFlag(1043319209)
    AND_3.Add(FlagEnabled(3407))
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(3386, 3397)))
    AND_3.Add(FlagEnabled(1043319207))
    SkipLinesIfConditionFalse(3, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3408)
    EnableFlag(1045349256)
    AND_4.Add(FlagEnabled(3407))
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(3386, 3397)))
    AND_4.Add(FlagEnabled(1045342719))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3408)
    AND_5.Add(FlagEnabled(3408))
    AND_5.Add(FlagEnabled(1045349255))
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3409)
    EnableFlag(1045349259)
    AND_6.Add(FlagRangeAnyEnabled(flag_range=(3405, 3408)))
    AND_6.Add(FlagEnabled(1039409206))
    SkipLinesIfConditionFalse(3, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3409)
    EnableFlag(1045349259)
    AND_7.Add(FlagEnabled(3407))
    AND_7.Add(FlagEnabled(3385))
    AND_7.Add(FlagEnabled(3383))
    AND_7.Add(FlagEnabled(1043319207))
    SkipLinesIfConditionFalse(5, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3408)
    DisableNetworkConnectedFlagRange(flag_range=(3400, 3403))
    EnableNetworkFlag(3402)
    EnableFlag(1045349256)
    AND_8.Add(FlagEnabled(3407))
    AND_8.Add(FlagEnabled(3385))
    AND_8.Add(FlagEnabled(3383))
    AND_8.Add(FlagEnabled(1045342719))
    SkipLinesIfConditionFalse(4, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(3405, 3417))
    EnableNetworkFlag(3408)
    DisableNetworkConnectedFlagRange(flag_range=(3400, 3403))
    EnableNetworkFlag(3402)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3418))
    
    Restart()
    End()


@RestartOnRest(3439)
def Event_3439():
    """Event 3439"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3438)
    SkipLinesIfFlagRangeAnyEnabled(2, (3420, 3424))
    DisableNetworkConnectedFlagRange(flag_range=(3420, 3424))
    EnableNetworkFlag(3420)
    AND_10.Add(FlagEnabled(3421))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3420, 3424))
    EnableNetworkFlag(3420)
    SkipLinesIfFlagRangeAnyEnabled(2, (3425, 3439))
    DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
    EnableNetworkFlag(3425)
    GotoIfFlagDisabled(Label.L0, flag=3420)
    AND_1.Add(FlagEnabled(1037429210))
    AND_1.Add(FlagDisabled(1038519205))
    AND_1.Add(FlagDisabled(16009208))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
    EnableNetworkFlag(3426)
    OR_2.Add(FlagEnabled(1038519205))
    OR_2.Add(FlagEnabled(16009208))
    SkipLinesIfConditionFalse(2, OR_2)
    DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
    EnableFlag(3427)
    AND_3.Add(FlagEnabled(16009306))
    AND_3.Add(EventValue(flag=16009260, bit_count=3) >= 2)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
    EnableFlag(3428)
    if FlagEnabled(16009319):
        DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
        EnableFlag(3429)
    AND_14.Add(FlagEnabled(16000800))
    AND_14.Add(FlagDisabled(16009208))
    OR_14.Add(AND_14)
    OR_14.Add(FlagEnabled(16009246))
    AND_4.Add(FlagEnabled(16009327))
    AND_4.Add(OR_14)
    AND_4.Add(FlagDisabled(3689))
    AND_4.Add(FlagDisabled(3448))
    AND_4.Add(FlagDisabled(3449))
    AND_4.Add(FlagDisabled(3886))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
    EnableFlag(3430)
    AND_5.Add(FlagEnabled(16009328))
    AND_5.Add(FlagDisabled(16009327))
    AND_6.Add(FlagRangeAnyEnabled(flag_range=(3425, 3428)))
    AND_6.Add(FlagDisabled(16009319))
    AND_6.Add(FlagEnabled(16000800))
    OR_5.Add(AND_5)
    OR_5.Add(AND_6)
    OR_5.Add(FlagEnabled(16009335))
    SkipLinesIfConditionFalse(2, OR_5)
    DisableNetworkConnectedFlagRange(flag_range=(3425, 3439))
    EnableFlag(3431)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3438))
    
    Restart()


@RestartOnRest(3459)
def Event_3459():
    """Event 3459"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3458)
    SkipLinesIfFlagRangeAnyEnabled(2, (3440, 3444))
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3440)
    AND_15.Add(FlagEnabled(3442))
    AND_15.Add(FlagEnabled(3443))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3443)
    AND_14.Add(FlagDisabled(3450))
    AND_14.Add(FlagEnabled(3440))
    AND_14.Add(FlagEnabled(3442))
    SkipLinesIfConditionFalse(2, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3440)
    AND_13.Add(FlagEnabled(3450))
    AND_13.Add(FlagEnabled(3440))
    AND_13.Add(FlagEnabled(3442))
    SkipLinesIfConditionFalse(2, AND_13)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3442)
    AND_10.Add(FlagEnabled(3441))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3440)
    SkipLinesIfFlagRangeAnyEnabled(2, (3445, 3459))
    DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
    EnableNetworkFlag(3445)
    AND_11.Add(FlagEnabled(1039449285))
    AND_11.Add(FlagDisabled(1039449316))
    SkipLinesIfConditionFalse(1, AND_11)
    EnableNetworkFlag(1039449316)
    GotoIfFlagDisabled(Label.L0, flag=3440)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3445, 3447)))
    AND_1.Add(FlagEnabled(9122))
    SkipLinesIfConditionFalse(5, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
    EnableNetworkFlag(3457)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3443)
    Goto(Label.L0)
    OR_1.Add(FlagEnabled(1037442701))
    OR_1.Add(FlagEnabled(1037449206))
    OR_1.Add(FlagEnabled(110))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
    EnableNetworkFlag(3446)
    if FlagEnabled(1037449205):
        DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
        EnableNetworkFlag(3447)
    if FlagEnabled(11109430):
        DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
        EnableNetworkFlag(3448)
    AND_5.Add(FlagEnabled(16009406))
    AND_5.Add(EventValue(flag=16009260, bit_count=4) >= 1)
    OR_5.Add(AND_5)
    AND_6.Add(FlagDisabled(16009405))
    AND_6.Add(FlagEnabled(9122))
    OR_5.Add(AND_6)
    SkipLinesIfConditionFalse(2, OR_5)
    DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
    EnableNetworkFlag(3449)
    AND_7.Add(FlagEnabled(16009405))
    AND_7.Add(FlagEnabled(9122))
    OR_7.Add(AND_7)
    AND_8.Add(FlagEnabled(16009416))
    OR_7.Add(AND_8)
    SkipLinesIfConditionFalse(3, OR_7)
    DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
    EnableNetworkFlag(3456)
    EnableNetworkFlag(11109430)
    AND_9.Add(FlagEnabled(3456))
    AND_9.Add(FlagEnabled(1039449263))
    SkipLinesIfConditionFalse(2, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
    EnableNetworkFlag(3450)
    if FlagEnabled(3827):
        DisableNetworkConnectedFlagRange(flag_range=(3445, 3457))
        EnableNetworkFlag(3451)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3458))
    
    Restart()


@RestartOnRest(3499)
def Event_3499():
    """Event 3499"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (3480, 3484))
    DisableNetworkConnectedFlagRange(flag_range=(3480, 3484))
    EnableNetworkFlag(3480)
    AND_10.Add(FlagEnabled(3481))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3480, 3484))
    EnableNetworkFlag(3480)
    SkipLinesIfFlagRangeAnyEnabled(2, (3485, 3499))
    DisableNetworkConnectedFlagRange(flag_range=(3485, 3499))
    EnableNetworkFlag(3485)
    GotoIfFlagDisabled(Label.L0, flag=3480)
    if FlagEnabled(182):
        DisableNetworkConnectedFlagRange(flag_range=(3485, 3499))
        EnableFlag(3486)
    if FlagEnabled(11000500):
        DisableNetworkConnectedFlagRange(flag_range=(3485, 3499))
        EnableFlag(3487)
    if FlagEnabled(110):
        DisableNetworkConnectedFlagRange(flag_range=(3485, 3499))
        EnableFlag(3488)
    if FlagEnabled(118):
        DisableNetworkConnectedFlagRange(flag_range=(3485, 3499))
        EnableFlag(3489)
        SaveRequest()
        DefineLabel(0)
        End()


@RestartOnRest(3559)
def Event_3559():
    """Event 3559"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (3540, 3544))
    DisableNetworkConnectedFlagRange(flag_range=(3540, 3544))
    EnableNetworkFlag(3540)
    AND_10.Add(FlagEnabled(3541))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3540, 3544))
    EnableNetworkFlag(3540)
    SkipLinesIfFlagRangeAnyEnabled(2, (3545, 3559))
    DisableNetworkConnectedFlagRange(flag_range=(3545, 3559))
    EnableNetworkFlag(3545)
    GotoIfFlagDisabled(Label.L0, flag=3540)
    if FlagEnabled(1035429210):
        DisableNetworkConnectedFlagRange(flag_range=(3545, 3559))
        EnableFlag(3546)
        DisableNetworkConnectedFlagRange(flag_range=(3540, 3544))
        EnableNetworkFlag(3543)
        SaveRequest()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3639)
def Event_3639():
    """Event 3639"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3638)
    SkipLinesIfFlagRangeAnyEnabled(2, (3620, 3624))
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3620)
    AND_10.Add(FlagEnabled(3621))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3620)
    SkipLinesIfFlagRangeAnyEnabled(2, (3625, 3639))
    DisableNetworkConnectedFlagRange(flag_range=(3625, 3639))
    EnableNetworkFlag(3626)
    AND_5.Add(FlagEnabled(3623))
    AND_5.Add(FlagDisabled(3631))
    SkipLinesIfConditionFalse(7, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3620)
    DisableNetworkConnectedFlagRange(flag_range=(3625, 3637))
    EnableNetworkFlag(3631)
    EnableFlag(1049539210)
    SaveRequest()
    Goto(Label.L0)
    GotoIfFlagDisabled(Label.L0, flag=3620)
    AND_1.Add(FlagEnabled(1043379263))
    AND_1.Add(FlagDisabled(1044389206))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3625, 3637))
    EnableFlag(3625)
    AND_2.Add(FlagEnabled(1043379263))
    AND_2.Add(FlagEnabled(1044389206))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(1043379263))
    SkipLinesIfConditionFalse(2, OR_2)
    DisableNetworkConnectedFlagRange(flag_range=(3625, 3637))
    EnableFlag(3626)
    if FlagEnabled(7607):
        DisableNetworkConnectedFlagRange(flag_range=(3625, 3637))
        EnableNetworkFlag(3627)
    if FlagEnabled(1035469207):
        DisableNetworkConnectedFlagRange(flag_range=(3625, 3637))
        EnableNetworkFlag(3630)
    OR_5.Add(FlagEnabled(1039529206))
    OR_5.Add(FlagEnabled(1049539210))
    SkipLinesIfConditionFalse(2, OR_5)
    DisableNetworkConnectedFlagRange(flag_range=(3625, 3637))
    EnableNetworkFlag(3631)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3638))
    
    Restart()


@RestartOnRest(3659)
def Event_3659():
    """Event 3659"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3658)
    SkipLinesIfFlagRangeAnyEnabled(2, (3640, 3643))
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3643))
    EnableNetworkFlag(3640)
    if FlagEnabled(3641):
        DisableNetworkConnectedFlagRange(flag_range=(3640, 3643))
        EnableNetworkFlag(3640)
    SkipLinesIfFlagRangeAnyEnabled(2, (3645, 3657))
    DisableNetworkConnectedFlagRange(flag_range=(3645, 3657))
    EnableNetworkFlag(3645)
    GotoIfFlagDisabled(Label.L0, flag=3640)
    AND_1.Add(FlagEnabled(3645))
    AND_1.Add(EventValue(flag=1051439235, bit_count=5) >= 4)
    SkipLinesIfConditionFalse(5, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3645, 3657))
    EnableNetworkFlag(3646)
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3643))
    EnableNetworkFlag(3642)
    EnableFlag(1051439212)
    AND_2.Add(FlagEnabled(3646))
    AND_2.Add(FlagEnabled(3640))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3645, 3657))
    EnableNetworkFlag(3647)
    AND_3.Add(FlagEnabled(3647))
    AND_3.Add(EventValue(flag=1051439235, bit_count=5) >= 9)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3645, 3657))
    EnableNetworkFlag(3648)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3658))
    
    Restart()
    End()


@RestartOnRest(3699)
def Event_3699():
    """Event 3699"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3698)
    SkipLinesIfFlagRangeAnyEnabled(2, (3680, 3684))
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    AND_10.Add(FlagEnabled(3681))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    GotoIfFlagDisabled(Label.L1, flag=3681)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    DisableFlag(31009207)
    DisableFlag(1038419265)
    DisableFlag(1037549209)
    DisableFlag(31009266)
    WaitFrames(frames=1)
    OR_11.Add(FlagEnabled(3685))
    OR_11.Add(FlagEnabled(3686))
    SkipLinesIfConditionFalse(2, OR_11)
    EnableFlag(31009207)
    Goto(Label.L1)
    OR_12.Add(FlagEnabled(3687))
    SkipLinesIfConditionFalse(2, OR_12)
    EnableFlag(1038419265)
    Goto(Label.L1)
    OR_13.Add(FlagEnabled(3688))
    OR_13.Add(FlagEnabled(3693))
    SkipLinesIfConditionFalse(2, OR_13)
    EnableFlag(1037549209)
    Goto(Label.L1)
    OR_14.Add(FlagEnabled(3691))
    OR_14.Add(FlagEnabled(3692))
    OR_14.Add(FlagEnabled(3694))
    SkipLinesIfConditionFalse(2, OR_14)
    EnableFlag(31009266)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagRangeAnyEnabled(5, (3685, 3699))
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3685)
    EnableNetworkFlag(1038419270)
    DisableNetworkFlag(1038419271)
    EnableFlag(31009219)
    GotoIfFlagDisabled(Label.L0, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3691)
    if FlagEnabled(31009206):
        DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
        EnableNetworkFlag(3686)
        EnableNetworkFlag(1038419270)
        DisableNetworkFlag(1038419271)
    AND_2.Add(FlagEnabled(31009206))
    AND_2.Add(FlagEnabled(1038419254))
    AND_2.Add(FlagDisabled(16009208))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3687)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    AND_3.Add(FlagEnabled(31009206))
    AND_3.Add(FlagEnabled(1037549211))
    AND_3.Add(FlagDisabled(16009208))
    AND_3.Add(FlagDisabled(1037549210))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3688)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    AND_4.Add(FlagEnabled(31009206))
    AND_4.Add(FlagEnabled(1037549211))
    AND_4.Add(FlagDisabled(16009208))
    AND_4.Add(FlagEnabled(1037549210))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3693)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    AND_5.Add(FlagEnabled(31009206))
    AND_5.Add(FlagEnabled(16009208))
    SkipLinesIfConditionFalse(4, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3689)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    if FlagEnabled(3697):
        DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
        EnableNetworkFlag(3690)
    if FlagEnabled(16009359):
        DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
        EnableNetworkFlag(3690)
        DisableNetworkFlag(1038419270)
        EnableNetworkFlag(1038419271)
    OR_6.Add(FlagEnabled(1039549205))
    SkipLinesIfConditionFalse(4, OR_6)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3696)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    OR_7.Add(FlagEnabled(1039549205))
    OR_7.Add(FlagEnabled(3696))
    AND_7.Add(OR_7)
    AND_7.Add(FlagDisabled(31002715))
    AND_7.Add(FlagDisabled(9000))
    SkipLinesIfConditionFalse(5, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3691)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    EnableFlag(31009269)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_8.Add(FlagEnabled(31000850))
    AND_8.Add(FlagDisabled(31009256))
    SkipLinesIfConditionFalse(4, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
    EnableNetworkFlag(3694)
    DisableNetworkFlag(1038419270)
    EnableNetworkFlag(1038419271)
    if FlagEnabled(31009256):
        DisableNetworkConnectedFlagRange(flag_range=(3685, 3699))
        EnableNetworkFlag(3692)
        DisableNetworkFlag(1038419270)
        EnableNetworkFlag(1038419271)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3698))
    
    Restart()


@RestartOnRest(3719)
def Event_3719():
    """Event 3719"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3718)
    SkipLinesIfFlagRangeAnyEnabled(2, (3700, 3704))
    DisableNetworkConnectedFlagRange(flag_range=(3700, 3704))
    EnableNetworkFlag(3700)
    AND_10.Add(FlagEnabled(3701))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3700, 3704))
    EnableNetworkFlag(3700)
    SkipLinesIfFlagRangeAnyEnabled(3, (3705, 3719))
    DisableNetworkConnectedFlagRange(flag_range=(3705, 3719))
    EnableNetworkFlag(3705)
    EnableFlag(10007452)
    GotoIfFlagDisabled(Label.L0, flag=3700)
    AND_1.Add(FlagEnabled(3705))
    AND_1.Add(FlagEnabled(1041389413))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(3062))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3705, 3719))
    EnableNetworkFlag(3707)
    AND_2.Add(FlagEnabled(3707))
    AND_2.Add(FlagEnabled(11109213))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3705, 3719))
    EnableNetworkFlag(3708)
    AND_3.Add(FlagEnabled(110))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3705, 3719))
    EnableNetworkFlag(3709)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3718))
    
    Restart()
    End()


@RestartOnRest(3879)
def Event_3879():
    """Event 3879"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3878)
    SkipLinesIfFlagRangeAnyEnabled(2, (3860, 3864))
    DisableNetworkConnectedFlagRange(flag_range=(3860, 3864))
    EnableNetworkFlag(3860)
    AND_10.Add(FlagEnabled(3861))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3860, 3864))
    EnableNetworkFlag(3860)
    SkipLinesIfFlagRangeAnyEnabled(2, (3865, 3879))
    DisableNetworkConnectedFlagRange(flag_range=(3865, 3879))
    EnableNetworkFlag(3865)
    GotoIfFlagDisabled(Label.L0, flag=3860)
    if FlagEnabled(11009210):
        DisableNetworkConnectedFlagRange(flag_range=(3865, 3879))
        EnableFlag(3866)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3878))
    
    Restart()


@RestartOnRest(3899)
def Event_3899():
    """Event 3899"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3898)
    SkipLinesIfFlagRangeAnyEnabled(2, (3880, 3884))
    DisableNetworkConnectedFlagRange(flag_range=(3880, 3884))
    EnableNetworkFlag(3880)
    AND_10.Add(FlagEnabled(3881))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3880, 3884))
    EnableNetworkFlag(3880)
    SkipLinesIfFlagRangeAnyEnabled(2, (3885, 3899))
    DisableNetworkConnectedFlagRange(flag_range=(3885, 3899))
    EnableNetworkFlag(3885)
    GotoIfFlagDisabled(Label.L0, flag=3880)
    if FlagEnabled(16009208):
        DisableNetworkConnectedFlagRange(flag_range=(3885, 3899))
        EnableFlag(3886)
    if FlagEnabled(16009460):
        DisableNetworkConnectedFlagRange(flag_range=(3885, 3899))
        EnableFlag(3887)
    AND_1.Add(FlagDisabled(16009208))
    AND_1.Add(FlagEnabled(16000800))
    SkipLinesIfConditionFalse(4, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3885, 3899))
    EnableFlag(3888)
    DisableNetworkConnectedFlagRange(flag_range=(3880, 3884))
    EnableFlag(3883)
    DisableFlag(16009464)
    OR_2.Add(FlagEnabled(7605))
    OR_2.Add(FlagDisabled(3886))
    OR_2.Add(FlagEnabled(118))
    GotoIfConditionFalse(Label.L0, input_condition=OR_2)
    EnableFlag(16009464)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(FlagEnabled(16009460))
    OR_5.Add(FlagEnabled(3883))
    GotoIfConditionFalse(Label.L1, input_condition=OR_5)
    OR_6.Add(FlagDisabled(16009458))
    OR_6.Add(FlagEnabled(7605))
    GotoIfConditionFalse(Label.L1, input_condition=OR_6)
    EnableFlag(400295)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(3898))
    
    Restart()


@RestartOnRest(3479)
def Event_3479():
    """Event 3479"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3478)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(3460, 3463)))
    OR_1.Add(not AND_1)
    OR_1.Add(not AND_2)
    AND_2.Add(FlagEnabled(3461))
    AND_2.Add(FlagEnabled(3000))
    SkipLinesIfConditionTrue(2, OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3460, 3463))
    EnableNetworkFlag(3460)
    SkipLinesIfFlagRangeAnyEnabled(2, (3465, 3469))
    DisableNetworkConnectedFlagRange(flag_range=(3465, 3469))
    EnableNetworkFlag(3465)
    if FlagEnabled(7608):
        DisableNetworkConnectedFlagRange(flag_range=(3460, 3463))
        EnableNetworkFlag(3463)
    GotoIfFlagDisabled(Label.L0, flag=3460)
    AND_3.Add(FlagEnabled(3465))
    AND_3.Add(FlagEnabled(3369))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3465, 3469))
    EnableNetworkFlag(3466)
    AND_10.Add(FlagEnabled(1034509255))
    AND_10.Add(FlagDisabled(3469))
    SkipLinesIfConditionFalse(1, AND_10)
    EnableNetworkFlag(1034509259)
    AND_4.Add(FlagEnabled(3466))
    AND_4.Add(FlagEnabled(1034509256))
    AND_4.Add(FlagEnabled(9118))
    SkipLinesIfConditionFalse(3, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3465, 3469))
    EnableNetworkFlag(3467)
    EnableNetworkFlag(1034509269)
    OR_5.Add(FlagEnabled(3363))
    OR_5.Add(FlagEnabled(7609))
    AND_5.Add(OR_5)
    AND_5.Add(FlagEnabled(9118))
    AND_5.Add(FlagEnabled(1034509256))
    SkipLinesIfConditionFalse(6, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3465, 3469))
    EnableNetworkFlag(3468)
    EnableNetworkFlag(14009267)
    DisableNetworkFlag(1034509269)
    DisableNetworkFlag(1051369239)
    DisableNetworkFlag(1034509267)
    AND_6.Add(FlagEnabled(3468))
    AND_6.Add(FlagEnabled(14009266))
    OR_6.Add(FlagEnabled(1044369228))
    OR_6.Add(FlagEnabled(14009263))
    AND_6.Add(OR_6)
    SkipLinesIfConditionFalse(3, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3465, 3469))
    EnableNetworkFlag(3469)
    DisableNetworkFlag(1034509259)
    
    MAIN.Await(FlagEnabled(3478))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3599)
def Event_3599():
    """Event 3599"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3598)
    SkipLinesIfFlagRangeAllDisabled(3, (3580, 3583))
    AND_1.Add(FlagEnabled(3581))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3580, 3583))
    EnableNetworkFlag(3580)
    SkipLinesIfFlagRangeAnyEnabled(2, (3585, 3587))
    DisableNetworkConnectedFlagRange(flag_range=(3585, 3587))
    EnableNetworkFlag(3585)
    GotoIfFlagDisabled(Label.L0, flag=3580)
    AND_2.Add(FlagEnabled(3585))
    AND_2.Add(FlagEnabled(1045389222))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3585, 3587))
    EnableNetworkFlag(3586)
    EnableNetworkFlag(1046360706)
    AND_3.Add(FlagEnabled(4229))
    AND_3.Add(FlagEnabled(1046369205))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3585, 3587))
    EnableNetworkFlag(3587)
    
    MAIN.Await(FlagEnabled(3598))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3819)
def Event_3819():
    """Event 3819"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3818)
    SkipLinesIfFlagRangeAllDisabled(3, (3800, 3803))
    AND_1.Add(FlagEnabled(3801))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3800, 3803))
    EnableNetworkFlag(3800)
    SkipLinesIfFlagRangeAnyEnabled(2, (3805, 3806))
    DisableNetworkConnectedFlagRange(flag_range=(3805, 3806))
    EnableNetworkFlag(3805)
    GotoIfFlagDisabled(Label.L0, flag=3800)
    AND_2.Add(FlagEnabled(3805))
    AND_2.Add(FlagEnabled(1039399220))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3805, 3806))
    EnableNetworkFlag(3806)
    DisableNetworkConnectedFlagRange(flag_range=(3800, 3803))
    EnableNetworkFlag(3803)
    
    MAIN.Await(FlagEnabled(3818))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3379)
def Event_3379():
    """Event 3379"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3378)
    SkipLinesIfFlagRangeAnyEnabled(2, (3360, 3364))
    DisableNetworkConnectedFlagRange(flag_range=(3360, 3364))
    EnableNetworkFlag(3360)
    AND_10.Add(FlagEnabled(3361))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3360, 3364))
    EnableNetworkFlag(3360)
    if FlagEnabled(7609):
        DisableNetworkConnectedFlagRange(flag_range=(3360, 3364))
        EnableNetworkFlag(3363)
    GotoIfFlagDisabled(Label.L0, flag=3360)
    SkipLinesIfFlagRangeAnyEnabled(2, (3365, 3377))
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3365)
    AND_3.Add(FlagEnabled(3365))
    AND_3.Add(FlagEnabled(9410))
    SkipLinesIfConditionFalse(3, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3366)
    EnableFlag(1051369360)
    AND_4.Add(FlagEnabled(3366))
    AND_4.Add(FlagEnabled(9130))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3367)
    AND_5.Add(FlagEnabled(3367))
    OR_5.Add(FlagEnabled(1051369235))
    OR_5.Add(FlagEnabled(1051369204))
    AND_5.Add(OR_5)
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3368)
    DisableFlag(1051369360)
    AND_6.Add(FlagEnabled(3368))
    AND_6.Add(FlagEnabled(1044369231))
    SkipLinesIfConditionFalse(4, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3369)
    EnableNetworkFlag(1041339259)
    EnableNetworkFlag(1034509254)
    AND_7.Add(FlagEnabled(3369))
    AND_7.Add(FlagEnabled(1034509256))
    AND_7.Add(FlagEnabled(9118))
    SkipLinesIfConditionFalse(4, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3370)
    EnableNetworkFlag(1051369239)
    EnableNetworkFlag(1034509267)
    AND_8.Add(FlagEnabled(3370))
    AND_8.Add(FlagEnabled(7608))
    SkipLinesIfConditionFalse(5, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3371)
    DisableNetworkFlag(1034509269)
    DisableNetworkFlag(1051369239)
    DisableNetworkFlag(1034509267)
    AND_9.Add(FlagEnabled(3371))
    AND_9.Add(FlagEnabled(14009356))
    OR_9.Add(AND_9)
    AND_11.Add(FlagEnabled(3463))
    AND_11.Add(FlagRangeAnyEnabled(flag_range=(3368, 3370)))
    OR_9.Add(AND_11)
    SkipLinesIfConditionFalse(4, OR_9)
    DisableNetworkConnectedFlagRange(flag_range=(3365, 3377))
    EnableNetworkFlag(3372)
    DisableNetworkFlag(1034509269)
    DisableNetworkFlag(1051369239)
    
    MAIN.Await(FlagEnabled(3378))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3739)
def Event_3739():
    """Event 3739"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3738)
    SkipLinesIfFlagRangeAnyEnabled(2, (3720, 3724))
    DisableNetworkConnectedFlagRange(flag_range=(3720, 3724))
    EnableNetworkFlag(3720)
    SkipLinesIfFlagRangeAnyEnabled(2, (3725, 3739))
    DisableNetworkConnectedFlagRange(flag_range=(3725, 3739))
    EnableNetworkFlag(3725)
    GotoIfFlagDisabled(Label.L0, flag=3720)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3738))
    
    Restart()
    End()


@RestartOnRest(4159)
def Event_4159():
    """Event 4159"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4158)
    SkipLinesIfFlagRangeAnyEnabled(2, (4140, 4144))
    DisableNetworkConnectedFlagRange(flag_range=(4140, 4144))
    EnableNetworkFlag(4140)
    AND_10.Add(FlagEnabled(4141))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4140, 4144))
    EnableNetworkFlag(4140)
    SkipLinesIfFlagRangeAnyEnabled(2, (4145, 4157))
    DisableNetworkConnectedFlagRange(flag_range=(4145, 4159))
    EnableNetworkFlag(4145)
    GotoIfFlagDisabled(Label.L0, flag=4140)
    OR_1.Add(FlagDisabled(35009316))
    OR_1.Add(FlagEnabled(1045520180))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1036439213))
    AND_1.Add(FlagEnabled(3063))
    AND_1.Add(FlagDisabled(1044522701))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4145, 4159))
    EnableNetworkFlag(4146)
    if FlagEnabled(1044529259):
        DisableNetworkConnectedFlagRange(flag_range=(4145, 4159))
        EnableNetworkFlag(4147)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(4158))
    
    Restart()


@RestartOnRest(3799)
def Event_3799():
    """Event 3799"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3798)
    SkipLinesIfFlagRangeAllDisabled(3, (3780, 3783))
    AND_1.Add(FlagEnabled(3781))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3780, 3783))
    EnableNetworkFlag(3780)
    SkipLinesIfFlagRangeAnyEnabled(2, (3785, 3787))
    DisableNetworkConnectedFlagRange(flag_range=(3785, 3787))
    EnableNetworkFlag(3785)
    GotoIfFlagDisabled(Label.L0, flag=3780)
    AND_2.Add(FlagEnabled(3785))
    AND_2.Add(FlagEnabled(9122))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3785, 3787))
    EnableNetworkFlag(3786)
    
    MAIN.Await(FlagEnabled(3798))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3859)
def Event_3859():
    """Event 3859"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (3840, 3844))
    DisableNetworkConnectedFlagRange(flag_range=(3840, 3844))
    EnableNetworkFlag(3840)
    AND_10.Add(FlagEnabled(3841))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3840, 3844))
    EnableNetworkFlag(3840)
    SkipLinesIfFlagRangeAnyEnabled(2, (3845, 3859))
    DisableNetworkConnectedFlagRange(flag_range=(3845, 3859))
    EnableNetworkFlag(3845)
    GotoIfFlagDisabled(Label.L0, flag=3840)
    if FlagEnabled(1051569206):
        DisableNetworkConnectedFlagRange(flag_range=(3845, 3859))
        EnableFlag(3846)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3959)
def Event_3959():
    """Event 3959"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3958)
    SkipLinesIfFlagRangeAnyEnabled(2, (3940, 3944))
    DisableNetworkConnectedFlagRange(flag_range=(3940, 3944))
    EnableNetworkFlag(3940)
    if FlagEnabled(11109306):
        DisableNetworkConnectedFlagRange(flag_range=(3940, 3944))
        EnableNetworkFlag(3943)
    AND_10.Add(FlagEnabled(3941))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3940, 3944))
    EnableNetworkFlag(3940)
    SkipLinesIfFlagRangeAnyEnabled(2, (3945, 3949))
    DisableNetworkConnectedFlagRange(flag_range=(3945, 3949))
    EnableNetworkFlag(3945)
    GotoIfFlagDisabled(Label.L0, flag=3940)
    AND_1.Add(FlagEnabled(3945))
    AND_1.Add(FlagEnabled(1043379356))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3945, 3949))
    EnableNetworkFlag(3946)
    AND_2.Add(FlagEnabled(3946))
    AND_2.Add(FlagEnabled(31159206))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3945, 3949))
    EnableFlag(3947)
    AND_3.Add(FlagEnabled(3947))
    AND_3.Add(FlagDisabled(1039409260))
    AND_3.Add(FlagEnabled(11109808))
    AND_3.Add(FlagEnabled(9118))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3945, 3949))
    EnableFlag(3948)
    AND_4.Add(FlagEnabled(3947))
    AND_4.Add(FlagDisabled(1039409260))
    AND_4.Add(FlagEnabled(11109812))
    AND_4.Add(FlagEnabled(9118))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3945, 3949))
    EnableFlag(3949)
    DisableNetworkConnectedFlagRange(flag_range=(3940, 3944))
    EnableNetworkFlag(3943)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3759)
def Event_3759():
    """Event 3759"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3758)
    SkipLinesIfFlagRangeAnyEnabled(2, (3740, 3743))
    DisableNetworkConnectedFlagRange(flag_range=(3740, 3743))
    EnableNetworkFlag(3740)
    AND_15.Add(FlagEnabled(3748))
    AND_15.Add(FlagEnabled(1034509425))
    SkipLinesIfConditionFalse(4, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(3740, 3743))
    EnableNetworkFlag(3741)
    DisableFlag(1034509425)
    EnableFlag(1034509403)
    SkipLinesIfFlagRangeAnyEnabled(2, (3745, 3757))
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3745)
    AND_14.Add(FlagRangeAnyEnabled(flag_range=(3745, 3749)))
    AND_14.Add(FlagEnabled(1035420150))
    SkipLinesIfConditionFalse(5, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(3740, 3743))
    EnableNetworkFlag(3740)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3750)
    DisableFlag(1042369415)
    AND_1.Add(FlagEnabled(3746))
    AND_1.Add(FlagDisabled(1042369410))
    AND_1.Add(FlagDisabled(1042369407))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3745)
    DisableFlag(1042369415)
    AND_2.Add(FlagEnabled(3745))
    AND_2.Add(FlagEnabled(1042369411))
    SkipLinesIfConditionFalse(6, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3746)
    DisableFlag(1042369411)
    EnableFlag(1042369414)
    EnableFlag(1042369415)
    EnableFlag(4718)
    OR_3.Add(FlagEnabled(1042369410))
    OR_3.Add(FlagEnabled(1042369407))
    AND_3.Add(FlagEnabled(3746))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3747)
    EnableFlag(1042369413)
    DisableFlag(1042369415)
    OR_4.Add(FlagEnabled(1034509419))
    OR_4.Add(FlagEnabled(3062))
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(3745, 3746)))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(6, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3747)
    DisableFlag(1042369415)
    if FlagDisabled(1042369410):
        EnableFlag(1042369416)
        EnableFlag(11109785)
    GotoIfFlagDisabled(Label.L0, flag=3740)
    AND_5.Add(FlagEnabled(3747))
    AND_5.Add(FlagEnabled(1034509416))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3748)
    AND_6.Add(FlagEnabled(3748))
    AND_6.Add(FlagEnabled(1034509421))
    SkipLinesIfConditionFalse(7, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3749)
    EnableNetworkFlag(1034510739)
    EnableNetworkFlag(1034500703)
    EnableFlag(1034509430)
    EnableFlag(1034509433)
    EnableFlag(3578)
    AND_7.Add(FlagEnabled(3750))
    AND_7.Add(FlagEnabled(1034509406))
    SkipLinesIfConditionFalse(3, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3745, 3757))
    EnableNetworkFlag(3751)
    EnableFlag(1035429255)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3758))
    
    Restart()


@RestartOnRest(3619)
def Event_3619():
    """Event 3619"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3618)
    SkipLinesIfFlagRangeAnyEnabled(2, (3600, 3603))
    DisableNetworkConnectedFlagRange(flag_range=(3600, 3603))
    EnableNetworkFlag(3600)
    SkipLinesIfFlagRangeAnyEnabled(2, (3605, 3617))
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3605)
    GotoIfFlagEnabled(Label.L1, flag=3617)
    GotoIfFlagDisabled(Label.L1, flag=3603)
    DisableNetworkConnectedFlagRange(flag_range=(3600, 3603))
    EnableNetworkFlag(3601)
    EnableFlag(1045379207)
    DisableFlag(1045379202)
    DisableFlag(1044349252)
    DisableFlag(12029152)
    DisableFlag(1051369352)
    DisableFlag(1052389302)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(3600):
        DisableFlag(1045379207)
        DisableFlag(1045379209)
    GotoIfFlagDisabled(Label.L0, flag=3600)
    AND_7.Add(FlagEnabled(3612))
    AND_7.Add(FlagDisabled(9411))
    SkipLinesIfConditionFalse(3, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3611)
    DisableFlag(1051369359)
    AND_8.Add(FlagEnabled(3611))
    AND_8.Add(FlagDisabled(1051369358))
    AND_8.Add(FlagDisabled(12029157))
    SkipLinesIfConditionFalse(3, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3605)
    DisableFlag(1051369357)
    AND_9.Add(FlagRangeAnyEnabled(flag_range=(3605, 3610)))
    AND_9.Add(FlagEnabled(9412))
    AND_9.Add(FlagDisabled(1051369357))
    SkipLinesIfConditionFalse(2, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3614)
    AND_1.Add(FlagEnabled(3606))
    AND_1.Add(FlagDisabled(1044350800))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3605)
    DisableFlag(1044349257)
    AND_2.Add(FlagEnabled(3605))
    AND_2.Add(FlagEnabled(1045379205))
    AND_2.Add(FlagEnabled(1044352717))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3606)
    EnableFlag(1044349257)
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(3605, 3606)))
    AND_3.Add(FlagEnabled(1045379205))
    AND_3.Add(FlagEnabled(1044350800))
    SkipLinesIfConditionFalse(3, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3607)
    DisableFlag(1044349257)
    AND_4.Add(FlagEnabled(3607))
    AND_4.Add(FlagEnabled(1044349255))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3608)
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(3605, 3608)))
    AND_5.Add(FlagEnabled(1034509410))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3609)
    AND_6.Add(FlagEnabled(3609))
    AND_6.Add(FlagEnabled(1034509416))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3610)
    OR_10.Add(FlagEnabled(12029157))
    OR_10.Add(FlagEnabled(1051362739))
    AND_10.Add(FlagRangeAnyEnabled(flag_range=(3605, 3610)))
    AND_10.Add(FlagEnabled(9410))
    AND_10.Add(OR_10)
    SkipLinesIfConditionFalse(3, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3611)
    EnableFlag(1051369357)
    AND_11.Add(FlagEnabled(3611))
    AND_11.Add(FlagEnabled(9411))
    SkipLinesIfConditionFalse(4, AND_11)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3612)
    EnableFlag(1051369359)
    EnableFlag(1051369358)
    AND_12.Add(FlagEnabled(3612))
    AND_12.Add(FlagEnabled(9412))
    SkipLinesIfConditionFalse(3, AND_12)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3613)
    DisableFlag(1051369359)
    OR_13.Add(FlagEnabled(1052389306))
    OR_13.Add(FlagEnabled(1034499238))
    OR_13.Add(FlagEnabled(12027080))
    AND_13.Add(FlagEnabled(3613))
    AND_13.Add(OR_13)
    SkipLinesIfConditionFalse(3, AND_13)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3614)
    DisableFlag(1051369357)
    AND_14.Add(FlagEnabled(3614))
    AND_14.Add(FlagEnabled(1044350800))
    AND_14.Add(FlagEnabled(1034509410))
    SkipLinesIfConditionFalse(3, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3615)
    EnableFlag(1044359259)
    AND_15.Add(FlagEnabled(3615))
    AND_15.Add(FlagEnabled(1044359256))
    SkipLinesIfConditionFalse(3, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3616)
    DisableFlag(1044359259)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagRangeAllDisabled(Label.L2, flag_range=(3605, 3616))
    GotoIfFlagDisabled(Label.L2, flag=9108)
    GotoIfFlagDisabled(Label.L2, flag=114)
    DisableNetworkConnectedFlagRange(flag_range=(3605, 3617))
    EnableNetworkFlag(3617)
    DisableFlag(1044359259)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(FlagEnabled(3618))
    
    Restart()


@RestartOnRest(3579)
def Event_3579():
    """Event 3579"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3578)
    SkipLinesIfFlagRangeAnyEnabled(3, (3560, 3563))
    DisableNetworkConnectedFlagRange(flag_range=(3560, 3563))
    EnableNetworkFlag(3560)
    EnableFlag(1034509349)
    SkipLinesIfFlagRangeAnyEnabled(2, (3565, 3577))
    DisableNetworkConnectedFlagRange(flag_range=(3565, 3577))
    EnableNetworkFlag(3565)
    GotoIfFlagDisabled(Label.L0, flag=3560)
    AND_1.Add(FlagEnabled(3565))
    AND_1.Add(FlagEnabled(1034509410))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3565, 3577))
    EnableNetworkFlag(3566)
    AND_2.Add(FlagEnabled(3566))
    AND_2.Add(FlagEnabled(1034509416))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3565, 3577))
    EnableNetworkFlag(3567)
    AND_3.Add(FlagEnabled(3567))
    AND_3.Add(FlagEnabled(1034509315))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3565, 3577))
    EnableNetworkFlag(3568)
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(3565, 3568)))
    AND_4.Add(FlagEnabled(1034509424))
    SkipLinesIfConditionFalse(6, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3565, 3577))
    EnableNetworkFlag(3569)
    if FlagDisabled(11109919):
        EnableFlag(1035509215)
    else:
        EnableFlag(1035509216)
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(3565, 3568)))
    AND_5.Add(FlagEnabled(1034509433))
    SkipLinesIfConditionFalse(6, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3565, 3577))
    EnableNetworkFlag(3569)
    if FlagDisabled(11109919):
        EnableFlag(1035509215)
    else:
        EnableFlag(1035509216)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3578))
    
    Restart()


@RestartOnRest(3779)
def Event_3779():
    """Event 3779"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3778)
    SkipLinesIfFlagRangeAnyEnabled(2, (3760, 3763))
    DisableNetworkConnectedFlagRange(flag_range=(3760, 3763))
    EnableNetworkFlag(3760)
    SkipLinesIfFlagRangeAnyEnabled(2, (3765, 3777))
    DisableNetworkConnectedFlagRange(flag_range=(3765, 3777))
    EnableNetworkFlag(3765)
    GotoIfFlagDisabled(Label.L0, flag=3760)
    AND_1.Add(FlagEnabled(3765))
    AND_1.Add(FlagEnabled(1034509410))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3765, 3777))
    EnableNetworkFlag(3766)
    EnableFlagRange((1034509360, 1034509361))
    AND_2.Add(FlagEnabled(3766))
    AND_2.Add(FlagEnabled(1034509416))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3765, 3777))
    EnableNetworkFlag(3767)
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(3765, 3767)))
    AND_3.Add(FlagEnabled(1034499242))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3765, 3777))
    EnableNetworkFlag(3768)
    DisableNetworkConnectedFlagRange(flag_range=(3760, 3763))
    EnableNetworkFlag(3763)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(3778))
    
    Restart()


@RestartOnRest(3919)
def Event_3919():
    """Event 3919"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3918)
    SkipLinesIfFlagRangeAnyEnabled(3, (3900, 3903))
    DisableNetworkConnectedFlagRange(flag_range=(3900, 3903))
    EnableNetworkFlag(3900)
    EnableFlag(400357)
    SkipLinesIfFlagRangeAnyEnabled(2, (3905, 3917))
    DisableNetworkConnectedFlagRange(flag_range=(3905, 3917))
    EnableNetworkFlag(3905)
    GotoIfFlagDisabled(Label.L0, flag=3900)
    OR_1.Add(FlagEnabled(9101))
    OR_1.Add(FlagEnabled(10009610))
    AND_1.Add(FlagEnabled(3905))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3905, 3917))
    EnableNetworkFlag(3906)
    AND_2.Add(FlagEnabled(3906))
    AND_2.Add(FlagEnabled(9101))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3905, 3917))
    EnableNetworkFlag(3907)
    OR_3.Add(FlagEnabled(11109532))
    OR_3.Add(FlagEnabled(1034509421))
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(3905, 3907)))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3905, 3917))
    EnableNetworkFlag(3908)
    OR_5.Add(FlagDisabled(11109506))
    OR_5.Add(FlagEnabled(1034509410))
    OR_5.Add(FlagEnabled(1034509431))
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(3905, 3907)))
    AND_5.Add(FlagEnabled(110))
    AND_5.Add(OR_5)
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3905, 3917))
    EnableNetworkFlag(3908)
    AND_4.Add(FlagEnabled(3908))
    AND_4.Add(EventValue(flag=11109545, bit_count=5) >= 2)
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3905, 3917))
    EnableNetworkFlag(3909)
    DisableNetworkConnectedFlagRange(flag_range=(3900, 3903))
    EnableNetworkFlag(3903)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(10009614)
    if FlagEnabled(3905):
        EnableFlag(10009614)
    
    MAIN.Await(FlagEnabled(3918))
    
    Restart()
    End()


@RestartOnRest(4139)
def Event_4139():
    """Event 4139"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4138)
    SkipLinesIfFlagRangeAnyEnabled(2, (4120, 4123))
    DisableNetworkConnectedFlagRange(flag_range=(4120, 4123))
    EnableNetworkFlag(4120)
    SkipLinesIfFlagRangeAnyEnabled(2, (4125, 4137))
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4125)
    GotoIfFlagDisabled(Label.L0, flag=4120)
    AND_1.Add(FlagEnabled(4125))
    AND_1.Add(FlagEnabled(4047))
    AND_1.Add(FlagEnabled(11109625))
    SkipLinesIfConditionFalse(7, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4126)
    DisableNetworkConnectedFlagRange(flag_range=(4045, 4057))
    EnableNetworkFlag(4048)
    DisableNetworkConnectedFlagRange(flag_range=(4040, 4043))
    EnableNetworkFlag(4043)
    EnableFlag(4058)
    AND_2.Add(FlagEnabled(4126))
    AND_2.Add(FlagEnabled(11109015))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4127)
    OR_3.Add(FlagEnabled(3063))
    OR_3.Add(FlagEnabled(9410))
    AND_3.Add(FlagEnabled(4125))
    AND_3.Add(FlagEnabled(4043))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4127)
    AND_11.Add(FlagRangeAnyEnabled(flag_range=(4125, 4126)))
    AND_11.Add(FlagEnabled(110))
    SkipLinesIfConditionFalse(8, AND_11)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4127)
    if FlagDisabled(4043):
        DisableNetworkConnectedFlagRange(flag_range=(4045, 4057))
        EnableNetworkFlag(4048)
        DisableNetworkConnectedFlagRange(flag_range=(4040, 4043))
        EnableNetworkFlag(4043)
    EnableFlag(4058)
    AND_4.Add(FlagEnabled(4127))
    AND_4.Add(FlagEnabled(12030800))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4128)
    AND_5.Add(FlagEnabled(4128))
    AND_5.Add(FlagEnabled(12039157))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4129)
    AND_6.Add(FlagEnabled(4129))
    AND_6.Add(FlagEnabled(12039158))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4130)
    AND_7.Add(FlagEnabled(4137))
    AND_7.Add(FlagDisabled(12030850))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4130)
    AND_8.Add(FlagEnabled(4130))
    AND_8.Add(FlagEnabled(12032870))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4137)
    AND_9.Add(FlagEnabled(4130))
    AND_9.Add(FlagEnabled(12030850))
    SkipLinesIfConditionFalse(2, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4131)
    AND_10.Add(FlagEnabled(4137))
    AND_10.Add(FlagEnabled(12030850))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4131)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_15.Add(FlagRangeAnyEnabled(flag_range=(4125, 4129)))
    AND_15.Add(FlagEnabled(4123))
    OR_15.Add(FlagEnabled(9502))
    OR_15.Add(AND_15)
    SkipLinesIfConditionFalse(1, OR_15)
    EnableFlag(12039162)
    
    MAIN.Await(FlagEnabled(4138))
    
    Restart()
    End()


@RestartOnRest(4059)
def Event_4059():
    """Event 4059"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4058)
    SkipLinesIfFlagRangeAnyEnabled(2, (4040, 4043))
    DisableNetworkConnectedFlagRange(flag_range=(4040, 4043))
    EnableNetworkFlag(4040)
    SkipLinesIfFlagRangeAnyEnabled(2, (4045, 4057))
    DisableNetworkConnectedFlagRange(flag_range=(4045, 4057))
    EnableNetworkFlag(4045)
    GotoIfFlagDisabled(Label.L0, flag=4040)
    AND_1.Add(FlagEnabled(4045))
    AND_1.Add(FlagEnabled(1045390800))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4045, 4057))
    EnableNetworkFlag(4046)
    OR_2.Add(FlagEnabled(1045399206))
    OR_2.Add(FlagEnabled(11109609))
    AND_2.Add(FlagEnabled(4046))
    AND_2.Add(OR_2)
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4045, 4057))
    EnableNetworkFlag(4047)
    OR_3.Add(FlagEnabled(132))
    OR_3.Add(FlagEnabled(3064))
    OR_3.Add(FlagEnabled(3063))
    OR_3.Add(FlagEnabled(1051439205))
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(4045, 4046)))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4045, 4057))
    EnableNetworkFlag(4047)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(11109648)
    DisableFlag(11109649)
    OR_15.Add(FlagEnabled(1045399206))
    OR_15.Add(FlagEnabled(1051439205))
    AND_15.Add(FlagEnabled(4040))
    AND_15.Add(FlagEnabled(4047))
    AND_15.Add(FlagEnabled(1044399206))
    AND_15.Add(OR_15)
    SkipLinesIfConditionFalse(2, AND_15)
    EnableFlag(11109648)
    EnableFlag(11109649)
    
    MAIN.Await(FlagEnabled(4058))
    
    Restart()
    End()


@RestartOnRest(4079)
def Event_4079():
    """Event 4079"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4078)
    SkipLinesIfFlagRangeAnyEnabled(2, (4060, 4063))
    DisableNetworkConnectedFlagRange(flag_range=(4060, 4063))
    EnableNetworkFlag(4060)
    SkipLinesIfFlagRangeAnyEnabled(2, (4065, 4077))
    DisableNetworkConnectedFlagRange(flag_range=(4065, 4077))
    EnableNetworkFlag(4065)
    GotoIfFlagDisabled(Label.L0, flag=4060)
    AND_1.Add(FlagEnabled(4065))
    AND_1.Add(FlagEnabled(12029016))
    AND_1.Add(FlagEnabled(4048))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4065, 4077))
    EnableNetworkFlag(4077)
    EnableFlag(12029019)
    AND_2.Add(FlagEnabled(4065))
    AND_2.Add(FlagEnabled(12029016))
    AND_2.Add(FlagDisabled(4048))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4060, 4063))
    EnableNetworkFlag(4062)
    AND_3.Add(FlagEnabled(4077))
    AND_3.Add(FlagEnabled(9502))
    AND_3.Add(FlagEnabled(4131))
    SkipLinesIfConditionFalse(7, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4065, 4077))
    EnableNetworkFlag(4066)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4132)
    DisableNetworkConnectedFlagRange(flag_range=(4120, 4123))
    EnableNetworkFlag(4123)
    DisableFlag(12029019)
    AND_4.Add(FlagEnabled(4066))
    AND_4.Add(FlagEnabled(12039005))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4065, 4077))
    EnableNetworkFlag(4067)
    AND_5.Add(FlagEnabled(4077))
    AND_5.Add(FlagEnabled(4123))
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(4128, 4129)))
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4065, 4077))
    EnableNetworkFlag(4067)
    DisableFlag(12029019)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(4078))
    
    Restart()
    End()


@RestartOnRest(4119)
def Event_4119():
    """Event 4119"""
    if PlayerNotInOwnWorld():
        return
    SkipLinesIfFlagRangeAnyEnabled(2, (4100, 4104))
    DisableNetworkConnectedFlagRange(flag_range=(4100, 4104))
    EnableNetworkFlag(4100)
    AND_10.Add(FlagEnabled(4101))
    AND_10.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4100, 4104))
    EnableNetworkFlag(4100)
    SkipLinesIfFlagRangeAnyEnabled(2, (4105, 4119))
    DisableNetworkConnectedFlagRange(flag_range=(4105, 4119))
    EnableNetworkFlag(4105)
    GotoIfFlagDisabled(Label.L0, flag=4100)
    if FlagEnabled(1036419209):
        DisableNetworkConnectedFlagRange(flag_range=(4105, 4119))
        EnableNetworkFlag(4106)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4179)
def Event_4179():
    """Event 4179"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4178)
    SkipLinesIfFlagRangeAllDisabled(3, (4160, 4163))
    AND_1.Add(FlagEnabled(4161))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4160)
    SkipLinesIfFlagRangeAnyEnabled(3, (4165, 4177))
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4165)
    EnableNetworkFlag(1050389209)
    AND_10.Add(FlagRangeAnyEnabled(flag_range=(4165, 4168)))
    AND_10.Add(FlagEnabled(4163))
    SkipLinesIfConditionFalse(1, AND_10)
    EnableFlag(1050382702)
    SkipLinesIfFlagRangeAnyEnabled(2, (4169, 4170))
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4160)
    GotoIfFlagDisabled(Label.L0, flag=4160)
    AND_2.Add(FlagEnabled(4165))
    AND_2.Add(FlagEnabled(1050389207))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4166)
    DisableNetworkFlag(1050389209)
    AND_3.Add(FlagEnabled(4166))
    AND_3.Add(FlagEnabled(1050389255))
    SkipLinesIfConditionFalse(3, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4167)
    DisableNetworkFlag(1050389209)
    AND_4.Add(FlagEnabled(4167))
    AND_4.Add(FlagEnabled(4193))
    SkipLinesIfConditionFalse(3, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4168)
    DisableNetworkFlag(1050389209)
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(4191, 4192)))
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4169)
    DisableNetworkFlag(1050389209)
    AND_6.Add(FlagEnabled(7611))
    SkipLinesIfConditionFalse(5, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4171)
    DisableNetworkFlag(1050389209)
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4163)
    AND_7.Add(FlagRangeAllDisabled(flag_range=(4191, 4192)))
    AND_7.Add(FlagEnabled(4183))
    SkipLinesIfConditionFalse(3, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(4165, 4177))
    EnableNetworkFlag(4170)
    DisableNetworkFlag(1050389209)
    
    MAIN.Await(FlagEnabled(4178))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4199)
def Event_4199():
    """Event 4199"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4198)
    SkipLinesIfFlagRangeAnyEnabled(2, (4180, 4183))
    DisableNetworkConnectedFlagRange(flag_range=(4180, 4183))
    EnableNetworkFlag(4180)
    AND_1.Add(FlagEnabled(4181))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4180, 4183))
    EnableNetworkFlag(4180)

    # --- Label 5 --- #
    DefineLabel(5)
    SkipLinesIfFlagRangeAnyEnabled(3, (4185, 4197))
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4185)
    EnableNetworkFlag(1050389259)
    GotoIfFlagDisabled(Label.L0, flag=4180)
    AND_2.Add(FlagEnabled(4185))
    AND_2.Add(FlagEnabled(1050389255))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4186)
    DisableNetworkFlag(1050389259)
    AND_3.Add(FlagEnabled(4186))
    AND_3.Add(FlagEnabled(1050389257))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4187)
    if FlagEnabled(1050389266):
        EnableNetworkFlag(4197)
    AND_11.Add(FlagEnabled(4187))
    AND_11.Add(FlagEnabled(1050389266))
    AND_11.Add(FlagDisabled(1038519257))
    SkipLinesIfConditionFalse(4, AND_11)
    EnableNetworkFlag(1042559206)
    DisableNetworkFlag(1042559207)
    DisableNetworkFlag(1042559208)
    DisableNetworkFlag(1042559209)
    AND_4.Add(FlagEnabled(4187))
    AND_4.Add(FlagEnabled(1042550800))
    AND_4.Add(FlagEnabled(1038519257))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4188)
    AND_5.Add(FlagEnabled(4188))
    AND_5.Add(FlagEnabled(1042559205))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4189)
    AND_6.Add(FlagEnabled(4189))
    AND_6.Add(FlagEnabled(1051569256))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4190)
    AND_12.Add(FlagRangeAnyEnabled(flag_range=(4187, 4190)))
    AND_12.Add(FlagEnabled(1050389266))
    AND_12.Add(FlagEnabled(1038519257))
    SkipLinesIfConditionFalse(4, AND_12)
    DisableNetworkFlag(1042559206)
    EnableNetworkFlag(1042559207)
    EnableNetworkFlag(1042559208)
    EnableNetworkFlag(1042559209)
    AND_7.Add(FlagEnabled(4190))
    AND_7.Add(FlagEnabled(15009206))
    AND_7.Add(FlagEnabled(15000398))
    OR_7.Add(FlagEnabled(1050389227))
    OR_7.Add(FlagEnabled(15009213))
    AND_7.Add(OR_7)
    SkipLinesIfConditionFalse(8, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4193)
    EnableNetworkFlag(15009208)
    EnableNetworkFlag(15009209)
    DisableNetworkFlag(1042559206)
    DisableNetworkFlag(1042559207)
    DisableNetworkFlag(1042559208)
    DisableNetworkFlag(1042559209)
    AND_8.Add(FlagEnabled(4193))
    AND_8.Add(FlagEnabled(7610))
    SkipLinesIfConditionFalse(4, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4191)
    DisableNetworkFlag(15009208)
    DisableNetworkFlag(15009209)
    AND_9.Add(FlagEnabled(4193))
    AND_9.Add(FlagEnabled(7611))
    SkipLinesIfConditionFalse(4, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4194)
    DisableNetworkFlag(15009208)
    DisableNetworkFlag(15009209)
    AND_10.Add(FlagEnabled(4191))
    AND_10.Add(FlagEnabled(15009211))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(4185, 4197))
    EnableNetworkFlag(4192)
    
    MAIN.Await(FlagEnabled(4198))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3979)
def Event_3979():
    """Event 3979"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3978)
    SkipLinesIfFlagRangeAllDisabled(3, (3960, 3963))
    AND_1.Add(FlagEnabled(3961))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3960, 3963))
    EnableNetworkFlag(3960)
    SkipLinesIfFlagRangeAnyEnabled(2, (3965, 3968))
    DisableNetworkConnectedFlagRange(flag_range=(3965, 3968))
    EnableNetworkFlag(3965)
    GotoIfFlagDisabled(Label.L0, flag=3960)
    AND_2.Add(FlagEnabled(3965))
    AND_2.Add(FlagEnabled(11109659))
    AND_10.Add(FlagEnabled(181))
    AND_10.Add(FlagEnabled(11109659))
    OR_1.Add(AND_2)
    OR_1.Add(AND_10)
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3965, 3968))
    EnableNetworkFlag(3966)
    AND_3.Add(FlagEnabled(3966))
    AND_3.Add(FlagEnabled(11109358))
    AND_3.Add(FlagEnabled(11109660))
    AND_11.Add(FlagEnabled(181))
    AND_11.Add(FlagEnabled(11109659))
    OR_2.Add(FlagEnabled(110))
    OR_2.Add(AND_3)
    OR_2.Add(AND_11)
    SkipLinesIfConditionFalse(2, OR_2)
    DisableNetworkConnectedFlagRange(flag_range=(3965, 3968))
    EnableNetworkFlag(3967)
    AND_4.Add(FlagEnabled(9116))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3965, 3968))
    EnableNetworkFlag(3968)
    
    MAIN.Await(FlagEnabled(3978))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4219)
def Event_4219():
    """Event 4219"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4218)
    SkipLinesIfFlagRangeAllDisabled(3, (4200, 4203))
    AND_1.Add(FlagEnabled(4201))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4200, 4203))
    EnableNetworkFlag(4200)
    SkipLinesIfFlagRangeAnyEnabled(2, (4205, 4217))
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4205)
    GotoIfFlagDisabled(Label.L0, flag=4200)
    AND_15.Add(FlagDisabled(11009555))
    AND_15.Add(FlagEnabled(110))
    SkipLinesIfConditionFalse(4, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(4200, 4203))
    EnableNetworkFlag(4203)
    EnableNetworkFlag(4217)
    Goto(Label.L0)
    AND_2.Add(FlagEnabled(4205))
    AND_2.Add(FlagEnabled(11109859))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4206)
    AND_3.Add(FlagEnabled(4206))
    AND_3.Add(FlagEnabled(1040529259))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4207)
    AND_4.Add(FlagEnabled(4207))
    AND_4.Add(FlagEnabled(1040549205))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4208)
    AND_5.Add(FlagEnabled(4208))
    AND_5.Add(FlagEnabled(11009555))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4209)
    AND_6.Add(FlagEnabled(4209))
    AND_6.Add(FlagEnabled(9116))
    AND_6.Add(FlagDisabled(1051569361))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4210)
    AND_7.Add(FlagEnabled(4209))
    AND_7.Add(FlagEnabled(9116))
    AND_7.Add(FlagEnabled(1051569361))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(4205, 4217))
    EnableNetworkFlag(4211)
    AND_8.Add(FlagDisabled(1051569362))
    AND_8.Add(FlagDisabled(11059207))
    SkipLinesIfConditionTrue(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(4200, 4203))
    EnableNetworkFlag(4203)
    
    MAIN.Await(FlagEnabled(4218))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4259)
def Event_4259():
    """Event 4259"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4258)
    SkipLinesIfFlagRangeAllDisabled(3, (4240, 4243))
    AND_1.Add(FlagEnabled(4241))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableNetworkFlag(4240)
    SkipLinesIfFlagRangeAnyEnabled(2, (4245, 4257))
    DisableNetworkConnectedFlagRange(flag_range=(4245, 4257))
    EnableNetworkFlag(4245)
    GotoIfFlagDisabled(Label.L0, flag=4240)
    AND_2.Add(FlagEnabled(4245))
    AND_2.Add(FlagEnabled(11109957))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4245, 4257))
    EnableNetworkFlag(4246)
    AND_3.Add(FlagEnabled(4246))
    AND_3.Add(FlagEnabled(35009306))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4245, 4257))
    EnableNetworkFlag(4247)
    EnableNetworkFlag(35009317)
    EnableNetworkFlag(35009318)
    AND_4.Add(FlagEnabled(4247))
    AND_4.Add(FlagEnabled(1045520180))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4245, 4257))
    EnableNetworkFlag(4248)
    DisableNetworkFlag(35009317)
    DisableNetworkFlag(35009318)
    AND_5.Add(FlagEnabled(4248))
    AND_5.Add(FlagEnabled(11109959))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4245, 4257))
    EnableNetworkFlag(4249)
    AND_6.Add(FlagEnabled(4249))
    AND_6.Add(FlagEnabled(35009326))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(4245, 4257))
    EnableNetworkFlag(4251)
    
    MAIN.Await(FlagEnabled(4258))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(4239)
def Event_4239():
    """Event 4239"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(4238)
    SkipLinesIfFlagRangeAnyEnabled(2, (4220, 4223))
    DisableNetworkConnectedFlagRange(flag_range=(4220, 4223))
    EnableNetworkFlag(4220)
    AND_1.Add(FlagEnabled(4221))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4220, 4223))
    EnableNetworkFlag(4220)
    SkipLinesIfFlagRangeAnyEnabled(2, (4225, 4237))
    DisableNetworkConnectedFlagRange(flag_range=(4225, 4237))
    EnableNetworkFlag(4225)
    AND_8.Add(FlagEnabled(11109921))
    AND_8.Add(FlagEnabled(4228))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(4220, 4223))
    EnableNetworkFlag(4220)
    GotoIfFlagDisabled(Label.L0, flag=4220)
    AND_13.Add(FlagRangeAnyEnabled(flag_range=(4225, 4227)))
    AND_13.Add(FlagEnabled(110))
    AND_15.Add(not AND_13)
    AND_14.Add(FlagEnabled(4228))
    AND_14.Add(FlagEnabled(9116))
    AND_14.Add(FlagDisabled(11109921))
    AND_15.Add(not AND_14)
    SkipLinesIfConditionTrue(3, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(4220, 4223))
    EnableNetworkFlag(4223)
    Goto(Label.L0)
    AND_10.Add(FlagEnabled(4225))
    AND_10.Add(FlagEnabled(10009706))
    SkipLinesIfConditionFalse(1, AND_10)
    EnableNetworkFlag(10009709)
    AND_2.Add(FlagEnabled(4225))
    OR_2.Add(FlagEnabled(9101))
    OR_2.Add(FlagEnabled(1034509305))
    AND_2.Add(OR_2)
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(4225, 4237))
    EnableNetworkFlag(4226)
    DisableNetworkFlag(10009709)
    AND_3.Add(FlagEnabled(4226))
    AND_3.Add(FlagEnabled(11109909))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(4225, 4237))
    EnableNetworkFlag(4227)
    AND_11.Add(FlagEnabled(4227))
    AND_11.Add(FlagEnabled(1034429205))
    SkipLinesIfConditionFalse(1, AND_11)
    EnableNetworkFlag(1034429209)
    AND_4.Add(FlagEnabled(4227))
    AND_4.Add(FlagEnabled(1035420800))
    AND_4.Add(FlagEnabled(1034429205))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(4225, 4237))
    EnableNetworkFlag(4228)
    AND_5.Add(FlagEnabled(4228))
    AND_5.Add(FlagEnabled(9101))
    AND_5.Add(FlagEnabled(10009722))
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(4225, 4237))
    EnableNetworkFlag(4229)
    EnableNetworkFlag(10009719)
    AND_6.Add(FlagEnabled(4228))
    AND_6.Add(FlagEnabled(11109919))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(4225, 4237))
    EnableNetworkFlag(4230)
    
    MAIN.Await(FlagEnabled(4238))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(3839)
def Event_3839():
    """Event 3839"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(3838)
    SkipLinesIfFlagRangeAnyEnabled(2, (3820, 3823))
    DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
    EnableNetworkFlag(3820)
    if FlagEnabled(3823):
        DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
        EnableNetworkFlag(3821)
    AND_15.Add(FlagEnabled(3820))
    AND_15.Add(FlagEnabled(3822))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
    EnableNetworkFlag(3822)
    AND_1.Add(FlagEnabled(3821))
    AND_1.Add(FlagEnabled(3000))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
    EnableNetworkFlag(3820)
    SkipLinesIfFlagRangeAnyEnabled(2, (3825, 3829))
    DisableNetworkConnectedFlagRange(flag_range=(3825, 3829))
    EnableNetworkFlag(3825)
    GotoIfFlagDisabled(Label.L0, flag=3820)
    AND_6.Add(FlagEnabled(3825))
    AND_6.Add(FlagEnabled(1039449258))
    OR_6.Add(FlagEnabled(1043399313))
    OR_6.Add(FlagEnabled(3663))
    AND_6.Add(OR_6)
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(3825, 3829))
    EnableNetworkFlag(3826)
    AND_7.Add(FlagEnabled(3826))
    AND_7.Add(FlagEnabled(1039449278))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(3825, 3829))
    EnableNetworkFlag(3827)
    AND_8.Add(FlagEnabled(3827))
    AND_8.Add(FlagEnabled(3443))
    AND_8.Add(FlagEnabled(1039449270))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(3825, 3829))
    EnableNetworkFlag(3828)
    if FlagEnabled(1039449285):
        EnableNetworkFlag(1039449296)
    AND_9.Add(FlagEnabled(1039449291))
    SkipLinesIfConditionFalse(2, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(3825, 3829))
    EnableNetworkFlag(3829)
    
    MAIN.Await(FlagEnabled(3838))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@ContinueOnRest(60701)
def Event_60701(_, flag: uint, flag_1: uint):
    """Event 60701"""
    GotoIfPlayerNotInOwnWorld(Label.L15)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    AND_15.Add(FlagEnabled(6000))
    AND_15.Add(FlagDisabled(6000))
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    ReplanAI(0)


@ContinueOnRest(9930)
def Event_9930(_, flag: uint, flag_1: uint, gesture_param_id: int):
    """Event 9930"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(flag_1):
        AwardGesture(gesture_param_id=gesture_param_id)
        EnableFlag(flag_1)
    DisableFlag(flag)


@ContinueOnRest(9940)
def Event_9940():
    """Event 9940"""
    MAIN.Await(FlagEnabled(9992))
    
    EnableFlag(82000)
    EnableFlag(82010)
    EnableFlag(82011)
    EnableFlag(82012)
    EnableFlag(82020)
    EnableFlag(82021)
    EnableFlag(82022)
    EnableFlag(82030)
    EnableFlag(82031)
    EnableFlag(82032)
    EnableFlag(82040)
    EnableFlag(82041)
    EnableFlag(82050)
    EnableFlag(82051)
    EnableFlag(82052)
    EnableFlag(82060)
    EnableFlag(82061)
    EnableFlag(82070)
    EnableFlag(82071)
    EnableFlag(82080)
    EnableFlag(82081)


@ContinueOnRest(9941)
def Event_9941():
    """Event 9941"""
    MAIN.Await(FlagEnabled(9993))
    
    EnableFlagRange((10000000, 10000004))
    EnableFlagRange((11000000, 11000001))
    EnableFlagRange((11000003, 11000007))
    EnableFlagRange((12010000, 12010003))
    EnableFlagRange((12020000, 12020004))
    EnableFlagRange((12030000, 12030001))
    EnableFlagRange((12040000, 12040001))
    EnableFlagRange((13000000, 13000001))
    EnableFlagRange((14000000, 14000003))
    EnableFlagRange((15000000, 15000004))
    EnableFlagRange((16000000, 16000004))
    EnableFlagRange((18000000, 16000001))
    EnableFlagRange((34120000, 34120001))
    EnableFlagRange((35000000, 35000003))
    EnableFlagRange((39200000, 39200001))
    EnableFlag(30000000)
    EnableFlag(30010000)
    EnableFlag(30020000)
    EnableFlag(30030000)
    EnableFlag(30040000)
    EnableFlag(30050000)
    EnableFlag(30060000)
    EnableFlag(30070000)
    EnableFlag(30080000)
    EnableFlag(30090000)
    EnableFlag(30100000)
    EnableFlag(30110000)
    EnableFlag(30120000)
    EnableFlag(30130000)
    EnableFlag(30140000)
    EnableFlag(30150000)
    EnableFlag(30160000)
    EnableFlag(30170000)
    EnableFlag(30180000)
    EnableFlag(30190000)
    EnableFlag(1042360000)
    EnableFlag(1042370000)
    EnableFlag(1042380000)
    EnableFlag(1045380000)
    EnableFlag(1045350000)
    EnableFlag(1044350000)
    EnableFlag(1041360000)
    EnableFlag(1043340000)
    EnableFlag(1041330000)
    EnableFlag(1043310000)
    EnableFlag(1044330000)
    EnableFlag(1044330001)
    EnableFlag(1039400000)
    EnableFlag(1035420000)
    EnableFlag(1039420000)
    EnableFlag(1035440000)
    EnableFlag(1037440000)
    EnableFlag(1033460000)
    EnableFlag(1038480000)
    EnableFlag(1036490000)
    EnableFlag(1036490001)
    EnableFlag(1036410000)
    EnableFlag(1038510000)
    EnableFlag(1042540000)
    EnableFlag(1043500000)
    EnableFlag(1036540000)
    EnableFlag(1037520000)
    EnableFlagRange((1099000000, 1099000015))
    EnableFlagRange((1099000190, 1099000195))
    
    MAIN.Await(FlagDisabled(9991))
    
    DisableFlagRange((10000000, 10000004))
    DisableFlagRange((11000000, 11000001))
    DisableFlagRange((11000003, 11000007))
    DisableFlagRange((12010000, 12010003))
    DisableFlagRange((12020000, 12020004))
    DisableFlagRange((12030000, 12030001))
    DisableFlagRange((12040000, 12040001))
    DisableFlagRange((13000000, 13000001))
    DisableFlagRange((14000000, 14000003))
    DisableFlagRange((15000000, 15000004))
    DisableFlagRange((16000000, 16000004))
    DisableFlagRange((18000000, 16000001))
    DisableFlagRange((35000000, 35000003))
    DisableFlagRange((39200000, 39200001))
    DisableFlagRange((1099000000, 1099000015))
    DisableFlagRange((1099000190, 1099000195))
    DisableFlag(30000000)
    DisableFlag(30000001)
    DisableFlag(30000002)
    DisableFlag(30000003)
    DisableFlag(30000004)
    DisableFlag(30050000)
    DisableFlag(30060000)
    DisableFlag(30070000)
    DisableFlag(30080000)
    DisableFlag(30090000)
    DisableFlag(30100000)
    DisableFlag(30110000)
    DisableFlag(30120000)
    DisableFlag(30130000)
    DisableFlag(30140000)
    DisableFlag(30150000)
    DisableFlag(30160000)
    DisableFlag(30170000)
    DisableFlag(30180000)
    DisableFlag(30190000)
    DisableFlag(1042360000)
    DisableFlag(1042370000)
    DisableFlag(1042380000)
    DisableFlag(1045380000)
    DisableFlag(1045350000)
    DisableFlag(1044350000)
    DisableFlag(1041360000)
    DisableFlag(1043340000)
    DisableFlag(1041330000)
    DisableFlag(1043310000)
    DisableFlag(1044330000)
    DisableFlag(1044330001)
    DisableFlag(1039400000)
    DisableFlag(1035420000)
    DisableFlag(1039420000)
    DisableFlag(1035440000)
    DisableFlag(1037440000)
    DisableFlag(1033460000)
    DisableFlag(1038480000)
    DisableFlag(1036490000)
    DisableFlag(1036490001)
    DisableFlag(1036410000)
    DisableFlag(1038510000)
    DisableFlag(1042540000)
    DisableFlag(1043500000)
    DisableFlag(1036540000)
    DisableFlag(1037520000)
    Restart()


@ContinueOnRest(9943)
def Event_9943():
    """Event 9943"""
    MAIN.Await(FlagEnabled(9993))
    
    AwardItemLot(100400, host_only=True)


@ContinueOnRest(9945)
def Event_9945():
    """Event 9945"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9995))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerInOwnWorld(Label.L1)
    Move(
        20000,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=260,
        set_draw_parent=PLAYER,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(2.4000000953674316)
    if PlayerInOwnWorld():
        Wait(0.6000000238418579)
    Restart()


@ContinueOnRest(9946)
def Event_9946(_, flag: uint, flag_1: uint):
    """Event 9946"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag)


@ContinueOnRest(9950)
def Event_9950(_, flag: uint, flag_1: uint):
    """Event 9950"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
