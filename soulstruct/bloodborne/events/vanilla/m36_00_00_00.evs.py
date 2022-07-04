"""
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


@NeverRestart(0)
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
        flag_6=13604712
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
        flag_6=13604711
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
    Event_13604400(0, obj__projectile_id=3601400)
    Event_13604400(1, obj__projectile_id=3601401)
    Event_13604400(2, obj__projectile_id=3601402)
    Event_13604400(3, obj__projectile_id=3601403)
    Event_13604400(4, obj__projectile_id=3601404)
    Event_13604400(5, obj__projectile_id=3601405)
    Event_13604400(6, obj__projectile_id=3601406)
    Event_13604400(7, obj__projectile_id=3601407)
    Event_13604400(8, obj__projectile_id=3601408)
    Event_13604400(9, obj__projectile_id=3601409)
    Event_13604400(10, obj__projectile_id=3601410)
    Event_13604400(11, obj__projectile_id=3601411)
    Event_13604400(12, obj__projectile_id=3601412)
    Event_13604400(13, obj__projectile_id=3601413)
    Event_13604400(20, obj__projectile_id=3601420)
    Event_13604400(21, obj__projectile_id=3601421)
    Event_13604400(22, obj__projectile_id=3601422)
    Event_13604400(23, obj__projectile_id=3601423)
    Event_13604400(24, obj__projectile_id=3601424)
    Event_13604400(25, obj__projectile_id=3601425)
    Event_13604400(26, obj__projectile_id=3601426)
    Event_13604400(27, obj__projectile_id=3601427)
    Event_13604400(28, obj__projectile_id=3601428)
    Event_13604400(29, obj__projectile_id=3601429)
    Event_13604400(30, obj__projectile_id=3601430)
    Event_13604400(31, obj__projectile_id=3601431)
    Event_13604400(40, obj__projectile_id=3601440)
    Event_13604400(41, obj__projectile_id=3601441)
    Event_13604400(42, obj__projectile_id=3601442)
    Event_13604400(43, obj__projectile_id=3601443)
    Event_13604400(44, obj__projectile_id=3601444)
    Event_13604400(45, obj__projectile_id=3601445)
    Event_13604400(46, obj__projectile_id=3601446)
    Event_13604400(47, obj__projectile_id=3601447)
    Event_13604400(50, obj__projectile_id=3601450)
    Event_13604400(51, obj__projectile_id=3601451)
    Event_13604400(52, obj__projectile_id=3601452)
    Event_13604400(53, obj__projectile_id=3601453)
    Event_13604400(54, obj__projectile_id=3601454)
    Event_13604400(55, obj__projectile_id=3601455)
    Event_13604400(56, obj__projectile_id=3601456)
    Event_13604400(57, obj__projectile_id=3601457)
    Event_13604400(60, obj__projectile_id=3601460)
    Event_13604400(61, obj__projectile_id=3601461)
    Event_13604400(62, obj__projectile_id=3601462)
    Event_13604400(63, obj__projectile_id=3601463)
    Event_13604400(64, obj__projectile_id=3601464)
    Event_13604400(65, obj__projectile_id=3601465)
    Event_13604400(66, obj__projectile_id=3601466)
    Event_13604400(67, obj__projectile_id=3601467)
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
    Event_13605200(0, 3600200, 3602200, 0, 3603200, 0.0, 0)
    Event_13605200(1, 3600202, 3602202, 0, 3603202, 0.0, 0)
    Event_13605200(2, 3600203, 3602202, 3602203, 3603203, 0.0, 0)
    Event_13605200(3, 3600204, 3602202, 3602203, 3603204, 0.0, 0)
    Event_13605200(4, 3600208, 3602208, 0, 3603208, 0.0, 0)
    Event_13605200(5, 3600209, 3602208, 0, 3603209, 0.0, 0)
    Event_13605200(6, 3600210, 3602210, 0, 3603210, 0.0, 0)
    Event_13605200(7, 3600300, 3602300, 0, 3603300, 0.0, 0)
    Event_13605200(8, 3600213, 3602213, 0, 3603213, 0.0, 0)
    Event_13605200(9, 3600214, 3602213, 0, 3603214, 0.0, 0)
    Event_13605200(10, 3600217, 3602215, 0, 3603217, 0.0, 0)
    Event_13605200(11, 3600229, 3602229, 0, 3603229, 0.0, 0)
    Event_13605200(12, 3600231, 3602231, 3602232, 3603231, 0.0, 0)
    Event_13605200(13, 3600232, 3602231, 3602232, 3603232, 0.0, 0)
    Event_13605200(14, 3600233, 3602231, 3602232, 3603233, 0.0, 0)
    Event_13605200(15, 3600610, 3602610, 0, 3603610, 0.0, 0)
    Event_13605200(16, 3600611, 3602231, 3602232, 3603611, 0.0, 0)
    Event_13605200(17, 3600301, 3602301, 0, 3603301, 0.0, 1)
    Event_13605200(18, 3600310, 3602310, 0, 3603310, 0.0, 1)
    Event_13605200(19, 3600700, 3602700, 0, 3603700, 0.0, 0)
    Event_13605200(20, 3600710, 3602710, 0, 3603710, 0.0, 0)
    Event_13605200(21, 3600251, 3602251, 0, 3603251, 0.0, 0)
    Event_13605200(23, 3600253, 3602252, 0, 3603253, 0.0, 0)
    Event_13605200(25, 3600314, 3602314, 0, 3603314, 0.0, 0)
    Event_13605200(26, 3600455, 3602455, 0, 3603455, 0.0, 0)
    Event_13605200(27, 3600456, 3602455, 0, 3603456, 1.0, 1)
    Event_13605200(28, 3600474, 3602474, 0, 3603474, 0.0, 0)
    Event_13605200(29, 3600475, 3602474, 0, 3603475, 1.0, 1)
    Event_13605200(30, 3600302, 3602302, 0, 3603302, 0.0, 0)
    Event_13605200(31, 3600312, 3602312, 0, 3603312, 0.0, 0)
    Event_13605200(32, 3600470, 3602470, 0, 3603470, 0.0, 1)
    Event_13605200(33, 3600500, 3602470, 0, 3603500, 0.0, 0)
    Event_13605200(34, 3600501, 3602501, 0, 3603501, 0.0, 0)
    Event_13605200(35, 3600920, 3602940, 0, 3603920, 0.0, 0)
    Event_13605400(0, 3600206, 7004, 404002, 7005, 404002, 3602206, 0.0, 0.0)
    Event_13605400(1, 3600211, 7012, 404000, 7013, 404000, 3602211, 0.0, 0.0)
    Event_13605400(2, 3600218, 0, 404011, 3005, 404010, 3602218, 0.0, 0.0)
    Event_13605400(3, 3600222, 7016, 404031, 7017, 404030, 3602222, 0.0, 0.0)
    Event_13605400(4, 3600230, 7004, 404000, 7005, 404000, 3602230, 0.0, 0.0)
    Event_13605400(5, 3600239, 7012, 404008, 7013, 404008, 3602240, 0.75, 0.75)
    Event_13605400(6, 3600240, 7012, 404004, 7013, 404004, 3602240, 0.25, 0.25)
    Event_13605400(7, 3600241, 7012, 404008, 7013, 404008, 3602240, 0.0, 0.0)
    Event_13605400(8, 3600242, 7012, 404004, 7013, 404004, 3602240, 0.5, 0.5)
    Event_13605400(9, 3600244, 7014, 404014, 7015, 404014, 3602244, 0.0, 0.0)
    Event_13605400(10, 3600245, 0, 404035, 3026, 404034, 3602245, 0.0, 0.0)
    Event_13605400(11, 3600246, 7018, 404034, 7019, 404034, 3602246, 0.0, 0.0)
    Event_13605400(12, 3600247, 7018, 404014, 7019, 404014, 3602246, 0.5, 0.5)
    Event_13605400(13, 3600260, 7012, 404018, 7013, 404019, 3602260, 0.0, 0.0)
    Event_13605400(14, 3600261, 7012, 404018, 7013, 404019, 3602261, 0.0, 0.0)
    Event_13605400(15, 3600262, 7012, 404018, 7013, 404019, 3602262, 0.0, 0.0)
    Event_13605400(16, 3600265, 7012, 404018, 7013, 404019, 3602265, 0.0, 0.0)
    Event_13605400(17, 3600400, 7010, 407022, 3001, 407020, 3602400, 0.0, 1.0)
    Event_13605400(18, 3600401, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0)
    Event_13605400(19, 3600402, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0)
    Event_13605400(20, 3600403, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0)
    Event_13605400(21, 3600404, 7010, 407022, 3001, 407020, 3602400, 0.0, 1.0)
    Event_13605400(22, 3600405, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0)
    Event_13605400(25, 3600408, 7010, 407022, 3001, 407020, 3602408, 0.0, 1.0)
    Event_13605400(26, 3600409, 7010, 407012, 7001, 407010, 3602408, 0.0, 1.0)
    Event_13605400(27, 3600410, 7010, 407022, 3001, 407020, 3602408, 0.0, 1.0)
    Event_13605400(28, 3600411, 7010, 407012, 7001, 407010, 3602408, 0.0, 1.0)
    Event_13605400(29, 3600412, 7010, 407012, 7001, 407010, 3602412, 0.0, 0.0)
    Event_13605400(30, 3600413, 7010, 407012, 7001, 407010, 3602412, 1.0, 1.0)
    Event_13605400(33, 3600416, 7010, 407022, 3001, 407020, 3602416, 0.0, 0.0)
    Event_13605400(34, 3600417, 7010, 407012, 7001, 407010, 3602416, 1.0, 1.0)
    Event_13605400(35, 3600418, 7010, 407012, 7001, 407010, 3602416, 0.5, 0.5)
    Event_13605400(36, 3600419, 7010, 407012, 7001, 407010, 3602419, 0.0, 0.0)
    Event_13605400(37, 3600424, 7010, 407022, 3001, 407020, 3602424, 0.5, 0.5)
    Event_13605400(38, 3600425, 7010, 407012, 7001, 407010, 3602424, 0.0, 0.0)
    Event_13605400(39, 3600426, 7010, 407012, 7001, 407010, 3602424, 1.0, 1.0)
    Event_13605400(40, 3600440, 7010, 407022, 7001, 407020, 3602440, 0.0, 0.0)
    Event_13605400(41, 3600441, 7010, 407022, 3001, 407020, 3602440, 0.0, 0.0)
    Event_13605480(0, 3600223, 7008, 404032, 7009, 404030, 3602223, 0.0, 33)
    Event_13605480(1, 3600476, 7012, 407000, 7013, 407000, 3602476, 0.0, 30)
    Event_13605480(2, 3600477, 7014, 407000, 7015, 407000, 3602476, 0.5, 30)
    Event_13605480(3, 3600478, 7016, 407000, 7017, 407000, 3602478, 0.0, 30)
    Event_13605490(0, 3600313, 9000, 405003, 9060, 405003, 3600314, 0.0, 0.0)
    Event_13605490(1, 3600266, 7012, 404018, 7013, 404019, 3600314, 0.5, 0.5)
    Event_13605490(2, 3600267, 7014, 404018, 7015, 404019, 3600314, 1.0, 1.0)
    Event_13605490(3, 3600263, 7012, 404018, 7013, 404019, 3600265, 0.5, 0.5)
    Event_13605490(4, 3600264, 7012, 404018, 7013, 404019, 3600265, 1.0, 1.0)
    Event_13605500(1, 3600207, 7006, 404002, 7007, 404002, 3602206, 4.0, 4.0)
    Event_13605500(2, 3600212, 7006, 404016, 7007, 404010, 3602211, 0.0, 0.0)
    Event_13605500(3, 3600216, 7006, 404003, 7007, 404000, 3602215, 0.0, 0.0)
    Event_13605520(1, character=3600310, region=3602310, ai_param_id=405001, ai_param_id_1=405000)
    Event_13605540(0, 3600210, 0, 8.0, 404040, 404000)
    Event_13605540(1, 3600300, 0, 8.0, 406001, 406000)
    Event_13605540(2, 3600500, 3602470, 4.0, 256901, 256900)
    Event_13605540(3, 3600501, 3602470, 4.0, 256901, 256900)
    Event_13605540(4, 3600218, 0, 1.0, 404011, 404010)
    Event_13605540(5, 3600220, 0, 4.0, 404011, 404010)
    Event_13605540(6, 3600221, 0, 4.0, 404011, 404010)
    Event_13605560(0, 3600331, 3602331, 4.0)
    Event_13605600(0, character__set_draw_parent=3600500, character=3600510)
    Event_13605600(1, character__set_draw_parent=3600501, character=3600511)
    Event_13605605()
    Event_13605606()
    Event_13605799()
    Event_13605720(0, character=3600206)
    Event_13605720(1, character=3600314)
    Event_13605740(0, 3600215, 3602215, 3600720, 2.0)
    Event_13605740(1, 3600219, 3602218, 3600721, 2.0)
    Event_13605740(2, 3600250, 3602250, 3600722, 2.0)
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
        destination=3602906
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
        destination=3602916
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
        destination=3602926
    )
    Event_13605930(
        0,
        character=3600900,
        flag=13605960,
        flag_1=13605970,
        region=3602908,
        region_1=3602909,
        flag_2=13605980
    )
    Event_13605930(
        1,
        character=3600901,
        flag=13605961,
        flag_1=13605971,
        region=3602918,
        region_1=3602909,
        flag_2=13605981
    )
    Event_13605930(2, character=3600902, flag=13605962, flag_1=13605972, region=3602928, region_1=0, flag_2=13605982)
    Event_13605940(0, character=3600900, flag=13605960, flag_1=13605970, item_lot_param_id=43730, character_1=3600910)
    Event_13605940(1, character=3600901, flag=13605961, flag_1=13605971, item_lot_param_id=43740, character_1=3600911)
    Event_13605940(2, character=3600902, flag=13605962, flag_1=13605972, item_lot_param_id=43720, character_1=3600912)
    Event_13600995()
    Event_13600942(0, 6.0, 10.0)
    Event_13600943(0, flag=73600300, item_lot_param_id=43600)
    Event_13600944()
    Event_13600951(0, character=3600905, flag=73600520, flag_1=1723)
    Event_13600952(0, character=3600905, flag=1723, flag_1=73600530)
    Event_13600953(0, character=3600905)
    Event_13600955()
    Event_13600956(0, character=3600905, flag=1723, flag_1=73600521)
    Event_13600900(1, character=3600905, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1713)
    Event_13600954(0, 1713, 73600530, 43220)


@NeverRestart(50)
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

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(flag)
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    IfOnline(1)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfInsideMap(1, game_map=FISHING_HAMLET)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, value=30)
    SkipLinesIfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(
        2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, flag_3)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    WaitFrames(frames=59)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(13604710)
def Event_13604710(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13604710"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfInsideMap(1, game_map=FISHING_HAMLET)
    IfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    EnableFlag(flag_2)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest(13604720)
def Event_13604720(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13604720"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_2)
    IfFlagEnabled(-1, flag_1)
    IfClientTypeCountComparison(
        -1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfOutsideMap(-1, game_map=FISHING_HAMLET)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(character, 9100)
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
    IfFlagEnabled(-15, flag_1)
    IfFlagEnabled(-15, flag_2)
    IfFlagEnabled(-15, flag_3)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_5)
    IfHealthEqual(2, character, value=0.0)
    IfFlagEnabled(-2, flag_3)
    IfFlagEnabled(-2, flag_6)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    EnableFlag(flag_4)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@RestartOnRest(13604740)
def Event_13604740():
    """Event 13604740"""
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 3604000)
    IfStandingOnCollision(-1, 3604001)
    IfStandingOnCollision(-1, 3604002)
    IfStandingOnCollision(-1, 3604003)
    IfStandingOnCollision(-1, 3604004)
    IfStandingOnCollision(-1, 3604005)
    IfStandingOnCollision(-1, 3604006)
    IfStandingOnCollision(-1, 3604007)
    IfStandingOnCollision(-1, 3604008)
    IfStandingOnCollision(-1, 3604009)
    IfStandingOnCollision(-1, 3604010)
    IfStandingOnCollision(-1, 3604011)
    IfStandingOnCollision(-1, 3604012)
    IfStandingOnCollision(-1, 3604013)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604741)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnCollision(-2, 3604000)
    IfStandingOnCollision(-2, 3604001)
    IfStandingOnCollision(-2, 3604002)
    IfStandingOnCollision(-2, 3604003)
    IfStandingOnCollision(-2, 3604004)
    IfStandingOnCollision(-2, 3604005)
    IfStandingOnCollision(-2, 3604006)
    IfStandingOnCollision(-2, 3604007)
    IfStandingOnCollision(-2, 3604008)
    IfStandingOnCollision(-2, 3604009)
    IfStandingOnCollision(-2, 3604010)
    IfStandingOnCollision(-2, 3604011)
    IfStandingOnCollision(-2, 3604012)
    IfStandingOnCollision(-2, 3604013)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13604741)
    Restart()


@RestartOnRest(13604742)
def Event_13604742():
    """Event 13604742"""
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 3604020)
    IfStandingOnCollision(-1, 3604021)
    IfStandingOnCollision(-1, 3604022)
    IfStandingOnCollision(-1, 3604023)
    IfStandingOnCollision(-1, 3604024)
    IfStandingOnCollision(-1, 3604025)
    IfStandingOnCollision(-1, 3604026)
    IfStandingOnCollision(-1, 3604027)
    IfStandingOnCollision(-1, 3604028)
    IfStandingOnCollision(-1, 3604029)
    IfStandingOnCollision(-1, 3604030)
    IfStandingOnCollision(-1, 3604031)
    IfStandingOnCollision(-1, 3604032)
    IfStandingOnCollision(-1, 3604033)
    IfStandingOnCollision(-1, 3604034)
    IfStandingOnCollision(-1, 3604035)
    IfStandingOnCollision(-1, 3604110)
    IfStandingOnCollision(-1, 3604111)
    IfStandingOnCollision(-1, 3604112)
    IfStandingOnCollision(-1, 3604113)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604743)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnCollision(-2, 3604020)
    IfStandingOnCollision(-2, 3604021)
    IfStandingOnCollision(-2, 3604022)
    IfStandingOnCollision(-2, 3604023)
    IfStandingOnCollision(-2, 3604024)
    IfStandingOnCollision(-2, 3604025)
    IfStandingOnCollision(-2, 3604026)
    IfStandingOnCollision(-2, 3604027)
    IfStandingOnCollision(-2, 3604028)
    IfStandingOnCollision(-2, 3604029)
    IfStandingOnCollision(-2, 3604030)
    IfStandingOnCollision(-2, 3604031)
    IfStandingOnCollision(-2, 3604032)
    IfStandingOnCollision(-2, 3604033)
    IfStandingOnCollision(-2, 3604034)
    IfStandingOnCollision(-2, 3604035)
    IfStandingOnCollision(-2, 3604110)
    IfStandingOnCollision(-2, 3604111)
    IfStandingOnCollision(-2, 3604112)
    IfStandingOnCollision(-2, 3604113)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13604743)
    Restart()


@NeverRestart(13600000)
def Event_13600000():
    """Event 13600000"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfStandingOnCollision(0, 3604002)
    RunEvent(9350, slot=0, args=(4,))


