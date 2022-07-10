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
    RegisterGrace(grace_flag=301600, obj=30161950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(30161200, 100, 800, 0), arg_types="IiiI")
    Event_30162800()
    Event_30162810()
    Event_30162849()
    Event_30162811()
    RunCommonEvent(0, 90005200, args=(30160316, 30000, 20000, 30162316, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005211, args=(30160314, 30001, 20001, 30162242, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_30162622()
    RunCommonEvent(0, 90005250, args=(30160221, 30162221, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005650, args=(30160540, 30161540, 30161541, 30163541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30160540, 30161540), arg_types="II")
    RunCommonEvent(
        0,
        90005646,
        args=(30160800, 30162840, 30162841, 30161840, 30162840, 30, 16, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(30160212, 30008, 20008, 30162212, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160230, 30010, 20010, 30162230, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160235, 30010, 20010, 30162230, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160216, 30008, 20008, 30162216, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30160211, 30162221, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30160204, 30002, 20002, 30162204, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30160205, 30162205, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30160206, 30010, 20010, 30162206, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(30160200, 30010, 20010, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(30160201, 30010, 20010, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(30160202, 30010, 20010, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(30160203, 30010, 20010, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(30160308, 30003, 20003, 30162244, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160301, 30003, 20003, 30162301, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160300, 30003, 20003, 30162244, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160302, 30003, 20003, 30162302, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160304, 30003, 20003, 30162210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160303, 30003, 20003, 30162210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160213, 30008, 20008, 30162210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160214, 30008, 20008, 30162210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30160340, 30001, 20001, 30162210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30162602(0, character=30160341, character_1=30160340, animation_id=20001)
    Event_30162602(1, character=30160342, character_1=30160341, animation_id=20001)
    Event_30162621(0, 30165290)


@RestartOnRest(30162601)
def Event_30162601(_, region: uint, entity: uint):
    """Event 30162601"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableSpawner(entity=entity)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30162602)
def Event_30162602(_, character: uint, character_1: uint, animation_id: int):
    """Event 30162602"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    IfCharacterDead(MAIN, character_1)
    EnableCharacter(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)


@RestartOnRest(30162511)
def Event_30162511(_, character: uint, special_effect_id: int, region: uint):
    """Event 30162511"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(30162622)
def Event_30162622():
    """Event 30162622"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30162245)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangePatrolBehavior(30160314, patrol_information_id=30163314)


@RestartOnRest(30162621)
def Event_30162621(_, character: uint):
    """Event 30162621"""
    ReturnIfFlagState(EventReturnType.End, FlagSetting.On, FlagType.RelativeToThisEventSlot, 30162621)
    AddSpecialEffect(character, 4802)
    AddSpecialEffect(character, 4800)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160303, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160304, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160213, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160214, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160340, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160341, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160342, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160303, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160304, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160213, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160214, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160340, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160341, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=30160342, attacker=35000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=character, radius=5.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=character, radius=5.0)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 30162621, state=FlagSetting.On)
    CancelSpecialEffect(character, 4800)
    AddSpecialEffect(character, 4802)
    Wait(90.0)
    IfCharacterType(AND_10, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_10, PLAYER, 3710)
    IfConditionTrue(OR_15, input_condition=AND_10)
    IfCharacterHuman(OR_15, PLAYER)
    IfCharacterHollow(OR_15, PLAYER)
    IfCharacterWhitePhantom(OR_15, PLAYER)
    IfConditionTrue(AND_4, input_condition=OR_15)
    IfConditionTrue(AND_5, input_condition=OR_15)
    IfCharacterInsideRegion(AND_4, character=PLAYER, region=30162256)
    SkipLinesIfConditionFalse(1, AND_4)
    MakeEnemyAppear(character=30163256)
    IfCharacterInsideRegion(AND_5, character=PLAYER, region=30162258)
    SkipLinesIfConditionFalse(1, AND_5)
    MakeEnemyAppear(character=30163258)
    Restart()


@RestartOnRest(30162520)
def Event_30162520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30162520"""
    EndIfFlagEnabled(flag)
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)


@RestartOnRest(30162800)
def Event_30162800():
    """Event 30162800"""
    EndIfFlagEnabled(30160800)
    IfHealthValueLessThanOrEqual(MAIN, 30160800, value=0)
    Wait(4.0)
    PlaySoundEffect(30160800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30160800)
    KillBossAndDisplayBanner(character=30160800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30160800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61216)
    EnableFlag(9216)


@RestartOnRest(30162810)
def Event_30162810():
    """Event 30162810"""
    GotoIfFlagDisabled(Label.L0, flag=30160800)
    DisableCharacter(30160800)
    DisableAnimations(30160800)
    Kill(30160800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30160800)
    DisableHealthBar(30160800)
    ForceAnimation(30160800, 30002, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 30162805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30162800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(30160800, 20002, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30160800)
    SetNetworkUpdateRate(30160800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(4.300000190734863)
    EnableBossHealthBar(30160800, name=904640300)


@RestartOnRest(30162811)
def Event_30162811():
    """Event 30162811"""
    EndIfFlagEnabled(30160800)
    IfHealthLessThanOrEqual(AND_1, 30160800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30162802)


@RestartOnRest(30162849)
def Event_30162849():
    """Event 30162849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30160800, 30161800, 30162800, 30162805, 30165800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30160800, 30161800, 30162800, 30162805, 30162806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30160800, 30161800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30160800, 920600, 30162805, 30162806, 0, 30162802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30162900)
def Event_30162900():
    """Event 30162900"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 30160800)
    CreateObjectVFX(30161900, vfx_id=90, model_point=1300)
    IfActionButtonParamActivated(MAIN, action_button_id=9000, entity=30161900)
    WarpToMap(game_map=MOHGWYN_PALACE, player_start=12052900)
