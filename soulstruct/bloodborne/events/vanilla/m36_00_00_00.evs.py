"""
Fishing Hamlet

linked:
76

strings:
0: ボス_撃破
12: PC情報_ボス撃破_ラスボス
42: ボス_戦闘開始
58: ボス戦_撃破時間
76: N:\\SPRJ\\data\\Param\\event\\common.emevd
152: 
154: 
156: 
158: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=65, args=(3600950, 3601950, 999, 13607800))
    RunEvent(7000, slot=66, args=(3600951, 3601951, 999, 13607820))
    RunEvent(7000, slot=67, args=(3600952, 3601952, 13601800, 13607840))
    RunEvent(7100, slot=65, args=(73600200, 3601950))
    RunEvent(7100, slot=66, args=(73600201, 3601951))
    RunEvent(7100, slot=67, args=(73600202, 3601952))
    RunEvent(7200, slot=65, args=(73600100, 3601950, 2102953))
    RunEvent(7200, slot=66, args=(73600101, 3601951, 2102953))
    RunEvent(7200, slot=67, args=(73600102, 3601952, 2102953))
    RunEvent(7300, slot=65, args=(72103600, 3601950))
    RunEvent(7300, slot=66, args=(72103601, 3601951))
    RunEvent(7300, slot=67, args=(72103602, 3601952))
    Event_13604700(0, character=3600790, flag=13604701, flag_1=13604711, flag_2=3600, flag_3=999)
    Event_13604700(5, character=3600791, flag=13604702, flag_1=13604712, flag_2=3600, flag_3=999)
    Event_13604710(0, character=3600790, flag=13604701, flag_1=13604711, flag_2=13604721)
    Event_13604710(5, character=3600791, flag=13604702, flag_1=13604712, flag_2=13604722)
    Event_13604720(0, character=3600790, flag=13604701, flag_1=13604711, flag_2=13604721)
    Event_13604720(5, character=3600791, flag=13604702, flag_1=13604712, flag_2=13604722)
    Event_13604730(
        0,
        character=3600790,
        flag=13604701,
        flag_1=13604711,
        flag_2=3600,
        flag_3=13604810,
        flag_4=999,
        flag_5=999,
        flag_6=13604712,
    )
    Event_13604730(
        5,
        character=3600791,
        flag=13604702,
        flag_1=13604712,
        flag_2=3600,
        flag_3=13604810,
        flag_4=999,
        flag_5=999,
        flag_6=13604711,
    )
    Event_13604740()
    Event_13604742()
    Event_13600000()
    Event_13600010()
    Event_13601090()
    Event_13601100()
    Event_13601101()
    Event_13601102()
    Event_13601103()
    Event_13601104()
    Event_13601105()
    Event_13601200(0, obj=3601200, obj_act_id=13604200, animation_id=1, obj_act_id_1=10)
    Event_13601200(1, obj=3601201, obj_act_id=13604201, animation_id=1, obj_act_id_1=10)
    Event_13601210(0, action_button_id=7030, entity=3601200, flag=13601200)
    Event_13601210(1, action_button_id=7030, entity=3601201, flag=13601201)
    RegisterLadder(start_climbing_flag=13601300, stop_climbing_flag=13601301, obj=3601300)
    RegisterLadder(start_climbing_flag=13601302, stop_climbing_flag=13601303, obj=3601301)
    RegisterLadder(start_climbing_flag=13601304, stop_climbing_flag=13601305, obj=3601302)
    RegisterLadder(start_climbing_flag=13601306, stop_climbing_flag=13601307, obj=3601303)
    RegisterLadder(start_climbing_flag=13601308, stop_climbing_flag=13601309, obj=3601304)
    Event_13601312()
    Event_13601140(0, entity=3601110, collision=3604110)
    Event_13601140(1, entity=3601111, collision=3604111)
    Event_13601140(2, entity=3601112, collision=3604112)
    Event_13601140(3, entity=3601113, collision=3604113)
    Event_13601400()
    Event_13604400(0, obj=3601400)
    Event_13604400(1, obj=3601401)
    Event_13604400(2, obj=3601402)
    Event_13604400(3, obj=3601403)
    Event_13604400(4, obj=3601404)
    Event_13604400(5, obj=3601405)
    Event_13604400(6, obj=3601406)
    Event_13604400(7, obj=3601407)
    Event_13604400(8, obj=3601408)
    Event_13604400(9, obj=3601409)
    Event_13604400(10, obj=3601410)
    Event_13604400(11, obj=3601411)
    Event_13604400(12, obj=3601412)
    Event_13604400(13, obj=3601413)
    Event_13604400(20, obj=3601420)
    Event_13604400(21, obj=3601421)
    Event_13604400(22, obj=3601422)
    Event_13604400(23, obj=3601423)
    Event_13604400(24, obj=3601424)
    Event_13604400(25, obj=3601425)
    Event_13604400(26, obj=3601426)
    Event_13604400(27, obj=3601427)
    Event_13604400(28, obj=3601428)
    Event_13604400(29, obj=3601429)
    Event_13604400(30, obj=3601430)
    Event_13604400(31, obj=3601431)
    Event_13604400(40, obj=3601440)
    Event_13604400(41, obj=3601441)
    Event_13604400(42, obj=3601442)
    Event_13604400(43, obj=3601443)
    Event_13604400(44, obj=3601444)
    Event_13604400(45, obj=3601445)
    Event_13604400(46, obj=3601446)
    Event_13604400(47, obj=3601447)
    Event_13604400(50, obj=3601450)
    Event_13604400(51, obj=3601451)
    Event_13604400(52, obj=3601452)
    Event_13604400(53, obj=3601453)
    Event_13604400(54, obj=3601454)
    Event_13604400(55, obj=3601455)
    Event_13604400(56, obj=3601456)
    Event_13604400(57, obj=3601457)
    Event_13604400(60, obj=3601460)
    Event_13604400(61, obj=3601461)
    Event_13604400(62, obj=3601462)
    Event_13604400(63, obj=3601463)
    Event_13604400(64, obj=3601464)
    Event_13604400(65, obj=3601465)
    Event_13604400(66, obj=3601466)
    Event_13604400(67, obj=3601467)
    Event_13601800()
    Event_13604811()
    Event_13601801()
    Event_13604800()
    Event_13604801()
    Event_13604802()
    Event_13604803()
    Event_13604805()
    Event_13604806()
    Event_13604807()
    Event_13604820()
    Event_13604830()
    Event_13604840()
    Event_13604850()
    Event_13601802()
    Event_13601803()
    Event_13601804()
    Event_13605200(0, character=3600200, region=3602200, region_1=0, patrol_information_id=3603200, seconds=0.0, left=0)
    Event_13605200(1, character=3600202, region=3602202, region_1=0, patrol_information_id=3603202, seconds=0.0, left=0)
    Event_13605200(
        2,
        character=3600203,
        region=3602202,
        region_1=3602203,
        patrol_information_id=3603203,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        3,
        character=3600204,
        region=3602202,
        region_1=3602203,
        patrol_information_id=3603204,
        seconds=0.0,
        left=0,
    )
    Event_13605200(4, character=3600208, region=3602208, region_1=0, patrol_information_id=3603208, seconds=0.0, left=0)
    Event_13605200(5, character=3600209, region=3602208, region_1=0, patrol_information_id=3603209, seconds=0.0, left=0)
    Event_13605200(6, character=3600210, region=3602210, region_1=0, patrol_information_id=3603210, seconds=0.0, left=0)
    Event_13605200(7, character=3600300, region=3602300, region_1=0, patrol_information_id=3603300, seconds=0.0, left=0)
    Event_13605200(8, character=3600213, region=3602213, region_1=0, patrol_information_id=3603213, seconds=0.0, left=0)
    Event_13605200(9, character=3600214, region=3602213, region_1=0, patrol_information_id=3603214, seconds=0.0, left=0)
    Event_13605200(
        10,
        character=3600217,
        region=3602215,
        region_1=0,
        patrol_information_id=3603217,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        11,
        character=3600229,
        region=3602229,
        region_1=0,
        patrol_information_id=3603229,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        12,
        character=3600231,
        region=3602231,
        region_1=3602232,
        patrol_information_id=3603231,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        13,
        character=3600232,
        region=3602231,
        region_1=3602232,
        patrol_information_id=3603232,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        14,
        character=3600233,
        region=3602231,
        region_1=3602232,
        patrol_information_id=3603233,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        15,
        character=3600610,
        region=3602610,
        region_1=0,
        patrol_information_id=3603610,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        16,
        character=3600611,
        region=3602231,
        region_1=3602232,
        patrol_information_id=3603611,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        17,
        character=3600301,
        region=3602301,
        region_1=0,
        patrol_information_id=3603301,
        seconds=0.0,
        left=1,
    )
    Event_13605200(
        18,
        character=3600310,
        region=3602310,
        region_1=0,
        patrol_information_id=3603310,
        seconds=0.0,
        left=1,
    )
    Event_13605200(
        19,
        character=3600700,
        region=3602700,
        region_1=0,
        patrol_information_id=3603700,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        20,
        character=3600710,
        region=3602710,
        region_1=0,
        patrol_information_id=3603710,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        21,
        character=3600251,
        region=3602251,
        region_1=0,
        patrol_information_id=3603251,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        23,
        character=3600253,
        region=3602252,
        region_1=0,
        patrol_information_id=3603253,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        25,
        character=3600314,
        region=3602314,
        region_1=0,
        patrol_information_id=3603314,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        26,
        character=3600455,
        region=3602455,
        region_1=0,
        patrol_information_id=3603455,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        27,
        character=3600456,
        region=3602455,
        region_1=0,
        patrol_information_id=3603456,
        seconds=1.0,
        left=1,
    )
    Event_13605200(
        28,
        character=3600474,
        region=3602474,
        region_1=0,
        patrol_information_id=3603474,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        29,
        character=3600475,
        region=3602474,
        region_1=0,
        patrol_information_id=3603475,
        seconds=1.0,
        left=1,
    )
    Event_13605200(
        30,
        character=3600302,
        region=3602302,
        region_1=0,
        patrol_information_id=3603302,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        31,
        character=3600312,
        region=3602312,
        region_1=0,
        patrol_information_id=3603312,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        32,
        character=3600470,
        region=3602470,
        region_1=0,
        patrol_information_id=3603470,
        seconds=0.0,
        left=1,
    )
    Event_13605200(
        33,
        character=3600500,
        region=3602470,
        region_1=0,
        patrol_information_id=3603500,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        34,
        character=3600501,
        region=3602501,
        region_1=0,
        patrol_information_id=3603501,
        seconds=0.0,
        left=0,
    )
    Event_13605200(
        35,
        character=3600920,
        region=3602940,
        region_1=0,
        patrol_information_id=3603920,
        seconds=0.0,
        left=0,
    )
    Event_13605400(
        0,
        character=3600206,
        animation_id=7004,
        ai_param_id=404002,
        animation=7005,
        ai_param_id_1=404002,
        region=3602206,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        1,
        character=3600211,
        animation_id=7012,
        ai_param_id=404000,
        animation=7013,
        ai_param_id_1=404000,
        region=3602211,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        2,
        character=3600218,
        animation_id=0,
        ai_param_id=404011,
        animation=3005,
        ai_param_id_1=404010,
        region=3602218,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        3,
        character=3600222,
        animation_id=7016,
        ai_param_id=404031,
        animation=7017,
        ai_param_id_1=404030,
        region=3602222,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        4,
        character=3600230,
        animation_id=7004,
        ai_param_id=404000,
        animation=7005,
        ai_param_id_1=404000,
        region=3602230,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        5,
        character=3600239,
        animation_id=7012,
        ai_param_id=404008,
        animation=7013,
        ai_param_id_1=404008,
        region=3602240,
        min_seconds=0.75,
        max_seconds=0.75,
    )
    Event_13605400(
        6,
        character=3600240,
        animation_id=7012,
        ai_param_id=404004,
        animation=7013,
        ai_param_id_1=404004,
        region=3602240,
        min_seconds=0.25,
        max_seconds=0.25,
    )
    Event_13605400(
        7,
        character=3600241,
        animation_id=7012,
        ai_param_id=404008,
        animation=7013,
        ai_param_id_1=404008,
        region=3602240,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        8,
        character=3600242,
        animation_id=7012,
        ai_param_id=404004,
        animation=7013,
        ai_param_id_1=404004,
        region=3602240,
        min_seconds=0.5,
        max_seconds=0.5,
    )
    Event_13605400(
        9,
        character=3600244,
        animation_id=7014,
        ai_param_id=404014,
        animation=7015,
        ai_param_id_1=404014,
        region=3602244,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        10,
        character=3600245,
        animation_id=0,
        ai_param_id=404035,
        animation=3026,
        ai_param_id_1=404034,
        region=3602245,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        11,
        character=3600246,
        animation_id=7018,
        ai_param_id=404034,
        animation=7019,
        ai_param_id_1=404034,
        region=3602246,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        12,
        character=3600247,
        animation_id=7018,
        ai_param_id=404014,
        animation=7019,
        ai_param_id_1=404014,
        region=3602246,
        min_seconds=0.5,
        max_seconds=0.5,
    )
    Event_13605400(
        13,
        character=3600260,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        region=3602260,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        14,
        character=3600261,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        region=3602261,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        15,
        character=3600262,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        region=3602262,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        16,
        character=3600265,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        region=3602265,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        17,
        character=3600400,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602400,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        18,
        character=3600401,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602400,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        19,
        character=3600402,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602400,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        20,
        character=3600403,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602400,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        21,
        character=3600404,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602400,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        22,
        character=3600405,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602400,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        25,
        character=3600408,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602408,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        26,
        character=3600409,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602408,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        27,
        character=3600410,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602408,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        28,
        character=3600411,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602408,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13605400(
        29,
        character=3600412,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602412,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        30,
        character=3600413,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602412,
        min_seconds=1.0,
        max_seconds=1.0,
    )
    Event_13605400(
        33,
        character=3600416,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602416,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        34,
        character=3600417,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602416,
        min_seconds=1.0,
        max_seconds=1.0,
    )
    Event_13605400(
        35,
        character=3600418,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602416,
        min_seconds=0.5,
        max_seconds=0.5,
    )
    Event_13605400(
        36,
        character=3600419,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602419,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        37,
        character=3600424,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602424,
        min_seconds=0.5,
        max_seconds=0.5,
    )
    Event_13605400(
        38,
        character=3600425,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602424,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        39,
        character=3600426,
        animation_id=7010,
        ai_param_id=407012,
        animation=7001,
        ai_param_id_1=407010,
        region=3602424,
        min_seconds=1.0,
        max_seconds=1.0,
    )
    Event_13605400(
        40,
        character=3600440,
        animation_id=7010,
        ai_param_id=407022,
        animation=7001,
        ai_param_id_1=407020,
        region=3602440,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605400(
        41,
        character=3600441,
        animation_id=7010,
        ai_param_id=407022,
        animation=3001,
        ai_param_id_1=407020,
        region=3602440,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605480(
        0,
        character=3600223,
        animation_id=7008,
        ai_param_id=404032,
        animation=7009,
        ai_param_id_1=404030,
        region=3602223,
        seconds=0.0,
        frames=33,
    )
    Event_13605480(
        1,
        character=3600476,
        animation_id=7012,
        ai_param_id=407000,
        animation=7013,
        ai_param_id_1=407000,
        region=3602476,
        seconds=0.0,
        frames=30,
    )
    Event_13605480(
        2,
        character=3600477,
        animation_id=7014,
        ai_param_id=407000,
        animation=7015,
        ai_param_id_1=407000,
        region=3602476,
        seconds=0.5,
        frames=30,
    )
    Event_13605480(
        3,
        character=3600478,
        animation_id=7016,
        ai_param_id=407000,
        animation=7017,
        ai_param_id_1=407000,
        region=3602478,
        seconds=0.0,
        frames=30,
    )
    Event_13605490(
        0,
        character=3600313,
        animation_id=9000,
        ai_param_id=405003,
        animation=9060,
        ai_param_id_1=405003,
        character_1=3600314,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605490(
        1,
        character=3600266,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        character_1=3600314,
        min_seconds=0.5,
        max_seconds=0.5,
    )
    Event_13605490(
        2,
        character=3600267,
        animation_id=7014,
        ai_param_id=404018,
        animation=7015,
        ai_param_id_1=404019,
        character_1=3600314,
        min_seconds=1.0,
        max_seconds=1.0,
    )
    Event_13605490(
        3,
        character=3600263,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        character_1=3600265,
        min_seconds=0.5,
        max_seconds=0.5,
    )
    Event_13605490(
        4,
        character=3600264,
        animation_id=7012,
        ai_param_id=404018,
        animation=7013,
        ai_param_id_1=404019,
        character_1=3600265,
        min_seconds=1.0,
        max_seconds=1.0,
    )
    Event_13605500(
        1,
        character=3600207,
        animation_id=7006,
        ai_param_id=404002,
        animation=7007,
        ai_param_id_1=404002,
        region=3602206,
        min_seconds=4.0,
        max_seconds=4.0,
    )
    Event_13605500(
        2,
        character=3600212,
        animation_id=7006,
        ai_param_id=404016,
        animation=7007,
        ai_param_id_1=404010,
        region=3602211,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605500(
        3,
        character=3600216,
        animation_id=7006,
        ai_param_id=404003,
        animation=7007,
        ai_param_id_1=404000,
        region=3602215,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13605520(1, character=3600310, region=3602310, ai_param_id=405001, ai_param_id_1=405000)
    Event_13605540(0, character=3600210, region=0, radius=8.0, ai_param_id=404040, ai_param_id_1=404000)
    Event_13605540(1, character=3600300, region=0, radius=8.0, ai_param_id=406001, ai_param_id_1=406000)
    Event_13605540(2, character=3600500, region=3602470, radius=4.0, ai_param_id=256901, ai_param_id_1=256900)
    Event_13605540(3, character=3600501, region=3602470, radius=4.0, ai_param_id=256901, ai_param_id_1=256900)
    Event_13605540(4, character=3600218, region=0, radius=1.0, ai_param_id=404011, ai_param_id_1=404010)
    Event_13605540(5, character=3600220, region=0, radius=4.0, ai_param_id=404011, ai_param_id_1=404010)
    Event_13605540(6, character=3600221, region=0, radius=4.0, ai_param_id=404011, ai_param_id_1=404010)
    Event_13605560(0, character=3600331, region=3602331, radius=4.0)
    Event_13605600(0, character__set_draw_parent=3600500, character=3600510)
    Event_13605600(1, character__set_draw_parent=3600501, character=3600511)
    Event_13605605()
    Event_13605606()
    Event_13605799()
    Event_13605720(0, character=3600206)
    Event_13605720(1, character=3600314)
    Event_13605740(0, character=3600215, region=3602215, region_1=3600720, radius=2.0)
    Event_13605740(1, character=3600219, region=3602218, region_1=3600721, radius=2.0)
    Event_13605740(2, character=3600250, region=3602250, region_1=3600722, radius=2.0)
    Event_13605750()
    Event_13605751()
    Event_13605752()
    Event_13605760()
    Event_13605761()
    Event_13605900(0, flag=13605950, flag_1=13605960, flag_2=13605970, region=3602900, region_1=0, flag_3=13600995)
    Event_13605900(1, flag=13605951, flag_1=13605961, flag_2=13605971, region=3602910, region_1=3602911, flag_3=6001)
    Event_13605900(2, flag=13605952, flag_1=13605962, flag_2=13605972, region=3602920, region_1=0, flag_3=6001)
    Event_13605910(0, flag=13605950, flag_1=13605960, flag_2=13605970, region=3602902, region_1=0)
    Event_13605910(1, flag=13605951, flag_1=13605961, flag_2=13605971, region=3602912, region_1=3602913)
    Event_13605910(2, flag=13605952, flag_1=13605962, flag_2=13605972, region=3602922, region_1=0)
    Event_13605920(
        0,
        character=3600900,
        flag=13605960,
        flag_1=13605970,
        region=3602904,
        region_1=3602905,
        flag_2=13605950,
        flag_3=13605980,
        destination=3602906,
    )
    Event_13605921(
        0,
        character=3600901,
        flag=13605961,
        flag_1=13605971,
        region=3602914,
        region_1=3602915,
        flag_2=13605951,
        flag_3=13605981,
        destination=3602916,
    )
    Event_13605920(
        2,
        character=3600902,
        flag=13605962,
        flag_1=13605972,
        region=3602924,
        region_1=0,
        flag_2=13605952,
        flag_3=13605982,
        destination=3602926,
    )
    Event_13605930(
        0,
        character=3600900,
        flag=13605960,
        flag_1=13605970,
        region=3602908,
        region_1=3602909,
        flag_2=13605980,
    )
    Event_13605930(
        1,
        character=3600901,
        flag=13605961,
        flag_1=13605971,
        region=3602918,
        region_1=3602909,
        flag_2=13605981,
    )
    Event_13605930(2, character=3600902, flag=13605962, flag_1=13605972, region=3602928, region_1=0, flag_2=13605982)
    Event_13605940(0, character=3600900, flag=13605960, flag_1=13605970, item_lot_param_id=43730, character_1=3600910)
    Event_13605940(1, character=3600901, flag=13605961, flag_1=13605971, item_lot_param_id=43740, character_1=3600911)
    Event_13605940(2, character=3600902, flag=13605962, flag_1=13605972, item_lot_param_id=43720, character_1=3600912)
    Event_13600995()
    Event_13600942(0, min_seconds=6.0, max_seconds=10.0)
    Event_13600943(0, flag=73600300, item_lot_param_id=43600)
    Event_13600944()
    Event_13600951(0, character=3600905, flag=73600520, flag_1=1723)
    Event_13600952(0, character=3600905, flag=1723, flag_1=73600530)
    Event_13600953(0, character=3600905)
    Event_13600955()
    Event_13600956(0, character=3600905, flag=1723, flag_1=73600521)
    Event_13600900(1, character=3600905, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1713)
    Event_13600954(0, 1713, 73600530, 43220)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13600940(0, character=3600920)
    Event_13600950(0, character=3600905)
    DisableGravity(3600201)
    DisableCharacterCollision(3600201)
    DisableGravity(3600207)
    DisableCharacterCollision(3600207)
    DisableGravity(3600212)
    DisableCharacterCollision(3600212)
    DisableGravity(3600216)
    DisableCharacterCollision(3600216)
    DisableHealthBar(3600330)
    DisableHealthBar(3600331)
    DisableHealthBar(3600332)


@RestartOnRest(13604700)
def Event_13604700(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 13604700"""
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag):
        return
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    AND_1.Add(Online())
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(InsideMap(game_map=FISHING_HAMLET))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(PlayerLevel() >= 30)
    if FlagEnabled(flag_3):
        AND_2.Add(ClientTypeCountComparison(
            client_type=ClientType.Coop,
            comparison_type=ComparisonType.GreaterThanOrEqual,
            value=1,
        ))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 9025))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(RandomTimeElapsed(min_seconds=10.0, max_seconds=10.0))
    
    if FlagEnabled(flag_3):
        DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    WaitFrames(frames=59)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(13604710)
