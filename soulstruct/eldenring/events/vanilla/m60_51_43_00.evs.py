"""
North Caelid (NE) (NE)

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
from .entities.m60_51_43_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1051430000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005870(0, character=Characters.Gargoyle, name=904770600, npc_threat_level=16)
    CommonFunc_90005860(
        0,
        flag=1051430800,
        left=0,
        character=Characters.Gargoyle,
        left_1=0,
        item_lot=30425,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.Gargoyle, npc_threat_level=16, right=0)
    Event_1051432209()
    Event_1051432200(0, character=Characters.Gargoyle, radius=55.0, seconds=0.0, animation_id=-1)
    Event_1051430700(0, character=Characters.BeastClergyman)
    CommonFunc_90005703(
        0,
        character=Characters.BeastClergyman,
        flag=3641,
        flag_1=3642,
        flag_2=1051439201,
        flag_3=1051439212,
        first_flag=3640,
        last_flag=3643,
        right=-1,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.BeastClergyman,
        flag=1051439212,
        flag_1=3640,
        flag_2=1051439201,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.BeastClergyman, flag=3643, first_flag=3640, last_flag=3643)
    Event_1051430702(0, character=Characters.BeastClergyman, value=0.8999999761581421)
    Event_1051430703(0, character=Characters.BeastClergyman)


@RestartOnRest(1051432200)
def Event_1051432200(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1051432200"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(FlagDisabled(1051430210))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1051432209)
def Event_1051432209():
    """Event 1051432209"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.Gargoyle, radius=160.0))
    
    DisableNetworkFlag(1051430210)


@RestartOnRest(1051430700)
def Event_1051430700(_, character: uint):
    """Event 1051430700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3640):
        DisableFlag(1051439202)
        DisableFlag(1051439212)
    OR_2.Add(FlagEnabled(3645))
    OR_2.Add(FlagEnabled(3647))
    AND_2.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 30, 0)))
    AND_2.Add(EventValue(flag=1051439230, bit_count=5) >= 1)
    AND_2.Add(OR_2)
    GotoIfConditionFalse(Label.L4, input_condition=AND_2)
    DisableFlagRange((1051439240, 1051439249))
    EnableRandomFlagInRange(flag_range=(1051439240, 1051439249))
    SkipLinesIfFlagEnabled(1, 1051439220)
    SkipLinesIfFlagDisabled(1, 1051439240)
    EnableNetworkFlag(1051432703)

    # --- Label 4 --- #
    DefineLabel(4)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3645)
    GotoIfFlagEnabled(Label.L6, flag=3646)
    GotoIfFlagEnabled(Label.L7, flag=3647)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3645))
    OR_3.Add(FlagEnabled(3646))
    OR_3.Add(FlagEnabled(3647))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3640)
    GotoIfFlagEnabled(Label.L1, flag=3641)
    GotoIfFlagEnabled(Label.L3, flag=3643)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    if FlagEnabled(1051432704):
        ForceAnimation(character, 930016)
        Goto(Label.L20)
    if FlagEnabled(1051432703):
        ForceAnimation(character, 930015)
        Move(
            character,
            destination=1051432700,
            destination_type=CoordEntityType.Region,
            model_point=900,
            copy_draw_parent=character,
        )
        Goto(Label.L20)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 20034)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3645))
    OR_4.Add(FlagEnabled(3647))
    
    MAIN.Await(not OR_4)
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L0, flag=3640)
    GotoIfFlagEnabled(Label.L1, flag=3641)
    GotoIfFlagEnabled(Label.L2, flag=3642)
    GotoIfFlagEnabled(Label.L3, flag=3643)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 20034)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3646))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1051430701)
def Event_1051430701(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    first_flag: uint,
    last_flag: uint,
    right: int,
):
    """Event 1051430701"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(FlagEnabled(first_flag))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=40000))
    AND_4.Add(HealthRatio(character) >= 1.0)
    SkipLinesIfConditionFalse(2, AND_4)
    AND_2.Add(HealthRatio(character) < 0.6499999761581421)
    Goto(Label.L10)
    AND_5.Add(HealthRatio(character) >= 0.8999999761581421)
    SkipLinesIfConditionFalse(2, AND_5)
    AND_2.Add(HealthRatio(character) < 0.550000011920929)
    Goto(Label.L10)
    AND_6.Add(HealthRatio(character) >= 0.800000011920929)
    SkipLinesIfConditionFalse(2, AND_6)
    AND_2.Add(HealthRatio(character) < 0.44999998807907104)
    Goto(Label.L10)
    AND_7.Add(HealthRatio(character) >= 0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_7)
    AND_2.Add(HealthRatio(character) < 0.3499999940395355)
    Goto(Label.L10)
    AND_8.Add(HealthRatio(character) >= 0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_8)
    AND_2.Add(HealthRatio(character) < 0.25)
    Goto(Label.L10)
    AND_2.Add(HealthRatio(character) < 0.15000000596046448)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_2.Add(OR_1)
    OR_2.Add(FlagEnabled(flag_2))
    OR_2.Add(AND_2)
    AND_3.Add(HealthRatio(character) > 0.0)
    AND_3.Add(OR_2)
    OR_3.Add(FlagEnabled(flag_3))
    OR_3.Add(FlagDisabled(first_flag))
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    RestartIfFinishedConditionTrue(input_condition=OR_3)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20034)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()
    Restart()


