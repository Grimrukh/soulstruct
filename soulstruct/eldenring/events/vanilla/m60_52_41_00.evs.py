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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052410000, obj=1052411950, unknown=5.0)
    Event_1052412220()
    Event_1052412270()
    Event_1052412270(slot=1)
    Event_1052412200(0, character=1052410210, obj=1052411210, region=1052412210)
    RunCommonEvent(0, 90005300, args=(1052410850, 1052410851, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005476, args=(1052410850, 1052410851), arg_types="II")
    Event_1052412291(0, character=1052410850, character_1=1052410851)
    RunCommonEvent(0, 90005871, args=(1052410850, 903150606, 10, 1052410851), arg_types="IiII")
    RunCommonEvent(0, 90005860, args=(1052410850, 0, 1052410850, 0, 1052410100, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1052410850, 10, 0), arg_types="III")
    Event_1052412510()
    RunCommonEvent(
        0,
        90005501,
        args=(1052410510, 1052410511, 0, 1052411510, 1052411511, 1052411512, 1052410512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005870, args=(1052410800, 904500601, 25), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1052410800, 0, 1052410800, 1, 30420, 0.0), arg_types="IIIIif")
    Event_1052412230()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1052410519()


@RestartOnRest(1052412200)
def Event_1052412200(_, character: uint, obj: uint, region: uint):
    """Event 1052412200"""
    DisableCharacter(character)
    EndIfFlagEnabled(region)
    IfCharacterDead(AND_3, character)
    EndIfConditionTrue(input_condition=AND_3)
    DisableHealthBar(character)
    IfCharacterType(AND_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_2)
    CreateObjectVFX(obj, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    EnableNetworkFlag(region)
    Wait(2.0)
    DeleteObjectVFX(obj)
    ForceAnimation(character, 20001, unknown2=1.0)
    Wait(1.899999976158142)
    ForceAnimation(character, 20004, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(character, 20004, unknown2=1.0)
    Wait(1.0)
    DisableCharacter(character)
    Kill(character)
    End()


@RestartOnRest(1052412220)
def Event_1052412220():
    """Event 1052412220"""
    CreateObjectVFX(1052411200, vfx_id=200, model_point=1500)


@RestartOnRest(1052412230)
def Event_1052412230():
    """Event 1052412230"""
    Unknown_2004_84(character=1052410800, unk_4_8=220.0, unk_8_12=40.0)


@RestartOnRest(1052412291)
def Event_1052412291(_, character: uint, character_1: uint):
    """Event 1052412291"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterBackreadEnabled(AND_3, character_1)
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterBackreadDisabled(AND_4, character_1)
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@NeverRestart(1052412510)
def Event_1052412510():
    """Event 1052412510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1052410510,
            1052410511,
            0,
            1052411510,
            1052411511,
            1052413511,
            1052411512,
            1052413512,
            1052412511,
            1052412512,
            1052410512,
            1052410513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1052410519)
def Event_1052410519():
    """Event 1052410519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1052410510)


@RestartOnRest(1052412270)
def Event_1052412270():
    """Event 1052412270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1052410270)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=1052410270, radius=60.0)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=8.0)
    IfNewGameCycleEqual(AND_2, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_3, completion_count=1)
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_4, completion_count=2)
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_5, completion_count=3)
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_6, completion_count=4)
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_7, completion_count=5)
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_8, completion_count=6)
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleGreaterThanOrEqual(AND_10, completion_count=7)
    SkipLinesIfConditionFalse(2, AND_10)
    ShootProjectile(
        owner_entity=1052410270,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()