def Event_13604710(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13604710"""
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(InsideMap(game_map=FISHING_HAMLET))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(RandomTimeElapsed(min_seconds=10.0, max_seconds=10.0))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    EnableFlag(flag_2)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest(13604720)
def Event_13604720(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13604720"""
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(ClientTypeCountComparison(
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    ))
    OR_1.Add(OutsideMap(game_map=FISHING_HAMLET))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RemoveSpecialEffect(PLAYER, 9020)
    RemoveSpecialEffect(character, 9100)
    ReplanAI(character)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(13604730)
def Event_13604730(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
    flag_6: int,
):
    """Event 13604730"""
    OR_15.Add(FlagEnabled(flag_1))
    OR_15.Add(FlagEnabled(flag_2))
    OR_15.Add(FlagEnabled(flag_3))
    if OR_15:
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_5))
    AND_2.Add(HealthRatio(character) == 0.0)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag_6))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    EnableFlag(flag_4)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@RestartOnRest(13604740)
def Event_13604740():
    """Event 13604740"""
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(PlayerStandingOnCollision(3604000))
    OR_1.Add(PlayerStandingOnCollision(3604001))
    OR_1.Add(PlayerStandingOnCollision(3604002))
    OR_1.Add(PlayerStandingOnCollision(3604003))
    OR_1.Add(PlayerStandingOnCollision(3604004))
    OR_1.Add(PlayerStandingOnCollision(3604005))
    OR_1.Add(PlayerStandingOnCollision(3604006))
    OR_1.Add(PlayerStandingOnCollision(3604007))
    OR_1.Add(PlayerStandingOnCollision(3604008))
    OR_1.Add(PlayerStandingOnCollision(3604009))
    OR_1.Add(PlayerStandingOnCollision(3604010))
    OR_1.Add(PlayerStandingOnCollision(3604011))
    OR_1.Add(PlayerStandingOnCollision(3604012))
    OR_1.Add(PlayerStandingOnCollision(3604013))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13604741)
    AND_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(PlayerStandingOnCollision(3604000))
    OR_2.Add(PlayerStandingOnCollision(3604001))
    OR_2.Add(PlayerStandingOnCollision(3604002))
    OR_2.Add(PlayerStandingOnCollision(3604003))
    OR_2.Add(PlayerStandingOnCollision(3604004))
    OR_2.Add(PlayerStandingOnCollision(3604005))
    OR_2.Add(PlayerStandingOnCollision(3604006))
    OR_2.Add(PlayerStandingOnCollision(3604007))
    OR_2.Add(PlayerStandingOnCollision(3604008))
    OR_2.Add(PlayerStandingOnCollision(3604009))
    OR_2.Add(PlayerStandingOnCollision(3604010))
    OR_2.Add(PlayerStandingOnCollision(3604011))
    OR_2.Add(PlayerStandingOnCollision(3604012))
    OR_2.Add(PlayerStandingOnCollision(3604013))
    AND_2.Add(not OR_2)
    
    MAIN.Await(AND_2)
    
    DisableFlag(13604741)
    Restart()


