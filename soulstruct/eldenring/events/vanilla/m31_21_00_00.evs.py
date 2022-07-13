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
    RegisterGrace(grace_flag=31210000, obj=31211950, unknown=5.0)
    Event_31212800()
    Event_31212810()
    Event_31212815()
    Event_31032849()
    Event_312112811()
    Event_31212830(0, flag=31210801, character=31210100)
    Event_31212860()
    RunCommonEvent(0, 900005610, args=(31211200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(31211201, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005261, args=(31210800, 31212810, 10.0, 0.0, 0), arg_types="IIffi")
    Event_31212500()
    RunCommonEvent(
        0,
        90005646,
        args=(31210800, 31212840, 31212841, 31211840, 31212840, 31, 21, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 90005511, args=(31210560, 31211560, 31213560, 27043, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(31210560, 31212560, 31212561), arg_types="III")
    Event_31212400(
        0,
        flag=31210600,
        obj=31211600,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        1,
        flag=31210600,
        obj=31211602,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        2,
        flag=31210600,
        obj=31211604,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        3,
        flag=31210600,
        obj=31211606,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        4,
        flag=31210600,
        obj=31211608,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        5,
        flag=31210600,
        obj=31211610,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        6,
        flag=31210600,
        obj=31211612,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        7,
        flag=31210600,
        obj=31211614,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        8,
        flag=31210600,
        obj=31211616,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        9,
        flag=31210600,
        obj=31211618,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        10,
        flag=31210600,
        obj=31211620,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    Event_31212400(
        11,
        flag=31210600,
        obj=31211622,
        obj_1=31211601,
        obj_act_id=31213601,
        obj_act_id_1=27080,
        animation_id=0,
        animation_id_1=0
    )
    RunCommonEvent(0, 90005621, args=(1047380570, 31211578), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_31212205()
    RunCommonEvent(0, 90005211, args=(31210209, 30000, 20000, 31212209, 0.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31210210, 31212209, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210219, 31212219, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210220, 31212219, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210221, 31212219, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31212230(0, character=31210227)
    Event_31212230(1, character=31210228)
    Event_31212230(2, character=31210229)
    Event_31212230(3, character=31210230)
    Event_31212230(4, character=31210231)
    Event_31212230(5, character=31210232)
    Event_31212230(6, character=31210233)
    Event_31212230(7, character=31210234)
    Event_31212230(8, character=31210235)
    Event_31212230(9, character=31210236)
    Event_31212230(10, character=31210237)
    Event_31212230(11, character=31210238)
    Event_31212230(12, character=31210239)
    Event_31212230(13, character=31210275)
    Event_31212230(14, character=31210276)
    Event_31212230(15, character=31210277)
    Event_31212250(0, 31210250, 30008, 20008, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(1, 31210251, 30005, 20005, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(2, 31210253, 30008, 20008, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(3, 31210255, 30005, 20005, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(17, 31210282, 30005, 20005, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(18, 31210283, 30005, 20005, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212260(0, character=31210254, region=31212253, patrol_information_id=31213254)
    RunCommonEvent(0, 90005201, args=(31210258, 30002, 20002, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_31212250(4, 31210259, 30008, 20008, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(5, 31210260, 30005, 20005, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(6, 31210261, 30005, 20005, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(7, 31210262, 30008, 20008, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(8, 31210263, 30005, 20005, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212260(1, character=31210264, region=31212259, patrol_information_id=31213264)
    Event_31212250(9, 31210265, 30005, 20005, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(10, 31210266, 30005, 20005, 31212259, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(11, 31210268, 30008, 20008, 31212268, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(12, 31210269, 30005, 20005, 31212268, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(13, 31210270, 30005, 20005, 31212268, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(14, 31210278, 30008, 20008, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212260(2, character=31210279, region=31212253, patrol_information_id=31213279)
    Event_31212250(15, 31210280, 30008, 20008, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    Event_31212250(16, 31210281, 30005, 20005, 31212253, 0.0, 0.0, 0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005261, args=(31210301, 31212300, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210305, 31212305, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210316, 31212316, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210317, 31212316, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31210318, 31212316, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31212308(0, character=31210306, region=31212306)
    Event_31212308(1, character=31210307, region=31212307)
    RunCommonEvent(0, 90005261, args=(31210330, 31212316, 2.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(31212500)
def Event_31212500():
    """Event 31212500"""
    GotoIfFlagDisabled(Label.L0, flag=31210500)
    DisableObject(31211500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31212500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(31211500)
    EnableNetworkFlag(31210500)


@RestartOnRest(31212205)
def Event_31212205():
    """Event 31212205"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(31210205)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31212205)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31212204)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    ChangePatrolBehavior(31210205, patrol_information_id=31213205)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(31210205)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31212210)
def Event_31212210(_, character: uint):
    """Event 31212210"""
    AddSpecialEffect(character, 90000)


@RestartOnRest(31212230)
def Event_31212230(_, character: uint):
    """Event 31212230"""
    Kill(character)


@RestartOnRest(31212250)
def Event_31212250(
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
    patrol_information_id: uint,
):
    """Event 31212250"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
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
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_1, 31210600)
    IfConditionTrue(OR_2, input_condition=AND_1)
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
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    CancelSpecialEffect(character, 8082)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(31212260)
def Event_31212260(_, character: uint, region: uint, patrol_information_id: uint):
    """Event 31212260"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfFlagEnabled(AND_1, 31210600)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_5)
    CancelSpecialEffect(character, 8082)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31212308)
def Event_31212308(_, character: uint, region: uint):
    """Event 31212308"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=2.0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfCharacterInsideRegion(OR_2, character=character, region=region)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    CancelSpecialEffect(character, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31212400)
def Event_31212400(
    _,
    flag: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 31212400"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(obj=obj, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, flag)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    ForceAnimation(obj, animation_id, unknown2=1.0)


@RestartOnRest(31212800)
def Event_31212800():
    """Event 31212800"""
    EndIfFlagEnabled(31210800)
    IfHealthValueLessThanOrEqual(MAIN, 31210800, value=0)
    Wait(4.0)
    PlaySoundEffect(31210800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31210800)
    KillBossAndDisplayBanner(character=31210800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31210800)
    EnableFlag(9243)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61243)


@RestartOnRest(31212810)
def Event_31212810():
    """Event 31212810"""
    GotoIfFlagDisabled(Label.L0, flag=31210800)
    DisableCharacter(31210800)
    DisableAnimations(31210800)
    Kill(31210800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=31210801)
    IfAttackedWithDamageType(OR_1, attacked_entity=31210800, attacker=PLAYER)
    IfHasAIStatus(OR_1, 31210800, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31212805)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=31212801)
    IfConditionTrue(MAIN, input_condition=OR_5)
    EnableNetworkFlag(31210801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(OR_2, attacked_entity=31210800, attacker=PLAYER)
    IfHasAIStatus(OR_2, 31210800, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31212805)
    IfFlagEnabled(AND_2, 31212805)
    IfConditionTrue(OR_6, input_condition=AND_2)
    IfCharacterInsideRegion(OR_6, character=PLAYER, region=31212801)
    IfConditionTrue(MAIN, input_condition=OR_6)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(31210800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31210800, name=903400310)


@RestartOnRest(312112811)
def Event_312112811():
    """Event 312112811"""
    EndIfFlagEnabled(31210800)
    IfHealthRatioLessThanOrEqual(AND_1, 31210800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31212852)


@RestartOnRest(31212815)
def Event_31212815():
    """Event 31212815"""
    GotoIfFlagEnabled(Label.L10, flag=31210800)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=31210801, right=0)
    GotoIfFlagEnabled(Label.L0, flag=31210801)
    IfFlagState(OR_1, FlagSetting.On, FlagType.RelativeToThisEventSlot, 31212810)
    IfFlagEnabled(OR_1, 31210801)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, 31210800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFlagEnabled(31210800)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfPlayerInOwnWorld(AND_3)
    IfFlagDisabled(AND_3, 31210800)
    IfActionButtonParamActivated(AND_3, action_button_id=10000, entity=31211800)
    IfFlagEnabled(OR_3, 31210800)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RestartIfFlagEnabled(31210800)
    UnknownSound_2010_11(unk_0_4=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, 31212800, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, 31212800, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=31212805)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=31212800)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, 31210800)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, 31210800)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(31210800)
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    SkipLinesIfFlagEnabled(1, 31210801)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(31215800, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(31215800)
    EnableNetworkFlag(31212805)
    EndIfPlayerNotInOwnWorld()
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, 31210800)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=31211800)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, 31212800, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31212860)
def Event_31212860():
    """Event 31212860"""
    EndIfFlagEnabled(31210800)
    IfFlagEnabled(AND_1, 31212805)
    IfAttackedWithDamageType(OR_1, attacked_entity=31210800, attacker=PLAYER)
    IfHasAIStatus(OR_1, 31210800, ai_status=AIStatusType.Battle)
    IfUnknownCharacterCondition_34(OR_1, character=31210800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31210800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31210800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31210800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31210800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31212805)
    IfPlayerInOwnWorld(AND_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(31212865)
    NotifyBossBattleStart()


@RestartOnRest(31212830)
def Event_31212830(_, flag: uint, character: uint):
    """Event 31212830"""
    EndIfFlagEnabled(flag)
    AddSpecialEffect(character, 9531)
    AwaitFlagEnabled(flag=flag)
    AddSpecialEffect(character, 9532)


@RestartOnRest(31032849)
def Event_31032849():
    """Event 31032849"""
    RunCommonEvent(0, 9005801, args=(31210800, 31211800, 31212800, 31212865, 31212806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31210800, 31211800, 3, 31210801), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(31210800, 31211801, 3, 31210801), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(31210800, 931000, 31212805, 31212806, 31212810, 31212852, 31212802, 0),
        arg_types="IiIIIIii",
    )
