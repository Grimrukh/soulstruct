"""
Land of Shadow 11-11 NE SE

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
    CommonFunc_90005754(
        0,
        flag=4871,
        first_flag=4870,
        last_flag=4874,
        flag_1=4876,
        region=2047462701,
        flag_2=2047460180,
        flag_3=4343,
        right=4860,
        character=2047460700,
        right_1=2047462181,
        distance=100.0,
        flag_4=2047462182,
        right_2=2047462185,
        flag_5=2047462186,
        right_3=2047462702,
    )
    CommonFunc_90005755(0, flag=4871, flag_1=4876, right=0, flag_2=4860, flag_3=4861, max_value__value=2)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2047460180,
        summon_flag=2047462181,
        dismissal_flag=2047462182,
        character=2047460700,
        sign_type=22,
        region=2047462700,
        region_1=2047462701,
        seconds=0.0,
        right_1=2047462702,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2047460180, flag_1=2047462181, flag_2=2047462182, character=2047460700)
    CommonFunc_90005792(
        0,
        flag=2047460180,
        flag_1=2047462181,
        flag_2=2047462182,
        character=2047460700,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2047460180,
        flag_1=2047462181,
        flag_2=2047462182,
        character=2047460700,
        other_entity=2047462700,
        region=2047462182,
        left=0,
    )
    CommonFunc_90005768(
        0,
        flag=2047460180,
        item_lot=106920,
        flag_1=400694,
        item_lot_1=106930,
        flag_2=400696,
        flag_3=4860,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=2047460184,
        summon_flag=2047462185,
        dismissal_flag=2047462186,
        character=2047460720,
        sign_type=22,
        region=2047462720,
        region_1=2047462721,
        seconds=0.0,
        right_1=2045429296,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2047460184, flag_1=2047462185, flag_2=2047462186, character=2047460720)
    CommonFunc_90005792(
        0,
        flag=2047460184,
        flag_1=2047462185,
        flag_2=2047462186,
        character=2047460720,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2047460184,
        flag_1=2047462185,
        flag_2=2047462186,
        character=2047460720,
        other_entity=2047462720,
        region=0,
        left=0,
    )
    CommonFunc_90005774(0, flag=2047460184, item_lot=116401, flag_1=400645)
    Event_2047460705(
        0,
        character=2047460710,
        character_1=2047460711,
        flag=4385,
        flag_1=4956,
        flag_2=2045422710,
        flag_3=4383,
        flag_4=4386,
        destination=2047462730,
    )
    Event_2047460706(
        0,
        character=2047460710,
        special_effect=3360,
        flag=4956,
        flag_1=4959,
        seconds=3.0,
        animation_id=20010,
        special_effect_1=20503310,
    )
    Event_2047460707(0, flag=2047462710, flag_1=4956, flag_2=400755, attacked_entity=2047460710, flag_3=4959)
    CommonFunc_90005779(0, character=2047460710, flag=4956, animation_id=20016, flag_1=4385, flag_2=4383)
    CommonFunc_90005744(0, entity=2047460710, flag=2047469250, flag_1=2047469250, animation_id=20015)
    Event_2047460709(
        0,
        flag=2045429280,
        flag_1=4385,
        flag_2=4966,
        character=2047460710,
        flag_3=4956,
        flag_4=2045429296,
        first_flag=4950,
        last_flag=4956,
        flag_5=2045429281,
        flag_6=2045429282,
        flag_7=4901,
        seconds=1.0,
        flag_8=2045429346,
        radius=30.0,
    )
    CommonFunc_90005766(0, flag=2047462185, character=2047460720, distance=100.0, flag_1=2045429277, flag_2=4966)
    CommonFunc_90005767(
        0,
        flag=2045429280,
        first_flag=4380,
        last_flag=4383,
        character=2047460720,
        flag_1=4901,
        character_1=2047460721,
        flag_2=2045429297,
    )
    CommonFunc_90005777(0, character=2047460721, flag=4966, flag_1=4383, flag_2=2047462185)
    CommonFunc_90005774(0, flag=2045429297, item_lot=116401, flag_1=400645)
    Event_2047460708(
        0,
        character=2047460730,
        flag=4380,
        flag_1=4383,
        flag_2=4386,
        animation_id=90101,
        flag_3=2047462730,
    )
    CommonFunc_90005750(
        0,
        asset=2047461730,
        action_button_id=4350,
        item_lot=106420,
        first_flag=400644,
        last_flag=400645,
        flag=4386,
        vfx_id=6102,
    )
    Event_2047460700(
        0,
        region=2047462701,
        flag=2047462701,
        flag_1=2047460180,
        flag_2=2047462182,
        flag_3=4860,
        seconds=6.0,
        flag_4=2047462181,
        first_flag=4870,
        last_flag=4874,
        flag_5=4871,
        flag_6=2047462185,
        flag_7=2047462186,
        flag_8=2047462703,
    )
    CommonFunc_90005737(0, flag=2047460180, flag_1=2047462703)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005485(0, character=2247460200)
    CommonFunc_90005485(0, character=2247460201)
    CommonFunc_90005251(0, character=2247460200, radius=340.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2247460201, radius=340.0, seconds=0.0, animation_id=-1)


@RestartOnRest(2047460700)
def Event_2047460700(
    _,
    region: Region | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds: float,
    flag_4: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
):
    """Event 2047460700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_4.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_4.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    OR_4.Add(FlagEnabled(flag_5))
    AND_4.Add(OR_4)
    OR_5.Add(FlagDisabled(flag_6))
    AND_5.Add(FlagEnabled(flag_6))
    AND_5.Add(FlagEnabled(flag_7))
    OR_5.Add(AND_5)
    AND_4.Add(OR_5)
    AND_4.Add(FlagDisabled(flag_8))
    
    MAIN.Await(AND_4)
    
    WaitFrames(frames=1)
    AND_1.Add(EventValue(flag=flag_3, bit_count=4) == 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_2)
    
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(FlagEnabled(flag_4))
    OR_3.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_3)
    
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    if FlagEnabled(flag_2):
        return
    EnableFlag(flag)
    End()


