"""
Catacombs

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11300992, obj=1301960)
    RegisterBonfire(bonfire_flag=11300984, obj=1301961)
    RegisterLadder(start_climbing_flag=11300010, stop_climbing_flag=11300011, obj=1301140)
    RegisterLadder(start_climbing_flag=11300012, stop_climbing_flag=11300013, obj=1301141)
    RegisterLadder(start_climbing_flag=11300014, stop_climbing_flag=11300015, obj=1301142)
    if FlagEnabled(6):
        RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=1301143)
    RegisterLadder(start_climbing_flag=11300018, stop_climbing_flag=11300019, obj=1301144)
    RegisterLadder(start_climbing_flag=11300020, stop_climbing_flag=11300021, obj=1301145)
    RegisterLadder(start_climbing_flag=11300022, stop_climbing_flag=11300023, obj=1301146)
    RegisterLadder(start_climbing_flag=11300024, stop_climbing_flag=11300025, obj=1301147)
    RegisterLadder(start_climbing_flag=11300026, stop_climbing_flag=11300027, obj=1301148)
    RegisterLadder(start_climbing_flag=11300028, stop_climbing_flag=11300029, obj=1301149)
    SkipLinesIfClient(3)
    DisableFlag(11300000)
    DisableObject(1301994)
    DeleteVFX(1301995, erase_root_only=False)
    Event_11300090(0, obj=1301700, vfx_id=1301701, destination=1302650, destination_1=1302651)
    Event_11305065()
    Event_11305066()
    Event_11305067()
    Event_11300800()
    Event_11300300()
    Event_11300350()
    Event_11300900(0, obj_act_id=11300900, obj=1301000, obj_1=1301100, navmesh_id=1304000)
    Event_11300900(1, obj_act_id=11300901, obj=1301001, obj_1=1301101, navmesh_id=1304001)
    Event_11305032(0, obj_act_id=11300902, obj_act_id_1=11300903, flag=11305035, flag_1=11305036)
    Event_11305030(0, flag=11300402, flag_1=11305035, flag_2=11305036, obj=1301002, obj_1=1301102, navmesh_id=1304002)
    Event_11305032(1, obj_act_id=11300904, obj_act_id_1=11300905, flag=11305037, flag_1=11305038)
    Event_11305030(1, flag=11300403, flag_1=11305037, flag_2=11305038, obj=1301003, obj_1=1301103, navmesh_id=1304003)
    Event_11305000()
    Event_11305001()
    Event_11305002()
    Event_11305003()
    Event_11305004()
    Event_11305009()
    Event_11300420(0, character=10000)
    Event_11300420(1, character=10001)
    Event_11300420(2, character=10002)
    Event_11300420(3, character=10003)
    Event_11300420(4, character=10004)
    Event_11300420(5, character=10005)
    Event_11300210()
    Event_11305060()
    Event_11300200()
    Event_11305045()
    Event_11300100(0, flag=11300100, region=1302100, obj=1301010, sound_id=303000000)
    Event_11300100(1, flag=11300101, region=1302101, obj=1301011, sound_id=303100000)
    Event_11300100(2, flag=11300102, region=1302102, obj=1301012, sound_id=303200000)
    Event_11300100(3, flag=11300103, region=1302103, obj=1301013, sound_id=303300000)
    Event_11300100(4, flag=11300104, region=1302104, obj=1301014, sound_id=303400000)
    Event_11300100(5, flag=11300105, region=1302105, obj=1301015, sound_id=303500000)
    Event_11300150()
    Event_11300160()
    Event_11300700(0, obj=1301200, obj_flag=11300750)
    Event_11300700(1, obj=1301201, obj_flag=11300751)
    Event_11300700(2, obj=1301202, obj_flag=11300752)
    Event_11300700(3, obj=1301203, obj_flag=11300753)
    Event_11300700(4, obj=1301204, obj_flag=11300754)
    Event_11300700(5, obj=1301205, obj_flag=11300755)
    Event_11300700(6, obj=1301206, obj_flag=11300756)
    Event_11300700(7, obj=1301207, obj_flag=11300757)
    Event_11300700(8, obj=1301208, obj_flag=11300758)
    Event_11300700(9, obj=1301209, obj_flag=11300759)
    Event_11300700(10, obj=1301210, obj_flag=11300760)
    Event_11300700(12, obj=1301212, obj_flag=11300762)
    Event_11300700(13, obj=1301213, obj_flag=11300763)
    Event_11300700(14, obj=1301214, obj_flag=11300764)
    Event_11300700(15, obj=1301215, obj_flag=11300765)
    Event_11300700(16, obj=1301216, obj_flag=11300766)
    Event_11300700(17, obj=1301217, obj_flag=11300767)
    Event_11300700(18, obj=1301218, obj_flag=11300768)
    Event_11300700(19, obj=1301219, obj_flag=11300769)
    Event_11300880()
    DisableSoundEvent(sound_id=1303800)
    if FlagEnabled(6):
        DisableObject(1301990)
        DeleteVFX(1301991, erase_root_only=False)
        Event_11305392()
    else:
        Event_11305390()
        Event_11305391()
        Event_11305393()
        Event_11305392()
        Event_11300001()
        Event_11305394()
        Event_11305395()
        Event_11300882()
        Event_11305396()
        Event_11305397()
        Event_11305398()
        Event_11305250()
        Event_11305350(
            0,
            flag=11305251,
            flag_1=11305252,
            character=1300801,
            character_1=1300802,
            destination=1302600,
            destination_1=1302612,
            flag_2=11305300,
        )
        Event_11305350(
            1,
            flag=11305253,
            flag_1=11305254,
            character=1300803,
            character_1=1300804,
            destination=1302601,
            destination_1=1302611,
            flag_2=11305301,
        )
        Event_11305350(
            2,
            flag=11305255,
            flag_1=11305256,
            character=1300805,
            character_1=1300806,
            destination=1302602,
            destination_1=1302610,
            flag_2=11305302,
        )
        Event_11305350(
            3,
            flag=11305257,
            flag_1=11305258,
            character=1300807,
            character_1=1300808,
            destination=1302603,
            destination_1=1302609,
            flag_2=11305303,
        )
        Event_11305350(
            4,
            flag=11305259,
            flag_1=11305260,
            character=1300809,
            character_1=1300810,
            destination=1302604,
            destination_1=1302608,
            flag_2=11305304,
        )
        Event_11305350(
            5,
            flag=11305261,
            flag_1=11305262,
            character=1300811,
            character_1=1300812,
            destination=1302605,
            destination_1=1302607,
            flag_2=11305305,
        )
        Event_11305350(
            6,
            flag=11305263,
            flag_1=11305264,
            character=1300813,
            character_1=1300814,
            destination=1302606,
            destination_1=1302606,
            flag_2=11305306,
        )
        Event_11305370(0, character=1300801, flag=11305251)
        Event_11305370(1, character=1300802, flag=11305252)
        Event_11305370(2, character=1300803, flag=11305253)
        Event_11305370(3, character=1300804, flag=11305254)
        Event_11305370(4, character=1300805, flag=11305255)
        Event_11305370(5, character=1300806, flag=11305256)
        Event_11305370(6, character=1300807, flag=11305257)
        Event_11305370(7, character=1300808, flag=11305258)
        Event_11305370(8, character=1300809, flag=11305259)
        Event_11305370(9, character=1300810, flag=11305260)
        Event_11305370(10, character=1300811, flag=11305261)
        Event_11305370(11, character=1300812, flag=11305262)
        Event_11305370(12, character=1300813, flag=11305263)
    Event_11305370(13, character=1300814, flag=11305264)
    Event_11300850(0, character=1300100, item_lot=0)
    Event_11300850(1, character=1300120, item_lot=0)
    Event_11300850(2, character=1300140, item_lot=0)
    Event_11300850(3, character=1300160, item_lot=0)
    Event_11300850(4, character=1300180, item_lot=0)
    Event_11300850(5, character=1300200, item_lot=0)
    Event_11300850(6, character=1300500, item_lot=33003000)
    Event_11300850(7, character=1300501, item_lot=33003000)
    Event_11300850(8, character=1300300, item_lot=0)
    Event_11300850(9, character=1300400, item_lot=27902000)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6550, event_flag=8948)
    Event_11305025()
    Event_11305027()
    Event_11300510(0, character=6200, flag=1341)
    Event_11300520(0, character=6200, first_flag=1340, last_flag=1343, flag=1342)
    Event_11305061(0, character=6200)
    HumanityRegistration(6320, event_flag=8478)
    SkipLinesIfFlagEnabled(2, 1627)
    SkipLinesIfFlagRangeAnyEnabled(1, (1620, 1621))
    DisableCharacter(6320)
    Event_11300510(1, character=6320, flag=1627)
    Event_11300531(0, character=6320, flag=1628)
    Event_11300530(0, character=6320, first_flag=1620, last_flag=1631, flag=1621)
    Event_11300533(0, character=6320, first_flag=1620, last_flag=1631, flag=1623)
    Event_11300592()
    Event_11300593()


@ContinueOnRest(11300090)
def Event_11300090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11300090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11305065)
def Event_11305065():
    """Event 11305065"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1300900)
    DisableCharacter(1300901)
    DisableCharacter(1300902)
    DisableCharacter(1300903)
    DisableCharacter(1300904)
    DisableCharacter(1300905)
    DisableCharacter(1300906)
    DisableCharacter(1300907)
    DisableCharacter(1300908)
    DisableCharacter(1300909)
    DisableCharacter(1300910)
    
    MAIN.Await(FlagEnabled(11300050))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1300900)
    EnableCharacter(1300901)
    EnableCharacter(1300902)
    EnableCharacter(1300903)
    EnableCharacter(1300904)
    EnableCharacter(1300905)
    EnableCharacter(1300906)
    EnableCharacter(1300907)
    EnableCharacter(1300908)
    EnableCharacter(1300909)
    EnableCharacter(1300910)


