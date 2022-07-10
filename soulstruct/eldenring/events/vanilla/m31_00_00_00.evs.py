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
    RegisterGrace(grace_flag=31000000, obj=31001950, unknown=5.0)
    Event_31002800()
    Event_31002810()
    Event_31002849()
    Event_31002811()
    Event_31002813()
    Event_31002814()
    Event_31002850()
    Event_31002860()
    Event_31002899()
    Event_31002861()
    Event_31002863()
    Event_31002845()
    Event_31002875()
    Event_31002876(
        0,
        flag=31000845,
        left_flag=31002840,
        cancel_flag__right_flag=31002841,
        obj=31001840,
        player_start=31002840,
        area_id=31,
        block_id=0,
        cc_id=0,
        dd_id=0
    )
    Event_31002500(0, attacked_entity=31001500, region=31002500)
    Event_31002500(1, attacked_entity=31001501, region=31002501)
    Event_31002500(2, attacked_entity=31001502, region=31002502)
    Event_31003700(0, character=31000701)
    Event_31003710(0, character=31000703)
    Event_31003701(0, character=31000701, flag=31002709, flag_1=31009201, character_1=31000800)
    Event_31003711(0, character=31000703, flag=31002709, flag_1=31009201, character_1=31000850)
    Event_31003702(0, character=31000800)
    Event_31003703()
    Event_31003704(0, 31000800, 10.0)
    Event_31003705(0, character=31000800)
    Event_31003707()
    Event_31003713(0, character=31000850)
    Event_31003714(0, 31000850, 10.0)
    Event_31003715(0, attacked_entity=31000850)
    RunCommonEvent(0, 90005704, args=(31000800, 31009219, 3680, 31009201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(31000800, 3681, 3682, 31009201, 31009219, 3680, 3684, -1), arg_types="IIIIIIIi")
    Event_31003706(0, character=31000800, flag=3683, first_flag=3680, last_flag=3684)
    RunCommonEvent(0, 90005704, args=(31000701, 31009219, 3680, 31009201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(31000701, 3681, 3682, 31009201, 31009219, 3680, 3684, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(31000701, 3683, 3680, 3684), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(31000703, 3681, 3680, 31009201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(31000703, 3681, 3682, 31009201, 3681, 3680, 3684, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(31000703, 3683, 3680, 3684), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(31000850, 31009269, 3680, 31009201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(31000850, 3681, 3682, 31009201, 31009269, 3680, 3684, -1), arg_types="IIIIIIIi")
    Event_31003716(0, 31000850, 3683, 3680, 3684)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(31000700)
    DisableBackread(31000701)
    DisableBackread(31000702)
    DisableBackread(31000703)
    Event_31002230(0, 31000200, 31002200, 2.0, 0.0, 0)
    Event_31002200(0, 31000201, 30010, 20010, 31002202, 2.0, 0.0, 0, 0, 0, 0, 31002500, 31002501, 31002502)
    Event_31002210(0, 31000205, 31002205, 3.0, 0.0, 0, 31002500, 31002501, 31002502)
    Event_31002210(1, 31000206, 31002205, 3.0, 0.0, 0, 31002500, 31002501, 31002502)
    Event_31002200(
        1,
        31000209,
        30010,
        20010,
        31002209,
        2.0,
        0.800000011920929,
        0,
        0,
        0,
        0,
        31002500,
        31002501,
        31002502,
    )
    Event_31002200(
        2,
        31000210,
        30010,
        20010,
        31002209,
        2.0,
        0.6000000238418579,
        0,
        0,
        0,
        0,
        31002500,
        31002501,
        31002502,
    )
    Event_31002200(
        3,
        31000211,
        30010,
        20010,
        31002209,
        2.0,
        0.30000001192092896,
        0,
        0,
        0,
        0,
        31002500,
        31002501,
        31002502,
    )
    Event_31003712()


@RestartOnRest(31002500)
def Event_31002500(_, attacked_entity: uint, region: uint):
    """Event 31002500"""
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1, unknown2=1.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(31002200)
def Event_31002200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
):
    """Event 31002200"""
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_2)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_3)
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


@RestartOnRest(31002210)
def Event_31002210(
    _,
    character: uint,
    region: uint,
    radius: float,
    seconds: float,
    animation_id: int,
    region_1: uint,
    region_2: uint,
    region_3: uint,
):
    """Event 31002210"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_2)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_3)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31002230)
def Event_31002230(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31002230"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
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


@RestartOnRest(31002800)
def Event_31002800():
    """Event 31002800"""
    IfFlagEnabled(OR_1, 31000800)
    IfFlagEnabled(OR_1, 3683)
    IfFlagEnabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfHealthValueLessThanOrEqual(MAIN, 31000800, value=0)
    EndIfFlagEnabled(31000800)
    Wait(4.0)
    PlaySoundEffect(31000800, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 31000800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 31000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(31000800)
    KillBossAndDisplayBanner(character=31000800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31000800)
    EnableFlag(9232)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61232)
    AwardItemLot(101830, host_only=False)


@RestartOnRest(31002810)
def Event_31002810():
    """Event 31002810"""
    IfFlagEnabled(OR_1, 31000800)
    IfFlagEnabled(OR_1, 3683)
    IfFlagEnabled(OR_1, 3691)
    GotoIfConditionFalse(Label.L0, input_condition=OR_1)
    DisableCharacter(31000800)
    DisableAnimations(31000800)
    DisableBackread(31000800)
    Kill(31000800)
    SkipLinesIfFlagEnabled(1, 31000800)
    EnableFlag(31000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31000800)
    AddSpecialEffect(31000800, 9643)
    GotoIfFlagDisabled(Label.L1, flag=31008521)
    EnableNetworkFlag(31008820)
    Move(31000800, destination=31002820, destination_type=CoordEntityType.Region, copy_draw_parent=31000800)
    ChangePatrolBehavior(31000800, patrol_information_id=0)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 31002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31002800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfFlagEnabled(3, 31008820)
    EnableNetworkFlag(31008821)
    DisableCharacter(31000800)
    End()
    SetTeamType(31000800, TeamType.Enemy)
    EnableAI(31000800)
    SetNetworkUpdateRate(31000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31000800, name=130900)
    EnableNetworkFlag(31000811)


@RestartOnRest(31002811)
def Event_31002811():
    """Event 31002811"""
    IfFlagEnabled(OR_1, 31000800)
    IfFlagEnabled(OR_1, 3683)
    IfFlagEnabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagEnabled(MAIN, 31009810)
    SetTeamType(31000800, TeamType.FriendlyNPC)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 31000800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(31000800)
    PlaySoundEffect(31000800, 888880000, sound_type=SoundType.s_SFX)
    KillBossAndDisplayBanner(character=31000800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31000800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61232)
    EnableFlag(9232)
    AwardItemLot(101830, host_only=False)
    ChangePatrolBehavior(31000800, patrol_information_id=31003820)
    ReplanAI(31000800)


@RestartOnRest(31002813)
def Event_31002813():
    """Event 31002813"""
    IfFlagEnabled(OR_1, 31000800)
    IfFlagEnabled(OR_1, 3683)
    IfFlagEnabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagState(MAIN, FlagSetting.Change, FlagType.Absolute, 31008521)
    EndIfFlagDisabled(31008821)
    EnableCharacter(31000800)
    Wait(4.0)
    SetTeamType(31000800, TeamType.Enemy)
    EnableAI(31000800)
    SetNetworkUpdateRate(31000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(5.0)
    EnableBossHealthBar(31000800, name=130900)
    EnableNetworkFlag(31000811)
    SetNest(31000800, region=31002820)


@RestartOnRest(31002814)
def Event_31002814():
    """Event 31002814"""
    IfFlagEnabled(OR_1, 31000800)
    IfFlagEnabled(OR_1, 3683)
    IfFlagEnabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagEnabled(MAIN, 31002713)
    EnableAI(31000800)
    SetTeamType(31000800, TeamType.Enemy)


@RestartOnRest(31002849)
def Event_31002849():
    """Event 31002849"""
    Event_31002830(
        0,
        flag=31000800,
        entity=31001800,
        region=31002800,
        flag_1=31002805,
        character=31005800,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    Event_31002831(
        0,
        flag=31000800,
        entity=31001800,
        region=31002800,
        flag_1=31002805,
        flag_2=31002806,
        action_button_id=10000
    )
    Event_31002832(0, flag=31000800, obj=31001800, model_point=4, right=0)
    Event_31002833(0, 31000800, 931000, 31002805, 31002806, 31000811, 0, 0, 0)


@RestartOnRest(31002831)
def Event_31002831(_, flag: uint, entity: uint, region: uint, flag_1: uint, flag_2: uint, action_button_id: int):
    """Event 31002831"""
    EndIfFlagEnabled(3691)
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterWhitePhantom(AND_1, PLAYER)
    IfActionButtonParamActivated(AND_1, action_button_id=action_button_id, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_11(unk_0_4=5.0)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    IfCharacterWhitePhantom(AND_2, PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfTimeElapsed(OR_1, seconds=3.0)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(31002830)
def Event_31002830(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 31002830"""
    EndIfFlagEnabled(3691)
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    SkipLinesIfUnsignedEqual(1, left=region_1, right=0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region_1)
    IfFlagEnabled(OR_1, left)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFlagEnabled(flag)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfPlayerInOwnWorld(AND_3)
    IfFlagDisabled(AND_3, flag)
    IfActionButtonParamActivated(AND_3, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RestartIfFlagEnabled(flag)
    UnknownSound_2010_11(unk_0_4=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(flag)
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    EndIfPlayerNotInOwnWorld()
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, flag)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31002832)
def Event_31002832(_, flag: uint, obj: uint, model_point: int, right: uint):
    """Event 31002832"""
    EndIfFlagEnabled(3691)
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfCharacterType(OR_2, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagDisabled(AND_2, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_3, right)
    IfFlagDisabled(AND_3, flag)
    IfFailedToCreateSession(OR_4)
    IfMultiplayerState(OR_4, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, flag)
    IfCharacterWhitePhantom(AND_7, PLAYER)
    IfConditionFalse(AND_4, input_condition=AND_7)
    IfFailedToCreateSession(OR_5)
    IfMultiplayerState(OR_5, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_5, input_condition=OR_5)
    IfFlagEnabled(AND_5, flag)
    IfCharacterWhitePhantom(AND_5, PLAYER)
    IfEntityBeyondDistance(AND_5, entity=PLAYER, other_entity=obj, radius=1.0)
    IfConditionTrue(OR_8, input_condition=AND_1)
    IfConditionTrue(OR_8, input_condition=AND_2)
    IfConditionTrue(OR_8, input_condition=AND_3)
    IfConditionTrue(OR_8, input_condition=AND_4)
    IfConditionTrue(OR_8, input_condition=AND_5)
    IfConditionTrue(MAIN, input_condition=OR_8)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_11, input_condition=OR_11)
    IfFlagDisabled(AND_11, flag)
    IfCharacterWhitePhantom(OR_12, PLAYER)
    IfCharacterType(OR_12, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_12, input_condition=OR_12)
    IfFlagDisabled(AND_12, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_13, right)
    IfFlagDisabled(AND_13, flag)
    IfFailedToCreateSession(OR_14)
    IfMultiplayerState(OR_14, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_14, input_condition=OR_14)
    IfFlagEnabled(AND_14, flag)
    IfCharacterWhitePhantom(OR_7, PLAYER)
    IfConditionFalse(AND_14, input_condition=OR_7)
    IfFailedToCreateSession(OR_15)
    IfMultiplayerState(OR_15, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag)
    IfCharacterWhitePhantom(AND_15, PLAYER)
    IfEntityBeyondDistance(AND_15, entity=PLAYER, other_entity=obj, radius=1.0)
    IfConditionFalse(AND_9, input_condition=AND_11)
    IfConditionFalse(AND_9, input_condition=AND_12)
    IfConditionFalse(AND_9, input_condition=AND_13)
    IfConditionFalse(AND_9, input_condition=AND_14)
    IfConditionFalse(AND_9, input_condition=AND_15)
    IfConditionTrue(MAIN, input_condition=AND_9)
    Restart()


@RestartOnRest(31002833)
def Event_31002833(
    _,
    flag: uint,
    unk_0_4: int,
    flag_1: uint,
    flag_2: uint,
    right: uint,
    flag_3: uint,
    left: int,
    left_1: int,
):
    """Event 31002833"""
    EndIfFlagEnabled(3691)
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_1)
    IfFlagEnabled(AND_1, flag_1)
    SkipLinesIfPlayerInOwnWorld(1)
    IfFlagEnabled(AND_1, flag_2)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(1, flag_3)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=0)
    IfFlagEnabled(OR_2, flag_3)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=1)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(2, left=left_1, right=1)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-1)
    End()
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-2)


