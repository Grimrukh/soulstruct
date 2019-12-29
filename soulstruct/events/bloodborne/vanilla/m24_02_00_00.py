"""
linked:
180

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス戦_撃破時間
58: ボス_撃破
70: PC情報_ボス撃破_月の落とし子
104: ボス_戦闘開始
120: PC情報_ボス撃破_月からの使者
154: PC情報_聖堂街C到達時
180: N:\\SPRJ\\data\\Param\\event\\common.events
"""
from soulstruct.events.bloodborne import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=20, args=(2420950, 2421950, 999, 12427800))
    RunEvent(7000, slot=21, args=(2420951, 2421951, 12421800, 12427820))
    RunEvent(7000, slot=22, args=(2420952, 2421952, 12421700, 12427840))
    RunEvent(7100, slot=20, args=(72420200, 2421950))
    RunEvent(7100, slot=21, args=(72420201, 2421951))
    RunEvent(7100, slot=22, args=(72420202, 2421952))
    RunEvent(7200, slot=20, args=(72420100, 2421950, 2102950))
    RunEvent(7200, slot=21, args=(72420101, 2421951, 2102950))
    RunEvent(7200, slot=22, args=(72420102, 2421952, 2102950))
    RunEvent(7300, slot=20, args=(72102420, 2421950))
    RunEvent(7300, slot=21, args=(72102421, 2421951))
    RunEvent(7300, slot=22, args=(72102422, 2421952))
    DeleteFX(2423910, erase_root_only=False)
    RunEvent(12424400, slot=0, args=(12424440, 2423910, 12424420, 12424430, 12421800, 6001))
    RunEvent(12424410, slot=0, args=(0, 2420910, 2422910, 12424420, 12424430, 12424440, 12421800, 10566))
    RunEvent(12424450, slot=0, args=(2420910, 2422911, 12424420, 12424430, 12424800))
    RunEvent(12424460, slot=0, args=(2420910, 2422911, 2422800, 2422801, 101130, 12424450, 2422801))
    RunEvent(9200, slot=4, args=(2423900,))
    RunEvent(9220, slot=4, args=(2420710, 12424220, 12424221, 2420, 24, 2), arg_types='iiiiBB')
    RunEvent(9240, slot=4, args=(2420710, 12424220, 12424221, 12424222, 24, 2), arg_types='iiiiBB')
    RunEvent(9260, slot=4, args=(2420710, 12424220, 12424221, 12424222, 24, 2), arg_types='iiiiBB')
    RunEvent(9280, slot=4, args=(2420710, 12424220, 12424221, 2420, 12424700, 24, 2), arg_types='iiiiiBB')
    StartPlayLogMeasurement(2420000, 0, overwrite=True)
    StartPlayLogMeasurement(2420001, 18, overwrite=True)
    RunEvent(12420990)
    RunEvent(12420400)
    RunEvent(7600, slot=40, args=(2421999, 2423999))
    RunEvent(7600, slot=41, args=(2421998, 2423998))
    CreateHazard(12420020, 2421230, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=0.6000000238418579, life=0.0, repetition_time=1.0)
    RunEvent(12420123)
    RunEvent(12420124)
    RunEvent(12420140)
    RunEvent(12420150)
    RunEvent(12420151)
    RunEvent(12420152)
    RunEvent(12420153)
    RunEvent(12420156)
    RunEvent(12420850, slot=0, args=(2427020, 2427021, 2427022, 12420130, 12420102, 2.0, 2427000, 920200), arg_types='iiiiifii')
    RunEvent(12420850, slot=1, args=(2427025, 2427026, 2427027, 12420132, 12420110, 3.0, 2427017, 920202), arg_types='iiiiifii')
    RunEvent(12420850, slot=2, args=(2427028, 2427029, 2427030, 12420131, 12420111, 3.0, 2427016, 920203), arg_types='iiiiifii')
    RunEvent(12420853)
    RunEvent(12420854)
    RunEvent(12420280, slot=0, args=(2422500,))
    RunEvent(12420280, slot=1, args=(2422501,))
    RunEvent(12420285, slot=0, args=(2422502, 12420032))
    RunEvent(12420285, slot=1, args=(2422503, 12420033))
    RunEvent(12420000, slot=0, args=(2421201, 1, 2420020, 12420120))
    RunEvent(12420000, slot=1, args=(2421223, 1, 2420030, 12420121))
    RunEvent(12420030, slot=0, args=(12420120,))
    RunEvent(12420030, slot=2, args=(12420126,))
    RunEvent(12420030, slot=3, args=(12420127,))
    RunEvent(12420050, slot=0, args=(2421100, 12421000, 9942))
    RunEvent(12420050, slot=1, args=(2421101, 12421001, 9942))
    DisableMapSound(2423802)
    DisableMapSound(2423803)
    DisableMapSound(2423812)
    DisableMapSound(2423813)
    CreateSpawner(2420801)
    RunEvent(12424812)
    RunEvent(12424813)
    RunEvent(12421800)
    RunEvent(12421801)
    RunEvent(12421802)
    RunEvent(12424810)
    RunEvent(12424811)
    RunEvent(12424802)
    RunEvent(12424803)
    RunEvent(12424804)
    RunEvent(12424805)
    RunEvent(12424980)
    RunEvent(12424990)
    RunEvent(12421803)
    RunEvent(12424870, slot=0, args=(2420, 2420, 5, 200, 480, 490, 8040), arg_types='hihiiii')
    RunEvent(12424871, slot=0, args=(2421, 2421, 1, 200, 481, 491, 8010), arg_types='hihiiii')
    RunEvent(12424871, slot=1, args=(2422, 2422, 2, 200, 482, 492, 8000), arg_types='hihiiii')
    RunEvent(12424871, slot=2, args=(2423, 2423, 3, 200, 483, 493, 8030), arg_types='hihiiii')
    RunEvent(12424871, slot=3, args=(2424, 2424, 4, 200, 484, 494, 8020), arg_types='hihiiii')
    RunEvent(12424712)
    RunEvent(12424713)
    RunEvent(12421700)
    RunEvent(12421701)
    RunEvent(12421702)
    RunEvent(12424710)
    RunEvent(12424711)
    RunEvent(12424702)
    RunEvent(12424703)
    RunEvent(12424704)
    RunEvent(12424705)
    RunEvent(12424790)
    RunEvent(12424780)
    RunEvent(12424791)
    RunEvent(12424792, slot=0, args=(2420750,))
    RunEvent(12424792, slot=1, args=(2420751,))
    RunEvent(12421703)
    RunEvent(12424785, slot=0, args=(2420810, 2422816, 10, 12424702))
    RunEvent(12424785, slot=1, args=(2420811, 2422817, 20, 12424790))
    RunEvent(12424784)
    RunEvent(12424787, slot=0, args=(2420711, 2422816, 10, 12424702, 2420810))
    RunEvent(12424787, slot=1, args=(2420712, 2422816, 10, 12424702, 2420810))
    RunEvent(12424795)
    RunEvent(12424770, slot=0, args=(2423711, 2420711))
    RunEvent(12424770, slot=1, args=(2423712, 2420712))
    RunEvent(12424770, slot=2, args=(2423713, 2420713))
    RunEvent(12424770, slot=5, args=(2423716, 2420716))
    RunEvent(12424770, slot=6, args=(2423717, 2420717))
    RunEvent(12424770, slot=8, args=(2423719, 2420719))
    RunEvent(12424770, slot=9, args=(2423720, 2420720))
    RunEvent(12424770, slot=12, args=(2423720, 2420810))
    Label(1)
    RunEvent(12420300)
    RunEvent(12420320)
    RunEvent(12420310)
    RunEvent(12425200, slot=0, args=(2420262,))
    RunEvent(12425210, slot=0, args=(2420250,))
    RunEvent(12425210, slot=1, args=(2420258,))
    RunEvent(12425210, slot=2, args=(2420267,))
    RunEvent(12425225)
    RunEvent(12425221, slot=0, args=(2420256,))
    RunEvent(12425250, slot=0, args=(2420252, 1.5, 2422659, 9.0, 2422252, 20, 1, 1), arg_types='ififiiiB')
    RunEvent(12425245)
    DisableFlag(12425246)
    RunEvent(12425300, slot=0, args=(2420451,))
    RunEvent(12425305, slot=0, args=(2420452,))
    RunEvent(12425310, slot=0, args=(2420352,))
    RunEvent(12425310, slot=1, args=(2420375,))
    RunEvent(12425310, slot=2, args=(2420376,))
    RunEvent(12425310, slot=3, args=(2420387,))
    RunEvent(12425310, slot=4, args=(2420388,))
    RunEvent(12425320, slot=0, args=(2420380, 7012, 7013, 2422380))
    RunEvent(12425320, slot=1, args=(2420381, 7012, 7013, 2422381))
    RunEvent(12425320, slot=2, args=(2420382, 7012, 7013, 2422382))
    RunEvent(12425320, slot=3, args=(2420383, 7012, 7013, 2422383))
    RunEvent(12425320, slot=4, args=(2420384, 7012, 7013, 2422384))
    RunEvent(12425320, slot=5, args=(2420350, 7012, 7013, 2422350))
    RunEvent(12425320, slot=6, args=(2420351, 7012, 7013, 2422351))
    RunEvent(12425320, slot=7, args=(2420377, 7012, 7013, 2422377))
    RunEvent(12425320, slot=8, args=(2420357, 7012, 7013, 2422357))
    RunEvent(12425320, slot=9, args=(2420358, 7012, 7013, 2422358))
    RunEvent(12425320, slot=10, args=(2420359, 7012, 7013, 2422359))
    RunEvent(12425320, slot=11, args=(2420363, 7012, 7013, 2422363))
    RunEvent(12425320, slot=12, args=(2420364, 7012, 7013, 2422364))
    RunEvent(12425320, slot=13, args=(2420385, 7012, 7013, 2422385))
    RunEvent(12425320, slot=14, args=(2420386, 7012, 7013, 2422386))
    SetNetworkUpdateRate(2420811, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RunEvent(12425500, slot=0, args=(2420357, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=1, args=(2420358, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=2, args=(2420359, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=3, args=(2420363, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=4, args=(2420364, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=5, args=(2420251, 5.0, 1, 2422251, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=6, args=(2420255, 3.0, 1, 2422254, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=7, args=(2420255, 3.0, 1, 2422255, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=8, args=(2420256, 5.0, 1, 2422256, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=9, args=(2420377, 5.0, 1, 2422656, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=10, args=(2420351, 5.0, 1, 2422656, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=11, args=(2420385, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=12, args=(2420386, 5.0, 1, 2422650, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=13, args=(2420259, 5.0, 1, 2422259, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=14, args=(2420350, 5.0, 1, 2422654, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=15, args=(2420380, 5.0, 1, 2422654, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=16, args=(2420381, 5.0, 1, 2422654, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=17, args=(2420382, 5.0, 1, 2422654, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=18, args=(2420383, 5.0, 1, 2422654, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=19, args=(2420384, 5.0, 1, 2422654, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=20, args=(2420203, 5.0, 1, 2422653, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=21, args=(2420264, 2.0, 1, 2422264, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=22, args=(2420400, 5.0, 1, 2422256, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=23, args=(2420450, 5.0, 1, 2422300, 0.0), arg_types='ifiif')
    RunEvent(12425500, slot=24, args=(2420451, 5.0, 1, 2422300, 0.0), arg_types='ifiif')
    RunEvent(12425600)
    RunEvent(12425601)
    RunEvent(12425602)
    RunEvent(12425603)
    RunEvent(12425350, slot=0, args=(2420350, 252002, 252000))
    RunEvent(12425350, slot=1, args=(2420351, 252002, 252000))
    RunEvent(12425350, slot=2, args=(2420377, 252002, 252000))
    RunEvent(12425350, slot=3, args=(2420380, 252002, 252000))
    RunEvent(12425350, slot=4, args=(2420381, 252002, 252000))
    RunEvent(12425350, slot=5, args=(2420382, 252002, 252000))
    RunEvent(12425350, slot=6, args=(2420383, 252002, 252000))
    RunEvent(12425350, slot=7, args=(2420384, 252002, 252000))
    RunEvent(12425400, slot=0, args=(2420263, 2422265, 3000))
    RunEvent(12425400, slot=1, args=(2420392, 2422686, 3004))
    RunEvent(12420100)
    RegisterLadder(start_climbing_flag=12420600, stop_climbing_flag=12420601, obj=2421600)
    RunEvent(12420500)
    RunEvent(12420700)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6648)
    EnableFlag(12421999)
    SkipLinesIfFlagOn(5, 12421999)
    EnableObject(2421102)
    DisableObject(2421103)
    EnableTreasure(2421102)
    DisableTreasure(2421103)
    SkipLines(4)
    DisableObject(2421102)
    EnableObject(2421103)
    DisableTreasure(2421102)
    EnableTreasure(2421103)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagOff(1, 6313)
    EnableFlag(12421998)
    SkipLinesIfFlagOn(5, 12421998)
    EnableObject(2421500)
    DisableObject(2421501)
    EnableTreasure(2421500)
    DisableTreasure(2421501)
    SkipLines(4)
    DisableObject(2421500)
    EnableObject(2421501)
    DisableTreasure(2421500)
    EnableTreasure(2421501)


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2423950)
    DisableGravity(2423950)
    DisableCollision(2423950)
    DisableAnimations(2423951)
    DisableGravity(2423951)
    DisableCollision(2423951)
    DisableAnimations(2423952)
    DisableGravity(2423952)
    DisableCollision(2423952)
    RunEvent(12425290)


@RestartOnRest
def Event12420700():
    """ 12420700: Event 12420700 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterDead(0, 2420268)
    AwardItemLot(2420900, host_only=False)


@NeverRestart
def Event12421800():
    """ 12421800: Event 12421800 """
    GotoIfThisEventOff(Label.L0)
    DisableMapSound(2423802)
    DisableMapSound(2423803)
    DisableCharacter(2420800)
    Kill(2420800, award_souls=False)
    DisableObject(2421800)
    DeleteFX(2423800, erase_root_only=False)
    End()
    Label(0)
    IfCharacterDead(0, 2420800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2421800)
    DeleteFX(2423800, erase_root_only=True)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(2420800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(28)
    AwardItemLot(80000300, host_only=False)
    EnableFlag(2421)
    EnableFlag(9459)
    StartPlayLogMeasurement(2420000, 0, overwrite=False)
    StartPlayLogMeasurement(2420001, 18, overwrite=False)
    StartPlayLogMeasurement(2420010, 40, overwrite=False)
    CreatePlayLog(58)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 70, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 70, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 70, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 70, PlayLogMultiplayerType.HostOnly)
    End()
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@NeverRestart
def Event12421801():
    """ 12421801: Event 12421801 """
    DisableNetworkSync()
    EndIfFlagOn(12421800)
    IfFlagOn(1, 12421800)
    IfCharacterBackreadDisabled(2, 2420800)
    IfHealthLessThanOrEqual(2, 2420800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2422800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


@NeverRestart
def Event12421802():
    """ 12421802: Event 12421802 """
    EndIfFlagOn(12421800)
    GotoIfThisEventOff(Label.L0)
    Move(2420800, destination=2422800, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    RotateToFaceEntity(2420800, 2422804, animation=-1, wait_for_completion=False)
    End()
    Label(0)
    ForceAnimation(2420800, 7001, loop=True)
    EnableImmortality(2420800)
    AddSpecialEffect(2420800, 5647, affect_npc_part_hp=False)
    IfFlagOff(1, 12421800)
    IfThisEventOff(1)
    IfCharacterHuman(1, PLAYER)
    IfDamageType(1, attacked_entity=2420800, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2420800, 7000, wait_for_completion=True)
    DisableImmortality(2420800)
    CancelSpecialEffect(2420800, 5647)
    EnableFlag(12424800)
    EndIfFlagOn(9304)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(9304)


@NeverRestart
def Event12421803():
    """ 12421803: Event 12421803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12424800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12424800)
    EnableFlag(12421802)


@NeverRestart
def Event12424810():
    """ 12424810: Event 12424810 """
    EndIfFlagOn(12421800)
    GotoIfFlagOn(Label.L0, 12421802)
    SkipLinesIfClient(2)
    DisableObject(2421800)
    DeleteFX(2423800, erase_root_only=False)
    IfFlagOff(1, 12421800)
    IfFlagOn(1, 12421802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2421800)
    CreateFX(2423800)
    Label(0)
    IfFlagOff(2, 12421800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=2420800, region=2421800)
    IfFlagOn(3, 12421800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2422800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2422801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12424800)
    Restart()


@NeverRestart
def Event12424811():
    """ 12424811: Event 12424811 """
    DisableNetworkSync()
    EndIfFlagOn(12421800)
    IfFlagOff(1, 12421800)
    IfFlagOn(1, 12421802)
    IfFlagOn(1, 12424800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=2420800, region=2421800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2422800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2422801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12424801)
    Restart()


@NeverRestart
def Event12424812():
    """ 12424812: Event 12424812 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 2421800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12424813():
    """ 12424813: Event 12424813 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 2421800, radius=6.0)
    IfEntityWithinDistance(1, 10000, 2421800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12424802():
    """ 12424802: Event 12424802 """
    EndIfFlagOn(12421800)
    DisableAI(2420800)
    DisableHealthBar(2420800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12424800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2420800, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(12424800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2420800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2420800)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2420800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2420800)
    Goto(Label.L4)
    Label(4)
    EnableAI(2420800)
    EnableBossHealthBar(2420800, name=251000, slot=0)
    CreatePlayLog(104)
    StartPlayLogMeasurement(2420010, 40, overwrite=True)


@NeverRestart
def Event12424803():
    """ 12424803: Event 12424803 """
    DisableNetworkSync()
    EndIfFlagOn(12421800)
    GotoIfThisEventOn(Label.L0)
    DisableMapSound(2423802)
    DisableMapSound(2423803)
    IfFlagOff(1, 12421800)
    IfFlagOn(1, 12424802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12424801)
    IfCharacterInsideRegion(1, PLAYER, region=2422802)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2423802, state=True)
    EnableFlag(12425246)
    IfHasTAEEvent(2, 2420800, tae_event_id=100)
    Label(0)
    IfFlagOff(2, 12421800)
    IfFlagOn(2, 12424802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12424801)
    IfCharacterInsideRegion(2, PLAYER, region=2422802)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2423802, state=False)
    EnableFlag(12425246)
    WaitFrames(0)
    SetBossMusicState(2423803, state=True)


@NeverRestart
def Event12424804():
    """ 12424804: Event 12424804 """
    DisableNetworkSync()
    EndIfFlagOn(12421800)
    IfHasTAEEvent(0, 2420800, tae_event_id=10)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=1)
    IfHasTAEEvent(0, 2420800, tae_event_id=20)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Restart()


@NeverRestart
def Event12424805():
    """ 12424805: Event 12424805 """
    DisableNetworkSync()
    EndIfFlagOn(12421800)
    IfFlagOn(0, 12421800)
    SetBossMusicState(2423802, state=False)
    SetBossMusicState(2423803, state=False)
    SetBossMusicState(-1, state=False)
    DisableFlag(12425246)


@RestartOnRest
def Event12424870(ARG_0_1: short, ARG_4_7: int, ARG_8_9: short, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12424870: Event 12424870 """
    CreateNPCPart(2420800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=ARG_12_15, damage_correction=1.0, body_damage_correction=2.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2420800, npc_part_id=ARG_4_7, material_special_effect_id=75, material_fx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, 2420800, npc_part_id=ARG_4_7, value=0)
    IfHealthLessThanOrEqual(3, 2420800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(2420800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=9999999, damage_correction=1.0, body_damage_correction=2.5, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2420800, npc_part_id=ARG_4_7, material_special_effect_id=75, material_fx_id=75)
    ResetAnimation(2420800, disable_interpolation=False)
    ForceAnimation(2420800, ARG_24_27)
    AddSpecialEffect(2420800, ARG_16_19, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, ARG_20_23)
    ReplanAI(2420800)
    IfHasTAEEvent(0, 2420800, tae_event_id=100)
    SetNPCPartHealth(2420800, npc_part_id=ARG_4_7, desired_hp=-1, overwrite_max=True)
    AddSpecialEffect(2420800, ARG_20_23, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, ARG_16_19)
    AICommand(2420800, command_id=-1, slot=0)
    ReplanAI(2420800)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12424871(ARG_0_1: short, ARG_4_7: int, ARG_8_9: short, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12424871: Event 12424871 """
    CreateNPCPart(2420800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=ARG_12_15, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2420800, npc_part_id=ARG_4_7, material_special_effect_id=74, material_fx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, 2420800, npc_part_id=ARG_4_7, value=0)
    IfHealthLessThanOrEqual(3, 2420800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(2420800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=9999999, damage_correction=1.0, body_damage_correction=1.25, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2420800, npc_part_id=ARG_4_7, material_special_effect_id=74, material_fx_id=74)
    ResetAnimation(2420800, disable_interpolation=False)
    ForceAnimation(2420800, ARG_24_27)
    AddSpecialEffect(2420800, ARG_16_19, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, ARG_20_23)
    ReplanAI(2420800)
    IfHasTAEEvent(0, 2420800, tae_event_id=100)
    SetNPCPartHealth(2420800, npc_part_id=ARG_4_7, desired_hp=-1, overwrite_max=True)
    AddSpecialEffect(2420800, ARG_20_23, affect_npc_part_hp=True)
    CancelSpecialEffect(2420800, ARG_16_19)
    AICommand(2420800, command_id=-1, slot=0)
    ReplanAI(2420800)
    WaitFrames(10)
    Restart()


@NeverRestart
def Event12424980():
    """ 12424980: Event 12424980 """
    WaitFrames(1)
    IfCharacterDead(1, 2420800)
    EndIfConditionTrue(1)
    IfFlagOn(2, 12424800)
    IfHealthLessThan(2, 2420800, 0.5)
    IfConditionTrue(0, input_condition=2)
    AICommand(2420800, command_id=100, slot=0)
    ReplanAI(2420800)
    IfHasTAEEvent(0, 2420800, tae_event_id=500)
    AICommand(2420800, command_id=-1, slot=0)
    ReplanAI(2420800)


@NeverRestart
def Event12424990():
    """ 12424990: Event 12424990 """
    IfCharacterHasSpecialEffect(1, 2420800, 5650)
    IfHealthValueLessThan(1, 2420800, 0)
    IfConditionTrue(0, input_condition=1)
    ShootProjectile(owner_entity=2420801, projectile_id=2420800, model_point=6, behavior_id=225100310, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    Wait(0.5)
    Restart()


@NeverRestart
def Event12421700():
    """ 12421700: Event 12421700 """
    GotoIfThisEventOff(Label.L0)
    DisableMapSound(2423812)
    DisableMapSound(2423813)
    DisableCharacter(2420810)
    Kill(2420810, award_souls=False)
    DisableCharacter(2420711)
    DisableCharacter(2420712)
    DisableCharacter(2420713)
    DisableCharacter(2420716)
    DisableCharacter(2420717)
    DisableCharacter(2420719)
    DisableCharacter(2420720)
    DisableCharacter(2420750)
    DisableCharacter(2420751)
    DisableAI(2420711)
    DisableAI(2420712)
    DisableAI(2420713)
    DisableAI(2420716)
    DisableAI(2420717)
    DisableAI(2420719)
    DisableAI(2420720)
    DisableObject(2421700)
    DisableObject(2421701)
    DeleteFX(2423810, erase_root_only=False)
    DeleteFX(2423811, erase_root_only=False)
    End()
    Label(0)
    IfCharacterDead(0, 2420811)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2421700)
    DisableObject(2421701)
    DeleteFX(2423810, erase_root_only=True)
    DeleteFX(2423811, erase_root_only=True)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    DisableCharacter(2420750)
    DisableCharacter(2420751)
    Wait(3.0)
    KillBoss(2420811)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(27)
    SkipLinesIfFlagOn(2, 6332)
    AwardItemLot(25700000, host_only=False)
    SkipLines(1)
    AwardItemLot(25700005, host_only=False)
    EnableFlag(2420)
    EnableFlag(9458)
    StartPlayLogMeasurement(2420000, 0, overwrite=False)
    StartPlayLogMeasurement(2420001, 18, overwrite=False)
    StartPlayLogMeasurement(2420010, 40, overwrite=False)
    CreatePlayLog(58)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 120, PlayLogMultiplayerType.HostOnly)
    End()
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@NeverRestart
def Event12421701():
    """ 12421701: Event 12421701 """
    DisableNetworkSync()
    EndIfFlagOn(12421800)
    IfFlagOn(1, 12421800)
    IfCharacterBackreadDisabled(2, 2420800)
    IfHealthLessThanOrEqual(2, 2420800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2422800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


@NeverRestart
def Event12421702():
    """ 12421702: Event 12421702 """
    EndIfFlagOn(12421700)
    EndIfThisEventOn()
    DisableCharacter(2420810)
    DisableCharacter(2420711)
    DisableCharacter(2420712)
    DisableCharacter(2420713)
    DisableCharacter(2420716)
    DisableCharacter(2420717)
    DisableCharacter(2420719)
    DisableCharacter(2420720)
    IfFlagOff(1, 12421700)
    IfThisEventSlotOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2422815)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12424700)
    EnableFlag(12421702)
    EnableCharacter(2420716)
    EnableAI(2420716)
    ForceAnimation(2420716, 6200)
    EnableCharacter(2420717)
    EnableAI(2420717)
    ForceAnimation(2420717, 6200)
    EnableCharacter(2420720)
    EnableAI(2420720)
    ForceAnimation(2420720, 6200)
    Wait(2.0)
    EnableCharacter(2420810)
    EnableAI(2420810)
    ForceAnimation(2420810, 6200)
    EnableCharacter(2420711)
    EnableAI(2420711)
    ForceAnimation(2420711, 6200)
    EnableCharacter(2420713)
    EnableAI(2420713)
    ForceAnimation(2420713, 6200)
    Wait(2.5)
    EnableCharacter(2420712)
    EnableAI(2420712)
    ForceAnimation(2420712, 6200)
    EnableCharacter(2420719)
    EnableAI(2420719)
    ForceAnimation(2420719, 6200)


@NeverRestart
def Event12421703():
    """ 12421703: Event 12421703 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12424700)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12424700)
    EnableFlag(12421702)
    EnableCharacter(2420716)
    EnableAI(2420716)
    ForceAnimation(2420716, 6200)
    EnableCharacter(2420717)
    EnableAI(2420717)
    ForceAnimation(2420717, 6200)
    EnableCharacter(2420720)
    EnableAI(2420720)
    ForceAnimation(2420720, 6200)
    Wait(2.0)
    EnableCharacter(2420810)
    EnableAI(2420810)
    ForceAnimation(2420810, 6200)
    EnableCharacter(2420711)
    EnableAI(2420711)
    ForceAnimation(2420711, 6200)
    EnableCharacter(2420713)
    EnableAI(2420713)
    ForceAnimation(2420713, 6200)
    Wait(2.5)
    EnableCharacter(2420712)
    EnableAI(2420712)
    ForceAnimation(2420712, 6200)
    EnableCharacter(2420719)
    EnableAI(2420719)
    ForceAnimation(2420719, 6200)


@NeverRestart
def Event12424710():
    """ 12424710: Event 12424710 """
    EndIfFlagOn(12421700)
    GotoIfFlagOn(Label.L0, 12421702)
    SkipLinesIfClient(2)
    DisableObject(2421700)
    DeleteFX(2423810, erase_root_only=False)
    DisableObject(2421701)
    DeleteFX(2423811, erase_root_only=False)
    IfFlagOff(1, 12421700)
    IfFlagOn(1, 12421702)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2421700)
    EnableObject(2421701)
    CreateFX(2423810)
    CreateFX(2423811)
    Label(0)
    IfFlagOff(1, 12421700)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=2420700, region=2421700)
    IfFlagOn(3, 12421700)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2422810, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2422811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12424700)
    Restart()


@NeverRestart
def Event12424711():
    """ 12424711: Event 12424711 """
    DisableNetworkSync()
    EndIfFlagOn(12421700)
    IfFlagOff(1, 12421700)
    IfFlagOn(1, 12424700)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=2420700, region=2421700)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2422810, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2422811)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12424701)
    Restart()


@NeverRestart
def Event12424712():
    """ 12424712: Event 12424712 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 2421700, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12424713():
    """ 12424713: Event 12424713 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 2421700, radius=4.0)
    IfEntityWithinDistance(1, 10000, 2421700, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12424702():
    """ 12424702: Event 12424702 """
    EndIfFlagOn(12421700)
    DisableAI(2420810)
    DisableAI(2420711)
    DisableAI(2420712)
    DisableAI(2420713)
    DisableAI(2420716)
    DisableAI(2420717)
    DisableAI(2420719)
    DisableAI(2420720)
    EnableImmortality(2420810)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12424700)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2800810, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2800811, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(12424700)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2800800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(2800803)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2800800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(2800803)
    Goto(Label.L4)
    Label(4)
    EnableBossHealthBar(2420810, name=257000, slot=0)
    CreatePlayLog(104)
    StartPlayLogMeasurement(2800010, 40, overwrite=True)
    EndIfFlagOff(12421702)
    IfCharacterInsideRegion(-1, PLAYER, region=2422817)
    IfDamageType(-1, attacked_entity=2420810, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420711, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420712, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420713, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420716, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420717, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420719, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=2420720, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2420810)
    EnableAI(2420711)
    EnableAI(2420712)
    EnableAI(2420713)
    EnableAI(2420716)
    EnableAI(2420717)
    EnableAI(2420719)
    EnableAI(2420720)


@NeverRestart
def Event12424703():
    """ 12424703: Event 12424703 """
    DisableNetworkSync()
    EndIfFlagOn(12421700)
    GotoIfThisEventOn(Label.L0)
    DisableMapSound(2703802)
    DisableMapSound(2703803)
    IfFlagOff(1, 12421700)
    IfFlagOn(1, 12424702)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12424701)
    IfCharacterInsideRegion(1, PLAYER, region=2422812)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2423812, state=True)
    EnableFlag(12425246)
    IfFlagOn(0, 12424790)
    Label(0)
    IfFlagOff(2, 12421700)
    IfFlagOn(2, 12424702)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12424701)
    IfCharacterInsideRegion(2, PLAYER, region=2422812)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2423812, state=False)
    EnableFlag(12425246)
    WaitFrames(0)
    SetBossMusicState(2423813, state=True)


@NeverRestart
def Event12424704():
    """ 12424704: Event 12424704 """
    DisableNetworkSync()
    IfHealthGreaterThan(1, 2420811, 0.0)
    IfHealthLessThanOrEqual(1, 2420811, 0.6000000238418579)
    IfEntityWithinDistance(1, 10000, 2420811, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=1)
    IfHealthGreaterThan(2, 2420811, 0.0)
    IfEntityBeyondDistance(2, 10000, 2420811, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=UPPER_CATHEDRAL_WARD, camera_slot=0)
    Restart()


@NeverRestart
def Event12424705():
    """ 12424705: Event 12424705 """
    DisableNetworkSync()
    EndIfFlagOn(12421700)
    IfFlagOn(0, 12421700)
    SetBossMusicState(2423812, state=False)
    SetBossMusicState(2423813, state=False)
    SetBossMusicState(-1, state=False)
    DisableFlag(12425246)


@RestartOnRest
def Event12424770(ARG_0_3: int, ARG_4_7: int):
    """ 12424770: Event 12424770 """
    IfCharacterDead(1, 2420811)
    IfCharacterAlive(2, ARG_0_3)
    IfCharacterDead(3, ARG_0_3)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableImmortality(ARG_4_7)
    DisableSpawner(ARG_0_3)
    Kill(ARG_4_7, award_souls=True)
    SkipLinesIfFinishedConditionTrue(1, 2)
    DisableCharacter(ARG_0_3)
    IfCharacterAlive(0, ARG_4_7)
    Restart()


@RestartOnRest
def Event12424780():
    """ 12424780: Event 12424780 """
    IfHasTAEEvent(0, 2420811, tae_event_id=40)
    AddSpecialEffect(2420711, 5530, affect_npc_part_hp=False)
    AddSpecialEffect(2420712, 5530, affect_npc_part_hp=False)
    AddSpecialEffect(2420713, 5530, affect_npc_part_hp=False)
    AddSpecialEffect(2420716, 5530, affect_npc_part_hp=False)
    AddSpecialEffect(2420717, 5530, affect_npc_part_hp=False)
    AddSpecialEffect(2420719, 5530, affect_npc_part_hp=False)
    AddSpecialEffect(2420720, 5530, affect_npc_part_hp=False)
    Restart()


@RestartOnRest
def Event12424785(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12424785: Event 12424785 """
    IfFlagOn(1, ARG_12_15)
    IfCharacterOutsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=ARG_4_7)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    Restart()


@RestartOnRest
def Event12424787(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12424787: Event 12424787 """
    IfFlagOn(1, ARG_12_15)
    IfHealthGreaterThan(1, ARG_16_19, 0.6000000238418579)
    IfCharacterOutsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=ARG_4_7)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    Restart()


@RestartOnRest
def Event12424784():
    """ 12424784: Event 12424784 """
    IfCharacterHasSpecialEffect(1, 2420811, 5609)
    IfCharacterOutsideRegion(1, 2420811, region=2422816)
    IfConditionTrue(0, input_condition=1)
    AICommand(2420811, command_id=20, slot=0)
    ReplanAI(2420811)
    IfCharacterInsideRegion(0, 2420811, region=2422722)
    AICommand(2420811, command_id=40, slot=0)
    ReplanAI(2420811)
    IfCharacterInsideRegion(0, PLAYER, region=2422816)
    WaitRandomFrames(min_frames=0, max_frames=60)
    AICommand(2420811, command_id=-1, slot=0)
    ReplanAI(2420811)
    Restart()


@RestartOnRest
def Event12424790():
    """ 12424790: Event 12424790 """
    IfCharacterBackreadEnabled(0, 2420811)
    DisableAI(2420811)
    DisableGravity(2420811)
    DisableHealthBar(2420811)
    ReferDamageToEntity(2420810, 2420811)
    DisableGravity(2420750)
    DisableGravity(2420751)
    IfHealthLessThan(1, 2420810, 0.6000000238418579)
    IfHealthGreaterThan(1, 2420811, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetNest(2420811, 2422721)
    AICommand(2420810, command_id=40, slot=1)
    ReplanAI(2420810)
    IfHasTAEEvent(0, 2420810, tae_event_id=30)
    DisableBossHealthBar(2420810, name=257000, slot=0)
    WaitFrames(5)
    DisableCharacter(2420810)
    Move(2420811, destination=2420810, destination_type=CoordEntityType.Character, model_point=203, copy_draw_Collision=2420810)
    EnableGravity(2420811)
    EnableAI(2420811)
    ForceAnimation(2420811, 3025, wait_for_completion=True)
    EnableBossHealthBar(2420811, name=257000, slot=0)


@RestartOnRest
def Event12424791():
    """ 12424791: Event 12424791 """
    IfHealthLessThanOrEqual(0, 2420811, 0.30000001192092896)
    SkipLinesIfThisEventOn(1)
    WaitFrames(135)
    Move(2420750, destination=2420811, destination_type=CoordEntityType.Character, model_point=40, copy_draw_Collision=2420811)
    Move(2420751, destination=2420811, destination_type=CoordEntityType.Character, model_point=41, copy_draw_Collision=2420811)
    Restart()


@RestartOnRest
def Event12424792(ARG_0_3: int):
    """ 12424792: Event 12424792 """
    IfHealthLessThanOrEqual(0, 2420811, 0.30000001192092896)
    SkipLinesIfThisEventSlotOn(2)
    WaitFrames(145)
    ForceAnimation(ARG_0_3, 3000)
    IfCharacterHasSpecialEffect(0, 2420811, 5402)
    ForceAnimation(ARG_0_3, 3000)
    Wait(3.5)
    DisableCharacter(ARG_0_3)
    IfCharacterHasSpecialEffect(0, 2420811, 5400)
    Wait(1.5)
    EnableCharacter(ARG_0_3)
    ForceAnimation(ARG_0_3, 3000)
    Restart()


@RestartOnRest
def Event12424795():
    """ 12424795: Event 12424795 """
    IfCharacterHasSpecialEffect(1, 2420811, 5531)
    IfDamageType(1, attacked_entity=2420811, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2420811, 3030)
    WaitFrames(59)
    ForceAnimation(2420811, 7000, loop=True, wait_for_completion=True, skip_transition=True)
    WaitFrames(150)
    ForceAnimation(2420811, 3000, loop=True, wait_for_completion=True, skip_transition=True)
    Restart()


@NeverRestart
def Event12420000(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12420000: Event 12420000 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, ARG_4_7)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_8_11)
    NotifyDoorEventSoundDampening(ARG_0_3, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_12_15)
    Wait(0.0)


@NeverRestart
def Event12420030(ARG_0_3: int):
    """ 12420030: Event 12420030 """
    DisableNetworkSync()
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    Wait(0.0)


@NeverRestart
def Event12420050(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12420050: Event 12420050 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_8_11)
    EnableTreasure(ARG_0_3)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@NeverRestart
def Event12420100():
    """ 12420100: Event 12420100 """
    SkipLinesIfThisEventOff(2)
    PostDestruction(2421850, slot=1)
    End()
    IfObjectDestroyed(0, 2421850)
    EnableFlag(12420100)


@NeverRestart
def Event12420123():
    """ 12420123: Event 12420123 """
    GotoIfThisEventOff(Label.L0)
    EndOfAnimation(2421200, 1)
    DisableObjectActivation(2421270, obj_act_id=2420000)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=12420122)
    ForceAnimation(2421200, 1)
    CreateObjectFX(920204, obj=2421200, model_point=200)
    CreateObjectFX(920205, obj=2421200, model_point=201)


@NeverRestart
def Event12420124():
    """ 12420124: Event 12420124 """
    DisableNetworkSync()
    EndIfFlagOn(12420123)
    IfActionButtonInRegion(1, action_button_id=2420030, region=2421200)
    IfActionButtonInRegion(2, action_button_id=2420000, region=2421200)
    IfObjectActivated(3, obj_act_id=12420122)
    IfFlagOn(4, 12420123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    EndIfFinishedConditionTrue(4)
    DisplayDialog(10010160, anchor_entity=2421200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()


@NeverRestart
def Event12420130(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12420130: Event 12420130 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, ARG_4_7)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_12_15)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_8_11)
    Wait(0.0)


@NeverRestart
def Event12420140():
    """ 12420140: Event 12420140 """
    DisableNetworkSync()
    IfFlagOn(1, 12420123)
    IfActionButtonInRegion(1, action_button_id=7100, region=2421270)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()


@NeverRestart
def Event12420150():
    """ 12420150: Event 12420150 """
    IfFlagOn(1, 12420154)
    IfFlagOff(2, 12420154)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(2421250, 0)
    DisableObjectActivation(2421251, obj_act_id=2420000)
    EnableObjectActivation(2421252, obj_act_id=2420000)
    SkipLines(3)
    EndOfAnimation(2421250, 8)
    EnableObjectActivation(2421251, obj_act_id=2420000)
    DisableObjectActivation(2421252, obj_act_id=2420000)


@NeverRestart
def Event12420151():
    """ 12420151: Event 12420151 """
    IfFlagOff(3, 12420154)
    IfFlagOn(3, 12420155)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOff(1, 12420154)
    IfFlagOff(1, 12420155)
    IfCharacterInsideRegion(1, PLAYER, region=2422651)
    IfFlagOff(2, 12420154)
    IfFlagOff(2, 12420155)
    IfObjectActivated(2, obj_act_id=12420124)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    EnableFlag(12420155)
    ForceAnimation(2421250, 1)
    ForceAnimation(2421250, 8)
    WaitFrames(250)
    IfAllPlayersOutsideRegion(0, region=2422652)
    DisableObjectActivation(2421252, obj_act_id=2420000)
    ForceAnimation(2421250, 9)
    WaitFrames(10)
    EnableFlag(12420154)
    DisableFlag(12420155)
    EnableObjectActivation(2421251, obj_act_id=2420000)
    Restart()


@NeverRestart
def Event12420152():
    """ 12420152: Event 12420152 """
    IfFlagOn(3, 12420154)
    IfFlagOn(3, 12420155)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOn(1, 12420154)
    IfFlagOff(1, 12420155)
    IfCharacterInsideRegion(1, PLAYER, region=2422652)
    IfFlagOn(2, 12420154)
    IfFlagOff(2, 12420155)
    IfObjectActivated(2, obj_act_id=12420123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    EnableFlag(12420155)
    ForceAnimation(2421250, 11)
    ForceAnimation(2421250, 12)
    WaitFrames(250)
    IfAllPlayersOutsideRegion(0, region=2422651)
    DisableObjectActivation(2421251, obj_act_id=2420000)
    ForceAnimation(2421250, 7)
    WaitFrames(10)
    DisableFlag(12420154)
    DisableFlag(12420155)
    EnableObjectActivation(2421252, obj_act_id=2420000)
    Restart()


@NeverRestart
def Event12420153():
    """ 12420153: Event 12420153 """
    DisableNetworkSync()
    IfFlagOff(-1, 12420154)
    IfFlagOn(-1, 12420155)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonInRegion(1, action_button_id=7100, region=2421251)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12420156():
    """ 12420156: Event 12420156 """
    DisableNetworkSync()
    IfFlagOn(-1, 12420154)
    IfFlagOn(-1, 12420155)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonInRegion(1, action_button_id=7100, region=2421252)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event12420280(ARG_0_3: int):
    """ 12420280: Event 12420280 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=ARG_0_3)
    AddSpecialEffect(PLAYER, 4150, affect_npc_part_hp=False)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event12420285(ARG_0_3: int, ARG_4_7: int):
    """ 12420285: Event 12420285 """
    IfFlagOn(0, ARG_4_7)
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=ARG_0_3)
    AddSpecialEffect(PLAYER, 4150, affect_npc_part_hp=False)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event12420300():
    """ 12420300: Event 12420300 """
    DisableNetworkSync()
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=2422681)
    PlaySoundEffect(anchor_entity=2422680, sound_type=SoundType.a_Ambient, sound_id=20011001)
    EnableFlag(12420301)


@RestartOnRest
def Event12420310():
    """ 12420310: Event 12420310 """
    SkipLinesIfThisEventSlotOff(5)
    EnableCharacter(2420205)
    DisableCharacter(2420204)
    Move(2420205, destination=2422205, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    PostDestruction(2421210, slot=1)
    End()
    DisableAI(2420205)
    DisableGravity(2420205)
    DisableCollision(2420205)
    DisableCharacter(2420205)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 52420170)
    IfCharacterInsideRegion(1, PLAYER, region=2422660)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=2421121, sound_type=SoundType.a_Ambient, sound_id=20011004)
    EnableCharacter(2420205)
    ForceAnimation(2420205, 7004)
    WaitFrames(10)
    DestroyObject(2421210, slot=1)
    EnableGravity(2420205)
    EnableCollision(2420205)
    EnableAI(2420205)


@RestartOnRest
def Event12420320():
    """ 12420320: Event 12420320 """
    GotoIfThisEventOff(Label.L0)
    DisableObject(2421300)
    Move(2420200, destination=2422200, destination_type=CoordEntityType.Region, model_point=-1, set_draw_Collision=2420203)
    Move(2420201, destination=2422201, destination_type=CoordEntityType.Region, model_point=-1, set_draw_Collision=2420203)
    Move(2420202, destination=2422202, destination_type=CoordEntityType.Region, model_point=-1, set_draw_Collision=2420203)
    SetNest(2420200, 2422200)
    SetNest(2420201, 2422201)
    SetNest(2420202, 2422202)
    PostDestruction(2421301, slot=1)
    End()
    Label(0)
    DisableObject(2421301)
    DisableCharacter(2420200)
    DisableAI(2420200)
    DisableGravity(2420200)
    DisableAI(2420201)
    DisableGravity(2420201)
    ForceAnimation(2420201, 7011, loop=True)
    DisableAI(2420202)
    DisableGravity(2420202)
    ForceAnimation(2420202, 7012, loop=True)
    CreateObjectFX(924500, obj=2421300, model_point=100)
    CreateObjectFX(924500, obj=2421300, model_point=101)
    CreateObjectFX(924500, obj=2421300, model_point=102)
    CreateObjectFX(924500, obj=2421300, model_point=103)
    CreateObjectFX(924500, obj=2421300, model_point=104)
    CreateObjectFX(924500, obj=2421300, model_point=105)
    CreateObjectFX(924500, obj=2421300, model_point=106)
    CreateObjectFX(924500, obj=2421300, model_point=107)
    CreateObjectFX(924500, obj=2421300, model_point=108)
    CreateObjectFX(924500, obj=2421300, model_point=109)
    CreateObjectFX(924500, obj=2421300, model_point=110)
    CreateObjectFX(924500, obj=2421300, model_point=111)
    CreateObjectFX(924500, obj=2421300, model_point=112)
    CreateObjectFX(924500, obj=2421300, model_point=113)
    CreateObjectFX(924500, obj=2421300, model_point=114)
    CreateObjectFX(924500, obj=2421300, model_point=115)
    CreateObjectFX(924500, obj=2421300, model_point=116)
    CreateObjectFX(924500, obj=2421300, model_point=117)
    CreateObjectFX(924500, obj=2421300, model_point=118)
    CreateObjectFX(924500, obj=2421300, model_point=119)
    CreateObjectFX(924500, obj=2421300, model_point=120)
    CreateObjectFX(924500, obj=2421300, model_point=121)
    CreateObjectFX(924500, obj=2421300, model_point=122)
    CreateObjectFX(924500, obj=2421300, model_point=123)
    CreateObjectFX(924500, obj=2421300, model_point=124)
    CreateObjectFX(924500, obj=2421300, model_point=125)
    CreateObjectFX(924500, obj=2421300, model_point=126)
    CreateObjectFX(924500, obj=2421300, model_point=127)
    CreateObjectFX(924500, obj=2421300, model_point=128)
    CreateObjectFX(924500, obj=2421300, model_point=129)
    CreateObjectFX(924500, obj=2421300, model_point=130)
    CreateObjectFX(924500, obj=2421300, model_point=131)
    CreateObjectFX(924500, obj=2421300, model_point=132)
    CreateObjectFX(924500, obj=2421300, model_point=133)
    CreateObjectFX(924500, obj=2421300, model_point=134)
    CreateObjectFX(924500, obj=2421300, model_point=135)
    CreateObjectFX(924500, obj=2421300, model_point=136)
    CreateObjectFX(924500, obj=2421300, model_point=137)
    CreateObjectFX(924500, obj=2421300, model_point=138)
    CreateObjectFX(924500, obj=2421300, model_point=139)
    CreateObjectFX(924501, obj=2421300, model_point=201)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=2422653)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2420200)
    ForceAnimation(2420200, 7007)
    ForceAnimation(2420201, 7008)
    ForceAnimation(2420202, 7009)
    ForceAnimation(2421300, 1)
    WaitFrames(81)
    DeleteObjectFX(2421300, erase_root=False)
    CreateObjectFX(924502, obj=2421300, model_point=201)
    WaitFrames(32)
    CreateObjectFX(924503, obj=2421300, model_point=201)
    DisableObject(2421300)
    EnableObject(2421301)
    DestroyObject(2421301, slot=1)
    EnableAI(2420200)
    EnableGravity(2420200)
    SetNest(2420200, 2422200)
    EnableAI(2420201)
    EnableGravity(2420201)
    SetNest(2420201, 2422201)
    EnableAI(2420202)
    EnableGravity(2420202)
    SetNest(2420202, 2422202)
    Wait(10.0)
    SetAIParamID(2420200, 100000)
    SetAIParamID(2420201, 100000)
    SetAIParamID(2420202, 100000)


@NeverRestart
def Event12420400():
    """ 12420400: Event 12420400 """
    GotoIfFlagOn(Label.L3, 9802)
    GotoIfFlagOn(Label.L2, 9801)
    GotoIfFlagOn(Label.L1, 9800)
    GotoIfFlagOff(Label.L0, 9800)
    Label(0)
    Label(1)
    Label(2)
    EnableMapPart(2424000)
    DisableMapPart(2424010)
    End()
    Label(3)
    DisableMapPart(2424000)
    EnableMapPart(2424010)


@NeverRestart
def Event12420500():
    """ 12420500: Event 12420500 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72500326)
    IfFlagOn(0, 72500326)
    DisableFlagRange((72500304, 72500309))
    EnableFlag(72500328)
    RemoveGoodFromPlayer(4305, quantity=1)
    PlayCutscene(24020000, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(10)
    DisableFlag(72500339)
    SaveRequest()
    Restart()


@RestartOnRest
def Event12420850(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: float, ARG_24_27: int, ARG_28_31: int):
    """ 12420850: Event 12420850 """
    DeleteFX(ARG_0_3, erase_root_only=False)
    DeleteFX(ARG_4_7, erase_root_only=False)
    DeleteFX(ARG_8_11, erase_root_only=False)
    SkipLinesIfFlagOff(3, ARG_12_15)
    CreateFX(ARG_4_7)
    CreateFX(ARG_8_11)
    End()
    IfObjectActivated(0, obj_act_id=ARG_16_19)
    Wait(ARG_20_23)
    CreateFX(ARG_0_3)
    CreateTemporaryFX(ARG_28_31, anchor_entity=ARG_24_27, anchor_type=CoordEntityType.Region, model_point=-1)
    Wait(4.0)
    CreateFX(ARG_4_7)
    CreateFX(ARG_8_11)


@RestartOnRest
def Event12420853():
    """ 12420853: Event 12420853 """
    DeleteFX(2427031, erase_root_only=False)
    DeleteFX(2427032, erase_root_only=False)
    DeleteFX(2427033, erase_root_only=False)
    SkipLinesIfFlagOff(3, 12420133)
    CreateFX(2427032)
    CreateFX(2427033)
    End()
    IfObjectActivated(0, obj_act_id=12420112)
    Wait(6.0)
    CreateFX(2427031)
    CreateTemporaryFX(920206, anchor_entity=2421204, anchor_type=CoordEntityType.Object, model_point=200)
    CreateTemporaryFX(920207, anchor_entity=2421204, anchor_type=CoordEntityType.Object, model_point=242)
    Wait(4.0)
    CreateFX(2427032)
    CreateFX(2427033)


@RestartOnRest
def Event12420854():
    """ 12420854: Event 12420854 """
    DeleteFX(2427023, erase_root_only=False)
    DeleteFX(2427024, erase_root_only=False)
    SkipLinesIfFlagOff(2, 12420310)
    CreateFX(2427024)
    End()
    IfFlagOn(0, 12420310)
    Wait(1.0)
    CreateFX(2427023)
    Wait(4.0)
    CreateFX(2427024)


@RestartOnRest
def Event12425200(ARG_0_3: int):
    """ 12425200: Event 12425200 """
    ForceAnimation(ARG_0_3, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfEntityWithinDistance(2, ARG_0_3, 10000, radius=2.0)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(3, PLAYER, region=2422661)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 3)
    ForceAnimation(ARG_0_3, 7001)
    ReplanAI(ARG_0_3)
    End()
    ForceAnimation(ARG_0_3, 7001)
    AICommand(ARG_0_3, command_id=10, slot=0)
    SetNest(ARG_0_3, 2422262)
    ReplanAI(ARG_0_3)
    IfAttacked(-3, ARG_0_3, attacking_character=10000)
    IfCharacterInsideRegion(-3, ARG_0_3, region=2422262)
    IfConditionTrue(0, input_condition=-3)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12425210(ARG_0_3: int):
    """ 12425210: Event 12425210 """
    EndIfThisEventSlotOn()
    ForceAnimation(ARG_0_3, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_0_3, 7001)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12425221(ARG_0_3: int):
    """ 12425221: Event 12425221 """
    IfCharacterInsideRegion(0, ARG_0_3, region=2422655)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=2423210)


@RestartOnRest
def Event12425250(ARG_0_3: int, ARG_4_7: float, ARG_8_11: int, ARG_12_15: float, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_28: uchar):
    """ 12425250: Event 12425250 """
    IfCharacterBackreadEnabled(0, ARG_0_3)
    Wait(1.0)
    SetNest(ARG_0_3, ARG_16_19)
    AICommand(ARG_0_3, command_id=20, slot=0)
    ReplanAI(ARG_0_3)
    Wait(ARG_4_7)
    AICommand(ARG_0_3, command_id=30, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-4, PLAYER, region=ARG_8_11)
    IfEntityWithinDistance(-4, 10000, ARG_0_3, radius=ARG_12_15)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(-1, input_condition=1)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_0_3, command_id=ARG_20_23, slot=0)
    ReplanAI(ARG_0_3)
    SkipLinesIfNotEqual(ARG_28_28, left=0, right=ARG_24_27)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-2)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12425225():
    """ 12425225: Event 12425225 """
    EndIfThisEventOn()
    ForceAnimation(2420253, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=2422253)
    IfEntityWithinDistance(-2, 2420253, 10000, radius=2.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfDamageType(-3, attacked_entity=2420253, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2420253, 7001)
    ReplanAI(2420253)


@RestartOnRest
def Event12425245():
    """ 12425245: Event 12425245 """
    DisableNetworkSync()
    DisableMapSound(2423600)
    IfInsideMap(1, game_map=UPPER_CATHEDRAL_WARD)
    IfFlagOff(1, 12425246)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(2423600)
    IfOutsideMap(-1, game_map=UPPER_CATHEDRAL_WARD)
    IfFlagOn(-1, 12425246)
    IfConditionTrue(0, input_condition=-1)
    DisableMapSound(2423600)
    Restart()


@RestartOnRest
def Event12425290():
    """ 12425290: Event 12425290 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountGreaterThanOrEqual(2, 10)
    EndIfConditionFalse(2)
    EnableFlag(12425291)


@RestartOnRest
def Event12425300(ARG_0_3: int):
    """ 12425300: Event 12425300 """
    IfFlagOn(-1, 12425291)
    IfFlagOn(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    SetDisplayMask(ARG_0_3, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(ARG_0_3, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(ARG_0_3, 5696, affect_npc_part_hp=False)


@RestartOnRest
def Event12425305(ARG_0_3: int):
    """ 12425305: Event 12425305 """
    IfFlagOn(-1, 12425291)
    IfFlagOn(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(ARG_0_3, 5552, affect_npc_part_hp=False)
    AddSpecialEffect(ARG_0_3, 5553, affect_npc_part_hp=False)
    AddSpecialEffect(ARG_0_3, 5554, affect_npc_part_hp=False)


@RestartOnRest
def Event12425310(ARG_0_3: int):
    """ 12425310: Event 12425310 """
    EndIfThisEventSlotOn()
    ForceAnimation(ARG_0_3, 7018, loop=True)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)
    ForceAnimation(ARG_0_3, 7019)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12425320(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12425320: Event 12425320 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, ARG_0_3)
    Wait(1.0)
    SetNest(ARG_0_3, ARG_12_15)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_12_15)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Normal)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)
    ForceAnimation(ARG_0_3, ARG_4_7, wait_for_completion=True)
    ForceAnimation(ARG_0_3, ARG_8_11, loop=True)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Battle)
    ForceAnimation(ARG_0_3, 0)
    Restart()


@RestartOnRest
def Event12425350(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12425350: Event 12425350 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, ARG_0_3)
    SetAIParamID(ARG_0_3, ARG_4_7)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    SetAIParamID(ARG_0_3, ARG_8_11)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12425500(ARG_0_3: int, ARG_4_7: float, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float):
    """ 12425500: Event 12425500 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, ARG_0_3)
    Wait(ARG_16_19)
    DisableAI(ARG_0_3)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=ARG_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    SkipLinesIfNotEqual(3, left=1, right=ARG_8_11)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_12_15)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(ARG_0_3)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12425600():
    """ 12425600: Event 12425600 """
    EndIfThisEventOn()
    IfCharacterBackreadEnabled(1, 2420401)
    IfCharacterBackreadEnabled(1, 2420402)
    IfConditionTrue(0, input_condition=1)
    DisableAI(2420401)
    DisableAI(2420402)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfEntityWithinDistance(-3, 10000, 2420401, radius=5.0)
    IfEntityWithinDistance(-3, 10000, 2420402, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=2422685)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfAttacked(-1, 2420401, attacking_character=10000)
    IfAttacked(-1, 2420402, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2420401)
    ReplanAI(2420401)
    Wait(3.0)
    EnableAI(2420402)
    ReplanAI(2420402)


@NeverRestart
def Event12425601():
    """ 12425601: Event 12425601 """
    DisableNetworkSync()
    IfCharacterAlive(1, 2420402)
    IfCharacterBackreadEnabled(1, 2420402)
    IfConditionTrue(0, input_condition=1)
    Move(2420731, destination=2420402, destination_type=CoordEntityType.Character, model_point=40, short_move=True)
    Restart()


@RestartOnRest
def Event12425602():
    """ 12425602: Event 12425602 """
    IfHealthLessThanOrEqual(0, 2420402, 0.0)
    Wait(1.0)
    ForceAnimation(2420731, 2200, wait_for_completion=True)
    DisableCharacter(2420731)


@NeverRestart
def Event12425603():
    """ 12425603: Event 12425603 """
    AddSpecialEffect(2420402, 5609, affect_npc_part_hp=False)
    DisableGravity(2420731)


@RestartOnRest
def Event12425400(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12425400: Event 12425400 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(ARG_0_3, ARG_8_11)


@NeverRestart
def Event12420990():
    """ 12420990: Event 12420990 """
    EndIfThisEventOn()
    EndIfClient()
    IfStandingOnCollision(0, 2423500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 154, PlayLogMultiplayerType.HostOnly)
    AwardAchievement(11)


@RestartOnRest
def Event12424450(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12424450: Event 12424450 """
    EndIfThisEventSlotOn()
    EndIfClient()
    SetEventPoint(ARG_0_3, region=ARG_4_7, reaction_range=1.0)
    IfFlagOn(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOn(1, ARG_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=990, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12424400(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12424400: Event 12424400 """
    GotoIfFlagOn(Label.L0, ARG_0_3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOff(1, ARG_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(-1, ARG_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    EnableFlag(ARG_0_3)
    CreateFX(ARG_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_8_11)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(-3, ARG_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12424410(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 12424410: Event 12424410 """
    SkipLinesIfFlagOn(1, ARG_12_15)
    DisableCharacter(ARG_4_7)
    SkipLinesIfFlagOn(3, ARG_16_19)
    IfClient(1)
    IfFlagOn(1, ARG_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(ARG_4_7)
    EndIfFlagOn(ARG_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(ARG_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfFlagOn(2, ARG_20_23)
    IfFlagOff(2, ARG_24_27)
    IfActionButtonInRegion(2, action_button_id=ARG_28_31, region=ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(ARG_0_3, ARG_4_7, ARG_8_11, summon_flag=ARG_12_15, dismissal_flag=ARG_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event12424460(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12424460: Event 12424460 """
    EndIfClient()
    IfFlagOn(1, ARG_20_23)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    RotateToFaceEntity(ARG_0_3, ARG_8_11, animation=ARG_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, ARG_0_3, region=ARG_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(ARG_0_3, region=ARG_8_11, reaction_range=1.0)
    AICommand(ARG_0_3, command_id=990, slot=0)
    ReplanAI(ARG_0_3)
    DisableGravity(ARG_0_3)
    DisableCollision(ARG_0_3)
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_24_27)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
