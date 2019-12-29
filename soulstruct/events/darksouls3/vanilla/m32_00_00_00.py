"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.events
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.events.darksouls3 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(13200000, obj=3201950, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13200002, obj=3201952, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13200003, obj=3201953, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunCommonEvent(20005500, args=(13200850, 13200001, 3200951, 3201951))
    RunEvent(13205390)
    RunCommonEvent(20005780, args=(3201781, 2))
    RunCommonEvent(20005780, args=(3201782, 2))
    RunCommonEvent(20005780, args=(3201783, 2))
    RunCommonEvent(20005780, args=(3201784, 2))
    RunEvent(13205490, slot=0, args=(3201785, 2, 13200850))
    RunEvent(13205490, slot=1, args=(3201786, 2, 13200850))
    RunCommonEvent(20005701, args=(13200931, 13204190, 13205190, 3200190, 3202190, 70000007))
    RunCommonEvent(20005720, args=(13204190, 13205190, 13200445, 3200190))
    RunEvent(13205930)
    RunEvent(13205931)
    RunEvent(13205300)
    RunEvent(13205310)
    RunEvent(13205320)
    RunEvent(13205330)
    RunEvent(13205340)
    RunCommonEvent(20005341, args=(13200305, 3200300, 31412000))
    RunCommonEvent(20005119, args=(3200200, 3202200, 3202201, 3202202, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200201, 3202201, 3202202, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200202, 3202201, 3202203, 0, 0, 0, 0, 0))
    RunCommonEvent(20005130, args=(3200203, 1097859072, 3202203))
    RunCommonEvent(20005119, args=(3200204, 3202201, 3202203, 0, 0, 0, 0, 0))
    RunCommonEvent(20005120, args=(3200205, 1097859072))
    RunCommonEvent(20005213, args=(3200210, 700, 1700, 1075838976, 3202210))
    RunCommonEvent(20005132, args=(3200211, 1082130432, 3202210))
    RunCommonEvent(20005119, args=(3200212, 3202212, 3202213, 3202214, 3204351, 3204352, 3204353, 3204354))
    RunCommonEvent(20005119, args=(3200220, 3202220, 3202221, 0, 0, 0, 0, 0))
    RunCommonEvent(20005190, args=(3200220, 1101004800))
    RunCommonEvent(20005132, args=(3200221, 1096810496, 3202221))
    RunCommonEvent(20005132, args=(3200222, 1096810496, 3202221))
    RunCommonEvent(20005132, args=(3200223, 1099956224, 3202225))
    RunCommonEvent(20005119, args=(3200224, 3202221, 0, 0, 0, 0, 0, 0))
    RunCommonEvent(20005205, args=(3200225, 701, 1701, 3202222, 0))
    RunCommonEvent(20005205, args=(3200226, 701, 1701, 3202222, 1067030938))
    RunCommonEvent(20005111, args=(3200227, 3003, 3202224))
    RunCommonEvent(20005190, args=(3200228, 1094713344))
    RunCommonEvent(20005119, args=(3200229, 3202225, 3202226, 3202227, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200230, 3202227, 3202233, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200231, 3202223, 3202225, 3202228, 3202232, 0, 0, 0))
    RunCommonEvent(20005132, args=(3200232, 1092616192, 3202232))
    RunCommonEvent(20005119, args=(3200233, 3202223, 3202225, 3202228, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200236, 3202231, 0, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200237, 3202231, 0, 0, 0, 0, 0, 0))
    RunCommonEvent(20005110, args=(3200240, 3202242))
    RunCommonEvent(20005110, args=(3200241, 3202242))
    RunCommonEvent(20005111, args=(3200242, 3010, 3202243))
    RunCommonEvent(20005140, args=(3200243, 3202244, 3200244))
    RunCommonEvent(20005132, args=(3200244, 1082130432, 3202244))
    RunCommonEvent(20005119, args=(3200245, 3202240, 3202241, 3202242, 3202244, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200246, 3202240, 3202241, 3202242, 3202244, 0, 0, 0))
    RunCommonEvent(20005119, args=(3200254, 3202251, 3202252, 0, 0, 0, 0, 0))
    RunCommonEvent(20005341, args=(13200259, 3200259, 21509000))
    RunCommonEvent(20005190, args=(3200264, 1097859072))
    RunCommonEvent(20005190, args=(3200265, 1101004800))
    RunCommonEvent(20005120, args=(3200260, 1099956224))
    RunCommonEvent(20005120, args=(3200261, 1099956224))
    RunCommonEvent(20005120, args=(3200262, 1099956224))
    RunCommonEvent(20005120, args=(3200263, 1099956224))
    RunCommonEvent(20005120, args=(3200266, 1099956224))
    RunCommonEvent(20005120, args=(3200267, 1099956224))
    RunEvent(13205260, slot=0, args=(3200260, 3200269, 1.0), arg_types='iif')
    RunEvent(13205260, slot=1, args=(3200261, 3200269, 50.0), arg_types='iif')
    RunEvent(13205260, slot=2, args=(3200262, 3200269, 55.0), arg_types='iif')
    RunEvent(13205260, slot=3, args=(3200263, 3200269, 16.0), arg_types='iif')
    RunEvent(13205260, slot=4, args=(3200266, 3200269, 18.0), arg_types='iif')
    RunEvent(13205260, slot=5, args=(3200267, 3200269, 22.0), arg_types='iif')
    RunEvent(13205290)
    RunCommonEvent(20005119, args=(3200235, 3202230, 3202234, 0, 0, 0, 0, 0))
    RunCommonEvent(20005132, args=(3200255, 1084227584, 3202251))
    RunEvent(13205350, slot=0, args=(3200235, 13204350, 13204360, 13204361))
    RunEvent(13205350, slot=1, args=(3200255, 13204355, 13204365, 13204366))
    RunEvent(13205360, slot=0, args=(13204350, 13204360, 13204361, 13205500, 13205509, 13205500, 13205509), arg_types='iiiiiII')
    RunEvent(13205360, slot=1, args=(13204355, 13204365, 13204366, 13205510, 13205519, 13205510, 13205519), arg_types='iiiiiII')
    RunEvent(13205370, slot=0, args=(3200290, 13204360, 13204365, 3202291, 3202290, 3202234, 3200235, 3204290))
    RunEvent(13205370, slot=1, args=(3200291, 13204361, 0, 3202291, 3202290, 3202234, 3200235, 3204291))
    RunEvent(13205375, slot=0, args=(3200295, 13204365, 13204360, 3202295, 3200255, 3204295))
    RunEvent(13205375, slot=1, args=(3200297, 13204366, 0, 3202295, 3200255, 3204297))
    RunCommonEvent(20005120, args=(3200299, 1097859072))
    RunEvent(13205380)
    RunEvent(13205381)
    RunCommonEvent(20005350, args=(3200291, 57400, 50006740))
    RunCommonEvent(20005350, args=(3200297, 57500, 50006750))
    RunCommonEvent(20005342, args=(13200299, 3200299))
    RunCommonEvent(20005111, args=(3200500, 3002, 3202500))
    RunCommonEvent(20005120, args=(3200510, 1077936128))
    RunCommonEvent(20005110, args=(3200512, 3202501))
    RunCommonEvent(20005114, args=(3200513, 3202501, 1065353216))
    RunEvent(13205810)
    RunEvent(13200811)
    RunEvent(13205820)
    RunCommonEvent(20005840, args=(3201800,))
    RunCommonEvent(20005841, args=(3201800,))
    RunEvent(13205860)
    RunEvent(13205861)
    RunEvent(13200862)
    RunEvent(13200863)
    RunEvent(13205864)
    RunEvent(13205870)
    RunEvent(13205880)
    RunCommonEvent(20005620, args=(13200400, 13205400, 3201400, 3201401, 3201402, 13201400))
    RunCommonEvent(20005628, args=(13200401, 3201402, 3202401))
    RunEvent(13205401)
    RunEvent(13205410)
    RunEvent(13205420)
    RunEvent(13205430)
    RunEvent(13205435)
    RunEvent(13205440)
    RunEvent(13205441)
    RunEvent(13205442)
    RunEvent(13205450)
    RunEvent(13205470, slot=0, args=(1, 321000001), arg_types='Ii')
    RunEvent(13205470, slot=1, args=(2, 321000002), arg_types='Ii')
    RunCommonEvent(20005523, args=(3201460, 1))
    RunCommonEvent(20005523, args=(3201461, 2))
    RunCommonEvent(20005520, args=(13201470, 3201470, 3204470))
    RunCommonEvent(20005520, args=(13201471, 3201471, 3204471))
    RunCommonEvent(20005525, args=(53200300, 3200300, 3201480, 62))
    RunCommonEvent(20005525, args=(53200310, 3200310, 3201481, 61))
    RunEvent(13205910, slot=0, args=(13200910, 3202910, 3200900))
    RunEvent(13205910, slot=1, args=(13200915, 3202915, 3200910))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13205100)
    DisableMapSound(3204801)
    DisableMapSound(3204851)
    DisableMapSound(3204852)


