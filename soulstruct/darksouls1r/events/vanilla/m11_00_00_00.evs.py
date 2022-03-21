"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11100992, obj=1101960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11100010, stop_climbing_flag=11100011, obj=1101140)
    RegisterLadder(start_climbing_flag=11100014, stop_climbing_flag=11100015, obj=1101142)
    RegisterLadder(start_climbing_flag=11100016, stop_climbing_flag=11100017, obj=1101143)
    SkipLinesIfClient(1)
    DisableFlag(11100410)
    SkipLinesIfFlagOn(2, 11100810)
    DisableTreasure(1101610)
    DisableObject(1101610)
    SkipLinesIfFlagOff(1, 11100810)
    EnableTreasure(1101610)
    RunEvent(11100090, slot=1, args=(1101702, 1101703, 1102602, 1102603))
    RunEvent(11105070)
    RunEvent(11105071)
    RunEvent(11105072)
    RunEvent(11105399)
    RunEvent(11100030)
    RunEvent(11100031)
    RunEvent(11100136)
    RunEvent(11100135)
    RunEvent(11100120, slot=0, args=(11100120, 10010868, 1101250))
    RunEvent(11100710)
    RunEvent(11100200)
    RunEvent(11100600, slot=0, args=(1101650, 11100650))
    RunEvent(11105150, slot=0, args=(1100100,))
    RunEvent(11105150, slot=1, args=(1100101,))
    RunEvent(11105150, slot=2, args=(1100102,))
    RunEvent(11105160, slot=0, args=(1100104, 1102006))
    RunEvent(11105160, slot=1, args=(1100105, 1102001))
    RunEvent(11105170, slot=0, args=(1100130, 1102202, 0.20000000298023224), arg_types="iif")
    RunEvent(11105170, slot=1, args=(1100132, 1102202, 0.0), arg_types="iif")
    RunEvent(11105170, slot=2, args=(1100135, 1102202, 0.4000000059604645), arg_types="iif")
    RunEvent(11105170, slot=3, args=(1100136, 1102202, 0.6000000238418579), arg_types="iif")
    RunEvent(11105170, slot=4, args=(1100137, 1102007, 0.30000001192092896), arg_types="iif")
    RunEvent(11105170, slot=5, args=(1100138, 1102007, 0.0), arg_types="iif")
    RunEvent(11106299)
    RunEvent(11106200, slot=0, args=(1101011, 1101011, 12, 4294967295))
    RunEvent(11106200, slot=1, args=(1101012, 1101012, 13, 11006200))
    RunEvent(11106200, slot=2, args=(1101013, 1101011, 12, 11006200))
    RunEvent(11106200, slot=3, args=(1101014, 1101014, 13, 11006200))
    RunEvent(11106200, slot=4, args=(1101015, 1101016, 12, 11006205))
    RunEvent(11106200, slot=5, args=(1101016, 1101016, 13, 4294967295))
    RunEvent(11106200, slot=6, args=(1101017, 1101016, 12, 11006205))
    RunEvent(11106200, slot=7, args=(1101018, 1101018, 13, 4294967295))
    RunEvent(11106200, slot=8, args=(1101019, 1101019, 13, 4294967295))
    RunEvent(11106200, slot=9, args=(1101020, 1101020, 12, 4294967295))
    RunEvent(11106200, slot=13, args=(1101024, 1101024, 13, 4294967295))
    RunEvent(11106200, slot=14, args=(1101025, 1101025, 12, 4294967295))
    RunEvent(11106200, slot=18, args=(1101029, 1101029, 12, 4294967295))
    RunEvent(11106200, slot=19, args=(1101030, 1101030, 13, 4294967295))
    RunEvent(11106200, slot=24, args=(1101035, 1101035, 12, 4294967295))
    RunEvent(11106200, slot=27, args=(1101038, 1101038, 12, 4294967295))
    RunEvent(11106200, slot=28, args=(1101039, 1101039, 13, 4294967295))
    RunEvent(11106200, slot=29, args=(1101040, 1101040, 12, 4294967295))
    RunEvent(11106200, slot=30, args=(1101041, 1101041, 12, 4294967295))
    RunEvent(11106200, slot=31, args=(1101042, 1101042, 13, 4294967295))
    RunEvent(11106200, slot=32, args=(1101043, 1101043, 12, 4294967295))
    RunEvent(11106200, slot=33, args=(1101044, 1101044, 12, 4294967295))
    RunEvent(11100070, slot=0, args=(1101120, 1101600, 120, 121))
    RunEvent(11100070, slot=1, args=(1101121, 1101601, 125, 126))
    SkipLinesIfFlagOff(1, 11100400)
    DisableCharacter(1100170)
    RunEvent(11105370)
    RunEvent(11100100, slot=0, args=(1101180, 1103000))
    RunEvent(11100100, slot=1, args=(1101181, 1103001))
    RunEvent(11100400)
    RunEvent(11105371)
    DisableSoundEvent(1103800)
    DisableObject(1101992)
    DeleteVFX(1101993, erase_root_only=False)
    SkipLinesIfFlagOff(4, 4)
    RunEvent(11105392)
    DisableObject(1101990)
    DeleteVFX(1101991, erase_root_only=False)
    SkipLines(10)
    RunEvent(11105390)
    RunEvent(11105391)
    RunEvent(11105393)
    RunEvent(11105392)
    RunEvent(11100000)
    RunEvent(11105394)
    RunEvent(11105395)
    RunEvent(11105396)
    RunEvent(11105397)
    RunEvent(11105398)
    RunEvent(11105843, slot=0, args=(4, 1101990, 1102998, 1102997))
    RunEvent(11105846, slot=0, args=(4, 1101990, 1101991))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11100420)
    HumanityRegistration(6570, 8964)
    RunEvent(11105030)
    RunEvent(11100810)
    RunEvent(11105010)
    SkipLinesIfFlagOn(1, 1691)
    SetTeamType(1100160, TeamType.Ally)
    RunEvent(11100530, slot=0, args=(1100160, 1690, 1693, 1691))
    RunEvent(11100531, slot=0, args=(1100160, 1690, 1693, 1692))
    HumanityRegistration(6312, 8470)
    HumanityRegistration(6422, 8900)
    DisableCharacter(6312)
    DisableCharacter(6422)
    RunEvent(11100040)
    RunEvent(11100532, slot=0, args=(6312, 1600, 1619, 1606, 1607, 6422))
    RunEvent(11100533, slot=0, args=(6312, 1600, 1619, 1608))
    RunEvent(11100534, slot=0, args=(6312, 1600, 1619, 1609))
    RunEvent(11100535, slot=0, args=(6312, 1600, 1619, 1608, 1609))
    RunEvent(11100300)


