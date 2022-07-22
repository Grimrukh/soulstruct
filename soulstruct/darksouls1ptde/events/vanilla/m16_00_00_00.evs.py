"""
New Londo Ruins / Valley of Drakes

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    if FlagEnabled(13):
        RegisterBonfire(bonfire_flag=11600920, obj=1601950)
    RegisterBonfire(bonfire_flag=11600984, obj=1601961)
    RegisterLadder(start_climbing_flag=11600010, stop_climbing_flag=11600011, obj=1601140)
    RegisterLadder(start_climbing_flag=11600012, stop_climbing_flag=11600013, obj=1601141)
    EnableFlag(11600102)
    SkipLinesIfClient(7)
    EnableFlag(404)
    DisableObject(1601994)
    DeleteVFX(1601995, erase_root_only=False)
    DisableObject(1601996)
    DeleteVFX(1601997, erase_root_only=False)
    DisableObject(1601998)
    DeleteVFX(1601999, erase_root_only=False)
    DisableSpawner(entity=1603000)
    Event_11600090(0, obj=1601700, vfx_id=1601701, destination=1602600, destination_1=1602601)
    Event_11600090(1, obj=1601702, vfx_id=1601703, destination=1602602, destination_1=1602603)
    Event_11605090()
    Event_11605091()
    Event_11605092()
    Event_11605100()
    Event_11600150()
    Event_11600100()
    Event_11600101(0, obj=1601101, flag=11600102, animation_id=0)
    Event_11600110(0, obj_act_id=11600110, text=10010872, obj=1601111)
    Event_11600120(0, obj_act_id=11600120, text=10010867, obj=1601110, text_1=10010883, item=2008)
    Event_11600160()
    Event_11600200()
    Event_11600250()
    Event_11600199()
    Event_11600210()
    Event_11600251()
    Event_11600220()
    Event_11600252()
    Event_11600230()
    Event_11600253()
    Event_11600810()
    Event_11600400()
    Event_11605397()
    Event_11605398()
    Event_11605360(0, character=10000)
    Event_11605360(1, character=10001)
    Event_11605360(2, character=10002)
    Event_11605360(3, character=10003)
    Event_11605360(4, character=10004)
    Event_11605360(5, character=10005)
    DisableSoundEvent(sound_id=1603800)
    if FlagEnabled(13):
        Event_11605392()
        DisableObject(1601990)
        DeleteVFX(1601991, erase_root_only=False)
    else:
        Event_11605390()
        Event_11605391()
        Event_11605393()
        Event_11605392()
        Event_11600001()
        Event_11605394()
        Event_11605395()
        Event_11605396()
        Event_11605350(0, character=1600801)
        Event_11605350(1, character=1600802)
        Event_11605350(2, character=1600803)
        Event_11605350(3, character=1600804)
        Event_11605399()
    DisableSoundEvent(sound_id=1603801)
    Event_11605150(0, character=1600202, region=1602850)
    Event_11605150(1, character=1600204, region=1602850)
    Event_11605150(2, character=1600205, region=1602850)
    Event_11605150(3, character=1600211, region=1602850)
    Event_11605150(4, character=1600351, region=1602850)
    Event_11605150(5, character=1600356, region=1602850)
    Event_11605150(6, character=1600357, region=1602850)
    Event_11605150(7, character=1600250, region=1602850)
    Event_11605150(8, character=1600252, region=1602851)
    Event_11605150(9, character=1600253, region=1602851)
    Event_11605150(10, character=1600255, region=1602851)
    Event_11605150(11, character=1600200, region=1602852)
    Event_11605150(12, character=1600201, region=1602852)
    Event_11605150(13, character=1600206, region=1602852)
    Event_11605150(14, character=1600251, region=1602852)
    Event_11605150(15, character=1600254, region=1602852)
    Event_11605150(16, character=1600301, region=1602852)
    Event_11605150(17, character=1600302, region=1602852)
    Event_11605150(18, character=1600352, region=1602852)
    Event_11605150(19, character=1600353, region=1602852)
    Event_11605150(20, character=1600354, region=1602852)
    Event_11605150(21, character=1600360, region=1602852)
    Event_11605150(22, character=1600350, region=1602853)
    Event_11605150(23, character=1600355, region=1602853)
    Event_11605150(24, character=1600203, region=1602853)
    Event_11605150(25, character=1600207, region=1602853)
    Event_11605150(26, character=1600208, region=1602853)
    Event_11605150(27, character=1600209, region=1602853)
    Event_11605150(28, character=1600210, region=1602853)
    Event_11605150(29, character=1600358, region=1602854)
    Event_11605150(30, character=1600359, region=1602854)
    Event_11605150(31, character=1600361, region=1602854)
    Event_11605150(32, character=1600300, region=1602860)
    Event_11605150(33, character=1600310, region=1602860)
    Event_11605001(0, character=1600200, radius=5.0, cancel_animation=9060)
    Event_11605001(1, character=1600201, radius=5.0, cancel_animation=9060)
    Event_11605001(2, character=1600202, radius=7.0, cancel_animation=9060)
    Event_11605001(3, character=1600203, radius=7.0, cancel_animation=9060)
    Event_11605001(4, character=1600204, radius=6.0, cancel_animation=9060)
    Event_11605001(5, character=1600205, radius=6.0, cancel_animation=9060)
    Event_11605001(6, character=1600206, radius=3.0, cancel_animation=9060)
    Event_11605001(7, character=1600210, radius=5.0, cancel_animation=9060)
    Event_11605050(0, character=1600250, region=1602250, cancel_animation=3007, left=0, radius=0.0)
    Event_11605050(1, character=1600251, region=1602251, cancel_animation=3007, left=0, radius=0.0)
    Event_11605050(2, character=1600252, region=1602252, cancel_animation=3006, left=1, radius=5.0)
    Event_11605050(3, character=1600253, region=1602253, cancel_animation=3006, left=1, radius=5.0)
    Event_11605050(4, character=1600254, region=1602254, cancel_animation=3005, left=0, radius=0.0)
    Event_11605050(5, character=1600255, region=1602255, cancel_animation=3005, left=0, radius=0.0)
    Event_11605050(6, character=1600207, region=1602270, cancel_animation=9060, left=0, radius=0.0)
    Event_11605050(7, character=1600208, region=1602270, cancel_animation=9060, left=0, radius=0.0)
    Event_11605050(8, character=1600209, region=1602270, cancel_animation=9060, left=0, radius=0.0)
    Event_11605050(9, character=1600211, region=1602271, cancel_animation=9060, left=0, radius=0.0)
    Event_11605200(0, character=1600400, character_1=1600410, command_id=1, flag=11600100)
    Event_11605200(1, character=1600400, character_1=1600411, command_id=2, flag=11605200)
    Event_11605200(2, character=1600400, character_1=1600412, command_id=3, flag=11605201)
    Event_11605200(3, character=1600400, character_1=1600413, command_id=4, flag=11605202)
    Event_11605200(4, character=1600400, character_1=1600414, command_id=5, flag=11605203)
    Event_11605200(5, character=1600400, character_1=1600415, command_id=6, flag=11605204)
    Event_11605200(10, character=1600401, character_1=1600416, command_id=1, flag=11600100)
    Event_11605200(11, character=1600401, character_1=1600417, command_id=2, flag=11605210)
    Event_11605200(12, character=1600401, character_1=1600418, command_id=3, flag=11605211)
    Event_11605200(13, character=1600401, character_1=1600419, command_id=4, flag=11605212)
    Event_11605200(14, character=1600401, character_1=1600420, command_id=5, flag=11605213)
    Event_11605200(15, character=1600401, character_1=1600421, command_id=6, flag=11605214)
    Event_11605250(0, character=1600410)
    Event_11605250(1, character=1600411)
    Event_11605250(2, character=1600412)
    Event_11605250(3, character=1600413)
    Event_11605250(4, character=1600414)
    Event_11605250(5, character=1600415)
    Event_11605250(6, character=1600416)
    Event_11605250(7, character=1600417)
    Event_11605250(8, character=1600418)
    Event_11605250(9, character=1600419)
    Event_11605250(10, character=1600420)
    Event_11605250(11, character=1600421)
    Event_11600850(0, character=1600400)
    Event_11600850(1, character=1600401)
    Event_11600600(0, obj=1601650, obj_act_id=11600600)
    Event_11600600(1, obj=1601651, obj_act_id=11600601)
    Event_11600600(2, obj=1601652, obj_act_id=11600602)
    Event_11600650(0, obj=1601610, obj_1=1601310)
    Event_11600650(1, 1601611, 1601311)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6520, event_flag=8932)
    Event_11605030()
    Event_11605032()
    Event_11605033()
    HumanityRegistration(6180, event_flag=8406)
    SkipLinesIfFlagEnabled(2, 1315)
    SkipLinesIfFlagEnabled(1, 1313)
    SkipLines(1)
    DisableCharacter(6180)
    Event_11600510(0, character=6180, flag=1314)
    Event_11600520(0, character=6180, first_flag=1310, last_flag=1319, flag=1315)
    Event_11600530(0, character=6180, first_flag=1310, last_flag=1319, flag=1311)
    Event_11600531(0, character=6180, first_flag=1310, last_flag=1319, flag=1312)
    Event_11600532(0, character=6180, first_flag=1310, last_flag=1319, flag=1313)
    HumanityRegistration(6220, event_flag=8414)
    Event_11600510(1, character=6220, flag=1381)
    Event_11600520(1, character=6220, first_flag=1380, last_flag=1399, flag=1382)
    SetTeamTypeAndExitStandbyAnimation(6271, team_type=TeamType.HostileAlly)
    if FlagDisabled(1464):
        DisableCharacter(6271)
    Event_11600520(5, character=6271, first_flag=1460, last_flag=1489, flag=1462)
    Event_11600545(0, character=6271)
    SkipLinesIfFlagDisabled(2, 15)
    DisableCharacter(6340)
    SkipLinesIfFlagEnabled(11, 15)
    EnableImmortality(6340)
    SkipLinesIfFlagEnabled(2, 1677)
    SkipLinesIfFlagEnabled(1, 1676)
    SkipLines(1)
    DisableCharacter(6340)
    Event_11600537(0, character=6340, first_flag=1670, last_flag=1678, flag=1671)
    Event_11600538(0, character=6340, first_flag=1670, last_flag=1678, flag=1672)
    Event_11600539(0, character=6340, first_flag=1670, last_flag=1678, flag=1673)
    Event_11600540(0, character=6340, first_flag=1670, last_flag=1678, flag=1677)
    Event_11600541(0, character=6340, first_flag=1670, last_flag=1678, flag=1677)
    Event_11606200()


@ContinueOnRest(11600090)
def Event_11600090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11600090"""
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


