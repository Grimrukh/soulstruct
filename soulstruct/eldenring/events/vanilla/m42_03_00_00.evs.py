"""
m42_03_00_00

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
    RegisterGrace(grace_flag=42030000, asset=42031950)
    CommonFunc_90005646(
        0,
        flag=42037000,
        left_flag=42032840,
        cancel_flag__right_flag=42032841,
        asset=42031840,
        player_start=42032840,
        area_id=42,
        block_id=3,
        cc_id=0,
        dd_id=0,
    )
    Event_42032580()
    Event_42032630()
    Event_42032631()
    Event_42032632()
    CommonFunc_90005555(0, flag=42037000, item_lot=42030000, asset=42031600)
    CommonFunc_900005610(0, asset=42031640, dummy_id=100, vfx_id=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, character=42030300, region=42032300, seconds=0.0, animation_id=3015)
    CommonFunc_90005200(
        0,
        character=42030301,
        animation_id=30002,
        animation_id_1=20002,
        region=42032301,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42030305, region=42032301, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42030302,
        animation_id=30001,
        animation_id_1=20001,
        region=42032302,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030303,
        animation_id=30001,
        animation_id_1=20001,
        region=42032303,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=42030304, region=42032304, radius=38.0, seconds=5.0, animation_id=0)
    Event_42032305()
    Event_42032304(
        0,
        character=42030245,
        character_1=42030246,
        character_2=42030247,
        character_3=42030248,
        character_4=42030249,
    )
    CommonFunc_90005200(
        0,
        character=42030200,
        animation_id=30000,
        animation_id_1=20000,
        region=42032200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030212,
        animation_id=30000,
        animation_id_1=20000,
        region=42032210,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030217,
        animation_id=30000,
        animation_id_1=20000,
        region=42032217,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030218,
        animation_id=30000,
        animation_id_1=20000,
        region=42032217,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030219,
        animation_id=30000,
        animation_id_1=20000,
        region=42032217,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030220,
        animation_id=30000,
        animation_id_1=20000,
        region=42032217,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030234,
        animation_id=30000,
        animation_id_1=20000,
        region=42032234,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030240,
        animation_id=30000,
        animation_id_1=20000,
        region=42032230,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42030241, region=42032302, seconds=0.4000000059604645, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42030237,
        animation_id=30000,
        animation_id_1=20000,
        region=42032236,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42030238,
        animation_id=30000,
        animation_id_1=20000,
        region=42032236,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42030239, region=42032303, seconds=0.0, animation_id=0)
    Event_42032201(0, character=42030245)
    Event_42032201(1, character=42030246)
    Event_42032201(2, character=42030247)
    Event_42032201(3, character=42030248)
    Event_42032201(4, character=42030249)
    Event_42032200(0, character=42030200, region=42032201)


@ContinueOnRest(42032580)
def Event_42032580():
    """Event 42032580"""
    RegisterLadder(start_climbing_flag=42030580, stop_climbing_flag=42030581, asset=42031580)
    RegisterLadder(start_climbing_flag=42030582, stop_climbing_flag=42030583, asset=42031582)
    RegisterLadder(start_climbing_flag=42030584, stop_climbing_flag=42030585, asset=42031584)


@RestartOnRest(42032600)
def Event_42032600():
    """Event 42032600"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(42037000):
        return
    CreateAssetVFX(42031600, dummy_id=100, vfx_id=834010)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209200, entity=42031600))
    
    MAIN.Await(AND_1)
    
    FaceEntityAndForceAnimation(PLAYER, 42031600, wait_for_completion=True)
    ForceAnimation(PLAYER, 60100)
    Wait(1.0)
    CreateAssetVFX(42031600, dummy_id=100, vfx_id=800380)
    Wait(1.0)
    DeleteAssetVFX(42031600)
    Wait(2.5)
    AwardItemLot(42030000, host_only=True)


@RestartOnRest(42032630)
def Event_42032630():
    """Event 42032630"""
    if FlagEnabled(42030631):
        return
    if FlagEnabled(42030632):
        return
    EndOfAnimation(asset=42031630, animation_id=10)
    EnableNetworkFlag(42032631)
    DisableAssetActivation(42031631, obj_act_id=449011)


@RestartOnRest(42032631)
def Event_42032631():
    """Event 42032631"""
    GotoIfFlagDisabled(Label.L0, flag=42030631)
    DisableAssetActivation(42031631, obj_act_id=449011)
    EndOfAnimation(asset=42031630, animation_id=10)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(42030631))
    AND_1.Add(AssetActivated(obj_act_id=42033631))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(42030631)
    DisableNetworkFlag(42030632)
    DisableAssetActivation(42031631, obj_act_id=449011)
    EnableAssetActivation(42031632, obj_act_id=449011)
    ForceAnimation(42031630, 21, wait_for_completion=True)
    Restart()


