"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 10)
    RegisterBonfire(11410920, obj=1411950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11410992, obj=1411960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11410984, obj=1411961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    SkipLinesIfFlagOff(1, 11410900)
    RegisterBonfire(11410976, obj=1411962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11410968, obj=1411963, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11410960, obj=1411964, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    SkipLinesIfClient(14)
    DisableObject(1411994)
    DeleteVFX(1411995, erase_root_only=False)
    DisableObject(1411996)
    DeleteVFX(1411997, erase_root_only=False)
    DisableObject(1411998)
    DeleteVFX(1411999, erase_root_only=False)
    DisableObject(1411988)
    DeleteVFX(1411989, erase_root_only=False)
    DisableObject(1411986)
    DeleteVFX(1411987, erase_root_only=False)
    DisableObject(1411984)
    DeleteVFX(1411985, erase_root_only=False)
    DisableObject(1411982)
    DeleteVFX(1411983, erase_root_only=False)
    SkipLinesIfFlagOff(3, 11410291)
    DisableObject(1411121)
    DeleteVFX(1413400, erase_root_only=True)
    DeleteVFX(1413410, erase_root_only=True)
    SkipLinesIfFlagOff(3, 11410292)
    DisableObject(1411122)
    DeleteVFX(1413401, erase_root_only=True)
    DeleteVFX(1413411, erase_root_only=True)
    RunEvent(11410095)
    RunEvent(11415090)
    RunEvent(11415091)
    RunEvent(11415092)
    RunEvent(11410800)
    RunEvent(11410400)
    RunEvent(11410340)
    RunEvent(11410341)
    RunEvent(11410350)
    RunEvent(11410360)
    RunEvent(11415399)
    RunEvent(11410260)
    RunEvent(11410200)
    RunEvent(11410201, slot=0, args=(1411210, 462000000))
    RunEvent(11410201, slot=1, args=(1411211, 462100000))
    RunEvent(11410201, slot=2, args=(1411212, 462200000))
    RunEvent(11410201, slot=3, args=(1411213, 462300000))
    RunEvent(11410201, slot=4, args=(1411214, 462400000))
    RunEvent(11410201, slot=5, args=(1411215, 462500000))
    RunEvent(11410201, slot=6, args=(1411216, 462600000))
    RunEvent(11410201, slot=7, args=(1411217, 462700000))
    RunEvent(11410201, slot=8, args=(1411218, 462800000))
    RunEvent(11410201, slot=9, args=(1411219, 462900000))
    RunEvent(11410201, slot=10, args=(1411220, 463000000))
    RunEvent(11410201, slot=11, args=(1411221, 463100000))
    RunEvent(11410201, slot=12, args=(1411222, 463200000))
    RunEvent(11410250)
    DisableSoundEvent(1413801)
    SkipLinesIfFlagOff(4, 11410900)
    RunEvent(11415372)
    DisableObject(1411790)
    DeleteVFX(1411791, erase_root_only=False)
    SkipLines(10)
    RunEvent(11415370)
    RunEvent(11415371)
    RunEvent(11415373)
    RunEvent(11415372)
    RunEvent(11415374)
    RunEvent(11415376)
    RunEvent(11415377)
    RunEvent(11415378)
    RunEvent(11415379)
    RunEvent(11410900)
    RunEvent(11415310, slot=0, args=(11415376,))
    RunEvent(11415310, slot=1, args=(11415310,))
    RunEvent(11415310, slot=2, args=(11415311,))
    RunEvent(11415310, slot=3, args=(11415312,))
    RunEvent(11415310, slot=4, args=(11415313,))
    DisableSoundEvent(1413803)
    SkipLinesIfFlagOff(6, 11410410)
    RunEvent(11415342)
    DisableObject(1411410)
    DeleteVFX(1411411, erase_root_only=False)
    DisableObject(1411412)
    DeleteVFX(1411413, erase_root_only=False)
    SkipLines(7)
    RunEvent(11415340)
    RunEvent(11415341)
    RunEvent(11415343)
    RunEvent(11415342)
    RunEvent(11415344)
    RunEvent(11410410)
    RunEvent(11415345)
    DisableSoundEvent(1413802)
    SkipLinesIfFlagOff(6, 11410901)
    RunEvent(11415382)
    DisableObject(1411890)
    DeleteVFX(1411891, erase_root_only=False)
    DisableObject(1411892)
    DeleteVFX(1411893, erase_root_only=False)
    SkipLines(7)
    RunEvent(11415380)
    RunEvent(11415381)
    RunEvent(11415383)
    RunEvent(11415382)
    RunEvent(11415384)
    RunEvent(11410901)
    RunEvent(11415386)
    DisableSoundEvent(1413800)
    SkipLinesIfFlagOff(4, 10)
    RunEvent(11415392)
    DisableObject(1411990)
    DeleteVFX(1411991, erase_root_only=False)
    SkipLines(11)
    RunEvent(11415390)
    RunEvent(11415391)
    RunEvent(11415393)
    RunEvent(11415392)
    RunEvent(11410001)
    RunEvent(11415394)
    RunEvent(11415395)
    RunEvent(11415396)
    RunEvent(11415397)
    RunEvent(11415398)
    RunEvent(11415300)
    RunEvent(800, slot=0, args=(1410100,))
    RunEvent(11410100, slot=4, args=(1410307,))
    RunEvent(11410100, slot=6, args=(6620,))
    RunEvent(11410100, slot=7, args=(1410110,))
    RunEvent(11410100, slot=8, args=(1410150,))
    RunEvent(11410100, slot=9, args=(1410350,))
    RunEvent(11410100, slot=10, args=(1410351,))
    RunEvent(11410100, slot=11, args=(1410352,))
    RunEvent(11410100, slot=12, args=(1410353,))
    RunEvent(11410100, slot=13, args=(1410354,))
    RunEvent(11410100, slot=14, args=(1410355,))
    RunEvent(11410100, slot=15, args=(1410356,))
    RunEvent(11410100, slot=16, args=(1410357,))
    RunEvent(11410100, slot=17, args=(1410358,))
    RunEvent(11410100, slot=18, args=(1410359,))
    RunEvent(11410100, slot=19, args=(1410360,))
    RunEvent(11410100, slot=20, args=(1410361,))
    RunEvent(11410100, slot=21, args=(1410362,))
    RunEvent(11410100, slot=22, args=(1410363,))
    RunEvent(11410100, slot=23, args=(1410364,))
    RunEvent(11410100, slot=24, args=(1410365,))
    RunEvent(11410100, slot=25, args=(1410366,))
    RunEvent(11410100, slot=26, args=(1410367,))
    RunEvent(11410100, slot=27, args=(1410368,))
    RunEvent(11410100, slot=28, args=(1410369,))
    RunEvent(11410100, slot=29, args=(1410370,))
    RunEvent(11410100, slot=30, args=(1410371,))
    RunEvent(11410100, slot=31, args=(1410372,))
    RunEvent(11410100, slot=32, args=(1410373,))
    RunEvent(11410100, slot=33, args=(1410374,))
    RunEvent(11410100, slot=34, args=(1410375,))
    RunEvent(11410100, slot=35, args=(1410376,))
    RunEvent(11410100, slot=36, args=(1410377,))
    RunEvent(11410100, slot=37, args=(1410378,))
    RunEvent(11410100, slot=38, args=(1410450,))
    RunEvent(11410100, slot=39, args=(1410451,))
    RunEvent(11410100, slot=40, args=(1410452,))
    RunEvent(11410100, slot=41, args=(1410453,))
    RunEvent(11410100, slot=42, args=(1410454,))
    RunEvent(11410100, slot=43, args=(1410455,))
    RunEvent(11410100, slot=44, args=(1410456,))
    RunEvent(11415210, slot=0, args=(11415250, 11415263, 11))
    RunEvent(11415250, slot=0, args=(1410200, 1410220, 1410221, 1410222, 1410223, 1410224))
    RunEvent(11415250, slot=1, args=(1410201, 1410225, 1410226, 1410227, 1410228, 1410229))
    RunEvent(11415250, slot=2, args=(1410202, 1410230, 1410231, 1410232, 1410233, 1410234))
    RunEvent(11415250, slot=3, args=(1410203, 1410235, 1410236, 1410237, 1410238, 1410239))
    RunEvent(11415250, slot=4, args=(1410204, 1410240, 1410241, 1410242, 1410243, 1410244))
    RunEvent(11415250, slot=5, args=(1410205, 1410245, 1410246, 1410247, 1410248, 1410249))
    RunEvent(11415250, slot=6, args=(1410206, 1410250, 1410251, 1410252, 1410253, 1410254))
    RunEvent(11415250, slot=7, args=(1410207, 1410255, 1410256, 1410257, 1410258, 1410259))
    RunEvent(11415250, slot=8, args=(1410208, 1410260, 1410261, 1410262, 1410263, 1410264))
    RunEvent(11415250, slot=9, args=(1410209, 1410265, 1410266, 1410267, 1410268, 1410269))
    RunEvent(11415250, slot=10, args=(1410210, 1410270, 1410271, 1410272, 1410273, 1410274))
    RunEvent(11415250, slot=11, args=(1410211, 1410275, 1410276, 1410277, 1410278, 1410279))
    RunEvent(11415250, slot=12, args=(1410212, 1410280, 1410281, 1410282, 1410283, 1410284))
    RunEvent(11415250, slot=13, args=(1410213, 1410285, 1410286, 1410287, 1410288, 1410289))
    RunEvent(11415100, slot=0, args=(1410301, 1410301, 9060, 15.0, 0.0), arg_types="iiiff")
    RunEvent(11415100, slot=1, args=(1410302, 1410302, 9060, 10.0, 0.0), arg_types="iiiff")
    RunEvent(11415100, slot=2, args=(1410307, 1410307, 9060, 15.0, 0.0), arg_types="iiiff")
    RunEvent(11415120, slot=0, args=(10000, 1410303, 9060, 1412302, 0.30000001192092896), arg_types="iiiif")
    RunEvent(11415120, slot=1, args=(10000, 1410304, 9060, 1412302, 0.10000000149011612), arg_types="iiiif")
    RunEvent(11415120, slot=2, args=(10000, 1410305, 9060, 1412302, 0.0), arg_types="iiiif")
    RunEvent(11415120, slot=3, args=(10000, 1410306, 9060, 1412302, 0.20000000298023224), arg_types="iiiif")
    RunEvent(11410150, slot=1, args=(1410301, 33900000))
    RunEvent(11410150, slot=2, args=(1410302, 33900000))
    RunEvent(11410150, slot=3, args=(1410303, 33900000))
    RunEvent(11410150, slot=4, args=(1410304, 33900000))
    RunEvent(11410150, slot=5, args=(1410305, 33900000))
    RunEvent(11410150, slot=6, args=(1410306, 33900000))
    RunEvent(11410600, slot=0, args=(1411650, 11410600))
    RunEvent(11410600, slot=1, args=(1411651, 11410601))
    RunEvent(11410600, slot=2, args=(1411652, 11410602))
    RunEvent(11410600, slot=3, args=(1411653, 11410603))
    RunEvent(11415843, slot=0, args=(10, 1411990, 1412998, 1412997))
    RunEvent(11415846, slot=0, args=(10, 1411990, 1411991))
    RunEvent(11415843, slot=1, args=(11410900, 1411790, 1412698, 1412697))
    RunEvent(11415846, slot=1, args=(11410900, 1411790, 1411791))
    RunEvent(11415843, slot=2, args=(11410901, 1411890, 1412898, 1412897))
    RunEvent(11415846, slot=2, args=(11410901, 1411890, 1411891))
    RunEvent(11415843, slot=3, args=(11410410, 1411410, 1412411, 1412412))
    RunEvent(11415846, slot=3, args=(11410410, 1411410, 1411411))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11410100, slot=0, args=(1410410,))
    RunEvent(11410100, slot=1, args=(1410411,))
    RunEvent(11410100, slot=2, args=(1410412,))
    RunEvent(11410100, slot=3, args=(1410413,))
    HumanityRegistration(6620, 8250)
    HumanityRegistration(6542, 8310)
    HumanityRegistration(6560, 8956)
    HumanityRegistration(6561, 8956)
    RunEvent(11415030)
    RunEvent(11415029)
    RunEvent(11415032)
    RunEvent(11415035)
    RunEvent(11415038)
    RunEvent(11410810, slot=0, args=(6560, 11415036, 11415037))
    RunEvent(11410810, slot=1, args=(6561, 11415039, 11415040))
    RunEvent(14015990, slot=0, args=(11415031, 6542))
    HumanityRegistration(6002, 8310)
    HumanityRegistration(6004, 8310)
    SkipLinesIfFlagOn(3, 1009)
    SkipLinesIfFlagOn(2, 1004)
    SkipLinesIfFlagOn(1, 1003)
    DisableCharacter(6002)
    SkipLinesIfFlagOn(1, 11410580)
    SkipLines(1)
    Move(6002, destination=1412500, destination_type=CoordEntityType.Region, set_draw_parent=1413000)
    SkipLinesIfFlagOn(1, 1002)
    DisableCharacter(6004)
    SetTeamTypeAndExitStandbyAnimation(6004, TeamType.HostileAlly)
    RunEvent(11410510, slot=0, args=(6002, 1004))
    RunEvent(11410520, slot=0, args=(6002, 1000, 1029, 1005))
    RunEvent(11410530, slot=0, args=(6002, 1000, 1029, 1009))
    RunEvent(11410531, slot=0, args=(6002, 1000, 1029, 1002))
    RunEvent(11410532, slot=0, args=(6002, 1000, 1029, 1003))
    RunEvent(11410533, slot=0, args=(6006, 1000, 1029, 1012))
    RunEvent(11410534, slot=0, args=(6004, 1000, 1029, 1011))
    HumanityRegistration(6286, 8446)
    SkipLinesIfFlagRangeAnyOn(1, (1503, 1507))
    DisableCharacter(6286)
    SkipLinesIfFlagOn(3, 1504)
    SkipLinesIfFlagOn(2, 1506)
    SkipLinesIfFlagOn(1, 1507)
    SkipLines(2)
    AddSpecialEffect(6286, 90111)
    Move(6286, destination=1412360, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(1, 11410593)
    SetStandbyAnimationSettings(6286, standby_animation=7855)
    RunEvent(11410501, slot=0, args=(6286, 1512))
    RunEvent(11410546, slot=0, args=(6286, 1490, 1514, 1513))
    RunEvent(11410540, slot=0, args=(6286, 1490, 1514, 1503))
    RunEvent(11410541, slot=0, args=(6286, 1490, 1514, 1504))
    RunEvent(11410542, slot=0, args=(6286, 1490, 1514, 1505))
    RunEvent(11410543, slot=0, args=(6286, 1490, 1514, 1506))
    RunEvent(11410544, slot=0, args=(6286, 1490, 1514, 1507))
    RunEvent(11410545, slot=0, args=(6286, 1490, 1514, 1513))
    RunEvent(11410549, slot=0, args=(6286,))
    RunEvent(11410550, slot=0, args=(6286, 1490, 1514, 1514))
    RunEvent(11410547, slot=0, args=(6286,))
    RunEvent(11410548, slot=0, args=(6286,))


def Event11410090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410090: Event 11410090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=False)
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
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11415090():
    """ 11415090: Event 11415090 """
    EndIfThisEventOn()
    DisableCharacter(1410900)
    DisableCharacter(1410901)
    DisableCharacter(1410902)
    DisableCharacter(1410903)
    DisableCharacter(1410904)
    DisableCharacter(1410905)
    DisableCharacter(1410906)
    DisableCharacter(1410907)
    IfFlagOn(0, 11410050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1410900)
    EnableCharacter(1410901)
    EnableCharacter(1410902)
    EnableCharacter(1410903)
    EnableCharacter(1410904)
    EnableCharacter(1410905)
    EnableCharacter(1410906)
    EnableCharacter(1410907)


@RestartOnRest
def Event11415091():
    """ 11415091: Event 11415091 """
    IfFlagOn(-1, 11415095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11410050)
    DisableFlag(11415095)
    EnableFlag(5001)
    Kill(1410900, award_souls=False)
    Kill(1410901, award_souls=False)
    Kill(1410902, award_souls=False)
    Kill(1410903, award_souls=False)
    Kill(1410904, award_souls=False)
    Kill(1410905, award_souls=False)
    Kill(1410906, award_souls=False)
    Kill(1410907, award_souls=False)


@RestartOnRest
def Event11415092():
    """ 11415092: Event 11415092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11410050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=LOST_IZALITH)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11410050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=LOST_IZALITH)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11410050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=LOST_IZALITH)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11410050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=LOST_IZALITH)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11410050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=LOST_IZALITH)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11410050)
    RestartIfConditionFalse(-6)
    EnableFlag(11410050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=LOST_IZALITH)
    RestartIfConditionFalse(7)
    DisableFlag(11410050)
    EnableFlag(11415095)


def Event11410095():
    """ 11410095: Event 11410095 """
    SkipLinesIfFlagOff(5, 11800100)
    EnableFlag(11410096)
    DisableObject(1411710)
    DeleteVFX(1411711, erase_root_only=False)
    DisableFlag(402)
    End()
    SkipLinesIfFlagOff(3, 11410096)
    DisableObject(1411710)
    DeleteVFX(1411711, erase_root_only=False)
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
    DisplayStatus(10010630, pad_enabled=True)
    Restart()


def Event11415390():
    """ 11415390: Event 11415390 """
    IfFlagOff(1, 10)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415391():
    """ 11415391: Event 11415391 """
    DisableNetworkSync()
    IfFlagOff(1, 10)
    IfFlagOn(1, 11415393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415393():
    """ 11415393: Event 11415393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 10)
    IfCharacterInsideRegion(1, PLAYER, region=1412996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1410800)


