"""
Land of Shadow 11-10 NW NE

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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_2045432550(
        0,
        character=580400,
        flag=580100,
        character_1=2045430250,
        animation_id=30015,
        animation_id_1=20015,
        asset=2045431550,
        asset_1=2045431560,
    )


@RestartOnRest(2045432550)
def Event_2045432550(
    _,
    character: uint,
    flag: Flag | int,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    asset: uint,
    asset_1: Asset | int,
):
    """Event 2045432550"""
    AddSpecialEffect(character, 10124)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableTreasure(asset=asset_1)
    if FlagEnabled(character):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=15.0))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    RemoveSpecialEffect(character, 10124)
    ForceAnimation(character_1, animation_id)
    EnableAsset(asset)
    EnableAsset(asset_1)
    ForceAnimation(asset, 2)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(character_1, animation_id_1)
    ForceAnimation(asset, 1)
    Wait(3.799999952316284)
    DisableCharacter(character_1)
    DisableAsset(asset)
    EnableTreasure(asset=asset_1)
