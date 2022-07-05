"""
linked:
164

strings:
0: PC情報_拠点到達時
22: ボス_撃破
34: PC情報_ボス撃破_拠点ボス
64: ボス_戦闘開始
80: ボス_撃破時間
96: PC情報_ボス撃破_拠点ボス2
128: ボス_戦闘開始2
146: ボス_撃破時間2
164: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_12100010()
    SkipLinesIfFlagDisabled(1, 9400)
    SetRespawnPoint(respawn_point=2102961)
    SkipLinesIfClient(2)
    SkipLinesIfFlagDisabled(1, 6600)
    EnableFlag(12101999)
    SkipLinesIfFlagEnabled(1, 12101999)
    DisableObject(2101100)
    SetNetworkUpdateRate(2100700, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(PLAYER, 110)
    AddSpecialEffect(PLAYER, 111)
    AddSpecialEffect(PLAYER, 112)
    AddSpecialEffect(PLAYER, 113)
    AddSpecialEffect(PLAYER, 114)
    AddSpecialEffect(PLAYER, 115)
    AddSpecialEffect(PLAYER, 116)
    DisableFlag(72100100)
    DisableFlag(72100101)
    DisableFlag(72100102)
    DisableFlag(72102110)
    DisableFlag(72102200)
    DisableFlag(72102201)
    DisableFlag(72102300)
    DisableFlag(72102301)
    DisableFlag(72102302)
    DisableFlag(72102400)
    DisableFlag(72102401)
    DisableFlag(72102410)
    DisableFlag(72102411)
    DisableFlag(72102412)
    DisableFlag(72102413)
    DisableFlag(72102420)
    DisableFlag(72102421)
    DisableFlag(72102422)
    DisableFlag(72102500)
    DisableFlag(72102501)
    DisableFlag(72102502)
    DisableFlag(72102600)
    DisableFlag(72102601)
    DisableFlag(72102602)
    DisableFlag(72102603)
    DisableFlag(72102700)
    DisableFlag(72102701)
    DisableFlag(72102800)
    DisableFlag(72102801)
    DisableFlag(72102802)
    DisableFlag(72102803)
    DisableFlag(72103200)
    DisableFlag(72103201)
    DisableFlag(72103202)
    DisableFlag(72103203)
    DisableFlag(72103300)
    DisableFlag(72103301)
    DisableFlag(72103400)
    DisableFlag(72103401)
    DisableFlag(72103402)
    DisableFlag(72103403)
    DisableFlag(72103500)
    DisableFlag(72103501)
    DisableFlag(72103502)
    DisableFlag(72103600)
    DisableFlag(72103601)
    DisableFlag(72103602)
    Event_12105210()
    Event_12107000(52, flag=72102110, target_entity=2100952, respawn_point_id=2112950)
    Event_12107000(0, flag=72102200, target_entity=2100951, respawn_point_id=2202950)
    Event_12107000(1, flag=72102201, target_entity=2100951, respawn_point_id=2202951)
    Event_12107000(5, flag=72102300, target_entity=2100950, respawn_point_id=2302950)
    Event_12107000(6, flag=72102301, target_entity=2100950, respawn_point_id=2302951)
    Event_12107000(7, flag=72102302, target_entity=2100950, respawn_point_id=2302952)
    Event_12107000(10, flag=72102400, target_entity=2100950, respawn_point_id=2402950)
    Event_12107000(11, flag=72102401, target_entity=2100950, respawn_point_id=2402951)
    Event_12107000(15, flag=72102410, target_entity=2100950, respawn_point_id=2412950)
    Event_12107000(16, flag=72102411, target_entity=2100950, respawn_point_id=2412951)
    Event_12107000(17, flag=72102412, target_entity=2100950, respawn_point_id=2412952)
    Event_12107000(18, flag=72102413, target_entity=2100950, respawn_point_id=2412953)
    Event_12107000(20, flag=72102420, target_entity=2100950, respawn_point_id=2422950)
    Event_12107000(21, flag=72102421, target_entity=2100950, respawn_point_id=2422951)
    Event_12107000(22, flag=72102422, target_entity=2100950, respawn_point_id=2422952)
    Event_12107000(25, flag=72102500, target_entity=2100952, respawn_point_id=2502950)
    Event_12107000(26, flag=72102501, target_entity=2100952, respawn_point_id=2502951)
    Event_12107000(27, flag=72102502, target_entity=2100952, respawn_point_id=2502952)
    Event_12107000(30, flag=72102600, target_entity=2100953, respawn_point_id=2602950)
    Event_12107000(31, flag=72102601, target_entity=2100953, respawn_point_id=2602951)
    Event_12107000(32, flag=72102602, target_entity=2100953, respawn_point_id=2602952)
    Event_12107000(33, flag=72102603, target_entity=2100953, respawn_point_id=2602953)
    Event_12107000(35, flag=72102700, target_entity=2100951, respawn_point_id=2702950)
    Event_12107000(36, flag=72102701, target_entity=2100951, respawn_point_id=2702951)
    Event_12107000(40, flag=72102800, target_entity=2100952, respawn_point_id=2802950)
    Event_12107000(41, flag=72102801, target_entity=2100952, respawn_point_id=2802951)
    Event_12107000(42, flag=72102802, target_entity=2100952, respawn_point_id=2802952)
    Event_12107000(43, flag=72102803, target_entity=2100952, respawn_point_id=2802953)
    Event_12107000(45, flag=72103200, target_entity=2100951, respawn_point_id=3202950)
    Event_12107000(46, flag=72103201, target_entity=2100953, respawn_point_id=3202951)
    Event_12107000(47, flag=72103202, target_entity=2100951, respawn_point_id=3202952)
    Event_12107000(48, flag=72103203, target_entity=2100953, respawn_point_id=3202953)
    Event_12107000(50, flag=72103300, target_entity=2100953, respawn_point_id=3302950)
    Event_12107000(51, flag=72103301, target_entity=2100953, respawn_point_id=3302951)
    Event_12107000(55, flag=72103400, target_entity=2100231, respawn_point_id=3402950)
    Event_12107000(56, flag=72103401, target_entity=2100231, respawn_point_id=3402951)
    Event_12107000(57, flag=72103402, target_entity=2100231, respawn_point_id=3402952)
    Event_12107000(58, flag=72103403, target_entity=2100231, respawn_point_id=3402953)
    Event_12107000(60, flag=72103500, target_entity=2100231, respawn_point_id=3502950)
    Event_12107000(61, flag=72103501, target_entity=2100231, respawn_point_id=3502951)
    Event_12107000(62, flag=72103502, target_entity=2100231, respawn_point_id=3502952)
    Event_12107000(65, flag=72103600, target_entity=2100231, respawn_point_id=3602950)
    Event_12107000(66, flag=72103601, target_entity=2100231, respawn_point_id=3602951)
    Event_12107000(67, flag=72103602, target_entity=2100231, respawn_point_id=3602952)
    DisableFlag(72100420)
    DisableFlag(72100421)
    DisableFlag(72100422)
    DisableFlag(72100423)
    DisableFlag(72100424)
    DisableFlag(72100425)
    DisableFlag(72100426)
    Event_12107100(0, flag=72100420, target_entity=2100954, flag_1=9020)
    Event_12107100(1, flag=72100421, target_entity=2100955, flag_1=9021)
    Event_12107100(2, flag=72100422, target_entity=2100956, flag_1=9022)
    Event_12107100(3, flag=72100423, target_entity=2100957, flag_1=9023)
    Event_12107100(4, flag=72100424, target_entity=2100958, flag_1=9024)
    Event_12107100(5, flag=72100425, target_entity=2100959, flag_1=9025)
    Event_12107100(6, flag=72100426, target_entity=2100960, flag_1=9026)
    DisableFlag(72100300)
    DisableFlag(72100301)
    DisableFlag(72100302)
    DisableFlag(72100303)
    DisableFlag(72100304)
    DisableFlag(72100305)
    DisableFlag(72100306)
    DisableFlag(72100307)
    DisableFlag(72100308)
    DisableFlag(72100309)
    Event_12107200(0, flag=72100300, respawn_point_id=2902950, flag_1=9001)
    Event_12107200(1, flag=72100301, respawn_point_id=2902951, flag_1=9002)
    Event_12107200(2, flag=72100302, respawn_point_id=2902952, flag_1=9003)
    Event_12107200(3, flag=72100303, respawn_point_id=2902953, flag_1=9004)
    Event_12107200(4, flag=72100304, respawn_point_id=2902954, flag_1=9005)
    Event_12107200(5, flag=72100305, respawn_point_id=2902955, flag_1=9006)
    Event_12107200(6, flag=72100306, respawn_point_id=2902956, flag_1=9007)
    Event_12107200(7, flag=72100307, respawn_point_id=2902957, flag_1=9008)
    Event_12107200(8, flag=72100308, respawn_point_id=2902958, flag_1=9009)
    Event_12107200(9, flag=72100309, respawn_point_id=2902959, flag_1=9010)
    Event_12100300()
    Event_12100310()
    Event_12100800()
    Event_12100180()
    Event_12101800()
    Event_12101801()
    Event_12101802()
    Event_12104810()
    Event_12104811()
    Event_12104802()
    Event_12104803()
    Event_12104804()
    Event_12104805()
    Event_12104807()
    Event_12104808()
    Event_12101803()
    Event_12100000()
    Event_12100002()
    Event_12101850()
    Event_12101851()
    Event_12101852()
    Event_12104880()
    Event_12104881()
    Event_12104852()
    Event_12104853()
    Event_12104854()
    Event_12104855()
    Event_12101853()
    Event_12104860(
        0,
        npc_part_id=5,
        npc_part_id_1=5,
        part_index=1,
        part_health=100,
        special_effect_id=480,
        special_effect_id_1=490,
        animation_id=8000
    )
    Event_12104860(
        1,
        npc_part_id=6,
        npc_part_id_1=6,
        part_index=2,
        part_health=150,
        special_effect_id=481,
        special_effect_id_1=491,
        animation_id=8010
    )
    Event_12104860(
        2,
        npc_part_id=7,
        npc_part_id_1=7,
        part_index=3,
        part_health=150,
        special_effect_id=482,
        special_effect_id_1=492,
        animation_id=8030
    )
    Event_12104860(
        3,
        npc_part_id=8,
        npc_part_id_1=8,
        part_index=4,
        part_health=200,
        special_effect_id=483,
        special_effect_id_1=493,
        animation_id=8020
    )
    Event_12104860(
        4,
        npc_part_id=9,
        npc_part_id_1=9,
        part_index=5,
        part_health=200,
        special_effect_id=484,
        special_effect_id_1=494,
        animation_id=8040
    )
    Event_12104870()
    Event_12100400()
    Event_12100410(0, action_button_id=7002, anchor_entity=2101000, flag=9462, text=10010171)
    Event_12100410(1, action_button_id=7030, anchor_entity=2101010, flag=9403, text=10010171)
    Event_12100410(2, action_button_id=7030, anchor_entity=2101020, flag=9403, text=10010171)
    Event_12100410(3, action_button_id=7030, anchor_entity=2101030, flag=9403, text=10010171)
    Event_9401()
    Event_12100990()
    Event_12105000(0, entity=2100950, flag=12105030)
    Event_12105000(1, entity=2100951, flag=12105031)
    Event_12105000(2, entity=2100952, flag=12105032)
    Event_12105000(3, entity=2100953, flag=12105033)
    Event_12105004(3, character=2100231, flag=12105034)
    Event_12105020()
    Event_12105021()
    Event_12105022()
    Event_12105023()
    Event_12105024()
    Event_12105040()
    Event_12101000(0, item=4110, character=2100211, bit_index=1, bit_index_1=10)
    Event_12101000(1, item=4111, character=2100211, bit_index=2, bit_index_1=13)
    Event_12101000(2, item=4112, character=2100211, bit_index=3, bit_index_1=15)
    Event_12101000(3, item=4113, character=2100212, bit_index=0, bit_index_1=15)
    Event_12101000(4, item=4114, character=2100212, bit_index=1, bit_index_1=12)
    Event_12101000(5, item=4115, character=2100212, bit_index=2, bit_index_1=11)
    Event_12101000(6, item=4116, character=2100212, bit_index=3, bit_index_1=15)
    Event_12101000(7, item=4117, character=2100213, bit_index=0, bit_index_1=15)
    Event_12101000(8, item=4118, character=2100213, bit_index=1, bit_index_1=15)
    Event_12101000(9, item=4119, character=2100213, bit_index=2, bit_index_1=15)
    Event_12101010()
    Event_12105043()
    Event_12101020()
    Event_12101021()
    Event_12101022()
    Event_12101024()
    Event_12101026()
    Event_12101028()
    Event_12105010()
    Event_12105011()
    Event_12105012()
    Event_12105013()
    Event_12105014()
    Event_12105015()
    Event_12105016()
    Event_12105310(0, flag=94005001, entity=2100954)
    Event_12105310(1, flag=94105001, entity=2100955)
    Event_12105310(2, flag=94205001, entity=2100956)
    Event_12105310(3, flag=94305001, entity=2100957)
    Event_12105310(4, flag=94405001, entity=2100958)
    Event_12105310(5, flag=94505001, entity=2100959)
    Event_12105310(6, flag=94605001, entity=2100960)
    Event_12100110()
    Event_12105200()
    Event_12100115()
    Event_12100116()
    Event_12100117()
    Event_12100120()
    Event_12100121()
    Event_12100123()
    Event_12100112()
    Event_12100113()
    Event_12100114()
    Event_12100160()
    Event_12100162()
    Event_12100163()
    Event_12100164()
    Event_12100165()
    DisableHealthBar(2100600)
    Event_12105060()
    Event_12105062()
    Event_12105070(0, flag=72100141, flag_1=6011, bit_index=20)
    Event_12105070(1, flag=72100142, flag_1=6012, bit_index=21)
    Event_12105070(2, flag=72100143, flag_1=6013, bit_index=22)
    Event_12105070(3, flag=72100144, flag_1=6014, bit_index=23)
    Event_12105070(4, flag=72100145, flag_1=6015, bit_index=24)
    Event_12105070(5, flag=72100146, flag_1=6016, bit_index=25)
    Event_12105070(6, flag=72100147, flag_1=6017, bit_index=26)
    Event_12105070(7, flag=72100148, flag_1=6018, bit_index=27)
    Event_12105070(8, flag=72100149, flag_1=6019, bit_index=28)
    Event_12105070(9, flag=72100150, flag_1=6020, bit_index=0)
    Event_12105070(10, flag=72100151, flag_1=6021, bit_index=0)
    Event_12105070(11, flag=72100152, flag_1=6022, bit_index=0)
    Event_12105070(12, flag=72100153, flag_1=6023, bit_index=0)
    Event_12105070(13, flag=72100154, flag_1=6024, bit_index=0)
    Event_12105070(14, flag=72100155, flag_1=6025, bit_index=0)
    Event_12100020(0, item=4900, flag=6071, left=1)
    Event_12100020(1, item=4901, flag=6072, left=1)
    Event_12100020(2, item=4902, flag=6073, left=1)
    Event_12100020(3, item=4903, flag=6074, left=0)
    Event_12100020(4, item=4904, flag=6075, left=0)
    Event_12100020(5, item=4905, flag=6076, left=0)
    Event_12100020(6, item=4906, flag=6077, left=0)
    Event_12100020(7, item=4907, flag=6078, left=0)
    Event_12100020(8, item=4908, flag=6079, left=0)
    Event_12100020(9, item=4909, flag=6080, left=0)
    Event_12100020(10, item=4910, flag=6081, left=0)
    Event_12100020(11, item=4911, flag=6082, left=0)
    Event_12100020(12, item=4912, flag=6083, left=0)
    Event_12100020(13, item=4913, flag=6084, left=0)
    Event_12100020(14, item=4914, flag=6085, left=0)
    Event_12105064()
    Event_12101100()
    Event_12105300()
    AddSpecialEffect(PLAYER, 9121)
    SkipLinesIfFlagEnabled(1, 12101802)
    AddSpecialEffect(PLAYER, 9120)
    Event_12100330()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    SkipLinesIfFlagDisabled(2, 12101020)
    DisableBackread(2100215)
    DisableBackread(2100220)
    SkipLinesIfFlagDisabled(2, 12101021)
    DisableBackread(2100216)
    DisableBackread(2100221)
    SkipLinesIfFlagEnabled(2, 9462)
    DisableBackread(2100800)
    DisableBackread(2100810)
    SkipLinesIfFlagEnabled(1, 12101802)
    EnableFlag(2100)
    GotoIfFlagDisabled(Label.L0, flag=1003)
    DisableFlag(1003)
    DisableFlag(72100110)
    DisableFlag(72100111)
    DisableFlag(72100112)
    DisableFlag(72100113)
    DisableFlag(72100114)
    GotoIfFlagDisabled(Label.L1, flag=9462)
    EnableFlag(1002)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(1000)

    # --- 0 --- #
    DefineLabel(0)
    Event_12100100(0, first_flag=1000, last_flag=1019)
    Event_12100101(0, first_flag=1000, last_flag=1019)
    Event_12100140(0, first_flag=1020, last_flag=1039)
    Event_12100141(0, first_flag=1020, last_flag=1039)
    Event_12100142(0, first_flag=1020, last_flag=1039)
    Event_12100143(0, first_flag=1020, last_flag=1039)
    Event_12100144(0, first_flag=1020, last_flag=1039)
    Event_12100145(0, first_flag=1020, last_flag=1039)
    Event_12100146()
    DisableAnimations(2100200)
    DisableAnimations(2100201)
    DisableAnimations(2100202)
    DisableAnimations(2100203)
    DisableAnimations(2100211)
    DisableAnimations(2100212)
    DisableAnimations(2100219)
    DisableAnimations(2100214)
    DisableAnimations(2100215)
    DisableAnimations(2100216)
    DisableAnimations(2100217)
    DisableAnimations(2100218)
    DisableAnimations(2100220)
    DisableAnimations(2100221)
    DisableAnimations(2100222)
    DisableAnimations(2100230)
    DisableAnimations(2100231)
    DisableAnimations(2100950)
    DisableAnimations(2100951)
    DisableAnimations(2100952)
    DisableAnimations(2100953)
    DisableAnimations(2100954)
    DisableAnimations(2100955)
    DisableAnimations(2100956)
    DisableAnimations(2100957)
    DisableAnimations(2100958)
    DisableAnimations(2100959)
    DisableAnimations(2100960)
    DisableGravity(2100200)
    DisableGravity(2100201)
    DisableGravity(2100202)
    DisableGravity(2100203)
    DisableGravity(2100211)
    DisableGravity(2100212)
    DisableGravity(2100219)
    DisableGravity(2100214)
    DisableGravity(2100215)
    DisableGravity(2100216)
    DisableGravity(2100217)
    DisableGravity(2100218)
    DisableGravity(2100220)
    DisableGravity(2100221)
    DisableGravity(2100222)
    DisableGravity(2100230)
    DisableGravity(2100231)
    DisableGravity(2100950)
    DisableGravity(2100951)
    DisableGravity(2100952)
    DisableGravity(2100953)
    DisableGravity(2100954)
    DisableGravity(2100955)
    DisableGravity(2100956)
    DisableGravity(2100957)
    DisableGravity(2100958)
    DisableGravity(2100959)
    DisableGravity(2100960)
    DisableCharacterCollision(2100200)
    DisableCharacterCollision(2100201)
    DisableCharacterCollision(2100202)
    DisableCharacterCollision(2100203)
    DisableCharacterCollision(2100211)
    DisableCharacterCollision(2100212)
    DisableCharacterCollision(2100219)
    DisableCharacterCollision(2100214)
    DisableCharacterCollision(2100215)
    DisableCharacterCollision(2100216)
    DisableCharacterCollision(2100217)
    DisableCharacterCollision(2100218)
    DisableCharacterCollision(2100220)
    DisableCharacterCollision(2100221)
    DisableCharacterCollision(2100222)
    DisableCharacterCollision(2100230)
    DisableCharacterCollision(2100231)
    DisableCharacterCollision(2100950)
    DisableCharacterCollision(2100951)
    DisableCharacterCollision(2100952)
    DisableCharacterCollision(2100953)
    DisableCharacterCollision(2100954)
    DisableCharacterCollision(2100955)
    DisableCharacterCollision(2100956)
    DisableCharacterCollision(2100957)
    DisableCharacterCollision(2100958)
    DisableCharacterCollision(2100959)
    DisableCharacterCollision(2100960)
    SkipLinesIfFlagDisabled(2, 12411000)
    DisableBackread(2100800)
    DisableBackread(2100810)


@NeverRestart(9401)
def Event_9401():
    """Event 9401"""
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventFlagEnabled()
    EnableFlag(9180)
    PlayCutscene(21000000, cutscene_flags=CutsceneFlags.FadeOut, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(12417810)


@NeverRestart(12100000)
def Event_12100000():
    """Event 12100000"""
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 12101800)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2103601)
    IfPlayerStandingOnCollision(-1, 2103602)
    IfPlayerStandingOnCollision(-1, 2103603)
    IfPlayerStandingOnCollision(-1, 2103604)
    IfPlayerStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 9900)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DeleteVFX(2103300)
    DeleteVFX(2103500)
    DeleteVFX(2103501)
    DeleteVFX(2103502)
    DeleteVFX(2103503)
    DeleteVFX(2103504)
    DeleteVFX(2103505)
    DeleteVFX(2103506)
    DeleteVFX(2103507)
    DeleteVFX(2103510)
    DeleteVFX(2103511)
    DeleteVFX(2103512)
    DeleteVFX(2103513)
    DeleteVFX(2103514)
    DeleteVFX(2103515)
    DeleteVFX(2103516)
    DeleteVFX(2103517)
    DeleteVFX(2103518)
    DeleteVFX(2103519)
    DeleteVFX(2103520)
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(21000020, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    AwardAchievement(achievement_id=2)
    Event_12100450()
    Event_12100451()
    Event_12100452()
    WaitFrames(frames=1)
    IncrementNewGameCycle(dummy_arg=1)
    EnableFlag(6604)
    EnableFlag(6601)
    EnableFlag(6603)
    EnableFlag(22)


@NeverRestart(12100002)
def Event_12100002():
    """Event 12100002"""
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 12101850)
    IfPlayerStandingOnCollision(-1, 2103601)
    IfPlayerStandingOnCollision(-1, 2103602)
    IfPlayerStandingOnCollision(-1, 2103603)
    IfPlayerStandingOnCollision(-1, 2103604)
    IfPlayerStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    EnableFlag(9180)
    WaitFrames(frames=1)
    DeleteVFX(2103300)
    DeleteVFX(2103500)
    DeleteVFX(2103501)
    DeleteVFX(2103502)
    DeleteVFX(2103503)
    DeleteVFX(2103504)
    DeleteVFX(2103505)
    DeleteVFX(2103506)
    DeleteVFX(2103507)
    GotoIfPlayerGender(Label.L0, gender=Gender.Male)
    PlayCutscene(21000030, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(21001030, cutscene_flags=0, player_id=10000)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    AwardAchievement(achievement_id=3)
    Event_12100450()
    Event_12100451()
    Event_12100452()
    WaitFrames(frames=1)
    IncrementNewGameCycle(dummy_arg=1)
    EnableFlag(6604)
    EnableFlag(6602)
    EnableFlag(6603)
    EnableFlag(23)


@NeverRestart(12100010)
def Event_12100010():
    """Event 12100010"""
    IfFlagDisabled(1, 9403)
    IfCharacterInsideRegion(1, PLAYER, region=2102100)
    IfConditionTrue(0, input_condition=1)
    DisableObject(2101010)
    EnableObject(2101011)
    DisableObject(2101020)
    EnableObject(2101021)
    DisableObject(2101030)
    EnableObject(2101031)


@NeverRestart(12100020)
def Event_12100020(_, item: int, flag: int, left: int):
    """Event 12100020"""
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfValueEqual(1, left=left, right=0)
    DisableFlag(flag)
    IfPlayerHasGood(0, item)
    EnableFlag(flag)


@NeverRestart(12100100)
def Event_12100100(_, first_flag: int, last_flag: int):
    """Event 12100100"""
    IfFlagDisabled(1, 1003)
    IfFlagEnabled(1, 9462)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1002)


@NeverRestart(12100101)
def Event_12100101(_, first_flag: int, last_flag: int):
    """Event 12100101"""
    IfCharacterDead(0, 2100700)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1003)
    SaveRequest()


@NeverRestart(12100110)
def Event_12100110():
    """Event 12100110"""
    DisableFlag(72100105)
    DisableFlag(72100106)
    DisableFlag(72100107)
    DisableFlag(12100510)
    IfFlagDisabled(-1, 9401)
    IfPlayerInsightAmountEqual(-1, value=0)
    GotoIfConditionTrue(Label.L9, input_condition=-1)
    EnableFlag(12100105)
    EnableFlag(9404)
    IfFlagEnabled(1, 13501800)
    IfFlagDisabled(1, 72100116)
    IfConditionTrue(-2, input_condition=1)
    IfFlagEnabled(2, 13601800)
    IfFlagDisabled(2, 72100117)
    IfFlagEnabled(-3, 1026)
    IfFlagEnabled(-3, 1027)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-2, input_condition=2)
    EndIfConditionTrue(-2)
    EndIfFlagEnabled(1000)
    GotoIfFlagEnabled(Label.L0, flag=1001)
    EndIfFlagEnabled(1002)
    GotoIfFlagEnabled(Label.L4, flag=1003)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(2, 100)
    DisableFlagRange((12100500, 12100509))
    EnableRandomFlagInRange(flag_range=(12100500, 12100509))
    SkipLinesIfFlagDisabled(1, 12105034)
    DisableFlagRange((12100501, 12100502))
    GotoIfFlagEnabled(Label.L1, flag=12100500)
    GotoIfFlagEnabled(Label.L2, flag=12100501)
    GotoIfFlagEnabled(Label.L3, flag=12100502)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(2100700, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9009, loop=True)
    Goto(Label.L8)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(12100510)
    Move(2100700, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9000, loop=True)
    Goto(Label.L8)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(12100510)
    SkipLinesIfFlagEnabled(2, 6600)
    DisableFlag(12100502)
    End()
    Move(2100700, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9000, loop=True)
    Goto(Label.L8)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagEnabled(Label.L5, flag=12100500)
    GotoIfFlagEnabled(Label.L6, flag=12100501)
    GotoIfFlagEnabled(Label.L7, flag=12100502)
    Move(2100700, destination=2102300, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 5 --- #
    DefineLabel(5)
    Move(2100700, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 6 --- #
    DefineLabel(6)
    Move(2100700, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 7 --- #
    DefineLabel(7)
    Move(2100700, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2100700)
    End()

    # --- 8 --- #
    DefineLabel(8)
    Event_12100111()
    End()

    # --- 9 --- #
    DefineLabel(9)
    Move(2100700, destination=2102304, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2100700, 9011, loop=True)
    EnableFlag(12105100)


@NeverRestart(12100111)
def Event_12100111():
    """Event 12100111"""
    GotoIfFlagEnabled(Label.L0, flag=12100500)
    GotoIfFlagEnabled(Label.L1, flag=12100501)
    GotoIfFlagEnabled(Label.L1, flag=12100502)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72100105)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagDisabled(9802)
    SkipLinesIfFlagEnabled(3, 102)
    DisableFlagRange((12100520, 12100524))
    EnableRandomFlagInRange(flag_range=(12100520, 12100524))
    EndIfFlagDisabled(12100520)
    EnableFlag(72100105)
    End()


@NeverRestart(12100112)
def Event_12100112():
    """Event 12100112"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72100100)
    GotoIfFlagEnabled(Label.L0, flag=1003)
    GotoIfFlagEnabled(Label.L1, flag=12105100)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100700, radius=1.0)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    RotateToFaceEntity(PLAYER, 2100700, animation=101290)
    IfCharacterHuman(2, PLAYER)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2100700, radius=1.0)
    IfConditionTrue(-1, input_condition=2)
    IfFramesElapsed(-1, frames=89)
    IfConditionTrue(0, input_condition=-1)

    # --- 2 --- #
    DefineLabel(2)
    RotateToFaceEntity(PLAYER, 2100700, animation=101270)
    WaitFrames(frames=0)
    EnableFlag(72100101)
    WaitFrames(frames=54)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(frames=19)
    DisableFlag(72100101)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=2100700, radius=1.5)
    GotoIfConditionTrue(Label.L3, input_condition=3)
    RotateToFaceEntity(PLAYER, 2100700, animation=101290)
    IfCharacterHuman(4, PLAYER)
    IfEntityWithinDistance(4, entity=PLAYER, other_entity=2100700, radius=1.5)
    IfConditionTrue(-2, input_condition=4)
    IfFramesElapsed(-2, frames=89)
    IfConditionTrue(0, input_condition=-2)

    # --- 3 --- #
    DefineLabel(3)
    RotateToFaceEntity(PLAYER, 2100700, animation=101280)
    WaitFrames(frames=0)
    EnableFlag(72100101)
    WaitFrames(frames=54)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(PLAYER, 101282)
    WaitFrames(frames=25)
    DisableFlag(72100101)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHuman(5, PLAYER)
    IfEntityWithinDistance(5, entity=PLAYER, other_entity=2100700, radius=2.0)
    GotoIfConditionTrue(Label.L4, input_condition=5)
    RotateToFaceEntity(PLAYER, 2100700, animation=101290)
    IfCharacterHuman(6, PLAYER)
    IfEntityWithinDistance(6, entity=PLAYER, other_entity=2100700, radius=2.0)
    IfConditionTrue(0, input_condition=6)

    # --- 4 --- #
    DefineLabel(4)
    RotateToFaceEntity(PLAYER, 2100700, animation=101270)
    WaitFrames(frames=0)
    EnableFlag(72100101)
    WaitFrames(frames=54)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(frames=19)
    DisableFlag(72100101)
    Restart()


