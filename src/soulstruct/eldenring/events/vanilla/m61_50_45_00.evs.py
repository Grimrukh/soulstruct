"""
Land of Shadow 12-11 SE NW

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
    RegisterGrace(grace_flag=2050450000, asset=2050451950)
    CommonFunc_90005251(0, character=2050450200, radius=25.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=2050450390, character=2050450390, item_lot=40900, seconds=0.0, left=0)
    CommonFunc_90005570(0, flag=60864, gesture_param_id=115, asset=2050451680, left=2, left_1=2, right=0)
    Event_2050450700(
        0,
        character=2050450700,
        flag=4500,
        flag_1=4505,
        flag_2=2051459725,
        flag_3=2051452719,
        flag_4=2051459210,
        animation_id=90102,
        distance=55.0,
    )
    Event_2050450701(
        0,
        entity=2050451700,
        action_button_id=206040,
        text=1030030,
        display_distance=30.0,
        left=0,
        flag=2051452719,
        flag_1=4505,
        flag_2=2051459725,
    )
    CommonFunc_90005750(
        0,
        asset=2050451701,
        action_button_id=4350,
        item_lot=106650,
        first_flag=400666,
        last_flag=400666,
        flag=2051450800,
        vfx_id=0,
    )


@RestartOnRest(2050450700)
def Event_2050450700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    animation_id: int,
    distance: float,
):
    """Event 2050450700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)
    SetCharacterTalkRange(character=character, distance=17.0)
    if FlagEnabled(flag_1):
        GotoIfFlagEnabled(Label.L20, flag=flag_2)
    AND_8.Add(FlagEnabled(flag_1))
    AND_8.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L0, input_condition=AND_8)
    
    MAIN.Await(AND_8)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableInvincibility(character)
    WaitRealFrames(frames=1)
    AND_5.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_5)
    
    Move(character, destination=2050452717, destination_type=CoordEntityType.Region, short_move=True)
    WaitRealFrames(frames=1)
    EnableFlag(flag_4)
    ForceAnimation(character, animation_id)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetCharacterTalkRange(character=character, distance=distance)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_3.Add(FlagDisabled(flag_1))
    OR_3.Add(FlagDisabled(flag_3))
    
    MAIN.Await(OR_3)
    
    Restart()


@RestartOnRest(2050450701)
def Event_2050450701(
    _,
    entity: uint,
    action_button_id: int,
    text: EventText | int,
    display_distance: float,
    left: Flag | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 2050450701"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag_2))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagDisabled(flag_2))
    if AND_3:
        return RESTART
    DisplayDialog(text=text, display_distance=display_distance, button_type=ButtonType.Yes_or_No)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    Wait(1.0)
    Restart()
