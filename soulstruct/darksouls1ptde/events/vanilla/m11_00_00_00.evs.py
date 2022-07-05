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
    Event_11100090(1, line_intersects__obj=1101702, vfx_id=1101703, destination=1102602, destination_1=1102603)
    Event_11105070()
    Event_11105071()
    Event_11105072()
    Event_11105399()
    Event_11100030()
    Event_11100031()
    Event_11100136()
    Event_11100135()
    Event_11100120(0, obj_act_id=11100120, text=10010868, anchor_entity=1101250)
    Event_11100710()
    Event_11100200()
    Event_11100600(0, obj=1101650, obj_act_id=11100650)
    Event_11105150(0, character=1100100)
    Event_11105150(1, character=1100101)
    Event_11105150(2, character=1100102)
    Event_11105160(0, character=1100104, region=1102006)
    Event_11105160(1, character=1100105, region=1102001)
    Event_11105170(0, 1100130, 1102202, 0.20000000298023224)
    Event_11105170(1, 1100132, 1102202, 0.0)
    Event_11105170(2, 1100135, 1102202, 0.4000000059604645)
    Event_11105170(3, 1100136, 1102202, 0.6000000238418579)
    Event_11105170(4, 1100137, 1102007, 0.30000001192092896)
    Event_11105170(5, 1100138, 1102007, 0.0)
    Event_11106299()
    Event_11106200(0, 1101011, 1101011, 12, -1)
    Event_11106200(1, obj=1101012, other_entity=1101012, animation_id=13, left=11006200)
    Event_11106200(2, obj=1101013, other_entity=1101011, animation_id=12, left=11006200)
    Event_11106200(3, obj=1101014, other_entity=1101014, animation_id=13, left=11006200)
    Event_11106200(4, obj=1101015, other_entity=1101016, animation_id=12, left=11006205)
    Event_11106200(5, 1101016, 1101016, 13, -1)
    Event_11106200(6, obj=1101017, other_entity=1101016, animation_id=12, left=11006205)
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
    Event_11100070(0, obj=1101120, obj_1=1101600, animation_id=120, animation_id_1=121)
    Event_11100070(1, obj=1101121, obj_1=1101601, animation_id=125, animation_id_1=126)
    SkipLinesIfFlagDisabled(1, 11100400)
    DisableCharacter(1100170)
    Event_11105370()
    Event_11100100(0, obj=1101180, vfx_id=1103000)
    Event_11100100(1, obj=1101181, vfx_id=1103001)
    Event_11100400()
    Event_11105371()
    DisableSoundEvent(sound_id=1103800)
    DisableObject(1101992)
    DeleteVFX(1101993, erase_root_only=False)
    SkipLinesIfFlagDisabled(4, 4)
    Event_11105392()
    DisableObject(1101990)
    DeleteVFX(1101991, erase_root_only=False)
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
    Event_11100530(0, character=1100160, first_flag=1690, last_flag=1693, flag=1691)
    Event_11100531(0, character=1100160, first_flag=1690, last_flag=1693, flag=1692)
    HumanityRegistration(6312, event_flag=8470)
    HumanityRegistration(6422, event_flag=8900)
    DisableCharacter(6312)
    DisableCharacter(6422)
    Event_11100040()
    Event_11100532(0, character=6312, first_flag=1600, last_flag=1619, flag=1606, flag_1=1607, character_1=6422)
    Event_11100533(0, character=6312, first_flag=1600, last_flag=1619, flag=1608)
    Event_11100534(0, character=6312, first_flag=1600, last_flag=1619, flag=1609)
    Event_11100535(0, character=6312, first_flag=1600, last_flag=1619, flag=1608, flag_1=1609)
    Event_11100300()


