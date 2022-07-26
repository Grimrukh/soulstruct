"""
Archdragon Peak

linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=13200000, obj=3201950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13200002, obj=3201952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13200003, obj=3201953, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13200850, bonfire_flag=13200001, character=3200951, obj=3201951)
    Event_13205390()
    CommonFunc_20005780(0, obj=3201781, model_point=2)
    CommonFunc_20005780(0, obj=3201782, model_point=2)
    CommonFunc_20005780(0, obj=3201783, model_point=2)
    CommonFunc_20005780(0, obj=3201784, model_point=2)
    Event_13205490(0, obj=3201785, model_point=2, flag=13200850)
    Event_13205490(1, obj=3201786, model_point=2, flag=13200850)
    CommonFunc_20005701(
        0,
        left=13200931,
        summon_flag=13204190,
        dismissal_flag=13205190,
        character=3200190,
        region=3202190,
        left_1=70000007,
    )
    CommonFunc_20005720(0, flag=13204190, flag_1=13205190, flag_2=13200445, character=3200190)
    Event_13205930()
    Event_13205931()
    Event_13205300()
    Event_13205310()
    Event_13205320()
    Event_13205330()
    Event_13205340()
    CommonFunc_20005341(0, flag=13200305, character=3200300, item_lot=31412000)
    CommonFunc_20005119(
        0,
        character=3200200,
        region=3202200,
        region_1=3202201,
        region_2=3202202,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200201,
        region=3202201,
        region_1=3202202,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200202,
        region=3202201,
        region_1=3202203,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005130(0, character=3200203, radius=15.0, region=3202203)
    CommonFunc_20005119(
        0,
        character=3200204,
        region=3202201,
        region_1=3202203,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005120(0, character=3200205, radius=15.0)
    CommonFunc_20005213(0, character=3200210, animation_id=700, animation_id_1=1700, radius=2.5, region=3202210)
    CommonFunc_20005132(0, character=3200211, radius=4.0, region=3202210)
    CommonFunc_20005119(
        0,
        character=3200212,
        region=3202212,
        region_1=3202213,
        region_2=3202214,
        region_3=3204351,
        region_4=3204352,
        region_5=3204353,
        region_6=3204354,
    )
    CommonFunc_20005119(
        0,
        character=3200220,
        region=3202220,
        region_1=3202221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005190(0, character=3200220, radius=20.0)
    CommonFunc_20005132(0, character=3200221, radius=14.0, region=3202221)
    CommonFunc_20005132(0, character=3200222, radius=14.0, region=3202221)
    CommonFunc_20005132(0, character=3200223, radius=18.0, region=3202225)
    CommonFunc_20005119(
        0,
        character=3200224,
        region=3202221,
        region_1=0,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005205(0, character=3200225, animation_id=701, animation_id_1=1701, region=3202222, seconds=0.0)
    CommonFunc_20005205(
        0,
        character=3200226,
        animation_id=701,
        animation_id_1=1701,
        region=3202222,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005111(0, character=3200227, animation_id=3003, region=3202224)
    CommonFunc_20005190(0, character=3200228, radius=12.0)
    CommonFunc_20005119(
        0,
        character=3200229,
        region=3202225,
        region_1=3202226,
        region_2=3202227,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200230,
        region=3202227,
        region_1=3202233,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200231,
        region=3202223,
        region_1=3202225,
        region_2=3202228,
        region_3=3202232,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005132(0, character=3200232, radius=10.0, region=3202232)
    CommonFunc_20005119(
        0,
        character=3200233,
        region=3202223,
        region_1=3202225,
        region_2=3202228,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200236,
        region=3202231,
        region_1=0,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200237,
        region=3202231,
        region_1=0,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005110(0, character=3200240, region=3202242)
    CommonFunc_20005110(0, character=3200241, region=3202242)
    CommonFunc_20005111(0, character=3200242, animation_id=3010, region=3202243)
    CommonFunc_20005140(0, character=3200243, region=3202244, character_1=3200244)
    CommonFunc_20005132(0, character=3200244, radius=4.0, region=3202244)
    CommonFunc_20005119(
        0,
        character=3200245,
        region=3202240,
        region_1=3202241,
        region_2=3202242,
        region_3=3202244,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200246,
        region=3202240,
        region_1=3202241,
        region_2=3202242,
        region_3=3202244,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3200254,
        region=3202251,
        region_1=3202252,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005341(0, flag=13200259, character=3200259, item_lot=21509000)
    CommonFunc_20005190(0, character=3200264, radius=15.0)
    CommonFunc_20005190(0, character=3200265, radius=20.0)
    CommonFunc_20005120(0, character=3200260, radius=18.0)
    CommonFunc_20005120(0, character=3200261, radius=18.0)
    CommonFunc_20005120(0, character=3200262, radius=18.0)
    CommonFunc_20005120(0, character=3200263, radius=18.0)
    CommonFunc_20005120(0, character=3200266, radius=18.0)
    CommonFunc_20005120(0, character=3200267, radius=18.0)
    Event_13205260(0, character=3200260, character_1=3200269, seconds=1.0)
    Event_13205260(1, character=3200261, character_1=3200269, seconds=50.0)
    Event_13205260(2, character=3200262, character_1=3200269, seconds=55.0)
    Event_13205260(3, character=3200263, character_1=3200269, seconds=16.0)
    Event_13205260(4, character=3200266, character_1=3200269, seconds=18.0)
    Event_13205260(5, character=3200267, character_1=3200269, seconds=22.0)
    Event_13205290()
    CommonFunc_20005119(
        0,
        character=3200235,
        region=3202230,
        region_1=3202234,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005132(0, character=3200255, radius=5.0, region=3202251)
    Event_13205350(0, character=3200235, flag=13204350, flag_1=13204360, flag_2=13204361)
    Event_13205350(1, character=3200255, flag=13204355, flag_1=13204365, flag_2=13204366)
    Event_13205360(
        0,
        flag=13204350,
        flag_1=13204360,
        flag_2=13204361,
        first_flag=13205500,
        last_flag=13205509,
        first_flag_1=13205500,
        last_flag_1=13205509,
    )
    Event_13205360(
        1,
        flag=13204355,
        flag_1=13204365,
        flag_2=13204366,
        first_flag=13205510,
        last_flag=13205519,
        first_flag_1=13205510,
        last_flag_1=13205519,
    )
    Event_13205370(
        0,
        character=3200290,
        flag=13204360,
        left=13204365,
        destination=3202291,
        destination_1=3202290,
        region=3202234,
        character_1=3200235,
        spawner=3204290,
    )
    Event_13205370(
        1,
        character=3200291,
        flag=13204361,
        left=0,
        destination=3202291,
        destination_1=3202290,
        region=3202234,
        character_1=3200235,
        spawner=3204291,
    )
    Event_13205375(
        0,
        character=3200295,
        flag=13204365,
        flag_1=13204360,
        destination=3202295,
        character_1=3200255,
        spawner=3204295,
    )
    Event_13205375(
        1,
        character=3200297,
        flag=13204366,
        flag_1=0,
        destination=3202295,
        character_1=3200255,
        spawner=3204297,
    )
    CommonFunc_20005120(0, character=3200299, radius=15.0)
    Event_13205380()
    Event_13205381()
    CommonFunc_20005350(0, character=3200291, item_lot=57400, flag=50006740)
    CommonFunc_20005350(0, character=3200297, item_lot=57500, flag=50006750)
    CommonFunc_20005342(0, flag=13200299, character=3200299)
    CommonFunc_20005111(0, character=3200500, animation_id=3002, region=3202500)
    CommonFunc_20005120(0, character=3200510, radius=3.0)
    CommonFunc_20005110(0, character=3200512, region=3202501)
    CommonFunc_20005114(0, character=3200513, region=3202501, seconds=1.0)
    Event_13205810()
    Event_13200811()
    Event_13205820()
    CommonFunc_20005840(0, other_entity=3201800)
    CommonFunc_20005841(0, other_entity=3201800)
    Event_13205860()
    Event_13205861()
    Event_13200862()
    Event_13200863()
    Event_13205864()
    Event_13205870()
    Event_13205880()
    CommonFunc_20005620(0, flag=13200400, flag_1=13205400, entity=3201400, obj=3201401, obj_1=3201402, flag_2=13201400)
    CommonFunc_20005628(0, flag=13200401, obj=3201402, region=3202401)
    Event_13205401()
    Event_13205410()
    Event_13205420()
    Event_13205430()
    Event_13205435()
    Event_13205440()
    Event_13205441()
    Event_13205442()
    Event_13205450()
    Event_13205470(0, event_id=1, sound_id=321000001)
    Event_13205470(1, event_id=2, sound_id=321000002)
    CommonFunc_20005523(0, obj=3201460, completion_count=1)
    CommonFunc_20005523(0, obj=3201461, completion_count=2)
    CommonFunc_20005520(0, flag=13201470, obj=3201470, obj_act_id=3204470)
    CommonFunc_20005520(0, flag=13201471, obj=3201471, obj_act_id=3204471)
    CommonFunc_20005525(0, flag=53200300, item_lot=3200300, obj=3201480, model_point=62)
    CommonFunc_20005525(0, flag=53200310, item_lot=3200310, obj=3201481, model_point=61)
    Event_13205910(0, flag=13200910, region=3202910, item_lot=3200900)
    Event_13205910(1, flag=13200915, region=3202915, item_lot=3200910)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13205100()
    DisableSoundEvent(sound_id=3204801)
    DisableSoundEvent(sound_id=3204851)
    DisableSoundEvent(sound_id=3204852)


@ContinueOnRest(13205100)
def Event_13205100():
    """Event 13205100"""
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(13205260)
def Event_13205260(_, character: int, character_1: int, seconds: float):
    """Event 13205260"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    
    MAIN.Await(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)


