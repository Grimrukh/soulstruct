"""
Lothric Castle / Consumed King's Garden

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
    RegisterBonfire(bonfire_flag=13010000, obj=3011950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13010002, obj=3011952, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13010800, bonfire_flag=13010001, character=3010951, obj=3011951)
    Event_13015470()
    CommonFunc_20005780(0, obj=3011750, model_point=3)
    CommonFunc_20005780(0, obj=3011751, model_point=3)
    CommonFunc_20005780(0, obj=3011753, model_point=3)
    CommonFunc_20005400(0, character=3010300)
    CommonFunc_20005400(0, character=3010301)
    CommonFunc_20005110(0, character=3010350, region=3012380)
    CommonFunc_20005132(0, character=3010413, radius=5.0, region=3012460)
    CommonFunc_20005201(0, character=3010414, animation_id=700, animation_id_1=1700, region=3012480, seconds=0.0)
    CommonFunc_20005201(
        0,
        character=3010415,
        animation_id=700,
        animation_id_1=1700,
        region=3012480,
        seconds=0.4000000059604645,
    )
    CommonFunc_20005210(0, character=3010417, animation_id=700, animation_id_1=1700, radius=22.0)
    CommonFunc_20005110(0, character=3010418, region=3012380)
    CommonFunc_20005110(0, character=3010419, region=3012380)
    CommonFunc_20005210(0, character=3010420, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005110(0, character=3010430, region=3012340)
    CommonFunc_20005330(0, character=3010431, region=3012450, flag=13015231)
    CommonFunc_20005110(0, character=3010432, region=3012450)
    CommonFunc_20005110(0, character=3010450, region=3012604)
    CommonFunc_20005111(0, character=3010451, animation_id=3010, region=3012605)
    Event_13015310(0, character=3010460, animation_id=706, animation_id_1=1706)
    CommonFunc_20005110(0, character=3010500, region=3012600)
    CommonFunc_20005215(
        0,
        character=3010501,
        animation_id=710,
        animation_id_1=1710,
        radius=5.0,
        seconds=0.800000011920929,
    )
    CommonFunc_20005215(
        0,
        character=3010502,
        animation_id=710,
        animation_id_1=1710,
        radius=5.0,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005220(0, character=3010503, animation_id=703, animation_id_1=1703)
    CommonFunc_20005220(0, character=3010504, animation_id=706, animation_id_1=1706)
    CommonFunc_20005220(0, character=3010506, animation_id=706, animation_id_1=1706)
    CommonFunc_20005202(0, character=3010507, animation_id=710, animation_id_1=1710, region=3012530)
    CommonFunc_20005110(0, character=3010508, region=3012600)
    CommonFunc_20005110(0, character=3010510, region=3012472)
    CommonFunc_20005110(0, character=3010511, region=3012472)
    CommonFunc_20005202(0, character=3010512, animation_id=710, animation_id_1=1710, region=3012531)
    CommonFunc_20005200(0, character=3010520, animation_id=706, animation_id_1=1706, region=3012435)
    CommonFunc_20005201(0, character=3010521, animation_id=706, animation_id_1=1706, region=3012435, seconds=0.5)
    CommonFunc_20005215(
        0,
        character=3010538,
        animation_id=710,
        animation_id_1=1710,
        radius=5.0,
        seconds=0.699999988079071,
    )
    CommonFunc_20005200(0, character=3010539, animation_id=703, animation_id_1=1703, region=3012600)
    CommonFunc_20005220(0, character=3010549, animation_id=705, animation_id_1=1705)
    CommonFunc_20005110(0, character=3010551, region=3012430)
    CommonFunc_20005119(
        0,
        character=3010557,
        region=3012338,
        region_1=3012339,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3010558,
        region=3012338,
        region_1=3012339,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005110(0, character=3010562, region=3012335)
    CommonFunc_20005110(0, character=3010563, region=3012440)
    CommonFunc_20005110(0, character=3010564, region=3012440)
    CommonFunc_20005110(0, character=3010565, region=3012335)
    CommonFunc_20005110(0, character=3010566, region=3012440)
    CommonFunc_20005202(0, character=3010567, animation_id=710, animation_id_1=1710, region=3012530)
    CommonFunc_20005110(0, character=3010568, region=3012600)
    CommonFunc_20005200(0, character=3010569, animation_id=703, animation_id_1=1703, region=3012470)
    CommonFunc_20005122(0, character=3010570, animation_id=3000, radius=5.0)
    CommonFunc_20005110(0, character=3010571, region=3012471)
    CommonFunc_20005202(0, character=3010572, animation_id=710, animation_id_1=1710, region=3012530)
    CommonFunc_20005220(0, character=3010573, animation_id=703, animation_id_1=1703)
    CommonFunc_20005220(0, character=3010574, animation_id=706, animation_id_1=1706)
    Event_13015230()
    CommonFunc_20005110(0, character=3010610, region=3012490)
    CommonFunc_20005341(0, flag=13010590, character=3010610, item_lot=13103000)
    CommonFunc_20000343(0, flag=13010591, character=3010300, flag_1=21201100)
    CommonFunc_20000343(0, flag=13010592, character=3010301, flag_1=21201000)
    CommonFunc_20005341(0, flag=13010593, character=3010310, item_lot=21504000)
    CommonFunc_20005341(0, flag=13010593, character=3010311, item_lot=21504010)
    Event_13015550(0, character=3010830)
    Event_13015551(0, character=3010831)
    Event_13015555()
    Event_13015590(0, flag=13010890, character=3010830, tae_event_id=20)
    Event_13015590(1, flag=13010891, character=3010831, tae_event_id=30)
    Event_13015556(0, character=3010835, flag=13010895, flag_1=13010890, flag_2=13015550)
    Event_13015557(0, character=3010836, flag=13010896, flag_1=13010891)
    Event_13015558(0, character=3010835, destination=3010830, flag=13010895, model_point=40)
    Event_13015559(0, character=3010836, destination=3010831, flag=13010896, model_point=41)
    Event_13015580()
    Event_13015581()
    Event_13015585()
    CommonFunc_20005410(0, character=3010551, animation_id=3005)
    CommonFunc_20005411(
        0,
        character=3010551,
        character_1=3010555,
        animation_id=703,
        animation_id_1=1703,
        seconds=0.4000000059604645,
    )
    CommonFunc_20005411(
        0,
        character=3010551,
        character_1=3010556,
        animation_id=705,
        animation_id_1=1705,
        seconds=0.800000011920929,
    )
    CommonFunc_20005411(
        0,
        character=3010551,
        character_1=3010560,
        animation_id=703,
        animation_id_1=1703,
        seconds=0.8999999761581421,
    )
    CommonFunc_20005411(0, character=3010551, character_1=3010561, animation_id=703, animation_id_1=1703, seconds=1.0)
    CommonFunc_20005415(
        0,
        flag=13011500,
        character=3010500,
        character_1=3010600,
        animation_id=706,
        animation_id_1=1706,
        region=0,
        flag_1=13015501,
        flag_2=13015502,
    )
    CommonFunc_20005415(
        0,
        flag=13011510,
        character=3010539,
        character_1=3010602,
        animation_id=703,
        animation_id_1=1703,
        region=0,
        flag_1=13015503,
        flag_2=13015504,
    )
    CommonFunc_20005415(
        0,
        flag=13011520,
        character=3010568,
        character_1=3010604,
        animation_id=703,
        animation_id_1=1703,
        region=0,
        flag_1=13015505,
        flag_2=13015506,
    )
    CommonFunc_20005520(0, flag=13010500, obj=3011450, obj_act_id=3014300)
    CommonFunc_20005520(0, flag=13010501, obj=3011451, obj_act_id=3014301)
    CommonFunc_20005520(0, flag=13010502, obj=3011452, obj_act_id=3014302)
    CommonFunc_20005520(0, flag=13010503, obj=3011453, obj_act_id=3014303)
    CommonFunc_20005520(0, flag=13010504, obj=3011454, obj_act_id=3014304)
    CommonFunc_20005520(0, flag=13010510, obj=3011460, obj_act_id=3014310)
    CommonFunc_20005520(0, flag=13010511, obj=3011461, obj_act_id=3014311)
    CommonFunc_20005520(0, flag=13010512, obj=3011462, obj_act_id=3014312)
    CommonFunc_20005520(0, flag=13010514, obj=3011464, obj_act_id=3014314)
    CommonFunc_20005530(0, obj_flag=13015400, obj=3011300)
    CommonFunc_20005530(0, obj_flag=13015401, obj=3011301)
    CommonFunc_20005530(0, obj_flag=13015402, obj=3011302)
    CommonFunc_20005530(0, obj_flag=13015403, obj=3011303)
    CommonFunc_20005530(0, obj_flag=13015404, obj=3011304)
    CommonFunc_20005530(0, obj_flag=13015405, obj=3011305)
    CommonFunc_20005530(0, obj_flag=13015406, obj=3011306)
    CommonFunc_20005530(0, obj_flag=13015407, obj=3011307)
    CommonFunc_20005530(0, obj_flag=13015408, obj=3011308)
    CommonFunc_20005530(0, obj_flag=13015409, obj=3011309)
    CommonFunc_20005530(0, obj_flag=13015410, obj=3011310)
    CommonFunc_20005530(0, obj_flag=13015411, obj=3011311)
    CommonFunc_20005530(0, obj_flag=13015412, obj=3011312)
    CommonFunc_20005530(0, obj_flag=13015413, obj=3011313)
    CommonFunc_20005530(0, obj_flag=13015414, obj=3011314)
    CommonFunc_20005530(0, obj_flag=13015415, obj=3011315)
    CommonFunc_20005530(0, obj_flag=13015416, obj=3011316)
    CommonFunc_20005530(0, obj_flag=13015417, obj=3011317)
    CommonFunc_20005530(0, obj_flag=13015418, obj=3011318)
    CommonFunc_20005530(0, obj_flag=13015419, obj=3011319)
    CommonFunc_20005530(0, obj_flag=13015420, obj=3011320)
    CommonFunc_20005530(0, obj_flag=13015421, obj=3011321)
    CommonFunc_20005530(0, obj_flag=13015422, obj=3011322)
    CommonFunc_20005530(0, obj_flag=13015423, obj=3011323)
    CommonFunc_20005530(0, obj_flag=13015424, obj=3011324)
    CommonFunc_20005530(0, obj_flag=13015425, obj=3011325)
    CommonFunc_20005530(0, obj_flag=13015426, obj=3011326)
    CommonFunc_20005530(0, obj_flag=13015427, obj=3011327)
    CommonFunc_20005530(0, obj_flag=13015428, obj=3011328)
    CommonFunc_20005530(0, obj_flag=13015429, obj=3011329)
    CommonFunc_20005530(0, obj_flag=13015430, obj=3011330)
    CommonFunc_20005530(0, obj_flag=13015431, obj=3011331)
    CommonFunc_20005650(0, flag=13010310, obj=3011390)
    CommonFunc_20005622(0, flag=13010450, flag_1=13010452, entity=3011400, obj=3011401, obj_1=3011402, flag_2=13011450)
    CommonFunc_20005628(0, flag=13010451, obj=3011402, region=3012401)
    CommonFunc_20005620(0, flag=13010460, flag_1=13010462, entity=3011410, obj=3011411, obj_1=3011412, flag_2=13011460)
    CommonFunc_20005628(0, flag=13010461, obj=3011412, region=3012411)
    Event_13015225()
    Event_13014522()
    EnableObjectInvulnerability(3011500)
    EnableObjectInvulnerability(3011501)
    Event_13015200(0, flag=13010300, flag_1=13010302, entity=3011491, flag_2=13011300)
    Event_13015202()
    Event_13015210(0, flag=13010301, obj=3011491)
    CommonFunc_20005610(0, flag=13010550, region=3012421, region_1=3012420)
    CommonFunc_20005611(0, flag=13010550, obj_act_id=13011580, obj=3011420, obj_act_id_1=300320)
    Event_13014242()
    RegisterLadder(start_climbing_flag=13010670, stop_climbing_flag=13010671, obj=3011670)
    RegisterLadder(start_climbing_flag=13010672, stop_climbing_flag=13010673, obj=3011671)
    RegisterLadder(start_climbing_flag=13010674, stop_climbing_flag=13010675, obj=3011672)
    RegisterLadder(start_climbing_flag=13010676, stop_climbing_flag=13010677, obj=3011673)
    CommonFunc_20005523(0, obj=3011270, completion_count=1)
    CommonFunc_20005523(0, obj=3011271, completion_count=1)
    CommonFunc_20005523(0, obj=3011272, completion_count=2)
    CommonFunc_20005701(
        0,
        left=13010800,
        summon_flag=13014191,
        dismissal_flag=13015191,
        character=3010191,
        region=3012705,
        left_1=70000008,
    )
    CommonFunc_20005710(0, flag=13014191, flag_1=13015805, character=3010191, region=3012801, region_1=3012820)
    CommonFunc_20005720(0, flag=13014191, flag_1=13015191, flag_2=13010800, character=3010191)
    CommonFunc_20005701(
        0,
        left=13010800,
        summon_flag=13014192,
        dismissal_flag=13015192,
        character=3010192,
        region=3012710,
        left_1=70000017,
    )
    CommonFunc_20005710(0, flag=13014192, flag_1=13015805, character=3010192, region=3012801, region_1=3012820)
    CommonFunc_20005720(0, flag=13014192, flag_1=13015192, flag_2=13010800, character=3010192)
    Event_13015810()
    Event_13015811()
    Event_13015812()
    Event_13015820()
    Event_13015815()
    Event_13015830(0, character=3010812, seconds=1.2000000476837158)
    CommonFunc_20006010(0, flag=73010952, animation_id=69003)
    CommonFunc_20006031(0, flag=73010953, region=3012750)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(3010790)
    DisableGravity(3010790)
    DisableCharacterCollision(3010790)
    DisableSoundEvent(sound_id=3012803)
    DisableSoundEvent(sound_id=3012804)


@RestartOnRest(13014242)
def Event_13014242():
    """Event 13014242"""
    if PlayerInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=13010550)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=3011420, animation_id=1)
    End()


@RestartOnRest(13014522)
def Event_13014522():
    """Event 13014522"""
    CommonFunc_20005623(
        0,
        flag=13010450,
        flag_1=13010452,
        obj=3011400,
        obj_1=3011401,
        obj_act_id=3014401,
        obj_2=3011402,
        obj_act_id_1=3014402,
        region=3012401,
        region_1=3012402,
        flag_2=13011450,
        flag_3=13014450,
        left=13010451,
    )
    Event_13015220(
        0,
        flag=13010460,
        entity=3011410,
        obj=3011411,
        obj_act_id=3014411,
        obj_1=3011413,
        obj_act_id_1=3014413,
        obj_2=3011412,
        obj_act_id_2=3014412,
    )


@RestartOnRest(13015200)
def Event_13015200(_, flag: int, flag_1: int, entity: int, flag_2: int):
    """Event 13015200"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(flag_2)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    ForceAnimation(entity, 0, skip_transition=True, unknown2=1.0)
    DisableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, 2, skip_transition=True, unknown2=1.0)
    EnableFlag(flag_1)
    End()


