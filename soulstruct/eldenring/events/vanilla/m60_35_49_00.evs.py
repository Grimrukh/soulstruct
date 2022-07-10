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
    Event_1035492220()
    RunCommonEvent(0, 90005631, args=(1035491640, 61022), arg_types="Ii")


@RestartOnRest(1035492220)
def Event_1035492220():
    """Event 1035492220"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=1035490220, radius=30.0)
    IfConditionTrue(AND_1, input_condition=AND_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ForceAnimation(1035490220, 3011, unknown2=1.0)
    Wait(5.0)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1035492220, unk_8_12=1)
    End()