def Event11100090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100090: Event 11100090 """
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
def Event11105070():
    """ 11105070: Event 11105070 """
    EndIfThisEventOn()
    DisableCharacter(1100900)
    DisableCharacter(1100901)
    DisableCharacter(1100902)
    DisableCharacter(1100903)
    DisableCharacter(1100904)
    DisableCharacter(1100905)
    DisableCharacter(1100906)
    DisableCharacter(1100907)
    DisableCharacter(1100908)
    DisableCharacter(1100909)
    DisableCharacter(1100910)
    DisableCharacter(1100911)
    IfFlagOn(0, 11100050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1100900)
    EnableCharacter(1100901)
    EnableCharacter(1100902)
    EnableCharacter(1100903)
    EnableCharacter(1100904)
    EnableCharacter(1100905)
    EnableCharacter(1100906)
    EnableCharacter(1100907)
    EnableCharacter(1100908)
    EnableCharacter(1100909)
    EnableCharacter(1100910)
    EnableCharacter(1100911)


@RestartOnRest
def Event11105071():
    """ 11105071: Event 11105071 """
    IfFlagOn(-1, 11105075)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11100050)
    DisableFlag(11105075)
    EnableFlag(5001)
    Kill(1100900, award_souls=False)
    Kill(1100901, award_souls=False)
    Kill(1100902, award_souls=False)
    Kill(1100903, award_souls=False)
    Kill(1100904, award_souls=False)
    Kill(1100905, award_souls=False)
    Kill(1100906, award_souls=False)
    Kill(1100907, award_souls=False)
    Kill(1100908, award_souls=False)
    Kill(1100909, award_souls=False)
    Kill(1100910, award_souls=False)
    Kill(1100911, award_souls=False)


@RestartOnRest
def Event11105072():
    """ 11105072: Event 11105072 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=PAINTED_WORLD)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11100050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=PAINTED_WORLD)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11100050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=PAINTED_WORLD)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11100050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=PAINTED_WORLD)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11100050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=PAINTED_WORLD)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11100050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=PAINTED_WORLD)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11100050)
    RestartIfConditionFalse(-6)
    EnableFlag(11100050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=PAINTED_WORLD)
    RestartIfConditionFalse(7)
    DisableFlag(11100050)
    EnableFlag(11105075)