@RestartOnRest(13015201)
def Event_13015201(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    obj_1: int,
    obj_act_id: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
):
    """Event 13015201"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObjectActivation(obj_1, obj_act_id=304874)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_2.Add(FlagEnabled(flag))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    ForceAnimation(obj, 1, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    Wait(2.0)
    ForceAnimation(obj, 1, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.Off)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(ObjectBackreadEnabled(obj=obj))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.Off)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObjectActivation(obj_1, obj_act_id=304874)
    OR_5.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_6.Add(FlagDisabled(flag))
    OR_7.Add(OR_5)
    OR_7.Add(OR_6)
    
    MAIN.Await(OR_7)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L3, flag=flag_3)
    EnableFlag(flag_4)
    ForceAnimation(obj, 3, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    Wait(2.0)
    EnableFlag(flag_4)
    ForceAnimation(obj, 3, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.Off)

    # --- Label 4 --- #
    DefineLabel(4)
    AND_2.Add(ObjectBackreadEnabled(obj=obj))
    
    MAIN.Await(AND_2)
    
    DisableFlag(flag_4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag_2, state=FlagSetting.Off)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@EndOnRest(13015202)
def Event_13015202():
    """Event 13015202"""
    Event_13015201(
        0,
        flag=13010300,
        flag_1=13010302,
        obj=3011491,
        obj_1=3011490,
        obj_act_id=3014500,
        flag_2=13011300,
        flag_3=13014300,
        flag_4=13010301,
    )


@RestartOnRest(13015210)
def Event_13015210(_, flag: int, obj: int):
    """Event 13015210"""
    MAIN.Await(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    
    WaitFrames(frames=2)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    Wait(1.2999999523162842)
    CreateHazard(
        obj_flag=13015211,
        obj=obj,
        model_point=40,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015212,
        obj=obj,
        model_point=41,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015213,
        obj=obj,
        model_point=42,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015214,
        obj=obj,
        model_point=43,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015215,
        obj=obj,
        model_point=44,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015216,
        obj=obj,
        model_point=45,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015217,
        obj=obj,
        model_point=46,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=13015218,
        obj=obj,
        model_point=47,
        behavior_param_id=5300,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.5,
        repetition_time=0.0,
    )
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(2.0)
    Restart()


@RestartOnRest(13015220)
def Event_13015220(
    _,
    flag: int,
    entity: int,
    obj: int,
    obj_act_id: int,
    obj_1: int,
    obj_act_id_1: int,
    obj_2: int,
    obj_act_id_2: int,
):
    """Event 13015220"""
    MAIN.Await(FlagEnabled(13010461))
    
    GotoIfFlagEnabled(Label.L3, flag=flag)
    EnableObjectActivation(obj_1, obj_act_id=304873)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(ObjectActivated(obj_act_id=obj_act_id_2))
    OR_3.Add(FlagEnabled(flag))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3012411))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=3012412))
    OR_6.Add(OR_1)
    OR_6.Add(OR_2)
    OR_6.Add(OR_3)
    OR_6.Add(OR_4)
    OR_6.Add(OR_5)
    
    MAIN.Await(OR_6)
    
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_2)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(2.0)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(2.0)
    ForceAnimation(entity, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_1.Add(AllPlayersOutsideRegion(region=3012412))
    AND_1.Add(AllPlayersOutsideRegion(region=3012413))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(entity, 10, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableObjectActivation(obj, obj_act_id=304873)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    OR_7.Add(ObjectActivated(obj_act_id=obj_act_id))
    OR_8.Add(ObjectActivated(obj_act_id=obj_act_id_2))
    OR_9.Add(FlagDisabled(flag))
    OR_10.Add(CharacterInsideRegion(character=PLAYER, region=3012412))
    OR_11.Add(CharacterInsideRegion(character=PLAYER, region=3012413))
    OR_12.Add(OR_7)
    OR_12.Add(OR_8)
    OR_12.Add(OR_9)
    OR_12.Add(OR_10)
    OR_12.Add(OR_11)
    
    MAIN.Await(OR_12)
    
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_7)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_8)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L6)

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(2.0)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    Wait(2.0)
    ForceAnimation(entity, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    AND_2.Add(AllPlayersOutsideRegion(region=3012411))
    AND_2.Add(AllPlayersOutsideRegion(region=3012412))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(entity, 120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(entity, 20, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    DisableFlag(flag)
    EnableObjectActivation(obj_1, obj_act_id=304873)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    Restart()


@RestartOnRest(13015225)
def Event_13015225():
    """Event 13015225"""
    if FlagEnabled(13010461):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3012412))
    AND_1.Add(FlagDisabled(13010461))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010170, number_buttons=NumberButtons.OneButton)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3012412))
    
    Wait(1.0)
    Restart()


@RestartOnRest(13015230)
def Event_13015230():
    """Event 13015230"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3012451))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(13015231))
    
    MAIN.Await(OR_2)
    
    ClearTargetList(3010505)
    AddSpecialEffect(3010505, 5000)
    ChangePatrolBehavior(3010505, patrol_information_id=3014300)
    EnableFlag(13015231)
    
    MAIN.Await(HasAIStatus(3010505, ai_status=AIStatusType.Battle))
    
    RemoveSpecialEffect(3010505, 5000)


