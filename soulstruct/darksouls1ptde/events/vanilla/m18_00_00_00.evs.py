"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    SkipLinesIfFlagDisabled(1, 11800100)
    RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=10)
    SkipLinesIfFlagDisabled(1, 11800210)
    RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=30)
    SkipLinesIfClient(2)
    DisableObject(1801994)
    DeleteVFX(1801995, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, 15)
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
    Event_11800230(0, value=1, model_point=180005, obj=1801960)
    Event_11800230(1, value=2, model_point=180006, obj=1801960)
    Event_11800230(2, value=3, model_point=180007, obj=1801960)
    Event_11800230(3, value=4, model_point=180008, obj=1801960)
    Event_11800210()
    Event_11800220()
    Event_11806100(0, character=1800100, destination=1802000)
    Event_11806100(1, character=1800101, destination=1802001)
    Event_11806100(2, character=1800102, destination=1802002)
    Event_11806100(3, character=1800103, destination=1802003)
    Event_11806100(4, character=1800104, destination=1802004)
    Event_11806100(5, 1800105, 1802005)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_11800002()
    DisableSoundEvent(sound_id=1803800)
    SkipLinesIfFlagDisabled(4, 15)
    Event_11805392()
    DisableObject(1801990)
    DeleteVFX(1801991, erase_root_only=False)
    SkipLines(7)
    Event_11805390()
    Event_11805391()
    Event_11805393()
    Event_11805392()
    Event_11800001()
    Event_11805394()
    Event_11805395()
    HumanityRegistration(6544, event_flag=8310)
    Event_11805030()
    Event_11805032()
    Event_11800550(0, first_flag=1000, last_flag=1029, flag=1012)
    EnableImmortality(6331)
    SkipLinesIfFlagEnabled(1, 830)
    DisableCharacter(6331)
    SkipLinesIfFlagEnabled(6, 15)
    Event_11800539(0, character=6331, first_flag=1640, last_flag=1647, flag=1647)
    Event_11800530(0, character=6331, first_flag=1640, last_flag=1647, flag=1644)
    Event_11800531(0, character=6331, first_flag=1640, last_flag=1647, flag=1645)
    Event_11800537(0, character=6331, first_flag=1640, last_flag=1647, flag=1649)
    Event_11800541(0, character=6331)
    Event_11806200()
    EnableImmortality(6341)
    SkipLinesIfFlagEnabled(1, 831)
    DisableCharacter(6341)
    SkipLinesIfFlagEnabled(6, 15)
    Event_11800540(0, character=6341, first_flag=1670, last_flag=1677, flag=1677)
    Event_11800533(0, character=6341, first_flag=1670, last_flag=1677, flag=1673)
    Event_11800534(0, character=6341, first_flag=1670, last_flag=1677, flag=1674)
    Event_11800538(0, character=6341, first_flag=1670, last_flag=1677, flag=1678)
    Event_11800542(0, character=6341)
    Event_11806201()


@RestartOnRest(11805090)
def Event_11805090():
    """Event 11805090"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1800900)
    DisableCharacter(1800901)
    DisableCharacter(1800902)
    DisableCharacter(1800903)
    DisableCharacter(1800904)
    IfFlagEnabled(0, 11800050)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1800900)
    EnableCharacter(1800901)
    EnableCharacter(1800902)
    EnableCharacter(1800903)
    EnableCharacter(1800904)


@RestartOnRest(11805091)
def Event_11805091():
    """Event 11805091"""
    IfFlagEnabled(-1, 11805095)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
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
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11800050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11800050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11800050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11800050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11800050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11800050)
    RestartIfConditionFalse(-6)
    EnableFlag(11800050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=KILN_OF_THE_FIRST_FLAME)
    RestartIfConditionFalse(7)
    DisableFlag(11800050)
    EnableFlag(11805095)


@NeverRestart(11805390)
def Event_11805390():
    """Event 11805390"""
    IfFlagDisabled(1, 15)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1802998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1801990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1802997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11805391)
def Event_11805391():
    """Event 11805391"""
    IfFlagDisabled(1, 15)
    IfFlagEnabled(1, 11805393)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1802998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1801990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1802997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11805393)
def Event_11805393():
    """Event 11805393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 15)
    IfCharacterInsideRegion(1, PLAYER, region=1802996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1800800)