@RestartOnRest(31002899)
def Event_31002899():
    """Event 31002899"""
    Event_31002870(
        0,
        flag=31000850,
        entity=31001800,
        region=31002800,
        flag_1=31002855,
        character=31005850,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    Event_31002872(0, flag=31000850, obj=31001800, model_point=4, right=0)
    Event_31002873(0, 31000850, 931000, 31002855, 31002856, 31000861, 0, 0, 0)


@RestartOnRest(31002850)
def Event_31002850():
    """Event 31002850"""
    IfFlagEnabled(OR_1, 31000850)
    IfFlagEnabled(OR_1, 3683)
    IfFlagDisabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfHealthValueLessThanOrEqual(MAIN, 31000850, value=0)
    EndIfFlagEnabled(31000850)
    Wait(4.0)
    PlaySoundEffect(31000850, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 31000850)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 31000850)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(31000850)
    KillBossAndDisplayBanner(character=31000850, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31000850)
    EnableFlag(9232)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61232)


@RestartOnRest(31002860)
def Event_31002860():
    """Event 31002860"""
    IfFlagEnabled(OR_1, 31000850)
    IfFlagEnabled(OR_1, 3683)
    IfFlagDisabled(OR_1, 3691)
    GotoIfConditionFalse(Label.L0, input_condition=OR_1)
    DisableCharacter(31000850)
    DisableAnimations(31000850)
    DisableBackread(31000850)
    Kill(31000850)
    SkipLinesIfFlagDisabled(1, 3683)
    EnableFlag(31000850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31000850)
    AddSpecialEffect(31000850, 9643)
    GotoIfFlagDisabled(Label.L1, flag=31008523)
    EnableNetworkFlag(31008870)
    Move(31000850, destination=31002820, destination_type=CoordEntityType.Region, copy_draw_parent=31000850)
    ChangePatrolBehavior(31000850, patrol_information_id=0)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 31002855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31002800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfFlagEnabled(3, 31008870)
    EnableNetworkFlag(31008871)
    DisableCharacter(31000850)
    End()
    SetTeamType(31000850, TeamType.Enemy)
    EnableAI(31000850)
    SetNetworkUpdateRate(31000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31000850, name=130900)
    EnableNetworkFlag(31000861)