@RestartOnRest
def Event11415392():
    """ 11415392: Event 11415392 """
    SkipLinesIfFlagOff(7, 10)
    DisableCharacter(1410800)
    DisableCharacter(1410801)
    DisableCharacter(1410802)
    Kill(1410800, award_souls=False)
    Kill(1410801, award_souls=False)
    Kill(1410802, award_souls=False)
    End()
    SkipLinesIfFlagRangeAnyOn(1, (11410291, 11410292))
    DisableCharacter(1410800)
    SkipLinesIfFlagRangeAllOff(1, (11410291, 11410292))
    ResetStandbyAnimationSettings(1410801)
    EnableInvincibility(1410800)
    EnableInvincibility(1410801)
    DisableHealthBar(1410800)
    DisableHealthBar(1410801)
    DisableAI(1410801)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=1)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagRangeAnyOn(2, (11410291, 11410292))
    ResetStandbyAnimationSettings(1410801)
    ForceAnimation(1410801, 9060)
    EnableAI(1410801)
    EnableBossHealthBar(1410802, name=5400, slot=0)


def Event11410001():
    """ 11410001: Event 11410001 """
    DisableObject(1411950)
    IfCharacterDead(0, 1410802)
    EnableFlag(10)
    KillBoss(1410800)
    SkipLinesIfClient(1)
    AwardAchievement(36)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=0)
    DisableObject(1411990)
    DeleteVFX(1411991, erase_root_only=True)
    DisableNetworkSync()
    CreateTemporaryVFX(90014, anchor_entity=1411950, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(1411950)
    RegisterBonfire(11410920, obj=1411950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)


def Event11415394():
    """ 11415394: Event 11415394 """
    DisableNetworkSync()
    IfFlagOff(1, 10)
    IfFlagOn(1, 11415392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415391)
    IfCharacterInsideRegion(1, PLAYER, region=1412990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413800)


def Event11415395():
    """ 11415395: Event 11415395 """
    DisableNetworkSync()
    IfFlagOn(1, 10)
    IfFlagOn(1, 11415394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1413800)


@RestartOnRest
def Event11415396():
    """ 11415396: Event 11415396 """
    SkipLinesIfFlagRangeAnyOn(15, (11410291, 11410292))
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOn(6, 11410292)
    EnableFlag(11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140116, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140116, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140115, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140115, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(1410800)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(1410800, 5130)
    SkipLinesIfFlagOn(12, 11410000)
    SkipLinesIfFlagOff(5, 11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140117, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140117, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140118, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140118, skippable=False, fade_out=False, player_id=PLAYER)
    SetStandbyAnimationSettings(1410800, standby_animation=10000)
    WaitFrames(1)
    EnableFlag(11410000)
    ResetStandbyAnimationSettings(1410800)
    WaitFrames(1)
    ResetAnimation(1410800, disable_interpolation=True)


@RestartOnRest
def Event11415397():
    """ 11415397: Event 11415397 """
    EnableInvincibility(1410802)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableInvincibility(1410802)
    IfHealthLessThanOrEqual(0, 1410802, 0.0)
    DisableInvincibility(1410800)
    DisableInvincibility(1410801)
    Kill(1410800, award_souls=True)
    Kill(1410801, award_souls=False)


@RestartOnRest
def Event11415398():
    """ 11415398: Event 11415398 """
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterBackreadEnabled(0, 1410800)
    AICommand(1410800, command_id=2, slot=0)
    ReplanAI(1410800)
    AICommand(1410801, command_id=2, slot=0)
    ReplanAI(1410801)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    SkipLinesIfFlagOn(1, 11410000)
    IfFlagOn(1, 11415396)
    IfConditionTrue(0, input_condition=1)
    IfCharacterBackreadEnabled(0, 1410800)
    AICommand(1410800, command_id=3, slot=0)
    ReplanAI(1410800)
    AICommand(1410801, command_id=3, slot=0)
    ReplanAI(1410801)


def Event11415399():
    """ 11415399: Event 11415399 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1412110)
    EnableInvincibility(PLAYER)
    IfCharacterOutsideRegion(0, PLAYER, region=1412110)
    Wait(3.0)
    DisableInvincibility(PLAYER)


def Event11415300():
    """ 11415300: Event 11415300 """
    EndIfFlagOn(10)
    SkipLinesIfThisEventOn(2)
    EnableFlag(11415300)
    EnableObjectInvulnerability(1411120)
    IfFlagOff(1, 11410291)
    IfObjectDestroyed(1, 1411121)
    IfFlagOff(2, 11410292)
    IfObjectDestroyed(2, 1411122)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfFlagOn(-1, 10)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(10)
    SkipLinesIfFinishedConditionFalse(4, 1)
    EnableFlag(11410291)
    DeleteVFX(1413400, erase_root_only=True)
    DeleteVFX(1413410, erase_root_only=True)
    Restart()
    EnableFlag(11410292)
    DeleteVFX(1413401, erase_root_only=True)
    DeleteVFX(1413411, erase_root_only=True)
    Restart()


def Event11410200():
    """ 11410200: Event 11410200 """
    SkipLinesIfThisEventOff(6)
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
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfCharacterInsideRegion(1, PLAYER, region=1412100)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11410200)
    DisableObjectInvulnerability(1411200)
    DisableObjectInvulnerability(1411201)
    DisableObjectInvulnerability(1411202)
    DisableObjectInvulnerability(1411203)
    DisableObjectInvulnerability(1411204)
    CreateTemporaryVFX(140009, anchor_entity=1411202, anchor_type=CoordEntityType.Object, model_point=-1)
    DestroyObject(1411200)
    PlaySoundEffect(anchor_entity=1411200, sound_type=SoundType.o_Object, sound_id=463300000)
    WaitFrames(4)
    DestroyObject(1411201)
    PlaySoundEffect(anchor_entity=1411201, sound_type=SoundType.o_Object, sound_id=463400000)
    WaitFrames(3)
    DestroyObject(1411202)
    PlaySoundEffect(anchor_entity=1411202, sound_type=SoundType.o_Object, sound_id=463500000)
    WaitFrames(2)
    DestroyObject(1411203)
    PlaySoundEffect(anchor_entity=1411203, sound_type=SoundType.o_Object, sound_id=463600000)
    WaitFrames(1)
    DestroyObject(1411204)
    PlaySoundEffect(anchor_entity=1411204, sound_type=SoundType.o_Object, sound_id=463700000)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(1411200)
    DisableObject(1411203)
    DisableObject(1411204)


def Event11410201(_, arg_0_3: int, arg_4_7: int):
    """ 11410201: Event 11410201 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    RestoreObject(arg_0_3)
    EnableObjectInvulnerability(arg_0_3)
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=8.0)
    DisableObjectInvulnerability(arg_0_3)
    DestroyObject(arg_0_3)
    CreateTemporaryVFX(140008, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=arg_4_7)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(arg_0_3)


def Event11410250():
    """ 11410250: Event 11410250 """
    EndIfFlagRangeAllOn((11410291, 11410292))
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
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
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


def Event11415370():
    """ 11415370: Event 11415370 """
    IfFlagOff(1, 11410900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412698,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411790,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412697)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415371():
    """ 11415371: Event 11415371 """
    IfFlagOff(1, 11410900)
    IfFlagOn(1, 11415373)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412698,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412697)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415373():
    """ 11415373: Event 11415373 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11410900)
    IfCharacterInsideRegion(1, PLAYER, region=1412696)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1410600, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1410600)
    SetNetworkUpdateRate(1410600, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableInvincibility(1410600)


@RestartOnRest
def Event11415372():
    """ 11415372: Event 11415372 """
    SkipLinesIfFlagOff(3, 11410900)
    DisableBackread(1410600)
    Kill(1410600, award_souls=False)
    End()
    DisableAI(1410600)
    DisableHealthBar(1410600)
    EnableInvincibility(1410600)
    IfFlagOn(1, 11415373)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51410180)
    IfFlagOn(2, 11415373)
    IfAttacked(2, 1410600, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1410600)
    EnableBossHealthBar(1410600, name=5250, slot=0)


def Event11410900():
    """ 11410900: Event 11410900 """
    DisableObject(1411962)
    IfCharacterDead(0, 1410600)
    EnableFlag(11410900)
    KillBoss(1410600)
    DisableBackread(1410600)
    EnableFlag(11410800)
    DisableObject(1411790)
    DeleteVFX(1411791, erase_root_only=True)
    EnableObject(1411962)
    RegisterBonfire(11410976, obj=1411962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    EndIfFlagOn(11800100)
    EnableFlag(402)


def Event11415374():
    """ 11415374: Event 11415374 """
    DisableNetworkSync()
    IfFlagOff(1, 11410900)
    IfFlagOn(1, 11415372)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415371)
    IfCharacterInsideRegion(1, PLAYER, region=1412690)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413801)
    IfFlagOn(0, 11410900)
    DisableSoundEvent(1413801)


@RestartOnRest
def Event11415376():
    """ 11415376: Event 11415376 """
    IfCharacterAlive(1, 1410600)
    IfCharacterInsideRegion(1, 1410600, region=1412799)
    IfConditionTrue(0, input_condition=1)
    Move(1410600, destination=1412797, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1410600, 17006, wait_for_completion=True)
    Move(1410600, destination=1412798, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest
def Event11415377():
    """ 11415377: Event 11415377 """
    SkipLinesIfThisEventOff(4)
    CancelSpecialEffect(1410600, 5132)
    AddSpecialEffect(1410600, 5133)
    AICommand(1410600, command_id=-1, slot=1)
    End()
    IfHasTAEEvent(0, 1410600, tae_event_id=300)
    CancelSpecialEffect(1410600, 5132)
    AddSpecialEffect(1410600, 5133)
    AICommand(1410600, command_id=-1, slot=1)
    ReplanAI(1410600)


@RestartOnRest
def Event11415378():
    """ 11415378: Event 11415378 """
    SkipLinesIfFlagOn(4, 0)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51410180)
    IfCharacterInsideRegion(1, PLAYER, region=1412796)
    IfConditionTrue(0, input_condition=1)
    AICommand(1410600, command_id=1, slot=1)
    ReplanAI(1410600)


@RestartOnRest
def Event11415379():
    """ 11415379: Event 11415379 """
    EndIfFlagOn(11410900)
    IfFlagRangeAllOn(1, (11415310, 11415314))
    IfHealthLessThanOrEqual(2, 1410600, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    Kill(1410600, award_souls=True)


@RestartOnRest
def Event11415310(_, arg_0_3: int):
    """ 11415310: Event 11415310 """
    IfFlagOn(1, 11415376)
    IfFlagOn(1, arg_0_3)
    IfAttacked(1, 1410600, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    End()


def Event11410800():
    """ 11410800: Event 11410800 """
    SkipLinesIfFlagOff(5, 11410801)
    DisableObject(1411100)
    DisableMapCollision(1413100)
    DisableSoundEvent(1413805)
    EnableTreasure(1411610)
    End()
    DisableObject(1411610)
    DisableTreasure(1411610)
    DisableMapCollision(1413101)
    DisableCharacter(1410450)
    DisableCharacter(1410451)
    DisableCharacter(1410452)
    DisableCharacter(1410453)
    DisableCharacter(1410454)
    DisableCharacter(1410455)
    DisableCharacter(1410456)
    DisableNetworkSync()
    IfThisEventOn(0)
    Wait(5.0)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, 0.0)
    EndIfConditionTrue(1)
    EndIfClient()
    IfCharacterInsideRegion(0, PLAYER, region=1412530)
    PlayCutscene(140100, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11410801)
    DisableObject(1411100)
    DisableSoundEvent(1413805)
    DisableMapCollision(1413100)
    EnableMapCollision(1413101)
    EnableObject(1411610)
    EnableTreasure(1411610)
    EnableCharacter(1410450)
    EnableCharacter(1410451)
    EnableCharacter(1410452)
    EnableCharacter(1410453)
    EnableCharacter(1410454)
    EnableCharacter(1410455)
    EnableCharacter(1410456)


def Event11415380():
    """ 11415380: Event 11415380 """
    IfFlagOff(1, 11410901)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412898,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411890,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412897)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415381():
    """ 11415381: Event 11415381 """
    IfFlagOff(1, 11410901)
    IfFlagOn(1, 11415383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412897)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415383():
    """ 11415383: Event 11415383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11410901)
    IfCharacterInsideRegion(1, PLAYER, region=1412896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1410700)