@RestartOnRest(1051430702)
def Event_1051430702(_, character: uint, value: float):
    """Event 1051430702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3643):
        return
    AND_1.Add(FlagEnabled(3642))
    AND_1.Add(HealthRatio(character) <= value)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 20039)
    WaitFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=9663):
        return RESTART
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3643))
    EnableNetworkFlag(3640)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableFlag(1051439212)
    SaveRequest()
    Wait(8.0)
    DisableFlag(1051439212)
    SaveRequest()


@RestartOnRest(1051430703)
def Event_1051430703(_, character: uint):
    """Event 1051430703"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3647))
    AND_1.Add(EventValue(flag=1051439235, bit_count=5) >= 9)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1051439212)
    EnableInvincibility(character)


@RestartOnRest(1051433705)
def Event_1051433705(_, character: uint):
    """Event 1051433705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3641):
        return
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3644))
    EnableNetworkFlag(3640)
    SaveRequest()
    DisableNetworkFlag(1051439201)
    SetTeamType(character, TeamType.FriendlyNPC)
    End()


@RestartOnRest(1051433706)
def Event_1051433706(_, flag: uint):
    """Event 1051433706"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3643):
        return
    if FlagDisabled(1051439224):
        return
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3644))
    EnableNetworkFlag(3642)
    SaveRequest()
    EnableFlag(flag)
    End()


@RestartOnRest(1051433707)
def Event_1051433707(_, flag: uint, flag_1: uint):
    """Event 1051433707"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3643):
        return
    if FlagDisabled(3645):
        return
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(1051439225))
    AND_1.Add(FlagDisabled(1051439227))
    if not AND_1:
        return
    EnableFlag(flag_1)
    EnableFlag(flag)
    End()


@RestartOnRest(1051433708)
def Event_1051433708(
    _,
    item: int,
    item_1: int,
    item_2: int,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    last_flag: uint,
):
    """Event 1051433708"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3643):
        return
    if FlagDisabled(3645):
        return
    GotoIfFlagEnabled(Label.L1, flag=1051439226)
    GotoIfFlagEnabled(Label.L1, flag=1051439219)
    AND_1.Add(PlayerDoesNotHaveGood(item))
    AND_1.Add(PlayerDoesNotHaveGood(item_1))
    AND_1.Add(PlayerDoesNotHaveGood(item_2))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(PlayerHasGood(item))
    AND_2.Add(PlayerDoesNotHaveGood(item_1))
    AND_2.Add(PlayerDoesNotHaveGood(item_2))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(PlayerDoesNotHaveGood(item))
    AND_3.Add(PlayerHasGood(item_1))
    AND_3.Add(PlayerDoesNotHaveGood(item_2))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    AND_4.Add(PlayerDoesNotHaveGood(item))
    AND_4.Add(PlayerDoesNotHaveGood(item_1))
    AND_4.Add(PlayerHasGood(item_2))
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(first_flag)
    OR_5.Add(PlayerHasGood(item))
    OR_5.Add(PlayerHasGood(item_1))
    OR_5.Add(PlayerHasGood(item_2))
    AND_5.Add(OR_5)
    AND_5.Add(FlagDisabled(1051439226))
    AND_5.Add(FlagDisabled(1051439219))
    
    MAIN.Await(AND_5)
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    OR_6.Add(FlagEnabled(1051439226))
    OR_6.Add(FlagEnabled(1051439219))
    OR_6.Add(PlayerDoesNotHaveGood(item))
    OR_6.Add(PlayerHasGood(item_1))
    OR_6.Add(PlayerHasGood(item_2))
    
    MAIN.Await(OR_6)
    
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    OR_7.Add(FlagEnabled(1051439226))
    OR_7.Add(FlagEnabled(1051439219))
    OR_7.Add(PlayerHasGood(item))
    OR_7.Add(PlayerDoesNotHaveGood(item_1))
    OR_7.Add(PlayerHasGood(item_2))
    
    MAIN.Await(OR_7)
    
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_2)
    OR_8.Add(FlagEnabled(1051439226))
    OR_8.Add(FlagEnabled(1051439219))
    OR_8.Add(PlayerHasGood(item))
    OR_8.Add(PlayerHasGood(item_1))
    OR_8.Add(PlayerDoesNotHaveGood(item_2))
    
    MAIN.Await(OR_8)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(last_flag)
    AND_9.Add(PlayerDoesNotHaveGood(item))
    AND_9.Add(PlayerDoesNotHaveGood(item_1))
    AND_10.Add(PlayerDoesNotHaveGood(item))
    AND_10.Add(PlayerDoesNotHaveGood(item_2))
    AND_11.Add(PlayerDoesNotHaveGood(item_1))
    AND_11.Add(PlayerDoesNotHaveGood(item_2))
    OR_12.Add(FlagEnabled(1051439226))
    OR_12.Add(FlagEnabled(1051439219))
    OR_12.Add(AND_9)
    OR_12.Add(AND_10)
    OR_12.Add(AND_11)
    
    MAIN.Await(OR_12)
    
    Restart()