@RestartOnRest(31002861)
def Event_31002861():
    """Event 31002861"""
    IfFlagEnabled(OR_1, 31000850)
    IfFlagEnabled(OR_1, 3683)
    IfFlagDisabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagEnabled(MAIN, 31009889)
    SetTeamType(31000850, TeamType.FriendlyNPC)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 31000850)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableNetworkFlag(31000850)
    PlaySoundEffect(31000850, 888880000, sound_type=SoundType.s_SFX)
    KillBossAndDisplayBanner(character=31000850, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31000850)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61232)
    EnableFlag(9232)
    ChangePatrolBehavior(31000850, patrol_information_id=31003820)
    ReplanAI(31000850)


@RestartOnRest(31002863)
def Event_31002863():
    """Event 31002863"""
    IfFlagEnabled(OR_1, 31000850)
    IfFlagEnabled(OR_1, 3683)
    IfFlagDisabled(OR_1, 3691)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagState(MAIN, FlagSetting.Change, FlagType.Absolute, 31008523)
    EndIfFlagDisabled(31008871)
    EnableCharacter(31000850)
    Wait(4.0)
    SetTeamType(31000850, TeamType.Enemy)
    EnableAI(31000850)
    SetNetworkUpdateRate(31000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(5.0)
    EnableBossHealthBar(31000850, name=130900)
    EnableNetworkFlag(31000861)
    SetNest(31000850, region=31002820)


@RestartOnRest(31002870)
def Event_31002870(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 31002870"""
    EndIfFlagDisabled(3691)
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    SkipLinesIfUnsignedEqual(1, left=region_1, right=0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region_1)
    IfFlagEnabled(OR_1, left)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFlagEnabled(flag)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfPlayerInOwnWorld(AND_3)
    IfFlagDisabled(AND_3, flag)
    IfActionButtonParamActivated(AND_3, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RestartIfFlagEnabled(flag)
    UnknownSound_2010_11(unk_0_4=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(flag)
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    EndIfPlayerNotInOwnWorld()
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, flag)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31002872)
def Event_31002872(_, flag: uint, obj: uint, model_point: int, right: uint):
    """Event 31002872"""
    EndIfFlagDisabled(3691)
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfCharacterType(OR_2, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagDisabled(AND_2, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_3, right)
    IfFlagDisabled(AND_3, flag)
    IfFailedToCreateSession(OR_4)
    IfMultiplayerState(OR_4, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, flag)
    IfCharacterWhitePhantom(AND_7, PLAYER)
    IfConditionFalse(AND_4, input_condition=AND_7)
    IfFailedToCreateSession(OR_5)
    IfMultiplayerState(OR_5, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_5, input_condition=OR_5)
    IfFlagEnabled(AND_5, flag)
    IfCharacterWhitePhantom(AND_5, PLAYER)
    IfEntityBeyondDistance(AND_5, entity=PLAYER, other_entity=obj, radius=1.0)
    IfConditionTrue(OR_8, input_condition=AND_1)
    IfConditionTrue(OR_8, input_condition=AND_2)
    IfConditionTrue(OR_8, input_condition=AND_3)
    IfConditionTrue(OR_8, input_condition=AND_4)
    IfConditionTrue(OR_8, input_condition=AND_5)
    IfConditionTrue(MAIN, input_condition=OR_8)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_11, input_condition=OR_11)
    IfFlagDisabled(AND_11, flag)
    IfCharacterWhitePhantom(OR_12, PLAYER)
    IfCharacterType(OR_12, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_12, input_condition=OR_12)
    IfFlagDisabled(AND_12, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_13, right)
    IfFlagDisabled(AND_13, flag)
    IfFailedToCreateSession(OR_14)
    IfMultiplayerState(OR_14, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_14, input_condition=OR_14)
    IfFlagEnabled(AND_14, flag)
    IfCharacterWhitePhantom(OR_7, PLAYER)
    IfConditionFalse(AND_14, input_condition=OR_7)
    IfFailedToCreateSession(OR_15)
    IfMultiplayerState(OR_15, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag)
    IfCharacterWhitePhantom(AND_15, PLAYER)
    IfEntityBeyondDistance(AND_15, entity=PLAYER, other_entity=obj, radius=1.0)
    IfConditionFalse(AND_9, input_condition=AND_11)
    IfConditionFalse(AND_9, input_condition=AND_12)
    IfConditionFalse(AND_9, input_condition=AND_13)
    IfConditionFalse(AND_9, input_condition=AND_14)
    IfConditionFalse(AND_9, input_condition=AND_15)
    IfConditionTrue(MAIN, input_condition=AND_9)
    Restart()


@RestartOnRest(31002873)
def Event_31002873(
    _,
    flag: uint,
    unk_0_4: int,
    flag_1: uint,
    flag_2: uint,
    right: uint,
    flag_3: uint,
    left: int,
    left_1: int,
):
    """Event 31002873"""
    EndIfFlagDisabled(3691)
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_1)
    IfFlagEnabled(AND_1, flag_1)
    SkipLinesIfPlayerInOwnWorld(1)
    IfFlagEnabled(AND_1, flag_2)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(1, flag_3)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=0)
    IfFlagEnabled(OR_2, flag_3)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=1)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(2, left=left_1, right=1)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-1)
    End()
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-2)


@RestartOnRest(31002845)
def Event_31002845():
    """Event 31002845"""
    GotoIfFlagEnabled(Label.L2, flag=3863)
    GotoIfFlagDisabled(Label.L0, flag=31000800)
    IfFlagEnabled(AND_1, 31000800)
    IfFlagDisabled(AND_1, 3691)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    IfFlagDisabled(AND_2, 31000850)
    IfFlagEnabled(AND_2, 3691)
    GotoIfConditionTrue(Label.L3, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L4, flag=31000850)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(31000845)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(31000845)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(31000845)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(31000845)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableFlag(31000845)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 31000800)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 31000850)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 3691)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 3683)
    IfConditionTrue(MAIN, input_condition=OR_15)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(31002875)
def Event_31002875():
    """Event 31002875"""
    GotoIfFlagEnabled(Label.L0, flag=3691)
    EnableObject(31001521)
    SkipLinesIfFlagEnabled(1, 31008521)
    EnableObjectActivation(31001521, obj_act_id=200)
    DisableObject(31001523)
    DisableObjectActivation(31001523, obj_act_id=200)
    DisableTreasure(obj=31001523)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(31001521)
    DisableObjectActivation(31001521, obj_act_id=200)
    DisableTreasure(obj=31001521)
    EnableObject(31001523)
    SkipLinesIfFlagEnabled(1, 31008523)
    EnableObjectActivation(31001523, obj_act_id=200)


@RestartOnRest(31002876)
def Event_31002876(
    _,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    obj: uint,
    player_start: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
):
    """Event 31002876"""
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagEnabled(1, obj)
    DeleteObjectVFX(obj, erase_root=False)
    Wait(0.5)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(obj, vfx_id=190, model_point=1300)
    IfTryingToJoinSession(OR_2)
    IfTryingToCreateSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9290, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisplayDialogAndSetFlags(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(PLAYER, 60460, unknown2=1.0)
    Wait(2.5)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(31003700)
def Event_31003700(_, character: uint):
    """Event 31003700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3686)
    IfFlagEnabled(AND_1, 3685)
    IfFlagEnabled(AND_1, 31000800)
    IfFlagDisabled(AND_1, 31002704)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3686)
    IfFlagEnabled(AND_3, 3685)
    IfFlagEnabled(AND_3, 31000800)
    IfFlagDisabled(AND_3, 31002704)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

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
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=31002714)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3686)
    IfFlagEnabled(AND_4, 3685)
    IfFlagEnabled(AND_4, 31000800)
    IfFlagDisabled(AND_4, 31002704)
    IfConditionTrue(OR_4, input_condition=AND_4)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(31003701)