@RestartOnRest
def Event11415382():
    """ 11415382: Event 11415382 """
    DisableObject(1411110)
    RunEvent(11415385)
    SkipLinesIfFlagOff(2, 11410901)
    DisableBackread(1410700)
    End()
    SkipLinesIfFlagOn(2, 11410002)
    EnableObject(1411110)
    DisableCharacter(1410700)
    DisableAI(1410700)
    IfFlagOn(1, 11415383)
    IfCharacterInsideRegion(1, PLAYER, region=1412896)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(8, 11410002)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140120, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140120, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(1410700)
    DisableObject(1411110)
    EnableFlag(11410002)
    EnableAI(1410700)
    EnableBossHealthBar(1410700, name=5200, slot=0)


def Event11410901():
    """ 11410901: Event 11410901 """
    IfCharacterDead(0, 1410700)
    EnableFlag(11410901)
    KillBoss(1410700)
    EnableFlag(11410901)
    DisableObject(1411890)
    DeleteVFX(1411891, erase_root_only=True)
    DisableObject(1411892)
    DeleteVFX(1411893, erase_root_only=True)
    DisableNetworkSync()
    Wait(10.0)
    DisableCharacter(1410700)
    DisableBackread(1410700)


def Event11415384():
    """ 11415384: Event 11415384 """
    DisableNetworkSync()
    IfFlagOff(1, 11410901)
    IfFlagOn(1, 11410002)
    IfFlagOn(1, 11415382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415381)
    IfCharacterInsideRegion(1, PLAYER, region=1412890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413802)
    IfFlagOn(0, 11410901)
    DisableSoundEvent(1413802)


