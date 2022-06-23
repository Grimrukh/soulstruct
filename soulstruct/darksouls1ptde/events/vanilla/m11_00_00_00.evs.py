"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11100992, obj=1101960)
    RegisterLadder(start_climbing_flag=11100010, stop_climbing_flag=11100011, obj=1101140)
    RegisterLadder(start_climbing_flag=11100014, stop_climbing_flag=11100015, obj=1101142)
    RegisterLadder(start_climbing_flag=11100016, stop_climbing_flag=11100017, obj=1101143)
    SkipLinesIfClient(1)
    DisableFlag(11100410)
    SkipLinesIfFlagEnabled(2, 11100810)
    DisableTreasure(obj=1101610)
    DisableObject(1101610)
    SkipLinesIfFlagDisabled(1, 11100810)
    EnableTreasure(obj=1101610)
    Event_11100090(1, 1101702, 1101703, 1102602, 1102603)
    Event_11105070()
    Event_11105071()
    Event_11105072()
    Event_11105399()
    Event_11100030()
    Event_11100031()
    Event_11100136()
    Event_11100135()
    Event_11100120(0, 11100120, 10010868, 1101250)
    Event_11100710()
    Event_11100200()
    Event_11100600(0, 1101650, 11100650)
    Event_11105150(0, 1100100)
    Event_11105150(1, 1100101)
    Event_11105150(2, 1100102)
    Event_11105160(0, 1100104, 1102006)
    Event_11105160(1, 1100105, 1102001)
    Event_11105170(0, 1100130, 1102202, 0.20000000298023224)
    Event_11105170(1, 1100132, 1102202, 0.0)
    Event_11105170(2, 1100135, 1102202, 0.4000000059604645)
    Event_11105170(3, 1100136, 1102202, 0.6000000238418579)
    Event_11105170(4, 1100137, 1102007, 0.30000001192092896)
    Event_11105170(5, 1100138, 1102007, 0.0)
    Event_11106299()
    Event_11106200(0, 1101011, 1101011, 12, -1)
    Event_11106200(1, 1101012, 1101012, 13, 11006200)
    Event_11106200(2, 1101013, 1101011, 12, 11006200)
    Event_11106200(3, 1101014, 1101014, 13, 11006200)
    Event_11106200(4, 1101015, 1101016, 12, 11006205)
    Event_11106200(5, 1101016, 1101016, 13, -1)
    Event_11106200(6, 1101017, 1101016, 12, 11006205)
    Event_11106200(7, 1101018, 1101018, 13, -1)
    Event_11106200(8, 1101019, 1101019, 13, -1)
    Event_11106200(9, 1101020, 1101020, 12, -1)
    Event_11106200(13, 1101024, 1101024, 13, -1)
    Event_11106200(14, 1101025, 1101025, 12, -1)
    Event_11106200(18, 1101029, 1101029, 12, -1)
    Event_11106200(19, 1101030, 1101030, 13, -1)
    Event_11106200(24, 1101035, 1101035, 12, -1)
    Event_11106200(27, 1101038, 1101038, 12, -1)
    Event_11106200(28, 1101039, 1101039, 13, -1)
    Event_11106200(29, 1101040, 1101040, 12, -1)
    Event_11106200(30, 1101041, 1101041, 12, -1)
    Event_11106200(31, 1101042, 1101042, 13, -1)
    Event_11106200(32, 1101043, 1101043, 12, -1)
    Event_11106200(33, 1101044, 1101044, 12, -1)
    Event_11100070(0, 1101120, 1101600, 120, 121)
    Event_11100070(1, 1101121, 1101601, 125, 126)
    SkipLinesIfFlagDisabled(1, 11100400)
    DisableCharacter(1100170)
    Event_11105370()
    Event_11100100(0, 1101180, 1103000)
    Event_11100100(1, 1101181, 1103001)
    Event_11100400()
    Event_11105371()
    DisableSoundEvent(sound_id=1103800)
    DisableObject(1101992)
    DeleteVFX(vfx_id=1101993, erase_root_only=False)
    SkipLinesIfFlagDisabled(4, 4)
    Event_11105392()
    DisableObject(1101990)
    DeleteVFX(vfx_id=1101991, erase_root_only=False)
    SkipLines(10)
    Event_11105390()
    Event_11105391()
    Event_11105393()
    Event_11105392()
    Event_11100000()
    Event_11105394()
    Event_11105395()
    Event_11105396()
    Event_11105397()
    Event_11105398()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_11100420()
    HumanityRegistration(6570, event_flag=8964)
    Event_11105030()
    Event_11100810()
    Event_11105010()
    SkipLinesIfFlagEnabled(1, 1691)
    SetTeamType(1100160, TeamType.Ally)
    Event_11100530(0, 1100160, 1690, 1693, 1691)
    Event_11100531(0, 1100160, 1690, 1693, 1692)
    HumanityRegistration(6312, event_flag=8470)
    HumanityRegistration(6422, event_flag=8900)
    DisableCharacter(6312)
    DisableCharacter(6422)
    Event_11100040()
    Event_11100532(0, 6312, 1600, 1619, 1606, 1607, 6422)
    Event_11100533(0, 6312, 1600, 1619, 1608)
    Event_11100534(0, 6312, 1600, 1619, 1609)
    Event_11100535(0, 6312, 1600, 1619, 1608, 1609)
    Event_11100300()


