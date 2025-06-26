"""
Land of Shadow 12-11 SW NW

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
    RegisterGrace(grace_flag=2048450000, asset=2048451950, enemy_block_distance=0.0)
    CommonFunc_900005571(0, flag=60860, gesture_param_id=111, flag_1=2048457510, right=0)
    Event_2048452500(0, flag=2048450500)
    CommonFunc_900005580(0, flag=580600, asset=2048451500, flag_1=2048450500)
    Event_2048450700(
        0,
        character=2048450700,
        flag=4366,
        animation_id=90100,
        animation_id_1=90101,
        flag_1=4360,
        flag_2=4363,
        flag_3=4898,
        flag_4=2048452703,
        flag_5=4927,
        flag_6=2048452702,
    )
    Event_2048450701(
        0,
        character=2048450700,
        flag=4368,
        flag_1=2048452704,
        animation_id=90101,
        animation_id_1=90102,
        flag_2=4360,
        flag_3=4363,
        flag_4=2048452706,
        flag_5=4898,
        flag_6=2048452705,
        flag_7=2048452702,
    )
    Event_2048450702(0, entity=2048450700, flag=4927, animation_id=90101)
    Event_2048450703(0, flag=21019225, flag_1=21019226)
    Event_2048450704(
        0,
        flag=2048459230,
        flag_1=400612,
        flag_2=2046429221,
        flag_3=4366,
        flag_4=4368,
        flag_5=21019214,
        flag_6=2048459217,
        flag_7=2048459223,
        flag_8=2048452703,
        flag_9=2048452704,
        flag_10=21019226,
        flag_11=2048452705,
        flag_12=21019215,
        flag_13=2048452706,
    )
    Event_2048450710(
        0,
        asset=2048451700,
        action_button_id=4350,
        item_lot=106140,
        first_flag=400610,
        last_flag=400612,
        flag=2048459223,
        vfx_id=6102,
        vfx_id_1=6100,
        flag_1=400610,
        flag_2=400611,
    )
    CommonFunc_90005744(0, entity=2048450700, flag=2048452701, flag_1=2048459229, animation_id=90201)
    CommonFunc_90005749(0, character=2048450701, character_1=2048450700, flag=2048459217, flag_1=2048452702)
    Event_2048450705(
        0,
        character=2048450710,
        flag=4440,
        flag_1=4443,
        flag_2=4446,
        animation_id=90100,
        animation_id_1=90101,
        flag_3=4896,
        flag_4=4927,
        flag_5=2048452710,
    )
    CommonFunc_90005749(0, character=2048450711, character_1=2048450710, flag=4446, flag_1=2048452710)
    Event_2048450706(0, flag=4927, entity=2048450710, animation_id=90101)
    CommonFunc_90005744(0, entity=2048450710, flag=2048459264, flag_1=2048459264, animation_id=90200)
    CommonFunc_90005744(0, entity=2048450710, flag=2048459270, flag_1=2048459270, animation_id=90200)
    Event_2048450707(0, flag=4926, flag_1=4458)
    Event_2048450708(0, asset=2048451710, action_button_id=4350, vfx_id=6102)
    CommonFunc_90005748(0, entity=2048451720, action_button_id=206021, text=1030024, display_distance=30.0, flag=4914)
    Event_2048450709(0, entity=2048450710, flag=2048452718, flag_1=4446, flag_2=4896)


@RestartOnRest(2048452500)
def Event_2048452500(_, flag: Flag | int):
    """Event 2048452500"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(9146))
    AND_1.Add(FlagEnabled(4896))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(2048450700)
def Event_2048450700(
    _,
    character: uint,
    flag: Flag | int,
    animation_id: int,
    animation_id_1: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 2048450700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_4))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag_4))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(10, flag_6)
    SkipLinesIfFlagEnabled(9, flag_3)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SetTeamType(character, TeamType.NoTeam)
    SkipLinesIfFlagEnabled(2, flag_5)
    ForceAnimation(character, animation_id)
    SkipLines(1)
    ForceAnimation(character, animation_id_1)
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
    AND_3.Add(FlagDisabled(flag_4))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(2048450701)