@NeverRestart(13600010)
def Event_13600010():
    """Event 13600010"""
    DisableNetworkSync()
    EndIfFlagEnabled(13601803)
    DisableSoundEvent(sound_id=3603001)
    IfStandingOnCollision(-1, 3604005)
    IfStandingOnCollision(-1, 3604007)
    IfStandingOnCollision(-1, 3604012)
    IfStandingOnCollision(-1, 3604021)
    IfStandingOnCollision(-1, 3604023)
    IfStandingOnCollision(-1, 3604026)
    IfStandingOnCollision(-1, 3604027)
    IfStandingOnCollision(-1, 3604028)
    IfStandingOnCollision(-1, 3604029)
    IfStandingOnCollision(-1, 3604030)
    IfStandingOnCollision(-1, 3604031)
    IfStandingOnCollision(-1, 3604032)
    IfStandingOnCollision(-1, 3604033)
    IfStandingOnCollision(-1, 3604034)
    IfStandingOnCollision(-1, 3604035)
    IfStandingOnCollision(-1, 3604060)
    IfConditionTrue(0, input_condition=-1)
    EnableSoundEvent(sound_id=3603001)
    IfStandingOnCollision(-2, 3604005)
    IfStandingOnCollision(-2, 3604007)
    IfStandingOnCollision(-2, 3604012)
    IfStandingOnCollision(-2, 3604021)
    IfStandingOnCollision(-2, 3604023)
    IfStandingOnCollision(-2, 3604026)
    IfStandingOnCollision(-2, 3604027)
    IfStandingOnCollision(-2, 3604028)
    IfStandingOnCollision(-2, 3604029)
    IfStandingOnCollision(-2, 3604030)
    IfStandingOnCollision(-2, 3604031)
    IfStandingOnCollision(-2, 3604032)
    IfStandingOnCollision(-2, 3604033)
    IfStandingOnCollision(-2, 3604034)
    IfStandingOnCollision(-2, 3604035)
    IfStandingOnCollision(-2, 3604060)
    IfConditionFalse(0, input_condition=-2)
    Restart()