@NeverRestart(12100113)
def Event_12100113():
    """Event 12100113"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(frames=1)
    IfHealthEqual(-1, 2100700, value=0.0)
    IfFlagEnabled(-1, 12105100)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    EnableFlag(72100102)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 72100100)
    RotateToFaceEntity(2100700, PLAYER, animation=7021)
    WaitFrames(frames=0)
    EnableFlag(72100102)
    WaitFrames(frames=89)
    ForceAnimation(2100700, 9010, loop=True)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(2100700, 7020)
    DisableFlag(72100102)
    WaitFrames(frames=92)
    Restart()


@NeverRestart(12100114)
def Event_12100114():
    """Event 12100114"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 7500)
    CreateTemporaryVFX(vfx_id=178, anchor_entity=PLAYER, model_point=1, anchor_type=CoordEntityType.Character)
    DisableFlag(7500)
    Restart()


@NeverRestart(12100115)
def Event_12100115():
    """Event 12100115"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(frames=2)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100700, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthEqual(-1, 2100700, value=0.0)
    IfFlagEnabled(-1, 12105100)
    IfFlagEnabled(-1, 72100105)
    EndIfConditionTrue(-1)
    IfCharacterHasSpecialEffect(2, 2100700, 151)
    GotoIfConditionFalse(Label.L0, input_condition=2)
    RotateToFaceEntity(2100700, PLAYER, animation=7010)
    WaitFrames(frames=89)
    IfCharacterHasSpecialEffect(3, 2100700, 152)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    RotateToFaceEntity(2100700, PLAYER, animation=7012)
    WaitFrames(frames=0)

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)


@NeverRestart(12100116)
def Event_12100116():
    """Event 12100116"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72100108)
    DisableFlag(72100108)
    IfCharacterHasSpecialEffect(1, 2100700, 151)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2100700, PLAYER, animation=7011)
    WaitFrames(frames=89)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(2, 2100700, 152)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    RotateToFaceEntity(2100700, PLAYER, animation=7013)
    WaitFrames(frames=0)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHasSpecialEffect(3, 2100700, 153)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    RotateToFaceEntity(2100700, PLAYER, animation=7019)
    WaitFrames(frames=89)

    # --- 2 --- #
    DefineLabel(2)
    Wait(0.0)


