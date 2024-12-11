"""
Land of Shadow 12-10 SE SW

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
    CommonFunc_90005250(0, character=2050400200, region=2050402200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2050400201, region=2050402200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2050400202, region=2050402200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2050400203, region=2050402200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2050400204, region=2050402200, seconds=0.0, animation_id=0)
    Event_2050402200(0, character=2050400201)
    Event_2050402210(0, character=2050400201, character_1=2050400202)
    Event_2050402210(1, character=2050400202, character_1=2050400203)
    Event_2050402210(2, character=2050400203, character_1=2050400204)
    Event_2050402210(3, character=2050400204, character_1=2050400205)
    CommonFunc_90005261(0, character=2050400210, region=2050402210, radius=10.0, seconds=0.0, animation_id=1703)
    Event_2050402600()


@RestartOnRest(2050402200)
def Event_2050402200(_, character: Character | int):
    """Event 2050402200"""
    MAIN.Await(CharacterBackreadEnabled(character))
    
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 20011075))
    AddSpecialEffect(character, 20011073)


@RestartOnRest(2050402210)
def Event_2050402210(_, character: Character | int, character_1: Character | int):
    """Event 2050402210"""
    AND_1.Add(CharacterHasSpecialEffect(character, 20011075))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 20011076)
    Wait(10.0)
    AddSpecialEffect(character_1, 20011073)


@ContinueOnRest(2050402600)
def Event_2050402600():
    """Event 2050402600"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2050400600):
        DisableAssetActivation(2050401600, obj_act_id=52407)
        Wait(1.0)
        AwardItemLot(2050400000, host_only=True)
        End()
    AND_10.Add(PlayerDoesNotHaveGood(2008008))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(2008008))
    AND_1.Add(AssetActivated(obj_act_id=2050403600))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(2050400600)
    Wait(10.0)
    AwardItemLot(2050400000, host_only=True)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableAssetActivation(2050401600, obj_act_id=52407)
    
    MAIN.Await(PlayerHasGood(2008008))
    
    EnableAssetActivation(2050401600, obj_act_id=52407)
    Wait(0.10000000149011612)
    Restart()