def Event_31003701(_, character: uint, flag: uint, flag_1: uint, character_1: uint):
    """Event 31003701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3683)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    EndIfConditionTrue(input_condition=AND_1)
    GotoIfFlagDisabled(Label.L1, flag=3681)
    GotoIfFlagEnabled(Label.L2, flag=3686)
    GotoIfFlagDisabled(Label.L2, flag=31002704)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 3681)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfCharacterHasSpecialEffect(AND_2, PLAYER, 9700)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)

    # --- Label 3 --- #
    DefineLabel(3)
    IfCharacterHasSpecialEffect(AND_3, PLAYER, 9700)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=character_1, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ClearTargetList(character_1)
    ReplanAI(character_1)
    End()


@RestartOnRest(31003702)
def Event_31003702(_, character: uint):
    """Event 31003702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3685)
    EndIfFlagEnabled(3683)
    IfFlagEnabled(AND_1, 31008521)
    IfFlagEnabled(AND_1, 31002805)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetCharacterTalkRange(character=character, distance=50.0)
    End()


@RestartOnRest(31003703)
def Event_31003703():
    """Event 31003703"""
    EndIfFlagEnabled(3683)
    EndIfFlagEnabled(31000800)
    DisableFlag(31009810)
    DisableFlag(31009215)
    DisableFlag(31009214)
    DisableFlag(31009217)
    WaitFrames(frames=1)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3682)
    IfFlagEnabled(MAIN, 31000800)
    DisableFlag(31009219)
    End()