@NeverRestart(12100117)
def Event_12100117():
    """Event 12100117"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2100700, 160)
    IfFlagEnabled(1, 12100118)
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(2, PLAYER, 161)
    IfCharacterHasSpecialEffect(3, PLAYER, 162)
    IfCharacterHasSpecialEffect(4, PLAYER, 163)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    RotateToFaceEntity(2100700, PLAYER, animation=7001)
    WaitFrames(frames=1)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    RotateToFaceEntity(2100700, PLAYER, animation=7000)
    WaitFrames(frames=1)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(2100700, PLAYER, animation=7026)
    WaitFrames(frames=39)
    RotateToFaceEntity(2100700, PLAYER, animation=7025)
    Restart()


@NeverRestart(12100120)
def Event_12100120():
    """Event 12100120"""
    EndIfThisEventFlagEnabled()


@NeverRestart(12100121)
def Event_12100121():
    """Event 12100121"""
    IfPlayerHasGood(0, 4300, including_storage=True)
    EnableFlag(12100122)
    IfPlayerDoesNotHaveGood(0, 4300, including_storage=True)
    DisableFlag(12100122)
    Restart()


@NeverRestart(12100123)
def Event_12100123():
    """Event 12100123"""
    DisableNetworkSync()
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100114)
    IfCharacterHasSpecialEffect(1, 2100700, 160)
    IfFlagEnabled(1, 72100114)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100700, 7030)
    IfFlagEnabled(0, 72100112)
    AwardItemLot(14000, host_only=False)
    RemoveGoodFromPlayer(item=4300, quantity=1)


@NeverRestart(12100140)
def Event_12100140(_, first_flag: int, last_flag: int):
    """Event 12100140"""
    IfFlagEnabled(1, 1020)
    IfFlagEnabled(1, 9403)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1021)


@NeverRestart(12100141)
def Event_12100141(_, first_flag: int, last_flag: int):
    """Event 12100141"""
    IfFlagEnabled(1, 1022)
    IfFlagEnabled(1, 9800)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1023)


@NeverRestart(12100142)
def Event_12100142(_, first_flag: int, last_flag: int):
    """Event 12100142"""
    IfFlagEnabled(1, 1024)
    IfFlagEnabled(-1, 12301800)
    IfFlagEnabled(-1, 9801)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1025)


@NeverRestart(12100143)
def Event_12100143(_, first_flag: int, last_flag: int):
    """Event 12100143"""
    IfFlagDisabled(1, 1029)
    IfFlagDisabled(1, 1030)
    IfFlagEnabled(1, 9462)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1028)


@NeverRestart(12100144)
def Event_12100144(_, first_flag: int, last_flag: int):
    """Event 12100144"""
    IfFlagDisabled(1, 1030)
    IfFlagEnabled(1, 12101802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1029)
    SaveRequest()


@NeverRestart(12100145)
def Event_12100145(_, first_flag: int, last_flag: int):
    """Event 12100145"""
    IfFlagEnabled(0, 12101800)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1030)
    SaveRequest()


@NeverRestart(12100146)
def Event_12100146():
    """Event 12100146"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SetDistanceLimitForConversationStateChanges(character=2100800, distance=17.0)
    IfFlagEnabled(0, 1029)
    SetDistanceLimitForConversationStateChanges(character=2100800, distance=80.0)