@RestartOnRest(11305066)
def Event_11305066():
    """Event 11305066"""
    OR_1.Add(FlagEnabled(11305069))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11300050)
    DisableFlag(11305069)
    EnableFlag(5001)
    Kill(1300900)
    Kill(1300901)
    Kill(1300902)
    Kill(1300903)
    Kill(1300904)
    Kill(1300905)
    Kill(1300906)
    Kill(1300907)
    Kill(1300908)
    Kill(1300909)
    Kill(1300910)


@RestartOnRest(11305067)
def Event_11305067():
    """Event 11305067"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=CATACOMBS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11300050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=CATACOMBS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11300050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=CATACOMBS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11300050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=CATACOMBS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11300050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=CATACOMBS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11300050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=CATACOMBS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11300050))
    if not OR_6:
        return RESTART
    EnableFlag(11300050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=CATACOMBS))
    if not AND_7:
        return RESTART
    DisableFlag(11300050)
    EnableFlag(11305069)


@ContinueOnRest(11305390)
def Event_11305390():
    """Event 11305390"""
    AND_1.Add(FlagDisabled(6))
    AND_1.Add(CharacterAlive(1300800))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1302998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1301990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11305391)
def Event_11305391():
    """Event 11305391"""
    AND_1.Add(FlagDisabled(6))
    AND_1.Add(FlagEnabled(11305393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1302998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1301990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11305393)
def Event_11305393():
    """Event 11305393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(6))
        AND_1.Add(FlagEnabled(11305390))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1302996))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1300800)


