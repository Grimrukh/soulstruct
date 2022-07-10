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
    RegisterGrace(grace_flag=76302, obj=1038511950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76314, 76302, 1038511980, 77300, 1, 78300, 78301, 78302, 78303, 78304, 78305, 78306, 78307, 78308, 78309),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1038512800()
    Event_1038512810()
    Event_1038512849()
    Event_1038512500()
    RunCommonEvent(0, 90005300, args=(1038510500, 1038510500, 40302, 0.0, 0), arg_types="IIifi")
    Event_1038513700(0, character=1038510700, obj=1038511700)
    RunCommonEvent(0, 90005752, args=(1038511700, 200, 120, 3.0), arg_types="Iiif")
    Event_1038513701()
    Event_1038513702(0, attacked_entity=1038511700, other_entity=1038510700)
    Event_1038513703()
    RunCommonEvent(
        0,
        90005740,
        args=(
            1038512725,
            1038512726,
            1038512727,
            1038510700,
            703,
            1038511701,
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
        args=(1038512728, 1038512729, 1038512727, 1038510700, 90201, 0, -1, -1, 0.5),
        arg_types="IIIIiIiif",
    )
    Event_1038513705(0, character=1038510705)
    RunCommonEvent(0, 90005704, args=(1038510705, 4181, 4180, 1038519251, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1038510705, 4181, 4182, 1038519251, 1059481190, 4180, 4184, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(1038510705, 4183, 4180, 4184), arg_types="IIII")
    RunCommonEvent(0, 90005771, args=(1038510950, 1038512700), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038510700)
    DisableBackread(1038510705)
    DisableObject(1038511700)
    RunCommonEvent(0, 90005261, args=(1038510301, 1038512301, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038510302, 1038512301, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1038510400, 30002, 20002, 1038512400, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038510401, 30002, 20002, 1038512400, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038510402, 30002, 20002, 1038512400, 2.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1038510600, 1038512600, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(1038510602, 30000, 20000, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(1038510482, 1038512482, 0.0, 3005), arg_types="IIfi")
    Event_1038512405(0, 1038510405, 30003, 20003, 2.0, 0.0, 0, 0, 0, 0)
    Event_1038512405(1, 1038510406, 30003, 20003, 2.0, 0.0, 0, 0, 0, 0)
    Event_1038512405(2, 1038510451, 30003, 20003, 2.0, 0.0, 0, 0, 0, 0)
    Event_1038512405(3, 1038510480, 30003, 20003, 2.0, 0.0, 0, 0, 0, 0)
    Event_1038512405(4, 1038510489, 30003, 20003, 2.0, 0.0, 0, 0, 0, 0)
    Event_1038512405(5, 1038510490, 30002, 20002, 2.0, 0.0, 0, 0, 0, 0)


@RestartOnRest(1038512405)
def Event_1038512405(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1038512405"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfCharacterHasSpecialEffect(OR_10, 1038510404, 10530)
    IfCharacterHasSpecialEffect(OR_10, 1038510409, 10530)
    IfCharacterHasSpecialEffect(OR_10, 1038510481, 10531)
    IfConditionTrue(OR_2, input_condition=OR_10)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(1038512500)
def Event_1038512500():
    """Event 1038512500"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1038512500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(1038500500)
    EnableFlag(1038500500)
    PlaySoundEffect(1038512500, 990000020, sound_type=SoundType.m_Music)


@RestartOnRest(1038512800)
def Event_1038512800():
    """Event 1038512800"""
    EndIfFlagEnabled(1038510800)
    IfHealthValueLessThanOrEqual(MAIN, 1038510800, value=0)
    Wait(4.0)
    PlaySoundEffect(1038510800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1038510800)
    KillBossAndDisplayBanner(character=1038510800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(1038511560, obj_act_id=1110064)
    EnableFlag(1038510800)


@RestartOnRest(1038512810)
def Event_1038512810():
    """Event 1038512810"""
    GotoIfFlagDisabled(Label.L0, flag=1038510800)
    DisableCharacter(1038510800)
    DisableAnimations(1038510800)
    Kill(1038510800)
    EnableObjectActivation(1038511560, obj_act_id=1110064)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1038510800)
    ForceAnimation(1038510800, 30000, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 1038512805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1038512800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(1038510800, 20000, unknown2=1.0)
    EnableAI(1038510800)
    SetNetworkUpdateRate(1038510800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1038510800, name=904130540)
    DisableObjectActivation(1038511560, obj_act_id=1110064)


@RestartOnRest(1038512849)
def Event_1038512849():
    """Event 1038512849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1038510800, 1038511800, 1038512800, 1038512805, 1038515800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1038510800, 1038511800, 1038512800, 1038512805, 1038512806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1038510800, 1038511800, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1038510800, 931000, 1038512805, 1038512806, 0, 1038512802, 0, 0),
        arg_types="IiIIIIii",
    )
    RunCommonEvent(0, 9005812, args=(1038510800, 1038511801, 3, 0, 0), arg_types="IIiIi")


@RestartOnRest(1038513700)
def Event_1038513700(_, character: uint, obj: uint):
    """Event 1038513700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3420)
    DisableFlag(1038519203)
    SkipLinesIfFlagDisabled(1, 1038519207)
    EnableNetworkFlag(1038512720)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagEnabled(OR_1, 1038519207)
    IfFlagEnabled(OR_1, 1038512720)
    IfFlagEnabled(AND_1, 3426)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 1038519207)
    IfFlagEnabled(OR_3, 1038512720)
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
    IfFlagEnabled(OR_4, 1038519207)
    IfFlagEnabled(OR_4, 1038512720)
    IfFlagEnabled(AND_4, 3426)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfConditionFalse(MAIN, input_condition=AND_4)
    Restart()


@RestartOnRest(1038513701)
def Event_1038513701():
    """Event 1038513701"""
    EndIfPlayerNotInOwnWorld()
    WaitFramesAfterCutscene(frames=1)
    EndIfFlagDisabled(3426)
    IfFlagEnabled(OR_1, 1038519207)
    IfFlagEnabled(OR_1, 1038509205)
    EndIfConditionTrue(input_condition=OR_1)
    IfEntityWithinDistance(OR_5, entity=PLAYER, other_entity=1038500952, radius=5.0)
    EndIfConditionTrue(input_condition=OR_5)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1038512700)
    IfFlagEnabled(OR_2, 16000860)
    IfFlagEnabled(OR_2, 76301)
    IfFlagEnabled(OR_2, 76302)
    IfConditionTrue(MAIN, input_condition=OR_2)
    IfFlagEnabled(OR_3, 1038519207)
    IfFlagEnabled(OR_3, 1038509205)
    EndIfConditionTrue(input_condition=OR_3)
    EnableFlag(1038519207)
    End()


@RestartOnRest(1038513702)
def Event_1038513702(_, attacked_entity: uint, other_entity: uint):
    """Event 1038513702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3426)
    EndIfFlagEnabled(1038509205)
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


@RestartOnRest(1038513703)
def Event_1038513703():
    """Event 1038513703"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3426)
    EndIfFlagEnabled(1038509205)
    IfFlagEnabled(AND_1, 1038519205)
    IfFlagEnabled(AND_1, 1038519207)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(16008540)
    BanishPhantoms(unknown=0)
    WarpToMap(game_map=VOLCANO_MANOR, player_start=16002701)
    End()


@RestartOnRest(1038513705)
def Event_1038513705(_, character: uint):
    """Event 1038513705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    DisableNetworkFlag(1050389265)
    DisableNetworkFlag(1038519255)
    DisableNetworkFlag(4197)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 4187)
    IfFlagEnabled(AND_1, 1050389266)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    SkipLinesIfPlayerInOwnWorld(3)
    IfFlagEnabled(AND_3, 4187)
    IfFlagEnabled(AND_3, 4197)
    GotoIfConditionTrue(Label.L6, input_condition=AND_3)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_2, 4187)
    IfFlagEnabled(AND_2, 1050389266)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableNetworkFlag(1050389265)
    EnableNetworkFlag(1038519255)
    EnableNetworkFlag(4197)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

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
    IfFlagEnabled(AND_15, 4187)
    IfFlagEnabled(AND_15, 1050389266)
    AwaitConditionFalse(AND_15)
    Restart()
