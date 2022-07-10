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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    EnableCharacterCollision(0)
    RunCommonEvent(0, 90005261, args=(1037550200, 1037552200, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1037550201, 1037552200, 10.0, 0.0, 0), arg_types="IIffi")
    Event_1037552200(0, character=1037550200, region=1037552200)
    Event_1037552200(1, character=1037550201, region=1037552200)
    RunCommonEvent(0, 90005261, args=(1037550205, 1037552205, 10.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(1037552200)
def Event_1037552200(_, character: uint, region: uint):
    """Event 1037552200"""
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterOutsideRegion(OR_1, character=PLAYER, region=region)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    End()