@RestartOnRest(11805392)
def Event_11805392():
    """Event 11805392"""
    SkipLinesIfFlagDisabled(3, 15)
    DisableCharacter(1800800)
    Kill(1800800)
    End()
    DisableAI(1800800)
    IfFlagEnabled(1, 11805393)
    IfCharacterInsideRegion(1, PLAYER, region=1802996)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1800800)
    EnableBossHealthBar(1800800, name=5370)


@NeverRestart(11800001)
def Event_11800001():
    """Event 11800001"""
    DisableObject(1801111)
    DisableObject(1801950)
    IfCharacterDead(0, 1800800)
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


@NeverRestart(20)
def Event_20():
    """Event 20"""
    EndIfClient()
    IfFlagEnabled(1, 15)
    IfActionButton(
        1,
        prompt_text=10010108,
        anchor_entity=1801950,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    IncrementNewGameCycle(dummy_arg=1)
    PlayCutscene(180000, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=1)
    EnableFlag(20)


@NeverRestart(21)
def Event_21():
    """Event 21"""
    EndIfClient()
    IfFlagEnabled(1, 15)
    IfCharacterOutsideRegion(1, PLAYER, region=1802990)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    IncrementNewGameCycle(dummy_arg=1)
    PlayCutscene(180001, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=2)
    EnableFlag(21)


@NeverRestart(11805394)
def Event_11805394():
    """Event 11805394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 15)
    IfFlagEnabled(1, 11805392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11805391)
    IfCharacterInsideRegion(1, PLAYER, region=1802990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1803800)


@NeverRestart(11805395)
def Event_11805395():
    """Event 11805395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 15)
    IfFlagEnabled(1, 11805394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1803800)


@RestartOnRest(11800002)
def Event_11800002():
    """Event 11800002"""
    IfFlagEnabled(0, 15)
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


@NeverRestart(11800100)
def Event_11800100():
    """Event 11800100"""
    EndIfThisEventFlagEnabled()
    DisableObject(1801110)
    IfHost(1)
    IfPlayerHasGood(1, 2510)
    IfActionButton(1, prompt_text=10010105, anchor_entity=1801960, anchor_type=CoordEntityType.Object, model_point=150)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180015, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableObject(1801110)
    RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=10)
    RemoveGoodFromPlayer(item=2510)


