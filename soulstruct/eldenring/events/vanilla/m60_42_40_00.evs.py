"""
Northwest Limgrave Coast (SE) (SW)

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
from .enums.m60_42_40_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1042402650(0, flag=710670, tutorial_param_id=1670, item=9123, flag_1=69230)
    CommonFunc_90005706(0, character=Characters.StormhillColosseumSilentSpirit, animation_id=90101, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.StormhillColosseumSilentSpirit)


@RestartOnRest(1042402650)
def Event_1042402650(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 1042402650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042403700)
def Event_1042403700(_, character: uint):
    """Event 1042403700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30025)