@NeverRestart(11100090)
def Event_11100090(_, line_intersects__obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11100090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=line_intersects__obj,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=line_intersects__obj,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id)


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
    IfCharacterWhitePhantom(1, PLAYER)
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
    EnableBossHealthBar(1100160, name=2730)
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
    DeleteVFX(1101991)


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
    IfCharacterPartHealthLessThanOrEqual(1, 1100160, npc_part_id=2730, value=0)
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
    DisableBossHealthBar(1100160, name=2730)
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
    EnableBossHealthBar(1100160, name=2730)
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
    RestartEvent(event_id=11105390)
    RestartEvent(event_id=11105391)
    RestartEvent(event_id=11105392)
    RestartEvent(event_id=11105393)
    RestartEvent(event_id=11105394)
    RestartEvent(event_id=11105395)
    RestartEvent(event_id=11105396)
    RestartEvent(event_id=11105397)
    RestartEvent(event_id=11105398)
    DisableFlagRange((11105390, 11105399))
    Restart()


@RestartOnRest(11105150)
def Event_11105150(_, character: int):
    """Event 11105150"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    DisableCharacterCollision(character)
    DisableAI(character)
    DisableGravity(character)
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=character, radius=5.0)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    EnableAI(character)


@RestartOnRest(11105160)
def Event_11105160(_, character: int, region: int):
    """Event 11105160"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    DisableCharacterCollision(character)
    DisableAI(character)
    DisableGravity(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    EnableAI(character)


@RestartOnRest(11105170)
def Event_11105170(_, character: int, region: int, seconds: float):
    """Event 11105170"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    DisableCharacterCollision(character)
    DisableAI(character)
    DisableGravity(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    Wait(seconds)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    EnableAI(character)


@RestartOnRest(11106200)
def Event_11106200(_, obj: int, other_entity: int, animation_id: int, left: int):
    """Event 11106200"""
    DisableNetworkSync()
    SkipLinesIfEqual(1, left=left, right=-1)
    IfFlagEnabled(-1, left)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=other_entity, radius=7.0)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


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
def Event_11106298(_, obj: int, animation_id: int):
    """Event 11106298"""
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@NeverRestart(11100070)
def Event_11100070(_, obj: int, obj_1: int, animation_id: int, animation_id_1: int):
    """Event 11100070"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj_1, animation_id=animation_id_1)
    PostDestruction(obj)
    EnableTreasure(obj=obj_1)
    End()
    DisableTreasure(obj=obj_1)
    SkipLinesIfClient(1)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=99005)
    ForceAnimation(obj_1, animation_id, loop=True)
    IfObjectDestroyed(0, obj)
    ForceAnimation(obj_1, animation_id_1, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(obj_1)
    EnableTreasure(obj=obj_1)


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
    PlaySoundEffect(1102080, 110003420, sound_type=SoundType.a_Ambient)


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
def Event_11100100(_, obj: int, vfx_id: int):
    """Event 11100100"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    DestroyObject(obj)
    ForceAnimation(obj, 0)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()
    IfObjectDestroyed(0, obj)
    DeleteVFX(vfx_id)


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
def Event_11100120(_, obj_act_id: int, text: int, anchor_entity: int):
    """Event 11100120"""
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EndIfClient()
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


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
    PlayCutscene(110000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
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
    PlayCutscene(110035, cutscene_flags=0, player_id=10000, move_to_region=1512500, game_map=ANOR_LONDO)
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
    Event_11105190(0, character=1100300, animation_id=3010, animation_id_1=3011, flag=11105230, flag_1=11105232)
    Event_11105190(1, character=1100301, animation_id=3012, animation_id_1=3013, flag=11105234, flag_1=11105236)
    Event_11105195(0, character=1100302, flag=11105240)
    Event_11105195(1, character=1100303, flag=11105244)
    Event_11105200(
        0,
        flag=11105190,
        flag_1=11105210,
        event_slot=0,
        event_id=11105250,
        flag_2=11105230,
        flag_3=11105231,
        flag_4=11105232,
        flag_5=11105233
    )
    Event_11105200(
        1,
        flag=11105191,
        flag_1=11105211,
        event_slot=1,
        event_id=11105260,
        flag_2=11105234,
        flag_3=11105235,
        flag_4=11105236,
        flag_5=11105237
    )
    Event_11105200(
        2,
        flag=11105195,
        flag_1=11105212,
        event_slot=2,
        event_id=11105270,
        flag_2=11105238,
        flag_3=11105239,
        flag_4=11105240,
        flag_5=11105241
    )
    Event_11105200(
        3,
        flag=11105196,
        flag_1=11105213,
        event_slot=3,
        event_id=11105280,
        flag_2=11105242,
        flag_3=11105243,
        flag_4=11105244,
        flag_5=11105245
    )
    Event_11105220(0, 1100300, 11105210, 10.0, 11105250)
    Event_11105220(1, 1100301, 11105211, 10.0, 11105260)
    Event_11105220(2, 1100302, 11105212, 10.0, 11105270)
    Event_11105220(3, 1100303, 11105213, 10.0, 11105280)
    Event_11105250(
        0,
        flag=11105210,
        character=1100300,
        command_id=1,
        region=1102040,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105232
    )
    Event_11105250(
        1,
        flag=11105210,
        character=1100300,
        command_id=2,
        region=1102020,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105230
    )
    Event_11105250(
        2,
        flag=11105210,
        character=1100300,
        command_id=3,
        region=1102030,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105231
    )
    Event_11105250(
        3,
        flag=11105210,
        character=1100300,
        command_id=4,
        region=1102020,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105230
    )
    Event_11105250(
        4,
        flag=11105210,
        character=1100300,
        command_id=5,
        region=1102050,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105233
    )
    Event_11105250(
        5,
        flag=11105210,
        character=1100300,
        command_id=6,
        region=1102040,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105232
    )
    Event_11105260(
        0,
        flag=11105211,
        character=1100301,
        command_id=1,
        region=1102040,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105236
    )
    Event_11105260(
        1,
        flag=11105211,
        character=1100301,
        command_id=2,
        region=1102020,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105234
    )
    Event_11105260(
        2,
        flag=11105211,
        character=1100301,
        command_id=3,
        region=1102030,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105235
    )
    Event_11105260(
        3,
        flag=11105211,
        character=1100301,
        command_id=4,
        region=1102020,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105234
    )
    Event_11105260(
        4,
        flag=11105211,
        character=1100301,
        command_id=5,
        region=1102050,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105237
    )
    Event_11105260(
        5,
        flag=11105211,
        character=1100301,
        command_id=6,
        region=1102040,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105236
    )
    Event_11105270(
        0,
        flag=11105212,
        character=1100302,
        command_id=1,
        region=1102040,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105240
    )
    Event_11105270(
        1,
        flag=11105212,
        character=1100302,
        command_id=2,
        region=1102020,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105238
    )
    Event_11105270(
        2,
        flag=11105212,
        character=1100302,
        command_id=3,
        region=1102030,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105239
    )
    Event_11105270(
        3,
        flag=11105212,
        character=1100302,
        command_id=4,
        region=1102020,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105238
    )
    Event_11105270(
        4,
        flag=11105212,
        character=1100302,
        command_id=5,
        region=1102050,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105241
    )
    Event_11105270(
        5,
        flag=11105212,
        character=1100302,
        command_id=6,
        region=1102040,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105240
    )
    Event_11105280(
        0,
        flag=11105213,
        character=1100303,
        command_id=1,
        region=1102040,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105244
    )
    Event_11105280(
        1,
        flag=11105213,
        character=1100303,
        command_id=2,
        region=1102020,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105242
    )
    Event_11105280(
        2,
        flag=11105213,
        character=1100303,
        command_id=3,
        region=1102030,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105243
    )
    Event_11105280(
        3,
        flag=11105213,
        character=1100303,
        command_id=4,
        region=1102020,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105242
    )
    Event_11105280(
        4,
        flag=11105213,
        character=1100303,
        command_id=5,
        region=1102050,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105245
    )
    Event_11105280(5, 11105213, 1100303, 6, 1102040, 11105242, 11105245, 11105244)


@UnknownRestart(11105190)
def Event_11105190(_, character: int, animation_id: int, animation_id_1: int, flag: int, flag_1: int):
    """Event 11105190"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    DisableCharacterCollision(character)
    DisableGravity(character)
    AddSpecialEffect(character, 4160)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, 51100260)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1202021)
    IfCharacterInsideRegion(2, PLAYER, region=1102040)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(character)
    EnableGravity(character)
    SetStandbyAnimationSettings(character)
    SkipLinesIfFinishedConditionFalse(5, condition=1)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    CancelSpecialEffect(character, 4160)
    SetNest(character, region=1102020)
    EnableFlag(flag)
    Restart()
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    CancelSpecialEffect(character, 4160)
    SetNest(character, region=1102040)
    EnableFlag(flag_1)
    Restart()