@RestartOnRest(11605090)
def Event_11605090():
    """Event 11605090"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1600900)
    DisableCharacter(1600901)
    DisableCharacter(1600902)
    DisableCharacter(1600903)
    DisableCharacter(1600904)
    DisableCharacter(1600905)
    
    MAIN.Await(FlagEnabled(11600050))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1600900)
    EnableCharacter(1600901)
    EnableCharacter(1600902)
    EnableCharacter(1600903)
    EnableCharacter(1600904)
    EnableCharacter(1600905)


@RestartOnRest(11605091)
def Event_11605091():
    """Event 11605091"""
    OR_1.Add(FlagEnabled(11605095))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11600050)
    DisableFlag(11605095)
    EnableFlag(5001)
    Kill(1600900)
    Kill(1600901)
    Kill(1600902)
    Kill(1600903)
    Kill(1600904)
    Kill(1600905)


@RestartOnRest(11605092)
def Event_11605092():
    """Event 11605092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11600050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11600050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11600050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11600050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11600050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11600050))
    if not OR_6:
        return RESTART
    EnableFlag(11600050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    if not AND_7:
        return RESTART
    DisableFlag(11600050)
    EnableFlag(11605095)


@ContinueOnRest(11605390)
def Event_11605390():
    """Event 11605390"""
    AND_1.Add(FlagDisabled(13))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1601990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1602997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11605391)