@NeverRestart(11100090)
def Event_11100090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100090"""
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


@RestartOnRest(11105070)
def Event_11105070():
    """Event 11105070"""
    EndIfThisEventFlagEnabled()
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
    IfFlagEnabled(0, 11100050)
    EndIfFlagEnabled(735)
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


@RestartOnRest(11105071)
def Event_11105071():
    """Event 11105071"""
    IfFlagEnabled(-1, 11105075)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11100050)
    DisableFlag(11105075)
    EnableFlag(5001)
    Kill(1100900)
    Kill(1100901)
    Kill(1100902)
    Kill(1100903)
    Kill(1100904)
    Kill(1100905)
    Kill(1100906)
    Kill(1100907)
    Kill(1100908)
    Kill(1100909)
    Kill(1100910)
    Kill(1100911)


@RestartOnRest(11105072)
def Event_11105072():
    """Event 11105072"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=PAINTED_WORLD)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11100050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=PAINTED_WORLD)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11100050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=PAINTED_WORLD)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11100050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=PAINTED_WORLD)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11100050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=PAINTED_WORLD)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11100050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=PAINTED_WORLD)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11100050)
    RestartIfConditionFalse(-6)
    EnableFlag(11100050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=PAINTED_WORLD)
    RestartIfConditionFalse(7)
    DisableFlag(11100050)
    EnableFlag(11105075)


@NeverRestart(11105390)
def Event_11105390():
    """Event 11105390"""
    IfFlagDisabled(1, 4)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1102998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1101990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1102997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11105391)
def Event_11105391():
    """Event 11105391"""
    IfFlagDisabled(1, 4)
    IfFlagEnabled(1, 11105393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1102998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1101990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1102997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11105393)
def Event_11105393():
    """Event 11105393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 4)
    IfCharacterInsideRegion(1, PLAYER, region=1102996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1100160)
    EnableFlag(11105393)
    IfFlagEnabled(0, 4)
    End()


@RestartOnRest(11105392)
def Event_11105392():
    """Event 11105392"""
    SkipLinesIfFlagDisabled(7, 4)
    DisableCharacter(1100160)
    DisableCharacter(1100161)
    Kill(1100160)
    Kill(1100161)
    DisableBackread(1100160)
    DisableBackread(1100161)
    End()
    SkipLinesIfFlagDisabled(1, 1691)
    SetTeamType(1100160, TeamType.Ally)
    DisableAI(1100160)
    DisableHealthBar(1100160)
    IfCharacterAlive(1, 1100160)
    IfFlagEnabled(1, 11105393)
    IfAttacked(1, attacked_entity=1100160, attacker=PLAYER)
    IfFlagEnabled(2, 11105393)
    IfCharacterInsideRegion(2, PLAYER, region=1102100)
    IfFlagEnabled(2, 1691)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1100160)
    SetTeamType(1100160, TeamType.Boss)
    EnableBossHealthBar(1100160, name=2730, slot=0)
    EnableFlag(11105392)
    IfFlagEnabled(0, 4)
    End()


@NeverRestart(11100000)
def Event_11100000():
    """Event 11100000"""
    EndIfThisEventFlagEnabled()
    IfCharacterDead(0, 1100160)
    EnableFlag(4)
    KillBoss(game_area_param_id=1100160)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=40)
    Kill(1100161)
    DisableBackread(1100161)
    DisableObject(1101990)
    DeleteVFX(vfx_id=1101991)


@NeverRestart(11105394)
def Event_11105394():
    """Event 11105394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 4)
    IfFlagEnabled(1, 11105390)
    IfCharacterInsideRegion(1, PLAYER, region=1102996)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11105391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1103800)
    EnableFlag(11105394)
    IfFlagEnabled(0, 4)
    End()


