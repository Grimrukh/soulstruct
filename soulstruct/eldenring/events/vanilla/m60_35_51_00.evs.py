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
    RunCommonEvent(0, 900005610, args=(1035511650, 100, 800, 0), arg_types="IiiI")


@NeverRestart(1035512210)
def Event_1035512210():
    """Event 1035512210"""
    IfCharacterHasSpecialEffect(AND_14, PLAYER, 415)
    IfEntityWithinDistance(AND_14, entity=1035510200, other_entity=PLAYER, radius=6.0)
    IfConditionTrue(OR_14, input_condition=AND_14)
    IfEntityWithinDistance(OR_14, entity=1035510200, other_entity=1035511200, radius=6.0)
    IfConditionTrue(MAIN, input_condition=OR_14)
    EnableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_model_point=220, state=True)
    AddSpecialEffect(1035510200, 14501)
    AddSpecialEffect(1035510200, 14502)
    WaitFrames(frames=1)
    Restart()


@NeverRestart(1035512220)
def Event_1035512220():
    """Event 1035512220"""
    IfCharacterDoesNotHaveSpecialEffect(OR_13, PLAYER, 415)
    IfEntityBeyondDistance(OR_13, entity=1035510200, other_entity=PLAYER, radius=6.0)
    IfEntityBeyondDistance(OR_13, entity=1035510200, other_entity=1035511200, radius=6.0)
    IfConditionTrue(AND_12, input_condition=OR_13)
    IfCharacterDoesNotHaveSpecialEffect(AND_12, 1035510200, 14503)
    IfConditionTrue(MAIN, input_condition=AND_12)
    DisableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_model_point=220, state=False)
    AddSpecialEffect(1035510200, 14500)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1035512211)
def Event_1035512211():
    """Event 1035512211"""
    IfCharacterHasSpecialEffect(AND_14, PLAYER, 415)
    IfEntityWithinDistance(AND_14, entity=1035510200, other_entity=PLAYER, radius=6.0)
    IfConditionTrue(OR_14, input_condition=AND_14)
    IfEntityWithinDistance(OR_14, entity=1035510200, other_entity=1035511200, radius=6.0)
    IfConditionTrue(AND_9, input_condition=OR_14)
    GotoIfConditionFalse(Label.L0, input_condition=AND_9)
    EnableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_model_point=220, state=True)
    AddSpecialEffect(1035510200, 14501)
    AddSpecialEffect(1035510200, 14502)
    WaitFrames(frames=1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_model_point=220, state=False)
    AddSpecialEffect(1035510200, 14500)
    WaitFrames(frames=1)
    Restart()