@RestartOnRest(31003704)
def Event_31003704(_, character: uint, seconds: float):
    """Event 31003704"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3685)
    EndIfFlagEnabled(3683)
    EndIfFlagEnabled(31000800)
    GotoIfFlagEnabled(Label.L2, flag=31002713)
    SkipLinesIfFlagEnabled(1, 31002704)
    DisableFlag(31009811)
    GotoIfFlagEnabled(Label.L1, flag=31002704)
    EnableImmortality(character)
    IfHealthLessThanOrEqual(MAIN, character, value=0.5)
    DisableImmortality(character)
    EndIfFlagEnabled(3683)
    EnableFlag(31002704)
    EnableFlag(31009811)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    AddSpecialEffect(character, 9701)
    AddSpecialEffect(character, 5005)
    AddSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9645)
    SkipLinesIfPlayerNotInOwnWorld(1)
    CancelSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9647)
    AddSpecialEffect(character, 9642)
    SetTeamType(character, TeamType.FriendlyNPC)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfTimeElapsed(OR_2, seconds=seconds)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfFlagEnabled(OR_3, 31002713)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFlagEnabled(Label.L2, flag=31002713)
    EndIfFlagEnabled(3683)
    SkipLinesIfFinishedConditionTrue(1, input_condition=OR_2)
    Restart()
    EnableFlag(31009215)
    EnableFlag(31009810)
    DisableFlag(31009201)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    SetCharacterTalkRange(character=character, distance=17.0)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(60819)
    IfCharacterDead(AND_10, character, target_comparison_type=ComparisonType.NotEqual)
    IfFlagEnabled(AND_10, 31000800)
    IfConditionTrue(MAIN, input_condition=AND_10)
    EnableFlag(60819)
    Unknown_2003_71(unk_0_4=41)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFramesAfterCutscene(frames=1)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    AddSpecialEffect(character, 9704)
    AddSpecialEffect(character, 9644)
    AddSpecialEffect(character, 9643)
    SetTeamType(character, TeamType.Enemy)
    End()


@RestartOnRest(31003705)
def Event_31003705(_, character: uint):
    """Event 31003705"""
    GotoIfPlayerNotInOwnWorld(Label.L1)
    WaitFrames(frames=1)
    EndIfFlagDisabled(3685)
    EndIfFlagEnabled(3683)
    EndIfFlagEnabled(31000800)
    DisableFlag(31009212)
    DisableFlag(31009211)
    DisableFlag(31009213)
    IfFlagEnabled(AND_1, 31002703)
    IfFlagDisabled(AND_1, 3683)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(2.5)
    EndIfFlagEnabled(31000800)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(AND_2, attacked_entity=character, attacker=PLAYER)
    IfFlagDisabled(AND_2, 3683)
    IfPlayerInOwnWorld(AND_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EndIfFlagEnabled(31000800)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(AND_10, attacked_entity=character, attacker=PLAYER)
    IfFlagDisabled(AND_10, 3683)
    IfPlayerInOwnWorld(AND_10)
    IfConditionTrue(MAIN, input_condition=AND_10)
    EndIfFlagEnabled(31000800)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(AND_3, attacked_entity=character, attacker=PLAYER)
    IfFlagDisabled(AND_3, 3683)
    IfPlayerInOwnWorld(AND_3)
    IfConditionTrue(MAIN, input_condition=AND_3)
    EndIfFlagEnabled(31000800)
    EnableNetworkFlag(31002713)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 31002713)
    EndIfFlagEnabled(31000800)
    SetTeamType(character, TeamType.Enemy)
    End()


@RestartOnRest(31003706)
def Event_31003706(_, character: uint, flag: uint, first_flag: uint, last_flag: uint):
    """Event 31003706"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(31000800)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, 3685)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31002714)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()