@RestartOnRest(13205290)
def Event_13205290():
    """Event 13205290"""
    EnableMapCollision(collision=3204280)
    
    MAIN.Await(CharacterHasTAEEvent(3205290, tae_event_id=10))
    
    DisableMapCollision(collision=3204280)
    Wait(2.0)
    Restart()


@RestartOnRest(13205300)
def Event_13205300():
    """Event 13205300"""
    GotoIfFlagEnabled(Label.L0, flag=13200300)
    SetBackreadStateAlternate(3200300, True)
    SetNetworkUpdateRate(3200300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3200300, authority_level=UpdateAuthority.Forced)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    
    MAIN.Await(CharacterDead(3200300))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13200300)
    End()


@RestartOnRest(13205310)
def Event_13205310():
    """Event 13205310"""
    GotoIfFlagDisabled(Label.L0, flag=13200300)
    DisableCharacter(3200300)
    Kill(3200300)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L9, flag=13205399)
    GotoIfFlagEnabled(Label.L1, flag=13205311)
    if FlagEnabled(13205312):
        return
    if FlagEnabled(13205321):
        return
    if FlagEnabled(13205331):
        return
    EnableCharacter(3200300)
    DisableAI(3200300)
    DisableGravity(3200300)
    Move(3200300, destination=3202310, destination_type=CoordEntityType.Region, copy_draw_parent=3200300)
    ForceAnimation(3200300, 30000, loop=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13205301, state=FlagSetting.On)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=3202300))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3202306))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3202399))
    OR_2.Add(OR_5)
    OR_2.Add(OR_4)
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_2.Add(Attacked(attacked_entity=3200300, attacker=PLAYER))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    AND_3.Add(FlagEnabled(13205301))
    AND_3.Add(FlagDisabled(13205398))
    AND_3.Add(OR_3)
    AND_3.Add(CharacterHasSpecialEffect(3200300, 5450))
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(13205399):
        return
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_5)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    Wait(1.0)
    ForceAnimation(3200300, 20004, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=3202300))
    GotoIfConditionTrue(Label.L1, input_condition=OR_6)
    Wait(3.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableGravity(3200300)
    EnableAI(3200300)
    SkipLinesIfFlagEnabled(8, 13205311)
    SetNetworkConnectedFlagState(flag=13205301, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagSetting.On)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    ForceAnimation(3200300, 20010, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    SkipLines(1)
    Move(3200300, destination=3202312, destination_type=CoordEntityType.Region, copy_draw_parent=3200300)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    if FlagDisabled(13205399):
        SetNetworkConnectedFlagState(flag=13205301, state=FlagSetting.Off)
        SetNetworkConnectedFlagState(flag=13205399, state=FlagSetting.On)
        ForceAnimation(3200300, 20013, skip_transition=True, unknown2=1.0)
        AND_4.Add(CharacterHasTAEEvent(3200300, tae_event_id=60))
        AND_4.Add(CharacterAlive(3200300))
        AND_4.Add(CharacterBackreadEnabled(3200300))
    
        MAIN.Await(AND_4)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest(13205320)
def Event_13205320():
    """Event 13205320"""
    if FlagEnabled(13200300):
        return
    GotoIfFlagEnabled(Label.L9, flag=13205399)
    GotoIfFlagEnabled(Label.L0, flag=13205321)
    AND_1.Add(CharacterInsideRegion(character=3200300, region=3202321))
    AND_1.Add(CharacterHasTAEEvent(3200300, tae_event_id=50))
    AND_1.Add(FlagDisabled(13205322))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3202304))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=3202399))
    OR_3.Add(OR_4)
    OR_3.Add(OR_5)
    AND_2.Add(OR_1)
    AND_2.Add(OR_3)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_6.Add(FlagEnabled(13205311))
    OR_6.Add(FlagEnabled(13205312))
    AND_3.Add(OR_2)
    AND_3.Add(OR_6)
    AND_3.Add(FlagDisabled(13205398))
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(13205399):
        return
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_5)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(3200300)
    DisableAI(3200300)
    SkipLinesIfFlagEnabled(9, 13205321)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=13205322, state=FlagSetting.On)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    ForceAnimation(3200300, 20011, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    SkipLines(1)
    ForceAnimation(3200300, 30001, loop=True, skip_transition=True, unknown2=1.0)
    Move(3200300, destination=3202311, destination_type=CoordEntityType.Region, copy_draw_parent=3200300)
    AND_4.Add(FlagDisabled(13205321))
    OR_7.Add(FlagEnabled(13205311))
    OR_7.Add(FlagEnabled(13205312))
    AND_4.Add(OR_7)
    
    MAIN.Await(AND_4)
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    if FlagDisabled(13205399):
        SetNetworkConnectedFlagState(flag=13205311, state=FlagSetting.Off)
        SetNetworkConnectedFlagState(flag=13205312, state=FlagSetting.Off)
        SetNetworkConnectedFlagState(flag=13205399, state=FlagSetting.On)
        Wait(1.0)
        DisableAI(3200300)
        RotateToFaceEntity(3200300, 3202350, animation=5002, wait_for_completion=True)
        ForceAnimation(3200300, 20014, skip_transition=True, unknown2=1.0)
        AND_5.Add(CharacterHasTAEEvent(3200300, tae_event_id=60))
        AND_5.Add(CharacterAlive(3200300))
        AND_5.Add(CharacterBackreadEnabled(3200300))
    
        MAIN.Await(AND_5)
    DisableAI(3200300)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest(13205330)
def Event_13205330():
    """Event 13205330"""
    if FlagEnabled(13200300):
        return
    GotoIfFlagEnabled(Label.L9, flag=13205399)
    GotoIfFlagEnabled(Label.L1, flag=13205331)
    GotoIfFlagEnabled(Label.L0, flag=13205312)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=3202302))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3202399))
    OR_3.Add(OR_4)
    AND_1.Add(OR_1)
    AND_1.Add(OR_3)
    AND_2.Add(Attacked(attacked_entity=3200300, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    AND_3.Add(FlagEnabled(13205321))
    AND_3.Add(FlagDisabled(13205398))
    AND_3.Add(OR_2)
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(13205399):
        return
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(3200300)
    EnableAI(3200300)
    SkipLinesIfFlagEnabled(8, 13205312)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13205312, state=FlagSetting.On)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    ForceAnimation(3200300, 20012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    SkipLines(1)
    Move(3200300, destination=3202313, destination_type=CoordEntityType.Region, copy_draw_parent=3200300)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(8, 13205331)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13205331, state=FlagSetting.On)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    ForceAnimation(3200300, 20016, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    SkipLines(1)
    ForceAnimation(3200300, 30000, loop=True, skip_transition=True, unknown2=1.0)
    Move(3200300, destination=3202310, destination_type=CoordEntityType.Region, copy_draw_parent=3200300)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    if FlagDisabled(13205399):
        SetNetworkConnectedFlagState(flag=13205321, state=FlagSetting.Off)
        SetNetworkConnectedFlagState(flag=13205399, state=FlagSetting.On)
        ForceAnimation(3200300, 20015, skip_transition=True, unknown2=1.0)
        AND_4.Add(CharacterHasTAEEvent(3200300, tae_event_id=60))
        AND_4.Add(CharacterAlive(3200300))
        AND_4.Add(CharacterBackreadEnabled(3200300))
    
        MAIN.Await(AND_4)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest(13205340)
def Event_13205340():
    """Event 13205340"""
    if FlagEnabled(13200300):
        return
    GotoIfFlagEnabled(Label.L9, flag=13205399)
    if FlagEnabled(13205311):
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3202303))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3202304))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=3202399))
    OR_2.Add(OR_4)
    OR_2.Add(OR_5)
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_2.Add(Attacked(attacked_entity=3200300, attacker=PLAYER))
    AND_2.Add(HealthRatio(3200300) <= 0.30000001192092896)
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    AND_3.Add(FlagEnabled(13205331))
    AND_3.Add(FlagDisabled(13205398))
    AND_3.Add(OR_3)
    AND_3.Add(CharacterHasSpecialEffect(3200300, 5450))
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(13205399):
        return
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    ForceAnimation(3200300, 20004, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=3202304))
    SkipLinesIfConditionTrue(1, OR_6)
    Wait(3.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(3200300)
    EnableAI(3200300)
    SkipLinesIfFlagEnabled(7, 13205311)
    SetNetworkConnectedFlagState(flag=13205331, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagSetting.On)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.On)
    ForceAnimation(3200300, 20010, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13205398, state=FlagSetting.Off)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    if FlagDisabled(13205399):
        SetNetworkConnectedFlagState(flag=13205331, state=FlagSetting.Off)
        SetNetworkConnectedFlagState(flag=13205399, state=FlagSetting.On)
        ForceAnimation(3200300, 20013, skip_transition=True, unknown2=1.0)
        AND_4.Add(CharacterHasTAEEvent(3200300, tae_event_id=60))
        AND_4.Add(CharacterAlive(3200300))
        AND_4.Add(CharacterBackreadEnabled(3200300))
    
        MAIN.Await(AND_4)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest(13205350)