@NeverRestart(11105395)
def Event_11105395():
    """Event 11105395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 4)
    IfCharacterInsideRegion(1, PLAYER, region=1102100)
    IfFlagEnabled(2, 11105380)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(sound_id=1103800)
    EnableFlag(11105395)
    IfFlagEnabled(0, 4)
    End()


@RestartOnRest(11105396)
def Event_11105396():
    """Event 11105396"""
    DisableCharacter(1100161)
    EndIfFlagEnabled(4)
    SkipLinesIfThisEventFlagDisabled(3)
    SetDisplayMask(1100160, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1100160, bit_index=1, switch_type=OnOffChange.Off)
    End()
    IfCharacterBackreadEnabled(0, 1100160)
    CreateNPCPart(1100160, npc_part_id=2730, part_index=NPCPartType.Part1, part_health=158)
    IfHealthGreaterThan(1, 1100160, value=0.0)
    IfCharacterPartHealthComparison(1, 1100160, npc_part_id=2730, comparison_type=ComparisonType.Equal, value=5)
    IfFlagDisabled(1, 11105381)
    IfAttacked(1, attacked_entity=1100160, attacker=PLAYER)
    IfHealthLessThanOrEqual(2, 1100160, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(1100160)
    ForceAnimation(1100160, 8000)
    IfCharacterHasTAEEvent(0, 1100160, tae_event_id=400)
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
    IfFlagEnabled(0, 4)
    End()


@RestartOnRest(11105397)
def Event_11105397():
    """Event 11105397"""
    IfCharacterHasTAEEvent(0, 1100160, tae_event_id=600)
    DisableHealthBar(1100160)
    DisableBossHealthBar(1100160, name=2730, slot=0)
    EnableFlag(11105381)
    DisableFlagRange((11105110, 11105119))
    SkipLinesIfClient(44)
    SetNetworkUpdateAuthority(1100160, authority_level=UpdateAuthority.Forced)
    EnableRandomFlagInRange(flag_range=(11105110, 11105119))
    SkipLinesIfFlagDisabled(3, 11105110)
    IfCharacterInsideRegion(1, 1100160, region=1102810)
    SkipLinesIfConditionTrue(2, 1)
    Move(1100160, destination=1102810, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105111)
    IfCharacterInsideRegion(2, 1100160, region=1102811)
    SkipLinesIfConditionTrue(2, 2)
    Move(1100160, destination=1102811, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105112)
    IfCharacterInsideRegion(3, 1100160, region=1102812)
    SkipLinesIfConditionTrue(2, 3)
    Move(1100160, destination=1102812, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105113)
    IfCharacterInsideRegion(4, 1100160, region=1102813)
    SkipLinesIfConditionTrue(2, 4)
    Move(1100160, destination=1102813, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105114)
    IfCharacterInsideRegion(5, 1100160, region=1102814)
    SkipLinesIfConditionTrue(2, 5)
    Move(1100160, destination=1102814, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105115)
    IfCharacterInsideRegion(6, 1100160, region=1102815)
    SkipLinesIfConditionTrue(2, 6)
    Move(1100160, destination=1102815, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105116)
    IfCharacterInsideRegion(7, 1100160, region=1102816)
    SkipLinesIfConditionTrue(2, 7)
    Move(1100160, destination=1102816, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105117)
    IfCharacterInsideRegion(-1, 1100160, region=1102817)
    SkipLinesIfConditionTrue(2, -1)
    Move(1100160, destination=1102817, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105118)
    IfCharacterInsideRegion(-2, 1100160, region=1102818)
    SkipLinesIfConditionTrue(2, -2)
    Move(1100160, destination=1102818, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105119)
    IfCharacterInsideRegion(-3, 1100160, region=1102819)
    SkipLinesIfConditionTrue(2, -3)
    Move(1100160, destination=1102819, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(1100160, destination=1102810, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterDoesNotHaveTAEEvent(0, 1100160, tae_event_id=600)
    Restart()


@RestartOnRest(11105398)
def Event_11105398():
    """Event 11105398"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, 1100160, tae_event_id=700)
    EnableHealthBar(1100160)
    EnableBossHealthBar(1100160, name=2730, slot=0)
    DisableFlag(11105381)
    IfCharacterDoesNotHaveTAEEvent(0, 1100160, tae_event_id=700)
    Restart()


