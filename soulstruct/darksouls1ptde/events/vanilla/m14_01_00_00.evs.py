"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    SkipLinesIfFlagDisabled(1, 10)
    RegisterBonfire(bonfire_flag=11410920, obj=1411950)
    RegisterBonfire(bonfire_flag=11410992, obj=1411960)
    RegisterBonfire(bonfire_flag=11410984, obj=1411961)
    SkipLinesIfFlagDisabled(1, 11410900)
    RegisterBonfire(bonfire_flag=11410976, obj=1411962)
    RegisterBonfire(bonfire_flag=11410968, obj=1411963)
    RegisterBonfire(bonfire_flag=11410960, obj=1411964)
    SkipLinesIfClient(14)
    DisableObject(1411994)
    DeleteVFX(vfx_id=1411995, erase_root_only=False)
    DisableObject(1411996)
    DeleteVFX(vfx_id=1411997, erase_root_only=False)
    DisableObject(1411998)
    DeleteVFX(vfx_id=1411999, erase_root_only=False)
    DisableObject(1411988)
    DeleteVFX(vfx_id=1411989, erase_root_only=False)
    DisableObject(1411986)
    DeleteVFX(vfx_id=1411987, erase_root_only=False)
    DisableObject(1411984)
    DeleteVFX(vfx_id=1411985, erase_root_only=False)
    DisableObject(1411982)
    DeleteVFX(vfx_id=1411983, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, 11410291)
    DisableObject(1411121)
    DeleteVFX(vfx_id=1413400)
    DeleteVFX(vfx_id=1413410)
    SkipLinesIfFlagDisabled(3, 11410292)
    DisableObject(1411122)
    DeleteVFX(vfx_id=1413401)
    DeleteVFX(vfx_id=1413411)
    Event_11410095()
    Event_11415090()
    Event_11415091()
    Event_11415092()
    Event_11410800()
    Event_11410400()
    Event_11410340()
    Event_11410341()
    Event_11410350()
    Event_11410360()
    Event_11415399()
    Event_11410260()
    Event_11410200()
    Event_11410201(0, 1411210, 462000000)
    Event_11410201(1, 1411211, 462100000)
    Event_11410201(2, 1411212, 462200000)
    Event_11410201(3, 1411213, 462300000)
    Event_11410201(4, 1411214, 462400000)
    Event_11410201(5, 1411215, 462500000)
    Event_11410201(6, 1411216, 462600000)
    Event_11410201(7, 1411217, 462700000)
    Event_11410201(8, 1411218, 462800000)
    Event_11410201(9, 1411219, 462900000)
    Event_11410201(10, 1411220, 463000000)
    Event_11410201(11, 1411221, 463100000)
    Event_11410201(12, 1411222, 463200000)
    Event_11410250()
    DisableSoundEvent(sound_id=1413801)
    SkipLinesIfFlagDisabled(4, 11410900)
    Event_11415372()
    DisableObject(1411790)
    DeleteVFX(vfx_id=1411791, erase_root_only=False)
    SkipLines(10)
    Event_11415370()
    Event_11415371()
    Event_11415373()
    Event_11415372()
    Event_11415374()
    Event_11415376()
    Event_11415377()
    Event_11415378()
    Event_11415379()
    Event_11410900()
    Event_11415310(0, 11415376)
    Event_11415310(1, 11415310)
    Event_11415310(2, 11415311)
    Event_11415310(3, 11415312)
    Event_11415310(4, 11415313)
    DisableSoundEvent(sound_id=1413803)
    SkipLinesIfFlagDisabled(6, 11410410)
    Event_11415342()
    DisableObject(1411410)
    DeleteVFX(vfx_id=1411411, erase_root_only=False)
    DisableObject(1411412)
    DeleteVFX(vfx_id=1411413, erase_root_only=False)
    SkipLines(7)
    Event_11415340()
    Event_11415341()
    Event_11415343()
    Event_11415342()
    Event_11415344()
    Event_11410410()
    Event_11415345()
    DisableSoundEvent(sound_id=1413802)
    SkipLinesIfFlagDisabled(6, 11410901)
    Event_11415382()
    DisableObject(1411890)
    DeleteVFX(vfx_id=1411891, erase_root_only=False)
    DisableObject(1411892)
    DeleteVFX(vfx_id=1411893, erase_root_only=False)
    SkipLines(7)
    Event_11415380()
    Event_11415381()
    Event_11415383()
    Event_11415382()
    Event_11415384()
    Event_11410901()
    Event_11415386()
    DisableSoundEvent(sound_id=1413800)
    SkipLinesIfFlagDisabled(4, 10)
    Event_11415392()
    DisableObject(1411990)
    DeleteVFX(vfx_id=1411991, erase_root_only=False)
    SkipLines(11)
    Event_11415390()
    Event_11415391()
    Event_11415393()
    Event_11415392()
    Event_11410001()
    Event_11415394()
    Event_11415395()
    Event_11415396()
    Event_11415397()
    Event_11415398()
    Event_11415300()
    Event_800(0, 1410100)
    Event_11410100(4, 1410307)
    Event_11410100(6, 6620)
    Event_11410100(7, 1410110)
    Event_11410100(8, 1410150)
    Event_11410100(9, 1410350)
    Event_11410100(10, 1410351)
    Event_11410100(11, 1410352)
    Event_11410100(12, 1410353)
    Event_11410100(13, 1410354)
    Event_11410100(14, 1410355)
    Event_11410100(15, 1410356)
    Event_11410100(16, 1410357)
    Event_11410100(17, 1410358)
    Event_11410100(18, 1410359)
    Event_11410100(19, 1410360)
    Event_11410100(20, 1410361)
    Event_11410100(21, 1410362)
    Event_11410100(22, 1410363)
    Event_11410100(23, 1410364)
    Event_11410100(24, 1410365)
    Event_11410100(25, 1410366)
    Event_11410100(26, 1410367)
    Event_11410100(27, 1410368)
    Event_11410100(28, 1410369)
    Event_11410100(29, 1410370)
    Event_11410100(30, 1410371)
    Event_11410100(31, 1410372)
    Event_11410100(32, 1410373)
    Event_11410100(33, 1410374)
    Event_11410100(34, 1410375)
    Event_11410100(35, 1410376)
    Event_11410100(36, 1410377)
    Event_11410100(37, 1410378)
    Event_11410100(38, 1410450)
    Event_11410100(39, 1410451)
    Event_11410100(40, 1410452)
    Event_11410100(41, 1410453)
    Event_11410100(42, 1410454)
    Event_11410100(43, 1410455)
    Event_11410100(44, 1410456)
    Event_11415210(0, 11415250, 11415263, 11)
    Event_11415250(0, 1410200, 1410220, 1410221, 1410222, 1410223, 1410224)
    Event_11415250(1, 1410201, 1410225, 1410226, 1410227, 1410228, 1410229)
    Event_11415250(2, 1410202, 1410230, 1410231, 1410232, 1410233, 1410234)
    Event_11415250(3, 1410203, 1410235, 1410236, 1410237, 1410238, 1410239)
    Event_11415250(4, 1410204, 1410240, 1410241, 1410242, 1410243, 1410244)
    Event_11415250(5, 1410205, 1410245, 1410246, 1410247, 1410248, 1410249)
    Event_11415250(6, 1410206, 1410250, 1410251, 1410252, 1410253, 1410254)
    Event_11415250(7, 1410207, 1410255, 1410256, 1410257, 1410258, 1410259)
    Event_11415250(8, 1410208, 1410260, 1410261, 1410262, 1410263, 1410264)
    Event_11415250(9, 1410209, 1410265, 1410266, 1410267, 1410268, 1410269)
    Event_11415250(10, 1410210, 1410270, 1410271, 1410272, 1410273, 1410274)
    Event_11415250(11, 1410211, 1410275, 1410276, 1410277, 1410278, 1410279)
    Event_11415250(12, 1410212, 1410280, 1410281, 1410282, 1410283, 1410284)
    Event_11415250(13, 1410213, 1410285, 1410286, 1410287, 1410288, 1410289)
    Event_11415100(0, 1410301, 1410301, 9060, 15.0, 0.0)
    Event_11415100(1, 1410302, 1410302, 9060, 10.0, 0.0)
    Event_11415100(2, 1410307, 1410307, 9060, 15.0, 0.0)
    Event_11415120(0, 10000, 1410303, 9060, 1412302, 0.30000001192092896)
    Event_11415120(1, 10000, 1410304, 9060, 1412302, 0.10000000149011612)
    Event_11415120(2, 10000, 1410305, 9060, 1412302, 0.0)
    Event_11415120(3, 10000, 1410306, 9060, 1412302, 0.20000000298023224)
    Event_11410150(1, 1410301, 33900000)
    Event_11410150(2, 1410302, 33900000)
    Event_11410150(3, 1410303, 33900000)
    Event_11410150(4, 1410304, 33900000)
    Event_11410150(5, 1410305, 33900000)
    Event_11410150(6, 1410306, 33900000)
    Event_11410600(0, 1411650, 11410600)
    Event_11410600(1, 1411651, 11410601)
    Event_11410600(2, 1411652, 11410602)
    Event_11410600(3, 1411653, 11410603)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_11410100(0, 1410410)
    Event_11410100(1, 1410411)
    Event_11410100(2, 1410412)
    Event_11410100(3, 1410413)
    HumanityRegistration(6620, event_flag=8250)
    HumanityRegistration(6542, event_flag=8310)
    HumanityRegistration(6560, event_flag=8956)
    HumanityRegistration(6561, event_flag=8956)
    Event_11415030()
    Event_11415032()
    Event_11415035()
    Event_11415038()
    Event_11410810(0, 6560, 11415036, 11415037)
    Event_11410810(1, 6561, 11415039, 11415040)
    HumanityRegistration(6002, event_flag=8310)
    HumanityRegistration(6004, event_flag=8310)
    SkipLinesIfFlagEnabled(3, 1009)
    SkipLinesIfFlagEnabled(2, 1004)
    SkipLinesIfFlagEnabled(1, 1003)
    DisableCharacter(6002)
    SkipLinesIfFlagEnabled(1, 11410580)
    SkipLines(1)
    Move(6002, destination=1412500, destination_type=CoordEntityType.Region, set_draw_parent=1413000)
    SkipLinesIfFlagEnabled(1, 1002)
    DisableCharacter(6004)
    SetTeamTypeAndExitStandbyAnimation(6004, team_type=TeamType.HostileAlly)
    Event_11410510(0, 6002, 1004)
    Event_11410520(0, 6002, 1000, 1029, 1005)
    Event_11410530(0, 6002, 1000, 1029, 1009)
    Event_11410531(0, 6002, 1000, 1029, 1002)
    Event_11410532(0, 6002, 1000, 1029, 1003)
    Event_11410533(0, 6006, 1000, 1029, 1012)
    Event_11410534(0, 6004, 1000, 1029, 1011)
    HumanityRegistration(6286, event_flag=8446)
    SkipLinesIfFlagRangeAnyEnabled(1, (1503, 1507))
    DisableCharacter(6286)
    SkipLinesIfFlagEnabled(3, 1504)
    SkipLinesIfFlagEnabled(2, 1506)
    SkipLinesIfFlagEnabled(1, 1507)
    SkipLines(2)
    AddSpecialEffect(6286, 90111)
    Move(6286, destination=1412360, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11410593)
    SetStandbyAnimationSettings(6286, standby_animation=7855)
    Event_11410501(0, 6286, 1512)
    Event_11410546(0, 6286, 1490, 1514, 1513)
    Event_11410540(0, 6286, 1490, 1514, 1503)
    Event_11410541(0, 6286, 1490, 1514, 1504)
    Event_11410542(0, 6286, 1490, 1514, 1505)
    Event_11410543(0, 6286, 1490, 1514, 1506)
    Event_11410544(0, 6286, 1490, 1514, 1507)
    Event_11410545(0, 6286, 1490, 1514, 1513)
    Event_11410549(0, 6286)
    Event_11410550(0, 6286, 1490, 1514, 1514)
    Event_11410547(0, 6286)
    Event_11410548(0, 6286)


