"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
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
    RegisterGrace(grace_flag=1034440000, obj=1034441950, unknown=5.0)
    RunCommonEvent(0, 1034442200)
    RunCommonEvent(0, 90005300, args=(1034440220, 1034440220, 40218, 0.0, 0), arg_types="IIifi")
    Event_1034440700(0, 1034440700, 930023, 3409)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1034440700)
    RunCommonEvent(0, 90005261, args=(1034440200, 1034442200, 3.0, 2.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1034440200, 30002, 20002, 1034442200, 3.0, 2.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1034440201, 30002, 20002, 1034442200, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1034440202, 1034442200, 3.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1034440202, 30002, 20002, 1034442200, 3.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(1034440700)
def Event_1034440700(_, character: uint, animation_id: int, flag: uint):
    """Event 1034440700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, flag)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    DisableGravity(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    IfFlagDisabled(MAIN, flag)
    Restart()


@RestartOnRest(1034442200)
def Event_1034442200():
    """Event 1034442200"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=1034442200)
    IfConditionTrue(AND_1, input_condition=AND_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1034442200, unk_8_12=1)
    End()