@NeverRestart(11105399)
def Event_11105399():
    """Event 11105399"""
    EndIfClient()
    DisableNetworkSync()
    IfInsideMap(0, game_map=ANOR_LONDO)
    IfInsideMap(0, game_map=PAINTED_WORLD)
    RestartEvent(event_id=11105390, slot=0)
    RestartEvent(event_id=11105391, slot=0)
    RestartEvent(event_id=11105392, slot=0)
    RestartEvent(event_id=11105393, slot=0)
    RestartEvent(event_id=11105394, slot=0)
    RestartEvent(event_id=11105395, slot=0)
    RestartEvent(event_id=11105396, slot=0)
    RestartEvent(event_id=11105397, slot=0)
    RestartEvent(event_id=11105398, slot=0)
    DisableFlagRange((11105390, 11105399))
    Restart()


@RestartOnRest(11105150)
def Event_11105150(_, arg_0_3: int):
    """Event 11105150"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=arg_0_3, radius=5.0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest(11105160)
def Event_11105160(_, arg_0_3: int, arg_4_7: int):
    """Event 11105160"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest(11105170)
def Event_11105170(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """Event 11105170"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
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


@RestartOnRest(11106200)
def Event_11106200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11106200"""
    DisableNetworkSync()
    SkipLinesIfEqual(1, left=arg_12_15, right=-1)
    IfFlagEnabled(-1, arg_12_15)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=arg_4_7, radius=7.0)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    DisableObject(arg_0_3)


@RestartOnRest(11106299)
def Event_11106299():
    """Event 11106299"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1102000)
    Event_11106298(-1, 1101300, 13)
    Event_11106298(-1, 1101301, 12)
    Event_11106298(-1, 1101302, 12)
    Event_11106298(-1, 1101303, 13)
    Event_11106298(-1, 1101304, 12)
    Event_11106298(-1, 1101305, 12)
    Event_11106298(-1, 1101306, 13)
    Event_11106298(-1, 1101307, 12)
    Event_11106298(-1, 1101308, 12)
    Event_11106298(-1, 1101309, 13)
    Event_11106298(-1, 1101310, 12)
    Event_11106298(-1, 1101311, 12)


@UnknownRestart(11106298)
def Event_11106298(_, arg_0_3: int, arg_4_7: int):
    """Event 11106298"""
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    DisableObject(arg_0_3)


@NeverRestart(11100070)
def Event_11100070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100070"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_4_7, animation_id=arg_12_15)
    PostDestruction(arg_0_3)
    EnableTreasure(obj=arg_4_7)
    End()
    DisableTreasure(obj=arg_4_7)
    SkipLinesIfClient(1)
    CreateObjectVFX(vfx_id=arg_4_7, obj=90, model_point=99005)
    ForceAnimation(arg_4_7, arg_8_11, loop=True)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(arg_4_7)
    EnableTreasure(obj=arg_4_7)


@RestartOnRest(11105370)
def Event_11105370():
    """Event 11105370"""
    SkipLinesIfFlagDisabled(2, 11100410)
    SetStandbyAnimationSettings(1100170)
    End()
    IfCharacterType(3, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=3)
    IfCharacterInsideRegion(1, PLAYER, region=1102070)
    IfConditionFalse(2, input_condition=3)
    IfAttacked(2, attacked_entity=1100170, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(11100410)
    SetStandbyAnimationSettings(1100170)
    ForceAnimation(1100170, 9060)
    PlaySoundEffect(anchor_entity=1102080, sound_id=110003420, sound_type=SoundType.a_Ambient)


@RestartOnRest(11105371)
def Event_11105371():
    """Event 11105371"""
    DisableCharacter(1100172)
    SkipLinesIfThisEventFlagDisabled(4)
    IfCharacterBackreadEnabled(0, 1100170)
    SetDisplayMask(1100170, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(1100170, bit_index=1, switch_type=OnOffChange.On)
    End()
    IfCharacterHasTAEEvent(0, 1100170, tae_event_id=400)
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


@NeverRestart(11100100)
def Event_11100100(_, arg_0_3: int, arg_4_7: int):
    """Event 11100100"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    DestroyObject(arg_0_3)
    ForceAnimation(arg_0_3, 0)
    DeleteVFX(vfx_id=arg_4_7, erase_root_only=False)
    End()
    IfObjectDestroyed(0, arg_0_3)
    DeleteVFX(vfx_id=arg_4_7)


