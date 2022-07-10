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
    RegisterGrace(grace_flag=1038500000, obj=1038501950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76209, 76209, 1038501980, 77210, 2, 78210, 78211, 78212, 78213, 78214, 78215, 78216, 78217, 78218, 78219),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1038500001, obj=1038501951, unknown=5.0)
    RegisterGrace(grace_flag=76301, obj=1038501952, unknown=5.0)
    RunCommonEvent(0, 90005300, args=(1038500210, 1038500210, 40256, 0.0, 0), arg_types="IIifi")
    Event_1038502580()
    Event_1038502500()
    Event_1038503700(0, character=1038500700, obj=1038501700)
    RunCommonEvent(0, 90005752, args=(1038501700, 200, 120, 3.0), arg_types="Iiif")
    Event_1038503701()
    Event_1038503702(0, attacked_entity=1038501700, other_entity=1038500700)
    Event_1038503703()
    RunCommonEvent(
        0,
        90005740,
        args=(
            1038502705,
            1038502706,
            1038502707,
            1038500700,
            703,
            1038501701,
            703,
            0.20000000298023224,
            90203,
            -1,
            -1,
            1.2000000476837158,
        ),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(
        0,
        90005741,
        args=(1038502708, 1038502709, 1038502707, 1038500700, 90201, 0, -1, -1, 0.5),
        arg_types="IIIIiIiif",
    )
    RunCommonEvent(0, 90005771, args=(1038500950, 1038502710), arg_types="II")
    RunCommonEvent(0, 90005771, args=(1038500952, 1038502711), arg_types="II")
    RunCommonEvent(0, 90005706, args=(1038500710, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038500700)
    DisableObject(1038501700)
    DisableBackread(1038500710)
    Event_1038502400(0, 1038500402, 1038502400, 0.0, 0, 1038500400)
    Event_1038502400(1, 1038500400, 1038502400, 0.0, 0, 1038500402)


@RestartOnRest(1038502400)
def Event_1038502400(_, character: uint, region: uint, seconds: float, animation_id: int, attacked_entity: uint):
    """Event 1038502400"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfFlagDisabled(OR_15, 1046367500)
    IfFlagDisabled(OR_15, 1051397900)
    IfConditionTrue(AND_1, input_condition=OR_15)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1038502500)
def Event_1038502500():
    """Event 1038502500"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1038500500)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1038502550)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1038500500)


@RestartOnRest(1038502580)
def Event_1038502580():
    """Event 1038502580"""
    RegisterLadder(start_climbing_flag=1038500580, stop_climbing_flag=1038500581, obj=1038501580)
    RegisterLadder(start_climbing_flag=1038500582, stop_climbing_flag=1038500583, obj=1038501582)
    RegisterLadder(start_climbing_flag=1038500584, stop_climbing_flag=1038500585, obj=1038501584)


@RestartOnRest(1038503700)
def Event_1038503700(_, character: uint, obj: uint):
    """Event 1038503700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3420)
    DisableFlag(1038519203)
    SkipLinesIfFlagDisabled(1, 1038509205)
    EnableNetworkFlag(1038502700)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagEnabled(OR_1, 1038509205)
    IfFlagEnabled(OR_1, 1038502700)
    IfFlagEnabled(AND_1, 3426)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 1038509205)
    IfFlagEnabled(OR_3, 1038502700)
    IfFlagEnabled(AND_3, 3426)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=character)
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
    IfFlagEnabled(OR_4, 1038509205)
    IfFlagEnabled(OR_4, 1038502700)
    IfFlagEnabled(AND_4, 3426)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfConditionFalse(MAIN, input_condition=AND_4)
    Restart()


@RestartOnRest(1038503701)
def Event_1038503701():
    """Event 1038503701"""
    EndIfPlayerNotInOwnWorld()
    WaitFramesAfterCutscene(frames=1)
    EndIfFlagDisabled(3426)
    IfFlagEnabled(OR_1, 1038519207)
    IfFlagEnabled(OR_1, 1038509205)
    EndIfConditionTrue(input_condition=OR_1)
    IfEntityWithinDistance(OR_5, entity=PLAYER, other_entity=1038510950, radius=5.0)
    EndIfConditionTrue(input_condition=OR_5)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1038502500)
    IfFlagEnabled(OR_2, 16000860)
    IfFlagEnabled(OR_2, 76301)
    IfFlagEnabled(OR_2, 76302)
    IfConditionTrue(MAIN, input_condition=OR_2)
    IfFlagEnabled(OR_3, 1038519207)
    IfFlagEnabled(OR_3, 1038509205)
    EndIfConditionTrue(input_condition=OR_3)
    EnableFlag(1038509205)
    End()


@RestartOnRest(1038503702)
def Event_1038503702(_, attacked_entity: uint, other_entity: uint):
    """Event 1038503702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3426)
    EndIfFlagEnabled(1038519207)
    EndIfFlagEnabled(1038512704)
    GotoIfFlagDisabled(Label.L1, flag=1038512701)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(AND_1, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAttackedWithDamageType(AND_2, attacked_entity=attacked_entity, attacker=20000)
    IfTimeElapsed(OR_2, seconds=4.0)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionFalse(Label.L7, input_condition=AND_2)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L5, flag=1038512701)
    GotoIfFlagDisabled(Label.L6, flag=1038512703)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    IfEntityWithinDistance(AND_5, entity=20000, other_entity=other_entity, radius=10.0)
    SkipLinesIfConditionFalse(2, AND_5)
    EnableFlag(1038512700)
    IfFlagEnabled(MAIN, 1038512706)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    IfEntityWithinDistance(AND_6, entity=20000, other_entity=other_entity, radius=10.0)
    SkipLinesIfConditionFalse(2, AND_6)
    EnableFlag(1038512702)
    IfFlagEnabled(MAIN, 1038512707)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(1038512704)
    End()


@RestartOnRest(1038503703)
def Event_1038503703():
    """Event 1038503703"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3426)
    EndIfFlagEnabled(1038519207)
    IfFlagEnabled(AND_1, 1038519205)
    IfFlagEnabled(AND_1, 1038509205)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(16008540)
    BanishPhantoms(unknown=0)
    WarpToMap(game_map=VOLCANO_MANOR, player_start=16002701)
    End()
