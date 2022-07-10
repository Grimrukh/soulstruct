"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049370000, obj=1049371950, unknown=5.0)
    RunCommonEvent(0, 90005251, args=(1049370200, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1049370800, 1049370801, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005476, args=(1049370800, 1049370801), arg_types="II")
    Event_1049372291(0, character=1049370800, character_1=1049370801)
    RunCommonEvent(0, 90005871, args=(1049370800, 903150605, 10, 1049370801), arg_types="IiII")
    RunCommonEvent(0, 90005860, args=(1049370800, 0, 1049370800, 0, 1049370100, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1049370800, 10, 0), arg_types="III")
    RunCommonEvent(0, 90005870, args=(1049370850, 904980606, 24), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1049370850, 0, 1049370850, 0, 1049370110, 0.0), arg_types="IIIIif")
    Event_1049372299()
    RunCommonEvent(0, 90005300, args=(1049370299, 1049370299, 1049370700, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005725,
        args=(4780, 4781, 4783, 1049379205, 1049370700, 1049370701, 1049376700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1049370700, 4781, 4782, 1049379206, 4781, 4780, 4784, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1049370700, 4781, 4780, 1049379206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1049370700, 4783, 4780, 4784), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1049370701, 4781, 4782, 1049379207, 4781, 4780, 4784, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1049370701, 4781, 4780, 1049379207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1049370701, 1049372706, 1049372707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4781, 1049370700, 1049370701, 4780, 4783), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1049370700)
    DisableBackread(1049370701)


@RestartOnRest(1049372291)
def Event_1049372291(_, character: uint, character_1: uint):
    """Event 1049372291"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterBackreadEnabled(AND_3, character_1)
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterBackreadDisabled(AND_4, character_1)
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1049372299)
def Event_1049372299():
    """Event 1049372299"""
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1049372299)
    ChangePatrolBehavior(1049370299, patrol_information_id=1049373299)
