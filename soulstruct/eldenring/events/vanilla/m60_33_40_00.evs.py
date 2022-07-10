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
    RegisterGrace(grace_flag=1033400000, obj=1033401950, unknown=5.0)
    Event_1033402510()
    RunCommonEvent(
        0,
        90005501,
        args=(1033400510, 1033400511, 0, 1033401510, 1033401511, 1033401512, 1033400512),
        arg_types="IIIIIII",
    )
    Event_1033402610(0, flag=1033400610, flag_1=1033420610, flag_2=1035410610, flag_3=1033400615)
    Event_1034432613(0, flag=1033400610, character=1033400610)
    Event_1034432614(0, flag=1033400610, attacked_entity=1033400610)
    Event_1033402611()
    Event_1034432612()
    RunCommonEvent(0, 90005201, args=(1033400610, 30006, 20006, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005300, args=(1033400610, 1033400610, 0, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1033400519()


@NeverRestart(200)
def Event_200():
    """Event 200"""
    Event_1033402615()


@RestartOnRest(1033402510)
def Event_1033402510():
    """Event 1033402510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1033400510,
            1033400511,
            0,
            1033401510,
            1033401511,
            1033403511,
            1033401512,
            1033403512,
            1033402511,
            1033402512,
            1033400512,
            1033400513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1033400519)
def Event_1033400519():
    """Event 1033400519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1033400510)
    DisableThisSlotFlag()


@RestartOnRest(1033402610)
def Event_1033402610(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 1033402610"""
    GotoIfFlagDisabled(Label.L0, flag=flag_3)
    DisableObject(1033401610)
    DeleteObjectVFX(1033401610)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(1033401610)
    CreateObjectVFX(1033401610, vfx_id=200, model_point=1500)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_3)
    PlaySoundEffect(1033401610, 1500, sound_type=SoundType.s_SFX)
    DisableObject(1033401610)
    DeleteObjectVFX(1033401610)
    End()


@RestartOnRest(1033402611)
def Event_1033402611():
    """Event 1033402611"""
    DisableNetworkSync()
    EndIfFlagEnabled(1033400615)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=1033401610)
    IfFlagEnabled(OR_1, 1033400615)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1033400615)
    DisplayDialog(text=20200, anchor_entity=1033401610)
    Wait(1.0)
    Restart()


@RestartOnRest(1034432612)
def Event_1034432612():
    """Event 1034432612"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9210, entity=1034431611)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=60026, anchor_entity=1034431611)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(1034432616)
    Wait(1.0)
    Restart()


@RestartOnRest(1034432613)
def Event_1034432613(_, flag: uint, character: uint):
    """Event 1034432613"""
    EndIfFlagEnabled(flag)
    DisableCharacter(character)
    DisableAnimations(character)
    SkipLinesIfPlayerInOwnWorld(1)
    EnableInvincibility(character)
    IfFlagEnabled(AND_1, 1034432616)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableImmortality(character)
    DisableHealthBar(character)


@RestartOnRest(1034432614)
def Event_1034432614(_, flag: uint, attacked_entity: uint):
    """Event 1034432614"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=PLAYER)
    ForceAnimation(attacked_entity, 20008, unknown2=1.0)
    EnableFlag(flag)


@RestartOnRest(1033402615)
def Event_1033402615():
    """Event 1033402615"""
    EndIfFlagEnabled(1033400615)
    IfFlagEnabled(AND_1, 1033400610)
    IfFlagEnabled(AND_1, 1033420610)
    IfFlagEnabled(AND_1, 1035410610)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
