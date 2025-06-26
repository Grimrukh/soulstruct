"""
North Caelid (SE) (NE)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_51_41_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1051412200(0, character=Characters.GiantBall, asset=Assets.AEG099_090_9000, region=1051412210)
    CommonFunc_90005300(0, flag=1051410290, character=Characters.Scarab, item_lot=40420, seconds=0.0, left=0)


@RestartOnRest(1051412200)
def Event_1051412200(_, character: uint, asset: Asset | int, region: uint):
    """Event 1051412200"""
    DisableCharacter(character)
    if FlagEnabled(region):
        return
    AND_3.Add(CharacterDead(character))
    if AND_3:
        return
    DisableHealthBar(character)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(OR_1)
    
    MAIN.Await(AND_2)
    
    CreateAssetVFX(asset, dummy_id=100, vfx_id=620383)
    EnableCharacter(character)
    EnableNetworkFlag(region)
    Wait(2.0)
    DeleteAssetVFX(asset)
    ForceAnimation(character, 20001)
    Wait(1.899999976158142)
    ForceAnimation(character, 20004)
    Wait(2.0)
    ForceAnimation(character, 20004)
    Wait(1.0)
    DisableCharacter(character)
    Kill(character)
    End()