def Event_13205350(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13205350"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    Restart()


@RestartOnRest(13205360)
def Event_13205360(
    _,
    flag: int,
    flag_1: int,
    flag_2: int,
    first_flag: int,
    last_flag: int,
    first_flag_1: uint,
    last_flag_1: uint,
):
    """Event 13205360"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlagRange((first_flag, last_flag))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=13200381)
    EnableRandomFlagInRange(flag_range=(first_flag_1, last_flag_1))
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L0, flag=first_flag)
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    Restart()


@RestartOnRest(13205370)
def Event_13205370(
    _,
    character: int,
    flag: int,
    left: int,
    destination: int,
    destination_1: int,
    region: int,
    character_1: int,
    spawner: int,
):
    """Event 13205370"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=left, right=0)
    GotoIfFlagDisabled(Label.L0, flag=left)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_9.Add(HealthRatio(character) != 0.0)
    SkipLinesIfConditionTrue(1, AND_9)
    ForceSpawnerToSpawn(spawner=spawner)
    Wait(1.100000023841858)
    AND_2.Add(AllPlayersOutsideRegion(region=region))
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    ForceAnimation(character, 63010, unknown2=1.0)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=destination, anchor_type=CoordEntityType.Region)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    AddSpecialEffect(character_1, 11292)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 63010, unknown2=1.0)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=destination_1, anchor_type=CoordEntityType.Region)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    AddSpecialEffect(character_1, 11292)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_1.Add(CharacterDead(character))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        Wait(3.0)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    RemoveSpecialEffect(character_1, 11292)
    Restart()