@RestartOnRest(13604742)
def Event_13604742():
    """Event 13604742"""
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(PlayerStandingOnCollision(3604020))
    OR_1.Add(PlayerStandingOnCollision(3604021))
    OR_1.Add(PlayerStandingOnCollision(3604022))
    OR_1.Add(PlayerStandingOnCollision(3604023))
    OR_1.Add(PlayerStandingOnCollision(3604024))
    OR_1.Add(PlayerStandingOnCollision(3604025))
    OR_1.Add(PlayerStandingOnCollision(3604026))
    OR_1.Add(PlayerStandingOnCollision(3604027))
    OR_1.Add(PlayerStandingOnCollision(3604028))
    OR_1.Add(PlayerStandingOnCollision(3604029))
    OR_1.Add(PlayerStandingOnCollision(3604030))
    OR_1.Add(PlayerStandingOnCollision(3604031))
    OR_1.Add(PlayerStandingOnCollision(3604032))
    OR_1.Add(PlayerStandingOnCollision(3604033))
    OR_1.Add(PlayerStandingOnCollision(3604034))
    OR_1.Add(PlayerStandingOnCollision(3604035))
    OR_1.Add(PlayerStandingOnCollision(3604110))
    OR_1.Add(PlayerStandingOnCollision(3604111))
    OR_1.Add(PlayerStandingOnCollision(3604112))
    OR_1.Add(PlayerStandingOnCollision(3604113))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13604743)
    AND_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(PlayerStandingOnCollision(3604020))
    OR_2.Add(PlayerStandingOnCollision(3604021))
    OR_2.Add(PlayerStandingOnCollision(3604022))
    OR_2.Add(PlayerStandingOnCollision(3604023))
    OR_2.Add(PlayerStandingOnCollision(3604024))
    OR_2.Add(PlayerStandingOnCollision(3604025))
    OR_2.Add(PlayerStandingOnCollision(3604026))
    OR_2.Add(PlayerStandingOnCollision(3604027))
    OR_2.Add(PlayerStandingOnCollision(3604028))
    OR_2.Add(PlayerStandingOnCollision(3604029))
    OR_2.Add(PlayerStandingOnCollision(3604030))
    OR_2.Add(PlayerStandingOnCollision(3604031))
    OR_2.Add(PlayerStandingOnCollision(3604032))
    OR_2.Add(PlayerStandingOnCollision(3604033))
    OR_2.Add(PlayerStandingOnCollision(3604034))
    OR_2.Add(PlayerStandingOnCollision(3604035))
    OR_2.Add(PlayerStandingOnCollision(3604110))
    OR_2.Add(PlayerStandingOnCollision(3604111))
    OR_2.Add(PlayerStandingOnCollision(3604112))
    OR_2.Add(PlayerStandingOnCollision(3604113))
    AND_2.Add(not OR_2)
    
    MAIN.Await(AND_2)
    
    DisableFlag(13604743)
    Restart()


