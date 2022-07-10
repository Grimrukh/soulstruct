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
    Event_1042402650(0, flag=710670, tutorial_param_id=1670, item=9123, flag_1=69230)
    RunCommonEvent(0, 90005706, args=(1042400700, 90101, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042400700)


@RestartOnRest(1042402650)
def Event_1042402650(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 1042402650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042403700)
def Event_1042403700(_, character: uint):
    """Event 1042403700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30025, unknown2=1.0)