@RestartOnRest(13205375)
def Event_13205375(_, character: int, flag: int, flag_1: int, destination: int, character_1: int, spawner: int):
    """Event 13205375"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_9.Add(HealthRatio(character) != 0.0)
    SkipLinesIfConditionTrue(1, AND_9)
    ForceSpawnerToSpawn(spawner=spawner)
    Wait(1.100000023841858)
    ForceAnimation(character, 63010, unknown2=1.0)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=destination, anchor_type=CoordEntityType.Region)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    AddSpecialEffect(character_1, 11292)
    OR_1.Add(CharacterDead(character))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        Wait(3.0)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    RemoveSpecialEffect(character_1, 11292)
    Restart()


@RestartOnRest(13205380)
def Event_13205380():
    """Event 13205380"""
    if FlagEnabled(13200380):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(3200291) == 0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(9480)
    EnableFlag(13200380)


@RestartOnRest(13205381)
def Event_13205381():
    """Event 13205381"""
    if FlagEnabled(13200381):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(3200299) == 0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(9481)
    EnableFlag(13200381)


@ContinueOnRest(13205390)
def Event_13205390():
    """Event 13205390"""
    DisableObject(3201780)
    End()


@RestartOnRest(13205401)
def Event_13205401():
    """Event 13205401"""
    CommonFunc_20005621(
        0,
        flag=13200400,
        flag_1=13200405,
        obj=3201400,
        obj_1=3201401,
        obj_act_id=3204401,
        obj_2=3201402,
        obj_act_id_1=3204402,
        region=3202401,
        region_1=3202402,
        flag_2=13201400,
        flag_3=13204400,
        left=13200401,
    )


@RestartOnRest(13205410)
def Event_13205410():
    """Event 13205410"""
    GotoIfFlagEnabled(Label.L0, flag=13200410)
    EnableObjectActivation(3201411, obj_act_id=1324051)
    
    MAIN.Await(ObjectActivated(obj_act_id=3204411))
    
    DisableObjectActivation(3201411, obj_act_id=1324051)
    Wait(2.25)
    ForceAnimation(3201410, 1, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(3201410, 2, skip_transition=True, unknown2=1.0)
    ForceAnimation(3201411, 3, skip_transition=True, unknown2=1.0)
    EnableFlag(13200410)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=3201410, animation_id=2)
    DisableObjectActivation(3201411, obj_act_id=1324051)
    End()


@RestartOnRest(13205420)
def Event_13205420():
    """Event 13205420"""
    GotoIfFlagEnabled(Label.L0, flag=13200800)
    
    MAIN.Await(FlagEnabled(13200800))
    
    ForceAnimation(3201420, 2, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=3201420, animation_id=2)
    End()


@RestartOnRest(13205430)
def Event_13205430():
    """Event 13205430"""
    EndOfAnimation(obj=3201430, animation_id=2)


@RestartOnRest(13205435)
def Event_13205435():
    """Event 13205435"""
    GotoIfFlagEnabled(Label.L0, flag=13200850)
    
    MAIN.Await(FlagEnabled(13200850))
    
    ForceAnimation(3201435, 2, skip_transition=True, unknown2=1.0)
    ForceAnimation(3201436, 2, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=3201435, animation_id=2)
    EndOfAnimation(obj=3201436, animation_id=2)
    End()


@RestartOnRest(13205440)
def Event_13205440():
    """Event 13205440"""
    GotoIfFlagEnabled(Label.L2, flag=13200445)
    GotoIfFlagEnabled(Label.L1, flag=13200440)
    EnableObjectActivation(3201441, obj_act_id=324012)
    
    MAIN.Await(ObjectActivated(obj_act_id=3204441))
    
    EnableFlag(13200440)
    DisableObjectActivation(3201441, obj_act_id=324012)
    Wait(2.200000047683716)
    ForceAnimation(3201441, 3, skip_transition=True, unknown2=1.0)
    Wait(0.20999999344348907)
    EnableFlag(13200445)
    DisableObjectActivation(3201441, obj_act_id=324012)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13200445)
    DisableObjectActivation(3201441, obj_act_id=324012)
    EndOfAnimation(obj=3201441, animation_id=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableObjectActivation(3201441, obj_act_id=324012)
    EndOfAnimation(obj=3201441, animation_id=0)
    End()


@RestartOnRest(13205441)
def Event_13205441():
    """Event 13205441"""
    if FlagEnabled(13200850):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=13200445)
    DisableObject(3203850)
    DisableObject(3203851)
    DisableObject(3203852)
    DisableObject(3203853)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(13200445))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfTryingToCreateSession(2)
    PlayCutsceneAndSetMapCeremony(
        cutscene=32000000,
        cutscene_flags=CutsceneFlags.FadeOut,
        ceremony_id=10,
        unknown=1,
        player_id=10000,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutsceneAndSetMapCeremony(
        cutscene=32000000,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        ceremony_id=10,
        unknown=1,
        player_id=10000,
    )
    SkipLines(1)
    PlayCutsceneAndSetMapCeremony(
        cutscene=32000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        ceremony_id=10,
        unknown=1,
        player_id=10000,
    )
    WaitFrames(frames=1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    TriggerMultiplayerEvent(event_id=1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetMapCeremony(game_map=ARCHDRAGON_PEAK, ceremony_id=10)
    EnableFlag(13200446)
    EnableObject(3203850)
    EnableObject(3203851)
    EnableObject(3203852)
    EnableObject(3203853)
    End()


@RestartOnRest(13205442)
def Event_13205442():
    """Event 13205442"""
    GotoIfFlagEnabled(Label.L0, flag=13200862)
    
    MAIN.Await(FlagEnabled(13200856))
    
    WaitFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(3203850)
    DisableObject(3203851)
    DisableObject(3203852)
    DisableObject(3203853)
    End()


@ContinueOnRest(13205450)
def Event_13205450():
    """Event 13205450"""
    RegisterLadder(start_climbing_flag=13200450, stop_climbing_flag=13200451, obj=3201450)
    RegisterLadder(start_climbing_flag=13200452, stop_climbing_flag=13200453, obj=3201451)
    RegisterLadder(start_climbing_flag=13200454, stop_climbing_flag=13200455, obj=3201452)
    RegisterLadder(start_climbing_flag=13200456, stop_climbing_flag=13200457, obj=3201453)
    RegisterLadder(start_climbing_flag=13200458, stop_climbing_flag=13200459, obj=3201454)


@RestartOnRest(13205470)
def Event_13205470(_, event_id: uint, sound_id: int):
    """Event 13205470"""
    DisableNetworkSync()
    DisableFlag(13205479)
    AND_1.Add(MultiplayerEvent(event_id=event_id))
    AND_1.Add(FlagDisabled(13205479))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13205479)
    PlaySoundEffect(3201440, sound_id, sound_type=SoundType.a_Ambient)
    Wait(7.0)
    PlaySoundEffect(3201440, sound_id, sound_type=SoundType.a_Ambient)
    Wait(7.0)
    PlaySoundEffect(3201440, sound_id, sound_type=SoundType.a_Ambient)
    Wait(10.0)
    DisableFlag(13205479)
    Restart()


@RestartOnRest(13205490)
def Event_13205490(_, obj: int, model_point: int, flag: int):
    """Event 13205490"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    OR_1.Add(TryingToJoinSession())
    OR_1.Add(TryingToCreateSession())
    
    MAIN.Await(OR_1)
    
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObject(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(TryingToJoinSession())
    OR_2.Add(TryingToCreateSession())
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(13205810)
def Event_13205810():
    """Event 13205810"""
    GotoIfFlagDisabled(Label.L0, flag=13200800)
    DisableCharacter(3200800)
    DisableAnimations(3200800)
    Kill(3200800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(3200800)
    DisableAI(3200800)
    Move(3200800, destination=3202802, destination_type=CoordEntityType.Region, copy_draw_parent=3200800)
    AND_1.Add(FlagEnabled(13205805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3202801))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13200801)
    EnableCharacter(3200800)
    SetNetworkUpdateRate(3200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3200800)
    ForceAnimation(3200800, 20001, wait_for_completion=True, unknown2=1.0)
    EnableBossHealthBar(3200800, name=903140)
    EnableFlag(13205802)


@ContinueOnRest(13200811)
def Event_13200811():
    """Event 13200811"""
    if FlagEnabled(13200800):
        return
    
    MAIN.Await(HealthRatio(3200800) <= 0.0)
    
    Wait(0.5)
    PlaySoundEffect(3200800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3200800))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3200800)
    EnableFlag(13200800)
    EnableFlag(9305)
    EnableFlag(6305)
    if PlayerNotInOwnWorld():
        return
    Wait(5.0)
    PlayCutscene(32000030, cutscene_flags=0, player_id=10000, move_to_region=3202809, game_map=ARCHDRAGON_PEAK)
    SetRespawnPoint(respawn_point=3202953)
    SaveRequest()
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 63010, unknown2=1.0)
    PlaySoundEffect(PLAYER, 138008020, sound_type=SoundType.c_CharacterMotion)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)