@UnknownRestart(11105195)
def Event_11105195(_, character: int, flag: int):
    """Event 11105195"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(flag)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(-1, PLAYER, region=1102050)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 3006)


@UnknownRestart(11105200)
def Event_11105200(
    _,
    flag: int,
    flag_1: int,
    event_slot: int,
    event_id: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
):
    """Event 11105200"""
    IfFlagEnabled(0, flag)
    IfFlagDisabled(1, flag_2)
    IfCharacterInsideRegion(1, PLAYER, region=1102020)
    IfFlagDisabled(2, flag_3)
    IfCharacterInsideRegion(2, PLAYER, region=1102030)
    IfFlagDisabled(3, flag_4)
    IfCharacterInsideRegion(3, PLAYER, region=1102040)
    IfFlagDisabled(4, flag_5)
    IfCharacterInsideRegion(4, PLAYER, region=1102050)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    RestartEvent(event_id=11105220, event_slot=event_slot)
    SkipLinesIfFinishedConditionFalse(6, condition=1)
    SkipLinesIfFlagDisabled(1, flag_3)
    RestartEvent(event_id=event_id, event_slot=3)
    SkipLinesIfFlagDisabled(1, flag_4)
    RestartEvent(event_id=event_id, event_slot=1)
    SkipLinesIfFlagDisabled(1, flag_5)
    RestartEvent(event_id=event_id, event_slot=5)
    SkipLinesIfFinishedConditionFalse(6, condition=2)
    SkipLinesIfFlagDisabled(1, flag_2)
    RestartEvent(event_id=event_id, event_slot=2)
    SkipLinesIfFlagDisabled(1, flag_4)
    RestartEvent(event_id=event_id, event_slot=1)
    SkipLinesIfFlagDisabled(1, flag_5)
    RestartEvent(event_id=event_id, event_slot=5)
    SkipLinesIfFinishedConditionFalse(6, condition=3)
    SkipLinesIfFlagDisabled(1, flag_2)
    RestartEvent(event_id=event_id)
    SkipLinesIfFlagDisabled(1, flag_3)
    RestartEvent(event_id=event_id, event_slot=3)
    SkipLinesIfFlagDisabled(1, flag_5)
    RestartEvent(event_id=event_id, event_slot=5)
    SkipLinesIfFinishedConditionFalse(6, condition=4)
    SkipLinesIfFlagDisabled(1, flag_2)
    RestartEvent(event_id=event_id)
    SkipLinesIfFlagDisabled(1, flag_3)
    RestartEvent(event_id=event_id, event_slot=3)
    SkipLinesIfFlagDisabled(1, flag_4)
    RestartEvent(event_id=event_id, event_slot=4)
    IfFlagDisabled(0, flag_1)
    Restart()


@UnknownRestart(11105220)
def Event_11105220(_, character: int, flag: int, seconds: float, event_id: int):
    """Event 11105220"""
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    Wait(seconds)
    RestartIfFlagDisabled(flag)
    DisableFlag(flag)
    RestartEvent(event_id=event_id)
    RestartEvent(event_id=event_id, event_slot=1)
    RestartEvent(event_id=event_id, event_slot=2)
    RestartEvent(event_id=event_id, event_slot=3)
    RestartEvent(event_id=event_id, event_slot=4)
    RestartEvent(event_id=event_id, event_slot=5)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@UnknownRestart(11105250)
def Event_11105250(
    _,
    flag: int,
    character: int,
    command_id: int,
    region: int,
    first_flag: int,
    last_flag: int,
    flag_1: int,
):
    """Event 11105250"""
    SkipLinesIfFlagEnabled(2, flag)
    IfCharacterDead(0, character)
    End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region)
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@UnknownRestart(11105260)
def Event_11105260(
    _,
    flag: int,
    character: int,
    command_id: int,
    region: int,
    first_flag: int,
    last_flag: int,
    flag_1: int,
):
    """Event 11105260"""
    SkipLinesIfFlagEnabled(2, flag)
    IfCharacterDead(0, character)
    End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region)
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@UnknownRestart(11105270)
def Event_11105270(
    _,
    flag: int,
    character: int,
    command_id: int,
    region: int,
    first_flag: int,
    last_flag: int,
    flag_1: int,
):
    """Event 11105270"""
    SkipLinesIfFlagEnabled(2, flag)
    IfCharacterDead(0, character)
    End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region)
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@UnknownRestart(11105280)
def Event_11105280(
    _,
    flag: int,
    character: int,
    command_id: int,
    region: int,
    first_flag: int,
    last_flag: int,
    flag_1: int,
):
    """Event 11105280"""
    SkipLinesIfFlagEnabled(2, flag)
    IfCharacterDead(0, character)
    End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region)
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@NeverRestart(11100600)
def Event_11100600(_, obj: int, obj_act_id: int):
    """Event 11100600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()
    DisableTreasure(obj=obj)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(11100510)