@RestartOnRest(11100400)
def Event_11100400():
    """Event 11100400"""
    EnableImmortality(1100171)
    EnableInvincibility(1100171)
    DisableHealthBar(1100171)
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1100170)
    End()
    SetBackreadStateAlternate(1100170, True)
    DisableGravity(1100170)
    IfCharacterDead(0, 1100170)
    EnableFlag(11100400)


@NeverRestart(11100030)
def Event_11100030():
    """Event 11100030"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    EndOfAnimation(obj=1101130, animation_id=2)
    DisableNavmeshType(navmesh_id=1102040, navmesh_type=NavmeshType.Solid)
    End()
    EnableNavmeshType(navmesh_id=1102040, navmesh_type=NavmeshType.Solid)
    IfFlagDisabled(1, 11100700)
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
    DisableNavmeshType(navmesh_id=1102040, navmesh_type=NavmeshType.Solid)


@NeverRestart(11100031)
def Event_11100031():
    """Event 11100031"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11100030)
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
    DisplayDialog(text=10010161, anchor_entity=1101130, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11100120)
def Event_11100120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11100120"""
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    DisplayDialog(text=arg_4_7, anchor_entity=arg_8_11, button_type=ButtonType.Yes_or_No)


@NeverRestart(11100135)
def Event_11100135():
    """Event 11100135"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=1101160, animation_id=1)
    EndOfAnimation(obj=1101170, animation_id=1)
    DisableNavmeshType(navmesh_id=1102041, navmesh_type=NavmeshType.Solid)
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
    PlayCutscene(110000, cutscene_flags=2, player_id=10000)
    SkipLines(1)
    PlayCutscene(110000, cutscene_flags=0, player_id=10000)
    ForceAnimation(1101160, 1)
    ForceAnimation(1101170, 1)
    DisableNavmeshType(navmesh_id=1102041, navmesh_type=NavmeshType.Solid)