@NeverRestart(11410090)
def Event_11410090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7)


@RestartOnRest(11415090)
def Event_11415090():
    """Event 11415090"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1410900)
    DisableCharacter(1410901)
    DisableCharacter(1410902)
    DisableCharacter(1410903)
    DisableCharacter(1410904)
    DisableCharacter(1410905)
    DisableCharacter(1410906)
    DisableCharacter(1410907)
    IfFlagEnabled(0, 11410050)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1410900)
    EnableCharacter(1410901)
    EnableCharacter(1410902)
    EnableCharacter(1410903)
    EnableCharacter(1410904)
    EnableCharacter(1410905)
    EnableCharacter(1410906)
    EnableCharacter(1410907)


@RestartOnRest(11415091)
def Event_11415091():
    """Event 11415091"""
    IfFlagEnabled(-1, 11415095)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11410050)
    DisableFlag(11415095)
    EnableFlag(5001)
    Kill(1410900)
    Kill(1410901)
    Kill(1410902)
    Kill(1410903)
    Kill(1410904)
    Kill(1410905)
    Kill(1410906)
    Kill(1410907)


@RestartOnRest(11415092)
def Event_11415092():
    """Event 11415092"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11410050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=LOST_IZALITH)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11410050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=LOST_IZALITH)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11410050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=LOST_IZALITH)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11410050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=LOST_IZALITH)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11410050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=LOST_IZALITH)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11410050)
    RestartIfConditionFalse(-6)
    EnableFlag(11410050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=LOST_IZALITH)
    RestartIfConditionFalse(7)
    DisableFlag(11410050)
    EnableFlag(11415095)


@NeverRestart(11410095)
def Event_11410095():
    """Event 11410095"""
    SkipLinesIfFlagDisabled(5, 11800100)
    EnableFlag(11410096)
    DisableObject(1411710)
    DeleteVFX(vfx_id=1411711, erase_root_only=False)
    DisableFlag(402)
    End()
    SkipLinesIfFlagDisabled(3, 11410096)
    DisableObject(1411710)
    DeleteVFX(vfx_id=1411711, erase_root_only=False)
    End()
    EndIfClient()
    IfActionButton(
        0,
        prompt_text=10010410,
        anchor_entity=1412660,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=1411710,
    )
    DisplayStatus(10010630)
    Restart()


@NeverRestart(11415390)
def Event_11415390():
    """Event 11415390"""
    IfFlagDisabled(1, 10)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1411990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415391)
def Event_11415391():
    """Event 11415391"""
    DisableNetworkSync()
    IfFlagDisabled(1, 10)
    IfFlagEnabled(1, 11415393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415393)