@RestartOnRest(11305392)
def Event_11305392():
    """Event 11305392"""
    if FlagEnabled(6):
        DisableCharacter(1300800)
        Kill(1300800)
        End()
    if FlagDisabled(11300000):
        DisableCharacter(1300800)
    DisableAI(1300800)
    AND_1.Add(FlagDisabled(6))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(8, 11300000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(130000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1300800)
    EnableFlag(11300000)
    EnableFlag(11300005)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1300800, authority_level=UpdateAuthority.Forced)
    EnableAI(1300800)
    EnableBossHealthBar(1300800, name=3320)


@ContinueOnRest(11300001)
def Event_11300001():
    """Event 11300001"""
    MAIN.Await(HealthRatio(1300800) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(1300800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(1300800))
    
    EnableFlag(6)
    KillBoss(game_area_param_id=1300800)
    DisableObject(1301990)
    DeleteVFX(1301991)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=1301143)
    Event_11300880()


@ContinueOnRest(11305394)
def Event_11305394():
    """Event 11305394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(6))
    AND_1.Add(FlagEnabled(11305392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11305391))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1303800)


@ContinueOnRest(11305395)
def Event_11305395():
    """Event 11305395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(6))
    AND_1.Add(FlagEnabled(11305394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1303800)


@ContinueOnRest(11305396)
def Event_11305396():
    """Event 11305396"""
    MAIN.Await(CharacterHasTAEEvent(1300800, tae_event_id=600))
    
    DisableCharacter(1300800)
    DisableFlagRange((11305320, 11305326))
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(1300800, authority_level=UpdateAuthority.Forced)
    EnableRandomFlagInRange(flag_range=(11305320, 11305326))
    EnableFlag(11305329)
    OR_1.Add(FlagDisabled(11305329))
    OR_1.Add(TimeElapsed(seconds=5.0))
    
    MAIN.Await(OR_1)
    
    Wait(3.0)
    EnableCharacter(1300800)
    if FlagEnabled(11305320):
        Move(1300800, destination=1302600, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305321):
        Move(1300800, destination=1302602, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305322):
        Move(1300800, destination=1302604, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305323):
        Move(1300800, destination=1302605, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305324):
        Move(1300800, destination=1302606, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305325):
        Move(1300800, destination=1302608, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305326):
        Move(1300800, destination=1302612, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=1)
    EnableCharacter(1300800)
    ForceAnimation(1300800, 7000, wait_for_completion=True)
    Restart()


@ContinueOnRest(11300882)
def Event_11300882():
    """Event 11300882"""
    AND_1.Add(FlagEnabled(11305329))
    AND_2.Add(FlagEnabled(11305329))
    AND_3.Add(FlagEnabled(11305329))
    AND_4.Add(FlagEnabled(11305329))
    AND_5.Add(FlagEnabled(11305329))
    AND_6.Add(FlagEnabled(11305329))
    AND_7.Add(FlagEnabled(11305329))
    AND_1.Add(FlagEnabled(11305320))
    AND_2.Add(FlagEnabled(11305321))
    AND_3.Add(FlagEnabled(11305322))
    AND_4.Add(FlagEnabled(11305323))
    AND_5.Add(FlagEnabled(11305324))
    AND_6.Add(FlagEnabled(11305325))
    AND_7.Add(FlagEnabled(11305326))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_1)
    EnableFlag(11305320)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_2)
    EnableFlag(11305321)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_3)
    EnableFlag(11305322)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_4)
    EnableFlag(11305323)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_5)
    EnableFlag(11305324)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_6)
    EnableFlag(11305325)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_7)
    EnableFlag(11305326)
    DisableFlag(11305329)
    Restart()


@ContinueOnRest(11305397)
def Event_11305397():
    """Event 11305397"""
    if Client():
        return
    if FlagDisabled(11305310):
        AND_1.Add(FlagDisabled(11305399))
        AND_1.Add(CharacterHasTAEEvent(1300800, tae_event_id=700))
    
        MAIN.Await(AND_1)
    
        EnableFlag(11305310)
    DisableFlagRange((11305300, 11305306))
    EnableRandomFlagInRange(flag_range=(11305300, 11305306))
    SkipLinesIfFlagDisabled(2, 11305300)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305251, 11305252))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305301)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305253, 11305254))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305302)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305255, 11305256))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305303)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305257, 11305258))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305304)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305259, 11305260))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305305)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305261, 11305262))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305306)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305263, 11305264))
    DisableFlag(11305310)
    if FlagEnabled(11305310):
        return RESTART
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(1300800, tae_event_id=700))
    
    Restart()