def Event_11100510(_, character: int, flag: int):
    """Event 11100510"""
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, flag)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(character)
    IfFlagEnabled(0, 703)
    EnableFlag(flag)
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11100520)
def Event_11100520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11100520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(character)
    End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11100530)
def Event_11100530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11100530"""
    IfFlagEnabled(1, 1690)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfHealthGreaterThan(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11100531)
def Event_11100531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11100531"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableCharacter(character)
    End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11100040)
def Event_11100040():
    """Event 11100040"""
    DisableNetworkSync()
    Wait(1.0)
    EndIfFlagEnabled(11100700)
    RegisterLadder(start_climbing_flag=11100012, stop_climbing_flag=11100013, obj=1101141)


@NeverRestart(11100532)
def Event_11100532(_, character: int, first_flag: int, last_flag: int, flag: int, flag_1: int, character_1: int):
    """Event 11100532"""
    DisableMapPiece(map_piece_id=1103100)
    DisableMapCollision(collision=1103101)
    DisableObject(1101750)
    DeleteVFX(1101751, erase_root_only=False)
    IfFlagEnabled(0, 11100700)
    DisableFlagRange((first_flag, last_flag))
    SkipLinesIfFlagDisabled(2, 8111)
    EnableFlag(flag)
    SkipLines(1)
    EnableFlag(flag_1)
    EnableMapPiece(map_piece_id=1103100)
    EnableMapCollision(collision=1103101)
    DisableObject(1101141)
    EnableObject(1101750)
    CreateVFX(1101751)
    EnableCharacter(character)
    EnableCharacter(character_1)
    SetTeamType(character_1, TeamType.WhitePhantom)
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
def Event_11100533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11100533"""
    IfFlagEnabled(1, 1606)
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(8110)


@NeverRestart(11100534)
def Event_11100534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11100534"""
    IfFlagEnabled(1, 1607)
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(8110)


@NeverRestart(11100535)
def Event_11100535(_, character: int, first_flag: int, last_flag: int, flag: int, flag_1: int):
    """Event 11100535"""
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, 11100700)
    IfFlagEnabled(1, 8110)
    IfConditionTrue(0, input_condition=1)
    RemoveGoodFromPlayer(item=116)
    EnableFlag(11100300)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    SkipLinesIfFlagDisabled(2, 8111)
    EnableFlag(flag)
    SkipLines(1)
    EnableFlag(flag_1)
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
