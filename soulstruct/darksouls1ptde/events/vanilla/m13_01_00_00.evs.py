"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    if FlagEnabled(7):
        RegisterBonfire(bonfire_flag=11310920, obj=1311950)
    RegisterBonfire(bonfire_flag=11310992, obj=1311960)
    RegisterBonfire(bonfire_flag=11310984, obj=1311961)
    RegisterLadder(start_climbing_flag=11310010, stop_climbing_flag=11310011, obj=1311140)
    RegisterLadder(start_climbing_flag=11310012, stop_climbing_flag=11310013, obj=1311141)
    RegisterLadder(start_climbing_flag=11310014, stop_climbing_flag=11310015, obj=1311142)
    RegisterLadder(start_climbing_flag=11310016, stop_climbing_flag=11310017, obj=1311143)
    RegisterLadder(start_climbing_flag=11310018, stop_climbing_flag=11310019, obj=1311144)
    RegisterLadder(start_climbing_flag=11310020, stop_climbing_flag=11310021, obj=1311145)
    RegisterLadder(start_climbing_flag=11310022, stop_climbing_flag=11310023, obj=1311146)
    RegisterLadder(start_climbing_flag=11310024, stop_climbing_flag=11310025, obj=1311147)
    RegisterLadder(start_climbing_flag=11310026, stop_climbing_flag=11310027, obj=1311148)
    SkipLinesIfClient(2)
    EnableFlag(401)
    DisableFlag(11310000)
    AND_1.Add(Client())
    AND_1.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    SkipLinesIfConditionTrue(2, AND_1)
    DisableObject(1311994)
    DeleteVFX(1311995, erase_root_only=False)
    if FlagDisabled(11310810):
        DisableTreasure(obj=1311600)
        DisableObject(1311600)
    if FlagEnabled(11310810):
        EnableTreasure(obj=1311600)
    Event_11310090(0, obj=1311700, vfx_id=1311701, destination=1312600, destination_1=1312601)
    Event_11315040()
    Event_11315041()
    Event_11315042()
    Event_11310095()
    Event_11315100()
    Event_11310051()
    Event_11310052()
    Event_11310053()
    Event_11310054()
    Event_11310100()
    Event_11315080()
    Event_11315050(0, character=1310200, entity=1310200, seconds=0.0)
    Event_11315050(1, character=1310201, entity=1310202, seconds=0.0)
    Event_11315050(2, character=1310202, entity=1310202, seconds=0.0)
    Event_11315060(0, character=1310203, flag=51310100, seconds=0.0)
    Event_11315060(1, character=1310204, flag=51310100, seconds=0.20000000298023224)
    Event_11315060(2, character=1310205, flag=51310100, seconds=0.8999999761581421)
    Event_11315060(3, character=1310206, flag=51310100, seconds=1.0)
    Event_11315070(0, character=1310207, region=1312251, seconds=0.0)
    Event_11315070(1, character=1310208, region=1312251, seconds=0.20000000298023224)
    Event_11315070(2, character=1310209, region=1312251, seconds=0.4000000059604645)
    Event_11315070(3, character=1310210, region=1312251, seconds=0.6000000238418579)
    Event_11315070(4, character=1310211, region=1312251, seconds=0.800000011920929)
    Event_11310820(0, character=1310300, item_lot_param_id=27903000)
    Event_11310820(1, character=1310400, item_lot_param_id=33005000)
    DisableSoundEvent(sound_id=1313800)
    if FlagEnabled(7):
        Event_11315392()
        DisableObject(1311990)
        DeleteVFX(1311991, erase_root_only=False)
    else:
        Event_11315390()
        Event_11315391()
        Event_11315393()
        Event_11315392()
        Event_11310001()
        Event_11315394()
        Event_11315395()
        Event_11315396()
        Event_11315398()
        Event_11315350(0, character=1310120)
        Event_11315350(1, character=1310121)
        Event_11315350(2, character=1310122)
        Event_11315350(3, character=1310123)
    Event_11315350(4, character=1310124)
    Event_11315350(5, 1310125)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6551, event_flag=8948)
    Event_11315030()
    Event_11310810()
    HumanityRegistration(6071, event_flag=8358)
    SkipLinesIfFlagEnabled(2, 1174)
    SkipLinesIfFlagEnabled(1, 1173)
    DisableCharacter(6071)
    Event_11310502(0, character=6071, flag=1176)
    Event_11310503(0, character=6071, flag=1179)
    Event_11310533(0, character=6071, first_flag=1170, last_flag=1181, flag=1177)
    Event_11310534(0, character=6071, first_flag=1170, last_flag=1181, flag=1180)
    Event_11310530()
    Event_11310531(0, character=6071, first_flag=1170, last_flag=1181, flag=1174)
    Event_11310532(0, character=6071, first_flag=1170, last_flag=1181, flag=1175)
    if FlagDisabled(1216):
        DisableCharacter(6091)
    SetTeamType(6091, TeamType.HostileAlly)
    Event_11310520(1, character=6091, first_flag=1210, last_flag=1219, flag=1214)
    if FlagDisabled(1226):
        DisableCharacter(6101)
    SetTeamType(6101, TeamType.HostileAlly)
    Event_11310520(2, character=6101, first_flag=1220, last_flag=1229, flag=1224)
    HumanityRegistration(6321, event_flag=8478)
    SkipLinesIfFlagRangeAnyEnabled(1, (1623, 1625))
    DisableCharacter(6321)
    Event_11310501(0, character=6321, flag=1627)
    Event_11310543(0, character=6321, flag=1625)
    Event_11310542(0, character=6321, flag=1628)
    Event_11310540(0, character=6321, first_flag=1620, last_flag=1631, flag=1623)
    Event_11310541(0, character=6321, first_flag=1620, last_flag=1631, flag=1624)
    Event_11310002()