def Event_11605391():
    """Event 11605391"""
    AND_1.Add(FlagDisabled(13))
    AND_1.Add(FlagEnabled(11605393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1601990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1602997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11605393)
def Event_11605393():
    """Event 11605393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(13))
        AND_1.Add(FlagEnabled(11605390))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1602996))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1600800)
    ActivateMultiplayerBuffs(1600801)
    ActivateMultiplayerBuffs(1600802)
    ActivateMultiplayerBuffs(1600803)
    ActivateMultiplayerBuffs(1600804)


@RestartOnRest(11605392)
def Event_11605392():
    """Event 11605392"""
    if FlagEnabled(13):
        DisableCharacter(1600800)
        DisableCharacter(1600801)
        DisableCharacter(1600802)
        DisableCharacter(1600803)
        DisableCharacter(1600804)
        Kill(1600800)
        Kill(1600801)
        Kill(1600802)
        Kill(1600803)
        Kill(1600804)
        EnableTreasure(obj=1601600)
        End()
    DisableAI(1600800)
    DisableAI(1600801)
    DisableAI(1600802)
    DisableAI(1600803)
    DisableAI(1600804)
    DisableCharacter(1600801)
    Kill(1600802)
    Kill(1600803)
    Kill(1600804)
    DisableGravity(1600800)
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(11605399))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1602999))
    
        MAIN.Await(AND_1)
    
        DisableNetworkSync()
        Wait(7.0)
    EnableCharacter(1600801)
    ForceAnimation(1600801, 6200)
    EnableAI(1600801)
    EnableAI(1600802)
    EnableAI(1600803)
    EnableAI(1600804)
    EnableBossHealthBar(1600800, name=5390)
    ReferDamageToEntity(1600801, target_entity=1600800)
    ReferDamageToEntity(1600802, target_entity=1600800)
    ReferDamageToEntity(1600803, target_entity=1600800)
    ReferDamageToEntity(1600804, target_entity=1600800)


@ContinueOnRest(11600001)
def Event_11600001():
    """Event 11600001"""
    DisableTreasure(obj=1601600)
    DisableObject(1601600)
    DisableObject(1601950)
    AND_1.Add(HealthRatio(1600800) <= 0.0)
    AND_1.Add(FlagEnabled(11605395))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160010, cutscene_flags=0, player_id=10000, move_to_region=1602120, game_map=NEW_LONDO_RUINS)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        160010,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1602120,
        game_map=NEW_LONDO_RUINS,
    )
    SkipLines(1)
    PlayCutscene(160010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(1600800)
    DisableCharacter(1600801)
    DisableCharacter(1600802)
    DisableCharacter(1600803)
    DisableCharacter(1600804)
    Kill(1600800, award_souls=True)
    Kill(1600801, award_souls=True)
    Kill(1600802, award_souls=True)
    Kill(1600803, award_souls=True)
    Kill(1600804, award_souls=True)
    
    MAIN.Await(CharacterDead(1600800))
    
    EnableFlag(13)
    DisableSpawner(entity=1603000)
    KillBoss(game_area_param_id=1600800)
    DisableObject(1601990)
    DeleteVFX(1601991)
    EnableTreasure(obj=1601600)
    EnableObject(1601600)
    if Client():
        return
    AwardAchievement(achievement_id=37)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1601950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1601950)
    RegisterBonfire(bonfire_flag=11600920, obj=1601950)


@ContinueOnRest(11605394)
def Event_11605394():
    """Event 11605394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(13))
    AND_1.Add(FlagEnabled(11605392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11605391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1603800)


@ContinueOnRest(11605395)
def Event_11605395():
    """Event 11605395"""
    DisableNetworkSync()
    AND_1.Add(HealthRatio(1600800) <= 0.0)
    AND_1.Add(FlagEnabled(11605394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1603800)


@ContinueOnRest(11605396)
def Event_11605396():
    """Event 11605396"""
    MAIN.Await(FlagEnabled(11605392))
    
    AND_7.Add(HealthRatio(1600800) <= 0.0)
    if AND_7:
        return
    AND_1.Add(CharacterAlive(1600801))
    SkipLinesIfConditionFalse(5, AND_1)
    AICommand(1600801, command_id=1, command_slot=0)
    OR_1.Add(CharacterDead(1600801))
    OR_1.Add(CharacterHasTAEEvent(1600801, tae_event_id=500))
    
    MAIN.Await(OR_1)
    
    AICommand(1600801, command_id=-1, command_slot=0)
    AND_2.Add(CharacterAlive(1600802))
    SkipLinesIfConditionFalse(5, AND_2)
    AICommand(1600802, command_id=1, command_slot=0)
    OR_2.Add(CharacterDead(1600802))
    OR_2.Add(CharacterHasTAEEvent(1600802, tae_event_id=500))
    
    MAIN.Await(OR_2)
    
    AICommand(1600802, command_id=-1, command_slot=0)
    AND_3.Add(CharacterAlive(1600803))
    SkipLinesIfConditionFalse(5, AND_3)
    AICommand(1600803, command_id=1, command_slot=0)
    OR_3.Add(CharacterDead(1600803))
    OR_3.Add(CharacterHasTAEEvent(1600803, tae_event_id=500))
    
    MAIN.Await(OR_3)
    
    AICommand(1600803, command_id=-1, command_slot=0)
    AND_4.Add(CharacterAlive(1600804))
    SkipLinesIfConditionFalse(5, AND_4)
    AICommand(1600804, command_id=1, command_slot=0)
    OR_4.Add(CharacterDead(1600804))
    OR_4.Add(CharacterHasTAEEvent(1600804, tae_event_id=500))
    
    MAIN.Await(OR_4)
    
    AICommand(1600804, command_id=-1, command_slot=0)
    Restart()


@ContinueOnRest(11605397)
def Event_11605397():
    """Event 11605397"""
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 2200))
    OR_1.Add(FlagEnabled(13))
    
    MAIN.Await(OR_1)
    
    DisableMapCollision(collision=1603310)
    DisableMapCollision(collision=1603311)
    if FlagEnabled(13):
        return
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 2200))
    
    EnableMapCollision(collision=1603310)
    EnableMapCollision(collision=1603311)
    Restart()