def Event_11415393():
    """Event 11415393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 10)
    IfCharacterInsideRegion(1, PLAYER, region=1412996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1410800)


@RestartOnRest(11415392)
def Event_11415392():
    """Event 11415392"""
    SkipLinesIfFlagDisabled(7, 10)
    DisableCharacter(1410800)
    DisableCharacter(1410801)
    DisableCharacter(1410802)
    Kill(1410800)
    Kill(1410801)
    Kill(1410802)
    End()
    SkipLinesIfFlagRangeAnyEnabled(1, (11410291, 11410292))
    DisableCharacter(1410800)
    SkipLinesIfFlagRangeAllDisabled(1, (11410291, 11410292))
    SetStandbyAnimationSettings(1410801)
    EnableInvincibility(1410800)
    EnableInvincibility(1410801)
    DisableHealthBar(1410800)
    DisableHealthBar(1410801)
    DisableAI(1410801)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=1)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagRangeAnyEnabled(2, (11410291, 11410292))
    SetStandbyAnimationSettings(1410801)
    ForceAnimation(1410801, 9060)
    EnableAI(1410801)
    EnableBossHealthBar(1410802, name=5400)


@NeverRestart(11410001)
def Event_11410001():
    """Event 11410001"""
    DisableObject(1411950)
    IfCharacterDead(0, 1410802)
    EnableFlag(10)
    KillBoss(game_area_param_id=1410800)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=36)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=0)
    DisableObject(1411990)
    DeleteVFX(vfx_id=1411991)
    DisableNetworkSync()
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1411950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1411950)
    RegisterBonfire(bonfire_flag=11410920, obj=1411950)


@NeverRestart(11415394)
def Event_11415394():
    """Event 11415394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 10)
    IfFlagEnabled(1, 11415392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11415391)
    IfCharacterInsideRegion(1, PLAYER, region=1412990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1413800)


@NeverRestart(11415395)
def Event_11415395():
    """Event 11415395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 10)
    IfFlagEnabled(1, 11415394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1413800)


@RestartOnRest(11415396)
def Event_11415396():
    """Event 11415396"""
    SkipLinesIfFlagRangeAnyEnabled(15, (11410291, 11410292))
    IfFlagEnabled(-1, 11410291)
    IfFlagEnabled(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagEnabled(6, 11410292)
    EnableFlag(11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140116, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140116, cutscene_flags=2, player_id=10000)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140115, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140115, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1410800)
    IfFlagEnabled(1, 11410291)
    IfFlagEnabled(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(1410800, 5130)
    SkipLinesIfFlagEnabled(12, 11410000)
    SkipLinesIfFlagDisabled(5, 11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140117, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140117, cutscene_flags=2, player_id=10000)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140118, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140118, cutscene_flags=2, player_id=10000)
    SetStandbyAnimationSettings(1410800, standby_animation=10000)
    WaitFrames(frames=1)
    EnableFlag(11410000)
    SetStandbyAnimationSettings(1410800)
    WaitFrames(frames=1)
    ResetAnimation(1410800, disable_interpolation=True)


@RestartOnRest(11415397)
def Event_11415397():
    """Event 11415397"""
    EnableInvincibility(1410802)
    IfFlagEnabled(1, 11410291)
    IfFlagEnabled(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableInvincibility(1410802)
    IfHealthLessThanOrEqual(0, 1410802, value=0.0)
    DisableInvincibility(1410800)
    DisableInvincibility(1410801)
    Kill(1410800, award_souls=True)
    Kill(1410801)


@RestartOnRest(11415398)
def Event_11415398():
    """Event 11415398"""
    IfFlagEnabled(-1, 11410291)
    IfFlagEnabled(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterBackreadEnabled(0, 1410800)
    AICommand(1410800, command_id=2, slot=0)
    ReplanAI(1410800)
    AICommand(1410801, command_id=2, slot=0)
    ReplanAI(1410801)
    IfFlagEnabled(1, 11410291)
    IfFlagEnabled(1, 11410292)
    SkipLinesIfFlagEnabled(1, 11410000)
    IfFlagEnabled(1, 11415396)
    IfConditionTrue(0, input_condition=1)
    IfCharacterBackreadEnabled(0, 1410800)
    AICommand(1410800, command_id=3, slot=0)
    ReplanAI(1410800)
    AICommand(1410801, command_id=3, slot=0)
    ReplanAI(1410801)


@NeverRestart(11415399)
def Event_11415399():
    """Event 11415399"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1412110)
    EnableInvincibility(PLAYER)
    IfCharacterOutsideRegion(0, PLAYER, region=1412110)
    Wait(3.0)
    DisableInvincibility(PLAYER)


@NeverRestart(11415300)
def Event_11415300():
    """Event 11415300"""
    EndIfFlagEnabled(10)
    SkipLinesIfThisEventFlagEnabled(2)
    EnableFlag(11415300)
    EnableObjectInvulnerability(1411120)
    IfFlagDisabled(1, 11410291)
    IfObjectDestroyed(1, 1411121)
    IfFlagDisabled(2, 11410292)
    IfObjectDestroyed(2, 1411122)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfFlagEnabled(-1, 10)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(10)
    SkipLinesIfFinishedConditionFalse(4, condition=1)
    EnableFlag(11410291)
    DeleteVFX(vfx_id=1413400)
    DeleteVFX(vfx_id=1413410)
    Restart()
    EnableFlag(11410292)
    DeleteVFX(vfx_id=1413401)
    DeleteVFX(vfx_id=1413411)
    Restart()


@NeverRestart(11410200)
def Event_11410200():
    """Event 11410200"""
    SkipLinesIfThisEventFlagDisabled(6)
    DisableObject(1411200)
    DisableObject(1411201)
    DisableObject(1411202)
    DisableObject(1411203)
    DisableObject(1411204)
    End()
    RestoreObject(1411200)
    RestoreObject(1411201)
    RestoreObject(1411202)
    RestoreObject(1411203)
    RestoreObject(1411204)
    EnableObjectInvulnerability(1411200)
    EnableObjectInvulnerability(1411201)
    EnableObjectInvulnerability(1411202)
    EnableObjectInvulnerability(1411203)
    EnableObjectInvulnerability(1411204)
    IfFlagEnabled(1, 11410291)
    IfFlagEnabled(1, 11410292)
    IfCharacterInsideRegion(1, PLAYER, region=1412100)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11410200)
    DisableObjectInvulnerability(1411200)
    DisableObjectInvulnerability(1411201)
    DisableObjectInvulnerability(1411202)
    DisableObjectInvulnerability(1411203)
    DisableObjectInvulnerability(1411204)
    CreateTemporaryVFX(vfx_id=140009, anchor_entity=1411202, anchor_type=CoordEntityType.Object)
    DestroyObject(1411200)
    PlaySoundEffect(1411200, 463300000, sound_type=SoundType.o_Object)
    WaitFrames(frames=4)
    DestroyObject(1411201)
    PlaySoundEffect(1411201, 463400000, sound_type=SoundType.o_Object)
    WaitFrames(frames=3)
    DestroyObject(1411202)
    PlaySoundEffect(1411202, 463500000, sound_type=SoundType.o_Object)
    WaitFrames(frames=2)
    DestroyObject(1411203)
    PlaySoundEffect(1411203, 463600000, sound_type=SoundType.o_Object)
    WaitFrames(frames=1)
    DestroyObject(1411204)
    PlaySoundEffect(1411204, 463700000, sound_type=SoundType.o_Object)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(1411200)
    DisableObject(1411203)
    DisableObject(1411204)