@NeverRestart(12100160)
def Event_12100160():
    """Event 12100160"""
    DisableFlag(72100133)
    DisableFlag(72100134)
    DisableFlag(72100135)
    DisableFlagRange((12105800, 12105809))
    IfCharacterBackreadEnabled(0, 2100600)
    GotoIfFlagEnabled(Label.L0, flag=1020)
    GotoIfFlagEnabled(Label.L1, flag=1021)
    GotoIfFlagEnabled(Label.L0, flag=1022)
    GotoIfFlagEnabled(Label.L1, flag=1023)
    GotoIfFlagEnabled(Label.L0, flag=1024)
    GotoIfFlagEnabled(Label.L1, flag=1025)
    GotoIfFlagEnabled(Label.L0, flag=1026)
    GotoIfFlagEnabled(Label.L0, flag=1027)
    GotoIfFlagEnabled(Label.L2, flag=1028)
    GotoIfFlagEnabled(Label.L3, flag=1029)
    GotoIfFlagEnabled(Label.L3, flag=1030)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2100600)
    Event_12100161()
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(2100600, destination=2102310, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(2100600, 9002, loop=True)
    Move(2100600, destination=2102312, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(2100600)


@NeverRestart(12100161)
def Event_12100161():
    """Event 12100161"""
    IfFlagEnabled(1, 13601800)
    IfFlagDisabled(1, 72100117)
    EndIfConditionTrue(1)
    GotoIfFlagEnabled(Label.L1, flag=1027)
    GotoIfFlagEnabled(Label.L0, flag=1026)
    SkipLinesIfFlagEnabled(2, 100)
    EnableRandomFlagInRange(flag_range=(12105800, 12105804))
    EndIfFlagDisabled(12105800)
    EnableFlag(72100133)
    EnableCharacter(2100600)
    ForceAnimation(2100600, 9000, loop=True)
    Move(2100600, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(2, 100)
    EnableRandomFlagInRange(flag_range=(12105800, 12105809))
    EndIfFlagDisabled(12105800)
    EnableFlag(72100133)
    EnableCharacter(2100600)
    ForceAnimation(2100600, 9000, loop=True)
    Move(2100600, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(2, 100)
    EnableRandomFlagInRange(flag_range=(12105800, 12105809))
    EndIfFlagDisabled(12105800)
    EnableFlag(72100133)
    EnableCharacter(2100600)
    ForceAnimation(2100600, 9000, loop=True)
    Move(2100600, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)


@NeverRestart(12100162)
def Event_12100162():
    """Event 12100162"""
    GotoIfFlagDisabled(Label.L0, flag=9403)
    DisableObject(2101010)
    EnableObject(2101011)
    DisableObject(2101020)
    EnableObject(2101021)
    DisableObject(2101030)
    EnableObject(2101031)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101010)
    DisableObject(2101011)
    EnableObject(2101020)
    DisableObject(2101021)
    EnableObject(2101030)
    DisableObject(2101031)


@RestartOnRest(12100163)
def Event_12100163():
    """Event 12100163"""
    DisableFlag(12100163)
    IfFlagDisabled(1, 1028)
    IfFlagDisabled(1, 1029)
    IfFlagDisabled(1, 1030)
    IfCharacterHasTAEEvent(1, 2100600, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12100163)


@NeverRestart(12100164)
def Event_12100164():
    """Event 12100164"""
    DisableSoapstoneMessage(2103000)
    DisableSoapstoneMessage(2103001)
    SkipLinesIfFlagDisabled(2, 1024)
    SkipLinesIfFlagEnabled(1, 5000)
    EnableSoapstoneMessage(2103000)
    IfFlagEnabled(-1, 1026)
    IfFlagEnabled(-1, 1027)
    SkipLinesIfConditionFalse(2, -1)
    SkipLinesIfFlagEnabled(1, 52400480)
    EnableSoapstoneMessage(2103001)


@NeverRestart(12100165)
def Event_12100165():
    """Event 12100165"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100136)
    IfFlagEnabled(0, 72100136)
    ForceAnimation(2100600, 7000)
    WaitFrames(frames=129)
    ForceAnimation(2100600, 9003, loop=True)


@NeverRestart(12100180)
def Event_12100180():
    """Event 12100180"""
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(0, 72100130)
    EnableFlag(9180)
    WaitFrames(frames=1)
    DeleteVFX(2103300)
    DeleteVFX(2103500)
    DeleteVFX(2103501)
    DeleteVFX(2103502)
    DeleteVFX(2103503)
    DeleteVFX(2103504)
    DeleteVFX(2103505)
    DeleteVFX(2103506)
    DeleteVFX(2103507)
    IncrementNewGameCycle(dummy_arg=1)
    GotoIfPlayerGender(Label.L0, gender=Gender.Male)
    PlayCutscene(21000010, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(21001010, cutscene_flags=0, player_id=10000)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    AwardAchievement(achievement_id=1)
    EnableFlag(6604)
    Event_12100450()
    Event_12100451()
    Event_12100452()
    WaitFrames(frames=1)
    EnableFlag(21)
    EnableFlag(6600)
    EnableFlag(6603)


@NeverRestart(12100300)
def Event_12100300():
    """Event 12100300"""
    GotoIfFlagEnabled(Label.L5, flag=12101852)
    GotoIfFlagEnabled(Label.L4, flag=9462)
    GotoIfFlagEnabled(Label.L3, flag=9802)
    GotoIfFlagEnabled(Label.L2, flag=9801)
    GotoIfFlagEnabled(Label.L1, flag=9800)
    GotoIfFlagDisabled(Label.L0, flag=9800)

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101310)
    DisableObject(2101311)
    EnableObject(2101300)
    DisableObject(2101301)
    DeleteVFX(2103300, erase_root_only=False)
    DeleteVFX(2103500, erase_root_only=False)
    DeleteVFX(2103501, erase_root_only=False)
    DeleteVFX(2103502, erase_root_only=False)
    DeleteVFX(2103503, erase_root_only=False)
    DeleteVFX(2103504, erase_root_only=False)
    DeleteVFX(2103505, erase_root_only=False)
    DeleteVFX(2103506, erase_root_only=False)
    DeleteVFX(2103507, erase_root_only=False)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101310)
    DisableObject(2101311)
    EnableObject(2101300)
    DisableObject(2101301)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableObject(2101310)
    EnableObject(2101311)
    DisableObject(2101300)
    EnableObject(2101301)


@NeverRestart(12100310)
def Event_12100310():
    """Event 12100310"""
    GotoIfFlagEnabled(Label.L1, flag=9462)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, value=50)
    IfFlagEnabled(-1, 9802)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    EnableSoundEvent(sound_id=2103900)
    DisableSoundEvent(sound_id=2103901)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(sound_id=2103900)
    EnableSoundEvent(sound_id=2103901)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableSoundEvent(sound_id=2103900)
    DisableSoundEvent(sound_id=2103901)


@NeverRestart(12100330)
def Event_12100330():
    """Event 12100330"""
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagEnabled(-1, 5051)
    IfFlagEnabled(-1, 6660)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(5051)
    EnableFlag(6660)


@NeverRestart(12100350)
def Event_12100350(_, obj: int, obj_act_id: int):
    """Event 12100350"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(12100400)
def Event_12100400():
    """Event 12100400"""
    EndIfFlagDisabled(9462)
    EndOfAnimation(obj=2101000, animation_id=1)


@NeverRestart(12100410)
def Event_12100410(_, action_button_id: int, anchor_entity: int, flag: int, text: int):
    """Event 12100410"""
    DisableNetworkSync()
    IfActionButtonParamActivated(-1, action_button_id=action_button_id, entity=anchor_entity)
    IfFlagEnabled(-1, flag)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(flag)
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12100450)
def Event_12100450():
    """Event 12100450"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerDoesNotHaveGood(1, 4103)
    SkipLinesIfConditionTrue(1, 1)
    EnableFlag(6630)
    IfPlayerDoesNotHaveGood(2, 4104)
    SkipLinesIfConditionTrue(1, 2)
    EnableFlag(6631)
    IfPlayerDoesNotHaveGood(3, 4105)
    SkipLinesIfConditionTrue(1, 3)
    EnableFlag(6632)
    IfPlayerDoesNotHaveGood(4, 4102)
    SkipLinesIfConditionTrue(1, 4)
    EnableFlag(6633)
    IfPlayerDoesNotHaveGood(5, 4110)
    SkipLinesIfConditionTrue(1, 5)
    EnableFlag(6640)
    IfPlayerDoesNotHaveGood(6, 4112)
    SkipLinesIfConditionTrue(1, 6)
    EnableFlag(6641)
    IfPlayerDoesNotHaveGood(7, 4113)
    SkipLinesIfConditionTrue(1, 7)
    EnableFlag(6642)
    IfPlayerDoesNotHaveGood(8, 4111)
    SkipLinesIfConditionTrue(1, 8)
    EnableFlag(6643)
    IfPlayerDoesNotHaveGood(9, 4118)
    SkipLinesIfConditionTrue(1, 9)
    EnableFlag(6644)
    IfPlayerDoesNotHaveGood(10, 4114)
    SkipLinesIfConditionTrue(1, 10)
    EnableFlag(6645)
    IfPlayerDoesNotHaveGood(11, 4115)
    SkipLinesIfConditionTrue(1, 11)
    EnableFlag(6646)
    IfPlayerDoesNotHaveGood(12, 4116)
    SkipLinesIfConditionTrue(1, 12)
    EnableFlag(6647)
    IfPlayerDoesNotHaveGood(13, 4119)
    SkipLinesIfConditionTrue(1, 13)
    EnableFlag(6648)
    IfPlayerDoesNotHaveGood(14, 4117)
    SkipLinesIfConditionTrue(1, 14)
    EnableFlag(6649)
    End()


@NeverRestart(12100451)
def Event_12100451():
    """Event 12100451"""
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 50000400)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6300)
    IfFlagEnabled(2, 50000600)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6301)
    IfFlagEnabled(3, 50000800)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6302)
    IfFlagEnabled(4, 50001100)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6303)
    IfFlagEnabled(5, 50001300)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6304)
    IfFlagEnabled(6, 50001610)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6305)
    IfFlagEnabled(7, 50002110)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6306)
    IfFlagEnabled(8, 50003400)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6307)
    IfFlagEnabled(9, 50003500)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6308)
    IfFlagEnabled(10, 52200380)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6309)
    IfFlagEnabled(11, 52420640)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6310)
    IfFlagEnabled(12, 52420690)
    SkipLinesIfConditionFalse(1, 12)
    EnableFlag(6311)
    IfFlagEnabled(13, 52410640)
    SkipLinesIfConditionFalse(1, 13)
    EnableFlag(6312)
    IfFlagEnabled(14, 52420120)
    SkipLinesIfConditionFalse(1, 14)
    EnableFlag(6313)
    IfFlagEnabled(15, 52600390)
    SkipLinesIfConditionFalse(1, 15)
    EnableFlag(6314)
    IfFlagEnabled(-1, 52600300)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6315)
    IfFlagEnabled(-2, 52700180)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6316)
    IfFlagEnabled(-3, 52700200)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6317)
    IfFlagEnabled(-4, 52700380)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6318)
    IfFlagEnabled(-5, 52700540)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6319)
    IfFlagEnabled(-6, 52700570)
    SkipLinesIfConditionFalse(1, -6)
    EnableFlag(6320)
    IfFlagEnabled(-7, 52700950)
    SkipLinesIfConditionFalse(1, -7)
    EnableFlag(6321)
    IfFlagEnabled(-8, 52800050)
    SkipLinesIfConditionFalse(1, -8)
    EnableFlag(6322)
    IfFlagEnabled(-9, 52800140)
    SkipLinesIfConditionFalse(1, -9)
    EnableFlag(6323)
    IfFlagEnabled(-10, 52800350)
    SkipLinesIfConditionFalse(1, -10)
    EnableFlag(6324)
    IfFlagEnabled(-11, 53200010)
    SkipLinesIfConditionFalse(1, -11)
    EnableFlag(6325)
    IfFlagEnabled(-12, 53200640)
    SkipLinesIfConditionFalse(1, -12)
    EnableFlag(6326)
    IfFlagEnabled(-13, 53300110)
    SkipLinesIfConditionFalse(1, -13)
    EnableFlag(6327)
    IfFlagEnabled(-14, 53300150)
    SkipLinesIfConditionFalse(1, -14)
    EnableFlag(6328)
    IfFlagEnabled(-15, 53300320)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(6329)


@NeverRestart(12100452)
def Event_12100452():
    """Event 12100452"""
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 53300420)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6330)
    IfFlagEnabled(2, 53300480)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6331)
    IfFlagEnabled(3, 9458)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6332)
    IfFlagEnabled(4, 12400861)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6333)
    IfFlagEnabled(5, 50003100)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6334)
    IfFlagEnabled(6, 50001500)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6335)
    IfFlagEnabled(7, 52605000)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6336)
    IfFlagEnabled(8, 50000200)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6340)
    IfFlagEnabled(9, 50001820)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6341)
    IfFlagEnabled(10, 50001910)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6342)
    IfFlagEnabled(11, 50002260)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6677)


@NeverRestart(12100990)
def Event_12100990():
    """Event 12100990"""
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2103600)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@NeverRestart(12100800)
def Event_12100800():
    """Event 12100800"""
    GotoIfFlagDisabled(Label.L0, flag=12101850)
    DisableCharacter(2100810)
    DisableCharacter(2100800)
    SkipLinesIfClient(2)
    DisableObject(2101800)
    DeleteVFX(2103800, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=12101852)
    DisableCharacter(2100800)
    End()

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=12101800)
    DisableCharacter(2100810)
    DisableCharacter(2100800)
    SkipLinesIfClient(2)
    DisableObject(2101800)
    DeleteVFX(2103800, erase_root_only=False)
    End()

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, flag=12101802)
    DisableCharacter(2100810)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(2100810)
    DisableCharacter(2100800)
    SkipLinesIfClient(2)
    DisableObject(2101800)
    DeleteVFX(2103800, erase_root_only=False)


@NeverRestart(12101800)
def Event_12101800():
    """Event 12101800"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2103802)
    DisableSoundEvent(sound_id=2103803)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(12104809)
    IfHealthEqual(0, 2100800, value=0.0)
    EnableFlag(12104809)
    IfCharacterDead(1, 2100800)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFlagEnabled(2, 9900)
    KillBoss(game_area_param_id=2100800)
    SkipLines(1)
    HandleMinibossDefeat(miniboss_id=2100800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    SkipLinesIfFlagEnabled(2, 6642)
    AwardItemLot(15000, host_only=False)
    SkipLines(1)
    AwardItemLot(15005, host_only=False)
    StopPlayLogMeasurement(measurement_id=2100000)
    StopPlayLogMeasurement(measurement_id=2100001)
    StopPlayLogMeasurement(measurement_id=2100010)
    CreatePlayLog(name=22)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=34,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=34,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=34,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=34,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12101801)
def Event_12101801():
    """Event 12101801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101800)
    IfFlagEnabled(1, 12101800)
    IfCharacterBackreadDisabled(2, 2100800)
    IfHealthLessThanOrEqual(2, 2100800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2102800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12101802)
def Event_12101802():
    """Event 12101802"""
    EndIfFlagEnabled(12101800)
    EndIfThisEventFlagEnabled()
    DisableCharacter(2100800)
    DisableFlag(72100131)
    IfFlagEnabled(0, 72100131)
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(21000040, cutscene_flags=0, player_id=10000, move_to_region=2102808, game_map=HUNTERS_DREAM)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableCharacter(2100800)
    DisableCharacter(2100600)
    EnableFlag(12104800)
    DisableFlag(2100)
    EndIfFlagEnabled(9343)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9343)


@NeverRestart(12101803)
def Event_12101803():
    """Event 12101803"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12104800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2100800)
    DisableCharacter(2100600)
    EnableFlag(12104800)
    EnableFlag(12101802)


@NeverRestart(12104810)
def Event_12104810():
    """Event 12104810"""
    EndIfFlagEnabled(12101800)
    GotoIfFlagEnabled(Label.L0, flag=12101802)
    IfFlagDisabled(1, 12101800)
    IfFlagEnabled(1, 12101802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2101800)
    CreateVFX(2103800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12101800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2100800, entity=2101800)
    IfFlagEnabled(3, 12101800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2102801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12104800)
    Restart()


@NeverRestart(12104811)
def Event_12104811():
    """Event 12104811"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101800)
    IfFlagDisabled(1, 12101800)
    IfFlagEnabled(1, 12101802)
    IfFlagEnabled(1, 12104800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2100800, entity=2101800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12104801)
    Restart()


@NeverRestart(12104802)
def Event_12104802():
    """Event 12104802"""
    EndIfFlagEnabled(12101800)
    DisableAI(2100800)
    DisableHealthBar(2100800)
    EnableInvincibility(2100800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12104800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2100800, authority_level=UpdateAuthority.Normal)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12104800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2100800, 7500)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2100800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2100800, 7501)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2100800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2100800)
    EnableBossHealthBar(2100800, name=804000)
    DisableInvincibility(2100800)
    SetCharacterEventTarget(2100800, region=2100801)
    CreatePlayLog(name=64)
    StartPlayLogMeasurement(measurement_id=2100010, name=80, overwrite=True)


@NeverRestart(12104803)
def Event_12104803():
    """Event 12104803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2103802)
    DisableSoundEvent(sound_id=2103803)
    IfFlagDisabled(1, 12101800)
    IfFlagEnabled(1, 12104802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12104801)
    IfCharacterInsideRegion(1, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=2103900)
    DisableSoundEvent(sound_id=2103901)
    EnableBossMusic(sound_id=2103802)
    IfCharacterHasTAEEvent(2, 2100800, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12101800)
    IfFlagEnabled(2, 12104802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12104801)
    IfCharacterInsideRegion(2, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2103802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2103803)


@NeverRestart(12104804)
def Event_12104804():
    """Event 12104804"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101800)
    IfHealthGreaterThan(1, 2100800, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, 2100800, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=2100800, radius=10.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


@NeverRestart(12104805)
def Event_12104805():
    """Event 12104805"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101800)
    IfFlagEnabled(0, 12104809)
    DisableBossMusic(sound_id=2103802)
    DisableBossMusic(sound_id=2103803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12104807)
def Event_12104807():
    """Event 12104807"""
    EndIfFlagEnabled(12101800)
    IfHealthLessThan(0, 2100800, value=0.5)
    AICommand(2100800, command_id=100, command_slot=0)
    IfCharacterHasTAEEvent(0, 2100800, tae_event_id=100)
    CancelSpecialEffect(2100800, 5305)
    AICommand(2100800, command_id=-1, command_slot=0)
    ReplanAI(2100800)
    Wait(0.10000000149011612)
    AICommand(2100800, command_id=1, command_slot=1)


@NeverRestart(12104808)
def Event_12104808():
    """Event 12104808"""
    EndIfFlagEnabled(12101800)
    IfCharacterHasTAEEvent(0, 2100800, tae_event_id=20)
    CancelSpecialEffect(2100800, 5526)
    Wait(0.10000000149011612)
    Restart()


@NeverRestart(12101850)
def Event_12101850():
    """Event 12101850"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2103812)
    DisableSoundEvent(sound_id=2103813)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2100810)
    EnableFlag(12104859)
    DisplayBanner(BannerType.NightmareSlain)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2100810)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(5,))
    StopPlayLogMeasurement(measurement_id=2100011)
    CreatePlayLog(name=22)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=96,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=96,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=96,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=96,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12101851)
def Event_12101851():
    """Event 12101851"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101850)
    IfFlagEnabled(1, 12101850)
    IfCharacterBackreadDisabled(2, 2100810)
    IfHealthLessThanOrEqual(2, 2100810, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2102800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12101852)
def Event_12101852():
    """Event 12101852"""
    EndIfFlagEnabled(12101850)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12101800)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2103601)
    IfPlayerStandingOnCollision(-1, 2103602)
    IfPlayerStandingOnCollision(-1, 2103603)
    IfPlayerStandingOnCollision(-1, 2103604)
    IfPlayerStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 9900)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableFlag(9180)
    WaitFrames(frames=1)
    DeleteVFX(2103510)
    DeleteVFX(2103511)
    DeleteVFX(2103512)
    DeleteVFX(2103513)
    DeleteVFX(2103514)
    DeleteVFX(2103515)
    DeleteVFX(2103516)
    DeleteVFX(2103517)
    DeleteVFX(2103518)
    DeleteVFX(2103519)
    DeleteVFX(2103520)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(21000050, cutscene_flags=0, player_id=10000, move_to_region=2102809, game_map=HUNTERS_DREAM)
    SkipLines(1)
    PlayCutscene(
        21000050,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=2102809,
        game_map=HUNTERS_DREAM,
    )
    WaitFrames(frames=1)
    DisableFlag(9180)
    CreateVFX(2103510)
    CreateVFX(2103511)
    CreateVFX(2103512)
    CreateVFX(2103513)
    CreateVFX(2103514)
    CreateVFX(2103515)
    CreateVFX(2103516)
    CreateVFX(2103517)
    CreateVFX(2103518)
    CreateVFX(2103519)
    CreateVFX(2103520)
    DisableObject(2101310)
    EnableObject(2101311)
    DisableObject(2101300)
    EnableObject(2101301)
    EnableCharacter(2100810)
    EnableFlag(12104850)
    EndIfFlagEnabled(9307)
    RunEvent(9350, slot=0, args=(5,))
    EnableFlag(9307)