@NeverRestart(11310090)
def Event_11310090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11310090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11315040)
def Event_11315040():
    """Event 11315040"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1310900)
    DisableCharacter(1310901)
    DisableCharacter(1310902)
    DisableCharacter(1310903)
    DisableCharacter(1310904)
    DisableCharacter(1310905)
    DisableCharacter(1310906)
    DisableCharacter(1310907)
    DisableCharacter(1310908)
    DisableCharacter(1310909)
    
    MAIN.Await(FlagEnabled(11310060))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1310900)
    EnableCharacter(1310901)
    EnableCharacter(1310902)
    EnableCharacter(1310903)
    EnableCharacter(1310904)
    EnableCharacter(1310905)
    EnableCharacter(1310906)
    EnableCharacter(1310907)
    EnableCharacter(1310908)
    EnableCharacter(1310909)


@RestartOnRest(11315041)
def Event_11315041():
    """Event 11315041"""
    OR_1.Add(FlagEnabled(11315045))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11310060)
    DisableFlag(11315045)
    EnableFlag(5001)
    Kill(1310900)
    Kill(1310901)
    Kill(1310902)
    Kill(1310903)
    Kill(1310904)
    Kill(1310905)
    Kill(1310906)
    Kill(1310907)
    Kill(1310908)
    Kill(1310909)


@RestartOnRest(11315042)
def Event_11315042():
    """Event 11315042"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11310060))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11310060))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11310060))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11310060))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11310060))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11310060))
    if not OR_6:
        return RESTART
    EnableFlag(11310060)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    if not AND_7:
        return RESTART
    DisableFlag(11310060)
    EnableFlag(11315045)


@NeverRestart(11310095)
def Event_11310095():
    """Event 11310095"""
    if FlagEnabled(11800100):
        EnableFlag(11310096)
        DisableObject(1311710)
        DeleteVFX(1311711, erase_root_only=False)
        DisableFlag(401)
        End()
    if FlagEnabled(11310096):
        DisableObject(1311710)
        DeleteVFX(1311711, erase_root_only=False)
        End()
    if Client():
        return
    
    MAIN.Await(ActionButton(
        prompt_text=10010410,
        anchor_entity=1312610,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1311710,
    ))
    
    DisplayStatus(10010630)
    Restart()


@NeverRestart(11315390)
def Event_11315390():
    """Event 11315390"""
    AND_1.Add(FlagDisabled(7))
    AND_1.Add(CharacterAlive(1310800))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1312998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1311990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1312997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11315391)