@ContinueOnRest(13600000)
def Event_13600000():
    """Event 13600000"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    
    MAIN.Await(PlayerStandingOnCollision(3604002))
    
    RunEvent(9350, slot=0, args=(4,))


@ContinueOnRest(13600010)
def Event_13600010():
    """Event 13600010"""
    DisableNetworkSync()
    if FlagEnabled(13601803):
        return
    DisableSoundEvent(sound_id=3603001)
    OR_1.Add(PlayerStandingOnCollision(3604005))
    OR_1.Add(PlayerStandingOnCollision(3604007))
    OR_1.Add(PlayerStandingOnCollision(3604012))
    OR_1.Add(PlayerStandingOnCollision(3604021))
    OR_1.Add(PlayerStandingOnCollision(3604023))
    OR_1.Add(PlayerStandingOnCollision(3604026))
    OR_1.Add(PlayerStandingOnCollision(3604027))
    OR_1.Add(PlayerStandingOnCollision(3604028))
    OR_1.Add(PlayerStandingOnCollision(3604029))
    OR_1.Add(PlayerStandingOnCollision(3604030))
    OR_1.Add(PlayerStandingOnCollision(3604031))
    OR_1.Add(PlayerStandingOnCollision(3604032))
    OR_1.Add(PlayerStandingOnCollision(3604033))
    OR_1.Add(PlayerStandingOnCollision(3604034))
    OR_1.Add(PlayerStandingOnCollision(3604035))
    OR_1.Add(PlayerStandingOnCollision(3604060))
    
    MAIN.Await(OR_1)
    
    EnableSoundEvent(sound_id=3603001)
    OR_2.Add(PlayerStandingOnCollision(3604005))
    OR_2.Add(PlayerStandingOnCollision(3604007))
    OR_2.Add(PlayerStandingOnCollision(3604012))
    OR_2.Add(PlayerStandingOnCollision(3604021))
    OR_2.Add(PlayerStandingOnCollision(3604023))
    OR_2.Add(PlayerStandingOnCollision(3604026))
    OR_2.Add(PlayerStandingOnCollision(3604027))
    OR_2.Add(PlayerStandingOnCollision(3604028))
    OR_2.Add(PlayerStandingOnCollision(3604029))
    OR_2.Add(PlayerStandingOnCollision(3604030))
    OR_2.Add(PlayerStandingOnCollision(3604031))
    OR_2.Add(PlayerStandingOnCollision(3604032))
    OR_2.Add(PlayerStandingOnCollision(3604033))
    OR_2.Add(PlayerStandingOnCollision(3604034))
    OR_2.Add(PlayerStandingOnCollision(3604035))
    OR_2.Add(PlayerStandingOnCollision(3604060))
    
    MAIN.Await(not OR_2)
    
    Restart()


@ContinueOnRest(13601090)
def Event_13601090():
    """Event 13601090"""
    if FlagEnabled(9468):
        return
    DisableObject(3601090)
    
    MAIN.Await(FlagEnabled(9468))
    
    EnableObject(3601090)


@ContinueOnRest(13601100)
def Event_13601100():
    """Event 13601100"""
    if FlagEnabled(13604100):
        return
    GotoIfFlagEnabled(Label.L0, flag=13601108)
    EnableFlag(13601106)
    EnableFlag(13601107)
    EndOfAnimation(obj=3601100, animation_id=0)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(13601106))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    DisableFlag(13601107)
    EndOfAnimation(obj=3601100, animation_id=4)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13601107)
    EndOfAnimation(obj=3601100, animation_id=0)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)


@ContinueOnRest(13601101)
def Event_13601101():
    """Event 13601101"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(13601108))
    AND_1.Add(FlagEnabled(13604100))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(FlagEnabled(13601106))
    SkipLinesIfConditionTrue(2, AND_2)
    DisableFlag(13601107)
    SkipLines(1)
    EnableFlag(13601107)
    AND_3.Add(CharacterHuman(PLAYER))
    AND_3.Add(FlagEnabled(13601108))
    AND_3.Add(FlagDisabled(13604100))
    
    MAIN.Await(AND_3)
    
    Restart()