@ContinueOnRest(11605398)
def Event_11605398():
    """Event 11605398"""
    DisableNetworkSync()
    SkipLinesIfFlagDisabled(3, 13)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(7, 13)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2200))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602999))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2200))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602900))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_1)
    DisableCharacterCollision(PLAYER)
    
    MAIN.Await(CharacterDead(PLAYER))
    
    EnableCharacterCollision(PLAYER)
    EnableFlag(8120)
    End()
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@ContinueOnRest(11605399)
def Event_11605399():
    """Event 11605399"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(PlayerStandingOnCollision(1603300))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=1603000)
    End()


@ContinueOnRest(11605360)
def Event_11605360(_, character: int):
    """Event 11605360"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(13))
    AND_1.Add(CharacterInsideRegion(character, region=1602990))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 2200))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 6084, wait_for_completion=True)
    DisableCharacter(character)
    if ValueNotEqual(left=character, right=10000):
        return
    EnableFlag(8120)


@ContinueOnRest(11605350)
def Event_11605350(_, character: int):
    """Event 11605350"""
    AND_7.Add(Host())
    AND_7.Add(HealthRatio(character) > 0.0)
    
    MAIN.Await(AND_7)
    
    EnableImmortality(character)
    AND_1.Add(Host())
    AND_1.Add(TimeElapsed(seconds=1.0))
    AND_1.Add(HealthRatio(1600800) > 0.0)
    AND_1.Add(HealthRatio(character) <= 0.009999999776482582)
    AND_2.Add(HealthRatio(1600800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_2)
    DisableImmortality(character)
    Kill(character)
    Restart()
    ForceAnimation(character, 7000, wait_for_completion=True)
    DisableCharacter(character)
    DisableImmortality(character)
    Kill(character)


@ContinueOnRest(11605380)
def Event_11605380():
    """Event 11605380"""
    AND_1.Add(FlagDisabled(11600900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
    ))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, target_entity=1602897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1600810)
    Restart()


@ContinueOnRest(11605381)
def Event_11605381():
    """Event 11605381"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11600900))
    AND_1.Add(FlagEnabled(11605380))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1602897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@RestartOnRest(11605382)
def Event_11605382():
    """Event 11605382"""
    if FlagEnabled(11600900):
        DisableCharacter(1600810)
        Kill(1600810)
        End()
    DisableAI(1600810)
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11605380))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602890))
    
    MAIN.Await(AND_1)
    
    EnableAI(1600810)
    EnableBossHealthBar(1600810, name=2390)


@ContinueOnRest(11600900)
def Event_11600900():
    """Event 11600900"""
    MAIN.Await(CharacterDead(1600810))
    
    KillBoss(game_area_param_id=1600810)
    DisableObject(1601890)
    DeleteVFX(1601891)
    if Client():
        return
    AND_1.Add(PlayerHasGood(2013))
    if AND_1:
        return
    AwardItemLot(1100, host_only=False)


@ContinueOnRest(11605384)
def Event_11605384():
    """Event 11605384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11600900))
    AND_1.Add(FlagEnabled(11605382))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602890))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11605381))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1603801)


