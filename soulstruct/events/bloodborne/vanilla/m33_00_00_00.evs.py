"""
linked:
162

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_邪神
78: ボス_戦闘開始
94: ボス戦_撃破時間
112: ギミック_エレベーター起動
140: PC情報_故郷到達時
162: N:\\SPRJ\\data\\Param\\event\\common.emevd
238: 
"""
from soulstruct.events.bloodborne import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=50, args=(3300950, 3301950, 999, 13307800))
    RunEvent(7000, slot=51, args=(3300951, 3301951, 13301800, 13307820))
    RunEvent(7100, slot=50, args=(73300200, 3301950))
    RunEvent(7100, slot=51, args=(73300201, 3301951))
    RunEvent(7200, slot=50, args=(73300100, 3301950, 2102953))
    RunEvent(7200, slot=51, args=(73300101, 3301951, 2102953))
    RunEvent(7300, slot=50, args=(72103300, 3301950))
    RunEvent(7300, slot=51, args=(72103301, 3301951))
    RunEvent(9200, slot=10, args=(3303900,))
    DisableSoundEvent(3304000)
    DisableSoundEvent(3304001)
    StartPlayLogMeasurement(3300000, 0, overwrite=False)
    StartPlayLogMeasurement(3300001, 18, overwrite=True)
    RunEvent(13300990)
    CreateObjectFX(8028, obj=3301020, model_point=100)
    CreateObjectFX(8028, obj=3301022, model_point=100)
    CreateObjectFX(8028, obj=3301023, model_point=100)
    CreateObjectFX(8028, obj=3301024, model_point=100)
    CreateObjectFX(8028, obj=3301025, model_point=100)
    ForceAnimation(3301020, 200, loop=True)
    ForceAnimation(3301022, 200, loop=True)
    ForceAnimation(3301023, 200, loop=True)
    ForceAnimation(3301024, 200, loop=True)
    ForceAnimation(3301025, 200, loop=True)
    RunEvent(13304872)
    RunEvent(13304873)
    RunEvent(13301800)
    RunEvent(13301801)
    RunEvent(13301802)
    RunEvent(13304870)
    RunEvent(13304871)
    RunEvent(13304802)
    RunEvent(13304803, slot=1)
    RunEvent(13304804)
    RunEvent(13304805)
    RunEvent(13304807)
    RunEvent(13304808)
    RunEvent(13301803)
    RunEvent(13304820, slot=0, args=(3311, 3311, 13, 9, 13), arg_types="hihBB")
    RunEvent(13304820, slot=1, args=(3322, 3322, 14, 8, 14), arg_types="hihBB")
    RunEvent(13304830, slot=0, args=(3301, 3301, 4, 482, 200, 8020, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=1, args=(3302, 3302, 6, 482, 180, 8020, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=2, args=(3303, 3303, 8, 482, 150, 8020, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=3, args=(3304, 3304, 5, 481, 200, 8010, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=4, args=(3305, 3305, 7, 481, 150, 8010, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=5, args=(3306, 3306, 9, 481, 120, 8010, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=6, args=(3307, 3307, 10, 481, 120, 8010, 1.0, 1.5), arg_types="hihiiiff")
    RunEvent(13304830, slot=7, args=(3308, 3308, 3, 483, 200, 8030, 0.20000000298023224, 0.30000001192092896), 
             arg_types="hihiiiff")
    RunEvent(13304830, slot=8, args=(3309, 3309, 11, 484, 100, 8040, 0.20000000298023224, 0.30000001192092896), 
             arg_types="hihiiiff")
    RunEvent(13304830, slot=9, args=(3310, 3310, 12, 483, 100, 8030, 0.20000000298023224, 0.30000001192092896), 
             arg_types="hihiiiff")
    RunEvent(13304840)
    RunEvent(13300100)
    RunEvent(13300110)
    RunEvent(13300111)
    RunEvent(13300112)
    RunEvent(13300113)
    RunEvent(13300120)
    RunEvent(13300130, slot=0, args=(3300551, 53300990))
    RunEvent(13300130, slot=1, args=(3300590, 53300980))
    RunEvent(13300130, slot=2, args=(3300591, 53300970))
    RunEvent(13300130, slot=3, args=(3300555, 53300960))
    RunEvent(13300130, slot=4, args=(3300558, 53300940))
    RunEvent(13300130, slot=5, args=(3300560, 53300930))
    RunEvent(13300130, slot=6, args=(3300561, 53300920))
    RunEvent(13300130, slot=7, args=(3300562, 53300910))
    RunEvent(13300130, slot=8, args=(3300565, 53300890))
    RunEvent(13300130, slot=9, args=(3300569, 53300870))
    RunEvent(13300130, slot=10, args=(3300573, 53300850))
    RunEvent(13300130, slot=11, args=(3300575, 53300830))
    RunEvent(13300130, slot=12, args=(3300576, 53300820))
    RunEvent(13300130, slot=13, args=(3300578, 53300800))
    RunEvent(13300130, slot=14, args=(3300581, 53300790))
    RunEvent(13300130, slot=15, args=(3300582, 53300780))
    RunEvent(13300130, slot=16, args=(3300583, 53300770))
    RunEvent(13300130, slot=17, args=(3300587, 53300750))
    RunEvent(13300130, slot=18, args=(3300588, 53300740))
    RunEvent(13300130, slot=19, args=(3300589, 53300730))
    RunEvent(13300130, slot=20, args=(3300593, 53300700))
    RunEvent(13300130, slot=21, args=(3300250, 53300690))
    RunEvent(13300130, slot=22, args=(3300251, 53300680))
    RunEvent(13300130, slot=23, args=(3300252, 53300670))
    RunEvent(13300130, slot=24, args=(3300253, 53300660))
    RunEvent(13300130, slot=25, args=(3300254, 53300650))
    RunEvent(13300130, slot=26, args=(3300257, 53300640))
    RunEvent(13300130, slot=27, args=(3300258, 53300630))
    RunEvent(13300130, slot=28, args=(3300259, 53300620))
    RunEvent(13300130, slot=29, args=(3300261, 53300610))
    RunEvent(13300130, slot=30, args=(3300262, 53300600))
    RunEvent(13300200)
    RunEvent(13300210)
    RunEvent(13300220, slot=0, args=(3300721,))
    RunEvent(13300220, slot=1, args=(3300722,))
    RunEvent(13305150, slot=0, args=(3300411, 3302205, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=1, args=(3300412, 3302205, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=2, args=(3300452, 3302205, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=3, args=(3300459, 3302205, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=4, args=(3300500, 3302206, 15.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=5, args=(3300502, 3302207, 2.0, 450), arg_types="iifi")
    RunEvent(13305150, slot=6, args=(3300413, 3302210, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=7, args=(3300460, 3302210, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=8, args=(3300413, 3302211, 5.0, 0), arg_types="iifi")
    RunEvent(13305150, slot=9, args=(3300460, 3302211, 5.0, 0), arg_types="iifi")
    RunEvent(13305210, slot=0, args=(3300102, 2.0, 7000, 7001, 0.0, 218300), arg_types="ifiifi")
    RunEvent(13305210, slot=1, args=(3300103, 2.0, 7000, 7001, 0.0, 218300), arg_types="ifiifi")
    RunEvent(13305210, slot=2, args=(3300104, 2.0, 7000, 7001, 0.0, 218300), arg_types="ifiifi")
    RunEvent(13305220)
    RunEvent(13305230)
    RunEvent(13305200, slot=1, args=(3300459, 3302301, 3300461, 5.0, 3306001), arg_types="iiifi")
    RunEvent(13305200, slot=2, args=(3300452, 3302302, 3300460, 5.0, 3306002), arg_types="iiifi")
    RunEvent(13305250, slot=0, args=(3300584, 3302410, 13305255))
    RunEvent(13305250, slot=1, args=(3300593, 3302411, 13305256))
    RunEvent(13305255, slot=0, args=(3300584, 3302410))
    RunEvent(13305255, slot=1, args=(3300593, 3302411))
    RunEvent(13305030, slot=0, args=(3300500, 3300520))
    RunEvent(13305030, slot=1, args=(3300501, 3300521))
    RunEvent(13305030, slot=2, args=(3300502, 3300522))
    RunEvent(13305040)
    RunEvent(13305041)
    RunEvent(13300700)
    RunEvent(13304700, slot=0, args=(3300700, 13304701, 13304711, 3300, 13301700))
    RunEvent(13304710, slot=0, args=(3300700, 13304701, 13304711, 13304721))
    RunEvent(13304720, slot=0, args=(3300700, 13304701, 13304711, 13304721))
    RunEvent(13304730, slot=0, args=(3300700, 13304701, 13304711, 3300, 13304800, 13301700))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6327)
    EnableFlag(13301999)
    SkipLinesIfFlagOn(5, 13301999)
    EnableObject(3301500)
    DisableObject(3301501)
    EnableTreasure(3301500)
    DisableTreasure(3301501)
    SkipLines(4)
    DisableObject(3301500)
    EnableObject(3301501)
    DisableTreasure(3301500)
    EnableTreasure(3301501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagOff(1, 6328)
    EnableFlag(13301998)
    SkipLinesIfFlagOn(5, 13301998)
    EnableObject(3301502)
    DisableObject(3301503)
    EnableTreasure(3301502)
    DisableTreasure(3301503)
    SkipLines(4)
    DisableObject(3301502)
    EnableObject(3301503)
    DisableTreasure(3301502)
    EnableTreasure(3301503)
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagOff(1, 6329)
    EnableFlag(13301997)
    SkipLinesIfFlagOn(5, 13301997)
    EnableObject(3301504)
    DisableObject(3301505)
    EnableTreasure(3301504)
    DisableTreasure(3301505)
    SkipLines(4)
    DisableObject(3301504)
    EnableObject(3301505)
    DisableTreasure(3301504)
    EnableTreasure(3301505)
    IfCharacterHuman(12, PLAYER)
    SkipLinesIfConditionFalse(2, 12)
    SkipLinesIfFlagOff(1, 6330)
    EnableFlag(13301996)
    SkipLinesIfFlagOn(5, 13301996)
    EnableObject(3301506)
    DisableObject(3301507)
    EnableTreasure(3301506)
    DisableTreasure(3301507)
    SkipLines(4)
    DisableObject(3301506)
    EnableObject(3301507)
    DisableTreasure(3301506)
    EnableTreasure(3301507)
    IfCharacterHuman(11, PLAYER)
    SkipLinesIfConditionFalse(2, 11)
    SkipLinesIfFlagOff(1, 6331)
    EnableFlag(13301995)
    SkipLinesIfFlagOn(5, 13301995)
    EnableObject(3301508)
    DisableObject(3301509)
    EnableTreasure(3301508)
    DisableTreasure(3301509)
    SkipLines(4)
    DisableObject(3301508)
    EnableObject(3301509)
    DisableTreasure(3301508)
    EnableTreasure(3301509)


def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(3303950)
    DisableGravity(3303950)
    DisableCharacterCollision(3303950)
    DisableAnimations(3303951)
    DisableGravity(3303951)
    DisableCharacterCollision(3303951)


@RestartOnRest
def Event13304700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13304700: Event 13304700 """
    GotoIfFlagOff(Label.L0, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagOn(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfCharacterHuman(2, PLAYER)
    IfPlayerSoulLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagOff(1, arg_16_19)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011, wait_for_completion=True)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event13304710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13304710: Event 13304710 """
    EndIfFlagOn(arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_8_11)
    IfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, 9100, affect_npc_part_hp=False)
    ReplanAI(arg_0_3)
    EnableFlag(arg_12_15)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    IfFlagOn(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    Restart()


@RestartOnRest
def Event13304720(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13304720: Event 13304720 """
    EndIfFlagOn(arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(1, arg_12_15)
    IfFlagOn(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()


@RestartOnRest
def Event13304730(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13304730: Event 13304730 """
    IfFlagOn(-15, arg_8_11)
    IfFlagOn(-15, arg_12_15)
    IfFlagOn(-15, arg_16_19)
    EndIfConditionTrue(-15)
    IfFlagOn(1, arg_4_7)
    IfHealthEqual(2, arg_0_3, 0.0)
    IfFlagOn(3, arg_16_19)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    EnableFlag(arg_20_23)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(arg_0_3, 7010)


def Event13301800():
    """ 13301800: Event 13301800 """
    GotoIfThisEventOff(Label.L0)
    DisableSoundEvent(3303802)
    DisableSoundEvent(3303803)
    DisableCharacter(3300800)
    Kill(3300800, award_souls=True)
    DisableObject(3301800)
    DisableObject(3301801)
    DeleteFX(3303800, erase_root_only=True)
    DeleteFX(3303801, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3300800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3301800)
    DisableObject(3301801)
    DeleteFX(3303800, erase_root_only=True)
    DeleteFX(3303801, erase_root_only=True)
    SetLockedCameraSlot(game_map=NIGHTMARE_FRONTIER, camera_slot=0)
    Wait(3.0)
    KillBoss(3300800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(25)
    AwardItemLot(80000200, host_only=False)
    EnableFlag(3300)
    EnableFlag(9466)
    StopPlayLogMeasurement(3300000)
    StopPlayLogMeasurement(3300001)
    StopPlayLogMeasurement(3300010)
    CreatePlayLog(40)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 52, PlayLogMultiplayerType.HostOnly)


def Event13301801():
    """ 13301801: Event 13301801 """
    DisableNetworkSync()
    EndIfFlagOn(13301800)
    IfFlagOn(1, 13301800)
    IfCharacterBackreadDisabled(2, 3300800)
    IfHealthLessThanOrEqual(2, 3300800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=3302800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


@RestartOnRest
def Event13301802():
    """ 13301802: Event 13301802 """
    EndIfFlagOn(13301800)
    EndIfThisEventOn()
    DisableCharacterCollision(3300800)
    DisableGravity(3300800)
    EnableInvincibility(3300800)
    ForceAnimation(3300800, 7003, loop=True)
    IfFlagOff(1, 13301800)
    IfThisEventOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3302805)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13304800)
    ForceAnimation(3300800, 7006)
    WaitFrames(30)
    ForceAnimation(3300800, 7002)
    WaitFrames(160)
    EnableGravity(3300800)
    DisableInvincibility(3300800)
    EnableCharacterCollision(3300800)
    EndIfFlagOn(9302)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(9302)


def Event13301803():
    """ 13301803: Event 13301803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13304800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(13304800)
    EnableFlag(13301802)


def Event13304870():
    """ 13304870: Event 13304870 """
    EndIfFlagOn(13301800)
    GotoIfFlagOn(Label.L0, 13301802)
    SkipLinesIfClient(2)
    DisableObject(3301800)
    DeleteFX(3303800, erase_root_only=False)
    DisableObject(3301801)
    DeleteFX(3303801, erase_root_only=False)
    IfFlagOff(1, 13301800)
    IfFlagOn(1, 13301802)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOff(2, 13301800)
    IfFlagOn(2, 13304800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(3301800)
    EnableObject(3301801)
    CreateFX(3303800)
    CreateFX(3303801)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfActionButtonParam(3, action_button_id=3300800, entity=3301800)
    IfFlagOff(3, 13301800)
    IfFlagOn(4, 13301800)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    RotateToFaceEntity(PLAYER, 3302800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(5, PLAYER)
    IfCharacterInsideRegion(5, PLAYER, region=3302801)
    IfCharacterHuman(6, PLAYER)
    IfTimeElapsed(6, 2.0)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(1, 6)
    EnableFlag(13304800)
    Restart()


@RestartOnRest
def Event13304871():
    """ 13304871: Event 13304871 """
    DisableNetworkSync()
    EndIfFlagOn(13301800)
    IfFlagOff(1, 13301800)
    IfFlagOn(1, 13301802)
    IfFlagOn(1, 13304800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=3300800, entity=3301800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3302800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3302801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(13304801)
    Restart()


def Event13304872():
    """ 13304872: Event 13304872 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 3301800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13304873():
    """ 13304873: Event 13304873 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 3301800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@RestartOnRest
def Event13304802():
    """ 13304802: Event 13304802 """
    EndIfFlagOn(13301800)
    DisableAI(3300800)
    DisableHealthBar(3300800)
    IfFlagOn(0, 13304800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3300800, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13304800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3300800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3300800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3300800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3300800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3300800)
    EnableBossHealthBar(3300800, name=512000, slot=0)
    CreatePlayLog(78)
    StartPlayLogMeasurement(3300010, 94, overwrite=True)


def Event13304803():
    """ 13304803: Event 13304803 """
    DisableNetworkSync()
    EndIfFlagOn(13301800)
    GotoIfThisEventOn(Label.L0)
    DisableSoundEvent(3303802)
    DisableSoundEvent(3303803)
    IfFlagOff(1, 13301800)
    IfFlagOn(1, 13304802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 13304801)
    IfCharacterInsideRegion(1, PLAYER, region=3302802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3303802)
    IfHasTAEEvent(2, 3300800, tae_event_id=10)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 13301800)
    IfFlagOn(2, 13304802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 13304801)
    IfCharacterInsideRegion(2, PLAYER, region=3302802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3303802)
    WaitFrames(0)
    EnableBossMusic(3303803)


def Event13304804():
    """ 13304804: Event 13304804 """
    EndIfFlagOn(13301800)
    DisableNetworkSync()
    IfHealthGreaterThan(1, 3300800, 0.0)
    IfEntityWithinDistance(1, PLAYER, 3300800, radius=14.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=NIGHTMARE_FRONTIER, camera_slot=1)
    IfHealthGreaterThan(1, 3300800, 0.0)
    IfEntityBeyondDistance(0, PLAYER, 3300800, radius=17.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=NIGHTMARE_FRONTIER, camera_slot=0)
    Restart()


def Event13304805():
    """ 13304805: Event 13304805 """
    DisableNetworkSync()
    EndIfFlagOn(13301800)
    IfFlagOn(0, 13301800)
    DisableBossMusic(3303802)
    DisableBossMusic(3303803)
    DisableBossMusic(-1)


def Event13304807():
    """ 13304807: Event 13304807 """
    EndIfFlagOn(13301800)
    EndIfThisEventOn()
    IfHealthLessThan(0, 3300800, 0.699999988079071)
    Wait(0.10000000149011612)
    ResetAnimation(3300800, disable_interpolation=True)
    AICommand(3300800, command_id=100, slot=0)
    ReplanAI(3300800)
    IfHasTAEEvent(0, 3300800, tae_event_id=10)
    AICommand(3300800, command_id=-1, slot=0)
    ReplanAI(3300800)


def Event13304808():
    """ 13304808: Event 13304808 """
    EndIfFlagOn(13301800)
    EndIfThisEventOn()
    IfHealthLessThan(1, 3300800, 0.30000001192092896)
    IfFlagOn(1, 13304807)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    ResetAnimation(3300800, disable_interpolation=True)
    AICommand(3300800, command_id=110, slot=0)
    ReplanAI(3300800)
    IfHasTAEEvent(0, 3300800, tae_event_id=10)
    AICommand(3300800, command_id=-1, slot=0)
    ReplanAI(3300800)


@RestartOnRest
def Event13304820(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_10_10: uchar, arg_11_11: uchar):
    """ 13304820: Event 13304820 """
    EndIfFlagOn(13301800)
    GotoIfThisEventOn(Label.L0)
    SetCollisionMask(3300800, bit_index=arg_11_11, switch_type=OnOffChange.Off)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(0, 3300800, 5402)
    SetCollisionMask(3300800, bit_index=arg_10_10, switch_type=OnOffChange.Off)
    SetCollisionMask(3300800, bit_index=arg_11_11, switch_type=OnOffChange.On)
    CreateNPCPart(3300800, npc_part_id=arg_0_1, part_index=arg_8_9, part_health=9999999, damage_correction=0.0, 
                  body_damage_correction=0.0, is_invincible=True, start_in_stop_state=False)
    SetNPCPartEffects(3300800, npc_part_id=arg_4_7, material_special_effect_id=59, material_fx_id=59)


@RestartOnRest
def Event13304830(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: float, arg_28_31: float):
    """ 13304830: Event 13304830 """
    EndIfFlagOn(13301800)
    CreateNPCPart(3300800, npc_part_id=arg_0_1, part_index=arg_8_9, part_health=arg_16_19, damage_correction=arg_24_27, 
                  body_damage_correction=arg_24_27, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(3300800, npc_part_id=arg_4_7, material_special_effect_id=59, material_fx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, 3300800, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(3, 3300800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(3300800, npc_part_id=arg_0_1, part_index=arg_8_9, part_health=9999999, damage_correction=1.0, 
                  body_damage_correction=arg_28_31, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(3300800, npc_part_id=arg_4_7, material_special_effect_id=60, material_fx_id=60)
    WaitFrames(1)
    ResetAnimation(3300800, disable_interpolation=False)
    ForceAnimation(3300800, arg_20_23)
    AddSpecialEffect(3300800, arg_12_15, affect_npc_part_hp=False)
    ReplanAI(3300800)
    Wait(30.0)
    AICommand(3300800, command_id=100, slot=1)
    ReplanAI(3300800)
    IfHasTAEEvent(0, 3300800, tae_event_id=300)
    SetNPCPartHealth(3300800, npc_part_id=arg_4_7, desired_hp=-1, overwrite_max=True)
    CancelSpecialEffect(3300800, arg_12_15)
    AICommand(3300800, command_id=-1, slot=1)
    ReplanAI(3300800)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event13304840():
    """ 13304840: Event 13304840 """
    EndIfFlagOn(13301800)
    CreateNPCPart(3300800, npc_part_id=3300, part_index=NPCPartType.Part1, part_health=300, 
                  damage_correction=1.399999976158142, body_damage_correction=1.399999976158142, is_invincible=False, 
                  start_in_stop_state=False)
    SetNPCPartEffects(3300800, npc_part_id=3300, material_special_effect_id=60, material_fx_id=60)
    IfCharacterPartHealthLessThanOrEqual(2, 3300800, npc_part_id=3300, value=0)
    IfHealthLessThanOrEqual(3, 3300800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(3300800, npc_part_id=3300, part_index=NPCPartType.Part1, part_health=9999999, damage_correction=1.0, 
                  body_damage_correction=2.0999999046325684, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(3300800, npc_part_id=3300, material_special_effect_id=60, material_fx_id=60)
    WaitFrames(1)
    ResetAnimation(3300800, disable_interpolation=False)
    ForceAnimation(3300800, 8000)
    AddSpecialEffect(3300800, 480, affect_npc_part_hp=False)
    ReplanAI(3300800)
    Wait(30.0)
    AICommand(3300800, command_id=100, slot=1)
    ReplanAI(3300800)
    IfHasTAEEvent(0, 3300800, tae_event_id=300)
    SetNPCPartHealth(3300800, npc_part_id=3300, desired_hp=-1, overwrite_max=True)
    CancelSpecialEffect(3300800, 480)
    AICommand(3300800, command_id=-1, slot=1)
    ReplanAI(3300800)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event13300100():
    """ 13300100: Event 13300100 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(3301100, 1)
    End()
    ForceAnimation(3301100, 0)
    IfCharacterInsideRegion(0, PLAYER, region=3302710)
    ForceAnimation(3301100, 1)


def Event13300110():
    """ 13300110: Event 13300110 """
    IfFlagOn(1, 13300115)
    IfFlagOff(2, 13300115)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(3301000, 6)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    EnableObjectActivation(3301011, obj_act_id=3300000)
    SkipLines(3)
    EndOfAnimation(3301000, 2)
    EnableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)
    SkipLinesIfFlagOn(4, 13300111)
    EndOfAnimation(3301000, 2)
    EnableFlag(13300115)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)


def Event13300111():
    """ 13300111: Event 13300111 """
    EndIfThisEventSlotOn()
    DisableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)
    IfCharacterInsideRegion(0, PLAYER, region=3302702)
    CreatePlayLog(112)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    EnableObjectActivation(3301011, obj_act_id=3300000)


def Event13300112():
    """ 13300112: Event 13300112 """
    IfFlagOff(3, 13300115)
    IfFlagOn(3, 13300116)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOn(0, 13300111)
    IfFlagOff(1, 13300115)
    IfFlagOff(1, 13300116)
    IfCharacterInsideRegion(1, PLAYER, region=3302700)
    IfFlagOff(2, 13300115)
    IfFlagOff(2, 13300116)
    IfCharacterInsideRegion(2, PLAYER, region=3302706)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13300116)
    ForceAnimation(3301011, 1)
    ForceAnimation(3301000, 1)
    WaitFrames(10)
    ForceAnimation(3301000, 2)
    WaitFrames(150)
    IfAllPlayersOutsideRegion(4, region=3302706)
    IfAllPlayersOutsideRegion(4, region=3302701)
    IfConditionTrue(0, input_condition=4)
    ForceAnimation(3301011, 3)
    ForceAnimation(3301000, 3)
    WaitFrames(10)
    EnableFlag(13300115)
    DisableFlag(13300116)
    EnableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)
    Restart()


def Event13300113():
    """ 13300113: Event 13300113 """
    IfFlagOn(3, 13300115)
    IfFlagOn(3, 13300116)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOn(0, 13300111)
    IfFlagOn(1, 13300115)
    IfFlagOff(1, 13300116)
    IfCharacterInsideRegion(1, PLAYER, region=3302701)
    IfFlagOn(2, 13300115)
    IfFlagOff(2, 13300116)
    IfCharacterInsideRegion(2, PLAYER, region=3302705)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13300116)
    ForceAnimation(3301010, 1)
    ForceAnimation(3301000, 5)
    WaitFrames(10)
    ForceAnimation(3301000, 6)
    WaitFrames(150)
    IfAllPlayersOutsideRegion(4, region=3302705)
    IfAllPlayersOutsideRegion(4, region=3302700)
    IfConditionTrue(0, input_condition=4)
    ForceAnimation(3301010, 3)
    ForceAnimation(3301000, 7)
    WaitFrames(10)
    DisableFlag(13300115)
    DisableFlag(13300116)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    EnableObjectActivation(3301011, obj_act_id=3300000)
    Restart()


def Event13300120():
    """ 13300120: Event 13300120 """
    GotoIfThisEventOn(Label.L0)
    DeleteFX(3303002, erase_root_only=True)
    EndIfThisEventSlotOn()
    IfCharacterInsideRegion(0, PLAYER, region=3303000)
    DeleteFX(3303010, erase_root_only=True)
    CreateFX(3303002)
    Wait(4.0)
    CreateFX(3303010)


@RestartOnRest
def Event13300130(_, arg_0_3: int, arg_4_7: int):
    """ 13300130: Event 13300130 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


def Event13300200():
    """ 13300200: Event 13300200 """
    EndIfThisEventOn()
    EndIfFlagOn(1431)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3302170)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    GotoIfMultiplayer(Label.L0)
    SkipLinesIfPlayerGender(2, Gender.Male)
    PlayCutscene(33000000, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=3302171, 
                 move_to_map=NIGHTMARE_FRONTIER)
    SkipLines(1)
    PlayCutscene(33001000, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=3302171, 
                 move_to_map=NIGHTMARE_FRONTIER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfClient(Label.L2)
    SkipLinesIfPlayerGender(2, Gender.Male)
    PlayCutscene(33000000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3302171, 
                 move_to_map=NIGHTMARE_FRONTIER)
    SkipLines(1)
    PlayCutscene(33001000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3302171, 
                 move_to_map=NIGHTMARE_FRONTIER)
    Goto(Label.L1)

    # --- 2 --- #
    DefineLabel(2)
    SkipLinesIfPlayerGender(2, Gender.Male)
    PlayCutscene(33000000, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(33001000, skippable=False, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(9180)


@RestartOnRest
def Event13300210():
    """ 13300210: Event 13300210 """
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 13300200)

    # --- 0 --- #
    DefineLabel(0)
    DisableSoapstoneMessage(3304020)
    DeleteFX(3303020, erase_root_only=True)


@RestartOnRest
def Event13300220(_, arg_0_3: int):
    """ 13300220: Event 13300220 """
    GotoIfThisEventSlotOff(Label.L0)
    DropMandatoryTreasure(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    DisableBackread(2300720)


@RestartOnRest
def Event13305150(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 13305150: Event 13305150 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(-2, input_condition=2)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(3, attacked_entity=arg_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    WaitFrames(arg_12_15)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13305030(_, arg_0_3: int, arg_4_7: int):
    """ 13305030: Event 13305030 """
    DisableGravity(arg_4_7)
    SkipLinesIfThisEventSlotOn(2)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(arg_4_7)
    End()
    Move(arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, model_point=100, 
         set_draw_parent=arg_0_3)
    Restart()


@RestartOnRest
def Event13305040():
    """ 13305040: Event 13305040 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(10, PLAYER, 4691)
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfCharacterHasSpecialEffect(0, PLAYER, 4690)
    Wait(2.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 4690)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 4690)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(2)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(PLAYER, 4691, affect_npc_parts_hp=False)
    Restart()


@RestartOnRest
def Event13305041():
    """ 13305041: Event 13305041 """
    DisableNetworkSync()
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 4690)
    IfCharacterHasSpecialEffect(1, PLAYER, 4691)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 4691)
    Restart()


@RestartOnRest
def Event13305200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int):
    """ 13305200: Event 13305200 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, arg_8_11, radius=arg_12_15)
    IfCharacterInsideRegion(-2, arg_0_3, region=arg_4_7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(arg_8_11, patrol_information_id=arg_16_19)


@RestartOnRest
def Event13305210(_, arg_0_3: int, arg_4_7: float, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 13305210: Event 13305210 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    SetAIParamID(arg_0_3, 218390)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_4_7)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=arg_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHasAIStatus(-3, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-3, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-3, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-3)
    Wait(arg_16_19)
    ForceAnimation(arg_0_3, arg_12_15)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_20_23)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13305220():
    """ 13305220: Event 13305220 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3302150)
    IfFlagOff(1, 13305212)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3300104, 7001)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(3300104, 218311)
    StopEvent(13305210, slot=2)


@RestartOnRest
def Event13305230():
    """ 13305230: Event 13305230 """
    EndIfThisEventOn()
    IfFlagOn(0, 13305220)
    SetCharacterEventTarget(3300104, 10000)
    AICommand(3300104, command_id=50, slot=0)
    IfEntityWithinDistance(-1, 3300104, PLAYER, radius=5.0)
    IfTimeElapsed(-1, 10.0)
    IfConditionTrue(0, input_condition=-1)
    AICommand(3300104, command_id=-1, slot=0)


@RestartOnRest
def Event13305250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13305250: Event 13305250 """
    EndIfFlagOn(arg_8_11)
    GotoIfThisEventSlotOn(Label.L0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13305255(_, arg_0_3: int, arg_4_7: int):
    """ 13305255: Event 13305255 """
    EndIfThisEventSlotOn()
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    ForceAnimation(arg_0_3, 3000)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13300700():
    """ 13300700: Event 13300700 """
    GotoIfThisEventOff(Label.L0)
    DropMandatoryTreasure(3300710)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(3300710)
    DisableGravity(3300710)
    DisableHealthBar(3300710)
    EnableImmortality(3300710)
    WaitFrames(1)
    ForceAnimation(3300710, 9002, loop=True)
    IfAttackedWithDamageType(0, attacked_entity=3300710, attacking_character=-1, damage_type=DamageType.Unspecified)
    ForceAnimation(3300710, 7006)
    WaitFrames(45)
    Move(3300710, destination=3302160, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=0)
    WaitFrames(1)
    DropMandatoryTreasure(3300710)


def Event13300990():
    """ 13300990: Event 13300990 """
    EndIfThisEventOn()
    EndIfClient()
    IfStandingOnCollision(0, 3303500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 140, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 140, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 140, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 140, PlayLogMultiplayerType.HostOnly)
    RunEvent(9350, slot=0, args=(2,))
