"""
Land of Shadow 11-10 NW SE

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
    RegisterGrace(grace_flag=2045420000, asset=2045421950, enemy_block_distance=0.0)
    CommonFunc_90005221(0, character=2048430214, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430216, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430223, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430225, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430228, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430229, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2048430231, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005639(0, flag=2045420500, asset=2045421500, asset_1=2045421501, asset_2=2045421502, seconds=0.0)
    CommonFunc_900005580(0, flag=580600, asset=2045421602, flag_1=9146)
    Event_2045420700(
        0,
        character=2045420700,
        flag=4400,
        flag_1=4405,
        animation_id=90100,
        flag_2=4899,
        flag_3=4928,
        flag_4=2045429205,
        flag_5=2045429207,
        flag_6=2045422701,
    )
    CommonFunc_90005749(0, character=2045420701, character_1=2045420700, flag=4405, flag_1=2045422701)
    Event_2045420705(
        0,
        character=2045420710,
        flag=4380,
        flag_1=4383,
        flag_2=4385,
        animation_id=90102,
        flag_3=4901,
        flag_4=4382,
        asset=2045421711,
        flag_5=2045422711,
    )
    CommonFunc_90005749(0, character=2045420711, character_1=2045420710, flag=4385, flag_1=2045422711)
    CommonFunc_90005744(0, entity=2045420710, flag=2045429268, flag_1=2045429268, animation_id=90200)
    CommonFunc_90005744(0, entity=2045420710, flag=2045429272, flag_1=2045429272, animation_id=90200)
    Event_2045420706(
        0,
        character=2045420710,
        flag=4382,
        flag_1=4386,
        animation_id=90202,
        animation_id_1=90203,
        radius=3.0,
    )
    CommonFunc_90005750(
        0,
        asset=2045421710,
        action_button_id=4350,
        item_lot=106420,
        first_flag=400644,
        last_flag=400644,
        flag=2045429280,
        vfx_id=6102,
    )
    CommonFunc_90005748(0, entity=2045421700, action_button_id=206022, text=1030023, display_distance=30.0, flag=4913)
    Event_2045420701(0, entity=2045420700, flag=2045422708, flag_1=4405, flag_2=4899)


@RestartOnRest(2045420700)
def Event_2045420700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 2045420700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableInvincibility(character)
    DisableFlag(flag_4)
    AND_5.Add(FlagEnabled(flag_2))
    SkipLinesIfConditionFalse(1, AND_5)
    Goto(Label.L20)
    AND_6.Add(FlagEnabled(flag_3))
    SkipLinesIfConditionFalse(1, AND_6)
    Goto(Label.L20)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=flag_6)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    ForceAnimation(character, animation_id)
    if FlagEnabled(flag_5):
        EnableFlag(flag_4)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_1))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(2045420705)
def Event_2045420705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    animation_id: int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    asset: Asset | int,
    flag_5: Flag | int,
):
    """Event 2045420705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableAssetInvulnerability(asset)
    AND_1.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L3, flag=flag_4)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=flag_5)
    if FlagDisabled(flag_3):
        EnableCharacter(character)
        EnableBackread(character)
        AND_5.Add(CharacterBackreadEnabled(character))
    
        MAIN.Await(AND_5)
    
        ResetCharacterPosition(character=character)
    WaitRealFrames(frames=1)
    Move(character, destination=2045422710, destination_type=CoordEntityType.Region, short_move=True)
    SetTeamType(character, TeamType.NoTeam)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id, loop=True)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_3.Add(FlagEnabled(flag_2))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(2045420706)
def Event_2045420706(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
):
    """Event 2045420706"""
    WaitFrames(frames=2)
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    if OR_1:
        return
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id, wait_for_completion=True)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    Restart()


@RestartOnRest(2045420701)
def Event_2045420701(_, entity: uint, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2045420701"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_10)
    
    WaitRealFrames(frames=1)
    if FlagEnabled(flag_2):
        return
    GotoIfFlagDisabled(Label.L1, flag=flag)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=2.5999999046325684))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(EntityBeyondDistance(entity=entity, other_entity=PLAYER, radius=2.5999999046325684))
    
    MAIN.Await(AND_2)
    
    DisableFlag(flag)
    Restart()