@ContinueOnRest(11605385)
def Event_11605385():
    """Event 11605385"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602890))
    AND_1.Add(CharacterDead(1600810))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1603801)


@ContinueOnRest(11600150)
def Event_11600150():
    """Event 11600150"""
    if FlagDisabled(11600100):
        DisableMapCollision(collision=1603250)
        DisableMapCollision(collision=1603251)
        DisableMapCollision(collision=1603252)
        DisableMapCollision(collision=1603253)
        DisableMapCollision(collision=1603254)
        DisableMapCollision(collision=1603255)
        DisableMapCollision(collision=1603256)
        DisableMapCollision(collision=1603257)
        DisableMapCollision(collision=1603258)
        DisableMapCollision(collision=1603259)
        DisableMapCollision(collision=1603260)
        DisableMapCollision(collision=1603261)
        DisableMapCollision(collision=1603262)
        DisableMapCollision(collision=1603263)
        DisableMapCollision(collision=1603264)
        DisableMapCollision(collision=1603265)
        DisableMapCollision(collision=1603266)
        DisableMapCollision(collision=1603267)
        DisableMapPiece(map_piece_id=1603110)
        DisableMapPiece(map_piece_id=1603111)
        DisableMapPiece(map_piece_id=1603112)
        DisableMapPiece(map_piece_id=1603113)
        DisableMapPiece(map_piece_id=1603114)
        DisableMapPiece(map_piece_id=1603115)
        DisableMapPiece(map_piece_id=1603116)
        DisableMapPiece(map_piece_id=1603117)
        DisableMapPiece(map_piece_id=1603118)
        DisableMapPiece(map_piece_id=1603119)
        DisableMapPiece(map_piece_id=1603120)
        DisableMapCollision(collision=1603121)
        DisableMapCollision(collision=1603122)
    
        MAIN.Await(FlagEnabled(11600100))
    
        EnableMapCollision(collision=1603250)
        EnableMapCollision(collision=1603251)
        EnableMapCollision(collision=1603252)
        EnableMapCollision(collision=1603253)
        EnableMapCollision(collision=1603254)
        EnableMapCollision(collision=1603255)
        EnableMapCollision(collision=1603256)
        EnableMapCollision(collision=1603257)
        EnableMapCollision(collision=1603258)
        EnableMapCollision(collision=1603259)
        EnableMapCollision(collision=1603260)
        EnableMapCollision(collision=1603261)
        EnableMapCollision(collision=1603262)
        EnableMapCollision(collision=1603263)
        EnableMapCollision(collision=1603264)
        EnableMapCollision(collision=1603265)
        EnableMapCollision(collision=1603266)
        EnableMapCollision(collision=1603267)
        EnableMapPiece(map_piece_id=1603110)
        EnableMapPiece(map_piece_id=1603111)
        EnableMapPiece(map_piece_id=1603112)
        EnableMapPiece(map_piece_id=1603113)
        EnableMapPiece(map_piece_id=1603114)
        EnableMapPiece(map_piece_id=1603115)
        EnableMapPiece(map_piece_id=1603116)
        EnableMapPiece(map_piece_id=1603117)
        EnableMapPiece(map_piece_id=1603118)
        EnableMapPiece(map_piece_id=1603119)
        EnableMapPiece(map_piece_id=1603120)
        EnableMapCollision(collision=1603121)
        EnableMapCollision(collision=1603122)
    DisableSoundEvent(sound_id=1603850)
    DisableMapCollision(collision=1603200)
    DisableMapCollision(collision=1603201)
    DisableMapCollision(collision=1603202)
    DisableMapCollision(collision=1603203)
    DisableMapCollision(collision=1603204)
    DisableMapCollision(collision=1603205)
    DisableMapCollision(collision=1603206)
    DisableMapCollision(collision=1603207)
    DisableMapCollision(collision=1603208)
    DisableMapCollision(collision=1603209)
    DisableMapCollision(collision=1603210)
    DisableMapCollision(collision=1603211)
    DisableMapCollision(collision=1603212)
    DisableMapCollision(collision=1603213)
    DisableMapCollision(collision=1603214)
    DisableMapCollision(collision=1603215)
    DisableMapCollision(collision=1603216)
    DisableMapCollision(collision=1603217)


@RestartOnRest(11605100)
def Event_11605100():
    """Event 11605100"""
    if FlagEnabled(11600100):
        return
    DisableBackread(1600100)
    DisableBackread(1600101)
    DisableBackread(1600102)
    DisableBackread(1600103)
    DisableBackread(1600104)
    DisableBackread(1600105)
    DisableBackread(1600106)
    DisableBackread(1600107)
    DisableBackread(1600108)
    DisableBackread(1600109)
    DisableBackread(1600110)
    DisableBackread(1600400)
    DisableBackread(1600401)
    DisableBackread(1600900)
    DisableBackread(1600901)
    DisableBackread(1600902)
    DisableBackread(1600903)
    DisableBackread(1600904)
    DisableBackread(1600905)
    
    MAIN.Await(FlagEnabled(11600100))
    
    EnableBackread(1600100)
    EnableBackread(1600101)
    EnableBackread(1600102)
    EnableBackread(1600103)
    EnableBackread(1600104)
    EnableBackread(1600105)
    EnableBackread(1600106)
    EnableBackread(1600107)
    EnableBackread(1600108)
    EnableBackread(1600109)
    EnableBackread(1600110)
    EnableBackread(1600400)
    EnableBackread(1600401)
    EnableBackread(1600900)
    EnableBackread(1600901)
    EnableBackread(1600902)
    EnableBackread(1600903)
    EnableBackread(1600904)
    EnableBackread(1600905)


@ContinueOnRest(11600100)
def Event_11600100():
    """Event 11600100"""
    SkipLinesIfFlagEnabled(1, 11600101)
    SkipLinesIfThisEventFlagDisabled(8)
    EndOfAnimation(obj=1601100, animation_id=10)
    DisableMapCollision(collision=1603100)
    DisableMapCollision(collision=1603102)
    DisableMapCollision(collision=1603103)
    DisableMapCollision(collision=1603104)
    DisableObject(1601120)
    DisableFlag(404)
    End()
    EnableMapCollision(collision=1603103)
    EnableMapCollision(collision=1603104)
    
    MAIN.Await(FlagEnabled(11600101))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(160000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11600100)
    Restart()


@ContinueOnRest(11600101)
def Event_11600101(_, obj: int, flag: int, animation_id: int):
    """Event 11600101"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=1601100, animation_id=animation_id)
        EndOfAnimation(obj=obj, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010502,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(obj, 0, wait_for_completion=True)
    if FlagEnabled(flag):
        return
    ForceAnimation(1601100, animation_id, wait_for_completion=True)


@ContinueOnRest(11600110)
def Event_11600110(_, obj_act_id: int, text: int, obj: int):
    """Event 11600110"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if Client():
        return
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@ContinueOnRest(11600120)
def Event_11600120(_, obj_act_id: int, text: int, obj: int, text_1: int, item: int):
    """Event 11600120"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if Client():
        return
    AND_1.Add(PlayerHasGood(item))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=text_1, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@ContinueOnRest(11600160)
def Event_11600160():
    """Event 11600160"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1601142, animation_id=0)
        RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601142)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010500,
        anchor_entity=1601142,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    EnableFlag(11600160)
    Move(PLAYER, destination=1601142, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1601142, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601142)


@ContinueOnRest(11600200)
def Event_11600200():
    """Event 11600200"""
    if FlagEnabled(11600201):
        EndOfAnimation(obj=1601200, animation_id=21)
        DisableObjectActivation(1601202, obj_act_id=6101)
    else:
        EndOfAnimation(obj=1601200, animation_id=20)
        DisableObjectActivation(1021201, obj_act_id=6101)
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagDisabled(11600201))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602200))
    AND_2.Add(Singleplayer())
    AND_2.Add(FlagEnabled(11600201))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602201))
    AND_3.Add(Singleplayer())
    AND_3.Add(ObjectActivated(obj_act_id=11020202))
    AND_4.Add(Singleplayer())
    AND_4.Add(ObjectActivated(obj_act_id=11600203))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605120)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_3)
    EnableFlag(11600201)
    DisableObjectActivation(1601202, obj_act_id=6101)
    ForceAnimation(1601200, 11, wait_for_completion=True)
    ForceAnimation(1601200, 1, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602201))
    
    ForceAnimation(1601200, 21, wait_for_completion=True)
    EnableObjectActivation(1021201, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()
    DisableFlag(11600201)
    DisableObjectActivation(1021201, obj_act_id=6101)
    ForceAnimation(1601200, 10, wait_for_completion=True)
    ForceAnimation(1601200, 0, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602200))
    
    ForceAnimation(1601200, 20, wait_for_completion=True)
    EnableObjectActivation(1601202, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()


@ContinueOnRest(11600250)
def Event_11600250():
    """Event 11600250"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605120))
    AND_1.Add(FlagDisabled(11600201))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1021201,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605120))
    AND_2.Add(FlagEnabled(11600201))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601202,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(Multiplayer())
    AND_3.Add(FlagDisabled(11600201))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1602200))
    AND_4.Add(Multiplayer())
    AND_4.Add(FlagEnabled(11600201))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1602201))
    AND_5.Add(Multiplayer())
    AND_5.Add(ObjectActivated(obj_act_id=11020202))
    AND_6.Add(Multiplayer())
    AND_6.Add(ObjectActivated(obj_act_id=11600203))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11600199)