@UnknownRestart
def Event11415385():
    """ 11415385: Event 11415385 """
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
    EndIfFlagOn(11410901)
    RunEvent(11415350, slot=0, args=(11415380, 5200, 5200, 125, 1410710), arg_types="ihiii")
    RunEvent(11415350, slot=1, args=(11415350, 5201, 5201, 125, 1410711), arg_types="ihiii")
    RunEvent(11415350, slot=2, args=(11415351, 5202, 5202, 125, 1410712), arg_types="ihiii")
    RunEvent(11415350, slot=3, args=(11415352, 5203, 5203, 125, 1410713), arg_types="ihiii")
    RunEvent(11415350, slot=4, args=(11415353, 5204, 5204, 125, 1410714), arg_types="ihiii")
    RunEvent(11415360, slot=0, args=(11415380, 5205, 5205, 95, 1410720), arg_types="ihiii")
    RunEvent(11415360, slot=1, args=(11415360, 5206, 5206, 95, 1410721), arg_types="ihiii")
    RunEvent(11415360, slot=2, args=(11415361, 5207, 5207, 95, 1410722), arg_types="ihiii")
    RunEvent(11415360, slot=3, args=(11415362, 5208, 5208, 95, 1410723), arg_types="ihiii")
    RunEvent(11415360, slot=4, args=(11415363, 5209, 5209, 95, 1410724), arg_types="ihiii")
    RunEvent(11415320, slot=0, args=(11415380, 1410710))
    RunEvent(11415320, slot=1, args=(11415350, 1410711))
    RunEvent(11415320, slot=2, args=(11415351, 1410712))
    RunEvent(11415320, slot=3, args=(11415352, 1410713))
    RunEvent(11415320, slot=4, args=(11415353, 1410714))
    RunEvent(11415320, slot=5, args=(11415380, 1410720))
    RunEvent(11415320, slot=6, args=(11415360, 1410721))
    RunEvent(11415320, slot=7, args=(11415361, 1410722))
    RunEvent(11415320, slot=8, args=(11415362, 1410723))
    RunEvent(11415320, slot=9, args=(11415363, 1410724))


