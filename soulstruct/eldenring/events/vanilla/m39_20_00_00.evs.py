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
    RegisterGrace(grace_flag=39200001, obj=39201951, unknown=5.0)
    RegisterGrace(grace_flag=39200002, obj=39201952, unknown=5.0)
    Event_39202800()
    Event_39202810()
    Event_39202829()
    RunCommonEvent(0, 9005810, args=(39200800, 39200000, 39200950, 39201950, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 900005610, args=(39201640, 100, 800, 0), arg_types="IiiI")
    Event_39202670()
    RunCommonEvent(
        0,
        90005501,
        args=(39200510, 39201510, 0, 39201510, 39201511, 39201512, 39200511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(39200515, 39201515, 0, 39201515, 39201516, 39201517, 39200516),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(39200520, 39201520, 0, 39201520, 39201521, 39201522, 39200521),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(39200525, 39201525, 1, 39201525, 39201526, 39201527, 39200526),
        arg_types="IIIIIII",
    )
    Event_39202500()
    RunCommonEvent(0, 90005502, args=(39200514, 39201521, 39202522), arg_types="III")
    Event_39202580()
    RunCommonEvent(
        0,
        90005780,
        args=(39200800, 39202160, 39202161, 39200700, 20, 39202700, 0, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(39200800, 39202160, 39202161, 39200700), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(39202160, 39202805, 39200700, 39202805, 39202808, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005780,
        args=(39200800, 39202164, 39202165, 39200705, 20, 39202705, 1042559206, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(39200800, 39202164, 39202165, 39200705), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(39202164, 39202805, 39200705, 39202805, 39202809, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005780,
        args=(39200800, 39202168, 39202169, 39200710, 20, 39202720, 39209250, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(39200800, 39202168, 39202169, 39200710), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(39202168, 39202805, 39200710, 39202805, 39202810, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005795,
        args=(7606, 0, 39209200, 39202141, 39202142, 80606, 9000, 39201700, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=50)
    RunCommonEvent(0, 90005796, args=(7606, 39200701, 5, 39202141), arg_types="IIBI")
    Event_39202145()
    Event_39203700()
    Event_39203701()
    RunCommonEvent(0, 90005774, args=(7606, 39200500, 39207500), arg_types="IiI")
    Event_39203710()
    Event_39203720()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(39200701)
    RunCommonEvent(0, 90005250, args=(39200268, 39202268, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(39200254, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(39200277, 0.0, -1), arg_types="Ifi")
    Event_39202280(0, 39200259, 30004, 20004, 39201600, 16576, 0.10000000149011612, 0)
    Event_39202280(1, 39200260, 30000, 20000, 39201601, 16572, 0.10000000149011612, 0)
    Event_39202280(2, 39200269, 30000, 20000, 39201602, 16572, 0.10000000149011612, 0)
    Event_39202280(4, 39200264, 30000, 20000, 39201604, 16572, 0.10000000149011612, 0)
    Event_39202260(0, character=39200259, region=39202260)
    Event_39202260(1, character=39200260, region=39202260)
    Event_39202260(2, character=39200269, region=39202260)
    Event_39202230(0, 39200244, 30002, 20002, 16574, 0.0, 0, 0, 0, 0, 39201605, 0, 0, 0, 39200244)
    Event_39202240(0, 39200244, 30005, 20005, 39200244, 3.0, 0.0, 0, 1, 0, 0)
    RunCommonEvent(0, 90005250, args=(39200203, 39202203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200204, 39202203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200213, 39202203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200205, 39202214, 0.0, -1), arg_types="IIfi")
    Event_39202200()
    RunCommonEvent(0, 90005250, args=(39200206, 39202356, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200216, 39202356, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200300, 39202301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200301, 39202301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200303, 39202301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200304, 39202301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200307, 39202350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200308, 39202350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200309, 39202350, 0.0, -1), arg_types="IIfi")
    Event_39202302()
    Event_39202351()
    Event_39202318()
    RunCommonEvent(0, 90005250, args=(39200350, 39202350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200360, 39202360, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(39200364, 39202360, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005460, args=(39200380,))
    RunCommonEvent(0, 90005461, args=(39200380,))
    RunCommonEvent(0, 90005462, args=(39200380,))
    RunCommonEvent(0, 90005300, args=(39200290, 39200290, 40290, 0.0, 0), arg_types="IIifi")


@RestartOnRest(39202145)
def Event_39202145():
    """Event 39202145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=50,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(39200701)
    SetTeamType(39200701, TeamType.Human)
    EnableFlag(39202104)
    DeleteObjectVFX(39201702)
    CreateObjectVFX(39201702, vfx_id=200, model_point=806700)
    DeleteObjectVFX(39201701)
    CreateObjectVFX(39201701, vfx_id=200, model_point=806700)


@NeverRestart(39202500)
def Event_39202500():
    """Event 39202500"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            39200510,
            39201510,
            0,
            39201510,
            39201511,
            39203511,
            39201512,
            39203512,
            39202511,
            39202512,
            39200511,
            39202512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            39200515,
            39201515,
            0,
            39201515,
            39201516,
            39203516,
            39201517,
            39203517,
            39202516,
            39202517,
            39200516,
            39202517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            39200520,
            39201520,
            0,
            39201520,
            39201521,
            39203521,
            39201522,
            39203522,
            39202521,
            39202522,
            39200521,
            39202522,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            39200525,
            39201525,
            1,
            39201525,
            39201526,
            39203526,
            39201527,
            39203527,
            39202526,
            39202527,
            39200526,
            39202527,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(39202580)
def Event_39202580():
    """Event 39202580"""
    RegisterLadder(start_climbing_flag=39200530, stop_climbing_flag=39200531, obj=3901530)
    RegisterLadder(start_climbing_flag=39200532, stop_climbing_flag=39200533, obj=3901532)
    RegisterLadder(start_climbing_flag=39200534, stop_climbing_flag=39200535, obj=3901534)
    RegisterLadder(start_climbing_flag=39200536, stop_climbing_flag=39200537, obj=3901536)
    RegisterLadder(start_climbing_flag=39200538, stop_climbing_flag=39200539, obj=3901538)
    RegisterLadder(start_climbing_flag=39200540, stop_climbing_flag=39200541, obj=3901540)


@RestartOnRest(39202670)
def Event_39202670():
    """Event 39202670"""
    DisableObject(39201670)
    DisableObject(39201671)


@RestartOnRest(39202200)
def Event_39202200():
    """Event 39202200"""
    EndIfThisEventSlotFlagEnabled()
    GotoIfUnknown_1004_05(Label.L0, character=39200207, unk_8_12=True)
    GotoIfUnknown_1004_05(Label.L0, character=39200208, unk_8_12=True)
    DisableAI(39200207)
    DisableAI(39200208)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=39202207)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=39200207, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=39200207, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200207, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200207, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200207, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200207, unk_8_12=260, unk_12_16=1)
    IfAttackedWithDamageType(OR_2, attacked_entity=39200208, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=39200208, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200208, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200208, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200208, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=39200208, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=39200207, unk_4_8=1)
    Unknown_2004_83(character=39200208, unk_4_8=1)
    IfCharacterInsideRegion(AND_5, character=PLAYER, region=39202356)
    GotoIfConditionTrue(Label.L10, input_condition=AND_5)
    EnableAI(39200207)
    EnableAI(39200208)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(39200207)
    EnableAI(39200208)
    ChangePatrolBehavior(39200207, patrol_information_id=39203207)
    ChangePatrolBehavior(39200208, patrol_information_id=39203208)
    End()


@RestartOnRest(39202280)
def Event_39202280(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    obj: uint,
    special_effect_id: int,
    seconds: float,
    left: uint,
):
    """Event 39202280"""
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
    IfObjectDestroyed(OR_10, obj)
    IfConditionTrue(AND_1, input_condition=OR_10)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
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
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(39202220)
def Event_39202220(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
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
    """Event 39202220"""
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
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
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
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(39202230)
def Event_39202230(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
    flag: uint,
):
    """Event 39202230"""
    EndIfFlagEnabled(flag)
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
    EnableFlag(flag)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(39202240)
def Event_39202240(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    flag: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 39202240"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    EndIfFlagDisabled(flag)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
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


@RestartOnRest(39202260)
def Event_39202260(_, character: uint, region: uint):
    """Event 39202260"""
    EndIfThisEventSlotFlagEnabled()
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterBackreadEnabled(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.EveryTwoFrames)


@RestartOnRest(39202302)
def Event_39202302():
    """Event 39202302"""
    IfCharacterDead(OR_15, 39200302)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=39202301)
    AddSpecialEffect(39200302, 8080)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(39202306)
def Event_39202306():
    """Event 39202306"""
    IfCharacterDead(OR_15, 39200306)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfAttackedWithDamageType(AND_1, attacked_entity=39202306, attacker=PLAYER)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=39202306)
    IfConditionTrue(MAIN, input_condition=OR_1)
    AddSpecialEffect(39200306, 8080)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_1)
    ForceAnimation(39200306, 3000, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(39202318)
def Event_39202318():
    """Event 39202318"""
    IfCharacterDead(OR_15, 39200318)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=39202318)
    AddSpecialEffect(39200318, 8080)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(39202351)
def Event_39202351():
    """Event 39202351"""
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(39200307, 8033)
    AddSpecialEffect(39200307, 8081)
    AddSpecialEffect(39200308, 8033)
    AddSpecialEffect(39200308, 8081)
    AddSpecialEffect(39200309, 8033)
    AddSpecialEffect(39200309, 8081)
    AddSpecialEffect(39200310, 8033)
    AddSpecialEffect(39200310, 8081)
    AddSpecialEffect(39200311, 8033)
    AddSpecialEffect(39200311, 8081)
    AddSpecialEffect(39200312, 8033)
    AddSpecialEffect(39200312, 8081)
    IfAttackedWithDamageType(OR_1, attacked_entity=39200308, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=39200309, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=39200311, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=39200312, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=39200350, attacker=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=39202350)
    IfHasAIStatus(AND_1, 39200350, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CancelSpecialEffect(39200307, 8033)
    CancelSpecialEffect(39200307, 8081)
    CancelSpecialEffect(39200308, 8033)
    CancelSpecialEffect(39200308, 8081)
    CancelSpecialEffect(39200309, 8033)
    CancelSpecialEffect(39200309, 8081)
    CancelSpecialEffect(39200310, 8033)
    CancelSpecialEffect(39200310, 8081)
    CancelSpecialEffect(39200311, 8033)
    CancelSpecialEffect(39200311, 8081)
    CancelSpecialEffect(39200312, 8033)
    CancelSpecialEffect(39200312, 8081)
    AddSpecialEffect(39200307, 8080)
    AddSpecialEffect(39200308, 8080)
    AddSpecialEffect(39200309, 8080)
    AddSpecialEffect(39200310, 8080)
    AddSpecialEffect(39200311, 8080)
    AddSpecialEffect(39200312, 8080)
    AddSpecialEffect(39200350, 8080)
    ChangePatrolBehavior(39200307, patrol_information_id=39203307)
    ChangePatrolBehavior(39200310, patrol_information_id=39203310)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(39202800)
def Event_39202800():
    """Event 39202800"""
    EndIfFlagEnabled(39200800)
    IfHealthValueLessThanOrEqual(MAIN, 39200800, value=0)
    Wait(4.0)
    PlaySoundEffect(39200800, 888880000, sound_type=SoundType.s_SFX)
    IfHealthValueEqual(MAIN, 39200800, value=0)
    KillBossAndDisplayBanner(character=39200800, banner_type=BannerType.Unknown)
    EnableFlag(39200800)
    EnableFlag(9126)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61126)


@RestartOnRest(39202810)
def Event_39202810():
    """Event 39202810"""
    GotoIfFlagDisabled(Label.L0, flag=39200800)
    DisableCharacter(39200800)
    DisableAnimations(39200800)
    Kill(39200800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(39200800)
    GotoIfFlagEnabled(Label.L1, flag=39200801)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=39202801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=39200800, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_1, character=39200800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=39200800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=39200800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=39200800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=39200800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(39200801)
    DisableHealthBar(39200800)
    EnableAI(39200800)
    ForceAnimation(39200800, 3004, unknown2=1.0)
    Wait(8.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 39202805)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(39200800)
    SetNetworkUpdateRate(39200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableHealthBar(39200800)
    EnableBossHealthBar(39200800, name=904910000)


@RestartOnRest(39202829)
def Event_39202829():
    """Event 39202829"""
    RunCommonEvent(
        0,
        9005800,
        args=(39200800, 39201800, 39202800, 39202805, 39200800, 10000, 0, 39202801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(39200800, 39201800, 39202800, 39202805, 39202806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(39200800, 39201800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(39200800, 39201801, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(39200800, 920900, 39202805, 39202806, 0, 39202802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(39203700)
def Event_39203700():
    """Event 39203700"""
    EndIfFlagDisabled(39200800)
    EndIfFlagDisabled(400180)
    EnableFlag(39209200)
    End()


@RestartOnRest(39203701)
def Event_39203701():
    """Event 39203701"""
    EndIfFlagEnabled(39209201)
    EndIfFlagDisabled(400180)
    IfFlagEnabled(MAIN, 39202141)
    EnableFlag(39209201)
    End()


@RestartOnRest(39203710)
def Event_39203710():
    """Event 39203710"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(4181, 4183))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1042559206)
    End()


@RestartOnRest(39203720)
def Event_39203720():
    """Event 39203720"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(39209250)
    EndIfFlagEnabled(39200800)
    EndIfFlagDisabled(4140)
    EndIfFlagEnabled(4147)
    EndIfFlagEnabled(1044529259)
    EndIfFlagDisabled(1036439210)
    EnableFlag(39209250)
    End()