def Event_11600199():
    """Event 11600199"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11600100))
    
    EnableObjectActivation(1601211, obj_act_id=6101)
    EnableObjectActivation(1601221, obj_act_id=6101)


@ContinueOnRest(11600210)
def Event_11600210():
    """Event 11600210"""
    if FlagEnabled(11600211):
        EndOfAnimation(obj=1601210, animation_id=22)
        DisableObjectActivation(1601211, obj_act_id=6101)
    else:
        EndOfAnimation(obj=1601210, animation_id=21)
        DisableObjectActivation(1601212, obj_act_id=6101)
    if FlagDisabled(11600100):
        DisableObjectActivation(1601211, obj_act_id=6101)
    AND_1.Add(FlagEnabled(11600100))
    AND_1.Add(FlagDisabled(11600211))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602211))
    AND_2.Add(FlagEnabled(11600100))
    AND_2.Add(FlagEnabled(11600211))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602210))
    AND_3.Add(ObjectActivated(obj_act_id=11600212))
    AND_4.Add(ObjectActivated(obj_act_id=11600213))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605121)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_4)
    EnableFlag(11600211)
    DisableObjectActivation(1601211, obj_act_id=6101)
    ForceAnimation(1601210, 10, wait_for_completion=True)
    ForceAnimation(1601210, 2, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602210))
    
    ForceAnimation(1601210, 22, wait_for_completion=True)
    EnableObjectActivation(1601212, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()
    DisableFlag(11600211)
    DisableObjectActivation(1601212, obj_act_id=6101)
    ForceAnimation(1601210, 13, wait_for_completion=True)
    ForceAnimation(1601210, 3, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602211))
    
    ForceAnimation(1601210, 21, wait_for_completion=True)
    EnableObjectActivation(1601211, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()


@ContinueOnRest(11600251)
def Event_11600251():
    """Event 11600251"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605121))
    AND_1.Add(FlagEnabled(11600211))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601211,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605121))
    AND_2.Add(FlagDisabled(11600211))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601212,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagDisabled(11600100))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601211,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11600220)