@NeverRestart(11410201)
def Event_11410201(_, arg_0_3: int, arg_4_7: int):
    """Event 11410201"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableObject(arg_0_3)
    End()
    RestoreObject(arg_0_3)
    EnableObjectInvulnerability(arg_0_3)
    IfFlagEnabled(-1, 11410291)
    IfFlagEnabled(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfEntityWithinDistance(0, entity=arg_0_3, other_entity=PLAYER, radius=8.0)
    DisableObjectInvulnerability(arg_0_3)
    DestroyObject(arg_0_3)
    CreateTemporaryVFX(vfx_id=140008, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(arg_0_3, arg_4_7, sound_type=SoundType.o_Object)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(arg_0_3)


@NeverRestart(11410250)
def Event_11410250():
    """Event 11410250"""
    EndIfFlagRangeAllEnabled(flag_range=(11410291, 11410292))
    EnableObjectInvulnerability(1411250)
    EnableObjectInvulnerability(1411251)
    EnableObjectInvulnerability(1411252)
    EnableObjectInvulnerability(1411253)
    EnableObjectInvulnerability(1411254)
    EnableObjectInvulnerability(1411255)
    EnableObjectInvulnerability(1411256)
    EnableObjectInvulnerability(1411257)
    EnableObjectInvulnerability(1411258)
    EnableObjectInvulnerability(1411259)
    EnableObjectInvulnerability(1411260)
    EnableObjectInvulnerability(1411261)
    EnableObjectInvulnerability(1411262)
    EnableObjectInvulnerability(1411263)
    EnableObjectInvulnerability(1411264)
    EnableObjectInvulnerability(1411265)
    EnableObjectInvulnerability(1411266)
    EnableObjectInvulnerability(1411267)
    EnableObjectInvulnerability(1411268)
    EnableObjectInvulnerability(1411269)
    EnableObjectInvulnerability(1411270)
    EnableObjectInvulnerability(1411271)
    EnableObjectInvulnerability(1411272)
    EnableObjectInvulnerability(1411273)
    EnableObjectInvulnerability(1411274)
    EnableObjectInvulnerability(1411275)
    EnableObjectInvulnerability(1411276)
    EnableObjectInvulnerability(1411277)
    EnableObjectInvulnerability(1411278)
    EnableObjectInvulnerability(1411279)
    EnableObjectInvulnerability(1411280)
    EnableObjectInvulnerability(1411281)
    EnableObjectInvulnerability(1411282)
    EnableObjectInvulnerability(1411283)
    EnableObjectInvulnerability(1411284)
    EnableObjectInvulnerability(1411285)
    EnableObjectInvulnerability(1411286)
    EnableObjectInvulnerability(1411287)
    EnableObjectInvulnerability(1411288)
    EnableObjectInvulnerability(1411289)
    EnableObjectInvulnerability(1411290)
    EnableObjectInvulnerability(1411291)
    EnableObjectInvulnerability(1411292)
    EnableObjectInvulnerability(1411293)
    EnableObjectInvulnerability(1411294)
    EnableObjectInvulnerability(1411295)
    EnableObjectInvulnerability(1411296)
    EnableObjectInvulnerability(1411297)
    IfFlagEnabled(1, 11410291)
    IfFlagEnabled(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableObjectInvulnerability(1411250)
    DisableObjectInvulnerability(1411251)
    DisableObjectInvulnerability(1411252)
    DisableObjectInvulnerability(1411253)
    DisableObjectInvulnerability(1411254)
    DisableObjectInvulnerability(1411255)
    DisableObjectInvulnerability(1411256)
    DisableObjectInvulnerability(1411257)
    DisableObjectInvulnerability(1411258)
    DisableObjectInvulnerability(1411259)
    DisableObjectInvulnerability(1411260)
    DisableObjectInvulnerability(1411261)
    DisableObjectInvulnerability(1411262)
    DisableObjectInvulnerability(1411263)
    DisableObjectInvulnerability(1411264)
    DisableObjectInvulnerability(1411265)
    DisableObjectInvulnerability(1411266)
    DisableObjectInvulnerability(1411267)
    DisableObjectInvulnerability(1411268)
    DisableObjectInvulnerability(1411269)
    DisableObjectInvulnerability(1411270)
    DisableObjectInvulnerability(1411271)
    DisableObjectInvulnerability(1411272)
    DisableObjectInvulnerability(1411273)
    DisableObjectInvulnerability(1411274)
    DisableObjectInvulnerability(1411275)
    DisableObjectInvulnerability(1411276)
    DisableObjectInvulnerability(1411277)
    DisableObjectInvulnerability(1411278)
    DisableObjectInvulnerability(1411279)
    DisableObjectInvulnerability(1411280)
    DisableObjectInvulnerability(1411281)
    DisableObjectInvulnerability(1411282)
    DisableObjectInvulnerability(1411283)
    DisableObjectInvulnerability(1411284)
    DisableObjectInvulnerability(1411285)
    DisableObjectInvulnerability(1411286)
    DisableObjectInvulnerability(1411287)
    DisableObjectInvulnerability(1411288)
    DisableObjectInvulnerability(1411289)
    DisableObjectInvulnerability(1411290)
    DisableObjectInvulnerability(1411291)
    DisableObjectInvulnerability(1411292)
    DisableObjectInvulnerability(1411293)
    DisableObjectInvulnerability(1411294)
    DisableObjectInvulnerability(1411295)
    DisableObjectInvulnerability(1411296)
    DisableObjectInvulnerability(1411297)


@NeverRestart(11415370)
def Event_11415370():
    """Event 11415370"""
    IfFlagDisabled(1, 11410900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412698,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1411790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412697)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415371)
def Event_11415371():
    """Event 11415371"""
    IfFlagDisabled(1, 11410900)
    IfFlagEnabled(1, 11415373)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412698,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412697)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415373)
def Event_11415373():
    """Event 11415373"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11410900)
    IfCharacterInsideRegion(1, PLAYER, region=1412696)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1410600, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1410600)
    SetNetworkUpdateRate(1410600, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableInvincibility(1410600)


@RestartOnRest(11415372)
def Event_11415372():
    """Event 11415372"""
    SkipLinesIfFlagDisabled(3, 11410900)
    DisableBackread(1410600)
    Kill(1410600)
    End()
    DisableAI(1410600)
    DisableHealthBar(1410600)
    EnableInvincibility(1410600)
    IfFlagEnabled(1, 11415373)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, 51410180)
    IfFlagEnabled(2, 11415373)
    IfAttacked(2, attacked_entity=1410600, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1410600)
    EnableBossHealthBar(1410600, name=5250)


@NeverRestart(11410900)
def Event_11410900():
    """Event 11410900"""
    DisableObject(1411962)
    IfCharacterDead(0, 1410600)
    EnableFlag(11410900)
    KillBoss(game_area_param_id=1410600)
    DisableBackread(1410600)
    EnableFlag(11410800)
    DisableObject(1411790)
    DeleteVFX(vfx_id=1411791)
    EnableObject(1411962)
    RegisterBonfire(bonfire_flag=11410976, obj=1411962)
    EndIfFlagEnabled(11800100)
    EnableFlag(402)