@NeverRestart
def Event13205100():
    """ 13205100: Event 13205100 """
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest
def Event13205260(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float):
    """ 13205260: Event 13205260 """
    GotoIfThisEventSlotOn(Label.L0)
    DisableAI(ARG_0_3)
    IfHasAIStatus(0, character=ARG_4_7, ai_status=AIStatusType.Battle)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    Wait(ARG_8_11)
    Label(0)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event13205290():
    """ 13205290: Event 13205290 """
    EnableCollision(3204280)
    IfHasTAEEvent(0, character=3205290, tae_event_id=10)
    DisableCollision(3204280)
    Wait(2.0)
    Restart()


@RestartOnRest
def Event13205300():
    """ 13205300: Event 13205300 """
    GotoIfFlagOn(Label.L0, 13200300)
    SetBackreadStateAlternate(3200300, state=True)
    SetNetworkUpdateRate(3200300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkUpdateAuthority(3200300, UpdateAuthority.Forced)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    IfCharacterDead(0, 3200300)
    Label(0)
    EnableFlag(13200300)
    End()


@RestartOnRest
def Event13205310():
    """ 13205310: Event 13205310 """
    GotoIfFlagOff(Label.L0, 13200300)
    DisableCharacter(3200300)
    Kill(3200300, award_souls=False)
    End()
    Label(0)
    GotoIfFlagOn(Label.L9, 13205399)
    GotoIfFlagOn(Label.L1, 13205311)
    EndIfFlagOn(13205312)
    EndIfFlagOn(13205321)
    EndIfFlagOn(13205331)
    EnableCharacter(3200300)
    DisableAI(3200300)
    DisableGravity(3200300)
    Move(3200300, destination=3202310, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=3200300)
    ForceAnimation(entity=3200300, animation_id=30000, loop=True, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13205301, state=FlagState.On)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Human)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.WhitePhantom)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Hollow)
    IfCharacterInsideRegion(-5, PLAYER, region=3202300)
    IfCharacterInsideRegion(-2, PLAYER, region=3202306)
    IfCharacterInsideRegion(-4, PLAYER, region=3202399)
    IfConditionTrue(-2, input_condition=-5)
    IfConditionTrue(-2, input_condition=-4)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfAttacked(2, 3200300, attacking_character=10000)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfFlagOn(3, 13205301)
    IfFlagOff(3, 13205398)
    IfConditionTrue(3, input_condition=-3)
    IfCharacterHasSpecialEffect(3, character=3200300, special_effect=5450)
    IfConditionTrue(0, input_condition=3)
    EndIfFlagOn(13205399)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=-5)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    SkipLinesIfFinishedConditionTrue(1, 2)
    Wait(1.0)
    ForceAnimation(entity=3200300, animation_id=20004, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    IfCharacterInsideRegion(-6, PLAYER, region=3202300)
    GotoIfConditionTrue(Label.L1, input_condition=-6)
    Wait(3.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    Restart()
    Label(1)
    EnableGravity(3200300)
    EnableAI(3200300)
    SkipLinesIfFlagOn(8, 13205311)
    SetNetworkConnectedFlagState(flag=13205301, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagState.On)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20010, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    SkipLines(1)
    Move(3200300, destination=3202312, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=3200300)
    End()
    Label(9)
    SkipLinesIfFlagOn(7, 13205399)
    SetNetworkConnectedFlagState(flag=13205301, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205399, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20013, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    IfHasTAEEvent(4, character=3200300, tae_event_id=60)
    IfCharacterAlive(4, 3200300)
    IfCharacterBackreadEnabled(4, character=3200300)
    IfConditionTrue(0, input_condition=4)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest
def Event13205320():
    """ 13205320: Event 13205320 """
    EndIfFlagOn(13200300)
    GotoIfFlagOn(Label.L9, 13205399)
    GotoIfFlagOn(Label.L0, 13205321)
    IfCharacterInsideRegion(1, 3200300, region=3202321)
    IfHasTAEEvent(1, character=3200300, tae_event_id=50)
    IfFlagOff(1, 13205322)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Human)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.WhitePhantom)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Hollow)
    IfCharacterInsideRegion(-4, PLAYER, region=3202304)
    IfCharacterInsideRegion(-5, PLAYER, region=3202399)
    IfConditionTrue(-3, input_condition=-4)
    IfConditionTrue(-3, input_condition=-5)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-6, 13205311)
    IfFlagOn(-6, 13205312)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(3, input_condition=-6)
    IfFlagOff(3, 13205398)
    IfConditionTrue(0, input_condition=3)
    EndIfFlagOn(13205399)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=-5)
    Label(0)
    DisableGravity(3200300)
    DisableAI(3200300)
    SkipLinesIfFlagOn(9, 13205321)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagState.On)
    SetNetworkConnectedFlagState(flag=13205322, state=FlagState.On)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20011, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    SkipLines(1)
    ForceAnimation(entity=3200300, animation_id=30001, loop=True, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    Move(3200300, destination=3202311, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=3200300)
    IfFlagOff(4, 13205321)
    IfFlagOn(-7, 13205311)
    IfFlagOn(-7, 13205312)
    IfConditionTrue(4, input_condition=-7)
    IfConditionTrue(0, input_condition=4)
    Restart()
    Label(9)
    SkipLinesIfFlagOn(11, 13205399)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205312, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205399, state=FlagState.On)
    Wait(1.0)
    DisableAI(3200300)
    RotateToFaceEntity(3200300, 3202350, animation=5002, wait_for_completion=True)
    ForceAnimation(entity=3200300, animation_id=20014, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    IfHasTAEEvent(5, character=3200300, tae_event_id=60)
    IfCharacterAlive(5, 3200300)
    IfCharacterBackreadEnabled(5, character=3200300)
    IfConditionTrue(0, input_condition=5)
    DisableAI(3200300)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest
def Event13205330():
    """ 13205330: Event 13205330 """
    EndIfFlagOn(13200300)
    GotoIfFlagOn(Label.L9, 13205399)
    GotoIfFlagOn(Label.L1, 13205331)
    GotoIfFlagOn(Label.L0, 13205312)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Human)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.WhitePhantom)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Hollow)
    IfCharacterInsideRegion(-3, PLAYER, region=3202302)
    IfCharacterInsideRegion(-4, PLAYER, region=3202399)
    IfConditionTrue(-3, input_condition=-4)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-3)
    IfAttacked(2, 3200300, attacking_character=10000)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(3, 13205321)
    IfFlagOff(3, 13205398)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(0, input_condition=3)
    EndIfFlagOn(13205399)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    Label(0)
    EnableGravity(3200300)
    EnableAI(3200300)
    SkipLinesIfFlagOn(8, 13205312)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205312, state=FlagState.On)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20012, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    SkipLines(1)
    Move(3200300, destination=3202313, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=3200300)
    End()
    Label(1)
    SkipLinesIfFlagOn(8, 13205331)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205331, state=FlagState.On)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20016, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    SkipLines(1)
    ForceAnimation(entity=3200300, animation_id=30000, loop=True, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    Move(3200300, destination=3202310, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=3200300)
    End()
    Label(9)
    SkipLinesIfFlagOn(7, 13205399)
    SetNetworkConnectedFlagState(flag=13205321, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205399, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20015, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    IfHasTAEEvent(4, character=3200300, tae_event_id=60)
    IfCharacterAlive(4, 3200300)
    IfCharacterBackreadEnabled(4, character=3200300)
    IfConditionTrue(0, input_condition=4)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest
def Event13205340():
    """ 13205340: Event 13205340 """
    EndIfFlagOn(13200300)
    GotoIfFlagOn(Label.L9, 13205399)
    EndIfFlagOn(13205311)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Human)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.WhitePhantom)
    IfCharacterType(-1, character=PLAYER, character_type=CharacterType.Hollow)
    IfCharacterInsideRegion(-2, PLAYER, region=3202303)
    IfCharacterInsideRegion(-4, PLAYER, region=3202304)
    IfCharacterInsideRegion(-5, PLAYER, region=3202399)
    IfConditionTrue(-2, input_condition=-4)
    IfConditionTrue(-2, input_condition=-5)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfAttacked(2, 3200300, attacking_character=10000)
    IfHealthComparison(2, character=3200300, comparison_type=ComparisonType.LessThanOrEqual, value=0.30000001192092896)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfFlagOn(3, 13205331)
    IfFlagOff(3, 13205398)
    IfConditionTrue(3, input_condition=-3)
    IfCharacterHasSpecialEffect(3, character=3200300, special_effect=5450)
    IfConditionTrue(0, input_condition=3)
    EndIfFlagOn(13205399)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=-5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20004, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    IfCharacterInsideRegion(-6, PLAYER, region=3202304)
    SkipLinesIfConditionTrue(1, -6)
    Wait(3.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    Restart()
    Label(0)
    EnableGravity(3200300)
    EnableAI(3200300)
    SkipLinesIfFlagOn(7, 13205311)
    SetNetworkConnectedFlagState(flag=13205331, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205311, state=FlagState.On)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20010, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=13205398, state=FlagState.Off)
    End()
    Label(9)
    SkipLinesIfFlagOn(7, 13205399)
    SetNetworkConnectedFlagState(flag=13205331, state=FlagState.Off)
    SetNetworkConnectedFlagState(flag=13205399, state=FlagState.On)
    ForceAnimation(entity=3200300, animation_id=20013, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    IfHasTAEEvent(4, character=3200300, tae_event_id=60)
    IfCharacterAlive(4, 3200300)
    IfCharacterBackreadEnabled(4, character=3200300)
    IfConditionTrue(0, input_condition=4)
    DisableCharacter(3200300)
    DisableAnimations(3200300)
    End()


@RestartOnRest
def Event13205350(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 13205350: Event 13205350 """
    GotoIfFlagOn(Label.L0, ARG_4_7)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    IfHasTAEEvent(1, character=ARG_0_3, tae_event_id=10)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.On)
    IfFlagOn(-1, ARG_8_11)
    IfFlagOn(-1, ARG_12_15)
    IfConditionTrue(0, input_condition=-1)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    Restart()


@RestartOnRest
def Event13205360(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: uint, ARG_24_27: uint):
    """ 13205360: Event 13205360 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    DisableFlagRange((ARG_12_15, ARG_16_19))
    IfPlayerInOwnWorld(1)
    IfFlagOn(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagOn(Label.L0, 13200381)
    EnableRandomFlagInRange((ARG_20_23, ARG_24_27))
    WaitFrames(1)
    GotoIfFlagOff(Label.L0, ARG_12_15)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.On)
    Restart()
    Label(0)
    SetNetworkConnectedFlagState(flag=ARG_8_11, state=FlagState.On)
    Restart()


@RestartOnRest
def Event13205370(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 13205370: Event 13205370 """
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    IfPlayerInOwnWorld(1)
    IfFlagOn(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.On)
    GotoIfValueComparison(Label.L0, ComparisonType.Equal, left=ARG_8_11, right=0)
    GotoIfFlagOff(Label.L0, ARG_8_11)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    Restart()
    Label(0)
    IfHealthComparison(9, character=ARG_0_3, comparison_type=ComparisonType.NotEqual, value=0.0)
    SkipLinesIfConditionTrue(1, 9)
    MakeEnemyAppear(ARG_28_31)
    Wait(1.100000023841858)
    IfAllPlayersOutsideRegion(2, region=ARG_20_23)
    GotoIfConditionTrue(Label.L1, input_condition=2)
    ForceAnimation(entity=ARG_0_3, animation_id=63010, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    CreateTemporaryFX(30300, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Region, model_point=-1)
    Move(ARG_0_3, destination=ARG_12_15, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=ARG_24_27)
    AddSpecialEffect(ARG_24_27, 11292)
    Goto(Label.L2)
    Label(1)
    ForceAnimation(entity=ARG_0_3, animation_id=63010, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    CreateTemporaryFX(30300, anchor_entity=ARG_16_19, anchor_type=CoordEntityType.Region, model_point=-1)
    Move(ARG_0_3, destination=ARG_16_19, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=ARG_24_27)
    AddSpecialEffect(ARG_24_27, 11292)
    Label(2)
    IfCharacterDead(-1, ARG_0_3)
    IfFlagOff(-1, ARG_4_7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, ARG_4_7)
    Wait(3.0)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    CancelSpecialEffect(ARG_24_27, 11292)
    Restart()


@RestartOnRest
def Event13205375(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 13205375: Event 13205375 """
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    IfPlayerInOwnWorld(1)
    IfFlagOn(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.On)
    GotoIfFlagOff(Label.L0, ARG_8_11)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    Restart()
    Label(0)
    IfHealthComparison(9, character=ARG_0_3, comparison_type=ComparisonType.NotEqual, value=0.0)
    SkipLinesIfConditionTrue(1, 9)
    MakeEnemyAppear(ARG_20_23)
    Wait(1.100000023841858)
    ForceAnimation(entity=ARG_0_3, animation_id=63010, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    CreateTemporaryFX(30300, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Region, model_point=-1)
    Move(ARG_0_3, destination=ARG_12_15, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=ARG_16_19)
    AddSpecialEffect(ARG_16_19, 11292)
    IfCharacterDead(-1, ARG_0_3)
    IfFlagOff(-1, ARG_4_7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, ARG_4_7)
    Wait(3.0)
    SetNetworkConnectedFlagState(flag=ARG_4_7, state=FlagState.Off)
    CancelSpecialEffect(ARG_16_19, 11292)
    Restart()


@RestartOnRest
def Event13205380():
    """ 13205380: Event 13205380 """
    EndIfFlagOn(13200380)
    IfPlayerInOwnWorld(1)
    IfHealthValueEqual(1, character=3200291, value=0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9480)
    EnableFlag(13200380)


@RestartOnRest
def Event13205381():
    """ 13205381: Event 13205381 """
    EndIfFlagOn(13200381)
    IfPlayerInOwnWorld(1)
    IfHealthValueEqual(1, character=3200299, value=0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9481)
    EnableFlag(13200381)


@NeverRestart
def Event13205390():
    """ 13205390: Event 13205390 """
    DisableObject(3201780)
    End()


@RestartOnRest
def Event13205401():
    """ 13205401: Event 13205401 """
    RunCommonEvent(20005621, args=(13200400, 13200405, 3201400, 3201401, 3204401, 3201402, 3204402, 3202401, 3202402, 13201400, 13204400, 13200401))


@RestartOnRest
def Event13205410():
    """ 13205410: Event 13205410 """
    GotoIfFlagOn(Label.L0, 13200410)
    EnableObjectActivation(3201411, obj_act_id=1324051)
    IfObjectActivated(0, obj_act_id=3204411)
    DisableObjectActivation(3201411, obj_act_id=1324051)
    Wait(2.25)
    ForceAnimation(entity=3201410, animation_id=1, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    ForceAnimation(entity=3201410, animation_id=2, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    ForceAnimation(entity=3201411, animation_id=3, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    EnableFlag(13200410)
    End()
    Label(0)
    EndOfAnimation(3201410, 2)
    DisableObjectActivation(3201411, obj_act_id=1324051)
    End()


@RestartOnRest
def Event13205420():
    """ 13205420: Event 13205420 """
    GotoIfFlagOn(Label.L0, 13200800)
    IfFlagOn(0, 13200800)
    ForceAnimation(entity=3201420, animation_id=2, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    End()
    Label(0)
    EndOfAnimation(3201420, 2)
    End()


@RestartOnRest
def Event13205430():
    """ 13205430: Event 13205430 """
    EndOfAnimation(3201430, 2)


@RestartOnRest
def Event13205435():
    """ 13205435: Event 13205435 """
    GotoIfFlagOn(Label.L0, 13200850)
    IfFlagOn(0, 13200850)
    ForceAnimation(entity=3201435, animation_id=2, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    ForceAnimation(entity=3201436, animation_id=2, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    End()
    Label(0)
    EndOfAnimation(3201435, 2)
    EndOfAnimation(3201436, 2)
    End()


@RestartOnRest
def Event13205440():
    """ 13205440: Event 13205440 """
    GotoIfFlagOn(Label.L2, 13200445)
    GotoIfFlagOn(Label.L1, 13200440)
    EnableObjectActivation(3201441, obj_act_id=324012)
    IfObjectActivated(0, obj_act_id=3204441)
    EnableFlag(13200440)
    DisableObjectActivation(3201441, obj_act_id=324012)
    Wait(2.200000047683716)
    ForceAnimation(entity=3201441, animation_id=3, loop=False, wait_for_completion=False, skip_transition=True, unknown1=0, unknown2=1.0)
    Wait(0.20999999344348907)
    EnableFlag(13200445)
    DisableObjectActivation(3201441, obj_act_id=324012)
    End()
    Label(1)
    EnableFlag(13200445)
    DisableObjectActivation(3201441, obj_act_id=324012)
    EndOfAnimation(3201441, 0)
    End()
    Label(2)
    DisableObjectActivation(3201441, obj_act_id=324012)
    EndOfAnimation(3201441, 0)
    End()


@RestartOnRest
def Event13205441():
    """ 13205441: Event 13205441 """
    EndIfFlagOn(13200850)
    GotoIfThisEventSlotOn(Label.L0)
    GotoIfFlagOn(Label.L0, 13200445)
    DisableObject(3203850)
    DisableObject(3203851)
    DisableObject(3203852)
    DisableObject(3203853)
    IfPlayerInOwnWorld(1)
    IfFlagOn(1, 13200445)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutsceneAndSetMapCeremony(cutscene=32000000, cutscene_type=CutsceneType.SkippableFadeOut, ceremony_id=10, unknown=1, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    PlayCutsceneAndSetMapCeremony(cutscene=32000000, cutscene_type=CutsceneType.UnskippableFadeOut, ceremony_id=10, unknown=1, player_id=10000)
    SkipLines(1)
    PlayCutsceneAndSetMapCeremony(cutscene=32000000, cutscene_type=CutsceneType.Unskippable, ceremony_id=10, unknown=1, player_id=10000)
    WaitFrames(1)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    TriggerMultiplayerEvent(1)
    Label(0)
    SetMapCeremony(game_map=ARCHDRAGON_PEAK, ceremony_id=10)
    EnableFlag(13200446)
    EnableObject(3203850)
    EnableObject(3203851)
    EnableObject(3203852)
    EnableObject(3203853)
    End()


@RestartOnRest
def Event13205442():
    """ 13205442: Event 13205442 """
    GotoIfFlagOn(Label.L0, 13200862)
    IfFlagOn(0, 13200856)
    WaitFrames(1)
    Label(0)
    DisableObject(3203850)
    DisableObject(3203851)
    DisableObject(3203852)
    DisableObject(3203853)
    End()


@NeverRestart
def Event13205450():
    """ 13205450: Event 13205450 """
    RegisterLadder(start_climbing_flag=13200450, stop_climbing_flag=13200451, obj=3201450)
    RegisterLadder(start_climbing_flag=13200452, stop_climbing_flag=13200453, obj=3201451)
    RegisterLadder(start_climbing_flag=13200454, stop_climbing_flag=13200455, obj=3201452)
    RegisterLadder(start_climbing_flag=13200456, stop_climbing_flag=13200457, obj=3201453)
    RegisterLadder(start_climbing_flag=13200458, stop_climbing_flag=13200459, obj=3201454)


@RestartOnRest
def Event13205470(ARG_0_3: uint, ARG_4_7: int):
    """ 13205470: Event 13205470 """
    DisableNetworkSync()
    DisableFlag(13205479)
    IfMultiplayerEvent(1, ARG_0_3)
    IfFlagOff(1, 13205479)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13205479)
    PlaySoundEffect(anchor_entity=3201440, sound_type=SoundType.a_Ambient, sound_id=ARG_4_7)
    Wait(7.0)
    PlaySoundEffect(anchor_entity=3201440, sound_type=SoundType.a_Ambient, sound_id=ARG_4_7)
    Wait(7.0)
    PlaySoundEffect(anchor_entity=3201440, sound_type=SoundType.a_Ambient, sound_id=ARG_4_7)
    Wait(10.0)
    DisableFlag(13205479)
    Restart()


@RestartOnRest
def Event13205490(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13205490: Event 13205490 """
    DisableNetworkSync()
    DisableObject(ARG_0_3)
    DeleteObjectFX(ARG_0_3, erase_root=True)
    IfTryingToJoinSession(-1)
    IfTryingToCreateSession(-1)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFlagOff(Label.L0, ARG_8_11)
    EnableObject(ARG_0_3)
    CreateObjectFX(ARG_4_7, obj=ARG_0_3, model_point=101)
    Label(0)
    IfTryingToJoinSession(-2)
    IfTryingToCreateSession(-2)
    IfConditionFalse(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event13205810():
    """ 13205810: Event 13205810 """
    GotoIfFlagOff(Label.L0, 13200800)
    DisableCharacter(3200800)
    DisableAnimations(3200800)
    Kill(3200800, award_souls=False)
    End()
    Label(0)
    DisableCharacter(3200800)
    DisableAI(3200800)
    Move(3200800, destination=3202802, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_Collision=3200800)
    IfFlagOn(1, 13205805)
    IfCharacterInsideRegion(1, PLAYER, region=3202801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13200801)
    EnableCharacter(3200800)
    SetNetworkUpdateRate(3200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3200800)
    ForceAnimation(entity=3200800, animation_id=20001, loop=False, wait_for_completion=True, skip_transition=False, unknown1=0, unknown2=1.0)
    EnableBossHealthBar(3200800, name=903140)
    EnableFlag(13205802)


@NeverRestart
def Event13200811():
    """ 13200811: Event 13200811 """
    EndIfFlagOn(13200800)
    IfHealthComparison(0, character=3200800, comparison_type=ComparisonType.LessThanOrEqual, value=0.0)
    Wait(0.5)
    PlaySoundEffect(anchor_entity=3200800, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 3200800)
    Wait(3.5)
    KillBoss(3200800)
    EnableFlag(13200800)
    EnableFlag(9305)
    EnableFlag(6305)
    EndIfPlayerNotInOwnWorld()
    Wait(5.0)
    PlayCutscene(32000030, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=3202809, move_to_map=ARCHDRAGON_PEAK)
    SetRespawnPoint(3202953)
    SaveRequest()
    WaitFrames(1)
    ForceAnimation(entity=10000, animation_id=63010, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.c_CharacterMotion, sound_id=138008020)
    CreateTemporaryFX(30300, anchor_entity=10000, anchor_type=CoordEntityType.Character, model_point=236)


@RestartOnRest
def Event13205820():
    """ 13205820: Event 13205820 """
    RunCommonEvent(20005800, args=(13200800, 3201800, 3202800, 13205805, 3201800, 3200800, 13200801, 3202801))
    RunCommonEvent(20005801, args=(13200800, 3201800, 3202800, 13205805, 3201800, 13205806))
    RunCommonEvent(20005820, args=(13200800, 3201800, 3, 13200801))
    RunCommonEvent(20005820, args=(13200800, 3201801, 2, 13200801))
    RunCommonEvent(20001835, args=(13200800, 13205805, 13205806, 13205802, 3204801))
    RunCommonEvent(20005810, args=(13200800, 3201800, 3202800, 10000))


@RestartOnRest
def Event13205860():
    """ 13205860: Event 13205860 """
    GotoIfFlagOn(Label.L1, 13200445)
    GotoIfFlagOff(Label.L0, 13200850)
    Kill(3205850, award_souls=False)
    DisableCharacter(3205850)
    DisableAnimations(3205850)
    SetNetworkUpdateRate(3205850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    End()
    Label(0)
    DisableCharacter(3205850)
    DisableAnimations(3205850)
    IfFlagOn(0, 13200445)
    Label(1)
    EnableCharacter(3200850)
    DisableCharacter(3200851)
    EnableAnimations(3200850)
    DisableAnimations(3200851)
    DisableAI(3205850)
    EnableImmortality(3200850)
    ForceAnimation(entity=3200850, animation_id=700, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    IfFlagOn(1, 13205855)
    IfCharacterInsideRegion(1, PLAYER, region=3202850)
    IfConditionTrue(0, input_condition=1)
    SetNetworkUpdateRate(3200850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(entity=3200850, animation_id=1700, loop=False, wait_for_completion=True, skip_transition=False, unknown1=0, unknown2=1.0)
    EnableAI(3200850)
    EnableBossHealthBar(3200850, name=905030)
    EnableFlag(13205851)


@RestartOnRest
def Event13205861():
    """ 13205861: Event 13205861 """
    EndIfFlagOn(13200850)
    IfHealthComparison(1, character=3200850, comparison_type=ComparisonType.LessThanOrEqual, value=0.009999999776482582)
    IfPlayerInOwnWorld(1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-1, character=3200850, special_effect=12160)
    SkipLinesIfConditionTrue(1, -1)
    ForceAnimation(entity=3200850, animation_id=20001, loop=False, wait_for_completion=True, skip_transition=False, unknown1=0, unknown2=1.0)
    DisableBossMusic(-1)
    WaitFrames(1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(32000010, skippable=True, fade_out=True, player_id=PLAYER, move_to_region=3202858, move_to_map=ARCHDRAGON_PEAK)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    PlayCutscene(32000010, skippable=False, fade_out=True, player_id=PLAYER, move_to_region=3202858, move_to_map=ARCHDRAGON_PEAK)
    SkipLines(1)
    PlayCutscene(32000010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    Kill(3200850, award_souls=False)
    DisableCharacter(3200850)
    DisableAnimations(3200850)
    DisableAI(3200850)
    SetNetworkUpdateRate(3200850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    DisableBossHealthBar(3200850, name=905030)
    EnableCharacter(3200851)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    SetNetworkUpdateAuthority(3200851, UpdateAuthority.Forced)
    EnableAnimations(3200851)
    EnableAI(3200851)
    SetNetworkUpdateRate(3200851, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3200851, name=905010)
    EnableFlag(13205852)


@NeverRestart
def Event13200862():
    """ 13200862: Event 13200862 """
    EndIfThisEventSlotOn()
    GotoIfFlagOn(Label.L2, 13200856)
    GotoIfFlagOn(Label.L1, 13200855)
    GotoIfFlagOn(Label.L0, 13200850)
    IfCharacterDead(1, 3200851)
    IfPlayerInOwnWorld(1)
    IfConditionTrue(0, input_condition=1)
    Wait(2.200000047683716)
    KillBoss(3200851)
    EnableFlag(13200850)
    EnableFlag(9304)
    EnableFlag(6304)
    Wait(5.0)
    Label(0)
    EnableFlag(13200855)
    WaitFrames(1)
    Label(1)
    EnableFlag(13200856)
    Label(2)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(32000020, cutscene_type=CutsceneType.SkippableFadeOut, ceremony_id=0, unknown=0, region=3202859, game_map=ARCHDRAGON_PEAK, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(32000020, cutscene_type=CutsceneType.UnskippableFadeOut, ceremony_id=0, unknown=0, region=3202859, game_map=ARCHDRAGON_PEAK, player_id=10000)
    SkipLines(1)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(32000020, cutscene_type=CutsceneType.Unskippable, ceremony_id=0, unknown=0, region=3202857, game_map=ARCHDRAGON_PEAK, player_id=10000)
    WaitFrames(1)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    TriggerMultiplayerEvent(2)


@NeverRestart
def Event13200863():
    """ 13200863: Event 13200863 """
    EndIfFlagOn(13200850)
    IfHealthComparison(0, character=3200851, comparison_type=ComparisonType.LessThanOrEqual, value=0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=3200851, sound_type=SoundType.s_SFX, sound_id=777777777)


@RestartOnRest
def Event13205864():
    """ 13205864: Event 13205864 """
    DisableNetworkSync()
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EndIfFlagOn(13200850)
    SkipLinesIfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    IfFlagOn(0, 13205855)
    SkipLines(1)
    IfFlagOn(0, 13205856)
    GotoIfFlagOn(Label.L0, 13205852)
    ChangeCamera(normal_camera_id=5030, locked_camera_id=5030)
    IfFlagOn(0, 13205852)
    Label(0)
    ChangeCamera(normal_camera_id=5270, locked_camera_id=5270)
    IfFlagOn(0, 13200850)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest
def Event13205870():
    """ 13205870: Event 13205870 """
    RunCommonEvent(20005800, args=(13200850, 3201850, 3202850, 13205855, 3201850, 3205850, 0, 0))
    RunCommonEvent(20005801, args=(13200850, 3201850, 3202850, 13205855, 3201850, 13205856))
    RunCommonEvent(20005820, args=(13200855, 3201850, 832040, 13200446))
    RunCommonEvent(20001836, args=(13200850, 13205855, 13205856, 13205851, 3204851, 3204852, 13205852))
    RunCommonEvent(20005810, args=(13200850, 3201785, 3202785, 10000))
    RunCommonEvent(20005810, args=(13200850, 3201786, 3202786, 10000))


@RestartOnRest
def Event13205880():
    """ 13205880: Event 13205880 """
    EndIfFlagOn(13200850)
    CreateNPCPart(3200850, npc_part_id=1, part_index=NPCPartType.Part1, part_health=350, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(0, 3200850, npc_part_id=1, value=0)
    ForceAnimation(entity=3200850, animation_id=20000, loop=False, wait_for_completion=True, skip_transition=True, unknown1=0, unknown2=1.0)
    Restart()


@RestartOnRest
def Event13205910(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13205910: Event 13205910 """
    DisableNetworkSync()
    EndIfFlagOn(ARG_0_3)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfCharacterHasSpecialEffect(1, character=PLAYER, special_effect=4400)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(-1, 4.0)
    IfCharacterDoesNotHaveSpecialEffect(-1, character=PLAYER, special_effect=4400)
    IfConditionTrue(0, input_condition=-1)
    RestartIfCharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4400)
    AwardItemLot(ARG_8_11, host_only=False)
    EnableFlag(ARG_0_3)
    End()


@RestartOnRest
def Event13205930():
    """ 13205930: Event 13205930 """
    EndIfFlagOn(13200850)
    EndIfFlagOn(13200930)
    EndIfFlagOn(13200445)
    IfFlagOn(1, 13204190)
    IfCharacterInsideRegion(1, 3200190, region=3202930)
    IfFlagOn(2, 13200445)
    IfFlagOn(2, 13204190)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFlagOn(Label.L1, 13200445)
    Label(0)
    EnableInvincibility(3200190)
    RotateToFaceEntity(3200190, 3202932, animation=60060, wait_for_completion=True)
    ForceAnimation(entity=3200190, animation_id=91050, loop=False, wait_for_completion=True, skip_transition=False, unknown1=0, unknown2=1.0)
    Wait(5.0)
    ForceAnimation(entity=3200190, animation_id=91052, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    Wait(1.0)
    SendNPCSummonHome(3200190)
    EnableFlag(13200930)
    End()
    Label(1)
    ForceAnimation(entity=3200190, animation_id=91030, loop=False, wait_for_completion=False, skip_transition=False, unknown1=0, unknown2=1.0)
    Wait(2.0)
    SendNPCSummonHome(3200190)


@RestartOnRest
def Event13205931():
    """ 13205931: Event 13205931 """
    IfFlagOn(-1, 13200445)
    IfFlagOn(-1, 13200930)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(13200931)