def Event_11600220():
    """Event 11600220"""
    if FlagEnabled(11600221):
        EndOfAnimation(obj=1601220, animation_id=24)
        DisableObjectActivation(1601221, obj_act_id=6101)
    else:
        EndOfAnimation(obj=1601220, animation_id=21)
        DisableObjectActivation(1601222, obj_act_id=6101)
    if FlagDisabled(11600100):
        DisableObjectActivation(1601221, obj_act_id=6101)
    AND_1.Add(FlagEnabled(11600100))
    AND_1.Add(FlagDisabled(11600221))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602221))
    AND_2.Add(FlagEnabled(11600100))
    AND_2.Add(FlagEnabled(11600221))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602220))
    AND_3.Add(ObjectActivated(obj_act_id=11600222))
    AND_4.Add(ObjectActivated(obj_act_id=11600223))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605122)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_4)
    EnableFlag(11600221)
    DisableObjectActivation(1601221, obj_act_id=6101)
    ForceAnimation(1601220, 10, wait_for_completion=True)
    ForceAnimation(1601220, 4, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602220))
    
    ForceAnimation(1601220, 24, wait_for_completion=True)
    EnableObjectActivation(1601222, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()
    DisableFlag(11600221)
    DisableObjectActivation(1601222, obj_act_id=6101)
    ForceAnimation(1601220, 15, wait_for_completion=True)
    ForceAnimation(1601220, 5, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602221))
    
    ForceAnimation(1601220, 21, wait_for_completion=True)
    EnableObjectActivation(1601221, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()


@ContinueOnRest(11600252)
def Event_11600252():
    """Event 11600252"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605122))
    AND_1.Add(FlagEnabled(11600221))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601221,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605122))
    AND_2.Add(FlagDisabled(11600221))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601222,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagDisabled(11600100))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601221,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11600230)
def Event_11600230():
    """Event 11600230"""
    if FlagEnabled(11600231):
        EndOfAnimation(obj=1601230, animation_id=26)
        DisableObjectActivation(1601231, obj_act_id=6101)
    else:
        EndOfAnimation(obj=1601230, animation_id=21)
        DisableObjectActivation(1601232, obj_act_id=6101)
    AND_1.Add(FlagDisabled(11600231))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602231))
    AND_2.Add(FlagEnabled(11600231))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602230))
    AND_3.Add(ObjectActivated(obj_act_id=11600232))
    AND_4.Add(ObjectActivated(obj_act_id=11600233))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605123)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_4)
    EnableFlag(11600231)
    DisableObjectActivation(1601231, obj_act_id=6101)
    ForceAnimation(1601230, 10, wait_for_completion=True)
    ForceAnimation(1601230, 6, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602230))
    
    ForceAnimation(1601230, 26, wait_for_completion=True)
    EnableObjectActivation(1601232, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()
    DisableFlag(11600231)
    DisableObjectActivation(1601232, obj_act_id=6101)
    ForceAnimation(1601230, 17, wait_for_completion=True)
    ForceAnimation(1601230, 7, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602231))
    
    ForceAnimation(1601230, 21, wait_for_completion=True)
    EnableObjectActivation(1601231, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()


@ContinueOnRest(11600253)
def Event_11600253():
    """Event 11600253"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605123))
    AND_1.Add(FlagEnabled(11600231))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601231,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605123))
    AND_2.Add(FlagDisabled(11600231))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601232,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@RestartOnRest(11605150)
def Event_11605150(_, character: int, region: int):
    """Event 11605150"""
    DisableNetworkSync()
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterOutsideRegion(character, region=region))
    
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(11605001)
def Event_11605001(_, character: int, radius: float, cancel_animation: int):
    """Event 11605001"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SetStandbyAnimationSettings(character)
    SkipLines(1)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)
    EnableAI(character)


@RestartOnRest(11605050)
def Event_11605050(_, character: int, region: int, cancel_animation: int, left: int, radius: float):
    """Event 11605050"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    if ValueNotEqual(left=left, right=0):
        AND_3.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    if ValueNotEqual(left=left, right=0):
        OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SetStandbyAnimationSettings(character)
    SkipLines(1)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)
    EnableAI(character)


@RestartOnRest(11605101)
def Event_11605101():
    """Event 11605101"""
    if ThisEventFlagEnabled():
        AICommand(1600300, command_id=1, command_slot=0)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(1600300, tae_event_id=700))
    
    SetNest(1600300, region=1602300)
    AICommand(1600300, command_id=0, command_slot=0)
    ReplanAI(1600300)
    
    MAIN.Await(CharacterInsideRegion(1600300, region=1602301))
    
    AICommand(1600300, command_id=1, command_slot=0)


@RestartOnRest(11600810)
def Event_11600810():
    """Event 11600810"""
    if ThisEventFlagEnabled():
        DisableCharacter(1600500)
        End()
    
    MAIN.Await(CharacterDead(1600500))
    
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    if not OR_1:
        return
    AwardItemLot(34200200, host_only=True)