def Event11415386():
    """ 11415386: Event 11415386 """
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


@UnknownRestart
def Event11415320(_, arg_0_3: int, arg_4_7: int):
    """ 11415320: Event 11415320 """
    IfFlagOn(1, arg_0_3)
    IfHasTAEEvent(1, 1410700, tae_event_id=400)
    IfHealthGreaterThan(1, 1410700, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthLessThanOrEqual(0, 1410700, 0.0)
    Kill(arg_4_7, award_souls=True)


@UnknownRestart
def Event11415350(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11415350: Event 11415350 """
    SkipLinesIfThisEventSlotOff(1)
    EnableCharacter(arg_16_19)
    SkipLinesIfFlagOff(4, 11415354)
    SetDisplayMask(1410700, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1410700, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1410700, command_id=20, slot=0)
    End()
    IfFlagOn(0, arg_0_3)
    CreateNPCPart(
        1410700,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, 1410700, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, 1410700, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EzstateAIRequest(1410700, command_id=1001, slot=0)
    IfHasTAEEvent(0, 1410700, tae_event_id=400)
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
    SkipLinesIfFlagOff(2, 11415353)
    AICommand(1410700, command_id=20, slot=0)
    End()
    IfHasTAEEvent(0, 1410700, tae_event_id=300)
    SetDisplayMask(1410700, bit_index=0, switch_type=OnOffChange.Off)
    SetCollisionMask(1410700, bit_index=1, switch_type=OnOffChange.On)
    AICommand(1410700, command_id=-1, slot=0)


@UnknownRestart
def Event11415360(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11415360: Event 11415360 """
    SkipLinesIfThisEventSlotOff(1)
    EnableCharacter(arg_16_19)
    SkipLinesIfFlagOff(4, 11415364)
    SetDisplayMask(1410700, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1410700, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(1410700, command_id=20, slot=1)
    End()
    IfFlagOn(0, arg_0_3)
    CreateNPCPart(
        1410700,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, 1410700, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, 1410700, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EzstateAIRequest(1410700, command_id=1002, slot=0)
    IfHasTAEEvent(0, 1410700, tae_event_id=400)
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
    SkipLinesIfFlagOff(2, 11415363)
    AICommand(1410700, command_id=20, slot=1)
    End()
    IfHasTAEEvent(0, 1410700, tae_event_id=600)
    SetDisplayMask(1410700, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(1410700, bit_index=2, switch_type=OnOffChange.On)
    AICommand(1410700, command_id=-1, slot=1)


def Event11410340():
    """ 11410340: Event 11410340 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1411340, 1)
    End()
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    IfFlagOn(1, 11400598)
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
    RotateToFaceEntity(PLAYER, 1411340)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    ForceAnimation(1411340, 1)
    CreateTemporaryVFX(140000, anchor_entity=1411340, anchor_type=CoordEntityType.Object, model_point=-1)


def Event11410341():
    """ 11410341: Event 11410341 """
    DisableNetworkSync()
    IfFlagOff(1, 11410340)
    IfHost(6)
    IfPlayerCovenant(7, Covenant.ChaosServant)
    IfConditionFalse(6, input_condition=7)
    IfConditionTrue(-7, input_condition=6)
    IfFlagOff(-7, 11400598)
    IfConditionTrue(1, input_condition=-7)
    IfActionButton(
        -2,
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411340,
    )
    IfConditionTrue(1, input_condition=-2)
    IfFlagOff(2, 11410340)
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
    IfFlagOn(3, 11410340)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(11410340)
    DisplayDialog(
        10010160,
        anchor_entity=1411340,
        display_distance=5.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11410360():
    """ 11410360: Event 11410360 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1411360)
    End()
    IfObjectDestroyed(0, 1411360)
    EnableFlag(11410360)


def Event11410400():
    """ 11410400: Event 11410400 """
    SkipLinesIfFlagOff(1, 11410401)
    EndOfAnimation(1411400, 0)
    IfFlagOn(0, 11410410)
    IfFlagOn(1, 11410401)
    IfCharacterInsideRegion(1, PLAYER, region=1412403)
    IfFlagOff(2, 11410401)
    IfCharacterInsideRegion(2, PLAYER, region=1412402)
    IfFlagOff(3, 11410401)
    IfCharacterInsideRegion(3, PLAYER, region=1412401)
    IfFlagOn(4, 11410401)
    IfCharacterInsideRegion(4, PLAYER, region=1412400)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SkipLinesIfFinishedConditionTrue(8, 4)
    SkipLinesIfFlagOn(7, 11410401)
    EnableFlag(11410401)
    CreateObjectVFX(140002, obj=1411400, model_point=100)
    ForceAnimation(1411400, 3, wait_for_completion=True)
    DeleteObjectVFX(1411400, erase_root=True)
    IfAllPlayersOutsideRegion(0, region=1412403)
    ForceAnimation(1411400, 4, wait_for_completion=True)
    Restart()
    DisableFlag(11410401)
    CreateObjectVFX(140002, obj=1411400, model_point=100)
    ForceAnimation(1411400, 1, wait_for_completion=True)
    DeleteObjectVFX(1411400, erase_root=True)
    IfAllPlayersOutsideRegion(0, region=1412402)
    ForceAnimation(1411400, 5, wait_for_completion=True)
    Restart()


def Event11410402():
    """ 11410402: Event 11410402 """
    DisableNetworkSync()
    IfFlagOff(-2, 11410410)
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
    DisplayDialog(
        10010170,
        anchor_entity=1411400,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11415340():
    """ 11415340: Event 11415340 """
    IfFlagOff(1, 11410410)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412411,
        anchor_type=CoordEntityType.Region,
        line_intersects=1411410,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412412)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415341():
    """ 11415341: Event 11415341 """
    IfFlagOff(1, 11410410)
    IfFlagOn(1, 11415343)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1412411,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411410,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412412)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415343():
    """ 11415343: Event 11415343 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11410410)
    IfCharacterInsideRegion(1, PLAYER, region=1412416)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1410400)


@RestartOnRest
def Event11415342():
    """ 11415342: Event 11415342 """
    SkipLinesIfFlagOff(8, 11410410)
    SkipLinesIfClient(4)
    DisableObject(1411410)
    DeleteVFX(1411411, erase_root_only=False)
    DisableObject(1411412)
    DeleteVFX(1411413, erase_root_only=False)
    DisableCharacter(1410400)
    DisableBackread(1410400)
    End()
    DisableAI(1410400)
    IfFlagOn(1, 11415343)
    IfCharacterInsideRegion(1, PLAYER, region=1412416)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1410400)
    EnableBossHealthBar(1410400, name=2230, slot=0)


def Event11415344():
    """ 11415344: Event 11415344 """
    DisableNetworkSync()
    IfFlagOff(1, 11410410)
    IfFlagOn(1, 11415342)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415341)
    IfCharacterInsideRegion(1, PLAYER, region=1412410)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413803)
    IfFlagOn(0, 11410410)
    DisableSoundEvent(1413803)


def Event11415345():
    """ 11415345: Event 11415345 """
    DisableNetworkSync()
    IfFlagOn(1, 11415340)
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
    IfFlagOn(0, 11410410)
    Wait(5.0)
    EnableBackread(1400700)
    EnableBackread(6160)
    EnableBackread(1400411)
    EnableBackread(1400412)
    EnableBackread(1400413)
    EnableBackread(1400414)
    EnableBackread(1400415)


def Event11410410():
    """ 11410410: Event 11410410 """
    IfCharacterDead(0, 1410400)
    EnableFlag(11410410)
    KillBoss(1410400)
    EnableFlag(11410410)
    DisableObject(1411410)
    DeleteVFX(1411411, erase_root_only=True)
    DisableObject(1411412)
    DeleteVFX(1411413, erase_root_only=True)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(1410400)
    DisableBackread(1410400)


@RestartOnRest
def Event11415100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: float):
    """ 11415100: Event 11415100 """
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)
    End()
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=arg_12_15)
    Wait(arg_16_19)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)


@RestartOnRest
def Event11415120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 11415120: Event 11415120 """
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)
    End()
    IfCharacterInsideRegion(0, arg_0_3, region=arg_12_15)
    Wait(arg_16_19)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)


@RestartOnRest
def Event11415200():
    """ 11415200: Event 11415200 """
    RunEvent(11415201, slot=0, args=(1410500, 1, 3290, 3290, 11415201), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415201, 0, 1), arg_types="iiBB")
    RunEvent(5200, slot=-1, args=(1410500, 11415201, 2, 3), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415201, 1411500, 1411501, 120, 123), arg_types="iiiihh")
    RunEvent(5201, slot=-1, args=(1410500, 11415201, 1411502, 1411503, 126, 129), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415201, 1410550, 1410551, 120, 123))
    RunEvent(5202, slot=-1, args=(1410500, 11415201, 1410552, 1410553, 126, 129))
    RunEvent(11415201, slot=1, args=(1410500, 2, 3291, 3291, 11415202), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415202, 5, 11), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415202, 1411504, 1411505, 135, 137), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415202, 1410554, 1410555, 135, 137))
    RunEvent(5202, slot=-1, args=(1410500, 11415202, 1410556, 1410557, 153, 155))
    RunEvent(11415201, slot=2, args=(1410500, 3, 3292, 3292, 11415203), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415203, 6, 7), arg_types="iiBB")
    RunEvent(5200, slot=-1, args=(1410500, 11415203, 8, 10), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415203, 1411506, 1411507, 138, 141), arg_types="iiiihh")
    RunEvent(5201, slot=-1, args=(1410500, 11415203, 1411508, 1411509, 144, 150), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415203, 1410558, 1410559, 138, 141))
    RunEvent(5202, slot=-1, args=(1410500, 11415203, 1410560, 1410561, 144, 150))
    RunEvent(11415201, slot=3, args=(1410500, 4, 3293, 3293, 11415204), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415204, 4, 9), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415204, 1411510, 1411511, 132, 134), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415204, 1410562, 1410563, 132, 134))
    RunEvent(5202, slot=-1, args=(1410500, 11415204, 1410564, 1410565, 150, 152))