@NeverRestart(13601090)
def Event_13601090():
    """Event 13601090"""
    EndIfFlagEnabled(9468)
    DisableObject(3601090)
    IfFlagEnabled(0, 9468)
    EnableObject(3601090)


@NeverRestart(13601100)
def Event_13601100():
    """Event 13601100"""
    EndIfFlagEnabled(13604100)
    GotoIfFlagEnabled(Label.L0, flag=13601108)
    EnableFlag(13601106)
    EnableFlag(13601107)
    EndOfAnimation(obj=3601100, animation_id=0)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13601106)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13601107)
    EndOfAnimation(obj=3601100, animation_id=4)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13601107)
    EndOfAnimation(obj=3601100, animation_id=0)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)


@NeverRestart(13601101)
def Event_13601101():
    """Event 13601101"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13601108)
    IfFlagEnabled(1, 13604100)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13601106)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13601107)
    SkipLines(1)
    EnableFlag(13601107)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13601108)
    IfFlagDisabled(3, 13604100)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart(13601102)
def Event_13601102():
    """Event 13601102"""
    IfFlagEnabled(3, 13604100)
    IfFlagEnabled(3, 13601106)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(obj=3601100, animation_id=6)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13601108)
    IfFlagDisabled(1, 13604100)
    IfFlagDisabled(1, 13601106)
    IfCharacterInsideRegion(-1, PLAYER, region=3602102)
    IfObjectActivated(-1, obj_act_id=13604101)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13601107)
    IfFlagEnabled(2, 13601107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604100)
    EnableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 5, wait_for_completion=True)
    ForceAnimation(3601100, 6, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3602101)
    ForceAnimation(3601100, 7, wait_for_completion=True)
    DisableFlag(13604100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    Restart()


@NeverRestart(13601103)
def Event_13601103():
    """Event 13601103"""
    IfFlagEnabled(3, 13604100)
    IfFlagDisabled(3, 13601106)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(obj=3601100, animation_id=2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13601108)
    IfFlagDisabled(1, 13604100)
    IfFlagEnabled(1, 13601106)
    IfCharacterInsideRegion(-1, PLAYER, region=3602101)
    IfObjectActivated(-1, obj_act_id=13604102)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13601107)
    IfFlagDisabled(2, 13601107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604100)
    DisableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 1, wait_for_completion=True)
    ForceAnimation(3601100, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3602102)
    WaitFrames(frames=1)
    ForceAnimation(3601100, 3, wait_for_completion=True)
    DisableFlag(13604100)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Restart()


@NeverRestart(13601104)
def Event_13601104():
    """Event 13601104"""
    DisableNetworkSync()
    IfFlagDisabled(1, 13601108)
    IfActionButtonParam(1, action_button_id=7100, entity=3601101)
    IfFlagDisabled(2, 13601108)
    IfActionButtonParam(2, action_button_id=7100, entity=3601102)
    IfFlagEnabled(3, 13604100)
    IfActionButtonParam(3, action_button_id=7100, entity=3601101)
    IfFlagEnabled(4, 13604100)
    IfActionButtonParam(4, action_button_id=7100, entity=3601102)
    IfFlagEnabled(5, 13601106)
    IfActionButtonParam(5, action_button_id=7100, entity=3601101)
    IfFlagDisabled(6, 13601106)
    IfActionButtonParam(6, action_button_id=7100, entity=3601102)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13601105)
def Event_13601105():
    """Event 13601105"""
    EndIfFlagEnabled(13601108)
    IfCharacterInsideRegion(0, PLAYER, region=3602100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    EnableFlag(13601108)


@NeverRestart(13601140)
def Event_13601140(_, entity: int, collision: int):
    """Event 13601140"""
    IfMovingOnCollision(0, collision)
    ForceAnimation(entity, 0, wait_for_completion=True)
    Restart()


@NeverRestart(13601200)
def Event_13601200(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 13601200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(13601312)
def Event_13601312():
    """Event 13601312"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=3601305, animation_id=1)
    WaitFrames(frames=1)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfActionButtonParam(0, action_button_id=3600000, entity=3601305)
    Move(PLAYER, destination=3601305, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 101330)
    ForceAnimation(3601305, 1, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)


