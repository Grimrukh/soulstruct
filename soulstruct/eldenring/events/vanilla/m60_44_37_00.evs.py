"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044370000, obj=1044371950, unknown=5.0)
    Event_1044372210(0, character=1044370211, obj=1044371211, region=1044372210)
    Event_1044372210(1, character=1044370212, obj=1044371212, region=1044372210)
    Event_1044372210(2, character=1044370213, obj=1044371213, region=1044372210)
    Event_1044372210(3, character=1044370214, obj=1044371214, region=1044372210)
    RunCommonEvent(0, 90005706, args=(1044370700, 930023, 0), arg_types="IiI")
    Event_1044373715(0, character=1044370705)
    Event_1044373716()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044370700)
    DisableBackread(1044370705)
    Event_1044375220()
    RunCommonEvent(0, 90005251, args=(1044370203, 106.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1044370262, 30001, 20001, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(1044370200, 1044372200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1044370200, 30014, 20014, 1044372200, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1044370201, 1044372200, 10.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1044370201, 30014, 20014, 1044372200, 10.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1044370350, 1044372350, 15.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(1044372210)
def Event_1044372210(_, character: uint, obj: uint, region: uint):
    """Event 1044372210"""
    EnableObject(obj)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    IfCharacterDead(AND_10, character)
    SkipLinesIfConditionFalse(2, AND_10)
    DisableObject(obj)
    End()
    EnableObject(obj)
    DisableCharacter(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
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
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableObject(obj)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1044375220)
def Event_1044375220():
    """Event 1044375220"""
    DropMandatoryTreasure(1044375220)


@RestartOnRest(1044372650)
def Event_1044372650(_, tutorial_param_id: int, flag: uint):
    """Event 1044372650"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerHasGood(AND_1, 130)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)


@RestartOnRest(1044373700)
def Event_1044373700(
    _,
    character__obj: uint,
    character__obj_1: uint,
    character__obj_2: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044373700"""
    WaitFrames(frames=1)
    DisableFlag(flag)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character__obj)
    EnableCharacter(character__obj_1)
    EnableObject(character__obj_2)
    EnableBackread(character__obj)
    EnableBackread(character__obj_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableCharacter(character__obj)
    DisableCharacter(character__obj_1)
    DisableObject(character__obj_2)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L2, flag=flag_2)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character__obj)
    DropMandatoryTreasure(character__obj_1)
    DisableCharacter(character__obj)
    DisableCharacter(character__obj_1)
    DisableObject(character__obj)
    DisableObject(character__obj_1)
    DisableObject(character__obj_2)
    DisableBackread(character__obj)
    DisableBackread(character__obj_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, flag)
    Restart()


@RestartOnRest(1044373701)
def Event_1044373701(_, flag: uint, flag_1: uint, flag_2: uint, first_flag: uint, last_flag: uint):
    """Event 1044373701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(flag)
    SkipLinesIfFlagEnabled(4, flag_1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(first_flag)
    End()
    EndIfFlagEnabled(flag_2)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_2)


@RestartOnRest(1044373702)
def Event_1044373702(_, character: uint, flag: uint, first_flag: uint, flag_1: uint, last_flag: uint, flag_2: uint):
    """Event 1044373702"""
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, first_flag)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)


@RestartOnRest(1044373710)
def Event_1044373710(_, character: uint):
    """Event 1044373710"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30021, unknown2=1.0)
    DisableGravity(character)


@RestartOnRest(1044373715)
def Event_1044373715(_, character: uint):
    """Event 1044373715"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(1044373716)
def Event_1044373716():
    """Event 1044373716"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3503)
    IfFlagEnabled(AND_1, 3506)
    IfFlagDisabled(AND_1, 1044379256)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1044372700)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1044379255)
    End()