def Event_11315391():
    """Event 11315391"""
    AND_1.Add(FlagDisabled(7))
    AND_1.Add(FlagEnabled(11315393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1312998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1311990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1312997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11315393)
def Event_11315393():
    """Event 11315393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(7))
        AND_1.Add(FlagEnabled(11315390))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1310800)
    DisableFlag(11310050)


@RestartOnRest(11315392)
def Event_11315392():
    """Event 11315392"""
    if FlagEnabled(7):
        DisableCharacter(1310800)
        Kill(1310800)
        DisableCharacter(1310810)
        Kill(1310810)
        DisableCharacter(1310120)
        DisableCharacter(1310121)
        DisableCharacter(1310122)
        DisableCharacter(1310123)
        DisableCharacter(1310124)
        DisableCharacter(1310125)
        Kill(1310120)
        Kill(1310121)
        Kill(1310122)
        Kill(1310123)
        Kill(1310124)
        Kill(1310125)
        End()
    SkipLinesIfThisEventFlagEnabled(1)
    SkipLinesIfFlagEnabled(1, 11310000)
    DisableCharacter(1310800)
    DisableAI(1310800)
    SetStandbyAnimationSettings(1310120, standby_animation=9001)
    SetStandbyAnimationSettings(1310121, standby_animation=9001)
    SetStandbyAnimationSettings(1310122, standby_animation=9001)
    SetStandbyAnimationSettings(1310123, standby_animation=9001)
    SetStandbyAnimationSettings(1310124, standby_animation=9001)
    SetStandbyAnimationSettings(1310125, standby_animation=9001)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11310050))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1312999))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(1310810)
    SkipLinesIfFlagEnabled(7, 11310000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130100, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(130100, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1310800)
    EnableFlag(11310000)
    EnableAI(1310800)
    EnableBossHealthBar(1310800, name=5220)
    EnableFlag(11315392)
    DisableNetworkSync()
    SetStandbyAnimationSettings(1310120)
    ForceAnimation(1310120, 9061)
    Wait(0.30000001192092896)
    SetStandbyAnimationSettings(1310121, cancel_animation=9061)
    ForceAnimation(1310121, 9061)
    Wait(0.5)
    SetStandbyAnimationSettings(1310122, cancel_animation=9061)
    ForceAnimation(1310122, 9061)
    Wait(0.20000000298023224)
    SetStandbyAnimationSettings(1310123, cancel_animation=9061)
    ForceAnimation(1310123, 9061)
    Wait(0.30000001192092896)
    SetStandbyAnimationSettings(1310124, cancel_animation=9061)
    ForceAnimation(1310124, 9061)
    Wait(0.699999988079071)
    SetStandbyAnimationSettings(1310125, cancel_animation=9061)
    ForceAnimation(1310125, 9061)


@NeverRestart(11310001)
def Event_11310001():
    """Event 11310001"""
    DisableObject(1311950)
    
    MAIN.Await(CharacterDead(1310800))
    
    EnableFlag(7)
    KillBoss(game_area_param_id=1310800)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=35)
    DisableObject(1311990)
    DeleteVFX(1311991)
    Kill(1310810)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1311950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1311950)
    RegisterBonfire(bonfire_flag=11310920, obj=1311950)


@NeverRestart(11315394)
def Event_11315394():
    """Event 11315394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(7))
    AND_1.Add(FlagEnabled(11315392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11315391))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1313800)