@RestartOnRest(2047460705)
def Event_2047460705(
    _,
    character: uint,
    character_1: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    destination: uint,
):
    """Event 2047460705"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableGravity(character)
    DisableGravity(character_1)
    DisableCharacterCollision(character)
    DisableCharacterCollision(character_1)
    EnableFlag(flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_4)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_3))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(4959))
    AND_1.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagEnabled(4959))
    AND_2.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(FlagEnabled(flag_1))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableHealthBar(character)
    EnableCharacter(character)
    AddSpecialEffect(character, 4409)
    ForceAnimation(character, 30012)
    Wait(1.0)
    EnableHealthBar(character)
    ResetCharacterPosition(character=character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    ForceAnimation(character, 30007)
    Wait(1.0)
    ResetCharacterPosition(character=character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 30008)
    SetTeamType(character_1, TeamType.NoTeam)
    DisableAnimations(character_1)
    Wait(1.0)
    ResetCharacterPosition(character=character_1)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 30008)
    SetTeamType(character_1, TeamType.NoTeam)
    DisableAnimations(character_1)
    AND_5.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_5)
    
    WaitRealFrames(frames=1)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(2047460706)
def Event_2047460706(
    _,
    character: uint,
    special_effect: int,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    animation_id: int,
    special_effect_1: int,
):
    """Event 2047460706"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    if OR_1:
        return
    OR_2.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_2.Add(CharacterHasSpecialEffect(character, special_effect_1))
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    if FlagEnabled(flag):
        return
    EnableFlag(flag_1)
    ForceAnimation(character, animation_id)


@RestartOnRest(2047460707)
def Event_2047460707(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    attacked_entity: Character | int,
    flag_3: Flag | int,
):
    """Event 2047460707"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    EnableFlag(flag)
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    if FlagDisabled(flag_3):
        return
    DisableFlag(flag)
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_6.Add(FlagEnabled(flag_1))
    OR_6.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_6)
    
    EnableFlag(flag)


@RestartOnRest(2047460708)
def Event_2047460708(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    animation_id: int,
    flag_3: uint,
):
    """Event 2047460708"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(flag_3):
        EnableCharacter(character)
        EnableBackread(character)
        SetTeamType(character, TeamType.NoTeam)
    AND_5.Add(CharacterBackreadEnabled(character))
    AND_5.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_5)
    
    ResetCharacterPosition(character=character)
    WaitRealFrames(frames=1)
    Move(character, destination=flag_3, destination_type=CoordEntityType.Region, short_move=True)
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


@RestartOnRest(2047460709)
def Event_2047460709(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: uint,
    flag_3: Flag | int,
    flag_4: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    seconds: float,
    flag_8: Flag | int,
    radius: float,
):
    """Event 2047460709"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    GotoIfFlagEnabled(Label.L10, flag=flag_8)
    GotoIfFlagDisabled(Label.L0, flag=flag_8)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_3):
        return
    OR_1.Add(CharacterProportionDead(character=character))
    OR_1.Add(HealthValue(character) <= 0)
    OR_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_3)
    OR_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 1)
    SkipLinesIfConditionFalse(1, OR_2)
    EnableFlag(flag_5)
    OR_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 2)
    SkipLinesIfConditionFalse(6, OR_3)
    EnableFlag(flag_6)
    if FlagEnabled(flag_7):
        return
    EnableFlag(flag_8)
    OR_10.Add(FlagDisabled(2047462181))
    OR_10.Add(FlagEnabled(2047460180))
    AND_10.Add(FlagEnabled(2047462181))
    AND_10.Add(FlagEnabled(2047462182))
    OR_10.Add(AND_10)
    
    MAIN.Await(OR_10)
    
    Wait(seconds)
    EnableFlag(flag_4)
    AND_5.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_5)
    
    DisableFlag(flag_8)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    OR_13.Add(FlagDisabled(2047462181))
    OR_13.Add(FlagEnabled(2047460180))
    AND_13.Add(FlagEnabled(2047462181))
    AND_13.Add(FlagEnabled(2047462182))
    OR_13.Add(AND_13)
    
    MAIN.Await(OR_13)
    
    WaitRealFrames(frames=1)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    if FlagEnabled(flag_7):
        return
    EnableFlag(flag_4)
    AND_5.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_5)
    
    DisableFlag(flag_8)
    End()