@NeverRestart(13601210)
def Event_13601210(_, action_button_id: int, entity: int, flag: int):
    """Event 13601210"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParam(1, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    DisplayDialog(text=10010161, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13601400)
def Event_13601400():
    """Event 13601400"""
    DisableNetworkSync()
    IfInsideMap(0, game_map=FISHING_HAMLET)
    DeleteVFX(3503120)


@RestartOnRest(13604400)
def Event_13604400(_, obj__projectile_id: int):
    """Event 13604400"""
    EndIfThisEventSlotFlagEnabled()
    RestoreObject(obj__projectile_id)
    IfAttackedWithDamageType(-1, attacked_entity=obj__projectile_id, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=obj__projectile_id, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, obj__projectile_id, ComparisonType.LessThanOrEqual, value=999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj__projectile_id)
    PlaySoundEffect(obj__projectile_id, 299961000, sound_type=SoundType.o_Object)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6320,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj__projectile_id)
    PlaySoundEffect(obj__projectile_id, 299961000, sound_type=SoundType.o_Object)


@NeverRestart(13601800)
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

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 3600800)
    IfCharacterDead(2, 3600801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3601800)
    DisableObject(3601801)
    DeleteVFX(3603800)
    DeleteVFX(3603801)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    KillBoss(game_area_param_id=3600800)
    SkipLines(1)
    KillBoss(game_area_param_id=3600801)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
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

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(13604811)
def Event_13604811():
    """Event 13604811"""
    EndIfFlagEnabled(13601800)
    EndIfFlagEnabled(13601801)
    DisableCharacter(3600800)
    IfFlagDisabled(1, 13601800)
    IfFlagDisabled(1, 13601801)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3602805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13604810)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    DeleteVFX(3603860)
    EnableFlag(9180)


@NeverRestart(13601801)
def Event_13601801():
    """Event 13601801"""
    EndIfFlagEnabled(13601800)
    EndIfThisEventFlagEnabled()
    IfCharacterType(1, PLAYER, character_type=CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagDisabled(2, 13601800)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(2, 13604811)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3602805)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(36000000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(36000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    CreateVFX(3603860)
    EnableFlag(13604808)
    EnableCharacter(3600800)
    EndIfFlagEnabled(9347)
    RunEvent(9350, slot=0, args=(5,))
    EnableFlag(9347)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


@NeverRestart(13601802)
def Event_13601802():
    """Event 13601802"""
    DisableAI(3600802)
    DisableHealthBar(3600802)
    DisableGravity(3600802)
    IfCharacterBackreadEnabled(0, 3600802)
    Move(3600802, destination=3601802, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    ForceAnimation(3600802, 7000, loop=True)
    EndIfFlagEnabled(13601803)
    GotoIfThisEventFlagDisabled(Label.L0)
    ForceAnimation(3600802, 0, loop=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 13601800)
    ForceAnimation(3600802, 7001)


@NeverRestart(13601803)
def Event_13601803():
    """Event 13601803"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableObject(3601811)
    IfCharacterDead(0, 3600802)
    DisplayBanner(BannerType.NightmareSlain)
    Wait(5.0)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)

    # --- 0 --- #
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
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(3601810)
    EnableObject(3601811)
    EndIfThisEventFlagEnabled()
    EnableFlag(9180)
    PlayCutscene(36000010, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(3601810)
    EnableObject(3601811)
    DisableFlag(9180)
    EnableFlag(9469)
    RunEvent(9350, slot=0, args=(3,))


@NeverRestart(13601804)
def Event_13601804():
    """Event 13601804"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13604808)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(3600800)
    EnableFlag(13604808)
    EnableFlag(13601801)


@NeverRestart(13604800)
def Event_13604800():
    """Event 13604800"""
    EndIfFlagEnabled(13601800)
    GotoIfFlagEnabled(Label.L0, flag=13601801)
    SkipLinesIfClient(2)
    DisableObject(3601800)
    DeleteVFX(3603800, erase_root_only=False)
    IfFlagDisabled(1, 13601800)
    IfFlagEnabled(1, 13601801)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3601800)
    EnableObject(3601801)
    CreateVFX(3603800)
    CreateVFX(3603801)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13601800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=3600800, entity=3601800)
    IfFlagEnabled(3, 13601800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 3602800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3602801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(13604808)
    Restart()


@NeverRestart(13604801)
def Event_13604801():
    """Event 13604801"""
    DisableNetworkSync()
    EndIfFlagEnabled(13601800)
    IfFlagDisabled(1, 13601800)
    IfFlagEnabled(1, 13601801)
    IfFlagEnabled(1, 13604808)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=3600800, entity=3601800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3602800, animation=101130, wait_for_completion=True)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3602801)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(13604809)
    Restart()


@NeverRestart(13604802)
def Event_13604802():
    """Event 13604802"""
    EndIfFlagEnabled(13601800)
    DisableAI(3600800)
    DisableAI(3600801)
    DisableHealthBar(3600800)
    DisableHealthBar(3600801)
    ReferDamageToEntity(3600800, target_entity=3600801)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 13604808)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13604810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3600800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3600801, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13604810)
    EnableFlag(13604808)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3600800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(3600801, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600801)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3600800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(3600801, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3600801)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableBossHealthBar(3600801, name=453000)
    EnableFlag(13604812)
    GotoIfThisEventFlagEnabled(Label.L5)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=3600800, radius=24.0)
    IfAttackedWithDamageType(-2, attacked_entity=3600800)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 5 --- #
    DefineLabel(5)
    SkipLinesIfFlagEnabled(4, 13604820)
    EnableAI(3600800)
    SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLines(3)
    EnableAI(3600801)
    SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreatePlayLog(name=42)
    StartPlayLogMeasurement(measurement_id=3600010, name=58, overwrite=True)


@NeverRestart(13604803)
def Event_13604803():
    """Event 13604803"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3603802)
    DisableSoundEvent(sound_id=3603803)
    EndIfFlagEnabled(13601800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(1, 13601800)
    IfFlagEnabled(1, 13604812)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13604809)
    IfCharacterInsideRegion(1, PLAYER, region=3602802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=3603802)
    IfFlagEnabled(2, 13604820)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13601800)
    IfFlagEnabled(2, 13604812)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13604809)
    IfCharacterInsideRegion(2, PLAYER, region=3602802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=3603802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3603803)


