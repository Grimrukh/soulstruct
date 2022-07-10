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
    RegisterGrace(grace_flag=1041330000, obj=1041331950, unknown=5.0)
    RunCommonEvent(0, 90005251, args=(1041330233, 8.0, 1.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330234, 8.0, 0.5, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330235, 8.0, 1.100000023841858, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330236, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330237, 8.0, 0.5, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330238, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330239, 8.0, 1.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330240, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041330241, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1041330200, 30000, 20000, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005920, args=(1041330900, 1041331900, 1041333900), arg_types="III")
    RunCommonEvent(0, 90005703, args=(1041330700, 3461, 3462, 1044369204, 3461, 3460, 3464, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1041330700, 3461, 3460, 1044369204, 3), arg_types="IIIIi")
    Event_1041333700(0, character=1041330700, character_1=1041330701)
    RunCommonEvent(
        0,
        90005740,
        args=(
            1044362702,
            1044362703,
            1044362704,
            1041330700,
            704,
            1041331700,
            704,
            0.20000000298023224,
            90204,
            -1,
            -1,
            1.2000000476837158,
        ),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(
        0,
        90005741,
        args=(1044362708, 1044362709, 1044362704, 1041330700, 90201, 0, -1, -1, 0.5),
        arg_types="IIIIiIiif",
    )
    Event_1041333705(0, character=1041330710)
    RunCommonEvent(0, 90005703, args=(1041330710, 3361, 3362, 1041339251, 3361, 3360, 3363, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1041330710, 3361, 3360, 1041339251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1041330710, 3363, 3360, 3363), arg_types="IIII")
    RunCommonEvent(0, 90005706, args=(1041330720, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1041330700)
    DisableBackread(1041330701)
    DisableBackread(1041330710)
    DisableBackread(1041330720)


@RestartOnRest(1041332800)
def Event_1041332800():
    """Event 1041332800"""
    EndIfFlagEnabled(1041330800)
    IfHealthValueLessThanOrEqual(MAIN, 1041330800, value=0)
    Wait(4.0)
    PlaySoundEffect(1041330800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1041330800)
    KillBossAndDisplayBanner(character=1041330800, banner_type=BannerType.Unknown)
    EnableObjectActivation(1041331560, obj_act_id=-1)
    EnableFlag(1041330800)


@RestartOnRest(1041332810)
def Event_1041332810():
    """Event 1041332810"""
    GotoIfFlagDisabled(Label.L0, flag=1041330800)
    DisableCharacter(1041330800)
    DisableAnimations(1041330800)
    Kill(1041330800)
    EnableObjectActivation(1041331560, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1041330800)
    IfFlagEnabled(AND_2, 1041332805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1041332800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(1041330800)
    SetNetworkUpdateRate(1041330800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1041330800, name=904133540)
    DisableObjectActivation(1041331560, obj_act_id=-1)


@RestartOnRest(1041332849)
def Event_1041332849():
    """Event 1041332849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1041330800, 1041331800, 1041332800, 1041332805, 1041335800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1041330800, 1041331800, 1041332800, 1041332805, 1041332806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1041330800, 1041331800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(1041330800, 0, 1041332805, 1041332806, 0, 1041332802, 0, 0), arg_types="IiIIIIii")
    RunCommonEvent(0, 9005812, args=(1041330800, 1041331801, 3, 0, 0), arg_types="IIiIi")


@RestartOnRest(1041333700)
def Event_1041333700(_, character: uint, character_1: uint):
    """Event 1041333700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3460)
    DisableFlag(1034509253)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3465)
    IfFlagEnabled(OR_1, 3466)
    IfFlagEnabled(OR_1, 3467)
    IfFlagEnabled(OR_1, 3468)
    IfFlagEnabled(OR_1, 3469)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(1041331701)
    IfFlagEnabled(OR_2, 3465)
    IfFlagEnabled(OR_2, 3466)
    IfFlagEnabled(OR_2, 3467)
    IfFlagEnabled(OR_2, 3468)
    IfFlagEnabled(OR_2, 3469)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L4, flag=1041339259)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    DisableObject(1041331701)
    ForceAnimation(character, 90101, unknown2=1.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableObject(1041331701)
    ForceAnimation(character, 90101, unknown2=1.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 90102, unknown2=1.0)
    SkipLinesIfFlagEnabled(1, 1041339259)
    DisableObject(1041331701)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_15, 3465)
    IfFlagDisabled(AND_15, 3466)
    IfFlagDisabled(AND_15, 3467)
    IfFlagDisabled(AND_15, 3468)
    IfFlagDisabled(AND_15, 3469)
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1041333705)
def Event_1041333705(_, character: uint):
    """Event 1041333705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3360)
    DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3369)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3369)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3369)
    Restart()