@NeverRestart(11415374)
def Event_11415374():
    """Event 11415374"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11410900)
    IfFlagEnabled(1, 11415372)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11415371)
    IfCharacterInsideRegion(1, PLAYER, region=1412690)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1413801)
    IfFlagEnabled(0, 11410900)
    DisableSoundEvent(sound_id=1413801)


@RestartOnRest(11415376)
def Event_11415376():
    """Event 11415376"""
    IfCharacterAlive(1, 1410600)
    IfCharacterInsideRegion(1, 1410600, region=1412799)
    IfConditionTrue(0, input_condition=1)
    Move(1410600, destination=1412797, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1410600, 17006, wait_for_completion=True)
    Move(1410600, destination=1412798, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(11415377)
def Event_11415377():
    """Event 11415377"""
    SkipLinesIfThisEventFlagDisabled(4)
    CancelSpecialEffect(1410600, 5132)
    AddSpecialEffect(1410600, 5133)
    AICommand(1410600, command_id=-1, slot=1)
    End()
    IfCharacterHasTAEEvent(0, 1410600, tae_event_id=300)
    CancelSpecialEffect(1410600, 5132)
    AddSpecialEffect(1410600, 5133)
    AICommand(1410600, command_id=-1, slot=1)
    ReplanAI(1410600)


@RestartOnRest(11415378)
def Event_11415378():
    """Event 11415378"""
    SkipLinesIfFlagEnabled(4, 0)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, 51410180)
    IfCharacterInsideRegion(1, PLAYER, region=1412796)
    IfConditionTrue(0, input_condition=1)
    AICommand(1410600, command_id=1, slot=1)
    ReplanAI(1410600)


@RestartOnRest(11415379)
def Event_11415379():
    """Event 11415379"""
    EndIfFlagEnabled(11410900)
    IfFlagRangeAllEnabled(1, flag_range=(11415310, 11415314))
    IfHealthLessThanOrEqual(2, 1410600, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    Kill(1410600, award_souls=True)


@RestartOnRest(11415310)
def Event_11415310(_, arg_0_3: int):
    """Event 11415310"""
    IfFlagEnabled(1, 11415376)
    IfFlagEnabled(1, arg_0_3)
    IfAttacked(1, attacked_entity=1410600, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    End()


@NeverRestart(11410800)
def Event_11410800():
    """Event 11410800"""
    SkipLinesIfFlagDisabled(5, 11410801)
    DisableObject(1411100)
    DisableMapCollision(collision=1413100)
    DisableSoundEvent(sound_id=1413805)
    EnableTreasure(obj=1411610)
    End()
    DisableObject(1411610)
    DisableTreasure(obj=1411610)
    DisableMapCollision(collision=1413101)
    DisableCharacter(1410450)
    DisableCharacter(1410451)
    DisableCharacter(1410452)
    DisableCharacter(1410453)
    DisableCharacter(1410454)
    DisableCharacter(1410455)
    DisableCharacter(1410456)
    DisableNetworkSync()
    IfThisEventFlagEnabled(0)
    Wait(5.0)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, value=0.0)
    EndIfConditionTrue(1)
    EndIfClient()
    IfCharacterInsideRegion(0, PLAYER, region=1412530)
    PlayCutscene(140100, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11410801)
    DisableObject(1411100)
    DisableSoundEvent(sound_id=1413805)
    DisableMapCollision(collision=1413100)
    EnableMapCollision(collision=1413101)
    EnableObject(1411610)
    EnableTreasure(obj=1411610)
    EnableCharacter(1410450)
    EnableCharacter(1410451)
    EnableCharacter(1410452)
    EnableCharacter(1410453)
    EnableCharacter(1410454)
    EnableCharacter(1410455)
    EnableCharacter(1410456)


@NeverRestart(11415380)
def Event_11415380():
    """Event 11415380"""
    IfFlagDisabled(1, 11410901)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1411890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415381)
def Event_11415381():
    """Event 11415381"""
    IfFlagDisabled(1, 11410901)
    IfFlagEnabled(1, 11415383)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415383)
def Event_11415383():
    """Event 11415383"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11410901)
    IfCharacterInsideRegion(1, PLAYER, region=1412896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1410700)


@RestartOnRest(11415382)
def Event_11415382():
    """Event 11415382"""
    DisableObject(1411110)
    Event_11415385()
    SkipLinesIfFlagDisabled(2, 11410901)
    DisableBackread(1410700)
    End()
    SkipLinesIfFlagEnabled(2, 11410002)
    EnableObject(1411110)
    DisableCharacter(1410700)
    DisableAI(1410700)
    IfFlagEnabled(1, 11415383)
    IfCharacterInsideRegion(1, PLAYER, region=1412896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(8, 11410002)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140120, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140120, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1410700)
    DisableObject(1411110)
    EnableFlag(11410002)
    EnableAI(1410700)
    EnableBossHealthBar(1410700, name=5200)


@NeverRestart(11410901)
def Event_11410901():
    """Event 11410901"""
    IfCharacterDead(0, 1410700)
    EnableFlag(11410901)
    KillBoss(game_area_param_id=1410700)
    EnableFlag(11410901)
    DisableObject(1411890)
    DeleteVFX(vfx_id=1411891)
    DisableObject(1411892)
    DeleteVFX(vfx_id=1411893)
    DisableNetworkSync()
    Wait(10.0)
    DisableCharacter(1410700)
    DisableBackread(1410700)