@NeverRestart(13604804)
def Event_13604804():
    """Event 13604804"""
    DisableNetworkSync()
    EndIfFlagEnabled(13601800)
    GotoIfFlagEnabled(Label.L0, flag=13604820)
    IfCharacterAlive(1, 3600800)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3600800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(2, 3600800)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=3600800, radius=12.5)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterAlive(3, 3600800)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=3600801, radius=12.0)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(4, 3600800)
    IfEntityBeyondDistance(4, entity=PLAYER, other_entity=3600801, radius=12.5)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


@NeverRestart(13604805)
def Event_13604805():
    """Event 13604805"""
    DisableNetworkSync()
    EndIfFlagEnabled(13601800)
    IfFlagEnabled(0, 13601800)
    DisableBossMusic(sound_id=3603802)
    DisableBossMusic(sound_id=3603803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(13604806)
def Event_13604806():
    """Event 13604806"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3601800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13604807)
def Event_13604807():
    """Event 13604807"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=3601800, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3601800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13604820)
def Event_13604820():
    """Event 13604820"""
    EndIfFlagEnabled(13601800)
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3600800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(3600801)
    IfHealthLessThan(0, 3600800, value=0.5)
    AICommand(3600800, command_id=100, command_slot=0)
    ReplanAI(3600800)
    IfCharacterHasTAEEvent(0, 3600800, tae_event_id=100)
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
    IfCharacterHasTAEEvent(0, 3600801, tae_event_id=50)
    CancelSpecialEffect(3600801, 5300)
    AddSpecialEffect(3600801, 5333)
    EnableAI(3600801)


@NeverRestart(13604830)
def Event_13604830():
    """Event 13604830"""
    EndIfFlagEnabled(13601800)
    IfCharacterHasTAEEvent(0, 3600801, tae_event_id=100)
    AICommand(3600803, command_id=10, command_slot=0)
    ReplanAI(3600803)
    IfCharacterHasSpecialEffect(0, 3600803, 5020)
    AICommand(3600803, command_id=20, command_slot=0)
    ReplanAI(3600803)
    IfCharacterHasTAEEvent(0, 3600803, tae_event_id=10)
    AICommand(3600803, command_id=-1, command_slot=0)
    CancelSpecialEffect(3600803, 5020)
    ReplanAI(3600803)
    Restart()


@NeverRestart(13604840)
def Event_13604840():
    """Event 13604840"""
    DisableNetworkSync()
    EndIfFlagEnabled(13601800)
    IfCharacterHasTAEEvent(1, 3600800, tae_event_id=30)
    IfCharacterHasSpecialEffect(1, PLAYER, 8055)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 8054)
    IfCharacterHasTAEEvent(-1, 3600800, tae_event_id=40)
    IfTimeElapsed(-1, seconds=4.5)
    IfEntityBeyondDistance(-1, entity=3600800, other_entity=PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 8054)
    Restart()