@RestartOnRest(11600400)
def Event_11600400():
    """Event 11600400"""
    DisableCharacterCollision(1600500)
    DisableGravity(1600500)
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(1600500, cancel_animation=29060)
        End()
    OR_1.Add(EntityWithinDistance(entity=1600500, other_entity=PLAYER, radius=10.0))
    OR_1.Add(Attacked(attacked_entity=1600500, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(1600500)
    ForceAnimation(1600500, 29060)


@RestartOnRest(11605200)
def Event_11605200(_, character: int, character_1: int, command_id: int, flag: int):
    """Event 11605200"""
    if ThisEventSlotFlagEnabled():
        MAIN.Await(CharacterBackreadEnabled(character))
    
        AICommand(character, command_id=command_id, command_slot=0)
        End()
    DisableCharacter(character_1)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=300))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=command_id, command_slot=0)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 8300, wait_for_completion=True)
    AND_1.Add(CharacterDoesNotHaveTAEEvent(character, tae_event_id=300))
    End()


@RestartOnRest(11605250)
def Event_11605250(_, character: int):
    """Event 11605250"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=400))
    DisableCharacter(character)


@RestartOnRest(11600850)
def Event_11600850(_, character: int):
    """Event 11600850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(11600600)
def Event_11600600(_, obj: int, obj_act_id: int):
    """Event 11600600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11600650)
def Event_11600650(_, obj: int, obj_1: int):
    """Event 11600650"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=101)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    ForceAnimation(obj, 100, loop=True)
    
    MAIN.Await(ObjectDestroyed(obj_1))
    
    ForceAnimation(obj, 101, wait_for_completion=True)
    EnableTreasure(obj=obj)


@ContinueOnRest(11600510)
def Event_11600510(_, character: int, flag: int):
    """Event 11600510"""
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


@ContinueOnRest(11600520)
def Event_11600520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600530)
def Event_11600530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600530"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1310))
    AND_1.Add(FlagEnabled(710))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600531)
def Event_11600531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600531"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1311))
    AND_1.Add(FlagEnabled(11600100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600532)
def Event_11600532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600532"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1312))
    AND_1.Add(FlagEnabled(13))
    AND_1.Add(FlagEnabled(11600593))
    AND_1.Add(OutsideMap(game_map=NEW_LONDO_RUINS))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11600537)
def Event_11600537(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600537"""
    if FlagDisabled(1670):
        return
    DisableCharacter(character)
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(1670))
    AND_1.Add(FlagDisabled(11800100))
    AND_1.Add(FlagEnabled(13))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    ForceAnimation(character, 9060, wait_for_completion=True)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600538)
def Event_11600538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600538"""
    AND_1.Add(FlagEnabled(1671))
    AND_1.Add(FlagEnabled(710))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600539)
def Event_11600539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600539"""
    AND_1.Add(FlagEnabled(1672))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600540)
def Event_11600540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600540"""
    OR_1.Add(FlagEnabled(1672))
    OR_1.Add(FlagEnabled(1678))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11600590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11600541)
def Event_11600541(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11600541"""
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_1.Add(FlagEnabled(11600590))
    AND_2.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(character) > 0.0)
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=15.0))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11600545)
def Event_11600545(_, character: int):
    """Event 11600545"""
    MAIN.Await(FlagEnabled(1464))
    
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)


@ContinueOnRest(11606200)
def Event_11606200():
    """Event 11606200"""
    OR_1.Add(FlagEnabled(1672))
    OR_1.Add(FlagEnabled(1673))
    OR_1.Add(FlagEnabled(1674))
    AND_1.Add(OR_1)
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    AND_1.Add(FlagEnabled(821))
    
    MAIN.Await(AND_1)
    
    DisableFlag(821)
    EnableFlag(831)
    EnableCharacter(6341)
    PlayCutscene(160040, cutscene_flags=0, player_id=10000, move_to_region=1802110, game_map=KILN_OF_THE_FIRST_FLAME)
    PlayCutscene(180041, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(823)
    Restart()


@ContinueOnRest(11605030)
def Event_11605030():
    """Event 11605030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6520, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11605034)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11605031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6520)
    if FlagEnabled(13):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11200300))
    AND_1.Add(CharacterBackreadEnabled(6520))
    AND_1.Add(EntityWithinDistance(entity=6520, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6520,
        region=1602000,
        summon_flag=11605031,
        dismissal_flag=11605034,
    )


@ContinueOnRest(11605032)
def Event_11605032():
    """Event 11605032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11605031))
    AND_1.Add(FlagEnabled(11605393))
    
    MAIN.Await(AND_1)
    
    AICommand(6520, command_id=10, command_slot=0)
    ReplanAI(6520)
    
    MAIN.Await(CharacterInsideRegion(6520, region=1602998))
    
    RotateToFaceEntity(6520, target_entity=1602997)
    ForceAnimation(6520, 7410)
    AICommand(6520, command_id=-1, command_slot=0)
    ReplanAI(6520)


@ContinueOnRest(11605033)
def Event_11605033():
    """Event 11605033"""
    AND_1.Add(FlagEnabled(11605031))
    AND_1.Add(CharacterHasSpecialEffect(6520, 2200))
    AND_1.Add(CharacterInsideRegion(6520, region=1602999))
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(6520)
    Wait(2.0)
    DisableInvincibility(6520)