@RestartOnRest(42032632)
def Event_42032632():
    """Event 42032632"""
    GotoIfFlagDisabled(Label.L0, flag=42030632)
    DisableAssetActivation(42031632, obj_act_id=449011)
    EndOfAnimation(asset=42031630, animation_id=20)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(42030632))
    AND_1.Add(AssetActivated(obj_act_id=42033632))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(42030632)
    DisableNetworkFlag(42030631)
    DisableAssetActivation(42031632, obj_act_id=449011)
    EnableAssetActivation(42031631, obj_act_id=449011)
    ForceAnimation(42031630, 12, wait_for_completion=True)
    Restart()


@RestartOnRest(42032200)
def Event_42032200(_, character: Character | int, region: Region | int):
    """Event 42032200"""
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4080)
    AddSpecialEffect(character, 4085)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4080)
    RemoveSpecialEffect(character, 4085)
    Restart()


@RestartOnRest(42032201)
def Event_42032201(_, character: uint):
    """Event 42032201"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)


@RestartOnRest(42032304)
def Event_42032304(_, character: uint, character_1: uint, character_2: uint, character_3: uint, character_4: uint):
    """Event 42032304"""
    if FlagEnabled(42032249):
        return
    AND_15.Add(CharacterDead(42030304))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_10.Add(CharacterHasSpecialEffect(42030304, 5025))
    OR_10.Add(FlagDisabled(42032245))
    OR_10.Add(FlagDisabled(42032246))
    OR_10.Add(FlagDisabled(42032247))
    OR_10.Add(FlagDisabled(42032248))
    OR_10.Add(FlagDisabled(42032249))
    AND_10.Add(OR_10)
    
    MAIN.Await(AND_10)
    
    GotoIfFlagEnabled(Label.L0, flag=42032245)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableGravity(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=42030304,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=42030304,
    )
    ForceAnimation(character, 20002)
    WaitRealFrames(frames=45)
    ForceAnimation(character, 20003)
    SetNest(character, region=42032245)
    EnableNetworkFlag(42032245)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=42032246)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableGravity(character_1)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character_1,
        destination=42030304,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=42030304,
    )
    ForceAnimation(character_1, 20002)
    WaitRealFrames(frames=45)
    ForceAnimation(character_1, 20003)
    SetNest(character_1, region=42032245)
    EnableNetworkFlag(42032246)
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=42032247)
    EnableCharacter(character_2)
    EnableAnimations(character_2)
    EnableGravity(character_2)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character_2,
        destination=42030304,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=42030304,
    )
    ForceAnimation(character_2, 20002)
    WaitRealFrames(frames=45)
    ForceAnimation(character_2, 20003)
    SetNest(character_2, region=42032245)
    EnableNetworkFlag(42032247)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L3, flag=42032248)
    EnableCharacter(character_3)
    EnableAnimations(character_3)
    EnableGravity(character_3)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character_3,
        destination=42030304,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=42030304,
    )
    ForceAnimation(character_3, 20002)
    WaitRealFrames(frames=45)
    ForceAnimation(character_3, 20003)
    SetNest(character_3, region=42032245)
    EnableNetworkFlag(42032248)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L10, flag=42032249)
    EnableCharacter(character_4)
    EnableAnimations(character_4)
    EnableGravity(character_4)
    SetNetworkUpdateRate(character_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character_4,
        destination=42030304,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=42030304,
    )
    ForceAnimation(character_4, 20002)
    WaitRealFrames(frames=45)
    ForceAnimation(character_4, 20003)
    SetNest(character_4, region=42032245)
    EnableNetworkFlag(42032249)
    SetNetworkUpdateRate(character_4, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(42030304, 8081)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    Restart()


@RestartOnRest(42032305)
def Event_42032305():
    """Event 42032305"""
    if FlagEnabled(42032249):
        return
    AND_10.Add(CharacterDead(42030304))
    GotoIfConditionFalse(Label.L0, input_condition=AND_10)
    EnableNetworkFlag(42032305)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=42032304))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=42030304, radius=4.0))
    OR_1.Add(FlagDisabled(42032245))
    OR_1.Add(FlagDisabled(42032246))
    OR_1.Add(FlagDisabled(42032247))
    OR_1.Add(FlagDisabled(42032248))
    OR_1.Add(FlagDisabled(42032249))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(42032305):
        Wait(17.0)
    AND_15.Add(HasAIStatus(42030304, ai_status=AIStatusType.Battle))
    SkipLinesIfConditionFalse(2, AND_15)
    EnableNetworkFlag(42032305)
    End()
    ForceAnimation(42030304, 20000, wait_for_completion=True)
    Wait(2.0)
    Restart()