@NeverRestart(13604850)
def Event_13604850():
    """Event 13604850"""
    DisableNetworkSync()
    EndIfFlagEnabled(13601800)
    IfCharacterHasSpecialEffect(0, 3600801, 5036)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=1)
    IfCharacterDoesNotHaveSpecialEffect(0, 3600801, 5036)
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
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterInsideRegion(-2, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(seconds)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfEqual(1, left=left, right=0)
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
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 0 --- #
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
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    Wait(seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    WaitFrames(frames=frames)

    # --- 0 --- #
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
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, character_1, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character_1, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 0 --- #
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
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    EnableGravity(character)
    EnableCharacterCollision(character)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605520)
def Event_13605520(_, character: int, region: int, ai_param_id: int, ai_param_id_1: int):
    """Event 13605520"""
    IfAllPlayersOutsideRegion(1, region=region)
    IfConditionFalse(0, input_condition=1)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfAllPlayersOutsideRegion(0, region=region)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    Restart()


@RestartOnRest(13605540)
def Event_13605540(_, character: int, region: int, radius: float, ai_param_id: int, ai_param_id_1: int):
    """Event 13605540"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfCharacterInsideRegion(1, character, region=region)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13605560)
def Event_13605560(_, character: int, region: int, radius: float):
    """Event 13605560"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=character)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(character)


@RestartOnRest(13605600)
def Event_13605600(_, character__set_draw_parent: int, character: int):
    """Event 13605600"""
    DisableGravity(character)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, character__set_draw_parent)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, character__set_draw_parent, value=0.0)
    SkipLinesIfConditionFalse(2, 1)
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
    IfCharacterHasSpecialEffect(1, PLAYER, 4691)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfCharacterHasSpecialEffect(0, PLAYER, 4690)
    Wait(2.0)
    IfCharacterHasSpecialEffect(2, PLAYER, 4690)
    IfCharacterDoesNotHaveSpecialEffect(3, PLAYER, 4690)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(input_condition=3)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(PLAYER, 4691)
    Restart()


