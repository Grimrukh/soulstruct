"""
Land of Shadow 12-10 NW SW

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2048420000, asset=2048421950, enemy_block_distance=0.0)
    CommonFunc_90005201(
        0,
        character=2048420200,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2048420202,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005557(0, entity=2048421680)
    CommonFunc_90005557(0, entity=2048421681)
    CommonFunc_90005557(0, entity=2048421682)
    CommonFunc_90005557(0, entity=2048421683)
    CommonFunc_90005557(0, entity=2048421684)
    CommonFunc_90005557(0, entity=2048421685)
    CommonFunc_90005557(0, entity=2048421686)
    CommonFunc_90005557(0, entity=2048421687)
    CommonFunc_90005557(0, entity=2048421688)
    CommonFunc_90005556(0, asset=2048421689, flag=2048427900)
    Event_2048420700(
        0,
        character=2048420700,
        flag=4260,
        flag_1=4261,
        flag_2=4262,
        flag_3=4263,
        flag_4=4265,
        flag_5=2048429202,
        distance=70.0,
        flag_6=2048422703,
        flag_7=2048422704,
        animation_id=90100,
        animation_id_1=90101,
        flag_8=2048429222,
        flag_9=2048429223,
    )
    Event_2048420702(
        0,
        flag=4265,
        flag_1=2048429210,
        flag_2=2048429211,
        flag_3=2048422703,
        flag_4=2048422704,
        first_flag=2048429212,
        last_flag=2048429216,
        flag_5=4261,
    )
    Event_2048420703(0, flag=2048422707, flag_1=4265, flag_2=2048422706, seconds=20.0, flag_3=2048422703)
    Event_2048420703(1, flag=2048422708, flag_1=4265, flag_2=2048422706, seconds=20.0, flag_3=2048422704)
    CommonFunc_90005703(
        0,
        character=2048420700,
        flag=4261,
        flag_1=4262,
        flag_2=2048429201,
        flag_3=4261,
        first_flag=4260,
        last_flag=4264,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=2048420700, flag=4261, flag_1=4260, flag_2=2048429201, right=3)
    CommonFunc_90005702(0, character=2048420700, flag=4263, first_flag=4260, last_flag=4264)
    Event_2048420701(
        0,
        flag=4265,
        flag_1=4261,
        flag_2=2048422703,
        flag_3=2048422704,
        animation_id=90403,
        animation_id_1=90404,
        attacked_entity=2048420700,
        flag_4=4263,
        radius=7.0,
        seconds=2.0,
    )


@RestartOnRest(2048420700)
def Event_2048420700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    distance: float,
    flag_6: Flag | int,
    flag_7: Flag | int,
    animation_id: int,
    animation_id_1: int,
    flag_8: Flag | int,
    flag_9: Flag | int,
):
    """Event 2048420700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DisableFlag(flag_9)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DisableFlag(flag_5)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L0, flag=flag_4)
    
    MAIN.Await(FlagEnabled(flag_4))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=flag_8)
    OR_3.Add(FlagEnabled(flag_6))
    OR_3.Add(FlagEnabled(flag_7))
    
    MAIN.Await(OR_3)
    
    WaitRealFrames(frames=1)
    EnableCharacter(character)
    EnableBackread(character)
    AND_5.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_5)
    
    ResetCharacterPosition(character=character)
    if FlagEnabled(flag_6):
        ForceAnimation(character, animation_id, loop=True)
    if FlagEnabled(flag_7):
        ForceAnimation(character, animation_id_1, loop=True)
    SetCharacterTalkRange(character=character, distance=distance)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, animation_id, loop=True)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, animation_id, loop=True)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_4))
    OR_10.Add(FlagEnabled(flag_9))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(2048420701)
def Event_2048420701(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    animation_id: int,
    animation_id_1: int,
    attacked_entity: uint,
    flag_4: Flag | int,
    radius: float,
    seconds: float,
):
    """Event 2048420701"""
    WaitFrames(frames=2)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_4):
        return
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=attacked_entity, radius=radius))
    AND_2.Add(TimeElapsed(seconds=seconds))
    OR_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_10.Add(AND_2)
    AND_1.Add(OR_10)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag_2):
        ForceAnimation(attacked_entity, animation_id, loop=True)
    if FlagEnabled(flag_3):
        ForceAnimation(attacked_entity, animation_id_1, loop=True)
    Wait(5.5)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_13)
    
    if FlagEnabled(flag_2):
        ForceAnimation(attacked_entity, animation_id, loop=True)
    if FlagEnabled(flag_3):
        ForceAnimation(attacked_entity, animation_id_1, loop=True)
    Wait(5.5)
    Restart()


@RestartOnRest(2048420702)
def Event_2048420702(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_5: Flag | int,
):
    """Event 2048420702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    GotoIfFlagEnabled(Label.L1, flag=flag_5)
    AND_1.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagDisabled(flag_2))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_3)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_4)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlagRange((first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    if FlagEnabled(last_flag):
        EnableFlag(flag_4)
        End()
    EnableFlag(flag_3)
    End()


@RestartOnRest(2048420703)
def Event_2048420703(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, seconds: float, flag_3: Flag | int):
    """Event 2048420703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L10, flag=flag_1)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_2))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag):
        return
    Wait(seconds)
    DisableFlag(flag_2)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()