@UnknownRestart
def Event11415201(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int):
    """ 11415201: Event 11415201 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(0, arg_0_3, npc_part_id=arg_8_11, value=0)
    DisableFlag(11415290)
    DisableFlag(11415291)
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11415290, 11415291))
    EnableFlag(arg_12_15)
    SkipLinesIfFlagOff(2, 11415290)
    ForceAnimation(arg_0_3, 8000)
    SkipLines(1)
    ForceAnimation(arg_0_3, 8010)


@UnknownRestart
def Event5200(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """ 5200: Event 5200 """
    SkipLinesIfFlagOn(6, arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SetDisplayMask(arg_0_3, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_9_9, switch_type=OnOffChange.On)


@UnknownRestart
def Event5201(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_17: short, arg_18_19: short):
    """ 5201: Event 5201 """
    DisableObject(arg_8_11)
    DisableObject(arg_12_15)
    EndIfFlagOn(arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_8_11, character=arg_0_3, model_point=arg_16_17)
    MoveObjectToCharacter(arg_12_15, character=arg_0_3, model_point=arg_18_19)
    DestroyObject(arg_8_11)
    DestroyObject(arg_12_15)


@UnknownRestart
def Event5202(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 5202: Event 5202 """
    EndIfFlagOn(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
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


@RestartOnRest
def Event11415210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11415210: Event 11415210 """
    IfTrueFlagCountGreaterThanOrEqual(0, arg_8_11, (arg_0_3, arg_4_7))
    DisableSoundEvent(1413806)


@RestartOnRest
def Event11415250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11415250: Event 11415250 """
    SkipLinesIfThisEventSlotOff(2)
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


def Event11410350():
    """ 11410350: Event 11410350 """
    SkipLinesIfThisEventOff(5)
    DisableObject(1411350)
    PostDestruction(1411351)
    EndOfAnimation(1411600, 116)
    EnableTreasure(1411600)
    End()
    DisableObject(1411351)
    DisableTreasure(1411600)
    CreateObjectVFX(99010, obj=1411600, model_point=90)
    ForceAnimation(1411600, 115, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=1412350)
    IfObjectDestroyed(-1, 1411350)
    IfConditionTrue(0, input_condition=-1)
    DisableObject(1411350)
    EnableObject(1411351)
    CreateTemporaryVFX(140001, anchor_entity=1411351, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=1411351, sound_type=SoundType.o_Object, sound_id=481000001)
    DestroyObject(1411351)
    ForceAnimation(1411600, 116, wait_for_completion=True)
    EnableTreasure(1411600)
    DeleteObjectVFX(1411600, erase_root=True)


@RestartOnRest
def Event11410100(_, arg_0_3: int):
    """ 11410100: Event 11410100 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=1410110)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33002000, host_only=True)


@RestartOnRest
def Event11410150(_, arg_0_3: int, arg_4_7: int):
    """ 11410150: Event 11410150 """
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    EndIfConditionFalse(-1)
    AwardItemLot(arg_4_7, host_only=True)


@RestartOnRest
def Event800(_, arg_0_3: int):
    """ 800: Event 800 """
    SkipLinesIfThisEventSlotOff(3)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11410600(_, arg_0_3: int, arg_4_7: int):
    """ 11410600: Event 11410600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11410260():
    """ 11410260: Event 11410260 """
    DisableNetworkSync()
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfTimeElapsed(1, 3.0)
    IfConditionTrue(0, input_condition=1)
    ActivateKillplaneForModel(game_map=LOST_IZALITH, y_threshold=-400.0, target_model_id=3240)
    Restart()


def Event11410510(_, arg_0_3: int, arg_4_7: int):
    """ 11410510: Event 11410510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
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
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11410520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410520: Event 11410520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410501(_, arg_0_3: int, arg_4_7: int):
    """ 11410501: Event 11410501 """
    IfFlagOn(-2, 1503)
    IfFlagOn(-2, 1505)
    IfFlagOn(-2, 1506)
    IfFlagOn(-2, 1507)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
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
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11410530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410530: Event 11410530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfFlagOn(1, 11410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11410531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410531: Event 11410531 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1009)
    IfFlagOff(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    EnableCharacter(6004)
    SetTeamTypeAndExitStandbyAnimation(6004, TeamType.HostileAlly)
    SaveRequest()


def Event11410532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410532: Event 11410532 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1009)
    IfFlagOn(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1412500, destination_type=CoordEntityType.Region, set_draw_parent=1413000)
    EnableFlag(11410580)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetNest(arg_0_3, 1412500)


def Event11410533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410533: Event 11410533 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1003)
    IfFlagOn(1, 11410595)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1004)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11410534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410534: Event 11410534 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1002)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410540: Event 11410540 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1502)
    IfFlagOn(1, 11400590)
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(814)


def Event11410541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410541: Event 11410541 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1503)
    IfCharacterAlive(-1, 1410410)
    IfCharacterAlive(-1, 1410411)
    IfCharacterAlive(-1, 1410412)
    IfCharacterAlive(-1, 1410413)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11410590)
    IfFlagOff(2, 1512)
    IfFlagOn(2, 1504)
    IfThisEventOn(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ResetStandbyAnimationSettings(arg_0_3)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.FightingAlly)
    AddSpecialEffect(arg_0_3, 90111)


def Event11410542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410542: Event 11410542 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1503)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410543: Event 11410543 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1504)
    IfHealthLessThan(1, arg_0_3, 0.5)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, 1412360)


def Event11410544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410544: Event 11410544 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1504)
    IfHealthGreaterThanOrEqual(1, arg_0_3, 0.5)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, 1412360)


def Event11410545(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410545: Event 11410545 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1506)
    IfFlagOn(1, 11410591)
    IfThisEventOff(1)
    IfFlagOff(2, 1512)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionTrue(3, 2)
    Kill(arg_0_3, award_souls=True)
    CancelSpecialEffect(arg_0_3, 90111)
    End()
    DropMandatoryTreasure(arg_0_3)


def Event11410546(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410546: Event 11410546 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfFlagOff(1, 1506)
    IfFlagOff(1, 1508)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410547(_, arg_0_3: int):
    """ 11410547: Event 11410547 """
    EndIfFlagOn(1512)
    SkipLinesIfThisEventSlotOff(3)
    SkipLinesIfFlagOn(1, 11410593)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfThisEventOn(-1)
    IfFlagOn(-1, 1503)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventOn(1)
    IfFlagOff(0, 814)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7856)


def Event11410548(_, arg_0_3: int):
    """ 11410548: Event 11410548 """
    EndIfFlagOn(1512)
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)
    End()
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410593)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)


def Event11410549(_, arg_0_3: int):
    """ 11410549: Event 11410549 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410594)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11410550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410550: Event 11410550 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1505)
    IfFlagOn(1, 11410594)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11415030():
    """ 11415030: Event 11415030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6542, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11415033)
    IfClient(2)
    IfFlagOn(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6542)
    EndIfFlagOn(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfCharacterBackreadEnabled(1, 6542)
    IfEntityWithinDistance(1, 6542, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6542, region=1412000, summon_flag=11415031, dismissal_flag=11415033)


def Event11415029():
    """ 11415029: Event 11415029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6542, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11415033)
    IfClient(2)
    IfFlagOn(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6542)
    EndIfFlagOn(10)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11415031)
    IfFlagOff(1, 11415033)
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfCharacterBackreadEnabled(1, 6542)
    IfEntityWithinDistance(1, 6542, PLAYER, radius=20.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6542, region=1412000, summon_flag=11415031, dismissal_flag=11415033)


