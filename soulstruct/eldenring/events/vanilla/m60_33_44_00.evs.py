"""
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
from .entities.m60_33_44_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1033440000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005460(0, character=Characters.GiantOctopus0)
    CommonFunc_90005461(0, character=Characters.GiantOctopus0)
    CommonFunc_90005462(0, character=Characters.GiantOctopus0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus1)
    CommonFunc_90005461(0, character=Characters.GiantOctopus1)
    CommonFunc_90005462(0, character=Characters.GiantOctopus1)
    CommonFunc_90005460(0, character=1033440204)
    CommonFunc_90005461(0, character=1033440204)
    CommonFunc_90005462(0, character=1033440204)
    CommonFunc_90005460(0, character=1033440205)
    CommonFunc_90005461(0, character=1033440205)
    CommonFunc_90005462(0, character=1033440205)
    CommonFunc_90005460(0, character=1033440206)
    CommonFunc_90005461(0, character=1033440206)
    CommonFunc_90005462(0, character=1033440206)
    CommonFunc_90005683(0, flag=62202, asset=Assets.AEG099_055_1000, vfx_id=209, flag_1=78292, flag_2=78292)
    CommonFunc_90005790(
        0,
        right=0,
        flag=1033440180,
        summon_flag=1033442181,
        dismissal_flag=1033442182,
        character=Characters.Edgar,
        sign_type=23,
        region=1033442701,
        region_1=1033442700,
        seconds=0.0,
        right_1=1045349259,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=1033440180, flag_1=1033442181, flag_2=1033442182, character=Characters.Edgar)
    CommonFunc_90005792(
        0,
        flag=1033440180,
        flag_1=1033442181,
        flag_2=1033442182,
        character=Characters.Edgar,
        item_lot_param_id=100610,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1033440180,
        flag_1=1033442181,
        flag_2=1033442182,
        character=Characters.Edgar,
        other_entity=1033442701,
        region=0,
        left=0,
    )
    Event_1033440700(0, character=Characters.ScalyMisbegotten0, animation_id=930027)
    Event_1033440700(1, character=Characters.ScalyMisbegotten1, animation_id=930029)
    Event_1033440700(2, character=Characters.ScalyMisbegotten2, animation_id=930028)
    Event_1033440705(0, asset=Assets.AEG099_620_9004)
    Event_1033440705(1, asset=Assets.AEG099_610_9001)
    Event_1033440705(2, asset=Assets.AEG099_610_9000)
    Event_1033440705(3, asset=Assets.AEG099_610_9002)
    Event_1033440705(4, asset=Assets.AEG099_610_9003)
    Event_1033440710(0, asset=Assets.AEG099_407_9000)
    Event_1033440710(1, asset=Assets.AEG099_408_9000)
    Event_1033440710(2, asset=Assets.AEG099_410_9001)
    Event_1033440710(3, 1033441713)


@RestartOnRest(1033440700)
def Event_1033440700(_, character: uint, animation_id: int):
    """Event 1033440700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3409)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3409))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableBackread(character)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, animation_id)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3409))
    
    Restart()


@RestartOnRest(1033440705)
def Event_1033440705(_, asset: uint):
    """Event 1033440705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3409)
    DisableAsset(asset)
    DisableTreasure(asset=asset)
    
    MAIN.Await(FlagEnabled(3409))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableAsset(asset)
    EnableTreasure(asset=asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3409))
    
    Restart()


@RestartOnRest(1033440710)
def Event_1033440710(_, asset: uint):
    """Event 1033440710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3409)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(3409))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3409))
    
    Restart()
