"""
Land of Shadow 12-10 NW NW

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
    RegisterGrace(grace_flag=2048430000, asset=2048431950, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=2048430001, asset=2048431951)
    CommonFunc_90005250(0, character=2048430310, region=2048432300, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2048430300, region=2048432300, seconds=4.0, animation_id=0)
    CommonFunc_90005221(0, character=2048430200, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430202, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430203, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430209, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430211, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_900005580(0, flag=580600, asset=2048431602, flag_1=9146)
    Event_2048430700(
        0,
        character=2048430700,
        flag=4460,
        flag_1=4463,
        flag_2=4465,
        distance=30.0,
        animation_id=90100,
        flag_3=4900,
        left=2048432700,
        flag_4=2048432706,
    )
    CommonFunc_90005749(0, character=2048430701, character_1=2048430700, flag=4465, flag_1=2048432706)
    Event_2048430701(
        0,
        flag=4465,
        flag_1=4460,
        flag_2=2048439213,
        flag_3=2048439207,
        flag_4=2048439208,
        max_value__value=2,
    )
    CommonFunc_90005744(0, entity=2048430700, flag=2048439217, flag_1=2048439217, animation_id=90200)
    CommonFunc_90005748(0, entity=2048431700, action_button_id=206020, text=1030027, display_distance=30.0, flag=4917)


@RestartOnRest(2048430700)
def Event_2048430700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    animation_id: int,
    flag_3: Flag | int,
    left: uint,
    flag_4: Flag | int,
):
    """Event 2048430700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableInvincibility(character)
    if FlagEnabled(flag_3):
        return
    OR_1.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=flag_4)
    EnableCharacter(character)
    EnableBackread(character)
    SetCharacterTalkRange(character=character, distance=distance)
    ForceAnimation(character, animation_id)
    AND_5.Add(CharacterBackreadEnabled(character))
    AND_5.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_5)
    
    WaitRealFrames(frames=1)
    if UnsignedEqual(left=left, right=0):
        ResetCharacterPosition(character=character)
    else:
        Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(flag_2))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(2048430701)
def Event_2048430701(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    max_value__value: uint,
):
    """Event 2048430701"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    if FlagDisabled(flag_1):
        return
    if FlagDisabled(flag_2):
        return
    if FlagEnabled(flag_3):
        return
    IncrementEventValue(flag_4, bit_count=4, max_value=max_value__value)
    AND_1.Add(EventValue(flag=flag_4, bit_count=4) < max_value__value)
    SkipLinesIfConditionTrue(1, AND_1)
    EnableFlag(flag_3)
    End()


@RestartOnRest(2048430705)
def Event_2048430705(
    _,
    character: uint,
    character_1: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 2048430705"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableFlag(flag_2)
    End()
    GotoIfFlagDisabled(Label.L20, flag=flag_3)
    GotoIfFlagEnabled(Label.L20, flag=flag_4)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_5))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(flag_1):
        EnableCharacter(character)
        ForceAnimation(character, 30007)
        End()
    EnableCharacter(character_1)
    ForceAnimation(character_1, 30008)
    SetTeamType(character_1, TeamType.NoTeam)
    DisableAnimations(character_1)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    End()
