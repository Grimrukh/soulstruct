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
    RegisterGrace(grace_flag=301700, obj=30171950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(30171150, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005525, args=(30170570, 30171570), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(30170560, 30171560, 30171561, 0, 30172560, 30172561, 30172562),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30170560, 30171563), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(30170565, 30171565, 30171566, 0, 30172565, 30172566, 30172567),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30170565, 30171568), arg_types="II")
    Event_30172400(0, character=30170200)
    Event_30172400(1, character=30170201)
    Event_30172400(2, character=30170202)
    RunCommonEvent(0, 90005261, args=(30170223, 30172223, 15.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(30170200, 30002, 20002, 30172450, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30170201, 30002, 20002, 30172450, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(2, 90005261, args=(30170202, 30172450, 7.0, 0.0, 0), arg_types="IIffi")
    Event_30172400(3, character=30170204)
    Event_30172400(4, character=30170205)
    Event_30172400(5, character=30170206)
    RunCommonEvent(0, 90005200, args=(30170204, 30000, 20000, 30172204, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30170205, 30000, 20000, 30172204, 3.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        2,
        90005200,
        args=(30170206, 30000, 20000, 30172204, 4.199999809265137, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    Event_30172400(6, character=30170210)
    Event_30172400(7, character=30170211)
    Event_30172400(8, character=30170219)
    RunCommonEvent(0, 90005250, args=(30170219, 30172315, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170219, 30172217, 0.0, 3005), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30170210, 30002, 20002, 30172210, 5.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30170211, 30002, 20002, 30172210, 5.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30172400(9, character=30170215)
    Event_30172402(0, character=30170216, region=30172202)
    Event_30172400(10, character=30170316)
    RunCommonEvent(0, 90005250, args=(30170215, 30172221, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170216, 30172201, 0.0, -1), arg_types="IIfi")
    Event_30172311()
    RunCommonEvent(0, 90005250, args=(30170317, 30172318, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170316, 30172318, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170215, 30172214, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170300, 30172300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30170301, 30172300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170305, 30172305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170306, 30172306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170309, 30172309, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170310, 30172350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170313, 30172310, 0.0, 3015), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(30170314, 30172315, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(30170315, 30172315, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(30170350, 30172315, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170201, 30172223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170200, 30172223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30170311, 30172353, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(30170312, 30172353, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30170313, 30000, 20000, 30172353, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30172400(12, character=30170250)
    Event_30172400(13, character=30170251)
    Event_30172400(14, character=30170252)
    RunCommonEvent(1, 90005250, args=(30170250, 30172451, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30170251, 30172216, 0.0, 3025), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30170252, 30172450, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170351, 30172351, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30170351, 30172352, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30170350, 30001, 20001, 30172315, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30170352, 30172353, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30170450, 30000, 20000, 30172451, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30170400, 30000, 20000, 30172410, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30172400(11, character=30170400)
    RunCommonEvent(0, 90005300, args=(30170400, 30170400, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005652, args=(30170540, 30171540, 30170400), arg_types="III")
    RunCommonEvent(0, 90005651, args=(30170540, 30171540), arg_types="II")
    Event_30172600()
    RunCommonEvent(
        0,
        90005501,
        args=(30170530, 30170531, 4, 30171530, 30171531, 30171532, 30170532),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(30170510, 30171510, 1, 30171510, 30171511, 30171512, 30170511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(30170515, 30170516, 0, 30171515, 30171516, 30171517, 30170517),
        arg_types="IIIIIII",
    )
    Event_30172510()
    RunCommonEvent(0, 90005513, args=(30170542, 30171542, 30171543, 30173543, 27115, 0, 0), arg_types="IIIIiii")
    Event_30172520()
    RunCommonEvent(0, 90005680, args=(30170500, 30170501, 30170502, 30170503, 30171500), arg_types="IIIII")
    RunCommonEvent(0, 90005680, args=(30170500, 30170501, 30170502, 30170503, 30171500), arg_types="IIIII")
    RunCommonEvent(0, 90005681, args=(30170500, 30170501, 30170502, 30170503, 30171500), arg_types="IIIII")
    Event_30172500()
    Event_30172525()
    Event_30172580()
    Event_30172800()
    Event_30172810()
    Event_30172849()
    Event_30122811()
    RunCommonEvent(
        0,
        90005646,
        args=(30170800, 30172840, 30172841, 30171840, 30172840, 30, 17, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(30172800, 30171695, 5), arg_types="IIi")
    Event_16002520(0, flag=30170620, obj=30171620)
    Event_30170050()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30170519()


@NeverRestart(30170050)
def Event_30170050():
    """Event 30170050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30170500)


@RestartOnRest(30172250)
def Event_30172250(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30172250"""
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


@RestartOnRest(30172200)
def Event_30172200(_, character: uint):
    """Event 30172200"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 17153)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30172200)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 17153)
    AddSpecialEffect(character, 17152)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30172311)
def Event_30172311():
    """Event 30172311"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30172316)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=30170316, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    ForceAnimation(30170316, 3004, wait_for_completion=True, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30172400)
def Event_30172400(_, character: uint):
    """Event 30172400"""
    IfCharacterDead(OR_2, character)
    IfThisEventSlotFlagEnabled(OR_2)
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AddSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4320)
    DisableAnimations(character)
    IfCharacterInsideRegion(OR_1, character=character, region=30172405)
    IfCharacterInsideRegion(AND_1, character=character, region=30172406)
    IfFlagEnabled(AND_1, 30170526)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterInsideRegion(AND_2, character=character, region=30172407)
    IfFlagEnabled(AND_2, 30170521)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfCharacterInsideRegion(AND_3, character=character, region=30172408)
    IfFlagEnabled(AND_3, 30170522)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableThisSlotFlag()
    AddSpecialEffect(character, 5881)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 5882)
    CancelSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()


@RestartOnRest(30172401)
def Event_30172401(_, character: uint):
    """Event 30172401"""
    IfCharacterDead(OR_2, character)
    IfThisEventSlotFlagEnabled(OR_2)
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AddSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4320)
    EnableInvincibility(character)
    DisableAnimations(character)
    IfCharacterInsideRegion(OR_1, character=character, region=30172405)
    IfCharacterInsideRegion(AND_1, character=character, region=30172406)
    IfFlagEnabled(AND_1, 30170526)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterInsideRegion(AND_2, character=character, region=30172407)
    IfFlagEnabled(AND_2, 30170521)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfCharacterInsideRegion(AND_3, character=character, region=30172408)
    IfFlagEnabled(AND_3, 30170522)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CancelSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4321)
    DisableInvincibility(character)
    EnableAnimations(character)
    End()


@RestartOnRest(30172402)
def Event_30172402(_, character: uint, region: uint):
    """Event 30172402"""
    IfCharacterDead(OR_2, character)
    IfThisEventSlotFlagEnabled(OR_2)
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    EnableSpawner(entity=30173216)
    Wait(4.0)
    AddSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4320)
    EnableInvincibility(character)
    DisableAnimations(character)
    IfCharacterInsideRegion(OR_1, character=character, region=30172405)
    IfCharacterInsideRegion(AND_1, character=character, region=30172406)
    IfFlagEnabled(AND_1, 30170526)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterInsideRegion(AND_2, character=character, region=30172407)
    IfFlagEnabled(AND_2, 30170521)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfCharacterInsideRegion(AND_3, character=character, region=30172408)
    IfFlagEnabled(AND_3, 30170522)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CancelSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4321)
    DisableInvincibility(character)
    EnableAnimations(character)
    End()


@NeverRestart(30172500)
def Event_30172500():
    """Event 30172500"""
    RunCommonEvent(0, 90005681, args=(30170500, 30170501, 30170502, 30170503, 30171500), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105070, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105060, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105050, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105040, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105030, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105020, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105010, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30170502, 30171500, 30172500, 30170500, 801105000, 801105005, 101, 104, 100, 0),
        arg_types="IIIIiiiiii",
    )


@NeverRestart(30172501)
def Event_30172501(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, attacked_entity: uint):
    """Event 30172501"""
    SkipLinesIfFlagEnabled(1, 30170504)
    GotoIfFlagDisabled(Label.L20, flag=30170504)
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_3)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    IfFlagDisabled(OR_1, flag)
    IfFlagEnabled(AND_2, flag_1)
    IfAttackedWithDamageType(AND_2, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    ForceAnimation(attacked_entity, 21, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_5, flag)
    IfFlagDisabled(AND_6, flag_1)
    IfAttackedWithDamageType(AND_6, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(MAIN, input_condition=OR_8)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(30170504)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    EnableFlag(flag_1)
    ForceAnimation(attacked_entity, 12, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)
    EnableFlag(flag_2)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_3)
    Restart()


@NeverRestart(30172502)
def Event_30172502(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
):
    """Event 30172502"""
    IfFlagEnabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=801105000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=801105005,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=801105000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=801105005,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=801105000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=801105005,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=801105000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=801105005,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30172510)
def Event_30172510():
    """Event 30172510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30170510,
            30171510,
            1,
            30171510,
            30171511,
            30173511,
            30171512,
            30173512,
            30172511,
            30172512,
            30170511,
            30172512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            30170515,
            30171516,
            0,
            30171515,
            30171516,
            30173516,
            30171517,
            30173517,
            30172516,
            30172517,
            30170517,
            30172517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            30170530,
            30170531,
            4,
            30171530,
            30171531,
            30173531,
            30171532,
            30173532,
            30172531,
            30172532,
            30170532,
            30172532,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30170519)
def Event_30170519():
    """Event 30170519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30170530)
    EnableFlag(30170510)
    EnableFlag(30170515)


@RestartOnRest(30172520)
def Event_30172520():
    """Event 30172520"""
    GotoIfFlagDisabled(Label.L0, flag=30170515)
    IfFlagEnabled(MAIN, 30170515)
    Wait(4.0)
    DeleteVFX(30172403)
    DisableFlag(30170522)
    Wait(6.0)
    CreateVFX(30172402)
    EnableFlag(30170521)
    IfFlagDisabled(MAIN, 30170515)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    DeleteVFX(30172402)
    DisableFlag(30170521)
    Wait(9.0)
    CreateVFX(30172403)
    EnableFlag(30170522)
    IfFlagEnabled(MAIN, 30170515)
    Restart()


@RestartOnRest(30172525)
def Event_30172525():
    """Event 30172525"""
    IfFlagEnabled(MAIN, 30170500)
    Wait(3.0)
    CreateVFX(30172401)
    EnableFlag(30170526)
    IfFlagDisabled(MAIN, 30170500)
    Wait(0.30000001192092896)
    DeleteVFX(30172401)
    DisableFlag(30170526)
    Restart()


@NeverRestart(30172580)
def Event_30172580():
    """Event 30172580"""
    RegisterLadder(start_climbing_flag=30170580, stop_climbing_flag=30170581, obj=30171580)
    RegisterLadder(start_climbing_flag=30170582, stop_climbing_flag=30170583, obj=30171582)


@RestartOnRest(30172600)
def Event_30172600():
    """Event 30172600"""
    EndIfFlagEnabled(30170400)
    IfCharacterDead(MAIN, 30170400)
    EnableFlag(30170400)
    End()


@RestartOnRest(30172800)
def Event_30172800():
    """Event 30172800"""
    EndIfFlagEnabled(30170800)
    IfHealthValueLessThanOrEqual(MAIN, 30170800, value=0)
    Wait(4.0)
    PlaySoundEffect(30170800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30170800)
    KillBossAndDisplayBanner(character=30170800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30170800)
    EnableFlag(9217)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61217)


@RestartOnRest(30172810)
def Event_30172810():
    """Event 30172810"""
    GotoIfFlagDisabled(Label.L0, flag=30170800)
    DisableCharacter(30170800)
    DisableAnimations(30170800)
    Kill(30170800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30170800)
    IfFlagEnabled(AND_2, 30172805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30172800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30170800)
    SetNetworkUpdateRate(30170800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30170800, name=907100301)


@RestartOnRest(30122811)
def Event_30122811():
    """Event 30122811"""
    EndIfFlagEnabled(30170800)
    IfHealthLessThanOrEqual(AND_1, 30170800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30172802)


@RestartOnRest(30172849)
def Event_30172849():
    """Event 30172849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30170800, 30171800, 30172800, 30172805, 30175800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30170800, 30171800, 30172800, 30172805, 30172806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30170800, 30171800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30170800, 920200, 30172805, 30172806, 0, 30172802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(16002520)
def Event_16002520(_, flag: uint, obj: uint):
    """Event 16002520"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=obj, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