@NeverRestart(11800101)
def Event_11800101():
    """Event 11800101"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11800100)
    IfPlayerDoesNotHaveGood(1, 2510)
    IfActionButton(
        1,
        prompt_text=10010105,
        anchor_entity=1801960,
        anchor_type=CoordEntityType.Object,
        model_point=150,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(2, 11800100)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    DisplayDialog(text=10010174, anchor_entity=1801960)
    Restart()


@NeverRestart(11800200)
def Event_11800200():
    """Event 11800200"""
    IfFlagEnabled(0, 756)
    ForceAnimation(PLAYER, 7697)
    WaitFrames(frames=75)
    IfFlagDisabled(1, 11800201)
    IfPlayerHasGood(1, 2500)
    IfFlagDisabled(2, 11800202)
    IfPlayerHasGood(2, 2501)
    IfFlagDisabled(3, 11800203)
    IfPlayerHasGood(3, 2502)
    IfFlagDisabled(4, 11800204)
    IfPlayerHasGood(4, 2503)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=1)
    EnableFlag(11800201)
    RemoveGoodFromPlayer(item=2500)
    SkipLinesIfFinishedConditionFalse(2, condition=2)
    EnableFlag(11800202)
    RemoveGoodFromPlayer(item=2501)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    EnableFlag(11800203)
    RemoveGoodFromPlayer(item=2502)
    SkipLinesIfFinishedConditionFalse(2, condition=4)
    EnableFlag(11800204)
    RemoveGoodFromPlayer(item=2503)
    EnableFlag(11805111)
    IfFlagDisabled(0, 11805111)
    WaitFrames(frames=10)
    EndIfFlagEnabled(11800211)
    DisableFlag(756)
    Restart()


@NeverRestart(11800230)
def Event_11800230(_, value: int, model_point: int, obj: int):
    """Event 11800230"""
    IfFlagEnabled(1, 11805111)
    IfTrueFlagCountEqual(1, FlagType.Absolute, flag_range=(11800201, 11800204), value=value)
    IfConditionTrue(0, input_condition=1)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=100, model_point=model_point)
    WaitFrames(frames=95)
    SkipLinesIfFlagRangeAllEnabled(1, (11800201, 11800204))
    ForceAnimation(PLAYER, 7701, loop=True)
    DisableFlag(11805111)


@NeverRestart(11800210)
def Event_11800210():
    """Event 11800210"""
    SkipLinesIfFlagEnabled(17, 15)
    IfTrueFlagCountEqual(2, FlagType.Absolute, flag_range=(11800201, 11800204), value=1)
    IfTrueFlagCountEqual(3, FlagType.Absolute, flag_range=(11800201, 11800204), value=2)
    IfTrueFlagCountEqual(4, FlagType.Absolute, flag_range=(11800201, 11800204), value=3)
    IfTrueFlagCountEqual(5, FlagType.Absolute, flag_range=(11800201, 11800204), value=4)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    CreateObjectVFX(1801960, vfx_id=100, model_point=180005)
    SkipLinesIfFinishedConditionFalse(1, condition=3)
    CreateObjectVFX(1801960, vfx_id=100, model_point=180006)
    SkipLinesIfFinishedConditionFalse(1, condition=4)
    CreateObjectVFX(1801960, vfx_id=100, model_point=180007)
    SkipLinesIfFinishedConditionFalse(1, condition=5)
    CreateObjectVFX(1801960, vfx_id=100, model_point=180008)
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1801101, animation_id=1)
    End()
    IfFlagEnabled(1, 11800201)
    IfFlagEnabled(1, 11800202)
    IfFlagEnabled(1, 11800203)
    IfFlagEnabled(1, 11800204)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11800211)
    DisableFlag(756)
    PlayCutscene(180010, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EndOfAnimation(obj=1801101, animation_id=1)
    RegisterBonfire(bonfire_flag=11800992, obj=1801960, initial_kindle_level=30)


@NeverRestart(11800220)
def Event_11800220():
    """Event 11800220"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11800210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1802100,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1801101,
    )
    IfFlagEnabled(2, 11805110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    DisplayDialog(text=10010160, anchor_entity=1801101)
    SkipLines(2)
    DisableFlag(11805110)
    DisplayDialog(text=10010171, anchor_entity=1801960)
    Restart()


@RestartOnRest(11806100)
def Event_11806100(_, character: int, destination: int):
    """Event 11806100"""
    DisableNetworkSync()
    SkipLinesIfThisEventSlotFlagEnabled(3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    DisableAI(character)
    ForceAnimation(character, 200, loop=True)
    IfCharacterInsideRegion(0, character, region=1802006)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


@RestartOnRest(11805100)
def Event_11805100(_, character: int, item_lot_param_id: int):
    """Event 11805100"""
    IfCharacterAlive(0, character)
    IfCharacterDead(0, character)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot_param_id, host_only=True)


@NeverRestart(11800510)
def Event_11800510(_, character: int, flag: int):
    """Event 11800510"""
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


@NeverRestart(11800520)
def Event_11800520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(character)
    End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800530)
def Event_11800530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800530"""
    IfFlagEnabled(1, 1643)
    IfFlagEnabled(1, 830)
    IfFlagEnabled(1, 11800100)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800531)
def Event_11800531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800531"""
    IfFlagEnabled(1, 1644)
    IfFlagEnabled(1, 830)
    IfFlagEnabled(1, 11800210)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800533)
def Event_11800533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800533"""
    IfFlagEnabled(1, 1672)
    IfFlagEnabled(1, 831)
    IfFlagEnabled(1, 11800100)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800534)
def Event_11800534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800534"""
    IfFlagEnabled(1, 1673)
    IfFlagEnabled(1, 831)
    IfFlagEnabled(1, 11800210)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800537)