def Event14015990(_, arg_0_3: int, arg_4_7: int):
    """ 14015990: Event 14015990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11415032():
    """ 11415032: Event 11415032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11415031)
    IfFlagOn(1, 11415383)
    IfConditionTrue(0, input_condition=1)
    AICommand(6542, command_id=10, slot=0)
    ReplanAI(6542)
    IfCharacterInsideRegion(0, 6542, region=1412898)
    RotateToFaceEntity(6542, 1412897)
    ForceAnimation(6542, 7410)
    AICommand(6542, command_id=-1, slot=0)
    ReplanAI(6542)


def Event11415035():
    """ 11415035: Event 11415035 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11415036)
    EndIfFlagOn(11410410)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11410810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412010)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6560, region=1412001, summon_flag=11415036, dismissal_flag=11415037)
    Wait(20.0)
    Restart()


def Event11415038():
    """ 11415038: Event 11415038 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11415039)
    EndIfFlagOn(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11410811)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412520)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6561, region=1412002, summon_flag=11415039, dismissal_flag=11415040)
    Wait(20.0)
    Restart()


def Event11410810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11410810: Event 11410810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_8_11)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_0_3)
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11415843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11415843: Event 11415843 """
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOn(1, arg_0_3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_4_7,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


def Event11415846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11415846: Event 11415846 """
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateVFX(arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=True)
    Restart()
