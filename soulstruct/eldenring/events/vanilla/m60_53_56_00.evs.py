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
    Event_1053562200(0, character=1053565200)
    Event_1053562250(0, 1053560250, 1053561250, 1053560270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1053562250(1, 1053560251, 1053561251, 1053560271, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1053562250(2, 1053560252, 1053561252, 1053560272, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1053562260(
        0,
        1053560250,
        1053561250,
        1053560270,
        1053565250,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1053560700,
        1053562250,
    )
    Event_1053562260(
        1,
        1053560251,
        1053561251,
        1053560271,
        1053565251,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1053560710,
        1053562251,
    )
    Event_1053562260(
        2,
        1053560252,
        1053561252,
        1053560272,
        1053565252,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1053560720,
        1053562252,
    )
    Event_1053562270(0, 1053560250, 0.0, 1053560270, 0.0, 1053560251, 30010, 20010, 45.0, 0.0, 0.0, 1053562250)
    Event_1053562270(1, 1053560250, 0.0, 1053560270, 0.0, 1053560260, 30010, 20010, 45.0, 0.0, 0.0, 1053562250)
    Event_1053562270(3, 1053560251, 0.0, 1053560271, 0.0, 1053560253, 30010, 20010, 35.0, 0.0, 0.0, 1053562251)
    Event_1053562270(4, 1053560251, 0.0, 1053560271, 0.0, 1053560261, 30010, 20010, 35.0, 0.0, 0.0, 1053562251)
    Event_1053562270(5, 1053560251, 0.0, 1053560271, 0.0, 1053560262, 30010, 20010, 35.0, 0.0, 0.0, 1053562251)
    RunCommonEvent(
        0,
        90005880,
        args=(1053560800, 1053560805, 1053562800, 1053560800, 30515, 60, 53, 56, 0, 1053562805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1053560800, 1053560805, 1053562801, 1053562802, 20300, 1053561805, 60, 53, 56, 0, 1053562805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1053560800,
            1053560805,
            1053562800,
            1053560800,
            1053562806,
            1053565810,
            1053561800,
            1053560810,
            1053562810,
            130401,
            -1,
            90005,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1053560800, 1053560805, 1053561805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1053560800, 921100, 1053562806, 1053562807, 0, 1), arg_types="IiIIii")
    Event_1053562820(0, flag=1053560800, flag_1=1053560805)
    RunCommonEvent(
        0,
        90005620,
        args=(1053560570, 1053561570, 1053561571, 1053561572, 1053562570, 1053562571, 1053562572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1053560570, 1053561573), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1053560700)


@RestartOnRest(1053562200)
def Event_1053562200(_, character: uint):
    """Event 1053562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1053562250)
def Event_1053562250(
    _,
    flag: uint,
    destination: uint,
    character: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    seconds_5: float,
    seconds_6: float,
):
    """Event 1053562250"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(AND_1, attacked_entity=character, attacker=20000)
    EndIfConditionTrue(input_condition=AND_1)
    ForceAnimation(destination, 0, unknown2=1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=220, short_move=True)
    Wait(5.400000095367432)
    Restart()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)
    Wait(seconds_5)
    Wait(seconds_6)


@RestartOnRest(1053562260)
def Event_1053562260(
    _,
    flag: uint,
    obj: uint,
    character: uint,
    character_1: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    item_lot_param_id: int,
    flag_1: uint,
):
    """Event 1053562260"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableObject(obj)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=200, model_point=803160)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    ForceAnimation(obj, 1, unknown2=1.0)
    DeleteObjectVFX(obj)
    Wait(1.0)
    DisableObject(obj)
    SkipLinesIfPlayerNotInOwnWorld(2)
    Wait(0.30000001192092896)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)


@RestartOnRest(1053562270)
def Event_1053562270(
    _,
    flag: uint,
    seconds: float,
    attacked_entity: uint,
    seconds_1: float,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds_2: float,
    seconds_3: float,
    flag_1: uint,
):
    """Event 1053562270"""
    EndIfFlagEnabled(flag)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    ForceAnimation(character, animation_id, unknown2=1.0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_2, entity=character, other_entity=20000, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag_1)
    Unknown_2004_83(character=character, unk_4_8=1)
    Wait(seconds_2)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_3)


@RestartOnRest(1053562820)
def Event_1053562820(_, flag: uint, flag_1: uint):
    """Event 1053562820"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=5)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=1)
