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
    RunCommonEvent(0, 90005600, args=(76350, 1039531950, 5.0, 0), arg_types="IIfI")
    RunCommonEvent(
        0,
        90005100,
        args=(71602, 76350, 1039531980, 77350, 1, 78350, 78351, 78352, 78353, 78354, 78355, 78356, 78357, 78358, 78359),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005261, args=(1039530350, 1039532350, 60.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1039530360, 30005, 20005, 1039532360, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1039532400()
    Event_1039532650()
    Event_1039532660()
    Event_1039532600()
    Event_1039532610()
    Event_1039532300()
    Event_1039532670()
    RegisterLadder(start_climbing_flag=1039530580, stop_climbing_flag=1039530581, obj=1039531580)
    RunCommonEvent(
        0,
        90005795,
        args=(7603, 0, 1039539200, 1039532141, 1039532142, 80603, 9000, 1039531700, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=20)
    RunCommonEvent(0, 90005796, args=(7603, 1039530700, 5, 1039532141), arg_types="IIBI")
    Event_1039532145()
    Event_1039533700()
    RunCommonEvent(0, 90005774, args=(7603, 1039530700, 1039537700), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039530700)


@NeverRestart(100)
def Event_100():
    """Event 100"""
    Event_1039532500()


@RestartOnRest(1039532145)
def Event_1039532145():
    """Event 1039532145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(1039530700)
    SetTeamType(1039530700, TeamType.Human)
    DeleteObjectVFX(1039536700)
    CreateObjectVFX(1039536700, vfx_id=200, model_point=806700)


@RestartOnRest(1039532300)
def Event_1039532300():
    """Event 1039532300"""
    EndIfThisEventSlotFlagEnabled()
    EnableObjectInvulnerability(1039531426)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(1039532400)
def Event_1039532400():
    """Event 1039532400"""
    GotoIfFlagEnabled(Label.L0, flag=1039530510)
    DisableObject(1039536400)
    DisableObject(1039531480)
    DisableTreasure(obj=1039533501)
    DisableObject(1039531481)
    DisableTreasure(obj=1039533502)
    IfFlagEnabled(AND_1, 1039530655)
    IfFlagEnabled(AND_1, 1039520655)
    IfFlagEnabled(AND_1, 1040530655)
    IfAllPlayersOutsideRegion(AND_1, region=1039532260)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1039530510)
    Wait(2.0)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(1039536400)
    EnableObject(1039531480)
    EnableTreasure(obj=1039533501)
    EnableObject(1039531481)
    EnableTreasure(obj=1039533502)
    End()


@RestartOnRest(1039532500)
def Event_1039532500():
    """Event 1039532500"""
    GotoIfFlagEnabled(Label.L0, flag=1039530505)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=1039531500, radius=100.0)
    EnableNetworkFlag(1039530505)
    CreateTemporaryVFX(vfx_id=806850, anchor_entity=1039531500, anchor_type=CoordEntityType.Object)
    ForceAnimation(1039531500, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1039531500)
    Wait(1.0)
    Restart()


@RestartOnRest(1039532600)
def Event_1039532600():
    """Event 1039532600"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9210, entity=1039531600)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=60031, anchor_entity=1039531600, number_buttons=NumberButtons.OneButton)
    SkipLinesIfFlagEnabled(1, 1039537080)
    AwardItemLot(1039530080, host_only=True)
    Wait(1.0)
    Restart()


@RestartOnRest(1039532610)
def Event_1039532610():
    """Event 1039532610"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1039537080)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1039537080)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(2.0)
    DisplayDialog(text=30101, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)


@RestartOnRest(1039532650)
def Event_1039532650():
    """Event 1039532650"""
    GotoIfFlagEnabled(Label.L0, flag=1039530655)
    DisableObject(1039531650)
    DeleteVFX(1039532650, erase_root_only=False)
    IfFlagEnabled(MAIN, 1039530505)
    EnableObject(1039531650)
    CreateVFX(1039532650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1039531650)
    DeleteVFX(1039532650, erase_root_only=False)
    End()


@RestartOnRest(1039532660)
def Event_1039532660():
    """Event 1039532660"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1039530655)
    IfFlagEnabled(AND_1, 1039530505)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1039532651)
    IfActionButtonParamActivated(AND_1, action_button_id=9521, entity=1039531650)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1039530655)
    DisableObject(1039531650)
    RotateToFaceEntity(PLAYER, 1039531650, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.0)
    PlaySoundEffect(1039532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1039532650)
    End()


@RestartOnRest(1039532670)
def Event_1039532670():
    """Event 1039532670"""
    AwaitFlagEnabled(flag=1039530510)
    MoveRemains(source_region=1039532270, destination_region=1039532272)
    MoveRemains(source_region=1039532271, destination_region=1039532272)


@RestartOnRest(1039533700)
def Event_1039533700():
    """Event 1039533700"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(400074)
    EnableFlag(1039539200)
    End()