@RestartOnRest(13015310)
def Event_13015310(_, character: int, animation_id: int, animation_id_1: int):
    """Event 13015310"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(CharacterDead(3010418))
    OR_2.Add(CharacterDead(3010419))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(13015470)
def Event_13015470():
    """Event 13015470"""
    DisableNetworkSync()
    
    MAIN.Await(ObjectBackreadEnabled(obj=3011600))
    
    WaitFrames(frames=5)
    ShowObjectByMapCeremony(obj=3011600, ceremony_id=10, unknown=2000)
    ShowObjectByMapCeremony(obj=3011601, ceremony_id=30, unknown=1400)
    ShowObjectByMapCeremony(obj=3011602, ceremony_id=10, unknown=790)
    ShowObjectByMapCeremony(obj=3011605, ceremony_id=20, unknown=1010)
    ShowObjectByMapCeremony(obj=3011606, ceremony_id=40, unknown=710)
    ShowObjectByMapCeremony(obj=3011607, ceremony_id=20, unknown=1400)
    ShowObjectByMapCeremony(obj=3011610, ceremony_id=10, unknown=4320)
    ShowObjectByMapCeremony(obj=3011611, ceremony_id=40, unknown=3800)
    ShowObjectByMapCeremony(obj=3011612, ceremony_id=30, unknown=4420)
    ShowObjectByMapCeremony(obj=3011613, ceremony_id=40, unknown=0)
    ShowObjectByMapCeremony(obj=3011615, ceremony_id=110, unknown=0)
    ShowObjectByMapCeremony(obj=3011616, ceremony_id=110, unknown=290)
    ShowObjectByMapCeremony(obj=3011617, ceremony_id=110, unknown=440)
    ShowObjectByMapCeremony(obj=3011628, ceremony_id=110, unknown=880)
    ShowObjectByMapCeremony(obj=3011631, ceremony_id=110, unknown=1640)
    ShowObjectByMapCeremony(obj=3011620, ceremony_id=120, unknown=470)
    ShowObjectByMapCeremony(obj=3011621, ceremony_id=120, unknown=680)
    ShowObjectByMapCeremony(obj=3011622, ceremony_id=120, unknown=920)
    ShowObjectByMapCeremony(obj=3011629, ceremony_id=120, unknown=1250)
    ShowObjectByMapCeremony(obj=3011632, ceremony_id=120, unknown=2070)
    ShowObjectByMapCeremony(obj=3011625, ceremony_id=130, unknown=1030)
    ShowObjectByMapCeremony(obj=3011626, ceremony_id=130, unknown=1280)
    ShowObjectByMapCeremony(obj=3011627, ceremony_id=130, unknown=1440)
    ShowObjectByMapCeremony(obj=3011630, ceremony_id=130, unknown=1880)
    ShowObjectByMapCeremony(obj=3011633, ceremony_id=130, unknown=2640)
    ShowObjectByMapCeremony(obj=3011636, ceremony_id=10, unknown=3100)
    ShowObjectByMapCeremony(obj=3011637, ceremony_id=20, unknown=2500)
    ShowObjectByMapCeremony(obj=3011638, ceremony_id=40, unknown=2300)
    ShowObjectByMapCeremony(obj=3011639, ceremony_id=10, unknown=2110)
    ShowObjectByMapCeremony(obj=3011640, ceremony_id=20, unknown=1920)
    ShowObjectByMapCeremony(obj=3011641, ceremony_id=30, unknown=2400)
    ShowObjectByMapCeremony(obj=3011642, ceremony_id=40, unknown=4790)
    ShowObjectByMapCeremony(obj=3011643, ceremony_id=20, unknown=4900)
    ShowObjectByMapCeremony(obj=3011644, ceremony_id=30, unknown=5490)
    ShowObjectByMapCeremony(obj=3011645, ceremony_id=110, unknown=1000)
    ShowObjectByMapCeremony(obj=3011646, ceremony_id=110, unknown=1290)
    ShowObjectByMapCeremony(obj=3011647, ceremony_id=110, unknown=1440)
    ShowObjectByMapCeremony(obj=3011648, ceremony_id=110, unknown=1880)
    ShowObjectByMapCeremony(obj=3011649, ceremony_id=110, unknown=2640)
    ShowObjectByMapCeremony(obj=3011650, ceremony_id=120, unknown=1470)
    ShowObjectByMapCeremony(obj=3011651, ceremony_id=120, unknown=1680)
    ShowObjectByMapCeremony(obj=3011652, ceremony_id=120, unknown=1920)
    ShowObjectByMapCeremony(obj=3011653, ceremony_id=120, unknown=2250)
    ShowObjectByMapCeremony(obj=3011654, ceremony_id=120, unknown=3200)
    ShowObjectByMapCeremony(obj=3011655, ceremony_id=130, unknown=2030)
    ShowObjectByMapCeremony(obj=3011656, ceremony_id=130, unknown=2280)
    ShowObjectByMapCeremony(obj=3011657, ceremony_id=130, unknown=2440)
    ShowObjectByMapCeremony(obj=3011658, ceremony_id=130, unknown=2880)
    ShowObjectByMapCeremony(obj=3011659, ceremony_id=130, unknown=3640)
    
    MAIN.Await(ObjectBackreadDisabled(obj=3011600))
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(13015475)
def Event_13015475():
    """Event 13015475"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(0.10000000149011612)
    Move(3010501, destination=3012510, destination_type=CoordEntityType.Region, short_move=True)
    Move(3010502, destination=3012511, destination_type=CoordEntityType.Region, short_move=True)
    Move(3010538, destination=3012512, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(13015550)
def Event_13015550(_, character: int):
    """Event 13015550"""
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    if FlagEnabled(13010895):
        return
    GotoIfFlagEnabled(Label.L1, flag=13010890)
    GotoIfFlagDisabled(Label.L0, flag=13010580)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableImmortality(character)
    ForceAnimation(character, 30000, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(13010580))
    
    Wait(0.0)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableImmortality(character)
    ForceAnimation(character, 20006, wait_for_completion=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    DisableAnimations(character)
    EnableImmortality(character)
    ForceAnimation(character, 30002, loop=True, unknown2=1.0)
    DisableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)


@RestartOnRest(13015551)
def Event_13015551(_, character: int):
    """Event 13015551"""
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    if FlagEnabled(13010896):
        return
    EnableCharacter(character)
    if FlagDisabled(13010891):
        EnableAnimations(character)
    EnableImmortality(character)
    GotoIfFlagEnabled(Label.L1, flag=13010891)
    GotoIfFlagDisabled(Label.L0, flag=13010580)
    ForceAnimation(character, 30000, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    OR_15.Add(CharacterHuman(PLAYER))
    OR_15.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_15)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3012320))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 20004, unknown2=1.0)
    EnableFlag(13010580)
    EnableFlag(9420)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, 30002, loop=True, unknown2=1.0)
    DisableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)


