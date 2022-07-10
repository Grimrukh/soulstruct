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
    RegisterGrace(grace_flag=76304, obj=1040521950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76314, 76304, 1040521980, 77310, 0, 78310, 78311, 78312, 78313, 78314, 78315, 78316, 78317, 78318, 78319),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005870, args=(1040520800, 902100600, 14), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1040520800, 0, 1040520800, 0, 30350, 0.0), arg_types="IIIIif")
    Event_1040522240(0, obj=1040521690, entity=1040521691, flag=62030)
    Unknown_2005_18(obj_1=1040521201, obj_2=1040521200, unk_8_12=151)
    Unknown_2005_18(obj_1=1040521211, obj_2=1040521210, unk_8_12=151)
    RunCommonEvent(0, 900005610, args=(1040521680, 100, 800, 1040528620), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005605,
        args=(1040521640, 60, 40, 55, 0, 1040552650, 0, 1040552651, 1040552652, 1040552653, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_1040523700(0, character=1040520700)
    Event_1040523701(0, attacked_entity=1040520700, flag=1040529205, flag_1=1040529206)
    Event_1040523702(0, entity=1040520700, attacked_entity=1040520710, flag=1040529206)
    Event_1040523703(0, character=1040520710)
    Event_1040523705(0, character=1040520705)
    RunCommonEvent(0, 90005704, args=(1040520705, 4201, 4200, 1040529251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1040520705, 4201, 4202, 1040529251, 4201, 4200, 4203, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1040520705, 4203, 4200, 4204), arg_types="IIII")
    RunCommonEvent(
        0,
        90005725,
        args=(4765, 4766, 4768, 1040529305, 1040520715, 1035450701, 1040526700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1040520715, 4766, 4767, 1035469206, 4766, 4765, 4769, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1040520715, 4766, 4765, 1035469206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1040520715, 4768, 4765, 4769), arg_types="IIII")
    RunCommonEvent(0, 90005705, args=(1040520720,))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1040520705)
    DisableBackread(1040520715)
    DisableBackread(1040520720)
    RunCommonEvent(0, 90005201, args=(1040520303, 30001, 20001, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1040520304, 30002, 20002, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1040520800, 30000, 20000, 1040522800, 20.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(1040522240)
def Event_1040522240(_, obj: uint, entity: uint, flag: uint):
    """Event 1040522240"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1040523700)
def Event_1040523700(_, character: uint):
    """Event 1040523700"""
    WaitFrames(frames=1)
    DisableFlag(1040529200)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3620)
    IfFlagEnabled(AND_1, 1043379255)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3630)
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    IfFlagEnabled(OR_2, 1040529205)
    IfFlagEnabled(OR_2, 1040529206)
    IfFlagEnabled(OR_2, 1040529207)
    SkipLinesIfConditionFalse(5, OR_2)
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    ForceAnimation(character, 90102, unknown2=1.0)
    Goto(Label.L20)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
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
    IfFlagEnabled(MAIN, 1040529200)
    Restart()


@RestartOnRest(1040523701)
def Event_1040523701(_, attacked_entity: uint, flag: uint, flag_1: uint):
    """Event 1040523701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3620)
    EndIfFlagDisabled(3630)
    IfFlagEnabled(OR_1, flag)
    IfFlagEnabled(OR_1, flag_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=PLAYER)
    EndIfConditionTrue(input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableAnimations(attacked_entity)
    EndIfFlagEnabled(flag)
    ForceAnimation(attacked_entity, 90201, unknown2=1.0)
    EndIfFlagEnabled(flag_1)
    EnableFlag(1040529207)
    End()


@RestartOnRest(1040523702)
def Event_1040523702(_, entity: uint, attacked_entity: uint, flag: uint):
    """Event 1040523702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3630)
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=PLAYER)
    EnableFlag(flag)
    DisableAnimations(entity)
    End()


@RestartOnRest(1040523703)
def Event_1040523703(_, character: uint):
    """Event 1040523703"""
    WaitFrames(frames=1)
    GotoIfFlagRangeAllDisabled(Label.L1, flag_range=(3620, 3624))
    GotoIfFlagRangeAnyEnabled(Label.L1, flag_range=(3625, 3629))
    GotoIfFlagEnabled(Label.L1, flag=3632)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
    End()


@RestartOnRest(1040523705)
def Event_1040523705(_, character: uint):
    """Event 1040523705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4200)
    DisableFlag(1040529253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4206)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4206)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    IfFlagDisabled(MAIN, 4206)
    Restart()