@ContinueOnRest(11305398)
def Event_11305398():
    """Event 11305398"""
    MAIN.Await(HealthRatio(1300800) <= 0.30000001192092896)
    
    EnableFlag(11305399)
    AICommand(1300800, command_id=1, command_slot=1)
    ReplanAI(1300800)
    Event_11305330(0, character=1300801, flag=11305251)
    Event_11305330(1, character=1300802, flag=11305252)
    Event_11305330(2, character=1300803, flag=11305253)
    Event_11305330(3, character=1300804, flag=11305254)
    Event_11305330(4, character=1300805, flag=11305255)
    Event_11305330(5, character=1300806, flag=11305256)
    Event_11305330(6, character=1300807, flag=11305257)
    Event_11305330(7, character=1300808, flag=11305258)
    Event_11305330(8, character=1300809, flag=11305259)
    Event_11305330(9, character=1300810, flag=11305260)
    Event_11305330(10, character=1300811, flag=11305261)
    Event_11305330(11, character=1300812, flag=11305262)
    Event_11305330(12, character=1300813, flag=11305263)
    Event_11305330(13, character=1300814, flag=11305264)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(11305251, 11305264)))
    
    AICommand(1300800, command_id=2, command_slot=1)
    ReplanAI(1300800)
    AND_1.Add(FlagEnabled(11305399))
    AND_1.Add(CharacterHasTAEEvent(1300800, tae_event_id=700))
    
    MAIN.Await(AND_1)
    
    AICommand(1300800, command_id=1, command_slot=1)
    ReplanAI(1300800)
    Event_11305350(
        10,
        flag=11305251,
        flag_1=11305252,
        character=1300801,
        character_1=1300802,
        destination=1302602,
        destination_1=1302603,
        flag_2=11305300,
    )
    Event_11305350(
        11,
        flag=11305253,
        flag_1=11305254,
        character=1300803,
        character_1=1300804,
        destination=1302604,
        destination_1=1302605,
        flag_2=11305301,
    )
    Event_11305350(
        12,
        flag=11305255,
        flag_1=11305256,
        character=1300805,
        character_1=1300806,
        destination=1302607,
        destination_1=1302608,
        flag_2=11305302,
    )
    Event_11305350(
        13,
        flag=11305257,
        flag_1=11305258,
        character=1300807,
        character_1=1300808,
        destination=1302609,
        destination_1=1302612,
        flag_2=11305303,
    )


@ContinueOnRest(11305330)
def Event_11305330(_, character: int, flag: int):
    """Event 11305330"""
    AICommand(character, command_id=1, command_slot=1)
    ReplanAI(character)
    
    MAIN.Await(FlagDisabled(flag))
    
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)


@ContinueOnRest(11305350)
def Event_11305350(
    _,
    flag: int,
    flag_1: int,
    character: int,
    character_1: int,
    destination: int,
    destination_1: int,
    flag_2: int,
):
    """Event 11305350"""
    if FlagDisabled(11305399):
        AND_1.Add(Host())
        AND_1.Add(FlagDisabled(11305310))
        AND_1.Add(FlagEnabled(flag_2))
    
        MAIN.Await(AND_1)
    
        WaitForNetworkApproval(max_seconds=3.0)
    DisableFlag(flag_2)
    AddSpecialEffect(character, 5450)
    AddSpecialEffect(character_1, 5450)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    EnableCharacter(character_1)
    ReplanAI(character)
    ReplanAI(character_1)
    ForceAnimation(character, 7000)
    ForceAnimation(character_1, 7000)
    EnableFlag(flag)
    EnableFlag(flag_1)
    if FlagEnabled(11305399):
        return
    RestartEvent(event_id=11305250)
    Restart()