@RestartOnRest(31003707)
def Event_31003707():
    """Event 31003707"""
    WaitFrames(frames=1)
    IfFlagEnabled(OR_10, 3685)
    IfFlagEnabled(OR_10, 3691)
    IfFlagEnabled(OR_10, 3692)
    IfFlagEnabled(OR_10, 3694)
    SkipLinesIfConditionFalse(3, OR_10)
    DisableObject(31001700)
    DisableObjectActivation(31001700, obj_act_id=200)
    End()
    EnableObject(31001700)
    EnableObjectActivation(31001700, obj_act_id=200)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagDisabled(2, 31008522)
    DisableObjectActivation(31001700, obj_act_id=200)
    End()
    IfFlagEnabled(MAIN, 31008522)
    CreateTemporaryVFX(vfx_id=806881, anchor_entity=31001700, model_point=90, anchor_type=CoordEntityType.Object)
    CreateTemporaryVFX(vfx_id=806882, anchor_entity=31001700, model_point=90, anchor_type=CoordEntityType.Object)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=1, unknown4=0.0)
    Wait(2.200000047683716)
    IfHealthValueEqual(AND_1, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(2.799999952316284)
    IfHealthValueEqual(AND_2, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_2)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=0.0)
    GotoIfFlagEnabled(Label.L1, flag=3683)
    GotoIfFlagDisabled(Label.L1, flag=3686)
    GotoIfFlagEnabled(Label.L2, flag=31009231)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    WarpToMap(game_map=EAST_LIMGRAVE_SW_NE, player_start=1045372710)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    UnknownCutscene_11(
        cutscene_id=31000001,
        cutscene_flags=0,
        move_to_region=1045372710,
        map_base_id=60453700,
        player_id=10000,
        unknown2=0,
        unknown3=1,
    )
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    UnknownCutscene_11(
        cutscene_id=31000000,
        cutscene_flags=0,
        move_to_region=1045372710,
        map_base_id=60453700,
        player_id=10000,
        unknown2=0,
        unknown3=1,
    )
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=0.0)
    End()


