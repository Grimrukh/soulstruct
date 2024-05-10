"""
Kiln of the First Flame

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    if FlagEnabled(11800100):
        RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=10)
    if FlagEnabled(11800210):
        RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=30)
    SkipLinesIfClient(2)
    DisableObject(1801994)
    DeleteVFX(1801995, erase_root_only=False)
    if FlagEnabled(15):
        DisableObject(1801960)
        DisableObject(1801110)
        EnableObject(1801111)
    Event_11805090()
    Event_11805091()
    Event_11805092()
    Event_20()
    Event_21()
    Event_11800100()
    Event_11800101()
    Event_11800200()
    Event_11800230(0, value=1, dummy_id=180005, obj=1801960)
    Event_11800230(1, value=2, dummy_id=180006, obj=1801960)
    Event_11800230(2, value=3, dummy_id=180007, obj=1801960)
    Event_11800230(3, value=4, dummy_id=180008, obj=1801960)
    Event_11800210()
    Event_11800220()
    Event_11806100(0, character=1800100, destination=1802000)
    Event_11806100(1, character=1800101, destination=1802001)
    Event_11806100(2, character=1800102, destination=1802002)
    Event_11806100(3, character=1800103, destination=1802003)
    Event_11806100(4, character=1800104, destination=1802004)
    Event_11806100(5, character=1800105, destination=1802005)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_11800002()
    DisableSoundEvent(sound_id=1803800)
    if FlagEnabled(15):
        Event_11805392()
        DisableObject(1801990)
        DeleteVFX(1801991, erase_root_only=False)
    else:
        Event_11805390()
        Event_11805391()
        Event_11805393()
        Event_11805392()
        Event_11800001()
        Event_11805394()
        Event_11805395()
    HumanityRegistration(6544, event_flag=8310)
    Event_11805030()
    Event_11805029()
    Event_11805032()
    Event_11805990(0, flag=11805031, summoned_character=6544)
    Event_11800550(0, first_flag=1000, last_flag=1029, flag=1012)
    EnableImmortality(6331)
    if FlagDisabled(830):
        DisableCharacter(6331)
    if FlagDisabled(15):
        Event_11800539(0, character=6331, first_flag=1640, last_flag=1647, flag=1647)
        Event_11800530(0, character=6331, first_flag=1640, last_flag=1647, flag=1644)
        Event_11800531(0, character=6331, first_flag=1640, last_flag=1647, flag=1645)
        Event_11800537(0, character=6331, first_flag=1640, last_flag=1647, flag=1649)
        Event_11800541(0, character=6331)
        Event_11806200()
    EnableImmortality(6341)
    if FlagDisabled(831):
        DisableCharacter(6341)
    if FlagDisabled(15):
        Event_11800540(0, character=6341, first_flag=1670, last_flag=1677, flag=1677)
        Event_11800533(0, character=6341, first_flag=1670, last_flag=1677, flag=1673)
        Event_11800534(0, character=6341, first_flag=1670, last_flag=1677, flag=1674)
        Event_11800538(0, character=6341, first_flag=1670, last_flag=1677, flag=1678)
        Event_11800542(0, character=6341)
        Event_11806201()


@RestartOnRest(11805090)
def Event_11805090():
    """Event 11805090"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1800900)
    DisableCharacter(1800901)
    DisableCharacter(1800902)
    DisableCharacter(1800903)
    DisableCharacter(1800904)
    
    MAIN.Await(FlagEnabled(11800050))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1800900)
    EnableCharacter(1800901)
    EnableCharacter(1800902)
    EnableCharacter(1800903)
    EnableCharacter(1800904)


@RestartOnRest(11805091)
def Event_11805091():
    """Event 11805091"""
    OR_1.Add(FlagEnabled(11805095))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11800050)
    DisableFlag(11805095)
    EnableFlag(5001)
    Kill(1800900)
    Kill(1800901)
    Kill(1800902)
    Kill(1800903)
    Kill(1800904)


@RestartOnRest(11805092)
def Event_11805092():
    """Event 11805092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11800050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11800050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11800050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11800050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11800050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11800050))
    if not OR_6:
        return RESTART
    EnableFlag(11800050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    if not AND_7:
        return RESTART
    DisableFlag(11800050)
    EnableFlag(11805095)


@ContinueOnRest(11805390)
def Event_11805390():
    """Event 11805390"""
    AND_1.Add(FlagDisabled(15))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1802998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1801990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1802997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11805391)
def Event_11805391():
    """Event 11805391"""
    AND_1.Add(FlagDisabled(15))
    AND_1.Add(FlagEnabled(11805393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1802998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1801990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1802997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11805393)
def Event_11805393():
    """Event 11805393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(15))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1802996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1800800)


