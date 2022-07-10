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
    RunCommonEvent(0, 90005525, args=(1035410612, 1035411612), arg_types="II")
    RunCommonEvent(0, 90005525, args=(1035410611, 1035411611), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(1035410570, 1035411570, 1035411571, 0, 1035412570, 1035412571, 1035412572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1035410570, 1035411573), arg_types="II")
    Event_1035412610(0, flag=1035410610, character=1035410610)
    Event_1035412611(0, flag=1035410610, attacked_entity=1035410610)
    RunCommonEvent(0, 90005251, args=(1035410610, 0.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1035410610, 1035410610, 0, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1035410200, 1035412200, 1.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410201, 1035412200, 1.0, 0.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410202, 1035412200, 1.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410203, 1035412203, 1.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410204, 1035412203, 1.0, 2.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410205, 1035412203, 1.0, 0.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410206, 1035412203, 1.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410340, 1035412340, 1.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035410350, 1035412350, 1.0, 0.0, 1700), arg_types="IIffi")


@RestartOnRest(1035412610)
def Event_1035412610(_, flag: uint, character: uint):
    """Event 1035412610"""
    EndIfFlagEnabled(flag)
    DisableCharacter(character)
    DisableAnimations(character)
    SkipLinesIfPlayerInOwnWorld(1)
    EnableInvincibility(character)
    IfFlagEnabled(AND_1, 1034432616)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableImmortality(character)
    DisableHealthBar(character)


@RestartOnRest(1035412611)
def Event_1035412611(_, flag: uint, attacked_entity: uint):
    """Event 1035412611"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=PLAYER)
    ForceAnimation(attacked_entity, 20008, unknown2=1.0)
    EnableFlag(flag)