@RestartOnRest(31003709)
def Event_31003709():
    """Event 31003709"""
    DisableCharacter(31000702)
    DisableCharacter(31000703)
    DisableBackread(31000702)
    DisableBackread(31000703)
    End()


@RestartOnRest(31003710)
def Event_31003710(_, character: uint):
    """Event 31003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3692)
    GotoIfFlagEnabled(Label.L5, flag=3694)
    IfFlagEnabled(AND_1, 3691)
    IfFlagEnabled(AND_1, 31000850)
    IfFlagEnabled(AND_1, 3683)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3692)
    IfFlagEnabled(OR_3, 3694)
    IfFlagEnabled(AND_3, 3691)
    IfFlagEnabled(AND_3, 31000850)
    IfFlagEnabled(AND_3, 3683)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

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
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=31002723)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3692)
    IfFlagEnabled(OR_4, 3694)
    IfFlagEnabled(AND_4, 3691)
    IfFlagEnabled(AND_4, 31000850)
    IfFlagEnabled(AND_4, 3683)
    IfConditionTrue(OR_4, input_condition=AND_4)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(31003711)
def Event_31003711(_, character: uint, flag: uint, flag_1: uint, character_1: uint):
    """Event 31003711"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3683)
    IfFlagDisabled(AND_1, 3691)
    IfFlagDisabled(AND_1, 3692)
    IfFlagDisabled(AND_1, 3694)
    EndIfConditionTrue(input_condition=AND_1)
    GotoIfFlagDisabled(Label.L1, flag=3681)
    GotoIfFlagEnabled(Label.L2, flag=3686)
    GotoIfFlagDisabled(Label.L2, flag=31002727)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 3681)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfCharacterHasSpecialEffect(AND_2, PLAYER, 9700)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)

    # --- Label 3 --- #
    DefineLabel(3)
    IfCharacterHasSpecialEffect(AND_3, PLAYER, 9700)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=character_1, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ClearTargetList(character_1)
    ReplanAI(character_1)
    End()