@NeverRestart(11415384)
def Event_11415384():
    """Event 11415384"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11410901)
    IfFlagEnabled(1, 11410002)
    IfFlagEnabled(1, 11415382)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11415381)
    IfCharacterInsideRegion(1, PLAYER, region=1412890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1413802)
    IfFlagEnabled(0, 11410901)
    DisableSoundEvent(sound_id=1413802)


@UnknownRestart(11415385)
def Event_11415385():
    """Event 11415385"""
    DisableCharacter(1410710)
    DisableCharacter(1410711)
    DisableCharacter(1410712)
    DisableCharacter(1410713)
    DisableCharacter(1410714)
    DisableCharacter(1410720)
    DisableCharacter(1410721)
    DisableCharacter(1410722)
    DisableCharacter(1410723)
    DisableCharacter(1410724)
    EndIfFlagEnabled(11410901)
    Event_11415350(0, 11415380, 5200, 5200, 125, 1410710)
    Event_11415350(1, 11415350, 5201, 5201, 125, 1410711)
    Event_11415350(2, 11415351, 5202, 5202, 125, 1410712)
    Event_11415350(3, 11415352, 5203, 5203, 125, 1410713)
    Event_11415350(4, 11415353, 5204, 5204, 125, 1410714)
    Event_11415360(0, 11415380, 5205, 5205, 95, 1410720)
    Event_11415360(1, 11415360, 5206, 5206, 95, 1410721)
    Event_11415360(2, 11415361, 5207, 5207, 95, 1410722)
    Event_11415360(3, 11415362, 5208, 5208, 95, 1410723)
    Event_11415360(4, 11415363, 5209, 5209, 95, 1410724)
    Event_11415320(0, 11415380, 1410710)
    Event_11415320(1, 11415350, 1410711)
    Event_11415320(2, 11415351, 1410712)
    Event_11415320(3, 11415352, 1410713)
    Event_11415320(4, 11415353, 1410714)
    Event_11415320(5, 11415380, 1410720)
    Event_11415320(6, 11415360, 1410721)
    Event_11415320(7, 11415361, 1410722)
    Event_11415320(8, 11415362, 1410723)
    Event_11415320(9, 11415363, 1410724)


@NeverRestart(11415386)
def Event_11415386():
    """Event 11415386"""
    EndIfClient()
    IfCharacterDead(-1, 1410700)
    IfCharacterDead(-1, 1410710)
    IfCharacterDead(-1, 1410711)
    IfCharacterDead(-1, 1410712)
    IfCharacterDead(-1, 1410713)
    IfCharacterDead(-1, 1410714)
    IfCharacterDead(-1, 1410720)
    IfCharacterDead(-1, 1410721)
    IfCharacterDead(-1, 1410722)
    IfCharacterDead(-1, 1410723)
    IfCharacterDead(-1, 1410724)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(2670, host_only=True)


@UnknownRestart(11415320)
def Event_11415320(_, arg_0_3: int, arg_4_7: int):
    """Event 11415320"""
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHasTAEEvent(1, 1410700, tae_event_id=400)
    IfHealthGreaterThan(1, 1410700, value=0.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthLessThanOrEqual(0, 1410700, value=0.0)
    Kill(arg_4_7, award_souls=True)


@UnknownRestart(11415350)
def Event_11415350(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11415350"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    EnableCharacter(arg_16_19)
    SkipLinesIfFlagDisabled(4, 11415354)
    SetDisplayMask(1410700, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1410700, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1410700, command_id=20, slot=0)
    End()
    IfFlagEnabled(0, arg_0_3)
    CreateNPCPart(1410700, npc_part_id=arg_4_5, part_index=NPCPartType.Part1, part_health=arg_12_15)
    IfCharacterPartHealthComparison(1, 1410700, npc_part_id=arg_8_11, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(2, 1410700, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EzstateAIRequest(1410700, command_id=1001, slot=0)
    IfCharacterHasTAEEvent(0, 1410700, tae_event_id=400)
    EnableCharacter(arg_16_19)
    Move(
        arg_16_19,
        destination=1410700,
        destination_type=CoordEntityType.Character,
        model_point=140,
        copy_draw_parent=1410700,
    )
    ForceAnimation(arg_16_19, 8100)
    SetDisplayMask(1410700, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1410700, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1410700, command_id=10, slot=0)
    SkipLinesIfFlagDisabled(2, 11415353)
    AICommand(1410700, command_id=20, slot=0)
    End()
    IfCharacterHasTAEEvent(0, 1410700, tae_event_id=300)
    SetDisplayMask(1410700, bit_index=0, switch_type=OnOffChange.Off)
    SetCollisionMask(1410700, bit_index=1, switch_type=OnOffChange.On)
    AICommand(1410700, command_id=-1, slot=0)


@UnknownRestart(11415360)
def Event_11415360(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11415360"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    EnableCharacter(arg_16_19)
    SkipLinesIfFlagDisabled(4, 11415364)
    SetDisplayMask(1410700, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1410700, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(1410700, command_id=20, slot=1)
    End()
    IfFlagEnabled(0, arg_0_3)
    CreateNPCPart(1410700, npc_part_id=arg_4_5, part_index=NPCPartType.Part2, part_health=arg_12_15)
    IfCharacterPartHealthComparison(1, 1410700, npc_part_id=arg_8_11, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(2, 1410700, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EzstateAIRequest(1410700, command_id=1002, slot=0)
    IfCharacterHasTAEEvent(0, 1410700, tae_event_id=400)
    EnableCharacter(arg_16_19)
    Move(
        arg_16_19,
        destination=1410700,
        destination_type=CoordEntityType.Character,
        model_point=141,
        copy_draw_parent=1410700,
    )
    ForceAnimation(arg_16_19, 8100)
    SetDisplayMask(1410700, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1410700, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(1410700, command_id=10, slot=1)
    SkipLinesIfFlagDisabled(2, 11415363)
    AICommand(1410700, command_id=20, slot=1)
    End()
    IfCharacterHasTAEEvent(0, 1410700, tae_event_id=600)
    SetDisplayMask(1410700, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(1410700, bit_index=2, switch_type=OnOffChange.On)
    AICommand(1410700, command_id=-1, slot=1)


@NeverRestart(11410340)
def Event_11410340():
    """Event 11410340"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1411340, animation_id=1)
    End()
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    IfFlagEnabled(1, 11400598)
    IfActionButton(
        1,
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411340,
    )
    IfActionButton(
        2,
        prompt_text=10010510,
        anchor_entity=1412200,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411340,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11410340)
    RotateToFaceEntity(PLAYER, target_entity=1411340)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    ForceAnimation(1411340, 1)
    CreateTemporaryVFX(vfx_id=140000, anchor_entity=1411340, anchor_type=CoordEntityType.Object)


@NeverRestart(11410341)
def Event_11410341():
    """Event 11410341"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11410340)
    IfHost(6)
    IfPlayerCovenant(7, Covenant.ChaosServant)
    IfConditionFalse(6, input_condition=7)
    IfConditionTrue(-7, input_condition=6)
    IfFlagDisabled(-7, 11400598)
    IfConditionTrue(1, input_condition=-7)
    IfActionButton(
        -2,
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411340,
    )
    IfConditionTrue(1, input_condition=-2)
    IfFlagDisabled(2, 11410340)
    IfClient(2)
    IfActionButton(
        -3,
        prompt_text=10010510,
        anchor_entity=1412200,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411340,
    )
    IfActionButton(
        -3,
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411340,
    )
    IfConditionTrue(2, input_condition=-3)
    IfFlagEnabled(3, 11410340)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(11410340)
    DisplayDialog(text=10010160, anchor_entity=1411340, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11410360)
def Event_11410360():
    """Event 11410360"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1411360)
    End()
    IfObjectDestroyed(0, 1411360)
    EnableFlag(11410360)


@NeverRestart(11410400)
def Event_11410400():
    """Event 11410400"""
    SkipLinesIfFlagDisabled(1, 11410401)
    EndOfAnimation(obj=1411400, animation_id=0)
    IfFlagEnabled(0, 11410410)
    IfFlagEnabled(1, 11410401)
    IfCharacterInsideRegion(1, PLAYER, region=1412403)
    IfFlagDisabled(2, 11410401)
    IfCharacterInsideRegion(2, PLAYER, region=1412402)
    IfFlagDisabled(3, 11410401)
    IfCharacterInsideRegion(3, PLAYER, region=1412401)
    IfFlagEnabled(4, 11410401)
    IfCharacterInsideRegion(4, PLAYER, region=1412400)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=3)
    SkipLinesIfFinishedConditionTrue(8, condition=4)
    SkipLinesIfFlagEnabled(7, 11410401)
    EnableFlag(11410401)
    CreateObjectVFX(vfx_id=1411400, obj=100, model_point=140002)
    ForceAnimation(1411400, 3, wait_for_completion=True)
    DeleteObjectVFX(1411400)
    IfAllPlayersOutsideRegion(0, region=1412403)
    ForceAnimation(1411400, 4, wait_for_completion=True)
    Restart()
    DisableFlag(11410401)
    CreateObjectVFX(vfx_id=1411400, obj=100, model_point=140002)
    ForceAnimation(1411400, 1, wait_for_completion=True)
    DeleteObjectVFX(1411400)
    IfAllPlayersOutsideRegion(0, region=1412402)
    ForceAnimation(1411400, 5, wait_for_completion=True)
    Restart()


@NeverRestart(11410402)
def Event_11410402():
    """Event 11410402"""
    DisableNetworkSync()
    IfFlagDisabled(-2, 11410410)
    IfMultiplayer(-2)
    IfConditionTrue(1, input_condition=-2)
    IfActionButton(
        1,
        prompt_text=10010510,
        anchor_entity=1411400,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010170, anchor_entity=1411400, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11415340)
def Event_11415340():
    """Event 11415340"""
    IfFlagDisabled(1, 11410410)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412411,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1411410,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412412)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415341)
def Event_11415341():
    """Event 11415341"""
    IfFlagDisabled(1, 11410410)
    IfFlagEnabled(1, 11415343)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412411,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411410,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1412412)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11415343)