@NeverRestart(11315395)
def Event_11315395():
    """Event 11315395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(7))
    AND_1.Add(FlagEnabled(11315394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1313800)


@NeverRestart(11315396)
def Event_11315396():
    """Event 11315396"""
    MAIN.Await(HealthRatio(1310800) <= 0.0)
    
    if FlagEnabled(11315370):
        Kill(1310110)
        Kill(1310111)
        Kill(1310112)
        Kill(1310113)
        Kill(1310114)
        Kill(1310115)
        End()
    if FlagEnabled(11315371):
        Kill(1310110, award_souls=True)
        Kill(1310111, award_souls=True)
        Kill(1310112)
        Kill(1310113)
        Kill(1310114)
        Kill(1310115)
        End()
    if FlagEnabled(11315372):
        Kill(1310110, award_souls=True)
        Kill(1310111, award_souls=True)
        Kill(1310112, award_souls=True)
        Kill(1310113, award_souls=True)
        Kill(1310114)
        Kill(1310115)
        End()
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=True)
    Kill(1310113, award_souls=True)
    Kill(1310114, award_souls=True)
    Kill(1310115, award_souls=True)


@RestartOnRest(11315397)
def Event_11315397():
    """Event 11315397"""
    DisableObject(1311200)
    DisableObject(1311201)
    DisableObject(1311202)
    DisableCharacter(1310110)
    DisableCharacter(1310111)
    DisableCharacter(1310112)
    DisableCharacter(1310113)
    DisableCharacter(1310114)
    DisableCharacter(1310115)
    Event_11315370(
        0,
        flag=11315392,
        part_index=2,
        npc_part_id=5220,
        npc_part_id_1=5220,
        obj=1311200,
        character=1310110,
        character_1=1310113,
        animation_id=8000,
    )
    Event_11315370(
        1,
        flag=11315370,
        part_index=3,
        npc_part_id=5221,
        npc_part_id_1=5221,
        obj=1311201,
        character=1310111,
        character_1=1310114,
        animation_id=8010,
    )
    Event_11315370(
        2,
        flag=11315371,
        part_index=4,
        npc_part_id=5222,
        npc_part_id_1=5222,
        obj=1311202,
        character=1310112,
        character_1=1310115,
        animation_id=8020,
    )
    
    MAIN.Await(CharacterBackreadEnabled(1310800))
    
    SetDisplayMask(1310800, bit_index=0, switch_type=OnOffChange.On)


@RestartOnRest(11315398)
def Event_11315398():
    """Event 11315398"""
    AND_1.Add(FlagEnabled(11315390))
    AND_1.Add(CharacterTargeting(targeting_character=1310800, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(1310800, tae_event_id=700))
    
    MAIN.Await(AND_1)
    
    MoveObjectToCharacter(1311250, character=PLAYER)
    
    MAIN.Await(CharacterHasTAEEvent(1310800, tae_event_id=710))
    
    CreateHazard(
        obj_flag=11315399,
        obj=1311250,
        model_point=1,
        behavior_param_id=11300,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.30000001192092896,
        repetition_time=0.0,
    )
    CreateTemporaryVFX(vfx_id=15224, anchor_entity=1311250, anchor_type=CoordEntityType.Object)
    Restart()


@UnknownRestart(11315370)
def Event_11315370(
    _,
    flag: int,
    part_index: short,
    npc_part_id: short,
    npc_part_id_1: int,
    obj: int,
    character: int,
    character_1: int,
    animation_id: int,
):
    """Event 11315370"""
    MAIN.Await(FlagEnabled(flag))
    
    CreateNPCPart(1310800, npc_part_id=npc_part_id, part_index=part_index, part_health=200)
    AND_1.Add(HealthRatio(1310800) > 0.0)
    AND_1.Add(CharacterPartHealth(1310800, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(1310800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    SkipLinesIfFlagEnabled(5, 11315370)
    SetCollisionMask(1310800, bit_index=1, switch_type=OnOffChange.Off)
    SetDisplayMask(1310800, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=4, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=7, switch_type=OnOffChange.On)
    SkipLines(10)
    if FlagDisabled(11315371):
        SetCollisionMask(1310800, bit_index=2, switch_type=OnOffChange.Off)
        SetDisplayMask(1310800, bit_index=2, switch_type=OnOffChange.On)
        SetDisplayMask(1310800, bit_index=5, switch_type=OnOffChange.On)
        SetDisplayMask(1310800, bit_index=8, switch_type=OnOffChange.On)
    else:
        SetCollisionMask(1310800, bit_index=3, switch_type=OnOffChange.Off)
        SetDisplayMask(1310800, bit_index=3, switch_type=OnOffChange.On)
        SetDisplayMask(1310800, bit_index=6, switch_type=OnOffChange.On)
        SetDisplayMask(1310800, bit_index=9, switch_type=OnOffChange.On)
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=1310800, model_point=50)
    DestroyObject(obj)
    EnableCharacter(character)
    Move(
        character,
        destination=1310800,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=1310800,
    )
    ForceAnimation(character, 7000)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=1310800,
        destination_type=CoordEntityType.Character,
        model_point=51,
        copy_draw_parent=1310800,
    )
    ForceAnimation(character_1, 7000)
    ForceAnimation(1310800, animation_id, wait_for_completion=True)


@RestartOnRest(11315350)
def Event_11315350(_, character: int):
    """Event 11315350"""
    if FlagEnabled(7):
        return
    if ThisEventSlotFlagEnabled():
        return
    EnableImmortality(character)
    
    MAIN.Await(HealthRatio(1310800) <= 0.0)
    
    RemoveSpecialEffect(character, 5451)
    DisableImmortality(character)
    Kill(character, award_souls=True)


@RestartOnRest(11315100)
def Event_11315100():
    """Event 11315100"""
    Event_11315091()
    Event_11315092()
    Event_11315150(0, flag=11315100, vfx_id=1313200, flag_1=11315101)
    Event_11315150(1, flag=11315101, vfx_id=1313201, flag_1=11315102)
    Event_11315150(2, flag=11315102, vfx_id=1313202, flag_1=11315103)
    Event_11315150(3, flag=11315103, vfx_id=1313203, flag_1=11315104)
    Event_11315150(4, flag=11315104, vfx_id=1313204, flag_1=11315105)
    Event_11315150(5, flag=11315105, vfx_id=1313205, flag_1=11315106)
    Event_11315150(6, flag=11315106, vfx_id=1313206, flag_1=11315107)
    Event_11315150(7, flag=11315107, vfx_id=1313207, flag_1=11315108)
    Event_11315150(8, flag=11315108, vfx_id=1313208, flag_1=11315109)
    Event_11315150(9, flag=11315109, vfx_id=1313209, flag_1=11315110)
    Event_11315150(10, flag=11315110, vfx_id=1313210, flag_1=11315111)
    Event_11315150(11, flag=11315111, vfx_id=1313211, flag_1=11315112)
    Event_11315150(12, flag=11315112, vfx_id=1313212, flag_1=11315113)
    Event_11315150(13, flag=11315113, vfx_id=1313213, flag_1=11315114)
    Event_11315150(14, flag=11315114, vfx_id=1313214, flag_1=11315115)
    Event_11315150(15, flag=11315115, vfx_id=1313215, flag_1=11315116)
    Event_11315150(16, flag=11315116, vfx_id=1313216, flag_1=11315117)
    Event_11315150(17, flag=11315117, vfx_id=1313217, flag_1=11315118)
    Event_11315150(18, flag=11315118, vfx_id=1313218, flag_1=11315119)
    Event_11315150(19, flag=11315119, vfx_id=1313219, flag_1=11315120)
    Event_11315150(20, flag=11315120, vfx_id=1313220, flag_1=11315121)
    Event_11315150(21, flag=11315121, vfx_id=1313221, flag_1=11315122)
    Event_11315150(22, flag=11315122, vfx_id=1313222, flag_1=11315123)
    Event_11315150(23, flag=11315123, vfx_id=1313223, flag_1=11315124)
    Event_11315150(24, flag=11315100, vfx_id=1313224, flag_1=11315125)
    Event_11315150(25, flag=11315125, vfx_id=1313225, flag_1=11315126)
    Event_11315150(26, flag=11315126, vfx_id=1313226, flag_1=11315127)
    Event_11315150(27, flag=11315127, vfx_id=1313227, flag_1=11315128)
    Event_11315150(28, flag=11315128, vfx_id=1313228, flag_1=11315129)
    Event_11315150(29, flag=11315129, vfx_id=1313229, flag_1=11315130)
    Event_11315150(30, flag=11315130, vfx_id=1313230, flag_1=11315131)
    Event_11315150(31, flag=11315131, vfx_id=1313231, flag_1=11315132)
    Event_11315150(32, flag=11315132, vfx_id=1313232, flag_1=11315133)
    Event_11315150(33, flag=11315133, vfx_id=1313233, flag_1=11315134)
    Event_11315150(34, flag=11315134, vfx_id=1313234, flag_1=11315135)
    Event_11315150(35, flag=11315135, vfx_id=1313235, flag_1=11315136)
    Event_11315150(36, flag=11315136, vfx_id=1313236, flag_1=11315137)
    Event_11315150(37, flag=11315137, vfx_id=1313237, flag_1=11315138)
    Event_11315150(38, flag=11315138, vfx_id=1313238, flag_1=11315139)
    Event_11315150(39, flag=11315139, vfx_id=1313239, flag_1=11315140)
    Event_11315150(40, flag=11315140, vfx_id=1313240, flag_1=11315141)
    Event_11315150(41, flag=11315141, vfx_id=1313241, flag_1=11315142)
    Event_11315150(42, flag=11315142, vfx_id=1313242, flag_1=11315143)
    Event_11315150(43, flag=11315143, vfx_id=1313243, flag_1=11315144)
    Event_11315150(44, flag=11315144, vfx_id=1313244, flag_1=11315145)
    Event_11315150(45, flag=11315145, vfx_id=1313245, flag_1=11315146)
    Event_11315150(46, flag=11315146, vfx_id=1313246, flag_1=11315147)
    Event_11315150(47, flag=11315147, vfx_id=1313247, flag_1=11315148)
    Event_11315150(48, 11315148, 1313248, 11315149)


@UnknownRestart(11315150)
def Event_11315150(_, flag: int, vfx_id: int, flag_1: int):
    """Event 11315150"""
    DisableNetworkSync()
    if FlagDisabled(11315090):
        DeleteVFX(vfx_id, erase_root_only=False)
        AND_1.Add(FlagEnabled(11315090))
        AND_1.Add(FlagEnabled(flag))
    
        MAIN.Await(AND_1)
    CreateVFX(vfx_id)
    EnableFlag(flag_1)
    
    MAIN.Await(FlagDisabled(11315090))
    
    DeleteVFX(vfx_id)
    DisableFlag(flag_1)
    Restart()


@UnknownRestart(11315091)
def Event_11315091():
    """Event 11315091"""
    AND_1.Add(SkullLanternActive())
    AND_1.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11315090)
    RestartEvent(event_id=11315092)
    Restart()


@UnknownRestart(11315092)
def Event_11315092():
    """Event 11315092"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11315090))
    
    Wait(3.0)
    DisableFlag(11315090)
    Restart()