@NeverRestart(12101853)
def Event_12101853():
    """Event 12101853"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12104850)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableObject(2101310)
    EnableObject(2101311)
    DisableObject(2101300)
    EnableObject(2101301)
    EnableCharacter(2100810)
    EnableFlag(12104850)
    EnableFlag(12101852)


@NeverRestart(12104880)
def Event_12104880():
    """Event 12104880"""
    EndIfFlagEnabled(12101850)
    GotoIfFlagEnabled(Label.L0, flag=12101852)
    IfFlagDisabled(1, 12101850)
    IfFlagEnabled(1, 12101852)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2101800)
    CreateVFX(2103800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12101850)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2100800, entity=2101800)
    IfFlagEnabled(3, 12101850)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2102801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12104850)
    Restart()


@NeverRestart(12104881)
def Event_12104881():
    """Event 12104881"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101850)
    IfFlagDisabled(1, 12101850)
    IfFlagEnabled(1, 12101852)
    IfFlagEnabled(1, 12104850)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2100800, entity=2101800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2102800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12104851)
    Restart()


@NeverRestart(12104852)
def Event_12104852():
    """Event 12104852"""
    EndIfFlagEnabled(12101850)
    DisableAI(2100810)
    DisableHealthBar(2100810)
    EnableInvincibility(2100810)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12104850)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2100810, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12104850)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2100810, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2100810)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2100810, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2100810)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2100810)
    EnableBossHealthBar(2100810, name=540000)
    DisableInvincibility(2100810)
    CreatePlayLog(name=128)
    StartPlayLogMeasurement(measurement_id=2100011, name=146, overwrite=True)


@NeverRestart(12104853)
def Event_12104853():
    """Event 12104853"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101850)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2103812)
    DisableSoundEvent(sound_id=2103813)
    IfFlagDisabled(1, 12101850)
    IfFlagEnabled(1, 12101852)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12104851)
    IfCharacterInsideRegion(1, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=2103900)
    DisableSoundEvent(sound_id=2103901)
    EnableBossMusic(sound_id=2103812)
    IfCharacterHasTAEEvent(0, 2100810, tae_event_id=500)
    IfFlagDisabled(2, 12101850)
    IfFlagEnabled(2, 12101852)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12104851)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2103812)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2103813)


@NeverRestart(12104854)
def Event_12104854():
    """Event 12104854"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101850)
    IfHealthGreaterThan(1, 2100810, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100810, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, 2100810, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=2100810, radius=12.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


@NeverRestart(12104855)
def Event_12104855():
    """Event 12104855"""
    DisableNetworkSync()
    EndIfFlagEnabled(12101850)
    IfFlagEnabled(0, 12104859)
    DisableBossMusic(sound_id=2103812)
    DisableBossMusic(sound_id=2103813)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12104860)