@ContinueOnRest(13601102)
def Event_13601102():
    """Event 13601102"""
    AND_3.Add(FlagEnabled(13604100))
    AND_3.Add(FlagEnabled(13601106))
    GotoIfConditionFalse(Label.L0, input_condition=AND_3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(obj=3601100, animation_id=6)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(13601108))
    AND_1.Add(FlagDisabled(13604100))
    AND_1.Add(FlagDisabled(13601106))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=3602102))
    OR_1.Add(ObjectActivated(obj_act_id=13604101))
    AND_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 13601107))
    AND_2.Add(FlagEnabled(13601107))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13604100)
    EnableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 5, wait_for_completion=True)
    ForceAnimation(3601100, 6, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(AllPlayersOutsideRegion(region=3602101))
    
    ForceAnimation(3601100, 7, wait_for_completion=True)
    DisableFlag(13604100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    Restart()


@ContinueOnRest(13601103)
def Event_13601103():
    """Event 13601103"""
    AND_3.Add(FlagEnabled(13604100))
    AND_3.Add(FlagDisabled(13601106))
    GotoIfConditionFalse(Label.L0, input_condition=AND_3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(obj=3601100, animation_id=2)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(13601108))
    AND_1.Add(FlagDisabled(13604100))
    AND_1.Add(FlagEnabled(13601106))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=3602101))
    OR_1.Add(ObjectActivated(obj_act_id=13604102))
    AND_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 13601107))
    AND_2.Add(FlagDisabled(13601107))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13604100)
    DisableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 1, wait_for_completion=True)
    ForceAnimation(3601100, 2, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(AllPlayersOutsideRegion(region=3602102))
    
    WaitFrames(frames=1)
    ForceAnimation(3601100, 3, wait_for_completion=True)
    DisableFlag(13604100)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Restart()


@ContinueOnRest(13601104)
def Event_13601104():
    """Event 13601104"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(13601108))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=3601101))
    AND_2.Add(FlagDisabled(13601108))
    AND_2.Add(ActionButtonParamActivated(action_button_id=7100, entity=3601102))
    AND_3.Add(FlagEnabled(13604100))
    AND_3.Add(ActionButtonParamActivated(action_button_id=7100, entity=3601101))
    AND_4.Add(FlagEnabled(13604100))
    AND_4.Add(ActionButtonParamActivated(action_button_id=7100, entity=3601102))
    AND_5.Add(FlagEnabled(13601106))
    AND_5.Add(ActionButtonParamActivated(action_button_id=7100, entity=3601101))
    AND_6.Add(FlagDisabled(13601106))
    AND_6.Add(ActionButtonParamActivated(action_button_id=7100, entity=3601102))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(13601105)
def Event_13601105():
    """Event 13601105"""
    if FlagEnabled(13601108):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3602100))
    
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    EnableFlag(13601108)


@ContinueOnRest(13601140)
def Event_13601140(_, entity: int, collision: int):
    """Event 13601140"""
    MAIN.Await(PlayerMovingOnCollision(collision))
    
    ForceAnimation(entity, 0, wait_for_completion=True)
    Restart()


@ContinueOnRest(13601200)
def Event_13601200(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 13601200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(0.0)


@ContinueOnRest(13601312)
def Event_13601312():
    """Event 13601312"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=3601305, animation_id=1)
    WaitFrames(frames=1)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3600000, entity=3601305))
    
    Move(PLAYER, destination=3601305, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 101330)
    ForceAnimation(3601305, 1, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)


@ContinueOnRest(13601210)
def Event_13601210(_, action_button_id: int, entity: int, flag: int):
    """Event 13601210"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    DisplayDialog(text=10010161, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(13601400)
def Event_13601400():
    """Event 13601400"""
    DisableNetworkSync()
    
    MAIN.Await(InsideMap(game_map=FISHING_HAMLET))
    
    DeleteVFX(3503120)


@RestartOnRest(13604400)
def Event_13604400(_, obj: int):
    """Event 13604400"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(obj)
    OR_1.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Fire))
    OR_1.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.NoType))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Magic))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Lightning))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Blunt))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Slash))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Thrust))
    AND_2.Add(OR_2)
    AND_2.Add(ObjectHealthValueComparison(obj, ComparisonType.LessThanOrEqual, value=999))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    ShootProjectile(
        owner_entity=3600799,
        source_entity=obj,
        model_point=-1,
        behavior_id=6310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj)
    PlaySoundEffect(obj, 299961000, sound_type=SoundType.o_Object)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=3600799,
        source_entity=obj,
        model_point=-1,
        behavior_id=6310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=3600799,
        source_entity=obj,
        model_point=-1,
        behavior_id=6320,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj)
    PlaySoundEffect(obj, 299961000, sound_type=SoundType.o_Object)