def Event11105390():
    """ 11105390: Event 11105390 """
    IfFlagOff(1, 4)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1102998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1101990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1102997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11105391():
    """ 11105391: Event 11105391 """
    IfFlagOff(1, 4)
    IfFlagOn(1, 11105393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1102998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1101990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1102997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11105393():
    """ 11105393: Event 11105393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 4)
    IfCharacterInsideRegion(1, PLAYER, region=1102996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1100160)
    EnableFlag(11105393)
    IfFlagOn(0, 4)
    End()


@RestartOnRest
def Event11105392():
    """ 11105392: Event 11105392 """
    SkipLinesIfFlagOff(7, 4)
    DisableCharacter(1100160)
    DisableCharacter(1100161)
    Kill(1100160, award_souls=False)
    Kill(1100161, award_souls=False)
    DisableBackread(1100160)
    DisableBackread(1100161)
    End()
    SkipLinesIfFlagOff(1, 1691)
    SetTeamType(1100160, TeamType.Ally)
    DisableAI(1100160)
    DisableHealthBar(1100160)
    IfCharacterAlive(1, 1100160)
    IfFlagOn(1, 11105393)
    IfAttacked(1, 1100160, attacker=PLAYER)
    IfFlagOn(2, 11105393)
    IfCharacterInsideRegion(2, PLAYER, region=1102100)
    IfFlagOn(2, 1691)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1100160)
    SetTeamType(1100160, TeamType.Boss)
    EnableBossHealthBar(1100160, name=2730, slot=0)
    EnableFlag(11105392)
    IfFlagOn(0, 4)
    End()


def Event11100000():
    """ 11100000: Event 11100000 """
    EndIfThisEventOn()
    IfCharacterDead(0, 1100160)
    EnableFlag(4)
    KillBoss(1100160)
    SkipLinesIfClient(1)
    AwardAchievement(40)
    Kill(1100161, award_souls=False)
    DisableBackread(1100161)
    DisableObject(1101990)
    DeleteVFX(1101991, erase_root_only=True)


def Event11105394():
    """ 11105394: Event 11105394 """
    DisableNetworkSync()
    IfFlagOff(1, 4)
    IfFlagOn(1, 11105390)
    IfCharacterInsideRegion(1, PLAYER, region=1102996)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11105391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1103800)
    EnableFlag(11105394)
    IfFlagOn(0, 4)
    End()


def Event11105395():
    """ 11105395: Event 11105395 """
    DisableNetworkSync()
    IfFlagOn(1, 4)
    IfCharacterInsideRegion(1, PLAYER, region=1102100)
    IfFlagOn(2, 11105380)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(1103800)
    EnableFlag(11105395)
    IfFlagOn(0, 4)
    End()


@RestartOnRest
def Event11105396():
    """ 11105396: Event 11105396 """
    DisableCharacter(1100161)
    EndIfFlagOn(4)
    SkipLinesIfThisEventOff(3)
    SetDisplayMask(1100160, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1100160, bit_index=1, switch_type=OnOffChange.Off)
    End()
    IfCharacterBackreadEnabled(0, 1100160)
    CreateNPCPart(
        1100160,
        npc_part_id=2730,
        part_index=NPCPartType.Part1,
        part_health=158,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfHealthGreaterThan(1, 1100160, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, 1100160, npc_part_id=2730, value=0)
    IfFlagOff(1, 11105381)
    IfAttacked(1, 1100160, attacker=PLAYER)
    IfHealthLessThanOrEqual(2, 1100160, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(1100160, disable_interpolation=False)
    ForceAnimation(1100160, 8000)
    IfHasTAEEvent(0, 1100160, tae_event_id=400)
    EnableCharacter(1100161)
    SetDisplayMask(1100160, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1100160, bit_index=1, switch_type=OnOffChange.Off)
    Move(
        1100161,
        destination=1100160,
        destination_type=CoordEntityType.Character,
        model_point=40,
        copy_draw_parent=1100160,
    )
    ForceAnimation(1100161, 8100)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    SkipLinesIfConditionFalse(1, -7)
    AwardItemLot(27310000, host_only=True)
    EnableFlag(11105396)
    IfFlagOn(0, 4)
    End()


@RestartOnRest
def Event11105397():
    """ 11105397: Event 11105397 """
    IfHasTAEEvent(0, 1100160, tae_event_id=600)
    DisableHealthBar(1100160)
    DisableBossHealthBar(1100160, name=2730, slot=0)
    EnableFlag(11105381)
    DisableFlagRange((11105110, 11105119))
    SkipLinesIfClient(44)
    SetNetworkUpdateAuthority(1100160, UpdateAuthority.Forced)
    EnableRandomFlagInRange((11105110, 11105119))
    SkipLinesIfFlagOff(3, 11105110)
    IfCharacterInsideRegion(1, 1100160, region=1102810)
    SkipLinesIfConditionTrue(2, 1)
    Move(1100160, destination=1102810, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105111)
    IfCharacterInsideRegion(2, 1100160, region=1102811)
    SkipLinesIfConditionTrue(2, 2)
    Move(1100160, destination=1102811, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105112)
    IfCharacterInsideRegion(3, 1100160, region=1102812)
    SkipLinesIfConditionTrue(2, 3)
    Move(1100160, destination=1102812, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105113)
    IfCharacterInsideRegion(4, 1100160, region=1102813)
    SkipLinesIfConditionTrue(2, 4)
    Move(1100160, destination=1102813, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105114)
    IfCharacterInsideRegion(5, 1100160, region=1102814)
    SkipLinesIfConditionTrue(2, 5)
    Move(1100160, destination=1102814, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105115)
    IfCharacterInsideRegion(6, 1100160, region=1102815)
    SkipLinesIfConditionTrue(2, 6)
    Move(1100160, destination=1102815, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105116)
    IfCharacterInsideRegion(7, 1100160, region=1102816)
    SkipLinesIfConditionTrue(2, 7)
    Move(1100160, destination=1102816, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105117)
    IfCharacterInsideRegion(-1, 1100160, region=1102817)
    SkipLinesIfConditionTrue(2, -1)
    Move(1100160, destination=1102817, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105118)
    IfCharacterInsideRegion(-2, 1100160, region=1102818)
    SkipLinesIfConditionTrue(2, -2)
    Move(1100160, destination=1102818, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagOff(3, 11105119)
    IfCharacterInsideRegion(-3, 1100160, region=1102819)
    SkipLinesIfConditionTrue(2, -3)
    Move(1100160, destination=1102819, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(1100160, destination=1102810, destination_type=CoordEntityType.Region, short_move=True)
    IfDoesNotHaveTAEEvent(0, 1100160, tae_event_id=600)
    Restart()


@RestartOnRest
def Event11105398():
    """ 11105398: Event 11105398 """
    DisableNetworkSync()
    IfHasTAEEvent(0, 1100160, tae_event_id=700)
    EnableHealthBar(1100160)
    EnableBossHealthBar(1100160, name=2730, slot=0)
    DisableFlag(11105381)
    IfDoesNotHaveTAEEvent(0, 1100160, tae_event_id=700)
    Restart()


def Event11105399():
    """ 11105399: Event 11105399 """
    EndIfClient()
    DisableNetworkSync()
    IfInsideMap(0, game_map=ANOR_LONDO)
    IfInsideMap(0, game_map=PAINTED_WORLD)
    RestartEvent(11105390)
    RestartEvent(11105391)
    RestartEvent(11105392)
    RestartEvent(11105393)
    RestartEvent(11105394)
    RestartEvent(11105395)
    RestartEvent(11105396)
    RestartEvent(11105397)
    RestartEvent(11105398)
    DisableFlagRange((11105390, 11105399))
    Restart()


@RestartOnRest
def Event11105150(_, arg_0_3: int):
    """ 11105150: Event 11105150 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=5.0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11105160(_, arg_0_3: int, arg_4_7: int):
    """ 11105160: Event 11105160 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11105170(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11105170: Event 11105170 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11106200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11106200: Event 11106200 """
    DisableNetworkSync()
    SkipLinesIfEqual(1, left=arg_12_15, right=-1)
    IfFlagOn(-1, arg_12_15)
    IfEntityWithinDistance(-1, PLAYER, arg_4_7, radius=7.0)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    DisableObject(arg_0_3)


@RestartOnRest
def Event11106299():
    """ 11106299: Event 11106299 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1102000)
    RunEvent(11106298, slot=-1, args=(1101300, 13))
    RunEvent(11106298, slot=-1, args=(1101301, 12))
    RunEvent(11106298, slot=-1, args=(1101302, 12))
    RunEvent(11106298, slot=-1, args=(1101303, 13))
    RunEvent(11106298, slot=-1, args=(1101304, 12))
    RunEvent(11106298, slot=-1, args=(1101305, 12))
    RunEvent(11106298, slot=-1, args=(1101306, 13))
    RunEvent(11106298, slot=-1, args=(1101307, 12))
    RunEvent(11106298, slot=-1, args=(1101308, 12))
    RunEvent(11106298, slot=-1, args=(1101309, 13))
    RunEvent(11106298, slot=-1, args=(1101310, 12))
    RunEvent(11106298, slot=-1, args=(1101311, 12))


@UnknownRestart
def Event11106298(_, arg_0_3: int, arg_4_7: int):
    """ 11106298: Event 11106298 """
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    DisableObject(arg_0_3)


def Event11100070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100070: Event 11100070 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_4_7, arg_12_15)
    PostDestruction(arg_0_3)
    EnableTreasure(arg_4_7)
    End()
    DisableTreasure(arg_4_7)
    SkipLinesIfClient(1)
    CreateObjectVFX(99005, obj=arg_4_7, model_point=90)
    ForceAnimation(arg_4_7, arg_8_11, loop=True)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableTreasure(arg_4_7)


@RestartOnRest
def Event11105370():
    """ 11105370: Event 11105370 """
    SkipLinesIfFlagOff(2, 11100410)
    ResetStandbyAnimationSettings(1100170)
    End()
    IfCharacterType(3, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=3)
    IfCharacterInsideRegion(1, PLAYER, region=1102070)
    IfConditionFalse(2, input_condition=3)
    IfAttacked(2, 1100170, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(11100410)
    ResetStandbyAnimationSettings(1100170)
    ForceAnimation(1100170, 9060)
    PlaySoundEffect(anchor_entity=1102080, sound_type=SoundType.a_Ambient, sound_id=110003420)


@RestartOnRest
def Event11105371():
    """ 11105371: Event 11105371 """
    DisableCharacter(1100172)
    SkipLinesIfThisEventOff(4)
    IfCharacterBackreadEnabled(0, 1100170)
    SetDisplayMask(1100170, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(1100170, bit_index=1, switch_type=OnOffChange.On)
    End()
    IfHasTAEEvent(0, 1100170, tae_event_id=400)
    SetDisplayMask(1100170, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(1100170, bit_index=1, switch_type=OnOffChange.On)
    Move(
        1100172,
        destination=1100170,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=1100170,
    )
    EnableCharacter(1100172)
    ForceAnimation(1100172, 8100, wait_for_completion=True)
    DisableCharacter(1100172)


def Event11100100(_, arg_0_3: int, arg_4_7: int):
    """ 11100100: Event 11100100 """
    SkipLinesIfThisEventSlotOff(4)
    DestroyObject(arg_0_3)
    ForceAnimation(arg_0_3, 0)
    DeleteVFX(arg_4_7, erase_root_only=False)
    End()
    IfObjectDestroyed(0, arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11100400():
    """ 11100400: Event 11100400 """
    EnableImmortality(1100171)
    EnableInvincibility(1100171)
    DisableHealthBar(1100171)
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1100170)
    End()
    SetBackreadStateAlternate(1100170, state=True)
    DisableGravity(1100170)
    IfCharacterDead(0, 1100170)
    EnableFlag(11100400)


def Event11100030():
    """ 11100030: Event 11100030 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(1101130, 2)
    DisableNavmeshType(1102040, NavmeshType.Solid)
    End()
    EnableNavmeshType(1102040, NavmeshType.Solid)
    IfFlagOff(1, 11100700)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1101130,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1102090, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1101130, 1, wait_for_completion=True)
    DisableNavmeshType(1102040, NavmeshType.Solid)