@RestartOnRest(11315050)
def Event_11315050(_, character: int, entity: int, seconds: float):
    """Event 11315050"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    SetStandbyAnimationSettings(character, standby_animation=9000)
    
    MAIN.Await(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=5.0))
    
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    ReplanAI(character)


@RestartOnRest(11315060)
def Event_11315060(_, character: int, flag: int, seconds: float):
    """Event 11315060"""
    if FlagEnabled(flag):
        SetStandbyAnimationSettings(character)
        End()
    SetStandbyAnimationSettings(character, standby_animation=9000)
    AND_1.Add(Host())
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    ReplanAI(character)


@RestartOnRest(11315070)
def Event_11315070(_, character: int, region: int, seconds: float):
    """Event 11315070"""
    if FlagEnabled(region):
        SetStandbyAnimationSettings(character)
        End()
    SetStandbyAnimationSettings(character, standby_animation=9000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    ReplanAI(character)


@RestartOnRest(11315080)
def Event_11315080():
    """Event 11315080"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1310250)
    AND_1.Add(EntityWithinDistance(entity=1310250, other_entity=PLAYER, radius=7.0))
    AND_2.Add(Attacked(attacked_entity=1310250, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableAI(1310250)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    SetStandbyAnimationSettings(1310250, standby_animation=9000)
    ForceAnimation(1310250, 9070, wait_for_completion=True)
    Move(1310250, destination=1312250, destination_type=CoordEntityType.Region, short_move=True)
    OR_1.Add(EntityWithinDistance(entity=1310251, other_entity=PLAYER, radius=5.0))
    OR_1.Add(Attacked(attacked_entity=1310251, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(1310250, cancel_animation=9060)


@NeverRestart(11310051)
def Event_11310051():
    """Event 11310051"""
    DisableCharacter(1310810)
    DisableObject(1311300)
    DisableObjectActivation(1311300, obj_act_id=-1)
    
    MAIN.Await(FlagEnabled(11310050))
    
    if FlagDisabled(7):
        EnableCharacter(1310810)
    EnableObject(1311300)
    EnableObjectActivation(1311300, obj_act_id=-1)
    DisableCharacter(1310120)
    DisableCharacter(1310121)
    DisableCharacter(1310122)
    DisableCharacter(1310123)
    DisableCharacter(1310124)
    DisableCharacter(1310125)
    
    MAIN.Await(FlagDisabled(11310050))
    
    EnableCharacter(1310120)
    EnableCharacter(1310121)
    EnableCharacter(1310122)
    EnableCharacter(1310123)
    EnableCharacter(1310124)
    EnableCharacter(1310125)
    Restart()


@NeverRestart(11310052)
def Event_11310052():
    """Event 11310052"""
    MAIN.Await(ObjectActivated(obj_act_id=11315340))
    
    SetStandbyAnimationSettings(PLAYER, standby_animation=7151, death_animation=6082)
    Wait(3.0)
    PlayCutscene(130121, cutscene_flags=0, player_id=10000, move_to_region=1302010, game_map=CATACOMBS)
    PlayCutscene(130021, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    SetStandbyAnimationSettings(PLAYER)
    EnableObjectActivation(1311300, obj_act_id=-1)
    Restart()


@NeverRestart(11310053)
def Event_11310053():
    """Event 11310053"""
    MAIN.Await(FlagEnabled(11315020))
    
    RotateToFaceEntity(PLAYER, target_entity=1310810)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    
    MAIN.Await(FlagDisabled(11315020))
    
    SetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()


@NeverRestart(11310054)
def Event_11310054():
    """Event 11310054"""
    DisableNetworkSync()
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagEnabled(11310050))
    AND_1.Add(EntityWithinDistance(entity=1311300, other_entity=PLAYER, radius=2.0))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    SetStandbyAnimationSettings(PLAYER)
    EnableObjectActivation(1311300, obj_act_id=-1)
    
    MAIN.Await(EntityBeyondDistance(entity=1311300, other_entity=PLAYER, radius=3.0))
    
    Restart()


@NeverRestart(11310100)
def Event_11310100():
    """Event 11310100"""
    if ThisEventFlagEnabled():
        DisableObject(1311400)
        End()
    
    MAIN.Await(ObjectDestroyed(1311400))
    
    End()


@RestartOnRest(11310820)
def Event_11310820(_, character: int, item_lot_param_id: int):
    """Event 11310820"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot_param_id, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot_param_id, host_only=True)


@NeverRestart(11310510)
def Event_11310510(_, character: int, flag: int):
    """Event 11310510"""
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventSlotFlagDisabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11310520)
def Event_11310520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11310501)
def Event_11310501(_, character: int, flag: int):
    """Event 11310501"""
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    OR_7.Add(FlagEnabled(1623))
    OR_7.Add(FlagEnabled(1624))
    AND_1.Add(OR_7)
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(character)


@NeverRestart(11310502)
def Event_11310502(_, character: int, flag: int):
    """Event 11310502"""
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagDisabled(1179))
    AND_1.Add(FlagEnabled(1173))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(character)


@NeverRestart(11310503)
def Event_11310503(_, character: int, flag: int):
    """Event 11310503"""
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagDisabled(1179))
    AND_1.Add(FlagEnabled(1174))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SetAIParamID(character, ai_param_id=1)
    SaveRequest()
    EnableCharacter(character)


@NeverRestart(11310530)
def Event_11310530():
    """Event 11310530"""
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1176, 1181)))
    AND_7.Add(FlagEnabled(1171))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1195, 1198)))
    AND_7.Add(FlagEnabled(1202))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1213, 1215)))
    AND_7.Add(FlagEnabled(1211))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(1223, 1225)))
    AND_7.Add(FlagEnabled(1221))
    AND_1.Add(AND_7)
    AND_1.Add(FlagEnabled(11020600))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(AND_7)
    AND_2.Add(FlagEnabled(11300005))
    AND_3.Add(AND_7)
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    ClearEventValue(600, bit_count=4)
    EnableFlag(11020693)
    DisableFlagRange((1170, 1189))
    EnableFlag(1173)
    EnableCharacter(6071)
    DisableFlagRange((1190, 1209))
    EnableFlag(1192)
    DisableFlagRange((1210, 1219))
    EnableFlag(1216)
    EnableCharacter(6091)
    DisableFlagRange((1220, 1229))
    EnableFlag(1226)
    EnableCharacter(6101)


@NeverRestart(11310531)
def Event_11310531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310531"""
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagDisabled(1179))
    AND_1.Add(FlagEnabled(1173))
    AND_1.Add(FlagEnabled(1214))
    AND_1.Add(FlagEnabled(1224))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11310532)
def Event_11310532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310532"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagDisabled(1179))
    AND_1.Add(FlagEnabled(1174))
    AND_1.Add(FlagEnabled(11310590))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    ClearEventValue(600, bit_count=4)


@NeverRestart(11310533)
def Event_11310533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310533"""
    AND_1.Add(FlagDisabled(1179))
    OR_7.Add(FlagEnabled(1173))
    OR_7.Add(FlagEnabled(1176))
    AND_1.Add(OR_7)
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EndIfFinishedConditionFalse(input_condition=AND_2)
    DropMandatoryTreasure(character)


@NeverRestart(11310534)
def Event_11310534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310534"""
    AND_1.Add(FlagDisabled(1176))
    OR_7.Add(FlagEnabled(1174))
    OR_7.Add(FlagEnabled(1179))
    AND_1.Add(OR_7)
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EndIfFinishedConditionFalse(input_condition=AND_2)
    DropMandatoryTreasure(character)


@NeverRestart(11310540)
def Event_11310540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310540"""
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(1620, 1621)))
    AND_2.Add(FlagEnabled(6))
    AND_3.Add(FlagEnabled(1173))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11310541)
def Event_11310541(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11310541"""
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_1.Add(FlagEnabled(1623))
    AND_1.Add(FlagEnabled(11310002))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11310542)
def Event_11310542(_, character: int, flag: int):
    """Event 11310542"""
    AND_1.Add(FlagEnabled(1623))
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(1624))
    AND_2.Add(HealthRatio(character) <= 0.0)
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(1625)
    DisableFlag(1627)
    EnableFlag(flag)
    EndIfFinishedConditionFalse(input_condition=AND_3)
    DropMandatoryTreasure(character)