@RestartOnRest(13205820)
def Event_13205820():
    """Event 13205820"""
    CommonFunc_20005800(
        0,
        flag=13200800,
        entity=3201800,
        region=3202800,
        flag_1=13205805,
        action_button_id=3201800,
        character=3200800,
        left=13200801,
        region_1=3202801,
    )
    CommonFunc_20005801(
        0,
        flag=13200800,
        entity=3201800,
        region=3202800,
        flag_1=13205805,
        action_button_id=3201800,
        flag_2=13205806,
    )
    CommonFunc_20005820(0, flag=13200800, obj=3201800, model_point=3, left=13200801)
    CommonFunc_20005820(0, flag=13200800, obj=3201801, model_point=2, left=13200801)
    CommonFunc_20001835(0, flag=13200800, flag_1=13205805, flag_2=13205806, flag_3=13205802, sound_id=3204801)
    CommonFunc_20005810(0, flag=13200800, entity=3201800, target_entity=3202800, action_button_id=10000)


@RestartOnRest(13205860)
def Event_13205860():
    """Event 13205860"""
    GotoIfFlagEnabled(Label.L1, flag=13200445)
    GotoIfFlagDisabled(Label.L0, flag=13200850)
    Kill(3205850)
    DisableCharacter(3205850)
    DisableAnimations(3205850)
    SetNetworkUpdateRate(3205850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(3205850)
    DisableAnimations(3205850)
    
    MAIN.Await(FlagEnabled(13200445))

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3200850)
    DisableCharacter(3200851)
    EnableAnimations(3200850)
    DisableAnimations(3200851)
    DisableAI(3205850)
    EnableImmortality(3200850)
    ForceAnimation(3200850, 700, unknown2=1.0)
    AND_1.Add(FlagEnabled(13205855))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3202850))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(3200850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3200850, 1700, wait_for_completion=True, unknown2=1.0)
    EnableAI(3200850)
    EnableBossHealthBar(3200850, name=905030)
    EnableFlag(13205851)