@RestartOnRest(11805392)
def Event_11805392():
    """Event 11805392"""
    if FlagEnabled(15):
        DisableCharacter(1800800)
        Kill(1800800)
        End()
    DisableAI(1800800)
    AND_1.Add(FlagEnabled(11805393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1802996))
    
    MAIN.Await(AND_1)
    
    EnableAI(1800800)
    EnableBossHealthBar(1800800, name=5370)


@ContinueOnRest(11800001)
def Event_11800001():
    """Event 11800001"""
    DisableObject(1801111)
    DisableObject(1801950)
    
    MAIN.Await(CharacterDead(1800800))
    
    EnableFlag(15)
    KillBoss(game_area_param_id=1800800)
    DisableObject(1801990)
    DeleteVFX(1801991)
    SkipLinesIfClient(2)
    SetRespawnPoint(respawn_point=1802130)
    SaveRequest()
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    DisableObject(1801960)
    DisableObject(1801110)
    EnableObject(1801111)
    DeleteObjectVFX(1801960)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1801950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1801950)


@ContinueOnRest(20)
def Event_20():
    """Event 20"""
    if Client():
        return
    AND_1.Add(FlagEnabled(15))
    AND_1.Add(ActionButton(
        prompt_text=10010108,
        anchor_entity=1801950,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        dummy_id=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    IncrementNewGameCycle(dummy_arg=1)
    PlayCutscene(180000, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=1)
    EnableFlag(20)


@ContinueOnRest(21)
def Event_21():
    """Event 21"""
    if Client():
        return
    AND_1.Add(FlagEnabled(15))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1802990))
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    
    MAIN.Await(AND_1)
    
    PlayCutscene(180001, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    IncrementNewGameCycle(dummy_arg=1)
    AwardAchievement(achievement_id=2)
    EnableFlag(21)


@ContinueOnRest(11805394)
def Event_11805394():
    """Event 11805394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(15))
    AND_1.Add(FlagEnabled(11805392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11805391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1802990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1803800)


@ContinueOnRest(11805395)
def Event_11805395():
    """Event 11805395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(15))
    AND_1.Add(FlagEnabled(11805394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1803800)


@RestartOnRest(11800002)
def Event_11800002():
    """Event 11800002"""
    MAIN.Await(FlagEnabled(15))
    
    DisableCharacter(1800200)
    DisableCharacter(1800201)
    DisableCharacter(1800202)
    DisableCharacter(1800203)
    DisableCharacter(1800204)
    DisableCharacter(1800900)
    DisableCharacter(1800901)
    DisableCharacter(1800902)
    DisableCharacter(1800903)
    DisableCharacter(1800904)
    DisableCharacter(1803900)
    DisableCharacter(1803901)
    DisableCharacter(1803902)
    Kill(1800200)
    Kill(1800201)
    Kill(1800202)
    Kill(1800203)
    Kill(1800204)
    Kill(1800900)
    Kill(1800901)
    Kill(1800902)
    Kill(1800903)
    Kill(1800904)
    Kill(1803900)
    Kill(1803901)
    Kill(1803902)


@ContinueOnRest(11800100)
def Event_11800100():
    """Event 11800100"""
    if ThisEventFlagEnabled():
        return
    DisableObject(1801110)
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(2510))
    AND_1.Add(ActionButton(
        prompt_text=10010105,
        anchor_entity=1801960,
        anchor_type=CoordEntityType.Object,
        dummy_id=150,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    PlayCutscene(180015, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableObject(1801110)
    RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=10)
    RemoveGoodFromPlayer(item=2510)


@ContinueOnRest(11800101)
def Event_11800101():
    """Event 11800101"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11800100))
    AND_1.Add(PlayerDoesNotHaveGood(2510))
    AND_1.Add(ActionButton(
        prompt_text=10010105,
        anchor_entity=1801960,
        anchor_type=CoordEntityType.Object,
        dummy_id=150,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagEnabled(11800100))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    DisplayDialog(text=10010174, anchor_entity=1801960)
    Restart()


@ContinueOnRest(11800200)
def Event_11800200():
    """Event 11800200"""
    MAIN.Await(FlagEnabled(756))
    
    ForceAnimation(PLAYER, 7697)
    WaitFrames(frames=75)
    AND_1.Add(FlagDisabled(11800201))
    AND_1.Add(PlayerHasGood(2500))
    AND_2.Add(FlagDisabled(11800202))
    AND_2.Add(PlayerHasGood(2501))
    AND_3.Add(FlagDisabled(11800203))
    AND_3.Add(PlayerHasGood(2502))
    AND_4.Add(FlagDisabled(11800204))
    AND_4.Add(PlayerHasGood(2503))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    EnableFlag(11800201)
    RemoveGoodFromPlayer(item=2500)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_2)
    EnableFlag(11800202)
    RemoveGoodFromPlayer(item=2501)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    EnableFlag(11800203)
    RemoveGoodFromPlayer(item=2502)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_4)
    EnableFlag(11800204)
    RemoveGoodFromPlayer(item=2503)
    EnableFlag(11805111)
    
    MAIN.Await(FlagDisabled(11805111))
    
    WaitFrames(frames=10)
    if FlagEnabled(11800211):
        return
    DisableFlag(756)
    Restart()


@ContinueOnRest(11800230)
def Event_11800230(_, value: int, dummy_id: int, obj: int):
    """Event 11800230"""
    AND_1.Add(FlagEnabled(11805111))
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11800201, 11800204)) == value)
    
    MAIN.Await(AND_1)
    
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=100, dummy_id=dummy_id)
    WaitFrames(frames=95)
    SkipLinesIfFlagRangeAllEnabled(1, (11800201, 11800204))
    ForceAnimation(PLAYER, 7701, loop=True)
    DisableFlag(11805111)


@ContinueOnRest(11800210)
def Event_11800210():
    """Event 11800210"""
    SkipLinesIfFlagEnabled(17, 15)
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11800201, 11800204)) == 1)
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11800201, 11800204)) == 2)
    AND_4.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11800201, 11800204)) == 3)
    AND_5.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11800201, 11800204)) == 4)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_2)
    CreateObjectVFX(1801960, vfx_id=100, dummy_id=180005)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_3)
    CreateObjectVFX(1801960, vfx_id=100, dummy_id=180006)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_4)
    CreateObjectVFX(1801960, vfx_id=100, dummy_id=180007)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_5)
    CreateObjectVFX(1801960, vfx_id=100, dummy_id=180008)
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1801101, animation_id=1)
        End()
    AND_1.Add(FlagEnabled(11800201))
    AND_1.Add(FlagEnabled(11800202))
    AND_1.Add(FlagEnabled(11800203))
    AND_1.Add(FlagEnabled(11800204))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11800211)
    DisableFlag(756)
    PlayCutscene(180010, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EndOfAnimation(obj=1801101, animation_id=1)
    RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=30)


@ContinueOnRest(11800220)
def Event_11800220():
    """Event 11800220"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11800210))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1802100,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1801101,
    ))
    AND_2.Add(FlagEnabled(11805110))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    DisplayDialog(text=10010160, anchor_entity=1801101)
    SkipLines(2)
    DisableFlag(11805110)
    DisplayDialog(text=10010171, anchor_entity=1801960)
    Restart()