def Event11100031():
    """ 11100031: Event 11100031 """
    DisableNetworkSync()
    IfFlagOff(1, 11100030)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1101130,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=1101130,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11100120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11100120: Event 11100120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11100135():
    """ 11100135: Event 11100135 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(1101160, 1)
    EndOfAnimation(1101170, 1)
    DisableNavmeshType(1102041, NavmeshType.Solid)
    End()
    IfActionButton(
        0,
        prompt_text=10010503,
        anchor_entity=1101150,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    DisableObject(1101018)
    DisableObject(1101019)
    DisableObject(1101020)
    Move(PLAYER, destination=1101150, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8010)
    ForceAnimation(1101150, 1, wait_for_completion=True)
    SkipLinesIfSingleplayer(2)
    PlayCutscene(110000, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(110000, skippable=True, fade_out=False, player_id=PLAYER)
    ForceAnimation(1101160, 1)
    ForceAnimation(1101170, 1)
    DisableNavmeshType(1102041, NavmeshType.Solid)


def Event11100136():
    """ 11100136: Event 11100136 """
    DisableNetworkSync()
    IfFlagOff(1, 11100135)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1101170,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010160,
        anchor_entity=1101170,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11100420():
    """ 11100420: Event 11100420 """
    SkipLinesIfThisEventOff(3)
    Move(1100180, destination=1102201, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1100180, 1102201)
    End()
    DisableAI(1100180)
    IfCharacterInsideRegion(-1, PLAYER, region=1102200)
    IfAttacked(-1, 1100180, attacker=PLAYER)
    IfAttacked(-1, 1100130, attacker=PLAYER)
    IfAttacked(-1, 1100132, attacker=PLAYER)
    IfAttacked(-1, 1100135, attacker=PLAYER)
    IfAttacked(-1, 1100136, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(1100180, 500)
    EnableAI(1100180)
    SetNest(1100180, 1102201)


def Event11100710():
    """ 11100710: Event 11100710 """
    DisableFlag(11105380)
    IfHost(1)
    IfFlagOff(1, 1691)
    IfCharacterInsideRegion(1, PLAYER, region=1102500)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(1100160)
    EndIfClient()
    DisableImmortality(1100160)
    EnableFlag(11105380)
    SkipLinesIfFlagOn(1, 4)
    IfFlagOn(0, 11105395)
    SkipLinesIfFlagOff(1, 11510400)
    SetMapDrawParamSlot(15, slot=2)
    PlayCutscene(
        110035,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1512500,
        move_to_map=ANOR_LONDO,
    )
    WaitFrames(1)
    SkipLinesIfThisEventOn(1)
    AwardItemLot(9030, host_only=True)
    SetRespawnPoint(1512960)
    SaveRequest()
    Restart()


@RestartOnRest
def Event11105010():
    """ 11105010: Event 11105010 """
    EndIfThisEventOn()
    IfCharacterAlive(1, 1100200)
    IfCharacterAlive(1, 1100201)
    IfCharacterAlive(1, 1100202)
    IfCharacterAlive(1, 1100203)
    IfCharacterAlive(1, 1100204)
    IfCharacterAlive(1, 1100205)
    IfCharacterAlive(1, 1100206)
    IfCharacterAlive(1, 1100207)
    IfCharacterAlive(1, 1100208)
    IfCharacterAlive(1, 1100209)
    IfCharacterAlive(1, 1100210)
    IfCharacterAlive(1, 1100211)
    IfCharacterAlive(1, 1100212)
    IfCharacterAlive(1, 1100213)
    EndIfConditionFalse(1)
    DisableCharacterCollision(1100200)
    DisableCharacterCollision(1100201)
    DisableCharacterCollision(1100202)
    DisableCharacterCollision(1100203)
    DisableCharacterCollision(1100204)
    DisableCharacterCollision(1100205)
    DisableCharacterCollision(1100206)
    DisableCharacterCollision(1100207)
    DisableCharacterCollision(1100208)
    DisableCharacterCollision(1100209)
    DisableCharacterCollision(1100210)
    DisableCharacterCollision(1100211)
    DisableCharacterCollision(1100212)
    DisableCharacterCollision(1100213)
    DisableAnimations(1100200)
    DisableAnimations(1100201)
    DisableAnimations(1100202)
    DisableAnimations(1100203)
    DisableAnimations(1100204)
    DisableAnimations(1100205)
    DisableAnimations(1100206)
    DisableAnimations(1100207)
    DisableAnimations(1100208)
    DisableAnimations(1100209)
    DisableAnimations(1100210)
    DisableAnimations(1100211)
    DisableAnimations(1100212)
    DisableAnimations(1100213)
    DisableGravity(1100200)
    DisableGravity(1100201)
    DisableGravity(1100202)
    DisableGravity(1100203)
    DisableGravity(1100204)
    DisableGravity(1100205)
    DisableGravity(1100206)
    DisableGravity(1100207)
    DisableGravity(1100208)
    DisableGravity(1100209)
    DisableGravity(1100210)
    DisableGravity(1100211)
    DisableGravity(1100212)
    DisableGravity(1100213)
    DisableAI(1100200)
    DisableAI(1100201)
    DisableAI(1100202)
    DisableAI(1100203)
    DisableAI(1100204)
    DisableAI(1100205)
    DisableAI(1100206)
    DisableAI(1100207)
    DisableAI(1100208)
    DisableAI(1100209)
    DisableAI(1100210)
    DisableAI(1100211)
    DisableAI(1100212)
    DisableAI(1100213)
    SetStandbyAnimationSettings(1100200, standby_animation=9000)
    SetStandbyAnimationSettings(1100201, standby_animation=9000)
    SetStandbyAnimationSettings(1100202, standby_animation=9000)
    SetStandbyAnimationSettings(1100203, standby_animation=9000)
    SetStandbyAnimationSettings(1100204, standby_animation=9000)
    SetStandbyAnimationSettings(1100205, standby_animation=9000)
    SetStandbyAnimationSettings(1100206, standby_animation=9000)
    SetStandbyAnimationSettings(1100207, standby_animation=9000)
    SetStandbyAnimationSettings(1100208, standby_animation=9000)
    SetStandbyAnimationSettings(1100209, standby_animation=9000)
    SetStandbyAnimationSettings(1100210, standby_animation=9000)
    SetStandbyAnimationSettings(1100211, standby_animation=9000)
    SetStandbyAnimationSettings(1100212, standby_animation=9000)
    SetStandbyAnimationSettings(1100213, standby_animation=9000)
    Move(1100200, destination=1102830, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100201, destination=1102831, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100202, destination=1102832, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100203, destination=1102833, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100204, destination=1102834, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100205, destination=1102835, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100206, destination=1102836, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100207, destination=1102837, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100208, destination=1102838, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100209, destination=1102839, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100210, destination=1102840, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100211, destination=1102841, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100212, destination=1102842, destination_type=CoordEntityType.Region, short_move=True)
    Move(1100213, destination=1102843, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterInsideRegion(0, PLAYER, region=1102300)
    EnableAI(1100200)
    EnableAI(1100201)
    EnableAI(1100202)
    EnableAI(1100203)
    EnableAI(1100204)
    EnableAI(1100205)
    EnableAI(1100206)
    EnableAI(1100207)
    EnableAI(1100208)
    EnableAI(1100209)
    EnableAI(1100210)
    EnableAI(1100211)
    EnableAI(1100212)
    EnableAI(1100213)
    ResetStandbyAnimationSettings(1100200)
    ResetStandbyAnimationSettings(1100201)
    ResetStandbyAnimationSettings(1100202)
    ResetStandbyAnimationSettings(1100203)
    ResetStandbyAnimationSettings(1100204)
    ResetStandbyAnimationSettings(1100205)
    ResetStandbyAnimationSettings(1100206)
    ResetStandbyAnimationSettings(1100207)
    ResetStandbyAnimationSettings(1100208)
    ResetStandbyAnimationSettings(1100209)
    ResetStandbyAnimationSettings(1100210)
    ResetStandbyAnimationSettings(1100211)
    ResetStandbyAnimationSettings(1100212)
    ResetStandbyAnimationSettings(1100213)
    EnableGravity(1100200)
    EnableGravity(1100201)
    EnableGravity(1100202)
    EnableGravity(1100203)
    EnableGravity(1100204)
    EnableGravity(1100205)
    EnableGravity(1100206)
    EnableGravity(1100207)
    EnableGravity(1100208)
    EnableGravity(1100209)
    EnableGravity(1100210)
    EnableGravity(1100211)
    EnableGravity(1100212)
    EnableGravity(1100213)
    EnableAnimations(1100200)
    EnableAnimations(1100201)
    EnableAnimations(1100202)
    EnableAnimations(1100203)
    EnableAnimations(1100204)
    EnableAnimations(1100205)
    EnableAnimations(1100206)
    EnableAnimations(1100207)
    EnableAnimations(1100208)
    EnableAnimations(1100209)
    EnableAnimations(1100210)
    EnableAnimations(1100211)
    EnableAnimations(1100212)
    EnableAnimations(1100213)
    EnableCharacterCollision(1100200)
    EnableCharacterCollision(1100201)
    EnableCharacterCollision(1100202)
    EnableCharacterCollision(1100203)
    EnableCharacterCollision(1100204)
    EnableCharacterCollision(1100205)
    EnableCharacterCollision(1100206)
    EnableCharacterCollision(1100207)
    EnableCharacterCollision(1100208)
    EnableCharacterCollision(1100209)
    EnableCharacterCollision(1100210)
    EnableCharacterCollision(1100211)
    EnableCharacterCollision(1100212)
    EnableCharacterCollision(1100213)


@RestartOnRest
def Event11100200():
    """ 11100200: Event 11100200 """
    RunEvent(11105190, slot=0, args=(1100300, 3010, 3011, 11105230, 11105232))
    RunEvent(11105190, slot=1, args=(1100301, 3012, 3013, 11105234, 11105236))
    RunEvent(11105195, slot=0, args=(1100302, 11105240))
    RunEvent(11105195, slot=1, args=(1100303, 11105244))
    RunEvent(11105200, slot=0, args=(11105190, 11105210, 0, 11105250, 11105230, 11105231, 11105232, 11105233))
    RunEvent(11105200, slot=1, args=(11105191, 11105211, 1, 11105260, 11105234, 11105235, 11105236, 11105237))
    RunEvent(11105200, slot=2, args=(11105195, 11105212, 2, 11105270, 11105238, 11105239, 11105240, 11105241))
    RunEvent(11105200, slot=3, args=(11105196, 11105213, 3, 11105280, 11105242, 11105243, 11105244, 11105245))
    RunEvent(11105220, slot=0, args=(1100300, 11105210, 10.0, 11105250), arg_types="iifi")
    RunEvent(11105220, slot=1, args=(1100301, 11105211, 10.0, 11105260), arg_types="iifi")
    RunEvent(11105220, slot=2, args=(1100302, 11105212, 10.0, 11105270), arg_types="iifi")
    RunEvent(11105220, slot=3, args=(1100303, 11105213, 10.0, 11105280), arg_types="iifi")
    RunEvent(11105250, slot=0, args=(11105210, 1100300, 1, 1102040, 11105230, 11105233, 11105232))
    RunEvent(11105250, slot=1, args=(11105210, 1100300, 2, 1102020, 11105230, 11105233, 11105230))
    RunEvent(11105250, slot=2, args=(11105210, 1100300, 3, 1102030, 11105230, 11105233, 11105231))
    RunEvent(11105250, slot=3, args=(11105210, 1100300, 4, 1102020, 11105230, 11105233, 11105230))
    RunEvent(11105250, slot=4, args=(11105210, 1100300, 5, 1102050, 11105230, 11105233, 11105233))
    RunEvent(11105250, slot=5, args=(11105210, 1100300, 6, 1102040, 11105230, 11105233, 11105232))
    RunEvent(11105260, slot=0, args=(11105211, 1100301, 1, 1102040, 11105234, 11105237, 11105236))
    RunEvent(11105260, slot=1, args=(11105211, 1100301, 2, 1102020, 11105234, 11105237, 11105234))
    RunEvent(11105260, slot=2, args=(11105211, 1100301, 3, 1102030, 11105234, 11105237, 11105235))
    RunEvent(11105260, slot=3, args=(11105211, 1100301, 4, 1102020, 11105234, 11105237, 11105234))
    RunEvent(11105260, slot=4, args=(11105211, 1100301, 5, 1102050, 11105234, 11105237, 11105237))
    RunEvent(11105260, slot=5, args=(11105211, 1100301, 6, 1102040, 11105234, 11105237, 11105236))
    RunEvent(11105270, slot=0, args=(11105212, 1100302, 1, 1102040, 11105238, 11105241, 11105240))
    RunEvent(11105270, slot=1, args=(11105212, 1100302, 2, 1102020, 11105238, 11105241, 11105238))
    RunEvent(11105270, slot=2, args=(11105212, 1100302, 3, 1102030, 11105238, 11105241, 11105239))
    RunEvent(11105270, slot=3, args=(11105212, 1100302, 4, 1102020, 11105238, 11105241, 11105238))
    RunEvent(11105270, slot=4, args=(11105212, 1100302, 5, 1102050, 11105238, 11105241, 11105241))
    RunEvent(11105270, slot=5, args=(11105212, 1100302, 6, 1102040, 11105238, 11105241, 11105240))
    RunEvent(11105280, slot=0, args=(11105213, 1100303, 1, 1102040, 11105242, 11105245, 11105244))
    RunEvent(11105280, slot=1, args=(11105213, 1100303, 2, 1102020, 11105242, 11105245, 11105242))
    RunEvent(11105280, slot=2, args=(11105213, 1100303, 3, 1102030, 11105242, 11105245, 11105243))
    RunEvent(11105280, slot=3, args=(11105213, 1100303, 4, 1102020, 11105242, 11105245, 11105242))
    RunEvent(11105280, slot=4, args=(11105213, 1100303, 5, 1102050, 11105242, 11105245, 11105245))
    RunEvent(11105280, slot=5, args=(11105213, 1100303, 6, 1102040, 11105242, 11105245, 11105244))


@UnknownRestart
def Event11105190(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11105190: Event 11105190 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    AddSpecialEffect(arg_0_3, 4160)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51100260)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1202021)
    IfCharacterInsideRegion(2, PLAYER, region=1102040)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    ResetStandbyAnimationSettings(arg_0_3)
    SkipLinesIfFinishedConditionFalse(5, 1)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    CancelSpecialEffect(arg_0_3, 4160)
    SetNest(arg_0_3, 1102020)
    EnableFlag(arg_12_15)
    Restart()
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    CancelSpecialEffect(arg_0_3, 4160)
    SetNest(arg_0_3, 1102040)
    EnableFlag(arg_16_19)
    Restart()


@UnknownRestart
def Event11105195(_, arg_0_3: int, arg_4_7: int):
    """ 11105195: Event 11105195 """
    EndIfThisEventSlotOn()
    EnableFlag(arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(-1, PLAYER, region=1102050)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 3006)


@UnknownRestart
def Event11105200(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 11105200: Event 11105200 """
    IfFlagOn(0, arg_0_3)
    IfFlagOff(1, arg_16_19)
    IfCharacterInsideRegion(1, PLAYER, region=1102020)
    IfFlagOff(2, arg_20_23)
    IfCharacterInsideRegion(2, PLAYER, region=1102030)
    IfFlagOff(3, arg_24_27)
    IfCharacterInsideRegion(3, PLAYER, region=1102040)
    IfFlagOff(4, arg_28_31)
    IfCharacterInsideRegion(4, PLAYER, region=1102050)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    RestartEvent(11105220, slot=arg_8_11)
    SkipLinesIfFinishedConditionFalse(6, 1)
    SkipLinesIfFlagOff(1, arg_20_23)
    RestartEvent(arg_12_15, slot=3)
    SkipLinesIfFlagOff(1, arg_24_27)
    RestartEvent(arg_12_15, slot=1)
    SkipLinesIfFlagOff(1, arg_28_31)
    RestartEvent(arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, 2)
    SkipLinesIfFlagOff(1, arg_16_19)
    RestartEvent(arg_12_15, slot=2)
    SkipLinesIfFlagOff(1, arg_24_27)
    RestartEvent(arg_12_15, slot=1)
    SkipLinesIfFlagOff(1, arg_28_31)
    RestartEvent(arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, 3)
    SkipLinesIfFlagOff(1, arg_16_19)
    RestartEvent(arg_12_15)
    SkipLinesIfFlagOff(1, arg_20_23)
    RestartEvent(arg_12_15, slot=3)
    SkipLinesIfFlagOff(1, arg_28_31)
    RestartEvent(arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, 4)
    SkipLinesIfFlagOff(1, arg_16_19)
    RestartEvent(arg_12_15)
    SkipLinesIfFlagOff(1, arg_20_23)
    RestartEvent(arg_12_15, slot=3)
    SkipLinesIfFlagOff(1, arg_24_27)
    RestartEvent(arg_12_15, slot=4)
    IfFlagOff(0, arg_4_7)
    Restart()


