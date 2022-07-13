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
    RunCommonEvent(0, 90005300, args=(1048550200, 1048550200, 40522, 0.0, 0), arg_types="IIifi")


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005421, args=(1248550300, 1248551301, 1248558301), arg_types="III")
    RunCommonEvent(0, 90005422, args=(1248558301, 1248551300, 1248553301), arg_types="III")
    RunCommonEvent(0, 90005424, args=(1248551300, 1248550302, 1248550303, 1248550300, 1248551301), arg_types="IIIII")
    RunCommonEvent(0, 90005423, args=(1248550302,))
    RunCommonEvent(0, 90005423, args=(1248550303,))
    RunCommonEvent(0, 90005476, args=(1248550800, 1248550810), arg_types="II")
    RunCommonEvent(0, 90005476, args=(1248550801, 1248550811), arg_types="II")
    Event_1248552820(0, 1248550800, 0.0)
    Event_1248552820(1, 1248550801, 0.0)
    Event_1248552830(0, character=1248550800, character_1=1248550810)
    Event_1248552830(1, character=1248550801, character_1=1248550811)
    Event_1248552840(0, character=1248550800, character_1=1248550810, destination=1248552800)
    Event_1248552840(1, character=1248550801, character_1=1248550811, destination=1248552801)
    RunCommonEvent(0, 90005871, args=(1248550800, 903150608, 10, 1248550810), arg_types="IiII")
    RunCommonEvent(0, 90005871, args=(1248550801, 903150609, 10, 1248550811), arg_types="IiII")
    RunCommonEvent(
        0,
        1248552800,
        args=(1248550800, 0, 1248550800, 0, 1048550700, 1248550801, 1048550710),
        arg_types="IIIIiIi",
    )
    Event_1248552321(0, character=1248550800, character_1=1248550801, entity_id__unk_4_8=10, flag=1248552815)
    Event_1248552320(0, 1248550800, 1248550801)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(
        0,
        90005420,
        args=(1248550300, 1248551300, 1248551301, 1248550301, 1248550302, 1248550303, 0.0),
        arg_types="IIIIIIf",
    )


@RestartOnRest(1248552320)
def Event_1248552320(_, character: uint, character_1: uint):
    """Event 1248552320"""
    EndIfFlagEnabled(1248550800)
    IfCharacterDead(OR_1, character)
    IfCharacterDead(OR_1, character_1)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfHealthRatioLessThanOrEqual(AND_1, character, value=0.5)
    IfHealthRatioLessThanOrEqual(AND_1, character_1, value=0.5)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(1248552815)


@NeverRestart(1248552321)
def Event_1248552321(_, character: uint, character_1: uint, entity_id__unk_4_8: uint, flag: uint):
    """Event 1248552321"""
    DisableNetworkSync()
    IfFlagEnabled(AND_1, flag)
    IfUnknownCondition_33(AND_1, unk_4_8=entity_id__unk_4_8, unk_8_9=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_12(entity_id=entity_id__unk_4_8, unk_4_8=1)
    IfCharacterDead(AND_2, character)
    IfCharacterDead(AND_2, character_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfUnknownCondition_33(OR_2, unk_4_8=entity_id__unk_4_8, unk_8_9=False)
    IfConditionTrue(MAIN, input_condition=OR_2)
    UnknownSound_2010_12(entity_id=entity_id__unk_4_8, unk_4_8=0)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(1248552800)
def Event_1248552800(
    _,
    flag: uint,
    left: uint,
    character: uint,
    left_1: uint,
    item_lot__item_lot_param_id: int,
    character_1: uint,
    item_lot_param_id: int,
):
    """Event 1248552800"""
    SkipLinesIfValueEqual(1, left=item_lot__item_lot_param_id, right=0)
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableAnimations(character)
    DisableAnimations(character_1)
    Kill(character)
    Kill(character_1)
    DisableCharacter(1248550810)
    DisableAnimations(1248550810)
    Kill(1248550810)
    DisableCharacter(1248550811)
    DisableAnimations(1248550811)
    Kill(1248550811)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(1.0)
    AwardItemLot(item_lot_param_id, host_only=True)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueLessThanOrEqual(AND_15, character, value=0)
    IfHealthValueLessThanOrEqual(AND_15, character_1, value=0)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_14, character)
    IfCharacterDead(AND_14, character_1)
    IfConditionTrue(MAIN, input_condition=AND_14)
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DutyFulfilled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.Unknown)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaWin)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(5.0)
    AwardItemLot(item_lot_param_id, host_only=True)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()


@RestartOnRest(1248552820)
def Event_1248552820(_, character: uint, seconds: float):
    """Event 1248552820"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfTimeOfDay(AND_3, earliest=(19, 59, 59), latest=(5, 59, 59))
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfTimeOfDay(AND_4, earliest=(5, 59, 59), latest=(19, 59, 59))
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()
    Wait(seconds)


@RestartOnRest(1248552830)
def Event_1248552830(_, character: uint, character_1: uint):
    """Event 1248552830"""
    IfCharacterAlive(AND_15, character)
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    IfCharacterBackreadEnabled(AND_14, character)
    AwaitConditionTrue(AND_14)
    IfCharacterHasSpecialEffect(AND_1, character, 11830)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    IfCharacterHasSpecialEffect(AND_2, character, 11830)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableAnimations(character)
    DisableAnimations(character_1)
    EnableInvincibility(character)
    EnableInvincibility(character_1)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAnimations(character)
    DisableAnimations(character_1)
    EnableInvincibility(character)
    EnableInvincibility(character_1)
    IfCharacterHasSpecialEffect(AND_2, character, 11831)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAnimations(character)
    EnableAnimations(character_1)
    DisableInvincibility(character)
    DisableInvincibility(character_1)
    Wait(1.0)
    Restart()


@RestartOnRest(1248552840)
def Event_1248552840(_, character: uint, character_1: uint, destination: uint):
    """Event 1248552840"""
    IfCharacterAlive(AND_15, character)
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    IfCharacterBackreadEnabled(AND_14, character)
    AwaitConditionTrue(AND_14)
    DisableAI(character)
    DisableAI(character_1)
    Wait(1.5)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    EnableAI(character)
    EnableAI(character_1)
