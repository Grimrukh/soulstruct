"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1051412200(0, character=1051410210, obj=1051411210, region=1051412210)
    RunCommonEvent(0, 90005300, args=(1051410290, 1051410290, 40420, 0.0, 0), arg_types="IIifi")


@RestartOnRest(1051412200)
def Event_1051412200(_, character: uint, obj: uint, region: uint):
    """Event 1051412200"""
    DisableCharacter(character)
    EndIfFlagEnabled(region)
    IfCharacterDead(AND_3, character)
    EndIfConditionTrue(input_condition=AND_3)
    DisableHealthBar(character)
    IfCharacterType(AND_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_2)
    CreateObjectVFX(obj, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    EnableNetworkFlag(region)
    Wait(2.0)
    DeleteObjectVFX(obj)
    ForceAnimation(character, 20001, unknown2=1.0)
    Wait(1.899999976158142)
    ForceAnimation(character, 20004, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(character, 20004, unknown2=1.0)
    Wait(1.0)
    DisableCharacter(character)
    Kill(character)
    End()
