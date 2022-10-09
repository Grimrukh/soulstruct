"""
Southwest Liurnia (SE) (NE)

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
from .entities.m60_35_41_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005525(0, flag=1035410612, asset=1035411612)
    CommonFunc_90005525(0, flag=1035410611, asset=1035411611)
    CommonFunc_90005620(
        0,
        flag=1035410570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=1035412570,
        cancel_flag__right_flag=1035412571,
        right=1035412572,
    )
    CommonFunc_90005621(0, flag=1035410570, asset=Assets.AEG099_272_9000)
    Event_1035412610(0, flag=1035410610, character=Characters.GiantTurtle)
    Event_1035412611(0, flag=1035410610, attacked_entity=Characters.GiantTurtle)
    CommonFunc_90005251(0, character=Characters.GiantTurtle, radius=0.0, seconds=0.0, animation_id=0)
    CommonFunc_90005300(0, flag=1035410610, character=Characters.GiantTurtle, item_lot=0, seconds=0.0, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower0,
        region=1035412200,
        radius=1.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower1,
        region=1035412200,
        radius=1.0,
        seconds=0.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower2,
        region=1035412200,
        radius=1.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower3,
        region=1035412203,
        radius=1.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower4,
        region=1035412203,
        radius=1.0,
        seconds=2.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower5,
        region=1035412203,
        radius=1.0,
        seconds=0.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower6,
        region=1035412203,
        radius=1.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Revenant0,
        region=1035412340,
        radius=1.0,
        seconds=0.0,
        animation_id=1700,
    )
    CommonFunc_90005261(0, character=Characters.Revenant1, region=1035412350, radius=1.0, seconds=0.0, animation_id=1700)


@RestartOnRest(1035412610)
def Event_1035412610(_, flag: uint, character: uint):
    """Event 1035412610"""
    if FlagEnabled(flag):
        return
    DisableCharacter(character)
    DisableAnimations(character)
    if PlayerNotInOwnWorld():
        EnableInvincibility(character)
    AND_1.Add(FlagEnabled(1034432616))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableAnimations(character)
    EnableImmortality(character)
    DisableHealthBar(character)


@RestartOnRest(1035412611)
def Event_1035412611(_, flag: uint, attacked_entity: uint):
    """Event 1035412611"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    ForceAnimation(attacked_entity, 20008)
    EnableFlag(flag)
