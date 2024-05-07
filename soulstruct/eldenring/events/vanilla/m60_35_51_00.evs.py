"""
Northwest Liurnia (NE) (NE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_35_51_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)


@ContinueOnRest(1035512210)
def Event_1035512210():
    """Event 1035512210"""
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 415))
    AND_14.Add(EntityWithinDistance(entity=1035510200, other_entity=PLAYER, radius=6.0))
    OR_14.Add(AND_14)
    OR_14.Add(EntityWithinDistance(entity=1035510200, other_entity=1035511200, radius=6.0))
    
    MAIN.Await(OR_14)
    
    EnableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_dummy_id=220, state=True)
    AddSpecialEffect(1035510200, 14501)
    AddSpecialEffect(1035510200, 14502)
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(1035512220)
def Event_1035512220():
    """Event 1035512220"""
    OR_13.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 415))
    OR_13.Add(EntityBeyondDistance(entity=1035510200, other_entity=PLAYER, radius=6.0))
    OR_13.Add(EntityBeyondDistance(entity=1035510200, other_entity=1035511200, radius=6.0))
    AND_12.Add(OR_13)
    AND_12.Add(CharacterDoesNotHaveSpecialEffect(1035510200, 14503))
    
    MAIN.Await(AND_12)
    
    DisableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_dummy_id=220, state=False)
    AddSpecialEffect(1035510200, 14500)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1035512211)
def Event_1035512211():
    """Event 1035512211"""
    AND_14.Add(CharacterHasSpecialEffect(PLAYER, 415))
    AND_14.Add(EntityWithinDistance(entity=1035510200, other_entity=PLAYER, radius=6.0))
    OR_14.Add(AND_14)
    OR_14.Add(EntityWithinDistance(entity=1035510200, other_entity=1035511200, radius=6.0))
    AND_9.Add(OR_14)
    GotoIfConditionFalse(Label.L0, input_condition=AND_9)
    EnableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_dummy_id=220, state=True)
    AddSpecialEffect(1035510200, 14501)
    AddSpecialEffect(1035510200, 14502)
    WaitFrames(frames=1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableHealthBar(1035510200)
    SetLockOnPoint(character=1035510200, lock_on_dummy_id=220, state=False)
    AddSpecialEffect(1035510200, 14500)
    WaitFrames(frames=1)
    Restart()