def Event_12104860(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12104860"""
    EndIfFlagEnabled(12101850)
    CreateNPCPart(2100810, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2100810, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, 2100810, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, 2100810, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        2100810,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(2100810, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(2100810)
    ForceAnimation(2100810, animation_id)
    AddSpecialEffect(2100810, special_effect_id)
    CancelSpecialEffect(2100810, special_effect_id_1)
    ReplanAI(2100810)
    Wait(30.0)
    AICommand(2100810, command_id=10, command_slot=1)
    ReplanAI(2100810)
    IfCharacterHasTAEEvent(0, 2100810, tae_event_id=300)
    SetNPCPartHealth(2100810, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2100810, special_effect_id_1)
    CancelSpecialEffect(2100810, special_effect_id)
    AICommand(2100810, command_id=-1, command_slot=1)
    ReplanAI(2100810)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12104870)
def Event_12104870():
    """Event 12104870"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, 2100810, tae_event_id=10)
    EnableImmortality(PLAYER)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5570)
    IfFramesElapsed(-1, frames=70)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=5)
    DisableImmortality(PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=PLAYER, attacker=2100810)
    IfTimeElapsed(-1, seconds=10.0)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 5572)
    Restart()


@RestartOnRest(12105000)
def Event_12105000(_, entity: int, flag: int):
    """Event 12105000"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    ForceAnimation(entity, 7000)
    WaitFrames(frames=109)
    ForceAnimation(entity, 7001, loop=True)
    IfFlagDisabled(0, flag)
    ForceAnimation(entity, 7002)
    WaitFrames(frames=74)
    Restart()


@RestartOnRest(12105004)
def Event_12105004(_, character: int, flag: int):
    """Event 12105004"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    Move(character, destination=2102305, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(character, 5401)
    ForceAnimation(character, 7000)
    WaitFrames(frames=109)
    ForceAnimation(character, 7001, loop=True)
    IfFlagDisabled(0, flag)
    ForceAnimation(character, 7002)
    WaitFrames(frames=74)
    Restart()


@RestartOnRest(12105010)
def Event_12105010():
    """Event 12105010"""
    DisableObject(2101200)
    DisableObject(2101201)
    DisableObject(2101202)
    DisableObject(2101203)
    DisableObject(2101204)
    DisableObject(2101205)
    DisableObject(2101206)
    DisableObject(2101207)
    DisableObject(2101208)
    IfFlagEnabled(10, 94005500)
    IfFlagRangeAnyEnabled(10, flag_range=(94005100, 94005101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94005500)
    IfFlagRangeAnyEnabled(11, flag_range=(94005103, 94005104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94005500)
    IfFlagEnabled(12, 94005102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94005503)
    GotoIfFlagEnabled(Label.L4, flag=94005504)
    GotoIfFlagEnabled(Label.L5, flag=94005505)
    GotoIfFlagEnabled(Label.L6, flag=94005502)
    GotoIfFlagEnabled(Label.L7, flag=94005507)
    GotoIfFlagEnabled(Label.L8, flag=94005501)
    IfFlagEnabled(1, 94005500)
    IfFlagRangeAnyEnabled(1, flag_range=(94005100, 94005101))
    IfFlagEnabled(2, 94005500)
    IfFlagRangeAnyEnabled(2, flag_range=(94005103, 94005104))
    IfFlagEnabled(3, 94005500)
    IfFlagEnabled(3, 94005102)
    IfFlagEnabled(4, 94005503)
    IfFlagEnabled(5, 94005504)
    IfFlagEnabled(6, 94005505)
    IfFlagEnabled(7, 94005502)
    IfFlagEnabled(8, 94005507)
    IfFlagEnabled(9, 94005501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100954, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101200)
    IfFlagDisabled(0, 94005500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101201)
    IfFlagDisabled(0, 94005500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101202)
    IfFlagDisabled(0, 94005500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101203)
    IfFlagDisabled(0, 94005503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101204)
    IfFlagDisabled(0, 94005504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101205)
    IfFlagDisabled(0, 94005505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101206)
    IfFlagDisabled(0, 94005502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101207)
    IfFlagDisabled(0, 94005507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101208)
    IfFlagDisabled(0, 94005501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100954, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105011)
def Event_12105011():
    """Event 12105011"""
    DisableObject(2101210)
    DisableObject(2101211)
    DisableObject(2101212)
    DisableObject(2101213)
    DisableObject(2101214)
    DisableObject(2101215)
    DisableObject(2101216)
    DisableObject(2101217)
    DisableObject(2101218)
    IfFlagEnabled(10, 94105500)
    IfFlagRangeAnyEnabled(10, flag_range=(94105100, 94105101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94105500)
    IfFlagRangeAnyEnabled(11, flag_range=(94105103, 94105104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94105500)
    IfFlagEnabled(12, 94105102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94105503)
    GotoIfFlagEnabled(Label.L4, flag=94105504)
    GotoIfFlagEnabled(Label.L5, flag=94105505)
    GotoIfFlagEnabled(Label.L6, flag=94105502)
    GotoIfFlagEnabled(Label.L7, flag=94105507)
    GotoIfFlagEnabled(Label.L8, flag=94105501)
    IfFlagEnabled(1, 94105500)
    IfFlagRangeAnyEnabled(1, flag_range=(94105100, 94105101))
    IfFlagEnabled(2, 94105500)
    IfFlagRangeAnyEnabled(2, flag_range=(94105103, 94105104))
    IfFlagEnabled(3, 94105500)
    IfFlagEnabled(3, 94105102)
    IfFlagEnabled(4, 94105503)
    IfFlagEnabled(5, 94105504)
    IfFlagEnabled(6, 94105505)
    IfFlagEnabled(7, 94105502)
    IfFlagEnabled(8, 94105507)
    IfFlagEnabled(9, 94105501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100955, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101210)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101211)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101212)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101213)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101214)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101215)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101216)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101217)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101218)
    WaitFrames(frames=45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100955, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105012)
def Event_12105012():
    """Event 12105012"""
    DisableObject(2101220)
    DisableObject(2101221)
    DisableObject(2101222)
    DisableObject(2101223)
    DisableObject(2101224)
    DisableObject(2101225)
    DisableObject(2101226)
    DisableObject(2101227)
    DisableObject(2101228)
    IfFlagEnabled(10, 94205500)
    IfFlagRangeAnyEnabled(10, flag_range=(94205100, 94205101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94205500)
    IfFlagRangeAnyEnabled(11, flag_range=(94205103, 94205104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94205500)
    IfFlagEnabled(12, 94205102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94205503)
    GotoIfFlagEnabled(Label.L4, flag=94205504)
    GotoIfFlagEnabled(Label.L5, flag=94205505)
    GotoIfFlagEnabled(Label.L6, flag=94205502)
    GotoIfFlagEnabled(Label.L7, flag=94205507)
    GotoIfFlagEnabled(Label.L8, flag=94205501)
    IfFlagEnabled(1, 94205500)
    IfFlagRangeAnyEnabled(1, flag_range=(94205100, 94205101))
    IfFlagEnabled(2, 94205500)
    IfFlagRangeAnyEnabled(2, flag_range=(94205103, 94205104))
    IfFlagEnabled(3, 94205500)
    IfFlagEnabled(3, 94205102)
    IfFlagEnabled(4, 94205503)
    IfFlagEnabled(5, 94205504)
    IfFlagEnabled(6, 94205505)
    IfFlagEnabled(7, 94205502)
    IfFlagEnabled(8, 94205507)
    IfFlagEnabled(9, 94205501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100956, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101220)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101221)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101222)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101223)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101224)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101225)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101226)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101227)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101228)
    WaitFrames(frames=45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100956, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105013)
def Event_12105013():
    """Event 12105013"""
    DisableObject(2101230)
    DisableObject(2101231)
    DisableObject(2101232)
    DisableObject(2101233)
    DisableObject(2101234)
    DisableObject(2101235)
    DisableObject(2101236)
    DisableObject(2101237)
    DisableObject(2101238)
    IfFlagEnabled(10, 94305500)
    IfFlagRangeAnyEnabled(10, flag_range=(94305100, 94305101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94305500)
    IfFlagRangeAnyEnabled(11, flag_range=(94305103, 94305104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94305500)
    IfFlagEnabled(12, 94305102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94305503)
    GotoIfFlagEnabled(Label.L4, flag=94305504)
    GotoIfFlagEnabled(Label.L5, flag=94305505)
    GotoIfFlagEnabled(Label.L6, flag=94305502)
    GotoIfFlagEnabled(Label.L7, flag=94305507)
    GotoIfFlagEnabled(Label.L8, flag=94305501)
    IfFlagEnabled(1, 94305500)
    IfFlagRangeAnyEnabled(1, flag_range=(94305100, 94305101))
    IfFlagEnabled(2, 94305500)
    IfFlagRangeAnyEnabled(2, flag_range=(94305103, 94305104))
    IfFlagEnabled(3, 94305500)
    IfFlagEnabled(3, 94305102)
    IfFlagEnabled(4, 94305503)
    IfFlagEnabled(5, 94305504)
    IfFlagEnabled(6, 94305505)
    IfFlagEnabled(7, 94305502)
    IfFlagEnabled(8, 94305507)
    IfFlagEnabled(9, 94305501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100957, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101230)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101231)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101232)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101233)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101234)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101235)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101236)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101237)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101238)
    WaitFrames(frames=45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100957, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105014)
def Event_12105014():
    """Event 12105014"""
    DisableObject(2101240)
    DisableObject(2101241)
    DisableObject(2101242)
    DisableObject(2101243)
    DisableObject(2101244)
    DisableObject(2101245)
    DisableObject(2101246)
    DisableObject(2101247)
    DisableObject(2101248)
    IfFlagEnabled(10, 94405500)
    IfFlagRangeAnyEnabled(10, flag_range=(94405100, 94405101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94405500)
    IfFlagRangeAnyEnabled(11, flag_range=(94405103, 94405104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94405500)
    IfFlagEnabled(12, 94405102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94405503)
    GotoIfFlagEnabled(Label.L4, flag=94405504)
    GotoIfFlagEnabled(Label.L5, flag=94405505)
    GotoIfFlagEnabled(Label.L6, flag=94405502)
    GotoIfFlagEnabled(Label.L7, flag=94405507)
    GotoIfFlagEnabled(Label.L8, flag=94405501)
    IfFlagEnabled(1, 94405500)
    IfFlagRangeAnyEnabled(1, flag_range=(94405100, 94405101))
    IfFlagEnabled(2, 94405500)
    IfFlagRangeAnyEnabled(2, flag_range=(94405103, 94405104))
    IfFlagEnabled(3, 94405500)
    IfFlagEnabled(3, 94405102)
    IfFlagEnabled(4, 94405503)
    IfFlagEnabled(5, 94405504)
    IfFlagEnabled(6, 94405505)
    IfFlagEnabled(7, 94405502)
    IfFlagEnabled(8, 94405507)
    IfFlagEnabled(9, 94405501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100958, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101240)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101241)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101242)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101243)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101244)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101245)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101246)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101247)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101248)
    WaitFrames(frames=45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100958, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105015)
def Event_12105015():
    """Event 12105015"""
    DisableObject(2101250)
    DisableObject(2101251)
    DisableObject(2101252)
    DisableObject(2101253)
    DisableObject(2101254)
    DisableObject(2101255)
    DisableObject(2101256)
    DisableObject(2101257)
    DisableObject(2101258)
    IfFlagEnabled(10, 94505500)
    IfFlagRangeAnyEnabled(10, flag_range=(94505100, 94505101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94505500)
    IfFlagRangeAnyEnabled(11, flag_range=(94505103, 94505104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94505500)
    IfFlagEnabled(12, 94505102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94505503)
    GotoIfFlagEnabled(Label.L4, flag=94505504)
    GotoIfFlagEnabled(Label.L5, flag=94505505)
    GotoIfFlagEnabled(Label.L6, flag=94505502)
    GotoIfFlagEnabled(Label.L7, flag=94505507)
    GotoIfFlagEnabled(Label.L8, flag=94505501)
    IfFlagEnabled(1, 94505500)
    IfFlagRangeAnyEnabled(1, flag_range=(94505100, 94505101))
    IfFlagEnabled(2, 94505500)
    IfFlagRangeAnyEnabled(2, flag_range=(94505103, 94505104))
    IfFlagEnabled(3, 94505500)
    IfFlagEnabled(3, 94505102)
    IfFlagEnabled(4, 94505503)
    IfFlagEnabled(5, 94505504)
    IfFlagEnabled(6, 94505505)
    IfFlagEnabled(7, 94505502)
    IfFlagEnabled(8, 94505507)
    IfFlagEnabled(9, 94505501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100959, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101250)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101251)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101252)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101253)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101254)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101255)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101256)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101257)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101258)
    WaitFrames(frames=45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100959, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105016)
