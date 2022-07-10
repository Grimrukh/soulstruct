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
    RegisterGrace(grace_flag=1052570000, obj=1052571950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76504, 1052571980, 77500, 3, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005211, args=(1052570205, 30018, 20018, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1052570215, 30019, 20019, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(1052570240, 1052572240, 0.0, 3010), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1052570241, 1052572240, 0.5, 3010), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1052570243, 1052572243, 0.0, 3032), arg_types="IIfi")
    Event_1052572200(0, character=1052575200)
    RunCommonEvent(0, 90005261, args=(1052570320, 1052572320, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1052570321, 1052572321, 3.0, 0.0, 0), arg_types="IIffi")
    Event_1052572210()
    Event_1052572220()
    Event_1052572230()
    RunCommonEvent(0, 90005560, args=(1052570490, 1052571490, 0), arg_types="IIi")
    Event_1052572510()
    RunCommonEvent(
        0,
        90005501,
        args=(1052570510, 1052570511, 0, 1052571510, 1052571511, 1052571512, 1052570512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005630, args=(65525700, 1052571500, 125), arg_types="IIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1052570519()


@RestartOnRest(1052572200)
def Event_1052572200(_, character: uint):
    """Event 1052572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1052572210)
def Event_1052572210():
    """Event 1052572210"""
    GotoIfFlagEnabled(Label.L0, flag=1052570210)
    DeleteObjectVFX(1052571210)
    CreateObjectVFX(1052571210, vfx_id=200, model_point=1500)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1052572210)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1052570210)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1052571210)
    DeleteObjectVFX(1052571210)
    PlaySoundEffect(1052571210, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1052572220)
def Event_1052572220():
    """Event 1052572220"""
    DisableNetworkSync()
    EndIfFlagEnabled(1052570210)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=1052571210)
    IfFlagEnabled(OR_1, 1052570210)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1052570210)
    DisplayDialog(text=20200, anchor_entity=1052571210)
    Wait(1.0)
    Restart()


@RestartOnRest(1052572230)
def Event_1052572230():
    """Event 1052572230"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9210, entity=1052571230)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=60051, anchor_entity=1052571230)
    Wait(1.0)
    Restart()


@NeverRestart(1052572510)
def Event_1052572510():
    """Event 1052572510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1052570510,
            1052570511,
            0,
            1052571510,
            1052571511,
            1052573511,
            1052571512,
            1052573512,
            1052572511,
            1052572512,
            1052570512,
            1052570513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1052570519)
def Event_1052570519():
    """Event 1052570519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1052570510)