@ContinueOnRest(11305370)
def Event_11305370(_, character: int, flag: int):
    """Event 11305370"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=710))
    AND_2.Add(HealthRatio(1300800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfLastConditionResultTrue(3, input_condition=AND_1)
    AICommand(character, command_id=1, command_slot=1)
    ReplanAI(character)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=710))
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ResetAnimation(character, disable_interpolation=True)
    DisableCharacter(character)
    DisableFlag(flag)
    EndIfLastConditionResultTrue(input_condition=AND_2)
    RestartEvent(event_id=11305250)
    if FlagDisabled(flag):
        return RESTART


@ContinueOnRest(11305250)
def Event_11305250():
    """Event 11305250"""
    MAIN.Await(FlagEnabled(11305392))
    
    AIEvent(1300800, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300801, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300802, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300803, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300804, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300805, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300806, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300807, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300808, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300809, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300810, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300811, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300812, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300813, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300814, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    ReplanAI(1300800)
    ReplanAI(1300801)
    ReplanAI(1300802)
    ReplanAI(1300803)
    ReplanAI(1300804)
    ReplanAI(1300805)
    ReplanAI(1300806)
    ReplanAI(1300807)
    ReplanAI(1300808)
    ReplanAI(1300809)
    ReplanAI(1300810)
    ReplanAI(1300811)
    ReplanAI(1300812)
    ReplanAI(1300813)
    ReplanAI(1300814)
    
    MAIN.Await(CharacterDead(1300800))
    
    End()


@RestartOnRest(11300880)
def Event_11300880():
    """Event 11300880"""
    DisableHealthBar(1300801)
    DisableHealthBar(1300802)
    DisableHealthBar(1300803)
    DisableHealthBar(1300804)
    DisableHealthBar(1300805)
    DisableHealthBar(1300806)
    DisableHealthBar(1300807)
    DisableHealthBar(1300808)
    DisableHealthBar(1300809)
    DisableHealthBar(1300810)
    DisableHealthBar(1300811)
    DisableHealthBar(1300812)
    DisableHealthBar(1300813)
    DisableHealthBar(1300814)
    DisableCharacter(1300801)
    DisableCharacter(1300802)
    DisableCharacter(1300803)
    DisableCharacter(1300804)
    DisableCharacter(1300805)
    DisableCharacter(1300806)
    DisableCharacter(1300807)
    DisableCharacter(1300808)
    DisableCharacter(1300809)
    DisableCharacter(1300810)
    DisableCharacter(1300811)
    DisableCharacter(1300812)
    DisableCharacter(1300813)
    DisableCharacter(1300814)
    if FlagDisabled(6):
        EnableImmortality(1300801)
        EnableImmortality(1300802)
        EnableImmortality(1300803)
        EnableImmortality(1300804)
        EnableImmortality(1300805)
        EnableImmortality(1300806)
        EnableImmortality(1300807)
        EnableImmortality(1300808)
        EnableImmortality(1300809)
        EnableImmortality(1300810)
        EnableImmortality(1300811)
        EnableImmortality(1300812)
        EnableImmortality(1300813)
        EnableImmortality(1300814)
    if FlagDisabled(6):
        return
    Kill(1300801)
    Kill(1300802)
    Kill(1300803)
    Kill(1300804)
    Kill(1300805)
    Kill(1300806)
    Kill(1300807)
    Kill(1300808)
    Kill(1300809)
    Kill(1300810)
    Kill(1300811)
    Kill(1300812)
    Kill(1300813)
    Kill(1300814)


@ContinueOnRest(11300700)
def Event_11300700(_, obj: int, obj_flag: int):
    """Event 11300700"""
    MAIN.Await(EntityWithinDistance(entity=obj, other_entity=PLAYER, radius=1.5))
    
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        dummy_id=100,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        dummy_id=101,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        dummy_id=102,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(obj, 0, wait_for_completion=True)
    Restart()


@ContinueOnRest(11300300)
def Event_11300300():
    """Event 11300300"""
    MAIN.Await(FlagDisabled(11300402))
    
    CreateHazard(
        obj_flag=11300301,
        obj=1301102,
        dummy_id=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300302,
        obj=1301102,
        dummy_id=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300303,
        obj=1301102,
        dummy_id=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300304,
        obj=1301102,
        dummy_id=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300305,
        obj=1301102,
        dummy_id=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300306,
        obj=1301102,
        dummy_id=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300307,
        obj=1301102,
        dummy_id=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300308,
        obj=1301102,
        dummy_id=15,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    
    MAIN.Await(FlagEnabled(11300402))
    
    RemoveObjectFlag(obj_flag=11300301)
    RemoveObjectFlag(obj_flag=11300302)
    RemoveObjectFlag(obj_flag=11300303)
    RemoveObjectFlag(obj_flag=11300304)
    RemoveObjectFlag(obj_flag=11300305)
    RemoveObjectFlag(obj_flag=11300306)
    RemoveObjectFlag(obj_flag=11300307)
    RemoveObjectFlag(obj_flag=11300308)
    Restart()


@ContinueOnRest(11300350)
def Event_11300350():
    """Event 11300350"""
    MAIN.Await(FlagDisabled(11300403))
    
    CreateHazard(
        obj_flag=11300351,
        obj=1301103,
        dummy_id=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300352,
        obj=1301103,
        dummy_id=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300353,
        obj=1301103,
        dummy_id=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300354,
        obj=1301103,
        dummy_id=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300355,
        obj=1301103,
        dummy_id=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300356,
        obj=1301103,
        dummy_id=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300357,
        obj=1301103,
        dummy_id=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300358,
        obj=1301103,
        dummy_id=33,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300359,
        obj=1301103,
        dummy_id=35,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300360,
        obj=1301103,
        dummy_id=37,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300361,
        obj=1301103,
        dummy_id=39,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    
    MAIN.Await(FlagEnabled(11300403))
    
    RemoveObjectFlag(obj_flag=11300351)
    RemoveObjectFlag(obj_flag=11300352)
    RemoveObjectFlag(obj_flag=11300353)
    RemoveObjectFlag(obj_flag=11300354)
    RemoveObjectFlag(obj_flag=11300355)
    RemoveObjectFlag(obj_flag=11300356)
    RemoveObjectFlag(obj_flag=11300357)
    RemoveObjectFlag(obj_flag=11300358)
    RemoveObjectFlag(obj_flag=11300359)
    RemoveObjectFlag(obj_flag=11300360)
    RemoveObjectFlag(obj_flag=11300361)
    Restart()


@ContinueOnRest(11300900)
def Event_11300900(_, obj_act_id: int, obj: int, obj_1: int, navmesh_id: int):
    """Event 11300900"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj_1, animation_id=2)
        EndOfAnimation(obj=obj, animation_id=2)
        DisableObjectActivation(obj, obj_act_id=-1)
        End()
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    ForceAnimation(obj_1, 1)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)


