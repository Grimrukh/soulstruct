"""
Land of Shadow 12-09 NW NE

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
    RegisterGrace(grace_flag=2049390000, asset=2049391950)
    CommonFunc_90005200(
        0,
        character=2054390200,
        animation_id=30003,
        animation_id_1=20003,
        region=2054392200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005615(0, region=2049392690, left=0)
    Event_2049390700(
        0,
        character=2049390700,
        flag=4300,
        first_flag=4305,
        last_flag=4306,
        flag_1=2049392713,
        flag_2=2049392714,
        flag_3=2049399725,
        flag_4=2049392715,
        flag_5=2049399723,
        animation_id=90101,
        animation_id_1=90102,
        animation_id_2=90100,
        flag_6=2049399736,
        flag_7=4318,
        distance=35.0,
        distance_1=17.0,
        flag_8=2049392716,
        flag_9=2054390800,
    )
    Event_2049390701(0, flag=4300, first_flag=4825, last_flag=4827, flag_1=4318)
    Event_2049390702(
        0,
        seconds=30.0,
        seconds_1=30.0,
        flag=2049392702,
        flag_1=4305,
        flag_2=2049399722,
        flag_3=2049399725,
        flag_4=2049392701,
    )
    Event_2049390707(0, flag=4305, flag_1=2049392710, seconds=5.0, flag_2=2049399716, flag_3=2049399722)
    Event_2049390705(0, target_entity=2049390700, flag=2049399722, animation_id=90201, animation=90209)
    Event_2049390706(0, character=2049390700, flag=2049392711, animation_id=90203)
    CommonFunc_90005744(0, entity=2049390700, flag=2049399727, flag_1=2049399727, animation_id=90200)
    Event_2049390708(0, flag=4305, flag_1=2049399729, flag_2=2049399722, flag_3=2054390800)
    CommonFunc_90005750(
        0,
        asset=2049391701,
        action_button_id=4350,
        item_lot=107030,
        first_flag=400704,
        last_flag=400704,
        flag=2049399729,
        vfx_id=6102,
    )
    Event_2049390709(
        0,
        flag=2049399728,
        flag_1=2049392713,
        flag_2=2049399732,
        flag_3=2049392714,
        flag_4=2049399722,
        flag_5=2049392715,
        flag_6=2049399743,
        flag_7=2049392716,
    )
    Event_2049390704(
        0,
        flag=2049392704,
        flag_1=2049392705,
        left=2049392706,
        character=2049390700,
        dummy_id=710,
        asset=2049391700,
        dummy_id_1=710,
        radius=0.3499999940395355,
        animation=90208,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.100000023841858,
        seconds=2.4000000953674316,
        flag_2=2049399703,
        flag_3=2049392709,
        flag_4=2049399705,
        seconds_1=0.10000000149011612,
    )
    CommonFunc_90005741(
        0,
        flag=2049392707,
        flag_1=2049392708,
        left=2049392706,
        character=2049390700,
        animation__animation_id=90202,
        left_1=0,
        animation_id=-1,
        special_effect=-1,
        seconds=0.5,
    )
    Event_2049390703(0, flag=2049392709, flag_1=2049399704, seconds=0.10000000149011612)
    Event_2049390710(0, character=2049390710)
    Event_2049390711()
    Event_2049390712(0, region=2049392710, region_1=2049392710, flag=2049392720, right=1)


@RestartOnRest(2049390700)
def Event_2049390700(
    _,
    character: uint,
    flag: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    distance: float,
    distance_1: float,
    flag_8: Flag | int,
    flag_9: Flag | int,
):
    """Event 2049390700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableInvincibility(character)
    SetCharacterTalkRange(character=character, distance=distance_1)
    DisableFlag(flag_3)
    DisableFlag(flag_6)
    GotoIfFlagEnabled(Label.L20, flag=flag_8)
    GotoIfFlagEnabled(Label.L0, flag=first_flag)
    GotoIfFlagEnabled(Label.L0, flag=last_flag)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_4.Add(FlagDisabled(flag_4))
    AND_4.Add(FlagEnabled(flag_9))
    SkipLinesIfConditionFalse(3, AND_4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)
    AND_5.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(22, 0, 0)))
    AND_5.Add(FlagDisabled(flag_1))
    SkipLinesIfConditionFalse(1, AND_5)
    Goto(Label.L20)
    AND_6.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(22, 0, 0)))
    AND_6.Add(FlagEnabled(flag_1))
    AND_6.Add(FlagDisabled(flag_2))
    SkipLinesIfConditionFalse(1, AND_6)
    Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ResetCharacterPosition(character=character)
    AND_1.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(22, 0, 0)))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(flag_3)
    SetCharacterTalkRange(character=character, distance=distance)
    if FlagEnabled(last_flag):
        ForceAnimation(character, animation_id_2)
        EnableFlag(flag_6)
        Goto(Label.L20)
    AND_2.Add(FlagEnabled(flag_4))
    AND_2.Add(FlagDisabled(flag_5))
    SkipLinesIfConditionFalse(4, AND_2)
    ForceAnimation(character, animation_id_1)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(flag_6)
    Goto(Label.L20)
    AND_3.Add(FlagDisabled(flag_4))
    AND_3.Add(FlagEnabled(flag_3))
    SkipLinesIfConditionFalse(3, AND_3)
    ForceAnimation(character, animation_id)
    EnableFlag(flag_6)
    Goto(Label.L20)
    ForceAnimation(character, animation_id_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    OR_10.Add(FlagEnabled(flag_7))
    
    MAIN.Await(OR_10)
    
    if FlagEnabled(flag_7):
        MAIN.Await(TimeElapsed(seconds=3.0))
    Restart()


@RestartOnRest(2049390701)
def Event_2049390701(_, flag: Flag | int, first_flag: Flag | int, last_flag: Flag | int, flag_1: Flag | int):
    """Event 2049390701"""
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    
    EnableFlag(flag_1)
    DisableFlagRange((first_flag, last_flag))
    Restart()


@RestartOnRest(2049390702)
def Event_2049390702(
    _,
    seconds: float,
    seconds_1: float,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """Event 2049390702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    OR_10.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_10)
    
    GotoIfFlagEnabled(Label.L1, flag=flag_2)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(TimeElapsed(seconds=seconds))
    OR_5.Add(FlagEnabled(flag_4))
    OR_5.Add(FlagDisabled(flag_3))
    OR_5.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_5)
    
    if FlagDisabled(flag_3):
        return RESTART
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_6.Add(TimeElapsed(seconds=seconds_1))
    OR_6.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_6)
    
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    Restart()


@RestartOnRest(2049390703)
def Event_2049390703(_, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 2049390703"""
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(2049390704)
def Event_2049390704(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    dummy_id: int,
    asset: uint,
    dummy_id_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
    seconds: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds_1: float,
):
    """Event 2049390704"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_4)
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    GotoIfUnsignedEqual(Label.L0, left=asset, right=0)
    MoveAssetToCharacter(asset, character=character, dummy_id=dummy_id_1)
    WaitRealFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLinesIfConditionFalse(3, AND_1)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius_1))
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    SkipLinesIfConditionFalse(3, AND_15)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableFlag(flag_2)
    WaitRealFrames(frames=1)
    DisableFlag(flag_2)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    SkipLinesIfValueEqual(3, left=dummy_id, right=0)
    SkipLinesIfUnsignedEqual(2, left=asset, right=0)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLines(1)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    SkipLinesIfValueEqual(5, left=dummy_id, right=0)
    ResetAnimation(PLAYER)
    SkipLinesIfFlagEnabled(3, flag_4)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    SkipLines(1)
    Goto(Label.L15)
    EnableFlag(flag_3)
    Wait(seconds_1)

    # --- Label 15 --- #
    DefineLabel(15)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if ValueNotEqual(left=dummy_id, right=0):
        Move(
            PLAYER,
            destination=character,
            destination_type=CoordEntityType.Character,
            dummy_id=dummy_id,
            short_move=True,
        )
    if ValueNotEqual(left=special_effect, right=-1):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    else:
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_3.Add(FlagDisabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_4.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(2049390705)
def Event_2049390705(_, target_entity: uint, flag: Flag | int, animation_id: int, animation: int):
    """Event 2049390705"""
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag))
    
    FaceEntityAndForceAnimation(PLAYER, target_entity, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, target_entity, animation=animation)
    Wait(3.0)
    ForceAnimation(target_entity, animation_id, wait_for_completion=True)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(4318)
    End()


@RestartOnRest(2049390706)
def Event_2049390706(_, character: uint, flag: Flag | int, animation_id: int):
    """Event 2049390706"""
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableAnimations(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id)
    Wait(4.5)
    DisableCharacter(character)
    Wait(10.0)
    DisableBackread(character)
    End()


@RestartOnRest(2049390707)
def Event_2049390707(_, flag: Flag | int, flag_1: Flag | int, seconds: float, flag_2: Flag | int, flag_3: Flag | int):
    """Event 2049390707"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    AwaitFlagEnabled(flag=flag_1)
    SkipLinesIfFlagEnabled(1, flag_3)
    SkipLinesIfFlagEnabled(1, flag_2)
    
    MAIN.Await(TimeElapsed(seconds=seconds))
    
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(2049390708)
def Event_2049390708(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 2049390708"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    Restart()


@RestartOnRest(2049390709)
def Event_2049390709(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 2049390709"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_2))
    AND_3.Add(FlagEnabled(flag_4))
    AND_4.Add(FlagEnabled(flag_6))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableNetworkFlag(flag_1)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableNetworkFlag(flag_3)
    SkipLinesIfConditionFalse(1, AND_3)
    EnableNetworkFlag(flag_5)
    SkipLinesIfConditionFalse(1, AND_4)
    EnableNetworkFlag(flag_7)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_4))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_6))
    
    MAIN.Await(OR_15)
    
    Restart()


@RestartOnRest(2049390710)
def Event_2049390710(_, character: uint):
    """Event 2049390710"""
    DisableGravity(character)
    DisableAnimations(character)


@RestartOnRest(2049390711)
def Event_2049390711():
    """Event 2049390711"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9611))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9612))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60510)
    Wait(0.20000000298023224)
    Restart()


@RestartOnRest(2049390712)
def Event_2049390712(_, region: Region | int, region_1: Region | int, flag: Flag | int, right: int):
    """Event 2049390712"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    EnableFlag(flag)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    DisableFlag(flag)
    WaitFrames(frames=1)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(AND_1)
    
    if ValueNotEqual(left=-1, right=right):
        EnableFlag(flag)
    Restart()
