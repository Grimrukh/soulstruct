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
    RegisterGrace(grace_flag=1038460000, obj=1038461950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(1038461610, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005511, args=(1038460560, 1038461550, 1038463560, 257018, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1038460560, 1038462550, 1038462551), arg_types="III")
    RunCommonEvent(0, 90005640, args=(1038460540, 1038461540), arg_types="II")
    Event_1038462200(0, character=1038460200)
    Event_1038462200(1, character=1038460201)
    Event_1038462200(2, character=1038460202)
    RunCommonEvent(0, 90005300, args=(1038460340, 1038460340, 0, 0.0, 0), arg_types="IIifi")
    Event_1038460510()
    RunCommonEvent(
        0,
        90005501,
        args=(1038460650, 1038460651, 0, 1038461650, 1038461651, 1038461652, 1038460652),
        arg_types="IIIIIII",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1038460519()
    Event_1038462340()


@RestartOnRest(1038462200)
def Event_1038462200(_, character: uint):
    """Event 1038462200"""
    Kill(character)


@RestartOnRest(1038462210)
def Event_1038462210(_, character: uint):
    """Event 1038462210"""
    DisableCharacter(character)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1038462210)
    CreateObjectVFX(1038461210, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    Wait(2.0)
    DeleteObjectVFX(1038461210)
    ForceAnimation(character, 20001, wait_for_completion=True, unknown2=1.0)
    End()


@RestartOnRest(1038462340)
def Event_1038462340():
    """Event 1038462340"""
    EndIfFlagEnabled(1038460340)
    DisableHealthBar(1038460340)
    AddSpecialEffect(1038460340, 12189)
    Wait(3.0)
    CancelSpecialEffect(1038460340, 12189)
    EnableHealthBar(1038460340)


@NeverRestart(1038460510)
def Event_1038460510():
    """Event 1038460510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1038460650,
            1038460651,
            0,
            1038461650,
            1038461651,
            1038463651,
            1038461652,
            1038463652,
            1038462651,
            1038462652,
            1038460652,
            1038462653,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1038460519)
def Event_1038460519():
    """Event 1038460519"""
    EndIfThisEventSlotFlagEnabled()
    IfOutsideMap(MAIN, game_map=AINSEL_RIVER)
    EnableFlag(1038460650)
