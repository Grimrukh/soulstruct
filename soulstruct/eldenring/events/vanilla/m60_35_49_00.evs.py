"""
Northwest Liurnia (SE) (NE)

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
from .enums.m60_35_49_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1035492220()
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61022)


@RestartOnRest(1035492220)
def Event_1035492220():
    """Event 1035492220"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.WolfPackLeader, radius=30.0))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(Characters.WolfPackLeader, 3011)
    Wait(5.0)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1035492220, unk_8_12=1)
    End()