def Event_2048450701(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    animation_id_1: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 2048450701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag_6))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_6))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(10, flag_7)
    SkipLinesIfFlagEnabled(9, flag_5)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SetTeamType(character, TeamType.NoTeam)
    SkipLinesIfFlagEnabled(2, flag_4)
    ForceAnimation(character, animation_id_1)
    SkipLines(1)
    ForceAnimation(character, animation_id)
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
    AND_3.Add(FlagEnabled(flag_1))
    AND_3.Add(FlagDisabled(flag_6))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(2048450702)
def Event_2048450702(_, entity: uint, flag: Flag | int, animation_id: int):
    """Event 2048450702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, animation_id)
    End()


@RestartOnRest(2048450703)
def Event_2048450703(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2048450703"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag):
        EnableFlag(flag_1)
    End()


@RestartOnRest(2048450704)
def Event_2048450704(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    flag_13: Flag | int,
):
    """Event 2048450704"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    GotoIfFlagEnabled(Label.L1, flag=flag_4)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagEnabled(1, flag_2)
    EnableFlag(flag_1)
    EnableFlag(flag)
    if FlagEnabled(flag_7):
        EnableFlag(flag_8)
    else:
        EnableFlag(flag_6)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(flag_5):
        EnableFlag(flag_6)
        EnableFlag(flag_9)
    if FlagEnabled(flag_10):
        EnableFlag(flag_11)
        DisableFlag(flag_6)
    if FlagEnabled(flag_12):
        EnableFlag(flag_13)
    EnableFlag(flag_7)
    End()


@RestartOnRest(2048450705)
def Event_2048450705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    animation_id: int,
    animation_id_1: int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 2048450705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L20, flag=flag_3)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=flag_5)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SetTeamType(character, TeamType.NoTeam)
    if FlagDisabled(flag_4):
        ForceAnimation(character, animation_id, loop=True)
    if FlagEnabled(flag_4):
        ForceAnimation(character, animation_id_1, loop=True)
    WaitRealFrames(frames=1)
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


@RestartOnRest(2048450706)
def Event_2048450706(_, flag: Flag | int, entity: uint, animation_id: int):
    """Event 2048450706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, animation_id)
    End()


@RestartOnRest(2048450707)
def Event_2048450707(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2048450707"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    EnableFlag(flag_1)


@RestartOnRest(2048450708)
def Event_2048450708(_, asset: uint, action_button_id: int, vfx_id: int):
    """Event 2048450708"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(FlagDisabled(4446))
    AND_10.Add(FlagEnabled(7623))
    AND_10.Add(FlagDisabled(400590))
    GotoIfConditionTrue(Label.L1, input_condition=AND_10)
    AND_11.Add(FlagDisabled(4446))
    AND_11.Add(FlagEnabled(7621))
    AND_11.Add(FlagDisabled(400592))
    GotoIfConditionTrue(Label.L2, input_condition=AND_11)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=vfx_id, right=0):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id)
    else:
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6101)
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    
    MAIN.Await(OR_1)
    
    DeleteAssetVFX(asset)
    AwardItemLot(105900, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    if ValueNotEqual(left=vfx_id, right=0):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id)
    else:
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6101)
    OR_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    
    MAIN.Await(OR_3)
    
    DeleteAssetVFX(asset)
    AwardItemLot(105910, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()


@RestartOnRest(2048450709)
def Event_2048450709(_, entity: uint, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2048450709"""
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


@RestartOnRest(2048450710)
def Event_2048450710(
    _,
    asset: uint,
    action_button_id: int,
    item_lot: int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    vfx_id: int,
    vfx_id_1: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 2048450710"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    SkipLinesIfConditionTrue(2, AND_2)
    CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id)
    SkipLines(1)
    CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id_1)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_2)
    DeleteAssetVFX(asset)
    AwardItemLot(item_lot, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()