@NeverRestart(11310543)
def Event_11310543(_, character: int, flag: int):
    """Event 11310543"""
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_1.Add(FlagEnabled(1624))
    AND_1.Add(FlagEnabled(11310595))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(character)


@NeverRestart(11315030)
def Event_11315030():
    """Event 11315030"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11315031):
        return
    if FlagEnabled(7):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11310810))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1312001))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6551,
        region=1312000,
        summon_flag=11315031,
        dismissal_flag=11315032,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11310810)
def Event_11310810():
    """Event 11310810"""
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(11315031))
    AND_1.Add(FlagDisabled(11315032))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(6551)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(6551))
    
    EnableFlag(11310810)


@NeverRestart(11310002)
def Event_11310002():
    """Event 11310002"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_1.Add(FlagEnabled(1623))
    AND_1.Add(FlagDisabled(1638))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1313400))
    AND_2.Add(Host())
    AND_2.Add(FlagDisabled(1625))
    AND_2.Add(FlagDisabled(1627))
    AND_2.Add(FlagDisabled(1628))
    AND_2.Add(FlagEnabled(1623))
    AND_2.Add(FlagEnabled(1638))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1313400))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfMultiplayer(7)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    PlayCutscene(130111, cutscene_flags=0, player_id=10000, move_to_region=1312120, game_map=TOMB_OF_THE_GIANTS)
    SkipLines(1)
    PlayCutscene(130110, cutscene_flags=0, player_id=10000, move_to_region=1312120, game_map=TOMB_OF_THE_GIANTS)
    WaitFrames(frames=1)
    MoveToEntity(6321, destination=1312121, destination_type=CoordEntityType.Region)
    End()
    SkipLinesIfClient(7)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    PlayCutscene(
        130111,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1312120,
        game_map=TOMB_OF_THE_GIANTS,
    )
    SkipLines(1)
    PlayCutscene(
        130110,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1312120,
        game_map=TOMB_OF_THE_GIANTS,
    )
    WaitFrames(frames=1)
    MoveToEntity(6321, destination=1312121, destination_type=CoordEntityType.Region)
    End()
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    PlayCutscene(130111, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(1)
    PlayCutscene(130110, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    MoveToEntity(6321, destination=1312121, destination_type=CoordEntityType.Region)