@ContinueOnRest(13601800)
def Event_13601800():
    """Event 13601800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3600800)
    DisableCharacter(3600801)
    Kill(3600800)
    Kill(3600801)
    DisableObject(3601800)
    DeleteVFX(3603800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDead(3600800))
    AND_2.Add(CharacterDead(3600801))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3601800)
    DisableObject(3601801)
    DeleteVFX(3603800)
    DeleteVFX(3603801)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    KillBoss(game_area_param_id=3600800)
    SkipLines(1)
    KillBoss(game_area_param_id=3600801)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    AwardAchievement(achievement_id=35)
    RunEvent(9350, slot=0, args=(5,))
    AwardItemLot(3601800, host_only=False)
    EnableFlag(3600)
    StopPlayLogMeasurement(measurement_id=9360000)
    StopPlayLogMeasurement(measurement_id=9360001)
    StopPlayLogMeasurement(measurement_id=9360010)
    CreatePlayLog(name=0)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(13604811)
def Event_13604811():
    """Event 13604811"""
    if FlagEnabled(13601800):
        return
    if FlagEnabled(13601801):
        return
    DisableCharacter(3600800)
    AND_1.Add(FlagDisabled(13601800))
    AND_1.Add(FlagDisabled(13601801))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3602805))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13604810)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    DeleteVFX(3603860)
    EnableFlag(9180)


@ContinueOnRest(13601801)
def Event_13601801():
    """Event 13601801"""
    if FlagEnabled(13601800):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagDisabled(13601800))
    AND_2.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(13604811))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3602805))
    
    MAIN.Await(AND_2)
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(36000000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(36000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    CreateVFX(3603860)
    EnableFlag(13604808)
    EnableCharacter(3600800)
    if FlagEnabled(9347):
        return
    RunEvent(9350, slot=0, args=(5,))
    EnableFlag(9347)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(6001))
    
    Wait(0.0)


@ContinueOnRest(13601802)
def Event_13601802():
    """Event 13601802"""
    DisableAI(3600802)
    DisableHealthBar(3600802)
    DisableGravity(3600802)
    
    MAIN.Await(CharacterBackreadEnabled(3600802))
    
    Move(3600802, destination=3601802, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    ForceAnimation(3600802, 7000, loop=True)
    if FlagEnabled(13601803):
        return
    GotoIfThisEventFlagDisabled(Label.L0)
    ForceAnimation(3600802, 0, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(13601800))
    
    ForceAnimation(3600802, 7001)


@ContinueOnRest(13601803)
def Event_13601803():
    """Event 13601803"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableObject(3601811)
    
    MAIN.Await(CharacterDead(3600802))
    
    DisplayBanner(BannerType.NightmareSlain)
    Wait(5.0)
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSoundEvent(sound_id=3603000)
    DisableSoundEvent(sound_id=3603001)
    DeleteVFX(3603810)
    DeleteVFX(3603811)
    DeleteVFX(3603812)
    DeleteVFX(3603813)
    DeleteVFX(3603814)
    DeleteVFX(3603815)
    DeleteVFX(3603816)
    DeleteVFX(3603817)
    DeleteVFX(3603818)
    DeleteVFX(3603819)
    DeleteVFX(3603820)
    DeleteVFX(3603821)
    DeleteVFX(3603822)
    DeleteVFX(3603823)
    DeleteVFX(3603824)
    DeleteVFX(3603825)
    DeleteVFX(3603826)
    DeleteVFX(3603827)
    DeleteVFX(3603828)
    DeleteVFX(3603829)
    DeleteVFX(3603830)
    DeleteVFX(3603831)
    DeleteVFX(3603832)
    DeleteVFX(3603840)
    DeleteVFX(3603841)
    DeleteVFX(3603842)
    DeleteVFX(3603843)
    DeleteVFX(3603844)
    DeleteVFX(3603845)
    DeleteVFX(3603846)
    DeleteVFX(3603847)
    DeleteVFX(3603848)
    DeleteVFX(3603849)
    DeleteVFX(3603850)
    DeleteVFX(3603851)
    DeleteVFX(3603852)
    DeleteVFX(3603860)
    DeleteVFX(3603870)
    DeleteVFX(3603871)
    DeleteVFX(3603872)
    DeleteVFX(3603873)
    DeleteVFX(3603874)
    if ThisEventFlagEnabled():
        DisableObject(3601810)
        EnableObject(3601811)
    if ThisEventFlagEnabled():
        return
    EnableFlag(9180)
    PlayCutscene(36000010, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(3601810)
    EnableObject(3601811)
    DisableFlag(9180)
    EnableFlag(9469)
    RunEvent(9350, slot=0, args=(3,))


@ContinueOnRest(13601804)
def Event_13601804():
    """Event 13601804"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(13604808))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(3600800)
    EnableFlag(13604808)
    EnableFlag(13601801)


@ContinueOnRest(13604800)
def Event_13604800():
    """Event 13604800"""
    if FlagEnabled(13601800):
        return
    GotoIfFlagEnabled(Label.L0, flag=13601801)
    SkipLinesIfClient(2)
    DisableObject(3601800)
    DeleteVFX(3603800, erase_root_only=False)
    AND_1.Add(FlagDisabled(13601800))
    AND_1.Add(FlagEnabled(13601801))
    
    MAIN.Await(AND_1)
    
    EnableObject(3601800)
    EnableObject(3601801)
    CreateVFX(3603800)
    CreateVFX(3603801)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(13601800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=3600800, entity=3601800))
    AND_3.Add(FlagEnabled(13601800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 3602800, animation=101130, wait_for_completion=True)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=3602801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_5)
    EnableFlag(13604808)
    Restart()


@ContinueOnRest(13604801)
def Event_13604801():
    """Event 13604801"""
    DisableNetworkSync()
    if FlagEnabled(13601800):
        return
    AND_1.Add(FlagDisabled(13601800))
    AND_1.Add(FlagEnabled(13601801))
    AND_1.Add(FlagEnabled(13604808))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=3600800, entity=3601800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 3602800, animation=101130, wait_for_completion=True)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3602801))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(13604809)
    Restart()


@ContinueOnRest(13604802)
def Event_13604802():
    """Event 13604802"""
    if FlagEnabled(13601800):
        return
    DisableAI(3600800)
    DisableAI(3600801)
    DisableHealthBar(3600800)
    DisableHealthBar(3600801)
    ReferDamageToEntity(3600800, target_entity=3600801)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(13604808))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(13604810):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3600800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3600801, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13604810)
    EnableFlag(13604808)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3600800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(3600801, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600801)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3600800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(3600801, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600801)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableBossHealthBar(3600801, name=453000)
    EnableFlag(13604812)
    GotoIfThisEventFlagEnabled(Label.L5)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=3600800, radius=24.0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=3600800))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)

    # --- Label 5 --- #
    DefineLabel(5)
    if FlagDisabled(13604820):
        EnableAI(3600800)
        SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    else:
        EnableAI(3600801)
        SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
        SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreatePlayLog(name=42)
    StartPlayLogMeasurement(measurement_id=3600010, name=58, overwrite=True)


@ContinueOnRest(13604803)
def Event_13604803():
    """Event 13604803"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3603802)
    DisableSoundEvent(sound_id=3603803)
    if FlagEnabled(13601800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(FlagDisabled(13601800))
    AND_1.Add(FlagEnabled(13604812))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(13604809))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3602802))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=3603802)
    AND_2.Add(FlagEnabled(13604820))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(13601800))
    AND_2.Add(FlagEnabled(13604812))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(13604809))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3602802))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=3603802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3603803)


@ContinueOnRest(13604804)
def Event_13604804():
    """Event 13604804"""
    DisableNetworkSync()
    if FlagEnabled(13601800):
        return
    GotoIfFlagEnabled(Label.L0, flag=13604820)
    AND_1.Add(CharacterAlive(3600800))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3600800, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    AND_2.Add(CharacterAlive(3600800))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3600800, radius=12.5))
    
    MAIN.Await(AND_2)
    
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterAlive(3600800))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=3600801, radius=12.0))
    
    MAIN.Await(AND_3)
    
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    AND_4.Add(CharacterAlive(3600800))
    AND_4.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3600801, radius=12.5))
    
    MAIN.Await(AND_4)
    
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


@ContinueOnRest(13604805)
def Event_13604805():
    """Event 13604805"""
    DisableNetworkSync()
    if FlagEnabled(13601800):
        return
    
    MAIN.Await(FlagEnabled(13601800))
    
    DisableBossMusic(sound_id=3603802)
    DisableBossMusic(sound_id=3603803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(13604806)
def Event_13604806():
    """Event 13604806"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3601800, radius=6.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(13604807)
def Event_13604807():
    """Event 13604807"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3601800, radius=6.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3601800, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(13604820)
def Event_13604820():
    """Event 13604820"""
    if FlagEnabled(13601800):
        return
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3600800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(3600801)
    
    MAIN.Await(HealthRatio(3600800) < 0.5)
    
    AICommand(3600800, command_id=100, command_slot=0)
    ReplanAI(3600800)
    
    MAIN.Await(CharacterHasTAEEvent(3600800, tae_event_id=100))
    
    DisableCharacter(3600800)
    EnableGravity(3600801)
    SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        3600801,
        destination=3600800,
        destination_type=CoordEntityType.Character,
        model_point=203,
        copy_draw_parent=3600800,
    )
    ForceAnimation(3600801, 3031)
    
    MAIN.Await(CharacterHasTAEEvent(3600801, tae_event_id=50))
    
    RemoveSpecialEffect(3600801, 5300)
    AddSpecialEffect(3600801, 5333)
    EnableAI(3600801)