@ContinueOnRest(11305030)
def Event_11305030(_, flag: int, flag_1: int, flag_2: int, obj: int, obj_1: int, navmesh_id: int):
    """Event 11305030"""
    if FlagEnabled(flag):
        DisableObjectActivation(obj, obj_act_id=3011)
        EndOfAnimation(obj=obj_1, animation_id=0)
        EndOfAnimation(obj=obj, animation_id=2)
    else:
        DisableObjectActivation(obj, obj_act_id=3012)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfLastConditionResultTrue(6, input_condition=AND_2)
    EnableFlag(flag)
    ForceAnimation(obj_1, 3)
    WaitFrames(frames=140)
    EnableObjectActivation(obj, obj_act_id=3012)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
    Restart()
    DisableFlag(flag)
    ForceAnimation(obj_1, 1)
    WaitFrames(frames=140)
    EnableObjectActivation(obj, obj_act_id=3011)
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
    Restart()


@ContinueOnRest(11305032)
def Event_11305032(_, obj_act_id: int, obj_act_id_1: int, flag: int, flag_1: int):
    """Event 11305032"""
    AND_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    EnableFlag(flag)
    Restart()
    EnableFlag(flag_1)
    Restart()


@ContinueOnRest(11305000)
def Event_11305000():
    """Event 11305000"""
    DisableNetworkSync()
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=CATACOMBS))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302700))
    AND_1.Add(FlagDisabled(11310000))
    AND_1.Add(PlayerHasGood(109))
    
    MAIN.Await(AND_1)
    
    Wait(30.0)
    if Multiplayer():
        return RESTART
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1302700))
    if not AND_6:
        return RESTART
    AND_7.Add(HealthRatio(PLAYER) <= 0.0)
    if AND_7:
        return RESTART
    EnableFlag(11310050)
    PlayCutscene(130020, cutscene_flags=0, player_id=10000, move_to_region=1312110, game_map=TOMB_OF_THE_GIANTS)
    PlayCutscene(130120, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableObjectActivation(1311300, obj_act_id=-1)
    SetStandbyAnimationSettings(PLAYER)
    Restart()


@RestartOnRest(11305001)
def Event_11305001():
    """Event 11305001"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302700))
    AND_1.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11305006)
    DisableObjectActivation(1301104, obj_act_id=3060)
    EnableObjectActivation(1301104, obj_act_id=3061)
    RestartEvent(event_id=11305002)
    RestartEvent(event_id=11305009)
    Restart()


@RestartOnRest(11305002)
def Event_11305002():
    """Event 11305002"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11305006))
    
    DisableFlag(11305006)
    Wait(5.0)
    EnableFlag(11305008)
    Restart()


@ContinueOnRest(11305003)
def Event_11305003():
    """Event 11305003"""
    MAIN.Await(FlagEnabled(11305008))
    
    EnableObjectActivation(1301104, obj_act_id=3060)
    DisableObjectActivation(1301104, obj_act_id=3061)
    DisableFlag(11305006)
    DisableFlag(11305008)
    RestartEvent(event_id=11305000)
    RestartEvent(event_id=11305001)
    RestartEvent(event_id=11305002)
    Restart()


@RestartOnRest(11305004)
def Event_11305004():
    """Event 11305004"""
    AND_1.Add(CharacterTargeting(targeting_character=1300300, targeted_character=PLAYER))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4130))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(1300300)
    ReplanAI(1300300)
    Restart()


@ContinueOnRest(11305009)
def Event_11305009():
    """Event 11305009"""
    AND_1.Add(AllPlayersOutsideRegion(region=1302700))
    AND_1.Add(EntityWithinDistance(entity=1301104, other_entity=PLAYER, radius=10.0))
    AND_1.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(AND_1)
    
    EnableObjectActivation(1301104, obj_act_id=3060)
    DisableObjectActivation(1301104, obj_act_id=3061)
    Restart()


@ContinueOnRest(11300420)
def Event_11300420(_, character: int):
    """Event 11300420"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=1301104, other_entity=character, radius=10.0))
    AND_1.Add(CharacterInsideRegion(character, region=1302700))
    
    MAIN.Await(AND_1)
    
    SetStandbyAnimationSettings(character, standby_animation=7151, death_animation=6082)
    AND_2.Add(EntityWithinDistance(entity=1301104, other_entity=character, radius=10.0))
    AND_2.Add(CharacterOutsideRegion(character, region=1302700))
    
    MAIN.Await(AND_2)
    
    SetStandbyAnimationSettings(character)
    Restart()


@ContinueOnRest(11300100)
def Event_11300100(_, flag: int, region: int, obj: int, sound_id: int):
    """Event 11300100"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=130000, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, sound_id, sound_type=SoundType.o_Object)


@ContinueOnRest(11300150)
def Event_11300150():
    """Event 11300150"""
    if ThisEventFlagEnabled():
        PostDestruction(1301020)
        End()
    DisableAI(1300050)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1302020))
    
    EnableAI(1300050)
    DestroyObject(1301020)
    PlaySoundEffect(1301020, 303600000, sound_type=SoundType.a_Ambient)


@ContinueOnRest(11300160)
def Event_11300160():
    """Event 11300160"""
    if ThisEventFlagEnabled():
        DisableObject(1301050)
        End()
    
    MAIN.Await(ObjectDestroyed(1301050))
    
    EnableFlag(11300160)