def Event_12105016():
    """Event 12105016"""
    DisableObject(2101260)
    DisableObject(2101261)
    DisableObject(2101262)
    DisableObject(2101263)
    DisableObject(2101264)
    DisableObject(2101265)
    DisableObject(2101266)
    DisableObject(2101267)
    DisableObject(2101268)
    IfFlagEnabled(10, 94605500)
    IfFlagRangeAnyEnabled(10, flag_range=(94605100, 94605101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94605500)
    IfFlagRangeAnyEnabled(11, flag_range=(94605103, 94605104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94605500)
    IfFlagEnabled(12, 94605102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, flag=94605503)
    GotoIfFlagEnabled(Label.L4, flag=94605504)
    GotoIfFlagEnabled(Label.L5, flag=94605505)
    GotoIfFlagEnabled(Label.L6, flag=94605502)
    GotoIfFlagEnabled(Label.L7, flag=94605507)
    GotoIfFlagEnabled(Label.L8, flag=94605501)
    IfFlagEnabled(1, 94605500)
    IfFlagRangeAnyEnabled(1, flag_range=(94605100, 94605101))
    IfFlagEnabled(2, 94605500)
    IfFlagRangeAnyEnabled(2, flag_range=(94605103, 94605104))
    IfFlagEnabled(3, 94605500)
    IfFlagEnabled(3, 94605102)
    IfFlagEnabled(4, 94605503)
    IfFlagEnabled(5, 94605504)
    IfFlagEnabled(6, 94605505)
    IfFlagEnabled(7, 94605502)
    IfFlagEnabled(8, 94605507)
    IfFlagEnabled(9, 94605501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=31)
    CreateTemporaryVFX(vfx_id=350, anchor_entity=2100960, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101260)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101261)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101262)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101263)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101264)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101265)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101266)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101267)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101268)
    WaitFrames(frames=45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(vfx_id=351, anchor_entity=2100960, model_point=200, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12105020)
def Event_12105020():
    """Event 12105020"""
    IfFlagEnabled(-1, 12417810)
    IfFlagEnabled(-1, 12417830)
    IfFlagEnabled(-1, 12417850)
    IfFlagEnabled(-1, 12417870)
    IfFlagEnabled(-1, 12407810)
    IfFlagEnabled(-1, 12407830)
    IfFlagEnabled(-1, 12427810)
    IfFlagEnabled(-1, 12427830)
    IfFlagEnabled(-1, 12427850)
    IfFlagEnabled(-1, 12307810)
    IfFlagEnabled(-1, 12307830)
    IfFlagEnabled(-1, 12307850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105030)
    IfFlagEnabled(-2, 12417810)
    IfFlagEnabled(-2, 12417830)
    IfFlagEnabled(-2, 12417850)
    IfFlagEnabled(-2, 12417870)
    IfFlagEnabled(-2, 12407810)
    IfFlagEnabled(-2, 12407830)
    IfFlagEnabled(-2, 12427810)
    IfFlagEnabled(-2, 12427830)
    IfFlagEnabled(-2, 12427850)
    IfFlagEnabled(-2, 12307810)
    IfFlagEnabled(-2, 12307830)
    IfFlagEnabled(-2, 12307850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105030)
    Restart()


@RestartOnRest(12105021)
def Event_12105021():
    """Event 12105021"""
    IfFlagEnabled(-1, 12207810)
    IfFlagEnabled(-1, 12207830)
    IfFlagEnabled(-1, 12707810)
    IfFlagEnabled(-1, 12707830)
    IfFlagEnabled(-1, 13207810)
    IfFlagEnabled(-1, 13207850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105031)
    IfFlagEnabled(-2, 12207810)
    IfFlagEnabled(-2, 12207830)
    IfFlagEnabled(-2, 12707810)
    IfFlagEnabled(-2, 12707830)
    IfFlagEnabled(-2, 13207810)
    IfFlagEnabled(-2, 13207850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105031)
    Restart()


@RestartOnRest(12105022)
def Event_12105022():
    """Event 12105022"""
    IfFlagEnabled(-1, 12807810)
    IfFlagEnabled(-1, 12807830)
    IfFlagEnabled(-1, 12807850)
    IfFlagEnabled(-1, 12807870)
    IfFlagEnabled(-1, 12507810)
    IfFlagEnabled(-1, 12507830)
    IfFlagEnabled(-1, 12507850)
    IfFlagEnabled(-1, 12117810)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105032)
    IfFlagEnabled(-2, 12807810)
    IfFlagEnabled(-2, 12807830)
    IfFlagEnabled(-2, 12807850)
    IfFlagEnabled(-2, 12807870)
    IfFlagEnabled(-2, 12507810)
    IfFlagEnabled(-2, 12507830)
    IfFlagEnabled(-2, 12507850)
    IfFlagEnabled(-2, 12117810)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105032)
    Restart()


@RestartOnRest(12105023)
def Event_12105023():
    """Event 12105023"""
    IfFlagEnabled(-1, 13207830)
    IfFlagEnabled(-1, 13207870)
    IfFlagEnabled(-1, 13307810)
    IfFlagEnabled(-1, 13307830)
    IfFlagEnabled(-1, 12607810)
    IfFlagEnabled(-1, 12607830)
    IfFlagEnabled(-1, 12607850)
    IfFlagEnabled(-1, 12607870)
    IfFlagEnabled(-1, 13307810)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105033)
    IfFlagEnabled(-2, 13207830)
    IfFlagEnabled(-2, 13207870)
    IfFlagEnabled(-2, 13307810)
    IfFlagEnabled(-2, 13307830)
    IfFlagEnabled(-2, 12607810)
    IfFlagEnabled(-2, 12607830)
    IfFlagEnabled(-2, 12607850)
    IfFlagEnabled(-2, 12607870)
    IfFlagEnabled(-2, 13307810)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105033)
    Restart()


@RestartOnRest(12105024)
def Event_12105024():
    """Event 12105024"""
    IfFlagEnabled(-1, 13407810)
    IfFlagEnabled(-1, 13407830)
    IfFlagEnabled(-1, 13407850)
    IfFlagEnabled(-1, 13407870)
    IfFlagEnabled(-1, 13507810)
    IfFlagEnabled(-1, 13507830)
    IfFlagEnabled(-1, 13507850)
    IfFlagEnabled(-1, 13607810)
    IfFlagEnabled(-1, 13607830)
    IfFlagEnabled(-1, 13607850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12105034)
    IfFlagEnabled(-2, 13407810)
    IfFlagEnabled(-2, 13407830)
    IfFlagEnabled(-2, 13407850)
    IfFlagEnabled(-2, 13407870)
    IfFlagEnabled(-2, 13507810)
    IfFlagEnabled(-2, 13507830)
    IfFlagEnabled(-2, 13507850)
    IfFlagEnabled(-2, 13607810)
    IfFlagEnabled(-2, 13607830)
    IfFlagEnabled(-2, 13607850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(12105034)
    Restart()


@RestartOnRest(12105040)
def Event_12105040():
    """Event 12105040"""
    ForceAnimation(2100211, 7001, loop=True)
    ForceAnimation(2100212, 7002, loop=True)
    ForceAnimation(2100213, 7041, loop=True)
    IfFlagEnabled(0, 12105041)
    ForceAnimation(2100211, 7005)
    ForceAnimation(2100212, 7006)
    ForceAnimation(2100213, 7045)
    WaitFrames(frames=29)
    ForceAnimation(2100211, 7003, loop=True)
    ForceAnimation(2100212, 7004, loop=True)
    ForceAnimation(2100213, 7043, loop=True)
    IfFlagDisabled(0, 12105041)
    ForceAnimation(2100211, 7007)
    ForceAnimation(2100212, 7008)
    ForceAnimation(2100213, 7047)
    WaitFrames(frames=28)
    Restart()


@NeverRestart(12101000)
def Event_12101000(_, item: int, character: int, bit_index: uchar, bit_index_1: uchar):
    """Event 12101000"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, character)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    IfPlayerHasGood(0, item)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)


@NeverRestart(12101010)
def Event_12101010():
    """Event 12101010"""
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfFlagDisabled(1, 9800)
    EnableFlag(5900)
    SkipLinesIfFlagDisabled(1, 9801)
    EnableFlag(5901)
    SkipLinesIfFlagDisabled(1, 9802)
    EnableFlag(5902)
    SkipLinesIfFlagDisabled(1, 12801800)
    EnableFlag(5903)
    SkipLinesIfFlagDisabled(1, 12601800)
    EnableFlag(5904)
    SkipLinesIfFlagDisabled(1, 6603)
    EnableFlagRange((5900, 5904))


@RestartOnRest(12105043)
def Event_12105043():
    """Event 12105043"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, flag=12100320)
    ForceAnimation(2100219, 7030, loop=True)
    EndIfClient()
    IfPlayerInsightAmountGreaterThanOrEqual(0, value=1)
    EnableFlag(12100320)
    ForceAnimation(2100219, 7031)
    WaitFrames(frames=30)
    EnableFlag(12105045)
    WaitFrames(frames=79)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12105045)
    ForceAnimation(2100219, 7032, loop=True)
    IfFlagEnabled(0, 12105044)
    ForceAnimation(2100219, 7034)
    WaitFrames(frames=29)
    ForceAnimation(2100219, 7035, loop=True)
    IfFlagDisabled(0, 12105044)
    ForceAnimation(2100219, 7036)
    WaitFrames(frames=28)
    Restart()


@NeverRestart(12101020)
def Event_12101020():
    """Event 12101020"""
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(2100215, 7013, loop=True)
    ForceAnimation(2100220, 7013, loop=True)
    IfCharacterBackreadEnabled(1, 2100215)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100215, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100215, 7014)
    ForceAnimation(2100220, 7014)
    WaitFrames(frames=30)
    EnableFlag(12105050)
    WaitFrames(frames=79)
    ForceAnimation(2100215, 7011, loop=True)
    ForceAnimation(2100220, 7011, loop=True)
    IfFlagEnabled(-1, 72101000)
    IfFlagEnabled(-1, 72101001)
    IfFlagEnabled(-1, 72101002)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(12105050)
    EnableFlag(12101020)
    ForceAnimation(2100215, 7012)
    ForceAnimation(2100220, 7012)
    WaitFrames(frames=49)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2100215)
    DisableBackread(2100220)


@NeverRestart(12101021)
def Event_12101021():
    """Event 12101021"""
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(2100216, 7023, loop=True)
    ForceAnimation(2100221, 7023, loop=True)
    IfCharacterBackreadEnabled(1, 2100216)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100216, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100216, 7024)
    ForceAnimation(2100221, 7024)
    WaitFrames(frames=30)
    EnableFlag(12105051)
    WaitFrames(frames=79)
    ForceAnimation(2100216, 7021, loop=True)
    ForceAnimation(2100221, 7021, loop=True)
    IfFlagEnabled(-1, 72101010)
    IfFlagEnabled(-1, 72101011)
    IfConditionTrue(0, input_condition=-1)
    EventValueOperation(
        source_flag=12104010,
        source_flag_bit_count=8,
        operand=10,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=900, flag=12104020, bit_count=8)
    EventValueOperation(
        source_flag=12104010,
        source_flag_bit_count=8,
        operand=0,
        target_flag=12104020,
        target_flag_bit_count=8,
        calculation_type=CalculationType.Subtract,
    )
    IfEventValueEqual(0, flag=0, bit_count=1, value=0)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=900, flag=12104010, bit_count=8)
    DisableFlag(12105051)
    EnableFlag(12101021)
    ForceAnimation(2100216, 7022)
    ForceAnimation(2100221, 7022)
    WaitFrames(frames=49)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2100216)
    DisableBackread(2100221)


