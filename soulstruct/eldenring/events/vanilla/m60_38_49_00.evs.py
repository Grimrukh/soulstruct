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
    Event_1038492300()
    Event_1038492301()
    Event_1038492306()
    Event_1038492400()
    Event_1038492401()
    Event_1038492304()
    Event_1038492320()
    Event_1038492580()
    RunCommonEvent(0, 90005250, args=(1038490302, 1038492302, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1038490313, 1038492313, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005706, args=(1038490700, 930018, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038490700)
    Event_1038492310(0, character=1038490200)
    Event_1038492305()


@RestartOnRest(1038492300)
def Event_1038492300():
    """Event 1038492300"""
    GotoIfFlagEnabled(Label.L3, flag=1038490201)
    GotoIfFlagEnabled(Label.L0, flag=1038492207)
    GotoIfFlagEnabled(Label.L0, flag=1038492208)
    GotoIfFlagDisabled(Label.L1, flag=1038492207)
    GotoIfFlagDisabled(Label.L1, flag=1038492208)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(1038492212)
    SkipLinesIfFlagDisabled(1, 1038492210)
    DisableCharacter(1038490200)
    SetNetworkUpdateRate(1038490200, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    SkipLinesIfFlagEnabled(2, 1038492210)
    EnableCharacter(1038490200)
    SetNetworkUpdateRate(1038490200, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(1038492212)
    SkipLinesIfFlagEnabled(2, 1038492209)
    CreateObjectVFX(1038491200, vfx_id=100, model_point=806740)
    EnableFlag(1038492209)
    IfFlagDisabled(OR_1, 1038492207)
    IfFlagDisabled(OR_1, 1038492208)
    IfFlagDisabled(AND_1, 1038492210)
    IfFlagDisabled(AND_1, 1038492212)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(AND_2, 1038492210)
    IfFlagEnabled(AND_2, 1038492212)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    WaitFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(1038490200)
    SetNetworkUpdateRate(1038490200, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DeleteObjectVFX(1038491200)
    DisableFlag(1038492209)
    IfFlagEnabled(OR_2, 1038492207)
    IfFlagEnabled(OR_2, 1038492208)
    IfConditionTrue(MAIN, input_condition=OR_2)
    WaitFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(1038490200)
    SetNetworkUpdateRate(1038490200, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DeleteObjectVFX(1038491200)
    DisableNetworkFlag(1038492207)
    DisableNetworkFlag(1038492208)


@RestartOnRest(1038492301)
def Event_1038492301():
    """Event 1038492301"""
    EnableNetworkSync()
    IfCharacterType(OR_2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfUnknownCharacterCondition_31(OR_2, character=PLAYER, unk_4_8=7, unk_8_12=1.0)
    EndIfConditionTrue(input_condition=OR_2)
    EndIfFlagEnabled(1038490201)
    IfFlagDisabled(OR_1, 1038492206)
    IfEntityBeyondDistance(OR_1, entity=1038490200, other_entity=PLAYER, radius=150.0)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(AND_1, 1038492206)
    IfEntityWithinDistance(AND_1, entity=1038490200, other_entity=PLAYER, radius=150.0)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Wait(1.0)
    IfFlagDisabled(MAIN, 1038492206)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableNetworkFlag(1038492207)
    SkipLinesIfPlayerInOwnWorld(1)
    DisableNetworkFlag(1038492208)
    Wait(1.0)
    IfFlagEnabled(MAIN, 1038492206)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(1038492207)
    SkipLinesIfPlayerInOwnWorld(1)
    EnableNetworkFlag(1038492208)
    IfFlagDisabled(MAIN, 1038492206)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1038492304)
def Event_1038492304():
    """Event 1038492304"""
    EnableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=1038490201)
    DisableCharacter(1038490201)
    DisableAnimations(1038490201)
    Kill(1038490201)
    DisableCharacter(1038490202)
    DisableAnimations(1038490202)
    Kill(1038490202)
    DisableCharacter(1038490203)
    DisableAnimations(1038490203)
    Kill(1038490203)
    DisableCharacter(1038490204)
    DisableAnimations(1038490204)
    Kill(1038490204)
    DisableCharacter(1038490205)
    DisableAnimations(1038490205)
    Kill(1038490205)
    DisableCharacter(1038490206)
    DisableAnimations(1038490206)
    Kill(1038490206)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(1038490201)
    IfCharacterDead(AND_1, 1038490201)
    IfCharacterDead(AND_1, 1038490202)
    IfCharacterDead(AND_1, 1038490203)
    IfCharacterDead(AND_1, 1038490204)
    IfCharacterDead(AND_1, 1038490205)
    IfCharacterDead(AND_1, 1038490206)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1038490201)


@RestartOnRest(1038492305)
def Event_1038492305():
    """Event 1038492305"""
    EndIfFlagEnabled(1038490201)
    EndIfPlayerNotInOwnWorld()
    EnableNetworkFlag(1038492206)
    DisableNetworkFlag(1038492207)
    DisableNetworkFlag(1038492208)
    DisableNetworkFlag(1038492209)
    DisableNetworkFlag(1038492210)
    DisableNetworkFlag(1038492211)


@RestartOnRest(1038492306)
def Event_1038492306():
    """Event 1038492306"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkSync()
    EndIfFlagEnabled(1038490201)
    Wait(7.0)
    DisableNetworkFlag(1038492206)
    DisableNetworkFlag(1038492208)
    Wait(5.0)
    EnableNetworkFlag(1038492206)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1038492310)
def Event_1038492310(_, character: uint):
    """Event 1038492310"""
    DisableNetworkSync()
    EndIfFlagEnabled(1038490201)
    SetBackreadStateAlternate(character, True)
    DisableGravity(character)


@RestartOnRest(1038492320)
def Event_1038492320():
    """Event 1038492320"""
    IfNewGameCycleEqual(AND_1, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_1)
    AddSpecialEffect(1038490200, 16630)
    End()
    IfNewGameCycleEqual(AND_2, completion_count=1)
    SkipLinesIfConditionFalse(2, AND_2)
    AddSpecialEffect(1038490200, 16631)
    End()
    IfNewGameCycleEqual(AND_3, completion_count=2)
    SkipLinesIfConditionFalse(2, AND_3)
    AddSpecialEffect(1038490200, 16632)
    End()
    IfNewGameCycleEqual(AND_4, completion_count=3)
    SkipLinesIfConditionFalse(2, AND_4)
    AddSpecialEffect(1038490200, 16633)
    End()
    IfNewGameCycleEqual(AND_5, completion_count=4)
    SkipLinesIfConditionFalse(2, AND_5)
    AddSpecialEffect(1038490200, 16634)
    End()
    IfNewGameCycleEqual(AND_6, completion_count=5)
    SkipLinesIfConditionFalse(2, AND_6)
    AddSpecialEffect(1038490200, 16635)
    End()
    IfNewGameCycleEqual(AND_7, completion_count=6)
    SkipLinesIfConditionFalse(2, AND_7)
    AddSpecialEffect(1038490200, 16636)
    End()
    IfNewGameCycleGreaterThanOrEqual(AND_8, completion_count=7)
    SkipLinesIfConditionFalse(2, AND_8)
    AddSpecialEffect(1038490200, 16637)
    End()


@RestartOnRest(1038492400)
def Event_1038492400():
    """Event 1038492400"""
    DisableNetworkSync()
    EndIfFlagEnabled(1038490201)
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1038492300)
    EnableFlag(1038492210)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=1038492300)
    DisableFlag(1038492210)
    Restart()


@RestartOnRest(1038492401)
def Event_1038492401():
    """Event 1038492401"""
    DisableNetworkSync()
    EndIfFlagEnabled(1038490201)
    EndIfPlayerInOwnWorld()
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1038492300)
    EnableFlag(1038492210)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=1038492300)
    DisableFlag(1038492210)
    Restart()


@NeverRestart(1038492580)
def Event_1038492580():
    """Event 1038492580"""
    RegisterLadder(start_climbing_flag=1038490580, stop_climbing_flag=1038490581, obj=1038491580)
    RegisterLadder(start_climbing_flag=1038490582, stop_climbing_flag=1038490583, obj=1038491582)
    RegisterLadder(start_climbing_flag=1038490584, stop_climbing_flag=1038490585, obj=1038491584)