@RestartOnRest(11806100)
def Event_11806100(_, character: int, destination: int):
    """Event 11806100"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
        DisableAI(character)
        ForceAnimation(character, 200, loop=True)
    
    MAIN.Await(CharacterInsideRegion(character, region=1802006))
    
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


@RestartOnRest(11805100)
def Event_11805100(_, character: int, item_lot: int):
    """Event 11805100"""
    MAIN.Await(CharacterAlive(character))
    
    MAIN.Await(CharacterDead(character))
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@ContinueOnRest(11800510)
def Event_11800510(_, character: int, flag: int):
    """Event 11800510"""
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
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11800520)
def Event_11800520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800530)
def Event_11800530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800530"""
    AND_1.Add(FlagEnabled(1643))
    AND_1.Add(FlagEnabled(830))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800531)
def Event_11800531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800531"""
    AND_1.Add(FlagEnabled(1644))
    AND_1.Add(FlagEnabled(830))
    AND_1.Add(FlagEnabled(11800210))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800533)
def Event_11800533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800533"""
    AND_1.Add(FlagEnabled(1672))
    AND_1.Add(FlagEnabled(831))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800534)
def Event_11800534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800534"""
    AND_1.Add(FlagEnabled(1673))
    AND_1.Add(FlagEnabled(831))
    AND_1.Add(FlagEnabled(11800210))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800537)
def Event_11800537(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800537"""
    OR_1.Add(FlagEnabled(1642))
    OR_1.Add(FlagEnabled(1643))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(830))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800538)