@RestartOnRest(31003712)
def Event_31003712():
    """Event 31003712"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(31002715)
    End()


@RestartOnRest(31003713)
def Event_31003713(_, character: uint):
    """Event 31003713"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    EndIfFlagDisabled(3691)
    EndIfFlagEnabled(3683)
    GotoIfFlagEnabled(Label.L1, flag=31000850)
    DisableFlag(31009889)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3682)
    SaveRequest()
    IfFlagEnabled(AND_1, 31008523)
    IfFlagEnabled(AND_1, 31002855)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetCharacterTalkRange(character=character, distance=50.0)
    IfFlagEnabled(MAIN, 31000850)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(31009269)
    End()


@RestartOnRest(31003714)
def Event_31003714(_, character: uint, seconds: float):
    """Event 31003714"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3691)
    EndIfFlagEnabled(3683)
    EndIfFlagEnabled(31000850)
    GotoIfFlagEnabled(Label.L2, flag=31002722)
    GotoIfFlagEnabled(Label.L1, flag=31002730)
    EnableImmortality(character)
    IfFlagEnabled(AND_5, 31009257)
    IfConditionTrue(MAIN, input_condition=AND_5)
    GotoIfFlagEnabled(Label.L5, flag=31002855)
    IfFlagEnabled(MAIN, 31002855)

    # --- Label 5 --- #
    DefineLabel(5)
    Wait(3.0)
    DisableImmortality(character)
    AddSpecialEffect(character, 18670)
    EndIfFlagEnabled(3683)
    EnableFlag(31002721)
    IfFlagEnabled(MAIN, 31002730)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    AddSpecialEffect(character, 9701)
    AddSpecialEffect(character, 5005)
    AddSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9645)
    SkipLinesIfPlayerNotInOwnWorld(1)
    CancelSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9647)
    AddSpecialEffect(character, 9642)
    SetTeamType(character, TeamType.FriendlyNPC)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfTimeElapsed(OR_2, seconds=seconds)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfFlagEnabled(OR_3, 31002722)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFlagEnabled(Label.L2, flag=31002722)
    EndIfFlagEnabled(3683)
    SkipLinesIfFinishedConditionTrue(1, input_condition=OR_2)
    Restart()
    EnableFlag(31002728)
    EnableFlag(31009889)
    DisableFlag(31009201)
    AddSpecialEffect(character, 9706)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    SetCharacterTalkRange(character=character, distance=17.0)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(60832)
    IfCharacterDead(AND_10, character, target_comparison_type=ComparisonType.NotEqual)
    IfFlagEnabled(AND_10, 31000850)
    IfConditionTrue(MAIN, input_condition=AND_10)
    EnableFlag(60832)
    Unknown_2003_71(unk_0_4=90)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFramesAfterCutscene(frames=1)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    AddSpecialEffect(character, 9704)
    AddSpecialEffect(character, 9644)
    AddSpecialEffect(character, 9706)
    AddSpecialEffect(character, 9643)
    SetTeamType(character, TeamType.Enemy)
    End()


@RestartOnRest(31003715)
def Event_31003715(_, attacked_entity: uint):
    """Event 31003715"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    EndIfFlagDisabled(3691)
    EndIfFlagEnabled(3683)
    EndIfFlagEnabled(31000850)
    IfFlagEnabled(AND_1, 31002720)
    IfFlagDisabled(AND_1, 3683)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(2.5)
    EndIfFlagEnabled(31000850)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(AND_2, attacked_entity=attacked_entity, attacker=PLAYER)
    IfFlagDisabled(AND_2, 3683)
    IfPlayerInOwnWorld(AND_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EndIfFlagEnabled(31000850)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(AND_10, attacked_entity=attacked_entity, attacker=PLAYER)
    IfFlagDisabled(AND_10, 3683)
    IfPlayerInOwnWorld(AND_10)
    IfConditionTrue(MAIN, input_condition=AND_10)
    EndIfFlagEnabled(31000850)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(AND_3, attacked_entity=attacked_entity, attacker=PLAYER)
    IfFlagDisabled(AND_3, 3683)
    IfPlayerInOwnWorld(AND_3)
    IfConditionTrue(MAIN, input_condition=AND_3)
    EndIfFlagEnabled(31000850)
    EnableNetworkFlag(31002722)
    End()


@RestartOnRest(31003716)
def Event_31003716(_, character: uint, flag: uint, first_flag: uint, last_flag: uint):
    """Event 31003716"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(31000800)
    EndIfFlagEnabled(31000850)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, 3691)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31002723)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
