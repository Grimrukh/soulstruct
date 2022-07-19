"""
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
from .entities.m60_40_54_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=76307, asset=Assets.AEG099_060_9000, enemy_block_distance=5.0, character=0)
    CommonFunc_90005100(
        0,
        flag=71602,
        flag_1=76307,
        asset=Assets.AEG099_060_9001,
        source_flag=77350,
        value=0,
        flag_2=78350,
        flag_3=78351,
        flag_4=78352,
        flag_5=78353,
        flag_6=78354,
        flag_7=78355,
        flag_8=78356,
        flag_9=78357,
        flag_10=78358,
        flag_11=78359,
    )
    CommonFunc_90005300(0, flag=1040540500, character=Characters.Scarab, item_lot_param_id=40312, seconds=0.0, left=0)
    Event_1040542700(0, character=Characters.BrotherCorhyn)
    CommonFunc_90005704(0, attacked_entity=Characters.BrotherCorhyn, flag=4201, flag_1=4200, flag_2=1040549201, right=3)
    CommonFunc_90005703(0, 1040540705, 4201, 4202, 1040549201, 4201, 4200, 4204, -1)
    CommonFunc_90005702(0, character=Characters.BrotherCorhyn, flag=4203, first_flag=4200, last_flag=4204)
    Event_1040542705(0, character=Characters.Goldmask)
    Event_1040542706(0, character=Characters.Goldmask)
    CommonFunc_90005706(0, 1040540710, 30023, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Goldmask)
    DisableBackread(Characters.BrotherCorhyn)
    DisableBackread(1040540710)
    CommonFunc_90005261(0, character=1040540270, region=1040542270, radius=20.0, seconds=0.0, animation_id=0)
    Event_1040542201(0, character=Characters.LeyndellSoldier3, patrol_information_id=1040543250)
    Event_1040542201(1, character=Characters.LeyndellSoldier4, patrol_information_id=1040543251)
    Event_1040542201(2, character=Characters.LeyndellFootSoldier6, patrol_information_id=1040543252)
    Event_1040542201(3, character=Characters.LeyndellFootSoldier7, patrol_information_id=1040543253)
    Event_1040542201(4, character=1040540254, patrol_information_id=1040543254)
    CommonFunc_90005201(
        0,
        character=Characters.MadPumpkinHead1,
        animation_id=30005,
        animation_id_1=20005,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1040540340, 0.0, 0.0, -1)
    CommonFunc_90005201(0, 1040540402, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005424(
        0,
        asset=Assets.AEG100_100_9001,
        character=Characters.Troll0,
        character_1=Characters.Troll1,
        character_2=Characters.CaravanDummy,
        asset_1=Assets.AEG100_101_9001,
    )
    Event_1040542301()
    CommonFunc_90005423(0, character=Characters.Troll0)
    CommonFunc_90005423(0, character=Characters.Troll1)
    Event_1040542300()
    Event_1040542210(0, character=Characters.MadPumpkinHead0, patrol_information_id=1040542330)
    Event_1040542210(1, character=Characters.LeyndellFootSoldier1, patrol_information_id=1040542310)
    Event_1040542210(2, character=Characters.LeyndellFootSoldier2, patrol_information_id=1040542311)
    Event_1040542210(3, character=Characters.LeyndellFootSoldier3, patrol_information_id=1040542312)
    Event_1040542210(4, character=1040540313, patrol_information_id=1040542313)
    Event_1040542210(5, character=Characters.LeyndellSoldier1, patrol_information_id=1040542314)
    Event_1040542210(6, character=Characters.LeyndellSoldier0, patrol_information_id=1040542315)
    Event_1040542210(7, 1040540316, 1040542316)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005420(0, 1040540300, 1040541300, 1040541301, 1040540301, 1040540302, 1040540303, 0.0)


@RestartOnRest(1040542201)
def Event_1040542201(_, character: uint, patrol_information_id: uint):
    """Event 1040542201"""
    if FlagEnabled(1040542201):
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.Dummy, region=1040542301))
    
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableFlag(1040542201)
    End()


@RestartOnRest(1040542210)
def Event_1040542210(_, character: uint, patrol_information_id: uint):
    """Event 1040542210"""
    if FlagEnabled(1040542210):
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.Dummy, region=1040542309))
    
    AddSpecialEffect(Characters.Dummy, 5555)
    Wait(1.0)
    AddSpecialEffect(character, 5002)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableFlag(1040542210)
    End()


@RestartOnRest(1040542300)
def Event_1040542300():
    """Event 1040542300"""
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=150,
        behavior_param_id=100700,
        target_type=DamageTargetType.Character,
        radius=3.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=200,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=201,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=202,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=203,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=204,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1040541301,
        asset=Assets.AEG100_100_9001,
        model_point=205,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )


@RestartOnRest(1040542301)
def Event_1040542301():
    """Event 1040542301"""
    if FlagEnabled(1040542301):
        return
    
    MAIN.Await(CharacterDead(1040540390))
    
    AwaitConditionTrue(MAIN)
    Kill(Characters.Dummy)
    End()


@RestartOnRest(1040542700)
def Event_1040542700(_, character: uint):
    """Event 1040542700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4200):
        DisableFlag(1040529253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(4208))
    AND_1.Add(FlagEnabled(1040549254))
    OR_1.Add(FlagEnabled(4207))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    AND_2.Add(FlagEnabled(4208))
    AND_2.Add(FlagEnabled(1040549254))
    OR_2.Add(FlagEnabled(4207))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagEnabled(4208))
    AND_15.Add(FlagEnabled(1040549254))
    OR_15.Add(FlagEnabled(4207))
    OR_15.Add(AND_15)
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1040542705)
def Event_1040542705(_, character: uint):
    """Event 1040542705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4205))
    OR_1.Add(FlagEnabled(4206))
    OR_1.Add(FlagEnabled(4207))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(4203))
    AND_2.Add(FlagDisabled(4217))
    AND_2.Add(FlagEnabled(4203))
    AND_2.Add(FlagDisabled(11009554))
    AND_2.Add(FlagDisabled(1051569454))
    AND_2.Add(FlagDisabled(11059304))
    AND_3.Add(FlagEnabled(1040549254))
    AND_3.Add(FlagDisabled(4217))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930000)
    EnableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagEnabled(4205))
    OR_10.Add(FlagEnabled(4206))
    OR_10.Add(FlagEnabled(4207))
    AND_10.Add(OR_10)
    AND_10.Add(FlagDisabled(4203))
    AND_11.Add(FlagDisabled(4217))
    AND_11.Add(FlagEnabled(4203))
    AND_11.Add(FlagDisabled(11009554))
    AND_11.Add(FlagDisabled(1051569454))
    AND_11.Add(FlagDisabled(11059304))
    AND_12.Add(FlagEnabled(1040549254))
    AND_12.Add(FlagDisabled(4217))
    OR_11.Add(AND_10)
    OR_11.Add(AND_11)
    OR_11.Add(AND_12)
    
    MAIN.Await(not OR_11)
    
    Restart()


@RestartOnRest(1040542706)
def Event_1040542706(_, character: uint):
    """Event 1040542706"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    EnableImmortality(character)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    EnableNetworkFlag(1040542710)
    ForceAnimation(character, 20010, wait_for_completion=True, skip_transition=True)
    End()