@NeverRestart(11100136)
def Event_11100136():
    """Event 11100136"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11100135)
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
    DisplayDialog(text=10010160, anchor_entity=1101170, button_type=ButtonType.Yes_or_No)
    Restart()


@RestartOnRest(11100420)
def Event_11100420():
    """Event 11100420"""
    SkipLinesIfThisEventFlagDisabled(3)
    Move(1100180, destination=1102201, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1100180, region=1102201)
    End()
    DisableAI(1100180)
    IfCharacterInsideRegion(-1, PLAYER, region=1102200)
    IfAttacked(-1, attacked_entity=1100180, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1100130, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1100132, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1100135, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1100136, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(1100180, 500)
    EnableAI(1100180)
    SetNest(1100180, region=1102201)


@NeverRestart(11100710)
def Event_11100710():
    """Event 11100710"""
    DisableFlag(11105380)
    IfHost(1)
    IfFlagDisabled(1, 1691)
    IfCharacterInsideRegion(1, PLAYER, region=1102500)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(1100160)
    EndIfClient()
    DisableImmortality(1100160)
    EnableFlag(11105380)
    SkipLinesIfFlagEnabled(1, 4)
    IfFlagEnabled(0, 11105395)
    PlayCutscene(110035, cutscene_flags=0, player_id=10000, move_to_region=1512500, move_to_map=ANOR_LONDO)
    WaitFrames(frames=1)
    SkipLinesIfThisEventFlagEnabled(1)
    AwardItemLot(9030, host_only=True)
    SetRespawnPoint(respawn_point=1512960)
    SaveRequest()
    Restart()


@RestartOnRest(11105010)
def Event_11105010():
    """Event 11105010"""
    EndIfThisEventFlagEnabled()
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
    SetStandbyAnimationSettings(1100200)
    SetStandbyAnimationSettings(1100201)
    SetStandbyAnimationSettings(1100202)
    SetStandbyAnimationSettings(1100203)
    SetStandbyAnimationSettings(1100204)
    SetStandbyAnimationSettings(1100205)
    SetStandbyAnimationSettings(1100206)
    SetStandbyAnimationSettings(1100207)
    SetStandbyAnimationSettings(1100208)
    SetStandbyAnimationSettings(1100209)
    SetStandbyAnimationSettings(1100210)
    SetStandbyAnimationSettings(1100211)
    SetStandbyAnimationSettings(1100212)
    SetStandbyAnimationSettings(1100213)
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


@RestartOnRest(11100200)
def Event_11100200():
    """Event 11100200"""
    Event_11105190(0, 1100300, 3010, 3011, 11105230, 11105232)
    Event_11105190(1, 1100301, 3012, 3013, 11105234, 11105236)
    Event_11105195(0, 1100302, 11105240)
    Event_11105195(1, 1100303, 11105244)
    Event_11105200(0, 11105190, 11105210, 0, 11105250, 11105230, 11105231, 11105232, 11105233)
    Event_11105200(1, 11105191, 11105211, 1, 11105260, 11105234, 11105235, 11105236, 11105237)
    Event_11105200(2, 11105195, 11105212, 2, 11105270, 11105238, 11105239, 11105240, 11105241)
    Event_11105200(3, 11105196, 11105213, 3, 11105280, 11105242, 11105243, 11105244, 11105245)
    Event_11105220(0, 1100300, 11105210, 10.0, 11105250)
    Event_11105220(1, 1100301, 11105211, 10.0, 11105260)
    Event_11105220(2, 1100302, 11105212, 10.0, 11105270)
    Event_11105220(3, 1100303, 11105213, 10.0, 11105280)
    Event_11105250(0, 11105210, 1100300, 1, 1102040, 11105230, 11105233, 11105232)
    Event_11105250(1, 11105210, 1100300, 2, 1102020, 11105230, 11105233, 11105230)
    Event_11105250(2, 11105210, 1100300, 3, 1102030, 11105230, 11105233, 11105231)
    Event_11105250(3, 11105210, 1100300, 4, 1102020, 11105230, 11105233, 11105230)
    Event_11105250(4, 11105210, 1100300, 5, 1102050, 11105230, 11105233, 11105233)
    Event_11105250(5, 11105210, 1100300, 6, 1102040, 11105230, 11105233, 11105232)
    Event_11105260(0, 11105211, 1100301, 1, 1102040, 11105234, 11105237, 11105236)
    Event_11105260(1, 11105211, 1100301, 2, 1102020, 11105234, 11105237, 11105234)
    Event_11105260(2, 11105211, 1100301, 3, 1102030, 11105234, 11105237, 11105235)
    Event_11105260(3, 11105211, 1100301, 4, 1102020, 11105234, 11105237, 11105234)
    Event_11105260(4, 11105211, 1100301, 5, 1102050, 11105234, 11105237, 11105237)
    Event_11105260(5, 11105211, 1100301, 6, 1102040, 11105234, 11105237, 11105236)
    Event_11105270(0, 11105212, 1100302, 1, 1102040, 11105238, 11105241, 11105240)
    Event_11105270(1, 11105212, 1100302, 2, 1102020, 11105238, 11105241, 11105238)
    Event_11105270(2, 11105212, 1100302, 3, 1102030, 11105238, 11105241, 11105239)
    Event_11105270(3, 11105212, 1100302, 4, 1102020, 11105238, 11105241, 11105238)
    Event_11105270(4, 11105212, 1100302, 5, 1102050, 11105238, 11105241, 11105241)
    Event_11105270(5, 11105212, 1100302, 6, 1102040, 11105238, 11105241, 11105240)
    Event_11105280(0, 11105213, 1100303, 1, 1102040, 11105242, 11105245, 11105244)
    Event_11105280(1, 11105213, 1100303, 2, 1102020, 11105242, 11105245, 11105242)
    Event_11105280(2, 11105213, 1100303, 3, 1102030, 11105242, 11105245, 11105243)
    Event_11105280(3, 11105213, 1100303, 4, 1102020, 11105242, 11105245, 11105242)
    Event_11105280(4, 11105213, 1100303, 5, 1102050, 11105242, 11105245, 11105245)
    Event_11105280(5, 11105213, 1100303, 6, 1102040, 11105242, 11105245, 11105244)


@UnknownRestart(11105190)
def Event_11105190(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11105190"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    AddSpecialEffect(arg_0_3, 4160)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, 51100260)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1202021)
    IfCharacterInsideRegion(2, PLAYER, region=1102040)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3)
    SkipLinesIfFinishedConditionFalse(5, condition=1)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    CancelSpecialEffect(arg_0_3, 4160)
    SetNest(arg_0_3, region=1102020)
    EnableFlag(arg_12_15)
    Restart()
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    CancelSpecialEffect(arg_0_3, 4160)
    SetNest(arg_0_3, region=1102040)
    EnableFlag(arg_16_19)
    Restart()


@UnknownRestart(11105195)
def Event_11105195(_, arg_0_3: int, arg_4_7: int):
    """Event 11105195"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(-1, PLAYER, region=1102050)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 3006)