@NeverRestart(12101022)
def Event_12101022():
    """Event 12101022"""
    GotoIfFlagEnabled(Label.L0, flag=6620)
    ForceAnimation(2100230, 7053, loop=True)
    IfCharacterBackreadEnabled(1, 2100230)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2100230, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100230, 7054)
    WaitFrames(frames=30)
    EnableFlag(12105052)
    WaitFrames(frames=79)
    ForceAnimation(2100230, 7051, loop=True)
    IfFlagEnabled(0, 12101023)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10000, host_only=False)
    DisableFlag(12105052)
    ForceAnimation(2100230, 7052)
    WaitFrames(frames=74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100230, 7053, loop=True)


@NeverRestart(12101024)
def Event_12101024():
    """Event 12101024"""
    GotoIfFlagEnabled(Label.L0, flag=6622)
    ForceAnimation(2100231, 7053, loop=True)
    IfCharacterBackreadEnabled(1, 2100231)
    IfFlagEnabled(1, 12100105)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2100231, 7054)
    WaitFrames(frames=30)
    EnableFlag(12105054)
    WaitFrames(frames=79)
    ForceAnimation(2100231, 7051, loop=True)
    IfFlagEnabled(0, 12101025)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10010, host_only=False)
    DisableFlag(12105054)
    ForceAnimation(2100231, 7052)
    WaitFrames(frames=74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100231, 7053, loop=True)


@NeverRestart(12101026)
def Event_12101026():
    """Event 12101026"""
    GotoIfFlagEnabled(Label.L0, flag=6670)
    IfCharacterBackreadEnabled(1, 2100230)
    IfFlagEnabled(1, 12101022)
    IfFlagEnabled(1, 12100105)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    ForceAnimation(2100230, 7054)
    WaitFrames(frames=30)
    EnableFlag(12105056)
    WaitFrames(frames=79)
    ForceAnimation(2100230, 7051, loop=True)
    IfFlagEnabled(0, 12101027)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10050, host_only=False)
    DisableFlag(12105056)
    ForceAnimation(2100230, 7052)
    WaitFrames(frames=74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100230, 7053, loop=True)


@NeverRestart(12101028)
def Event_12101028():
    """Event 12101028"""
    GotoIfFlagEnabled(Label.L0, flag=50000100)
    IfCharacterBackreadEnabled(1, 2100231)
    IfFlagEnabled(1, 12101024)
    IfFlagEnabled(1, 9801)
    IfFlagEnabled(1, 6899)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    ForceAnimation(2100231, 7054)
    WaitFrames(frames=30)
    EnableFlag(12105058)
    WaitFrames(frames=79)
    ForceAnimation(2100231, 7051, loop=True)
    IfFlagEnabled(0, 12101029)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10040, host_only=False)
    DisableFlag(12105058)
    ForceAnimation(2100231, 7052)
    WaitFrames(frames=74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100231, 7053, loop=True)


@NeverRestart(12101100)
def Event_12101100():
    """Event 12101100"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 6899)
    IfFlagEnabled(1, 9801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12101101)


@RestartOnRest(12105060)
def Event_12105060():
    """Event 12105060"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12105061)
    IfFlagEnabled(0, 72100140)
    EnableFlag(12105061)
    DisableFlag(72100140)
    DisableFlagRange((6011, 6025))
    RotateToFaceEntity(PLAYER, 2100218, animation=101310)
    Wait(1.0)
    ForceAnimation(2100218, 7003)
    WaitFrames(frames=39)
    SetDisplayMask(2100218, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=23, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=26, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=27, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=28, switch_type=OnOffChange.On)
    ForceAnimation(2100218, 7004)
    WaitFrames(frames=49)
    ForceAnimation(2100218, 7001, loop=True)
    Restart()


@NeverRestart(12105062)
def Event_12105062():
    """Event 12105062"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=12105063)
    ForceAnimation(2100218, 0, loop=True)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SkipLinesIfFlagDisabled(1, 6011)
    SetDisplayMask(2100218, bit_index=20, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6012)
    SetDisplayMask(2100218, bit_index=21, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6013)
    SetDisplayMask(2100218, bit_index=22, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6014)
    SetDisplayMask(2100218, bit_index=23, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6015)
    SetDisplayMask(2100218, bit_index=24, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6016)
    SetDisplayMask(2100218, bit_index=25, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6017)
    SetDisplayMask(2100218, bit_index=26, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6018)
    SetDisplayMask(2100218, bit_index=27, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, 6019)
    SetDisplayMask(2100218, bit_index=28, switch_type=OnOffChange.Off)
    IfFlagEnabled(-1, 6071)
    IfFlagEnabled(-1, 6072)
    IfFlagEnabled(-1, 6073)
    IfFlagEnabled(-1, 6074)
    IfFlagEnabled(-1, 6075)
    IfFlagEnabled(-1, 6076)
    IfFlagEnabled(-1, 6077)
    IfFlagEnabled(-1, 6078)
    IfFlagEnabled(-1, 6079)
    IfFlagEnabled(-1, 6080)
    IfFlagEnabled(-1, 6081)
    IfFlagEnabled(-1, 6082)
    IfFlagEnabled(-1, 6083)
    IfFlagEnabled(-1, 6084)
    IfFlagEnabled(-1, 6085)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(2100218, 7004)
    WaitFrames(frames=89)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2100218, 7001, loop=True)
    IfCharacterHuman(14, PLAYER)
    EndIfConditionFalse(14)
    EnableFlag(12105063)
    IfFlagEnabled(-1, 6071)
    IfFlagEnabled(-1, 6072)
    IfFlagEnabled(-1, 6073)
    IfFlagEnabled(-1, 6074)
    IfFlagEnabled(-1, 6075)
    IfFlagEnabled(-1, 6076)
    IfFlagEnabled(-1, 6077)
    IfFlagEnabled(-1, 6078)
    IfFlagEnabled(-1, 6079)
    IfFlagEnabled(-1, 6080)
    IfFlagEnabled(-1, 6081)
    IfFlagEnabled(-1, 6082)
    IfFlagEnabled(-1, 6083)
    IfFlagEnabled(-1, 6084)
    IfFlagEnabled(-1, 6085)
    IfConditionFalse(0, input_condition=-1)
    DisableFlag(12105063)
    ForceAnimation(2100218, 7003)
    WaitFrames(frames=39)
    Restart()


@NeverRestart(12105064)
def Event_12105064():
    """Event 12105064"""
    DisableNetworkSync()
    ForceAnimation(2100232, 7053, loop=True)
    EndIfClient()
    IfFlagEnabled(1, 6900)
    IfFlagDisabled(1, 6071)
    IfFlagEnabled(2, 6901)
    IfFlagDisabled(2, 6072)
    IfFlagEnabled(3, 6902)
    IfFlagDisabled(3, 6073)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(2100232, 7054)
    WaitFrames(frames=30)
    WaitFrames(frames=79)
    ForceAnimation(2100232, 7051, loop=True)
    IfCharacterHuman(4, PLAYER)
    IfActionButtonParamActivated(4, action_button_id=6025, entity=2100232)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFlagEnabled(3, 6071)
    SkipLinesIfFlagDisabled(2, 6900)
    AwardItemLot(2100900, host_only=False)
    EnableFlag(6071)
    SkipLinesIfFlagEnabled(3, 6072)
    SkipLinesIfFlagDisabled(2, 6901)
    AwardItemLot(2100910, host_only=False)
    EnableFlag(6072)
    SkipLinesIfFlagEnabled(3, 6073)
    SkipLinesIfFlagDisabled(2, 6902)
    AwardItemLot(2100920, host_only=False)
    EnableFlag(6073)
    ForceAnimation(2100232, 7052)
    WaitFrames(frames=74)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2100232)


@RestartOnRest(12105070)
def Event_12105070(_, flag: int, flag_1: int, bit_index: uchar):
    """Event 12105070"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12105061)
    IfFlagEnabled(0, flag)
    EnableFlag(12105061)
    DisableFlag(flag)
    DisableFlagRange((6011, 6025))
    RotateToFaceEntity(PLAYER, 2100218, animation=101310)
    Wait(1.0)
    ForceAnimation(2100218, 7003)
    WaitFrames(frames=39)
    EnableFlag(flag_1)
    SetDisplayMask(2100218, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=23, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=26, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=27, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(2100218, bit_index=bit_index, switch_type=OnOffChange.Off)
    ForceAnimation(2100218, 7004)
    WaitFrames(frames=49)
    ForceAnimation(2100218, 7001, loop=True)
    Restart()


@NeverRestart(12105200)
def Event_12105200():
    """Event 12105200"""
    DisableFlag(12105200)
    IfCharacterHasSpecialEffect(0, 2100700, 153)
    WaitFrames(frames=1)


@NeverRestart(12105210)
def Event_12105210():
    """Event 12105210"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 70000100)
    DisableFlag(70000100)
    CancelSpecialEffect(PLAYER, 2200)
    CancelSpecialEffect(PLAYER, 2210)
    CancelSpecialEffect(PLAYER, 2220)
    Restart()


@NeverRestart(12105300)
def Event_12105300():
    """Event 12105300"""
    DisableNetworkSync()
    EndIfClient()
    SkipLinesIfFlagDisabled(1, 5020)
    EnableFlag(6228)
    SkipLinesIfFlagDisabled(1, 5021)
    EnableFlag(6235)
    IfFlagEnabled(-1, 5023)
    IfFlagEnabled(-1, 70009200)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6242)
    SkipLinesIfFlagDisabled(1, 5027)
    EnableFlag(6249)
    IfFlagEnabled(-2, 5029)
    IfFlagEnabled(-2, 70009220)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6256)
    SkipLinesIfFlagDisabled(1, 5022)
    EnableFlag(6236)
    IfFlagEnabled(-3, 5025)
    IfFlagEnabled(-3, 70009210)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6243)
    SkipLinesIfFlagDisabled(1, 5028)
    EnableFlag(6251)
    IfFlagEnabled(-4, 5031)
    IfFlagEnabled(-4, 70009230)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6258)
    IfFlagEnabled(-5, 5033)
    IfFlagEnabled(-5, 70009240)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6259)


@RestartOnRest(12105310)
def Event_12105310(_, flag: int, entity: int):
    """Event 12105310"""
    IfFlagEnabled(0, flag)
    WaitFrames(frames=31)
    ForceAnimation(entity, 7000)
    WaitFrames(frames=109)
    ForceAnimation(entity, 7001, loop=True)
    IfFlagDisabled(0, flag)
    ForceAnimation(entity, 7002)
    WaitFrames(frames=74)
    Restart()


@NeverRestart(12107000)
def Event_12107000(_, flag: int, target_entity: int, respawn_point_id: int):
    """Event 12107000"""
    EndIfClient()
    IfFlagEnabled(0, flag)
    RotateToFaceEntity(PLAYER, target_entity, animation=101164)
    Wait(4.0)
    WarpPlayerToRespawnPoint(respawn_point_id)


@NeverRestart(12107100)
def Event_12107100(_, flag: int, target_entity: int, flag_1: int):
    """Event 12107100"""
    EndIfClient()
    IfFlagEnabled(0, flag)
    Wait(4.0)
    DisableFlag(9020)
    DisableFlag(9021)
    DisableFlag(9022)
    DisableFlag(9023)
    DisableFlag(9024)
    DisableFlag(9025)
    DisableFlag(9026)
    EnableFlag(flag_1)
    DisableFlag(flag)
    End()
    RotateToFaceEntity(PLAYER, target_entity, animation=101164)


@NeverRestart(12107200)
def Event_12107200(_, flag: int, respawn_point_id: int, flag_1: int):
    """Event 12107200"""
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    WarpPlayerToRespawnPoint(respawn_point_id)
    EnableFlag(flag_1)
