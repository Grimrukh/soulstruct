"""
Land of Shadow 11-10 NE SW

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
    RegisterGrace(grace_flag=2046420000, asset=2046421950, enemy_block_distance=0.0)
    CommonFunc_900005580(0, flag=580600, asset=2046421602, flag_1=9146)
    Event_2046420700(
        0,
        character=2046420700,
        flag=4365,
        animation_id=90100,
        flag_1=4360,
        flag_2=4363,
        flag_3=4898,
        flag_4=2046422702,
    )
    CommonFunc_90005744(0, entity=2046420700, flag=2046422701, flag_1=2046429220, animation_id=90201)
    CommonFunc_90005749(0, character=2046420701, character_1=2046420700, flag=4365, flag_1=2046422702)
    Event_2046420710(
        0,
        character=2046420720,
        flag=4425,
        animation_id=90100,
        flag_1=4420,
        flag_2=4897,
        flag_3=2046422720,
    )
    Event_2046420711(
        0,
        flag=2046429376,
        flag_1=2046429356,
        flag_2=2046429206,
        flag_3=4897,
        flag_4=2046429375,
        flag_5=4425,
    )
    CommonFunc_90005749(0, character=2046420721, character_1=2046420720, flag=4425, flag_1=2046422720)
    CommonFunc_90005750(
        0,
        asset=2046421721,
        action_button_id=4350,
        item_lot=106010,
        first_flag=400602,
        last_flag=400602,
        flag=2046429375,
        vfx_id=6102,
    )
    CommonFunc_90005748(0, entity=2046421720, action_button_id=206020, text=1030022, display_distance=30.0, flag=4912)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005430(0, character=2246420300)
    CommonFunc_90005432(0, character=2246420300, flag=2246422300)
    CommonFunc_90005435(
        0,
        character=2246420300,
        flag=2246422301,
        flag_1=2246422302,
        flag_2=2246422303,
        flag_3=2246422304,
    )
    CommonFunc_90005433(0, character=2246420300, flag=2246422305, flag_1=2246422306, flag_2=2246422307)
    CommonFunc_90005434(0, character=2246420300, flag=2246422305, flag_1=2246422306, flag_2=2246422307)
    CommonFunc_90005437(0, character=2246420300, flag=2246422308, flag_1=2246422309)
    CommonFunc_90005301(0, flag=2046420300, character=2246420300, item_lot__unk1=2046420980, seconds=4.0, unk1=0)


@RestartOnRest(2046420700)
def Event_2046420700(
    _,
    character: uint,
    flag: Flag | int,
    animation_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """Event 2046420700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(7, flag_4)
    SkipLinesIfFlagEnabled(6, flag_3)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    ForceAnimation(character, animation_id)
    SetTeamType(character, TeamType.NoTeam)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(not OR_3)
    
    Restart()


@RestartOnRest(2046420710)
def Event_2046420710(
    _,
    character: uint,
    flag: Flag | int,
    animation_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 2046420710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(7, flag_3)
    SkipLinesIfFlagEnabled(6, flag_2)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    ForceAnimation(character, animation_id)
    SetTeamType(character, TeamType.NoTeam)
    if FlagEnabled(flag_2):
        EnableFlag(flag_3)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_3.Add(FlagEnabled(flag))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(2046420711)
def Event_2046420711(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 2046420711"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag)
    AND_2.Add(FlagEnabled(flag_3))
    AND_2.Add(FlagEnabled(flag_5))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_4)
