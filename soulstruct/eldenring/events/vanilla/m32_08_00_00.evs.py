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
    RegisterGrace(grace_flag=32080000, obj=32081950, unknown=5.0)
    Event_32082800()
    Event_32082810()
    Event_32082811()
    Event_32082849()
    Event_32082580()
    RunCommonEvent(0, 90005520, args=(32080588, 32081586, 32080586, 32080587), arg_types="IIII")
    Event_32082498()
    RunCommonEvent(
        0,
        90005646,
        args=(32080800, 32082840, 32082841, 32081840, 32082840, 32, 8, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_32082650()
    RunCommonEvent(0, 900005610, args=(32081680, 100, 800, 0), arg_types="IiiI")
    Event_32082200(0, 32080200, 30005, 20005, 0.0, 0, 0, 0, 0, 32081600, 32081601, 32081602, 0)
    Event_32082200(1, 32080201, 30001, 20001, 0.0, 0, 0, 0, 0, 32081603, 0, 0, 0)
    Event_32082200(2, 32080202, 30001, 20001, 0.0, 0, 0, 0, 0, 32081604, 32081605, 0, 0)
    Event_32082200(3, 32080203, 30004, 20004, 0.0, 0, 0, 0, 0, 32081615, 0, 0, 0)
    Event_32082200(4, 32080204, 30001, 20001, 0.0, 0, 0, 0, 0, 32081616, 32081617, 0, 0)
    Event_32082200(5, 32080205, 30005, 20005, 0.0, 0, 0, 0, 0, 32081618, 32081619, 0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32082820()
    RunCommonEvent(0, 90005250, args=(32080211, 32082211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080216, 32082302, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080217, 32082217, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080218, 32082217, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080250, 32082250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(32080300, 30009, 20029, 32082300, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32080301, 30009, 20029, 32082301, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32080302, 30009, 20029, 32082302, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32080303, 30009, 20029, 32082303, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(32080305, 32082305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080306, 32082306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080307, 32082306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32080308, 32082308, 0.0, 3008), arg_types="IIfi")


@RestartOnRest(32082580)
def Event_32082580():
    """Event 32082580"""
    RegisterLadder(start_climbing_flag=32080580, stop_climbing_flag=32080581, obj=32081580)
    RegisterLadder(start_climbing_flag=32080582, stop_climbing_flag=32080583, obj=32081582)
    RegisterLadder(start_climbing_flag=32080584, stop_climbing_flag=32080585, obj=32081584)


@RestartOnRest(32082498)
def Event_32082498():
    """Event 32082498"""
    GotoIfFlagEnabled(Label.L0, flag=32080588)
    EnableNavmeshType(navmesh_id=32082498, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(MAIN, 32080588)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=32082498, navmesh_type=NavmeshType.Solid)
    End()


@RestartOnRest(32082200)
def Event_32082200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
):
    """Event 32082200"""
    EndIfThisEventSlotFlagEnabled()
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
    IfObjectDestroyed(OR_10, obj)
    IfObjectDestroyed(OR_10, obj_1)
    IfObjectDestroyed(OR_10, obj_2)
    IfObjectDestroyed(OR_10, obj_3)
    IfConditionTrue(AND_1, input_condition=OR_10)
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
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
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


@RestartOnRest(32082650)
def Event_32082650():
    """Event 32082650"""
    IfFlagEnabled(MAIN, 32080650)
    ForceAnimation(PLAYER, 60131, unknown2=1.0)
    EnableFlag(9080)
    DisableFlag(32080650)


@RestartOnRest(32082800)
def Event_32082800():
    """Event 32082800"""
    EndIfFlagEnabled(32080800)
    IfHealthValueLessThanOrEqual(MAIN, 32080800, value=0)
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 32080800)
    KillBossAndDisplayBanner(character=32080800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(32080800)
    EnableFlag(9267)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61267)


@RestartOnRest(32082810)
def Event_32082810():
    """Event 32082810"""
    GotoIfFlagDisabled(Label.L0, flag=32080800)
    DisableCharacter(32080800)
    DisableAnimations(32080800)
    Kill(32080800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32080800)
    EnableInvincibility(32080800)
    GotoIfFlagEnabled(Label.L1, flag=32080801)
    ForceAnimation(32080800, 30008, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 32082805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32082800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableNetworkFlag(32080801)
    ForceAnimation(32080800, 20008, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(32080800, 30008, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 32082805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32082800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(32080800, 20008, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32080800)
    DisableInvincibility(32080800)
    SetNetworkUpdateRate(32080800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32080800, name=904680320)


@RestartOnRest(32082811)
def Event_32082811():
    """Event 32082811"""
    EndIfFlagEnabled(32080800)
    IfCharacterHasSpecialEffect(AND_1, 32080800, 16495)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(32082802)


@RestartOnRest(32082820)
def Event_32082820():
    """Event 32082820"""
    EndIfFlagEnabled(32080800)
    EndIfFlagEnabled(32080801)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(32088590)
    DisableFlag(32088590)


@RestartOnRest(32082849)
def Event_32082849():
    """Event 32082849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32080800, 32081800, 32082800, 32082805, 32085800, 10000, 32080801, 32082801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32080800, 32081800, 32082800, 32082805, 32082806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32080800, 32081800, 7, 32080801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32080800, 920800, 32082805, 32082806, 0, 32082802, 0, 0), arg_types="IiIIIIii")