def Event_11415343():
    """Event 11415343"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11410410)
    IfCharacterInsideRegion(1, PLAYER, region=1412416)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1410400)


@RestartOnRest(11415342)
def Event_11415342():
    """Event 11415342"""
    SkipLinesIfFlagDisabled(7, 11410410)
    DisableObject(1411410)
    DeleteVFX(vfx_id=1411411, erase_root_only=False)
    DisableObject(1411412)
    DeleteVFX(vfx_id=1411413, erase_root_only=False)
    DisableCharacter(1410400)
    DisableBackread(1410400)
    End()
    DisableAI(1410400)
    IfFlagEnabled(1, 11415343)
    IfCharacterInsideRegion(1, PLAYER, region=1412416)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1410400)
    EnableBossHealthBar(1410400, name=2230)


@NeverRestart(11415344)
def Event_11415344():
    """Event 11415344"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11410410)
    IfFlagEnabled(1, 11415342)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11415341)
    IfCharacterInsideRegion(1, PLAYER, region=1412410)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1413803)
    IfFlagEnabled(0, 11410410)
    DisableSoundEvent(sound_id=1413803)


@NeverRestart(11415345)
def Event_11415345():
    """Event 11415345"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11415340)
    IfCharacterInsideRegion(1, PLAYER, region=1412410)
    IfCharacterBackreadEnabled(-1, 1400700)
    IfCharacterBackreadEnabled(-1, 6160)
    IfCharacterBackreadEnabled(-1, 1400411)
    IfCharacterBackreadEnabled(-1, 1400412)
    IfCharacterBackreadEnabled(-1, 1400413)
    IfCharacterBackreadEnabled(-1, 1400414)
    IfCharacterBackreadEnabled(-1, 1400415)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableBackread(1400700)
    DisableBackread(6160)
    DisableBackread(1400411)
    DisableBackread(1400412)
    DisableBackread(1400413)
    DisableBackread(1400414)
    DisableBackread(1400415)
    IfFlagEnabled(0, 11410410)
    Wait(5.0)
    EnableBackread(1400700)
    EnableBackread(6160)
    EnableBackread(1400411)
    EnableBackread(1400412)
    EnableBackread(1400413)
    EnableBackread(1400414)
    EnableBackread(1400415)


@NeverRestart(11410410)
def Event_11410410():
    """Event 11410410"""
    IfCharacterDead(0, 1410400)
    EnableFlag(11410410)
    KillBoss(game_area_param_id=1410400)
    EnableFlag(11410410)
    DisableObject(1411410)
    DeleteVFX(vfx_id=1411411)
    DisableObject(1411412)
    DeleteVFX(vfx_id=1411413)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(1410400)
    DisableBackread(1410400)


@RestartOnRest(11415100)
def Event_11415100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: float):
    """Event 11415100"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)
    End()
    IfEntityWithinDistance(0, entity=arg_0_3, other_entity=PLAYER, radius=arg_12_15)
    Wait(arg_16_19)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)


@RestartOnRest(11415120)
def Event_11415120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """Event 11415120"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)
    End()
    IfCharacterInsideRegion(0, arg_0_3, region=arg_12_15)
    Wait(arg_16_19)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)


@RestartOnRest(11415200)
def Event_11415200():
    """Event 11415200"""
    Event_11415201(0, 1410500, 1, 3290, 3290, 11415201)
    Event_5200(-1, 1410500, 11415201, 0, 1)
    Event_5200(-1, 1410500, 11415201, 2, 3)
    Event_5201(-1, 1410500, 11415201, 1411500, 1411501, 120, 123)
    Event_5201(-1, 1410500, 11415201, 1411502, 1411503, 126, 129)
    Event_5202(-1, 1410500, 11415201, 1410550, 1410551, 120, 123)
    Event_5202(-1, 1410500, 11415201, 1410552, 1410553, 126, 129)
    Event_11415201(1, 1410500, 2, 3291, 3291, 11415202)
    Event_5200(-1, 1410500, 11415202, 5, 11)
    Event_5201(-1, 1410500, 11415202, 1411504, 1411505, 135, 137)
    Event_5202(-1, 1410500, 11415202, 1410554, 1410555, 135, 137)
    Event_5202(-1, 1410500, 11415202, 1410556, 1410557, 153, 155)
    Event_11415201(2, 1410500, 3, 3292, 3292, 11415203)
    Event_5200(-1, 1410500, 11415203, 6, 7)
    Event_5200(-1, 1410500, 11415203, 8, 10)
    Event_5201(-1, 1410500, 11415203, 1411506, 1411507, 138, 141)
    Event_5201(-1, 1410500, 11415203, 1411508, 1411509, 144, 150)
    Event_5202(-1, 1410500, 11415203, 1410558, 1410559, 138, 141)
    Event_5202(-1, 1410500, 11415203, 1410560, 1410561, 144, 150)
    Event_11415201(3, 1410500, 4, 3293, 3293, 11415204)
    Event_5200(-1, 1410500, 11415204, 4, 9)
    Event_5201(-1, 1410500, 11415204, 1411510, 1411511, 132, 134)
    Event_5202(-1, 1410500, 11415204, 1410562, 1410563, 132, 134)
    Event_5202(-1, 1410500, 11415204, 1410564, 1410565, 150, 152)


@UnknownRestart(11415201)
def Event_11415201(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int):
    """Event 11415201"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(arg_0_3, npc_part_id=arg_6_7, part_index=arg_4_5, part_health=100)
    IfCharacterPartHealthComparison(0, arg_0_3, npc_part_id=arg_8_11, comparison_type=ComparisonType.Equal, value=5)
    DisableFlag(11415290)
    DisableFlag(11415291)
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11415290, 11415291))
    EnableFlag(arg_12_15)
    SkipLinesIfFlagDisabled(2, 11415290)
    ForceAnimation(arg_0_3, 8000)
    SkipLines(1)
    ForceAnimation(arg_0_3, 8010)


@UnknownRestart(5200)
def Event_5200(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """Event 5200"""
    SkipLinesIfFlagEnabled(6, arg_4_7)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SetDisplayMask(arg_0_3, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_9_9, switch_type=OnOffChange.On)


@UnknownRestart(5201)
def Event_5201(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_17: short, arg_18_19: short):
    """Event 5201"""
    DisableObject(arg_8_11)
    DisableObject(arg_12_15)
    EndIfFlagEnabled(arg_4_7)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_8_11, character=arg_0_3, model_point=arg_16_17)
    MoveObjectToCharacter(arg_12_15, character=arg_0_3, model_point=arg_18_19)
    DestroyObject(arg_8_11)
    DestroyObject(arg_12_15)


@UnknownRestart(5202)
def Event_5202(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 5202"""
    EndIfFlagEnabled(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(arg_0_3)
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_16_19,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_20_23,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)


@RestartOnRest(11415210)
def Event_11415210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11415210"""
    IfTrueFlagCountGreaterThanOrEqual(0, FlagType.Absolute, flag_range=(arg_0_3, arg_4_7), value=arg_8_11)
    DisableSoundEvent(sound_id=1413806)


@RestartOnRest(11415250)
def Event_11415250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11415250"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    End()
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    IfCharacterDead(0, arg_0_3)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    EnableCharacter(arg_4_7)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    EnableCharacter(arg_16_19)
    EnableCharacter(arg_20_23)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_16_19,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_20_23,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=arg_0_3,
    )
    ForceAnimation(arg_4_7, 7000)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    ForceAnimation(arg_16_19, 7000)
    ForceAnimation(arg_20_23, 7000)