def Event_11800538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800538"""
    OR_1.Add(FlagEnabled(1671))
    OR_1.Add(FlagEnabled(1672))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(831))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11800539)
def Event_11800539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800539"""
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_7.Add(FlagEnabled(11020598))
    AND_7.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_7.Add(HealthRatio(character) > 0.0)
    AND_7.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_7.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=15.0))
    OR_7.Add(AND_7)
    AND_1.Add(OR_7)
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(3, input_condition=AND_2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7009, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11800540)
def Event_11800540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800540"""
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    OR_7.Add(FlagEnabled(11600590))
    AND_7.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_7.Add(HealthRatio(character) > 0.0)
    AND_7.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_7.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=15.0))
    OR_7.Add(AND_7)
    AND_1.Add(OR_7)
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(3, input_condition=AND_2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11800541)
def Event_11800541(_, character: int):
    """Event 11800541"""
    AND_1.Add(FlagEnabled(830))
    AND_1.Add(FlagDisabled(1647))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    
    MAIN.Await(FlagDisabled(830))
    
    DisableCharacter(character)
    Restart()


@ContinueOnRest(11800542)
def Event_11800542(_, character: int):
    """Event 11800542"""
    AND_1.Add(FlagEnabled(831))
    AND_1.Add(FlagDisabled(1676))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    
    MAIN.Await(FlagDisabled(831))
    
    DisableCharacter(character)
    Restart()


@ContinueOnRest(11800550)
def Event_11800550(_, first_flag: int, last_flag: int, flag: int):
    """Event 11800550"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1003))
    AND_1.Add(FlagEnabled(11410595))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11806200)
def Event_11806200():
    """Event 11806200"""
    OR_1.Add(FlagEnabled(1643))
    OR_1.Add(FlagEnabled(1644))
    OR_1.Add(FlagEnabled(1645))
    AND_1.Add(OR_1)
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    AND_1.Add(FlagEnabled(824))
    
    MAIN.Await(AND_1)
    
    DisableFlag(824)
    PlayCutscene(180050, cutscene_flags=0, player_id=10000, move_to_region=1022110, game_map=FIRELINK_SHRINE)
    PlayCutscene(100250, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(6331)
    DisableFlag(830)
    Restart()


@ContinueOnRest(11806201)
def Event_11806201():
    """Event 11806201"""
    OR_1.Add(FlagEnabled(1672))
    OR_1.Add(FlagEnabled(1673))
    OR_1.Add(FlagEnabled(1674))
    AND_1.Add(OR_1)
    AND_1.Add(InsideMap(game_map=KILN_OF_THE_FIRST_FLAME))
    AND_1.Add(FlagEnabled(825))
    
    MAIN.Await(AND_1)
    
    DisableFlag(825)
    PlayCutscene(180051, cutscene_flags=0, player_id=10000, move_to_region=1602110, game_map=NEW_LONDO_RUINS)
    PlayCutscene(160050, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(6341)
    DisableFlag(831)
    Restart()


@ContinueOnRest(11805029)
def Event_11805029():
    """Event 11805029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6544, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11805033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11805031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6544)
    if FlagEnabled(15):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11805031))
    AND_1.Add(FlagDisabled(11805033))
    AND_1.Add(FlagEnabled(1012))
    AND_1.Add(CharacterBackreadEnabled(6544))
    AND_1.Add(EntityWithinDistance(entity=6544, other_entity=PLAYER, radius=30.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6544,
        region=1802050,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


@ContinueOnRest(11805990)
def Event_11805990(_, flag: int, summoned_character: int):
    """Event 11805990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11805030)
def Event_11805030():
    """Event 11805030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6544, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11805033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11805031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6544)
    if FlagEnabled(15):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(1012))
    AND_1.Add(CharacterBackreadEnabled(6544))
    AND_1.Add(EntityWithinDistance(entity=6544, other_entity=PLAYER, radius=30.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6544,
        region=1802050,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


@ContinueOnRest(11805032)
def Event_11805032():
    """Event 11805032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11805031))
    AND_1.Add(FlagEnabled(11805393))
    
    MAIN.Await(AND_1)
    
    AICommand(6544, command_id=10, command_slot=0)
    ReplanAI(6544)
    
    MAIN.Await(EntityWithinDistance(entity=6544, other_entity=1801990, radius=1.5))
    
    RotateToFaceEntity(6544, target_entity=1802997)
    ForceAnimation(6544, 7410)
    AICommand(6544, command_id=-1, command_slot=0)
    ReplanAI(6544)


@RestartOnRest(11805200)
def Event_11805200():
    """Event 11805200"""
    DisableAI(1800999)
    AND_1.Add(PlayerMovingOnCollision(1803000))
    AND_2.Add(PlayerRunningOnCollision(1803000))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    RequestAnimation(1800999, animation_id=1750, wait_for_completion=True)
    Restart()
    RequestAnimation(1800999, animation_id=2000, wait_for_completion=True)
    Restart()