@RestartOnRest(13015555)
def Event_13015555():
    """Event 13015555"""
    if FlagEnabled(13010890):
        return
    CreateNPCPart(3010831, npc_part_id=10, part_index=NPCPartType.Part3, part_health=100)
    AND_1.Add(FlagEnabled(13015550))
    AND_1.Add(FlagEnabled(13015551))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(3010830, npc_part_id=10, part_index=NPCPartType.Part3, part_health=100)
    OR_1.Add(CharacterPartHealth(3010830, npc_part_id=10) <= 1)
    OR_1.Add(CharacterPartHealth(3010831, npc_part_id=10) <= 1)
    OR_1.Add(HealthRatio(3010830) <= 0.0010000000474974513)
    OR_1.Add(HealthRatio(3010831) <= 0.0010000000474974513)
    
    MAIN.Await(OR_1)
    
    EnableFlag(13010890)
    AND_1.Add(CharacterPartHealth(3010830, npc_part_id=10) <= 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(CharacterPartHealth(3010831, npc_part_id=10) <= 0)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    AND_3.Add(HealthRatio(3010830) <= 0.0010000000474974513)
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_4.Add(HealthRatio(3010831) <= 0.0010000000474974513)
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableHealthBar(3010830)
    SetLockOnPoint(character=3010830, lock_on_model_point=220, state=False)
    ForceAnimation(3010830, 20005, unknown2=1.0)
    DisableAnimations(3010830)
    Wait(3.0)
    DisableHealthBar(3010831)
    SetLockOnPoint(character=3010831, lock_on_model_point=220, state=False)
    DisableAnimations(3010831)
    ForceAnimation(3010831, 20005, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3010830, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    SetNetworkUpdateRate(3010831, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableHealthBar(3010831)
    SetLockOnPoint(character=3010831, lock_on_model_point=220, state=False)
    ForceAnimation(3010831, 20005, unknown2=1.0)
    DisableAnimations(3010831)
    Wait(3.0)
    DisableHealthBar(3010830)
    SetLockOnPoint(character=3010830, lock_on_model_point=220, state=False)
    DisableAnimations(3010830)
    ForceAnimation(3010830, 20005, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3010830, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    SetNetworkUpdateRate(3010831, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    End()


@RestartOnRest(13015556)
def Event_13015556(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13015556"""
    DisableCharacter(character)
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_2))
    
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    ForceAnimation(character, 700, loop=True, unknown2=1.0)
    EnableCharacter(character)
    EnableAnimations(character)
    DisableAI(character)
    DisableGravity(character)
    EnableInvincibility(character)
    DisableHealthBar(character)
    DisableCharacterCollision(character)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableAI(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=True)
    DisableInvincibility(character)
    EnableHealthBar(character)
    ForceAnimation(character, 1700, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=True)
    DisableInvincibility(character)
    EnableHealthBar(character)
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    EnableFlag(flag)
    SetNetworkUpdateRate(3010830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3010830, 20007, skip_transition=True, unknown2=1.0)
    Wait(6.800000190734863)
    Kill(3010830, award_souls=True)
    DisableCharacter(3010830)
    DisableAnimations(3010830)
    SetNetworkUpdateRate(3010830, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    AwardItemLot(31411000, host_only=False)


@RestartOnRest(13015557)
def Event_13015557(_, character: int, flag: int, flag_1: int):
    """Event 13015557"""
    DisableCharacter(character)
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableHealthBar(character)
    DisableCharacterCollision(character)
    if FlagEnabled(flag):
        return
    EnableCharacter(character)
    EnableAnimations(character)
    DisableAI(character)
    DisableGravity(character)
    EnableInvincibility(character)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    ForceAnimation(character, 700, loop=True, unknown2=1.0)
    EnableCharacter(character)
    EnableAnimations(character)
    DisableAI(character)
    DisableGravity(character)
    EnableInvincibility(character)
    DisableHealthBar(character)
    DisableCharacterCollision(character)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableAI(character)
    DisableInvincibility(character)
    EnableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=True)
    ForceAnimation(character, 1700, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)
    DisableInvincibility(character)
    EnableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=True)
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    EnableFlag(flag)
    SetNetworkUpdateRate(3010831, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3010831, 20007, skip_transition=True, unknown2=1.0)
    Wait(6.800000190734863)
    Kill(3010831, award_souls=True)
    DisableCharacter(3010831)
    DisableAnimations(3010831)
    SetNetworkUpdateRate(3010831, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    AwardItemLot(31411100, host_only=False)


@RestartOnRest(13015558)
def Event_13015558(_, character: int, destination: int, flag: int, model_point: int):
    """Event 13015558"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    MoveToEntity(
        character,
        destination=destination,
        model_point=model_point,
        destination_type=CoordEntityType.Character,
    )
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=10.0))
    SkipLinesIfConditionTrue(2, AND_1)
    Wait(5.0)
    Restart()
    WaitFrames(frames=5)
    Restart()


@RestartOnRest(13015559)
def Event_13015559(_, character: int, destination: int, flag: int, model_point: int):
    """Event 13015559"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    MoveToEntity(
        character,
        destination=destination,
        model_point=model_point,
        destination_type=CoordEntityType.Character,
    )
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=10.0))
    SkipLinesIfConditionTrue(2, AND_1)
    Wait(5.0)
    Restart()
    WaitFrames(frames=5)
    Restart()


@RestartOnRest(13015580)
def Event_13015580():
    """Event 13015580"""
    if FlagEnabled(13010890):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3012300))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3010830, 11021)
    AddSpecialEffect(3010830, 11023)
    WaitFrames(frames=190)
    Restart()


@RestartOnRest(13015581)
def Event_13015581():
    """Event 13015581"""
    if FlagEnabled(13010890):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3012310))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3010830))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3010831))
    AND_2.Add(AND_1)
    AND_2.Add(OR_1)
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3010830, 11022)
    WaitFrames(frames=190)
    Restart()


@RestartOnRest(13015585)
def Event_13015585():
    """Event 13015585"""
    if FlagEnabled(13010890):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3012300))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3012301))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3010831, 11031)
    AddSpecialEffect(3010831, 11032)
    WaitFrames(frames=150)
    Restart()


@RestartOnRest(13015590)
def Event_13015590(_, flag: int, character: int, tae_event_id: int):
    """Event 13015590"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id))
    
    EnableFlag(flag)


@RestartOnRest(13015810)
def Event_13015810():
    """Event 13015810"""
    DisableAI(3010800)
    DisableCharacter(3010800)
    DisableAnimations(3010800)
    DisableGravity(3010800)
    DisableGravity(3010801)
    DisableCharacterCollision(3010801)
    DisableGravity(3010802)
    DisableCharacterCollision(3010802)
    DisableAI(3010801)
    DisableCharacter(3010801)
    DisableAnimations(3010801)
    DisableAI(3010802)
    DisableCharacter(3010802)
    DisableAnimations(3010802)
    if FlagEnabled(13010800):
        return
    EnableCharacter(3010800)
    EnableCharacter(3010801)
    EnableAnimations(3010801)
    EnableCharacter(3010802)
    EnableAnimations(3010802)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(3010800, 700, loop=True, unknown2=1.0)
    AND_1.Add(FlagEnabled(13015805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3012830))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    ForceAnimation(3010800, 1700, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(3010800)
    EnableAnimations(3010800)
    EnableAI(3010800)
    SetNetworkUpdateRate(3010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ActivateMultiplayerBuffs(3010800)
    ActivateMultiplayerBuffs(3010801)
    ActivateMultiplayerBuffs(3010802)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=3,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(3010800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3010801, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3010802, authority_level=UpdateAuthority.Forced)
    EnableBossHealthBar(3010800, name=903160)


@RestartOnRest(13015811)
def Event_13015811():
    """Event 13015811"""
    if FlagEnabled(13010800):
        return
    EnableInvincibility(3010801)
    EnableInvincibility(3010802)
    AND_1.Add(HealthRatio(3010800) <= 0.699999988079071)
    AND_1.Add(Attacked(attacked_entity=3010800, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3010800, 20000, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(3010801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3010801)
    SetNetworkUpdateRate(3010802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(3010802)
    DisableInvincibility(3010801)
    DisableInvincibility(3010802)


@RestartOnRest(13015812)
def Event_13015812():
    """Event 13015812"""
    if FlagEnabled(13010800):
        return
    
    MAIN.Await(HealthRatio(3010800) <= 0.0)
    
    Wait(3.5)
    PlaySoundEffect(3010800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3010800))
    
    Wait(3.5)
    DisableBossHealthBar(3010800, name=903160)
    DisableObject(3011800)
    KillBoss(game_area_param_id=3010800)
    SetNetworkUpdateRate(3010800, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Kill(3010801)
    SetNetworkUpdateRate(3010801, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Kill(3010802)
    SetNetworkUpdateRate(3010802, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableFlag(13010800)
    EnableFlag(9308)
    EnableFlag(6308)


@RestartOnRest(13015815)
def Event_13015815():
    """Event 13015815"""
    if FlagEnabled(13010800):
        return
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(13015805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3012830))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=3160, locked_camera_id=3160)


@RestartOnRest(13015830)
def Event_13015830(_, character: int, seconds: float):
    """Event 13015830"""
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    if FlagEnabled(13010800):
        return
    if ThisEventSlotFlagEnabled():
        return
    EnableCharacter(character)
    ForceAnimation(character, 30000, loop=True, unknown2=1.0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3012830))
    
    Wait(seconds)
    ForceAnimation(character, 20000, wait_for_completion=True, unknown2=1.0)
    WaitFrames(frames=1)
    DisableCharacter(character)


@RestartOnRest(13015820)
def Event_13015820():
    """Event 13015820"""
    CommonFunc_20005800(
        0,
        flag=13010800,
        entity=3011800,
        region=3012801,
        flag_1=13015805,
        action_button_id=3011800,
        character=0,
        left=0,
        region_1=3012800,
    )
    CommonFunc_20005801(
        0,
        flag=13010800,
        entity=3011800,
        region=3012801,
        flag_1=13015805,
        action_button_id=3011800,
        flag_2=13015806,
    )
    CommonFunc_20001836(
        0,
        flag=13010800,
        flag_1=13015805,
        flag_2=13015806,
        flag_3=13015810,
        sound_id=3012803,
        sound_id_1=3012804,
        flag_4=13015811,
    )
    CommonFunc_20005820(0, flag=13010800, obj=3011800, model_point=3, left=0)
    CommonFunc_20005820(0, flag=13010800, obj=3011801, model_point=3, left=0)
    CommonFunc_20005810(0, flag=13010800, entity=3011800, target_entity=3012801, action_button_id=10000)