@RestartOnRest(13605606)
def Event_13605606():
    """Event 13605606"""
    DisableNetworkSync()
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 4690)
    IfCharacterHasSpecialEffect(1, PLAYER, 4691)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 4691)
    Restart()


@RestartOnRest(13605700)
def Event_13605700(_, character: int, animation: int, flag: int):
    """Event 13605700"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    RotateToFaceEntity(character, PLAYER, animation=animation, wait_for_completion=True)

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest(13605720)
def Event_13605720(_, character: int):
    """Event 13605720"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    MoveObjectToCharacter(3601799, character=PLAYER)
    WaitFrames(frames=1)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=3601799,
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
    IfCharacterType(1, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(1)
    IfCharacterInsideRegion(0, PLAYER, region=3602798)
    MoveObjectToCharacter(3601798, character=PLAYER)
    WaitFrames(frames=1)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=3601798,
        model_point=200,
        behavior_id=6330,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfCharacterOutsideRegion(0, PLAYER, region=3602798)
    Restart()


@RestartOnRest(13605740)
def Event_13605740(_, character: int, region: int, region_1: int, radius: float):
    """Event 13605740"""
    EndIfThisEventFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, condition=3)
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
    IfHasAIStatus(-1, 3600201, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 3600201, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    SkipLinesIfFlagEnabled(2, 53600100)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3600201, radius=12.0)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=3602201)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    RotateToFaceEntity(3600201, PLAYER, animation=7007)
    EnableGravity(3600201)
    EnableCharacterCollision(3600201)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(3600201, ai_param_id=404000)


@RestartOnRest(13605751)
def Event_13605751():
    """Event 13605751"""
    IfCharacterHasTAEEvent(0, 3600330, tae_event_id=100)
    SetAIParamID(3600208, ai_param_id=404002)
    SetAIParamID(3600209, ai_param_id=404002)
    MoveObjectToCharacter(3601799, character=PLAYER)
    WaitFrames(frames=1)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=3601799,
        model_point=200,
        behavior_id=6300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@RestartOnRest(13605752)
def Event_13605752():
    """Event 13605752"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3602315)
    IfAttackedWithDamageType(2, attacked_entity=3600315)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SetNest(3600315, region=3602316)
    AICommand(3600315, command_id=10, command_slot=0)
    ReplanAI(3600315)
    IfCharacterInsideRegion(0, 3600315, region=3602316)
    AICommand(3600315, command_id=-1, command_slot=0)
    ReplanAI(3600315)


@RestartOnRest(13605760)
def Event_13605760():
    """Event 13605760"""
    EndIfThisEventFlagEnabled()
    IfHealthLessThan(0, 3600302, value=0.5)
    SetNest(3600302, region=3602303)
    AICommand(3600302, command_id=10, command_slot=0)
    ReplanAI(3600302)
    IfCharacterInsideRegion(0, 3600302, region=3602303)
    AICommand(3600302, command_id=-1, command_slot=0)
    ReplanAI(3600302)


@RestartOnRest(13605761)
def Event_13605761():
    """Event 13605761"""
    EndIfThisEventFlagEnabled()
    DisableAI(3600303)
    ForceAnimation(3600303, 7004, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3602304)
    IfHealthLessThan(1, 3600302, value=0.5)
    IfHealthLessThan(2, 3600302, value=0.4000000059604645)
    IfAttackedWithDamageType(3, attacked_entity=3600303)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(3600303, 7005)
    EnableAI(3600303)


@RestartOnRest(13605762)
def Event_13605762():
    """Event 13605762"""
    EndIfFlagEnabled(53600800)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterDead(2, 3600302)
    IfCharacterDead(2, 3600303)
    IfConditionTrue(0, input_condition=2)
    AwardItemLot(3601100, host_only=True)


@RestartOnRest(13605770)
def Event_13605770(_, character: int, region: int, min_seconds: float, max_seconds: float):
    """Event 13605770"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfAttackedWithDamageType(2, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
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
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_2)
    EndIfFlagEnabled(flag_1)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)


@RestartOnRest(13605910)
def Event_13605910(_, flag: int, flag_1: int, flag_2: int, region: int, region_1: int):
    """Event 13605910"""
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_2)
    EndIfFlagEnabled(flag_1)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagEnabled(1, flag)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
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
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfFlagDisabled(1, 1730)
    IfFlagEnabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    CancelSpecialEffect(character, 5560)
    AddSpecialEffect(character, 8060)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    ForceAnimation(character, 101203)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    CancelSpecialEffect(character, 5560)
    EnableFlag(flag)
    DisableFlag(flag_3)
    IfFlagEnabled(0, flag_3)
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
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfFlagDisabled(1, 1730)
    IfFlagEnabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=2)
    IfCharacterInsideRegion(3, PLAYER, region=region_1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, condition=3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=3604027)
    SkipLines(1)
    Move(character, destination=3602917, destination_type=CoordEntityType.Region, set_draw_parent=3604027)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    CancelSpecialEffect(character, 5560)
    AddSpecialEffect(character, 8060)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    ForceAnimation(character, 101203)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    CancelSpecialEffect(character, 5560)
    EnableFlag(flag)
    DisableFlag(flag_3)
    IfFlagEnabled(0, flag_3)
    Restart()