@ContinueOnRest(11300200)
def Event_11300200():
    """Event 11300200"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1301040, animation_id=0)
        End()
    
    MAIN.Await(FlagEnabled(6))
    
    ForceAnimation(1301040, 0)


@ContinueOnRest(11300210)
def Event_11300210():
    """Event 11300210"""
    if ThisEventFlagEnabled():
        DisableObject(1301030)
        DisableObject(1301031)
        End()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302030))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfMultiplayer(3)
    PlayCutscene(130010, cutscene_flags=0, player_id=10000, move_to_region=1302030, game_map=CATACOMBS)
    WaitFrames(frames=1)
    SkipLines(5)
    if FlagEnabled(11305060):
        PlayCutscene(
            130010,
            cutscene_flags=CutsceneFlags.Unskippable,
            player_id=10000,
            move_to_region=1302030,
            game_map=CATACOMBS,
        )
    else:
        PlayCutscene(130010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(1301030)
    DisableObject(1301031)


@ContinueOnRest(11305060)
def Event_11305060():
    """Event 11305060"""
    if FlagEnabled(11300210):
        return
    DisableNetworkSync()
    DisableFlag(11305060)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1302030))
    
    EnableFlag(11305060)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1302030))
    
    Restart()


@RestartOnRest(11300800)
def Event_11300800():
    """Event 11300800"""
    EnableFlag(11305200)
    EnableFlag(11305040)
    Event_11305050(1, flag=11305040, character=1300100, region=1302202, radius=10.0)
    Event_11305050(2, flag=11305051, character=1300100, region=1302203, radius=10.0)
    Event_11305050(3, flag=11305052, character=1300100, region=1302204, radius=10.0)
    Event_11305050(4, flag=11305053, character=1300100, region=1302205, radius=10.0)
    Event_11300801(0, character=1300100)
    Event_11300801(1, character=1300120)
    Event_11300801(2, character=1300140)
    Event_11300801(3, character=1300160)
    Event_11300801(4, character=1300180)
    Event_11300801(5, character=1300200)
    Event_11305100(0, character=1300100, character_1=1300101)
    Event_11305100(1, character=1300100, character_1=1300102)
    Event_11305100(2, character=1300100, character_1=1300103)
    Event_11305100(3, character=1300100, character_1=1300104)
    Event_11305100(4, character=1300100, character_1=1300105)
    Event_11305100(5, character=1300100, character_1=1300106)
    Event_11305100(6, character=1300100, character_1=1300107)
    Event_11305100(7, character=1300100, character_1=1300108)
    Event_11305100(8, character=1300100, character_1=1300109)
    Event_11305100(9, character=1300100, character_1=1300110)
    Event_11305100(10, character=1300100, character_1=1300111)
    Event_11305100(11, character=1300100, character_1=1300112)
    Event_11305100(12, character=1300100, character_1=1300113)
    Event_11305100(13, character=1300100, character_1=1300114)
    Event_11305100(14, character=1300120, character_1=1300121)
    Event_11305100(15, character=1300120, character_1=1300122)
    Event_11305100(16, character=1300120, character_1=1300123)
    Event_11305100(17, character=1300120, character_1=1300124)
    Event_11305100(18, character=1300120, character_1=1300125)
    Event_11305100(19, character=1300120, character_1=1300126)
    Event_11305100(20, character=1300120, character_1=1300127)
    Event_11305100(21, character=1300120, character_1=1300020)
    Event_11305100(22, character=1300140, character_1=1300141)
    Event_11305100(23, character=1300140, character_1=1300142)
    Event_11305100(24, character=1300140, character_1=1300143)
    Event_11305100(25, character=1300140, character_1=1300144)
    Event_11305100(26, character=1300140, character_1=1300145)
    Event_11305100(27, character=1300140, character_1=1300146)
    Event_11305100(28, character=1300140, character_1=1300147)
    Event_11305100(29, character=1300160, character_1=1300161)
    Event_11305100(30, character=1300160, character_1=1300162)
    Event_11305100(31, character=1300160, character_1=1300163)
    Event_11305100(32, character=1300160, character_1=1300164)
    Event_11305100(33, character=1300160, character_1=1300165)
    Event_11305100(34, character=1300160, character_1=1300166)
    Event_11305100(35, character=1300180, character_1=1300181)
    Event_11305100(36, character=1300180, character_1=1300182)
    Event_11305100(37, character=1300180, character_1=1300183)
    Event_11305100(38, character=1300180, character_1=1300184)
    Event_11305100(39, character=1300180, character_1=1300185)
    Event_11305100(40, character=1300180, character_1=1300000)
    Event_11305100(41, character=1300180, character_1=1300001)
    Event_11305100(44, character=1300200, character_1=1300201)
    Event_11305100(45, character=1300200, character_1=1300202)
    Event_11305100(46, character=1300200, character_1=1300203)
    Event_11305100(47, character=1300200, character_1=1300204)
    Event_11305100(48, character=1300200, character_1=1300205)
    Event_11305100(49, character=1300200, character_1=1300206)
    Event_11305100(50, character=1300200, character_1=1300207)
    Event_11305070(0, character=1300107, radius=5.0)
    Event_11305070(1, character=1300109, radius=5.0)
    Event_11305070(2, character=1300110, radius=5.0)
    Event_11305070(3, character=1300113, radius=5.0)
    Event_11305070(4, character=1300121, radius=5.0)
    Event_11305070(5, character=1300122, radius=5.0)
    Event_11305070(6, character=1300123, radius=5.0)
    Event_11305070(7, character=1300124, radius=5.0)
    Event_11305070(8, character=1300125, radius=5.0)
    Event_11305070(9, character=1300147, radius=5.0)
    Event_11305070(10, character=1300181, radius=5.0)
    Event_11305070(11, character=1300182, radius=5.0)
    Event_11305070(12, character=1300000, radius=5.0)
    Event_11305070(13, character=1300001, radius=5.0)
    Event_11305070(16, character=1300163, radius=5.0)
    Event_11305070(17, character=1300164, radius=5.0)
    Event_11305070(18, character=1300020, radius=5.0)
    Event_11305210(0, character=1300350)
    Event_11305210(1, character=1300351)
    Event_11305210(2, character=1300352)
    Event_11305210(3, character=1300353)
    Event_11305210(4, character=1300354)
    Event_11305210(5, character=1300355)
    Event_11305210(6, character=1300356)
    Event_11305210(7, character=1300357)
    Event_11305210(8, character=1300358)
    Event_11305210(9, character=1300359)
    Event_11305210(10, character=1300360)
    Event_11305210(13, character=1300363)


@EndOnRest(11305050)
def Event_11305050(_, flag: int, character: int, region: int, radius: float):
    """Event 11305050"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(11300801)
