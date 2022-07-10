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
    RunCommonEvent(0, 900005610, args=(1045371610, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005251, args=(1045370201, 80.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045370207, 50.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045370214, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045370216, 50.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005511, args=(1045370560, 1045374550, 1045373560, 257018, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1045370560, 1045372550, 1045372551), arg_types="III")
    RunCommonEvent(0, 90005640, args=(1045370560, 1045374550), arg_types="II")
    Event_1045372230()
    RunCommonEvent(0, 90005261, args=(1045370240, 1045372240, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045370230, 1045372240, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045370231, 1045372240, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045370232, 1045372240, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1045370233, 1045372240, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1045370340, 4.0, 1.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1045370364, 30002, 20002, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1045372344()
    RunCommonEvent(0, 90005300, args=(1045370200, 1045370200, 40116, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005400, args=(1045370370, 0, 0.0, 0.0, 0), arg_types="IiffI")
    RunCommonEvent(0, 90005401, args=(98101, 1045370370), arg_types="II")
    RunCommonEvent(0, 90005637, args=(1045378601, 1045370620, 1045371620), arg_types="III")
    RunCommonEvent(
        0,
        90005636,
        args=(1045378601, 1045370620, 1045371620, 4470, 1045372620, 1045372621, 1045372620, 1045373620, -1),
        arg_types="IIIiIIIIi",
    )
    RunCommonEvent(0, 90005704, args=(1045370700, 3601, 3600, 1045379201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1045370700, 3601, 3602, 1045379201, 3603, 3600, 3603, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1045370700, 3603, 3600, 3604), arg_types="IIII")
    Event_1045370710(0, character=1045370700)
    Event_1045370711(0, character=1045370700, destination=1045372700)
    Event_1045370714(0, character=1045370700)
    Event_1045370713()
    RunCommonEvent(0, 90005731, args=(1045379221, 1045370700, 70.0, 90.0), arg_types="IIff")
    RunCommonEvent(0, 90005730, args=(1045379220, 60.0, 1045379221, 3605, 1045370711, 1045379223), arg_types="IfIIII")
    RunCommonEvent(0, 90005732, args=(1045379223, 1045372701, 1045372701), arg_types="III")
    RunCommonEvent(0, 90005730, args=(1045379222, 15.0, 1045379223, 3605, 1045370711, 1045372706), arg_types="IfIIII")
    Event_1045370720()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045370700)
    DisableBackread(1045370701)
    EnableObjectInvulnerability(1045371700)


@RestartOnRest(1045372200)
def Event_1045372200(_, obj: uint, entity: uint, flag: uint):
    """Event 1045372200"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1045372230)
def Event_1045372230():
    """Event 1045372230"""
    DropMandatoryTreasure(1045370234)
    DropMandatoryTreasure(1045370235)
    End()


@RestartOnRest(1045372344)
def Event_1045372344():
    """Event 1045372344"""
    RestoreObject(1045371364)


@RestartOnRest(1045370650)
def Event_1045370650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1045370650"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=EAST_LIMGRAVE_SW_NE)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9120, flag=flag_1, bit_count=1)


@RestartOnRest(1045370710)
def Event_1045370710(_, character: uint):
    """Event 1045370710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3600)
    DisableFlag(1045379202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=3605)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3605)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    SkipLinesIfFlagEnabled(2, 1045370711)
    ForceAnimation(character, 930012, unknown2=1.0)
    Goto(Label.L20)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3605)
    Restart()


@RestartOnRest(1045370711)
def Event_1045370711(_, character: uint, destination: uint):
    """Event 1045370711"""
    EndIfThisEventSlotFlagEnabled()
    DisableNetworkSync()
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    IfFlagEnabled(AND_2, 3600)
    IfFlagEnabled(AND_2, 3605)
    IfThisEventSlotFlagEnabled(OR_2)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetTeamType(character, TeamType.NoTeam)
    DisableAI(character)
    EnableInvincibility(character)
    IfCharacterBackreadEnabled(MAIN, character)
    WaitFrames(frames=1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EndIfPlayerNotInOwnWorld()
    EnableNetworkSync()
    IfFlagEnabled(AND_1, 3600)
    IfFlagEnabled(AND_1, 3605)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9672)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1045372701)
    IfThisEventSlotFlagEnabled(OR_1)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(0.30000001192092896)
    ForceAnimation(character, 20055, unknown2=1.0)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    WaitFrames(frames=1)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9671)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableAI(character)
    EnableFlag(1045372707)
    DisableInvincibility(character)


@RestartOnRest(1045370712)
def Event_1045370712():
    """Event 1045370712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045370711)
    DisableNetworkSync()
    IfFlagDisabled(MAIN, 1045379221)
    IfFlagEnabled(AND_1, 3600)
    IfFlagEnabled(AND_1, 3605)
    IfFlagDisabled(AND_1, 1045372705)
    IfFlagEnabled(AND_1, 1045379221)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1045379220)


@RestartOnRest(1045370713)
def Event_1045370713():
    """Event 1045370713"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045370711)
    DisableNetworkSync()
    IfFlagEnabled(MAIN, 1045372706)
    Wait(15.0)
    DisableFlag(1045372706)
    Restart()


@RestartOnRest(1045370714)
def Event_1045370714(_, character: uint):
    """Event 1045370714"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045370711)
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1045372705)
    SetCharacterTalkRange(character=character, distance=160.0)
    IfFlagEnabled(AND_1, 3600)
    IfFlagEnabled(AND_1, 3605)
    IfFlagEnabled(AND_1, 1045372705)
    IfFlagEnabled(AND_2, 3600)
    IfFlagEnabled(AND_2, 3605)
    IfFlagEnabled(AND_2, 1045370711)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=character, distance=160.0)
    IfFlagEnabled(AND_3, 3600)
    IfFlagEnabled(AND_3, 3605)
    IfFlagEnabled(AND_3, 1045370711)
    IfConditionTrue(MAIN, input_condition=AND_3)
    SetCharacterTalkRange(character=character, distance=17.0)
    End()


@RestartOnRest(1045370720)
def Event_1045370720():
    """Event 1045370720"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045379250)
    EndIfFlagDisabled(31008522)
    EnableFlag(1045379250)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=1045372710, radius=1.0)
    EndIfConditionFalse(input_condition=AND_1)
    EnableFlag(9080)
    ForceAnimation(PLAYER, 60131, unknown2=1.0)
    SetRespawnPoint(respawn_point=1045372710)
    SaveRequest()
    End()
