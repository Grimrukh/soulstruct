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
    RegisterGrace(grace_flag=1035460000, obj=1035461950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76206, 1035461980, 77200, 6, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005201, args=(1035460350, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1035462600(
        0,
        anchor_entity=1035461600,
        area_id=60,
        block_id=35,
        cc_id=45,
        dd_id=0,
        player_start=1035452610,
        flag=1035450605,
        target_entity=1035461602,
        animation_id=60470,
        action_button_id=9522
    )
    Event_1035462600(
        1,
        anchor_entity=1035461601,
        area_id=60,
        block_id=36,
        cc_id=47,
        dd_id=0,
        player_start=1036472610,
        flag=1036470605,
        target_entity=1035461603,
        animation_id=60470,
        action_button_id=9522
    )
    Event_1035462605(0, flag=1035460605, target_entity=1035462601, animation=60471)
    Event_1035462605(1, flag=1035460615, target_entity=1035462606, animation=60471)
    RunCommonEvent(0, 900005610, args=(1035461680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005795,
        args=(7607, 0, 1035469205, 1035462141, 1035462142, 80607, 9000, 1035461700, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=40)
    RunCommonEvent(0, 90005796, args=(7607, 1035460715, 5, 1035462141), arg_types="IIBI")
    Event_1035462145()
    RunCommonEvent(0, 90005704, args=(1035460710, 3621, 3620, 1035469201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1035460710, 3621, 3622, 1035469201, 3621, 3620, 3624, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1035460710, 1035469209, 1035469209, 1035469209), arg_types="IIII")
    Event_1035463700(0, character=1035460710)
    Event_1035463701()
    Event_1035463702(0, character=1035460710)
    RunCommonEvent(0, 90005774, args=(7607, 1035460700, 1035467700), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1035460710)
    DisableBackread(1035460711)
    DisableBackread(1035460715)
    RunCommonEvent(0, 90005251, args=(1035460212, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035460213, 7.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1035462145)
def Event_1035462145():
    """Event 1035462145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=40,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(1035460715)
    EnableBackread(1035460711)
    SetTeamType(1035460715, TeamType.Human)
    SetTeamType(1035460711, TeamType.Enemy)
    DeleteObjectVFX(1035466700)
    CreateObjectVFX(1035466700, vfx_id=200, model_point=806700)


@RestartOnRest(1035463700)
def Event_1035463700(_, character: uint):
    """Event 1035463700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3620)
    DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3627)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3627)
    IfConditionTrue(MAIN, input_condition=OR_3)
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
    IfFlagEnabled(OR_4, 3627)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1035463701)
def Event_1035463701():
    """Event 1035463701"""
    WaitFrames(frames=1)
    EndIfFlagEnabled(3631)
    EndIfFlagDisabled(3620)
    EndIfFlagDisabled(1043379260)
    EnableFlag(1035469205)
    End()


@RestartOnRest(1035463702)
def Event_1035463702(_, character: uint):
    """Event 1035463702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043359259)
    EndIfFlagEnabled(1044389209)
    EndIfFlagEnabled(1039529209)
    GotoIfFlagEnabled(Label.L1, flag=1035469209)
    IfFlagEnabled(MAIN, 1035469209)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    EndIfFlagEnabled(3627)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(1035462600)
def Event_1035462600(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    flag: uint,
    target_entity: uint,
    animation_id: int,
    action_button_id: int,
):
    """Event 1035462600"""
    EndIfPlayerNotInOwnWorld()
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    SkipLinesIfConditionTrue(7, OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=action_button_id, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfPlayerHasGood(AND_9, 8109)
    GotoIfConditionTrue(Label.L1, input_condition=AND_9)
    Wait(0.10000000149011612)
    DisplayDialog(text=20030, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(PLAYER, target_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, animation_id, unknown2=1.0)
    Wait(2.5)
    EnableFlag(flag)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1035462605)
def Event_1035462605(_, flag: uint, target_entity: uint, animation: int):
    """Event 1035462605"""
    EndIfFlagDisabled(flag)
    IfFlagEnabled(MAIN, flag)
    WaitFrames(frames=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    DisableFlag(flag)