@UnknownRestart
def Event11105220(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 11105220: Event 11105220 """
    DisableNetworkSync()
    IfFlagOn(0, arg_4_7)
    Wait(arg_8_11)
    RestartIfFlagOff(arg_4_7)
    DisableFlag(arg_4_7)
    RestartEvent(arg_12_15)
    RestartEvent(arg_12_15, slot=1)
    RestartEvent(arg_12_15, slot=2)
    RestartEvent(arg_12_15, slot=3)
    RestartEvent(arg_12_15, slot=4)
    RestartEvent(arg_12_15, slot=5)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@UnknownRestart
def Event11105250(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105250: Event 11105250 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart
def Event11105260(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105260: Event 11105260 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart
def Event11105270(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105270: Event 11105270 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart
def Event11105280(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105280: Event 11105280 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


def Event11100600(_, arg_0_3: int, arg_4_7: int):
    """ 11100600: Event 11100600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11100510(_, arg_0_3: int, arg_4_7: int):
    """ 11100510: Event 11100510 """
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
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11100520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100520: Event 11100520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11100530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100530: Event 11100530 """
    IfFlagOn(1, 1690)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11100531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100531: Event 11100531 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11100040():
    """ 11100040: Event 11100040 """
    DisableNetworkSync()
    Wait(1.0)
    EndIfFlagOn(11100700)
    RegisterLadder(start_climbing_flag=11100012, stop_climbing_flag=11100013, obj=1101141)


def Event11100532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11100532: Event 11100532 """
    DisableMapPiece(1103100)
    DisableMapCollision(1103101)
    DisableObject(1101750)
    DeleteVFX(1101751, erase_root_only=False)
    IfFlagOn(0, 11100700)
    DisableFlagRange((arg_4_7, arg_8_11))
    SkipLinesIfFlagOff(2, 8111)
    EnableFlag(arg_12_15)
    SkipLines(1)
    EnableFlag(arg_16_19)
    EnableMapPiece(1103100)
    EnableMapCollision(1103101)
    DisableObject(1101141)
    EnableObject(1101750)
    CreateVFX(1101751)
    EnableCharacter(arg_0_3)
    EnableCharacter(arg_20_23)
    SetTeamType(arg_20_23, TeamType.WhitePhantom)
    DisableCharacter(1100200)
    DisableCharacter(1100201)
    DisableCharacter(1100202)
    DisableCharacter(1100203)
    DisableCharacter(1100204)
    DisableCharacter(1100205)
    DisableCharacter(1100206)
    DisableCharacter(1100207)
    DisableCharacter(1100208)
    DisableCharacter(1100209)
    DisableCharacter(1100210)
    DisableCharacter(1100211)
    DisableCharacter(1100212)
    DisableCharacter(1100213)
    DisableCharacter(1100400)
    DisableCharacter(1100401)
    DisableCharacter(1100402)
    DisableCharacter(1100403)
    DisableCharacter(1100404)


def Event11100533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100533: Event 11100533 """
    IfFlagOn(1, 1606)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8110)


def Event11100534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100534: Event 11100534 """
    IfFlagOn(1, 1607)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8110)


