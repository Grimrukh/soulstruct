"""
linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044380000, obj=1044381950, unknown=5.0)
    RunCommonEvent(0, 90005460, args=(1044380200,))
    RunCommonEvent(0, 90005461, args=(1044380200,))
    RunCommonEvent(0, 90005462, args=(1044380200,))
    RunCommonEvent(0, 90005300, args=(1044380210, 1044380210, 40142, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005632, args=(580000, 1044381600, 80000), arg_types="IIi")
    Event_1044382220()
    RunCommonEvent(0, 90005704, args=(1044380710, 3621, 3620, 1043379251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1044380710, 3621, 3622, 1043379251, 3621, 3620, 3624, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1044380710, 1044389209, 1044389209, 1044389209), arg_types="IIII")
    Event_1044383720(0, character=1044380710)
    Event_1044383721(0, 1044380710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044380700)
    DisableBackread(1044380701)
    DisableBackread(1044380702)
    DisableBackread(1044380710)
    RunCommonEvent(0, 90005251, args=(1044380340, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1044380200, 1044382200, 1.0, 1700), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044380201, 1044382200, 0.30000001192092896, 1700), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044380202, 1044382200, 0.0, 1700), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044380203, 1044382200, 0.0, 1700), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1044380204, 1044382200, 0.5, 1700), arg_types="IIfi")


@RestartOnRest(1044382220)
def Event_1044382220():
    """Event 1044382220"""
    IfFlagDisabled(AND_1, 3625)
    IfFlagEnabled(AND_1, 1044380220)
    SkipLinesIfConditionFalse(3, AND_1)
    EnableCharacter(1044385220)
    EnableAnimations(1044385220)
    End()
    IfFlagEnabled(MAIN, 3625)
    DisableCharacter(1044385220)
    DisableAnimations(1044385220)
    EnableFlag(1044380220)
    Wait(1.0)
    Restart()


@RestartOnRest(1044382600)
def Event_1044382600(_, obj: uint, item_lot_param_id: int, flag: uint):
    """Event 1044382600"""
    EndIfFlagEnabled(flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=806840)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9310, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot_param_id, host_only=False)
    EnableFlag(flag)


@RestartOnRest(1044383720)
def Event_1044383720(_, character: uint):
    """Event 1044383720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3620)
    DisableFlag(1043379255)
    DisableFlag(1043369200)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagDisabled(OR_1, 1043372717)
    IfFlagEnabled(OR_1, 1043372718)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(OR_11, 1043369200)
    IfFlagEnabled(OR_11, 1043360800)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfFlagEnabled(AND_1, 3625)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagDisabled(OR_3, 1043372717)
    IfFlagEnabled(OR_3, 1043372718)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfFlagDisabled(OR_13, 1043369200)
    IfFlagEnabled(OR_13, 1043360800)
    IfConditionTrue(AND_3, input_condition=OR_13)
    IfFlagEnabled(AND_3, 3625)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
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
    IfFlagDisabled(OR_4, 1043372717)
    IfFlagEnabled(OR_4, 1043372718)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagDisabled(OR_14, 1043369200)
    IfFlagEnabled(OR_14, 1043360800)
    IfConditionTrue(AND_4, input_condition=OR_14)
    IfFlagEnabled(AND_4, 3625)
    IfConditionFalse(MAIN, input_condition=AND_4)
    Restart()


@RestartOnRest(1044383721)
def Event_1044383721(_, character: uint):
    """Event 1044383721"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043359259)
    EndIfFlagEnabled(1035469209)
    EndIfFlagEnabled(1039529209)
    GotoIfFlagEnabled(Label.L1, flag=1044389209)
    IfFlagEnabled(MAIN, 1044389209)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    EndIfFlagEnabled(3625)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()