def Event_11800537(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800537"""
    IfFlagEnabled(-1, 1642)
    IfFlagEnabled(-1, 1643)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 830)
    IfFlagEnabled(1, 11800100)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800538)
def Event_11800538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800538"""
    IfFlagEnabled(-1, 1671)
    IfFlagEnabled(-1, 1672)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 831)
    IfFlagEnabled(1, 11800100)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11800539)
def Event_11800539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800539"""
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagEnabled(-7, 11020598)
    IfHealthLessThanOrEqual(7, character, value=0.8999999761581421)
    IfHealthGreaterThan(7, character, value=0.0)
    IfAttacked(7, attacked_entity=character, attacker=PLAYER)
    IfEntityBeyondDistance(7, entity=character, other_entity=PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(2, flag)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, condition=2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7009, wait_for_completion=True)
    DisableCharacter(character)


@NeverRestart(11800540)
def Event_11800540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11800540"""
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagEnabled(-7, 11600590)
    IfHealthLessThanOrEqual(7, character, value=0.8999999761581421)
    IfHealthGreaterThan(7, character, value=0.0)
    IfAttacked(7, attacked_entity=character, attacker=PLAYER)
    IfEntityBeyondDistance(7, entity=character, other_entity=PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(2, flag)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, condition=2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@NeverRestart(11800541)
def Event_11800541(_, character: int):
    """Event 11800541"""
    IfFlagEnabled(1, 830)
    IfFlagDisabled(1, 1647)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(character)
    IfFlagDisabled(0, 830)
    DisableCharacter(character)
    Restart()


@NeverRestart(11800542)
def Event_11800542(_, character: int):
    """Event 11800542"""
    IfFlagEnabled(1, 831)
    IfFlagDisabled(1, 1676)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(character)
    IfFlagDisabled(0, 831)
    DisableCharacter(character)
    Restart()


@NeverRestart(11800550)
def Event_11800550(_, first_flag: int, last_flag: int, flag: int):
    """Event 11800550"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1003)
    IfFlagEnabled(1, 11410595)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11806200)
def Event_11806200():
    """Event 11806200"""
    IfFlagEnabled(-1, 1643)
    IfFlagEnabled(-1, 1644)
    IfFlagEnabled(-1, 1645)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagEnabled(1, 824)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(824)
    PlayCutscene(180050, cutscene_flags=0, player_id=10000, move_to_region=1022110, game_map=FIRELINK_SHRINE)
    PlayCutscene(100250, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(6331)
    DisableFlag(830)
    Restart()


@NeverRestart(11806201)
def Event_11806201():
    """Event 11806201"""
    IfFlagEnabled(-1, 1672)
    IfFlagEnabled(-1, 1673)
    IfFlagEnabled(-1, 1674)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagEnabled(1, 825)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(825)
    PlayCutscene(180051, cutscene_flags=0, player_id=10000, move_to_region=1602110, game_map=NEW_LONDO_RUINS)
    PlayCutscene(160050, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(6341)
    DisableFlag(831)
    Restart()


@NeverRestart(11805030)
def Event_11805030():
    """Event 11805030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6544, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11805033)
    IfClient(2)
    IfFlagEnabled(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6544)
    EndIfFlagEnabled(15)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 1012)
    IfCharacterBackreadEnabled(1, 6544)
    IfEntityWithinDistance(1, entity=6544, other_entity=PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6544,
        region=1802050,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


@NeverRestart(11805032)
def Event_11805032():
    """Event 11805032"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11805031)
    IfFlagEnabled(1, 11805393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6544, command_id=10, command_slot=0)
    ReplanAI(6544)
    IfEntityWithinDistance(0, entity=6544, other_entity=1801990, radius=1.5)
    RotateToFaceEntity(6544, target_entity=1802997)
    ForceAnimation(6544, 7410)
    AICommand(6544, command_id=-1, command_slot=0)
    ReplanAI(6544)


@RestartOnRest(11805200)
def Event_11805200():
    """Event 11805200"""
    DisableAI(1800999)
    IfPlayerMovingOnCollision(1, 1803000)
    IfPlayerRunningOnCollision(2, 1803000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    RequestAnimation(1800999, animation_id=1750, wait_for_completion=True)
    Restart()
    RequestAnimation(1800999, animation_id=2000, wait_for_completion=True)
    Restart()
