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
    RegisterGrace(grace_flag=311800, obj=31181950, unknown=5.0)
    Event_31182800()
    Event_31182801()
    Event_31182802()
    Event_31182810()
    Event_31182849()
    Event_31182811()
    RunCommonEvent(
        0,
        90005646,
        args=(31180800, 31182840, 31182841, 31181840, 31182840, 31, 18, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_31182500(0, obj=31181500, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(1, obj=31181501, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(2, obj=31181502, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(3, obj=31181503, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(4, obj=31181504, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(5, obj=31181505, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(6, obj=31181506, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(7, obj=31181507, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(8, obj=31181508, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182515()
    RunCommonEvent(0, 900005610, args=(31181200, 100, 800, 0), arg_types="IiiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31180200, 31182200, 2.0, 3.4000000953674316, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31180202, 31182200, 2.0, 3.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31180203, 30000, 20000, 31182203, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31180207, 30000, 20000, 31182207, 2.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_31182200(0, character=31180200, region=31182250)
    Event_31182200(1, character=31180201, region=31182251)
    Event_31182200(2, character=31180202, region=31182252)
    Event_31182200(3, character=31180207, region=31182257)
    RunCommonEvent(0, 90005261, args=(31180300, 31182300, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31180306, 31182306, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31180307, 31182307, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31180310, 30000, 20000, 31182310, 0.0, 9.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31180311, 30000, 20000, 31182310, 0.0, 10.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31180314, 31182314, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31180315, 31182314, 10.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31180351, 31182351, 2.0, 0.0, 3001), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31180355, 31182355, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31182402(0, 31180400, 31182400, 3.0, 0.0, 3012, 32052401)
    RunCommonEvent(0, 90005300, args=(31180400, 31180400, 0, 0.0, 0), arg_types="IIifi")
    Event_31182400()


@RestartOnRest(31182500)
def Event_31182500(_, obj: uint, vfx_id: int, model_point: int, model_point_1: int):
    """Event 31182500"""
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=model_point)
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=model_point_1)


@RestartOnRest(31182515)
def Event_31182515():
    """Event 31182515"""
    CreateTemporaryVFX(vfx_id=802020, anchor_entity=31182515, anchor_type=CoordEntityType.Region)


@RestartOnRest(31182200)
def Event_31182200(_, character: uint, region: uint):
    """Event 31182200"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=6.0)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Battle)
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
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=OR_3)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfAttackedWithDamageType(OR_5, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_5)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31182400)
def Event_31182400():
    """Event 31182400"""
    IfCharacterDead(AND_1, 31180400)
    EndIfConditionTrue(input_condition=AND_1)
    ForceAnimation(31180400, 0, unknown2=1.0)


@RestartOnRest(31182401)
def Event_31182401():
    """Event 31182401"""
    EndIfFlagEnabled(31180400)
    IfCharacterDead(OR_1, 31180400)
    EnableFlag(31180400)


@RestartOnRest(31182402)
def Event_31182402(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int, region_1: uint):
    """Event 31182402"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_15, character=PLAYER, region=region_1)
    IfCharacterInsideRegion(OR_15, character=PLAYER, region=region)
    IfConditionTrue(OR_3, input_condition=OR_15)
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
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    IfCharacterInsideRegion(OR_14, character=PLAYER, region=region_1)
    GotoIfConditionTrue(Label.L1, input_condition=OR_14)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31182800)
def Event_31182800():
    """Event 31182800"""
    EndIfFlagEnabled(31180800)
    IfCharacterDead(AND_1, 31180800)
    IfCharacterDead(AND_1, 31180801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    KillBossAndDisplayBanner(character=31180800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31180800)
    EnableFlag(9241)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61241)


@RestartOnRest(31182801)
def Event_31182801():
    """Event 31182801"""
    EndIfFlagEnabled(31180800)
    IfHealthValueLessThanOrEqual(MAIN, 31180800, value=0)
    Wait(4.0)
    PlaySoundEffect(31180800, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31182802)
def Event_31182802():
    """Event 31182802"""
    EndIfFlagEnabled(31180800)
    IfHealthValueLessThanOrEqual(MAIN, 31180801, value=0)
    Wait(4.0)
    PlaySoundEffect(31180801, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31182810)
def Event_31182810():
    """Event 31182810"""
    GotoIfFlagDisabled(Label.L0, flag=31180800)
    DisableCharacter(31180800)
    DisableCharacter(31180801)
    DisableAnimations(31180800)
    DisableAnimations(31180801)
    Kill(31180800)
    Kill(31180801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31180800)
    DisableAI(31180801)
    ForceAnimation(31180800, 30001, unknown2=1.0)
    IfFlagEnabled(AND_1, 31182805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31182800)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBossHealthBar(31180800, name=904480310)
    EnableBossHealthBar(31180801, name=904820310, bar_slot=1)
    Wait(0.5)
    EnableAI(31180800)
    EnableAnimations(31180800)
    SetNetworkUpdateRate(31180800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(31180800, 20001, unknown2=1.0)
    EnableAI(31180801)
    EnableAnimations(31180801)
    SetNetworkUpdateRate(31180801, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(31182811)
def Event_31182811():
    """Event 31182811"""
    EndIfFlagEnabled(31180800)
    IfCharacterDead(OR_15, 31180800)
    IfCharacterDead(OR_15, 31180801)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31182842)


@RestartOnRest(31182849)
def Event_31182849():
    """Event 31182849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31180800, 31181800, 31182800, 31182805, 31185800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31180800, 31181800, 31182800, 31182805, 31182806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31180800, 31181800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31180800, 920900, 31182805, 31182806, 0, 31182842, 0, 0), arg_types="IiIIIIii")