@RestartOnRest(13605930)
def Event_13605930(_, character: int, flag: int, flag_1: int, region: int, region_1: int, flag_2: int):
    """Event 13605930"""
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    Wait(2.0)
    EnableInvincibility(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5560)
    CancelSpecialEffect(character, 8060)
    CancelSpecialEffect(character, 1130)
    CancelSpecialEffect(character, 1150)
    PlaySoundEffect(PLAYER, 122, sound_type=SoundType.s_SFX)
    Wait(4.0)
    EnableFlag(flag_2)
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    Restart()


@RestartOnRest(13605940)
def Event_13605940(_, character: int, flag: int, flag_1: int, item_lot_param_id: int, character_1: int):
    """Event 13605940"""
    DisableBackread(character_1)
    GotoIfFlagDisabled(Label.L0, flag=1730)
    DropMandatoryTreasure(character_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterDead(1, character)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(character, 8060)
    CancelSpecialEffect(character, 1130)
    CancelSpecialEffect(character, 1150)
    PlaySoundEffect(PLAYER, 122, sound_type=SoundType.s_SFX)
    EnableFlag(flag_1)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionFalse(1, 2)
    AwardItemLot(item_lot_param_id, host_only=True)


@NeverRestart(13600900)
def Event_13600900(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 13600900"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    IfCharacterDead(1, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(13600940)
def Event_13600940(_, character: int):
    """Event 13600940"""
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlagRange((1770, 1789))
    EnableFlag(1780)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L0, flag=1770)
    GotoIfFlagEnabled(Label.L1, flag=1780)
    DisableBackread(character)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(73600310)
    DisableFlag(73600314)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    SetDistanceLimitForConversationStateChanges(character=character, distance=35.0)
    End()


@NeverRestart(13600943)
def Event_13600943(_, flag: int, item_lot_param_id: int):
    """Event 13600943"""
    EndIfFlagEnabled(flag)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    AwardItemLot(item_lot_param_id, host_only=False)


@NeverRestart(13600941)
def Event_13600941(_, flag: int, flag_1: int):
    """Event 13600941"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagDisabled(-1, flag)
    IfFlagEnabled(-1, flag_1)
    IfConditionTrue(0, input_condition=-1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    Restart()


@NeverRestart(13600942)
def Event_13600942(_, min_seconds: float, max_seconds: float):
    """Event 13600942"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(0, 73600310)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    SkipLinesIfFlagDisabled(3, 73600313)
    IfFlagDisabled(0, 73600314)
    DisableFlag(73600313)
    Restart()
    DisableFlag(73600310)
    Restart()


@NeverRestart(13600944)
def Event_13600944():
    """Event 13600944"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(73600318)
    IfCharacterInsideRegion(0, PLAYER, region=3602941)
    EnableFlag(73600318)
    IfCharacterOutsideRegion(0, PLAYER, region=3602941)
    Restart()


@NeverRestart(13600950)
def Event_13600950(_, character: int):
    """Event 13600950"""
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L8, input_condition=-15)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagRangeAnyEnabled(1, flag_range=(1720, 1722))
    IfFlagEnabled(1, 73400403)
    IfFlagEnabled(1, 1650)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(2, 1722)
    IfFlagEnabled(-2, 1660)
    IfFlagEnabled(-2, 1651)
    IfConditionTrue(2, input_condition=-2)
    IfFlagEnabled(2, 73500602)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(3, 1723)
    IfFlagEnabled(3, 73600501)
    GotoIfConditionFalse(Label.L3, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1713)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagRangeAnyEnabled(Label.L4, flag_range=(1710, 1712))
    GotoIfFlagEnabled(Label.L4, flag=1720)
    DisableObject(3600906)
    DisableTreasure(obj=3600906)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(3600906)
    EnableTreasure(obj=3600906)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    DisableTreasure(obj=3600906)
    GotoIfFlagRangeAnyEnabled(Label.L5, flag_range=(1710, 1712))
    GotoIfFlagEnabled(Label.L5, flag=1720)
    DisableObject(3600906)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(3600906)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=1723)
    GotoIfFlagEnabled(Label.L1, flag=1713)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103151)
    EnableImmortality(character)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableAnimations(character)
    ForceAnimation(character, 103157, skip_transition=True)
    End()


@NeverRestart(13600951)
def Event_13600951(_, character: int, flag: int, flag_1: int):
    """Event 13600951"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(flag)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(1, flag)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103152)
    IfFlagEnabled(2, flag_1)
    IfFlagDisabled(2, flag)
    IfHealthNotEqual(2, character, value=0.0)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(character, 103151)
    Restart()


@NeverRestart(13600952)
def Event_13600952(_, character: int, flag: int, flag_1: int):
    """Event 13600952"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(1, flag)
    IfAttackedWithDamageType(1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103153)
    Kill(character, award_souls=True)
    EnableFlag(flag_1)


@NeverRestart(13600953)
def Event_13600953(_, character: int):
    """Event 13600953"""
    IfFlagEnabled(-1, 1724)
    IfFlagRangeAnyEnabled(-1, flag_range=(1720, 1722))
    EndIfConditionFalse(-1)
    IfFlagEnabled(0, 1723)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 103151)
    EnableImmortality(character)
    DisableObject(3600906)
    DisableTreasure(obj=3600906)


@NeverRestart(13600954)
def Event_13600954(_, flag: int, flag_1: int, item_lot_param_id: int):
    """Event 13600954"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, flag_1)
    IfCharacterDead(1, 3600905)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(item_lot_param_id, host_only=False)


@NeverRestart(13600955)
def Event_13600955():
    """Event 13600955"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(1, 1723)
    IfFlagDisabled(1, 73600502)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(73600500)
    IfCharacterInsideRegion(0, PLAYER, region=3602850)
    DisableFlag(73600500)
    EnableFlag(73600502)


@NeverRestart(13600956)
def Event_13600956(_, character: int, flag: int, flag_1: int):
    """Event 13600956"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(flag_1)
    Kill(character)
    EnableFlag(73600530)
    ForceAnimation(character, 103156, wait_for_completion=True, skip_transition=True)
    ForceAnimation(character, 103157, skip_transition=True)


@NeverRestart(13600995)
def Event_13600995():
    """Event 13600995"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 13605952)
    DisableFlag(13605940)