@NeverRestart(11410350)
def Event_11410350():
    """Event 11410350"""
    SkipLinesIfThisEventFlagDisabled(5)
    DisableObject(1411350)
    PostDestruction(1411351)
    EndOfAnimation(obj=1411600, animation_id=116)
    EnableTreasure(obj=1411600)
    End()
    DisableObject(1411351)
    DisableTreasure(obj=1411600)
    CreateObjectVFX(vfx_id=1411600, obj=90, model_point=99010)
    ForceAnimation(1411600, 115, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=1412350)
    IfObjectDestroyed(-1, 1411350)
    IfConditionTrue(0, input_condition=-1)
    DisableObject(1411350)
    EnableObject(1411351)
    CreateTemporaryVFX(vfx_id=140001, anchor_entity=1411351, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(1411351, 481000001, sound_type=SoundType.o_Object)
    DestroyObject(1411351)
    ForceAnimation(1411600, 116, wait_for_completion=True)
    EnableTreasure(obj=1411600)
    DeleteObjectVFX(1411600)


@RestartOnRest(11410100)
def Event_11410100(_, arg_0_3: int):
    """Event 11410100"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=1410110)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33002000, host_only=True)


@RestartOnRest(11410150)
def Event_11410150(_, arg_0_3: int, arg_4_7: int):
    """Event 11410150"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    EndIfConditionFalse(-1)
    AwardItemLot(arg_4_7, host_only=True)


@RestartOnRest(800)
def Event_800(_, arg_0_3: int):
    """Event 800"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@NeverRestart(11410600)
def Event_11410600(_, arg_0_3: int, arg_4_7: int):
    """Event 11410600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11410260)
def Event_11410260():
    """Event 11410260"""
    DisableNetworkSync()
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfTimeElapsed(1, seconds=3.0)
    IfConditionTrue(0, input_condition=1)
    ActivateKillplaneForModel(game_map=LOST_IZALITH, y_threshold=-400.0, target_model_id=3240)
    Restart()


@NeverRestart(11410510)
def Event_11410510(_, arg_0_3: int, arg_4_7: int):
    """Event 11410510"""
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, arg_4_7)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11410520)
def Event_11410520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11410501)
def Event_11410501(_, arg_0_3: int, arg_4_7: int):
    """Event 11410501"""
    IfFlagEnabled(-2, 1503)
    IfFlagEnabled(-2, 1505)
    IfFlagEnabled(-2, 1506)
    IfFlagEnabled(-2, 1507)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, arg_4_7)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11410530)
def Event_11410530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410530"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1007)
    IfFlagEnabled(1, 11410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11410531)
def Event_11410531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410531"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1009)
    IfFlagDisabled(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    EnableCharacter(6004)
    SetTeamTypeAndExitStandbyAnimation(6004, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11410532)
def Event_11410532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410532"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1009)
    IfFlagEnabled(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1412500, destination_type=CoordEntityType.Region, set_draw_parent=1413000)
    EnableFlag(11410580)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetNest(arg_0_3, region=1412500)


@NeverRestart(11410533)
def Event_11410533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410533"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1003)
    IfFlagEnabled(1, 11410595)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventFlagDisabled(1)
    IfHost(2)
    IfFlagDisabled(2, 1004)
    IfFlagEnabled(2, arg_12_15)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11410534)
def Event_11410534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410534"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1002)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11410540)
def Event_11410540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410540"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1502)
    IfFlagEnabled(1, 11400590)
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(814)


@NeverRestart(11410541)
def Event_11410541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410541"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1503)
    IfCharacterAlive(-1, 1410410)
    IfCharacterAlive(-1, 1410411)
    IfCharacterAlive(-1, 1410412)
    IfCharacterAlive(-1, 1410413)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 11410590)
    IfFlagDisabled(2, 1512)
    IfFlagEnabled(2, 1504)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetStandbyAnimationSettings(arg_0_3)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.FightingAlly)
    AddSpecialEffect(arg_0_3, 90111)


@NeverRestart(11410542)
def Event_11410542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410542"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1503)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11410543)
def Event_11410543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410543"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1504)
    IfHealthLessThan(1, arg_0_3, value=0.5)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, region=1412360)


@NeverRestart(11410544)
def Event_11410544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410544"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1504)
    IfHealthGreaterThanOrEqual(1, arg_0_3, value=0.5)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, region=1412360)


@NeverRestart(11410545)
def Event_11410545(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410545"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1506)
    IfFlagEnabled(1, 11410591)
    IfThisEventFlagDisabled(1)
    IfFlagDisabled(2, 1512)
    IfFlagEnabled(2, arg_12_15)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionTrue(3, condition=2)
    Kill(arg_0_3, award_souls=True)
    CancelSpecialEffect(arg_0_3, 90111)
    End()
    DropMandatoryTreasure(arg_0_3)


@NeverRestart(11410546)
def Event_11410546(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410546"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfFlagDisabled(1, 1506)
    IfFlagDisabled(1, 1508)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11410547)
def Event_11410547(_, arg_0_3: int):
    """Event 11410547"""
    EndIfFlagEnabled(1512)
    SkipLinesIfThisEventSlotFlagDisabled(3)
    SkipLinesIfFlagEnabled(1, 11410593)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    IfThisEventFlagEnabled(-1)
    IfFlagEnabled(-1, 1503)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventFlagEnabled(1)
    IfFlagDisabled(0, 814)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7856)


@NeverRestart(11410548)
def Event_11410548(_, arg_0_3: int):
    """Event 11410548"""
    EndIfFlagEnabled(1512)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)
    End()
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1507)
    IfFlagEnabled(1, 11410593)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)


@NeverRestart(11410549)
def Event_11410549(_, arg_0_3: int):
    """Event 11410549"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1507)
    IfFlagEnabled(1, 11410594)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


@NeverRestart(11410550)
def Event_11410550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11410550"""
    IfHost(1)
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1505)
    IfFlagEnabled(1, 11410594)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11415030)
def Event_11415030():
    """Event 11415030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6542, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11415033)
    IfClient(2)
    IfFlagEnabled(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6542)
    EndIfFlagEnabled(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1007)
    IfCharacterBackreadEnabled(1, 6542)
    IfEntityWithinDistance(1, entity=6542, other_entity=PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6542,
        region=1412000,
        summon_flag=11415031,
        dismissal_flag=11415033,
    )


@NeverRestart(11415032)
def Event_11415032():
    """Event 11415032"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11415031)
    IfFlagEnabled(1, 11415383)
    IfConditionTrue(0, input_condition=1)
    AICommand(6542, command_id=10, slot=0)
    ReplanAI(6542)
    IfCharacterInsideRegion(0, 6542, region=1412898)
    RotateToFaceEntity(6542, target_entity=1412897)
    ForceAnimation(6542, 7410)
    AICommand(6542, command_id=-1, slot=0)
    ReplanAI(6542)


@NeverRestart(11415035)
def Event_11415035():
    """Event 11415035"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(11415036)
    EndIfFlagEnabled(11410410)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11410810)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412010)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6560,
        region=1412001,
        summon_flag=11415036,
        dismissal_flag=11415037,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11415038)
def Event_11415038():
    """Event 11415038"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(11415039)
    EndIfFlagEnabled(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11410811)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412520)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6561,
        region=1412002,
        summon_flag=11415039,
        dismissal_flag=11415040,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11410810)
def Event_11410810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11410810"""
    SkipLinesIfHost(3)
    IfFlagEnabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_0_3)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterDead(0, arg_0_3)
    End()