def Event_11300801(_, character: int):
    """Event 11300801"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@EndOnRest(11305070)
def Event_11305070(_, character: int, radius: float):
    """Event 11305070"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    SetStandbyAnimationSettings(character, cancel_animation=9061)


@EndOnRest(11305100)
def Event_11305100(_, character: int, character_1: int):
    """Event 11305100"""
    if ThisEventSlotFlagEnabled():
        RemoveSpecialEffect(character_1, 5451)
        End()
    EnableImmortality(character_1)
    
    MAIN.Await(CharacterDead(character))
    
    RemoveSpecialEffect(character_1, 5451)
    DisableImmortality(character_1)


@EndOnRest(11305210)
def Event_11305210(_, character: int):
    """Event 11305210"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=400))
    DisableCharacter(character)


@RestartOnRest(11305045)
def Event_11305045():
    """Event 11305045"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1300300)
    SetStandbyAnimationSettings(1300300, standby_animation=9000)
    OR_1.Add(EntityWithinDistance(entity=1300300, other_entity=PLAYER, radius=5.0))
    OR_1.Add(Attacked(attacked_entity=1300300, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(1300300)
    EnableAI(1300300)


@RestartOnRest(11300850)
def Event_11300850(_, character: int, item_lot: int):
    """Event 11300850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@ContinueOnRest(11300510)
def Event_11300510(_, character: int, flag: int):
    """Event 11300510"""
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
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11300520)
def Event_11300520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11300520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11300530)
def Event_11300530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11300530"""
    AND_1.Add(FlagDisabled(1622))
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(FlagEnabled(11300593))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11300531)
def Event_11300531(_, character: int, flag: int):
    """Event 11300531"""
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(1621))
    AND_2.Add(HealthRatio(character) <= 0.0)
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(1627)
    EnableFlag(flag)
    EndIfLastConditionResultFalse(input_condition=AND_3)
    DropMandatoryTreasure(character)


@ContinueOnRest(11300533)
def Event_11300533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11300533"""
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    OR_7.Add(FlagEnabled(1620))
    OR_7.Add(FlagEnabled(1621))
    AND_1.Add(OR_7)
    AND_2.Add(AND_1)
    AND_2.Add(FlagEnabled(6))
    AND_3.Add(AND_1)
    AND_3.Add(FlagEnabled(1173))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11305025)
def Event_11305025():
    """Event 11305025"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6550, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11305028)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11305026))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6550)
    if FlagEnabled(6):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(6550))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6550,
        region=1302050,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    
    MAIN.Await(FlagEnabled(11305026))
    
    SetNest(6550, region=1302051)


@ContinueOnRest(11305027)
def Event_11305027():
    """Event 11305027"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11305026))
    AND_1.Add(FlagEnabled(11305393))
    
    MAIN.Await(AND_1)
    
    AICommand(6550, command_id=10, command_slot=0)
    ReplanAI(6550)
    
    MAIN.Await(CharacterInsideRegion(6550, region=1302998))
    
    FaceEntity(6550, target_entity=1302997)
    ForceAnimation(6550, 7410)
    AICommand(6550, command_id=-1, command_slot=0)
    ReplanAI(6550)


@RestartOnRest(11305061)
def Event_11305061(_, character: int):
    """Event 11305061"""
    if ThisEventFlagEnabled():
        return
    DisableCharacterCollision(character)
    DisableGravity(character)
    WaitFrames(frames=10)
    EnableCharacterCollision(character)
    EnableGravity(character)


@ContinueOnRest(11300592)
def Event_11300592():
    """Event 11300592"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(FlagDisabled(11300403))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11300592)
    ActivateObject(1301003, obj_act_id=3011, relative_index=-1)


@ContinueOnRest(11300593)
def Event_11300593():
    """Event 11300593"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(FlagEnabled(11300592))
    AND_1.Add(FlagEnabled(11300403))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302001))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11300593)
    ActivateObject(1301003, obj_act_id=3012, relative_index=-1)
