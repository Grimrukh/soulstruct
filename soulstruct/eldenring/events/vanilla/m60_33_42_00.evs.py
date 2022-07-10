"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1033422211()
    Event_1033422611()
    RunCommonEvent(0, 90005300, args=(1033420610, 1033420610, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005880,
        args=(1033420800, 1033420805, 1033422800, 1033420800, 30265, 60, 33, 42, 0, 1033422805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1033420800, 1033420805, 1033422801, 1033422802, 20300, 1033421805, 60, 33, 42, 0, 1033422805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1033420800,
            1033420805,
            1033422800,
            1033420800,
            1033422806,
            1033425810,
            1033421800,
            1033420810,
            1033422810,
            902100521,
            -1,
            20020,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1033420800, 1033420805, 1033421805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1033420800, 0, 1033422806, 1033422807, 0, 1), arg_types="IiIIii")


@RestartOnRest(1033422211)
def Event_1033422211():
    """Event 1033422211"""
    EndIfFlagEnabled(1033420610)
    DisableAI(1033420610)
    ForceAnimation(1033420610, 30008, unknown2=1.0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=1033420610, attacker=PLAYER)
    IfEntityWithinDistance(OR_2, entity=1033420610, other_entity=40000, radius=7.0)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1033420610)
    ForceAnimation(1033420610, 20016, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(1033422611)
def Event_1033422611():
    """Event 1033422611"""
    EndIfFlagEnabled(1033420610)
    DisableCharacter(1033420610)
    DisableAnimations(1033420610)
    SkipLinesIfPlayerInOwnWorld(1)
    EnableInvincibility(1033420610)
    IfFlagEnabled(AND_1, 1034432616)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(1033420610)
    EnableAnimations(1033420610)
    EnableImmortality(1033420610)
    DisableHealthBar(1033420610)
