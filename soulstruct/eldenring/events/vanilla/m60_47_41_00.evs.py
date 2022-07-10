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
    Event_1047412300()
    Event_1047412301()
    Event_1047412302()
    Event_1047412306()
    Event_1047412305()
    Event_1047412400()
    RunCommonEvent(
        0,
        90005793,
        args=(1047419201, 1047412220, 1047410230, 1047410701, 1047412200, 0, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1047419201, 1047412221, 1047410231, 1047410702, 1047412201, 0, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1047419201, 1047412222, 1047410232, 1047410703, 1047412202, 0, 0),
        arg_types="IIIIIIi",
    )


@NeverRestart(100)
def Event_100():
    """Event 100"""
    Event_1047412304(0, character=1047410700)
    Event_1047410700()
    Event_1047410701()
    Event_1047410702()


@NeverRestart(150)
def Event_150():
    """Event 150"""
    Event_1047412303(0, 1047410700)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005485, args=(1047410300,))


@RestartOnRest(1047412300)
def Event_1047412300():
    """Event 1047412300"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    GotoIfFlagEnabled(Label.L0, flag=1047412350)
    DisableCharacter(1047410701)
    DisableCharacter(1047410702)
    DisableCharacter(1047410703)
    EndIfFlagEnabled(1047419201)
    EndIfPlayerNotInOwnWorld()
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_1, 1047419200)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1047412310)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfNewGameCycleEqual(AND_5, completion_count=0)
    SkipLinesIfConditionFalse(4, AND_5)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23731, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23741, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23751, unk_8_12=1047410703)
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_6, completion_count=1)
    SkipLinesIfConditionFalse(4, AND_6)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23732, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23742, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23752, unk_8_12=1047410703)
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_7, completion_count=2)
    SkipLinesIfConditionFalse(4, AND_7)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23733, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23743, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23753, unk_8_12=1047410703)
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_8, completion_count=3)
    SkipLinesIfConditionFalse(4, AND_8)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23734, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23744, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23754, unk_8_12=1047410703)
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_9, completion_count=4)
    SkipLinesIfConditionFalse(4, AND_9)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23735, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23745, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23755, unk_8_12=1047410703)
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_10, completion_count=5)
    SkipLinesIfConditionFalse(4, AND_10)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23736, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23746, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23756, unk_8_12=1047410703)
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_11, completion_count=6)
    SkipLinesIfConditionFalse(4, AND_11)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23737, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23747, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23757, unk_8_12=1047410703)
    Goto(Label.L0)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23738, unk_8_12=1047410701)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23748, unk_8_12=1047410702)
    Unknown_2004_78(unk_0_4=1, unk_4_8=23758, unk_8_12=1047410703)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(1047412350)
    IfCharacterDead(AND_2, 1047410701)
    SkipLinesIfConditionTrue(2, AND_2)
    PlaceSummonSign(
        sign_type=SummonSignType.RedEyeSign,
        character=1047410701,
        region=1047412200,
        summon_flag=1047412220,
        dismissal_flag=1047410230,
        unknown=0,
    )
    CreateObjectVFX(1047411300, vfx_id=100, model_point=30090)
    IfCharacterDead(AND_3, 1047410702)
    SkipLinesIfConditionTrue(2, AND_3)
    PlaceSummonSign(
        sign_type=SummonSignType.RedEyeSign,
        character=1047410702,
        region=1047412201,
        summon_flag=1047412221,
        dismissal_flag=1047410231,
        unknown=0,
    )
    CreateObjectVFX(1047411301, vfx_id=100, model_point=30090)
    IfCharacterDead(AND_4, 1047410703)
    SkipLinesIfConditionTrue(2, AND_4)
    PlaceSummonSign(
        sign_type=SummonSignType.RedEyeSign,
        character=1047410703,
        region=1047412202,
        summon_flag=1047412222,
        dismissal_flag=1047410232,
        unknown=0,
    )
    CreateObjectVFX(1047411302, vfx_id=100, model_point=30090)
    IfTryingToJoinSession(MAIN)
    Unknown_2003_82(character=1047410701)
    Unknown_2003_82(character=1047410702)
    Unknown_2003_82(character=1047410703)
    DeleteObjectVFX(1047411300)
    DeleteObjectVFX(1047411301)
    DeleteObjectVFX(1047411302)
    Wait(1.0)
    Restart()


@RestartOnRest(1047412301)
def Event_1047412301():
    """Event 1047412301"""
    EndIfFlagEnabled(1047419201)
    IfFlagEnabled(AND_1, 1047419200)
    IfCharacterDead(AND_1, 1047410701)
    IfCharacterDead(AND_1, 1047410702)
    IfCharacterDead(AND_1, 1047410703)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1047419201)


@RestartOnRest(1047412302)
def Event_1047412302():
    """Event 1047412302"""
    EndIfFlagEnabled(1047419201)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1047412300)
    Unknown_2004_79(unk_0_4=1, unk_4_8=3)


@RestartOnRest(1047412303)
def Event_1047412303(_, character__unk_0_4: uint):
    """Event 1047412303"""
    DisableNetworkSync()
    SetBackreadStateAlternate(character__unk_0_4, True)
    Unknown_2004_63(unk_0_4=character__unk_0_4, unk_4_8=430.0)
    Unknown_2004_69(unk_0_4=character__unk_0_4, unk_4_8=0)
    Unknown_2004_70(unk_0_4=character__unk_0_4, unk_4_8=1)


@RestartOnRest(1047412304)
def Event_1047412304(_, character: uint):
    """Event 1047412304"""
    DisableNetworkSync()
    DisableGravity(character)
    IfEntityWithinDistance(MAIN, entity=character, other_entity=PLAYER, radius=200.0)
    EnableGravity(character)
    IfEntityBeyondDistance(MAIN, entity=character, other_entity=PLAYER, radius=220.0)
    Restart()


@RestartOnRest(1047412305)
def Event_1047412305():
    """Event 1047412305"""
    GotoIfFlagEnabled(Label.L2, flag=1047419201)
    IfCharacterInsideRegion(AND_15, character=PLAYER, region=1047412400)
    IfFlagEnabled(AND_15, 1047419200)
    IfConditionTrue(MAIN, input_condition=AND_15)
    IfMultiplayerState(AND_5, state=MultiplayerState.Unknown6)
    IfFailedToCreateSession(OR_1)
    IfConditionFalse(AND_5, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=AND_5)
    IfFlagEnabled(AND_2, 1047412220)
    IfCharacterAlive(AND_2, 1047410701)
    IfFailedToCreateSession(AND_2)
    IfFlagEnabled(AND_3, 1047412221)
    IfCharacterAlive(AND_3, 1047410702)
    IfFailedToCreateSession(AND_3)
    IfFlagEnabled(AND_4, 1047412222)
    IfCharacterAlive(AND_4, 1047410703)
    IfFailedToCreateSession(AND_4)
    IfConditionTrue(OR_15, input_condition=AND_1)
    IfConditionTrue(OR_15, input_condition=AND_2)
    IfConditionTrue(OR_15, input_condition=AND_3)
    IfConditionTrue(OR_15, input_condition=AND_4)
    GotoIfConditionTrue(Label.L0, input_condition=OR_15)
    GotoIfConditionFalse(Label.L1, input_condition=OR_15)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(1047411500)
    EnableObject(1047411501)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(1047411500)
    DisableObject(1047411501)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableObject(1047411500)
    DisableObject(1047411501)
    End()


@RestartOnRest(1047412306)
def Event_1047412306():
    """Event 1047412306"""
    EndIfFlagEnabled(1047419200)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 1047419200)
    Wait(0.30000001192092896)
    DisplayDialog(text=30110, anchor_entity=1047411300)


@RestartOnRest(1047412400)
def Event_1047412400():
    """Event 1047412400"""
    DisableNetworkSync()
    IfCharacterInsideRegion(MAIN, character=20000, region=1047412400)
    AddSpecialEffect(20000, 514)
    Wait(1.0)
    IfCharacterOutsideRegion(MAIN, character=20000, region=1047412401)
    CancelSpecialEffect(20000, 514)
    Restart()


@RestartOnRest(1047410700)
def Event_1047410700():
    """Event 1047410700"""
    ForceAnimation(1047410700, 30003, unknown2=1.0)
    DisableHealthBar(1047410700)
    EnableImmortality(1047410700)


@RestartOnRest(1047410701)
def Event_1047410701():
    """Event 1047410701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400470)
    DisableNetworkSync()
    IfFlagEnabled(MAIN, 400470)
    Unknown_2004_80(unk_0_4=1)


@RestartOnRest(1047410702)
def Event_1047410702():
    """Event 1047410702"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=1047410700, distance=50.0)
    End()