@RestartOnRest(13205861)
def Event_13205861():
    """Event 13205861"""
    if FlagEnabled(13200850):
        return
    AND_1.Add(HealthRatio(3200850) <= 0.009999999776482582)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterHasSpecialEffect(3200850, 12160))
    SkipLinesIfConditionTrue(1, OR_1)
    ForceAnimation(3200850, 20001, wait_for_completion=True, unknown2=1.0)
    DisableBossMusic(sound_id=-1)
    WaitFrames(frames=1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        32000010,
        cutscene_flags=CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3202858,
        game_map=ARCHDRAGON_PEAK,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        32000010,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3202858,
        game_map=ARCHDRAGON_PEAK,
    )
    SkipLines(1)
    PlayCutscene(32000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Kill(3200850)
    DisableCharacter(3200850)
    DisableAnimations(3200850)
    DisableAI(3200850)
    SetNetworkUpdateRate(3200850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    DisableBossHealthBar(3200850, name=905030)
    EnableCharacter(3200851)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3200851, authority_level=UpdateAuthority.Forced)
    EnableAnimations(3200851)
    EnableAI(3200851)
    SetNetworkUpdateRate(3200851, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3200851, name=905010)
    EnableFlag(13205852)


@ContinueOnRest(13200862)
def Event_13200862():
    """Event 13200862"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L2, flag=13200856)
    GotoIfFlagEnabled(Label.L1, flag=13200855)
    GotoIfFlagEnabled(Label.L0, flag=13200850)
    AND_1.Add(CharacterDead(3200851))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(2.200000047683716)
    KillBoss(game_area_param_id=3200851)
    EnableFlag(13200850)
    EnableFlag(9304)
    EnableFlag(6304)
    Wait(5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13200855)
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13200856)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        cutscene=32000020,
        cutscene_flags=CutsceneFlags.FadeOut,
        ceremony_id=0,
        unknown=0,
        move_to_region=3202859,
        game_map=ARCHDRAGON_PEAK,
        player_id=10000,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        cutscene=32000020,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        ceremony_id=0,
        unknown=0,
        move_to_region=3202859,
        game_map=ARCHDRAGON_PEAK,
        player_id=10000,
    )
    SkipLines(1)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        cutscene=32000020,
        cutscene_flags=CutsceneFlags.Unskippable,
        ceremony_id=0,
        unknown=0,
        move_to_region=3202857,
        game_map=ARCHDRAGON_PEAK,
        player_id=10000,
    )
    WaitFrames(frames=1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    TriggerMultiplayerEvent(event_id=2)


@ContinueOnRest(13200863)
def Event_13200863():
    """Event 13200863"""
    if FlagEnabled(13200850):
        return
    
    MAIN.Await(HealthRatio(3200851) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(3200851, 777777777, sound_type=SoundType.s_SFX)


@RestartOnRest(13205864)
def Event_13205864():
    """Event 13205864"""
    DisableNetworkSync()
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    if FlagEnabled(13200850):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    
    MAIN.Await(FlagEnabled(13205855))
    
    SkipLines(1)
    
    MAIN.Await(FlagEnabled(13205856))
    
    GotoIfFlagEnabled(Label.L0, flag=13205852)
    ChangeCamera(normal_camera_id=5030, locked_camera_id=5030)
    
    MAIN.Await(FlagEnabled(13205852))

    # --- Label 0 --- #
    DefineLabel(0)
    ChangeCamera(normal_camera_id=5270, locked_camera_id=5270)
    
    MAIN.Await(FlagEnabled(13200850))
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(13205870)
def Event_13205870():
    """Event 13205870"""
    CommonFunc_20005800(
        0,
        flag=13200850,
        entity=3201850,
        region=3202850,
        flag_1=13205855,
        action_button_id=3201850,
        character=3205850,
        left=0,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=13200850,
        entity=3201850,
        region=3202850,
        flag_1=13205855,
        action_button_id=3201850,
        flag_2=13205856,
    )
    CommonFunc_20005820(0, flag=13200855, obj=3201850, model_point=832040, left=13200446)
    CommonFunc_20001836(
        0,
        flag=13200850,
        flag_1=13205855,
        flag_2=13205856,
        flag_3=13205851,
        sound_id=3204851,
        sound_id_1=3204852,
        flag_4=13205852,
    )
    CommonFunc_20005810(0, flag=13200850, entity=3201785, target_entity=3202785, action_button_id=10000)
    CommonFunc_20005810(0, flag=13200850, entity=3201786, target_entity=3202786, action_button_id=10000)


@RestartOnRest(13205880)
def Event_13205880():
    """Event 13205880"""
    if FlagEnabled(13200850):
        return
    CreateNPCPart(3200850, npc_part_id=1, part_index=NPCPartType.Part1, part_health=350)
    
    MAIN.Await(CharacterPartHealth(3200850, npc_part_id=1) <= 0)
    
    ForceAnimation(3200850, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Restart()


@RestartOnRest(13205910)
def Event_13205910(_, flag: int, region: int, item_lot: int):
    """Event 13205910"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4400))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(TimeElapsed(seconds=4.0))
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4400))
    
    MAIN.Await(OR_1)
    
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4400):
        return RESTART
    AwardItemLot(item_lot, host_only=False)
    EnableFlag(flag)
    End()


