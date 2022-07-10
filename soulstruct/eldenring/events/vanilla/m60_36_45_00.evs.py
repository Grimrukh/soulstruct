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
    RegisterGrace(grace_flag=1036450000, obj=1036451950, unknown=5.0)
    RunCommonEvent(0, 90005261, args=(1036450340, 1036452340, 10.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005860, args=(1036450800, 0, 1036450340, 0, 1036450400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(1036450340, 904980604, 24), arg_types="IiI")
    RunCommonEvent(
        0,
        90005605,
        args=(1036451620, 60, 34, 48, 0, 1034482620, 0, 1036452620, 1036452621, 1036452622, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1036450220, 1036452220, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450221, 1036452220, 10.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450222, 1036452220, 10.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1036450223, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1036450224, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1036450225, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1036450226, 1036452226, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450227, 1036452226, 0.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450228, 1036452226, 0.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450229, 1036452226, 0.0, 0.30000001192092896, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450230, 1036452226, 0.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450231, 1036452226, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450241, 1036452250, 0.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450242, 1036452250, 0.0, 0.30000001192092896, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450243, 1036452250, 0.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036450250, 1036452250, 0.0, 0.0, -1), arg_types="IIffi")


@RestartOnRest(1036452200)
def Event_1036452200(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1036452200"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    AddSpecialEffect(character, 8560)
    DisableCharacter(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    EnableCharacter(character)