@ContinueOnRest(13604830)
def Event_13604830():
    """Event 13604830"""
    if FlagEnabled(13601800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3600801, tae_event_id=100))
    
    AICommand(3600803, command_id=10, command_slot=0)
    ReplanAI(3600803)
    
    MAIN.Await(CharacterHasSpecialEffect(3600803, 5020))
    
    AICommand(3600803, command_id=20, command_slot=0)
    ReplanAI(3600803)
    
    MAIN.Await(CharacterHasTAEEvent(3600803, tae_event_id=10))
    
    AICommand(3600803, command_id=-1, command_slot=0)
    RemoveSpecialEffect(3600803, 5020)
    ReplanAI(3600803)
    Restart()


@ContinueOnRest(13604840)
def Event_13604840():
    """Event 13604840"""
    DisableNetworkSync()
    if FlagEnabled(13601800):
        return
    AND_1.Add(CharacterHasTAEEvent(3600800, tae_event_id=30))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 8055))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 8054)
    OR_1.Add(CharacterHasTAEEvent(3600800, tae_event_id=40))
    OR_1.Add(TimeElapsed(seconds=4.5))
    OR_1.Add(EntityBeyondDistance(entity=3600800, other_entity=PLAYER, radius=20.0))
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(PLAYER, 8054)
    Restart()


@ContinueOnRest(13604850)
def Event_13604850():
    """Event 13604850"""
    DisableNetworkSync()
    if FlagEnabled(13601800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(3600801, 5036))
    
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=1)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(3600801, 5036))
    
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


@RestartOnRest(13605200)
def Event_13605200(
    _,
    character: int,
    region: int,
    region_1: int,
    patrol_information_id: int,
    seconds: float,
    left: int,
):
    """Event 13605200"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueNotEqual(left=left, right=0):
        AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13605400)
def Event_13605400(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    region: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13605400"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605480)
def Event_13605480(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    region: int,
    seconds: float,
    frames: int,
):
    """Event 13605480"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    Wait(seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    WaitFrames(frames=frames)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605490)
def Event_13605490(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    character_1: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13605490"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=4.0))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605500)
def Event_13605500(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    region: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13605500"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    EnableGravity(character)
    EnableCharacterCollision(character)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605520)
def Event_13605520(_, character: int, region: int, ai_param_id: int, ai_param_id_1: int):
    """Event 13605520"""
    AND_1.Add(AllPlayersOutsideRegion(region=region))
    
    MAIN.Await(not AND_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    Restart()


@RestartOnRest(13605540)
def Event_13605540(_, character: int, region: int, radius: float, ai_param_id: int, ai_param_id_1: int):
    """Event 13605540"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetAIParamID(character, ai_param_id=ai_param_id)
    AND_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605560)
def Event_13605560(_, character: int, region: int, radius: float):
    """Event 13605560"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    EnableAI(character)


@RestartOnRest(13605600)
def Event_13605600(_, character__set_draw_parent: int, character: int):
    """Event 13605600"""
    DisableGravity(character)
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterBackreadEnabled(character__set_draw_parent))
    
        Wait(1.0)
    AND_1.Add(HealthRatio(character__set_draw_parent) <= 0.0)
    SkipLinesIfConditionFalse(2, AND_1)
    DisableBackread(character)
    End()
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=100,
        set_draw_parent=character__set_draw_parent,
    )
    Restart()


@RestartOnRest(13605605)
def Event_13605605():
    """Event 13605605"""
    DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4691))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 4690))
    
    Wait(2.0)
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 4690))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4690))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_3)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(PLAYER, 4691)
    Restart()


@RestartOnRest(13605606)
def Event_13605606():
    """Event 13605606"""
    DisableNetworkSync()
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4690))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4691))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 4691)
    Restart()


@RestartOnRest(13605700)
def Event_13605700(_, character: int, animation: int, flag: int):
    """Event 13605700"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    RotateToFaceEntity(character, PLAYER, animation=animation, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    Restart()


@RestartOnRest(13605720)
def Event_13605720(_, character: int):
    """Event 13605720"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=100))
    
    MoveObjectToCharacter(3601799, character=PLAYER)
    WaitFrames(frames=1)
    ShootProjectile(
        owner_entity=3600799,
        source_entity=3601799,
        model_point=200,
        behavior_id=6300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(13605730)
def Event_13605730():
    """Event 13605730"""
    DisableNetworkSync()
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_1:
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3602798))
    
    MoveObjectToCharacter(3601798, character=PLAYER)
    WaitFrames(frames=1)
    ShootProjectile(
        owner_entity=3600799,
        source_entity=3601798,
        model_point=200,
        behavior_id=6330,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=3602798))
    
    Restart()


@RestartOnRest(13605740)
def Event_13605740(_, character: int, region: int, region_1: int, radius: float):
    """Event 13605740"""
    if ThisEventFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    SetCharacterEventTarget(character, region=region_1)
    AICommand(character, command_id=100, command_slot=0)
    EnableAI(character)
    WaitFrames(frames=60)
    AICommand(character, command_id=-1, command_slot=0)


@RestartOnRest(13605750)
def Event_13605750():
    """Event 13605750"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(3600201)
    DisableCharacterCollision(3600201)
    ForceAnimation(3600201, 7006, loop=True)
    SetAIParamID(3600201, ai_param_id=404003)
    OR_1.Add(HasAIStatus(3600201, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(3600201, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    if FlagDisabled(53600100):
        AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3600201, radius=12.0))
    else:
        AND_1.Add(CharacterInsideRegion(PLAYER, region=3602201))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    RotateToFaceEntity(3600201, PLAYER, animation=7007)
    EnableGravity(3600201)
    EnableCharacterCollision(3600201)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(3600201, ai_param_id=404000)


@RestartOnRest(13605751)
def Event_13605751():
    """Event 13605751"""
    MAIN.Await(CharacterHasTAEEvent(3600330, tae_event_id=100))
    
    SetAIParamID(3600208, ai_param_id=404002)
    SetAIParamID(3600209, ai_param_id=404002)
    MoveObjectToCharacter(3601799, character=PLAYER)
    WaitFrames(frames=1)
    ShootProjectile(
        owner_entity=3600799,
        source_entity=3601799,
        model_point=200,
        behavior_id=6300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@RestartOnRest(13605752)
def Event_13605752():
    """Event 13605752"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3602315))
    AND_2.Add(AttackedWithDamageType(attacked_entity=3600315))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SetNest(3600315, region=3602316)
    AICommand(3600315, command_id=10, command_slot=0)
    ReplanAI(3600315)
    
    MAIN.Await(CharacterInsideRegion(3600315, region=3602316))
    
    AICommand(3600315, command_id=-1, command_slot=0)
    ReplanAI(3600315)


@RestartOnRest(13605760)
def Event_13605760():
    """Event 13605760"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(HealthRatio(3600302) < 0.5)
    
    SetNest(3600302, region=3602303)
    AICommand(3600302, command_id=10, command_slot=0)
    ReplanAI(3600302)
    
    MAIN.Await(CharacterInsideRegion(3600302, region=3602303))
    
    AICommand(3600302, command_id=-1, command_slot=0)
    ReplanAI(3600302)


@RestartOnRest(13605761)
def Event_13605761():
    """Event 13605761"""
    if ThisEventFlagEnabled():
        return
    DisableAI(3600303)
    ForceAnimation(3600303, 7004, loop=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3602304))
    AND_1.Add(HealthRatio(3600302) < 0.5)
    AND_2.Add(HealthRatio(3600302) < 0.4000000059604645)
    AND_3.Add(AttackedWithDamageType(attacked_entity=3600303))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    ForceAnimation(3600303, 7005)
    EnableAI(3600303)


@RestartOnRest(13605762)
def Event_13605762():
    """Event 13605762"""
    if FlagEnabled(53600800):
        return
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    AND_2.Add(CharacterDead(3600302))
    AND_2.Add(CharacterDead(3600303))
    
    MAIN.Await(AND_2)
    
    AwardItemLot(3601100, host_only=True)


@RestartOnRest(13605770)
def Event_13605770(_, character: int, region: int, min_seconds: float, max_seconds: float):
    """Event 13605770"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    EnableAI(character)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(13605799)
def Event_13605799():
    """Event 13605799"""
    CreateProjectileOwner(entity=3600799)


