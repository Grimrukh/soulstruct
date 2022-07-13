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
    RunCommonEvent(0, 90005220, args=(1048560210, 30004, 20004, 0.0, 0, 1, 1), arg_types="IiifIII")
    Event_1048562350(2, character__region=1048560352, character=1048560372)
    Event_1048562350(5, character__region=1048560355, character=1048560374)
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1048560180, 1048562181, 1048562182, 1048560700, 22, 1048562180, 1048562181, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1048560180, 1048562181, 1048562182, 1048560700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1048560180, 1048562181, 1048562182, 1048560700, 1048560800, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1048560180, 1048562181, 1048562182, 1048560700, 1048562180, 1048562182, 0),
        arg_types="IIIIIIi",
    )


@RestartOnRest(1048562350)
def Event_1048562350(_, character__region: uint, character: uint):
    """Event 1048562350"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    SetCharacterEventTarget(character, region=character__region)
    IfCharacterHasSpecialEffect(AND_1, character, 11893)
    IfCharacterAlive(AND_1, character__region)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkUpdateRate(character__region, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=283,
        set_draw_parent=0,
    )
    WaitFrames(frames=1)
    ForceAnimation(character, 20003, unknown2=1.0)
    AddSpecialEffect(character__region, 11880)
    AddSpecialEffect(character, 11880)
    ReplanAI(character__region)
    Wait(5.0)
    SetNetworkUpdateRate(character__region, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@NeverRestart(100)
def Event_100():
    """Event 100"""
    RunCommonEvent(0, 90005300, args=(1148560200, 1148560200, 40524, 0.0, 0), arg_types="IIifi")
