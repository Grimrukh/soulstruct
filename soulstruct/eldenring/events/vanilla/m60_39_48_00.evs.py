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

    # --- Label 0 --- #
    DefineLabel(0)
    RunCommonEvent(0, 900005610, args=(1039481680, 100, 800, 1039488600), arg_types="IiiI")
    Event_1039482510()
    RunCommonEvent(
        0,
        90005501,
        args=(1039480510, 1039480511, 0, 1039481510, 1039481511, 1039481512, 1039480512),
        arg_types="IIIIIII",
    )
    Event_1039482610()
    Event_1039482611()
    RunCommonEvent(0, 90005300, args=(1039480340, 1039480340, 0, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1039480519()
    RunCommonEvent(0, 90005251, args=(1039480200, 10.0, 0.0, 1700), arg_types="Iffi")


@RestartOnRest(1039482510)
def Event_1039482510():
    """Event 1039482510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1039480510,
            1039480511,
            0,
            1039481510,
            1039481511,
            1039483511,
            1039481512,
            1039483512,
            1039482511,
            1039482512,
            1039480512,
            1039480513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1039480519)
def Event_1039480519():
    """Event 1039480519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1039480510)
    DisableThisSlotFlag()


@RestartOnRest(1039482610)
def Event_1039482610():
    """Event 1039482610"""
    GotoIfFlagDisabled(Label.L0, flag=1039480610)
    DisableObject(1039481610)
    DeleteObjectVFX(1039481610)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(1039481610)
    CreateObjectVFX(1039481610, vfx_id=200, model_point=1502)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1039480610)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 485)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 486)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1039480610)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
    PlaySoundEffect(1039481610, 1500, sound_type=SoundType.s_SFX)
    DisableObject(1039481610)
    DeleteObjectVFX(1039481610)
    End()


@RestartOnRest(1039482611)
def Event_1039482611():
    """Event 1039482611"""
    DisableNetworkSync()
    EndIfFlagEnabled(1039480610)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=1039481610)
    IfFlagEnabled(OR_1, 1039480610)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1039480610)
    DisplayDialog(text=20200, anchor_entity=1039481610)
    Wait(1.0)
    Restart()
