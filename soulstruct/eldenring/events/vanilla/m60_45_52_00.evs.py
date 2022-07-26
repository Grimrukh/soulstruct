"""
Northeast Altus Plateau (SW) (SE)

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_45_52_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76314, asset=Assets.AEG099_060_9000)
    Event_1045522500()
    CommonFunc_90005870(0, character=Characters.DraconicTreeSentinel, name=903250600, npc_threat_level=12)
    CommonFunc_90005860(
        0,
        flag=1045520800,
        left=0,
        character=Characters.DraconicTreeSentinel,
        left_1=0,
        item_lot=30315,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.DraconicTreeSentinel, npc_threat_level=12, right=0)
    CommonFunc_9005811(0, flag=1045520800, asset=Assets.AEG099_001_9000, model_point=5, right=0)
    CommonFunc_90005251(0, character=Characters.GuardianGolem2, radius=70.0, seconds=0.0, animation_id=3006)
    Event_1045522200()
    CommonFunc_90005300(0, flag=1045520200, character=Characters.GuardianGolem0, item_lot=30360, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1045520202, character=Characters.GuardianGolem1, item_lot=30365, seconds=0.0, left=0)
    CommonFunc_90005251(0, character=Characters.WanderingNoble0, radius=100.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.WanderingNoble1, radius=100.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.WanderingNoble2, radius=100.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.WanderingNoble3, radius=100.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.WanderingNoble4, radius=100.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=1045520400,
        animation_id=30000,
        animation_id_1=20000,
        radius=33.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005560(0, flag=1045520600, asset=Assets.AEG099_635_9000, left=0)
    CommonFunc_90005683(0, flag=62315, asset=Assets.AEG099_055_1000, vfx_id=205, flag_1=78394, flag_2=78394)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=1045528600)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005780(
        0,
        flag=1045520800,
        summon_flag=1045522160,
        dismissal_flag=1045522161,
        character=Characters.Millicent,
        sign_type=20,
        region=1045522720,
        right=1042559208,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1045520800, flag_1=1045522160, flag_2=1045522161, character=Characters.Millicent)
    CommonFunc_90005783(
        0,
        flag=1045520800,
        flag_1=1045522160,
        flag_2=1045522161,
        character=Characters.Millicent,
        other_entity=1045522722,
        region=1045522721,
        left=0,
    )
    CommonFunc_90005780(
        0,
        flag=1045520800,
        summon_flag=1045522170,
        dismissal_flag=1045522171,
        character=Characters.GreatHornedTragoth,
        sign_type=20,
        region=1045522731,
        right=1045529250,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(
        0,
        flag=1045520800,
        flag_1=1045522170,
        flag_2=1045522171,
        character=Characters.GreatHornedTragoth,
    )
    CommonFunc_90005783(
        0,
        flag=1045520800,
        flag_1=1045522170,
        flag_2=1045522171,
        character=Characters.GreatHornedTragoth,
        other_entity=1045522730,
        region=1045522732,
        left=0,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1045520180,
        summon_flag=1045522181,
        dismissal_flag=1045522182,
        character=Characters.DungEater,
        sign_type=23,
        region=1045522180,
        region_1=1044522181,
        seconds=0.0,
        right_1=35009315,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=1045520180, flag_1=1045522181, flag_2=1045522182, character=Characters.DungEater)
    CommonFunc_90005792(
        0,
        flag=1045520180,
        flag_1=1045522181,
        flag_2=1045522182,
        character=Characters.DungEater,
        item_lot=113800,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1045520180,
        flag_1=1045522181,
        flag_2=1045522182,
        character=Characters.DungEater,
        other_entity=1045522180,
        region=0,
        left=0,
    )
    Event_1045520700()
    Event_1045520710()
    Event_1045520720()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045520700)
    DisableBackread(1045520701)
    DisableBackread(Characters.DungEater)


@RestartOnRest(1045522200)
def Event_1045522200():
    """Event 1045522200"""
    if FlagEnabled(1045520200):
        return
    AND_1.Add(AllPlayersInsideRegion(region=1045522182))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.GuardianGolem0, 8082)
    ClearTargetList(Characters.GuardianGolem0)


@RestartOnRest(1045522500)
def Event_1045522500():
    """Event 1045522500"""
    GotoIfFlagDisabled(Label.L0, flag=1045520500)
    DisableAsset(Assets.AEG099_002_9000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=1045522550)
    DeleteAssetVFX(Assets.AEG099_002_9000)
    CreateAssetVFX(Assets.AEG099_002_9000, vfx_id=101, model_point=1540)
    EnableNetworkFlag(1045522550)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9503, entity=Assets.AEG099_002_9000))
    AND_2.Add(FlagEnabled(182))
    AND_2.Add(FlagEnabled(105))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=20003, anchor_entity=Assets.AEG099_002_9000, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(1045520500)
    DeleteAssetVFX(Assets.AEG099_002_9000)
    DisableAsset(Assets.AEG099_002_9000)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteAssetVFX(Assets.AEG099_002_9000)
    CreateAssetVFX(Assets.AEG099_002_9000, vfx_id=101, model_point=1540)
    End()


@RestartOnRest(1045520700)
def Event_1045520700():
    """Event 1045520700"""
    EnableAssetInvulnerability(1045521700)
    DisableGravity(1045520700)
    DisableAnimations(1045520700)
    ForceAnimation(1045520700, 90101)
    Move(1045520700, destination=1045522700, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(1045520710)
def Event_1045520710():
    """Event 1045520710"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAllDisabled(flag_range=(1042559207, 1042559209))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4181, 4183)))
    AwaitConditionTrue(AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1042559207, 1042559209))
    End()


@RestartOnRest(1045520720)
def Event_1045520720():
    """Event 1045520720"""
    WaitFrames(frames=1)
    DisableFlag(1045529250)
    if FlagEnabled(1045520800):
        return
    if FlagEnabled(7606):
        return
    EnableFlag(1045529250)
    End()


@ContinueOnRest(150)
def Event_150():
    """Event 150"""
    CommonFunc_90005485(0, character=Characters.GuardianGolem1)