@RestartOnRest(13205930)
def Event_13205930():
    """Event 13205930"""
    if FlagEnabled(13200850):
        return
    if FlagEnabled(13200930):
        return
    if FlagEnabled(13200445):
        return
    AND_1.Add(FlagEnabled(13204190))
    AND_1.Add(CharacterInsideRegion(character=3200190, region=3202930))
    AND_2.Add(FlagEnabled(13200445))
    AND_2.Add(FlagEnabled(13204190))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L1, flag=13200445)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableInvincibility(3200190)
    RotateToFaceEntity(3200190, 3202932, animation=60060, wait_for_completion=True)
    ForceAnimation(3200190, 91050, wait_for_completion=True, unknown2=1.0)
    Wait(5.0)
    ForceAnimation(3200190, 91052, unknown2=1.0)
    Wait(1.0)
    SendNPCSummonHome(character=3200190)
    EnableFlag(13200930)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(3200190, 91030, unknown2=1.0)
    Wait(2.0)
    SendNPCSummonHome(character=3200190)


@RestartOnRest(13205931)
def Event_13205931():
    """Event 13205931"""
    OR_1.Add(FlagEnabled(13200445))
    OR_1.Add(FlagEnabled(13200930))
    
    MAIN.Await(OR_1)
    
    EnableFlag(13200931)