@RestartOnRest(13605900)
def Event_13605900(_, flag: int, flag_1: int, flag_2: int, region: int, region_1: int, flag_3: int):
    """Event 13605900"""
    if FlagEnabled(1730):
        return
    if FlagEnabled(flag_2):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagDisabled(1730))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(13605910)
def Event_13605910(_, flag: int, flag_1: int, flag_2: int, region: int, region_1: int):
    """Event 13605910"""
    if FlagEnabled(1730):
        return
    if FlagEnabled(flag_2):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagDisabled(1730))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(PLAYER, 10306, sound_type=SoundType.s_SFX)
    WaitRandomSeconds(min_seconds=2.0, max_seconds=4.0)
    Restart()


@RestartOnRest(13605920)
def Event_13605920(
    _,
    character: int,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    flag_2: int,
    flag_3: int,
    destination: int,
):
    """Event 13605920"""
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    EnableInvincibility(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5560)
    if FlagEnabled(1730):
        return
    if FlagEnabled(flag_1):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(FlagDisabled(1730))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    RemoveSpecialEffect(character, 5560)
    AddSpecialEffect(character, 8060)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    ForceAnimation(character, 101203)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    RemoveSpecialEffect(character, 5560)
    EnableFlag(flag)
    DisableFlag(flag_3)
    
    MAIN.Await(FlagEnabled(flag_3))
    
    Restart()


@RestartOnRest(13605921)
def Event_13605921(
    _,
    character: int,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    flag_2: int,
    flag_3: int,
    destination: int,
):
    """Event 13605921"""
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    EnableInvincibility(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5560)
    if FlagEnabled(1730):
        return
    if FlagEnabled(flag_1):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(FlagDisabled(1730))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_2)
    AND_3.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=3604027)
    SkipLines(1)
    Move(character, destination=3602917, destination_type=CoordEntityType.Region, set_draw_parent=3604027)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    RemoveSpecialEffect(character, 5560)
    AddSpecialEffect(character, 8060)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    ForceAnimation(character, 101203)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    RemoveSpecialEffect(character, 5560)
    EnableFlag(flag)
    DisableFlag(flag_3)
    
    MAIN.Await(FlagEnabled(flag_3))
    
    Restart()


@RestartOnRest(13605930)
def Event_13605930(_, character: int, flag: int, flag_1: int, region: int, region_1: int, flag_2: int):
    """Event 13605930"""
    if FlagEnabled(1730):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    Wait(2.0)
    EnableInvincibility(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5560)
    RemoveSpecialEffect(character, 8060)
    RemoveSpecialEffect(character, 1130)
    RemoveSpecialEffect(character, 1150)
    PlaySoundEffect(PLAYER, 122, sound_type=SoundType.s_SFX)
    Wait(4.0)
    EnableFlag(flag_2)
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()


@RestartOnRest(13605940)
def Event_13605940(_, character: int, flag: int, flag_1: int, item_lot_param_id: int, character_1: int):
    """Event 13605940"""
    DisableBackread(character_1)
    GotoIfFlagDisabled(Label.L0, flag=1730)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 8060)
    RemoveSpecialEffect(character, 1130)
    RemoveSpecialEffect(character, 1150)
    PlaySoundEffect(PLAYER, 122, sound_type=SoundType.s_SFX)
    EnableFlag(flag_1)
    AND_2.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(1, AND_2)
    AwardItemLot(item_lot_param_id, host_only=True)


@ContinueOnRest(13600900)
def Event_13600900(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 13600900"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    AND_1.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(13600940)
def Event_13600940(_, character: int):
    """Event 13600940"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    DisableFlagRange((1770, 1789))
    EnableFlag(1780)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L0, flag=1770)
    GotoIfFlagEnabled(Label.L1, flag=1780)
    DisableBackread(character)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(73600310)
    DisableFlag(73600314)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    SetDistanceLimitForConversationStateChanges(character=character, distance=35.0)
    End()


@ContinueOnRest(13600943)
def Event_13600943(_, flag: int, item_lot_param_id: int):
    """Event 13600943"""
    if FlagEnabled(flag):
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(item_lot_param_id, host_only=False)


@ContinueOnRest(13600941)
def Event_13600941(_, flag: int, flag_1: int):
    """Event 13600941"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    Restart()


@ContinueOnRest(13600942)
def Event_13600942(_, min_seconds: float, max_seconds: float):
    """Event 13600942"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    
    MAIN.Await(FlagEnabled(73600310))
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    if FlagEnabled(73600313):
        MAIN.Await(FlagDisabled(73600314))
    
        DisableFlag(73600313)
        Restart()
    DisableFlag(73600310)
    Restart()


@ContinueOnRest(13600944)
def Event_13600944():
    """Event 13600944"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    DisableFlag(73600318)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3602941))
    
    EnableFlag(73600318)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=3602941))
    
    Restart()


@ContinueOnRest(13600950)
def Event_13600950(_, character: int):
    """Event 13600950"""
    OR_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L8, input_condition=OR_15)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1720, 1722)))
    AND_1.Add(FlagEnabled(73400403))
    AND_1.Add(FlagEnabled(1650))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(1722))
    OR_2.Add(FlagEnabled(1660))
    OR_2.Add(FlagEnabled(1651))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(73500602))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(FlagEnabled(1723))
    AND_3.Add(FlagEnabled(73600501))
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1713)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagRangeAnyEnabled(Label.L4, flag_range=(1710, 1712))
    GotoIfFlagEnabled(Label.L4, flag=1720)
    DisableObject(3600906)
    DisableTreasure(obj=3600906)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableObject(3600906)
    EnableTreasure(obj=3600906)
    Goto(Label.L9)

    # --- Label 8 --- #
    DefineLabel(8)
    DisableTreasure(obj=3600906)
    GotoIfFlagRangeAnyEnabled(Label.L5, flag_range=(1710, 1712))
    GotoIfFlagEnabled(Label.L5, flag=1720)
    DisableObject(3600906)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableObject(3600906)

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=1723)
    GotoIfFlagEnabled(Label.L1, flag=1713)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103151)
    EnableImmortality(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAnimations(character)
    ForceAnimation(character, 103157, skip_transition=True)
    End()


@ContinueOnRest(13600951)
def Event_13600951(_, character: int, flag: int, flag_1: int):
    """Event 13600951"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103152)
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag))
    AND_2.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_2)
    
    ForceAnimation(character, 103151)
    Restart()


@ContinueOnRest(13600952)
def Event_13600952(_, character: int, flag: int, flag_1: int):
    """Event 13600952"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103153)
    Kill(character, award_souls=True)
    EnableFlag(flag_1)


@ContinueOnRest(13600953)
def Event_13600953(_, character: int):
    """Event 13600953"""
    OR_1.Add(FlagEnabled(1724))
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(1720, 1722)))
    if not OR_1:
        return
    
    MAIN.Await(FlagEnabled(1723))
    
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 103151)
    EnableImmortality(character)
    DisableObject(3600906)
    DisableTreasure(obj=3600906)


@ContinueOnRest(13600954)
def Event_13600954(_, flag: int, flag_1: int, item_lot_param_id: int):
    """Event 13600954"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(3600905))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(item_lot_param_id, host_only=False)


@ContinueOnRest(13600955)
def Event_13600955():
    """Event 13600955"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    AND_1.Add(FlagEnabled(1723))
    AND_1.Add(FlagDisabled(73600502))
    
    MAIN.Await(AND_1)
    
    EnableFlag(73600500)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3602850))
    
    DisableFlag(73600500)
    EnableFlag(73600502)


@ContinueOnRest(13600956)
def Event_13600956(_, character: int, flag: int, flag_1: int):
    """Event 13600956"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag_1)
    Kill(character)
    EnableFlag(73600530)
    ForceAnimation(character, 103156, wait_for_completion=True, skip_transition=True)
    ForceAnimation(character, 103157, skip_transition=True)


@ContinueOnRest(13600995)
def Event_13600995():
    """Event 13600995"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(13605952))
    
    DisableFlag(13605940)