@UnknownRestart(11105200)
def Event_11105200(
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
    """Event 11105200"""
    IfFlagEnabled(0, arg_0_3)
    IfFlagDisabled(1, arg_16_19)
    IfCharacterInsideRegion(1, PLAYER, region=1102020)
    IfFlagDisabled(2, arg_20_23)
    IfCharacterInsideRegion(2, PLAYER, region=1102030)
    IfFlagDisabled(3, arg_24_27)
    IfCharacterInsideRegion(3, PLAYER, region=1102040)
    IfFlagDisabled(4, arg_28_31)
    IfCharacterInsideRegion(4, PLAYER, region=1102050)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    RestartEvent(event_id=11105220, slot=arg_8_11)
    SkipLinesIfFinishedConditionFalse(6, condition=1)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    RestartEvent(event_id=arg_12_15, slot=3)
    SkipLinesIfFlagDisabled(1, arg_24_27)
    RestartEvent(event_id=arg_12_15, slot=1)
    SkipLinesIfFlagDisabled(1, arg_28_31)
    RestartEvent(event_id=arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, condition=2)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    RestartEvent(event_id=arg_12_15, slot=2)
    SkipLinesIfFlagDisabled(1, arg_24_27)
    RestartEvent(event_id=arg_12_15, slot=1)
    SkipLinesIfFlagDisabled(1, arg_28_31)
    RestartEvent(event_id=arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, condition=3)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    RestartEvent(event_id=arg_12_15, slot=0)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    RestartEvent(event_id=arg_12_15, slot=3)
    SkipLinesIfFlagDisabled(1, arg_28_31)
    RestartEvent(event_id=arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, condition=4)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    RestartEvent(event_id=arg_12_15, slot=0)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    RestartEvent(event_id=arg_12_15, slot=3)
    SkipLinesIfFlagDisabled(1, arg_24_27)
    RestartEvent(event_id=arg_12_15, slot=4)
    IfFlagDisabled(0, arg_4_7)
    Restart()


@UnknownRestart(11105220)
def Event_11105220(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """Event 11105220"""
    DisableNetworkSync()
    IfFlagEnabled(0, arg_4_7)
    Wait(arg_8_11)
    RestartIfFlagDisabled(arg_4_7)
    DisableFlag(arg_4_7)
    RestartEvent(event_id=arg_12_15, slot=0)
    RestartEvent(event_id=arg_12_15, slot=1)
    RestartEvent(event_id=arg_12_15, slot=2)
    RestartEvent(event_id=arg_12_15, slot=3)
    RestartEvent(event_id=arg_12_15, slot=4)
    RestartEvent(event_id=arg_12_15, slot=5)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@UnknownRestart(11105250)
def Event_11105250(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11105250"""
    SkipLinesIfFlagEnabled(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, region=arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart(11105260)
def Event_11105260(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11105260"""
    SkipLinesIfFlagEnabled(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, region=arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart(11105270)
def Event_11105270(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11105270"""
    SkipLinesIfFlagEnabled(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, region=arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart(11105280)
def Event_11105280(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11105280"""
    SkipLinesIfFlagEnabled(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, region=arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@NeverRestart(11100600)
def Event_11100600(_, arg_0_3: int, arg_4_7: int):
    """Event 11100600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11100510)
def Event_11100510(_, arg_0_3: int, arg_4_7: int):
    """Event 11100510"""
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
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11100520)
def Event_11100520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11100530)
def Event_11100530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100530"""
    IfFlagEnabled(1, 1690)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11100531)
def Event_11100531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100531"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableCharacter(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11100040)
def Event_11100040():
    """Event 11100040"""
    DisableNetworkSync()
    Wait(1.0)
    EndIfFlagEnabled(11100700)
    RegisterLadder(start_climbing_flag=11100012, stop_climbing_flag=11100013, obj=1101141)


@NeverRestart(11100532)
def Event_11100532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11100532"""
    DisableMapPiece(map_piece_id=1103100)
    DisableMapCollision(collision=1103101)
    DisableObject(1101750)
    DeleteVFX(vfx_id=1101751, erase_root_only=False)
    IfFlagEnabled(0, 11100700)
    DisableFlagRange((arg_4_7, arg_8_11))
    SkipLinesIfFlagDisabled(2, 8111)
    EnableFlag(arg_12_15)
    SkipLines(1)
    EnableFlag(arg_16_19)
    EnableMapPiece(map_piece_id=1103100)
    EnableMapCollision(collision=1103101)
    DisableObject(1101141)
    EnableObject(1101750)
    CreateVFX(vfx_id=1101751)
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


@NeverRestart(11100533)
def Event_11100533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100533"""
    IfFlagEnabled(1, 1606)
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8110)


@NeverRestart(11100534)
def Event_11100534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11100534"""
    IfFlagEnabled(1, 1607)
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8110)


@NeverRestart(11100535)
def Event_11100535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11100535"""
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, 11100700)
    IfFlagEnabled(1, 8110)
    IfConditionTrue(0, input_condition=1)
    RemoveGoodFromPlayer(item=116)
    EnableFlag(11100300)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    SkipLinesIfFlagDisabled(2, 8111)
    EnableFlag(arg_12_15)
    SkipLines(1)
    EnableFlag(arg_16_19)
    DisableFlagRange((1760, 1769))
    EnableFlag(1764)


@NeverRestart(11100300)
def Event_11100300():
    """Event 11100300"""
    EndIfThisEventFlagEnabled()
    IfThisEventFlagEnabled(0)
    SkipLinesIfFlagDisabled(1, 11400400)
    AwardItemLot(2800, host_only=False)
    SkipLinesIfFlagDisabled(1, 11400401)
    AwardItemLot(2810, host_only=False)
    SkipLinesIfFlagDisabled(1, 11400402)
    AwardItemLot(2820, host_only=False)


@NeverRestart(11105030)
def Event_11105030():
    """Event 11105030"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(11105031)
    EndIfFlagEnabled(4)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11100810)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1102011)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6570,
        region=1102010,
        summon_flag=11105031,
        dismissal_flag=11105032,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11100810)
def Event_11100810():
    """Event 11100810"""
    SkipLinesIfHost(3)
    IfFlagEnabled(1, 11105031)
    IfFlagDisabled(1, 11105032)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6570)
    EndIfThisEventFlagEnabled()
    IfCharacterDead(0, 6570)
    EnableFlag(11100810)