def Event11100535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11100535: Event 11100535 """
    EndIfThisEventOn()
    IfFlagOff(1, 11100700)
    IfFlagOn(1, 8110)
    IfConditionTrue(0, input_condition=1)
    RemoveGoodFromPlayer(116)
    EnableFlag(11100300)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    SkipLinesIfFlagOff(2, 8111)
    EnableFlag(arg_12_15)
    SkipLines(1)
    EnableFlag(arg_16_19)
    DisableFlagRange((1760, 1769))
    EnableFlag(1764)


def Event11100300():
    """ 11100300: Event 11100300 """
    EndIfThisEventOn()
    IfThisEventOn(0)
    SkipLinesIfFlagOff(1, 11400400)
    AwardItemLot(2800, host_only=False)
    SkipLinesIfFlagOff(1, 11400401)
    AwardItemLot(2810, host_only=False)
    SkipLinesIfFlagOff(1, 11400402)
    AwardItemLot(2820, host_only=False)


def Event11105030():
    """ 11105030: Event 11105030 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11105031)
    EndIfFlagOn(4)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11100810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1102011)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6570, region=1102010, summon_flag=11105031, dismissal_flag=11105032)
    Wait(20.0)
    Restart()


def Event11100810():
    """ 11100810: Event 11100810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11105031)
    IfFlagOff(1, 11105032)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6570)
    EndIfThisEventOn()
    IfCharacterDead(0, 6570)
    EnableFlag(11100810)


def Event11105843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11105843: Event 11105843 """
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


def Event11105846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11105846: Event 11105846 """
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
