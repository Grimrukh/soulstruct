"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1042392200(0, character=1042390200, region=1042392200, owner_entity=1042390210, flag=1042392200)
    Event_1042392200(1, character=1042390201, region=1042392200, owner_entity=1042390210, flag=1042392200)
    Event_1042392200(2, character=1042390202, region=1042392200, owner_entity=1042390210, flag=1042392200)
    Event_1042392200(3, character=1042390203, region=1042392200, owner_entity=1042390210, flag=1042392200)
    Event_1042392200(4, character=1042390204, region=1042392200, owner_entity=1042390210, flag=1042392200)
    Event_1042392200(5, character=1042390240, region=1042392240, owner_entity=1042390210, flag=1042392240)
    Event_1042392200(6, character=1042390241, region=1042392240, owner_entity=1042390210, flag=1042392240)
    Event_1042392200(7, character=1042390242, region=1042392240, owner_entity=1042390210, flag=1042392240)
    Event_1042392200(8, character=1042390249, region=1042392249, owner_entity=1042390210, flag=1042392249)
    Event_1042392200(9, character=1042390250, region=1042392249, owner_entity=1042390210, flag=1042392249)
    Event_1042392200(10, character=1042390251, region=1042392249, owner_entity=1042390210, flag=1042392249)
    Event_1042392200(11, character=1042390252, region=1042392249, owner_entity=1042390210, flag=1042392249)
    RunCommonEvent(0, 90005300, args=(1042390310, 1042390310, 40146, 0.0, 0), arg_types="IIifi")
    Event_1042392600(0, attacked_entity=1042391600, region=1042392600)
    Event_1042392600(1, attacked_entity=1042391601, region=1042392601)
    Event_1042392600(2, attacked_entity=1042391602, region=1042392602)
    Event_1042392600(3, attacked_entity=1042391603, region=1042392603)
    Event_1042392600(4, attacked_entity=1042391604, region=1042392604)
    Event_1042392600(5, attacked_entity=1042391605, region=1042392605)
    Event_1042392600(6, attacked_entity=1042391606, region=1042392606)
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1042390180, 1042392181, 1042392182, 1042390710, 22, 1042392180, 1042392181, 0.0, 1042399250, 1, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1042390180, 1042392181, 1042392182, 1042390710), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1042390180, 1042392181, 1042392182, 1042390710, 1042390700, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1042390180, 1042392181, 1042392182, 1042390710, 1042392180, 0, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005795,
        args=(7602, 0, 1042399300, 1042392141, 1042392142, 80602, 9000, 1042391701, 30010),
        arg_types="IIIIIiiIi",
    )
    SkipOrGotoIfUnknown_206(label_or_goto=2, unk_4_8=20)
    RunCommonEvent(0, 90005796, args=(7602, 1042390700, 5, 1042392141), arg_types="IIBI")
    Event_1042392145()
    Event_1042393700()
    Event_1042393710()
    RunCommonEvent(0, 90005774, args=(7602, 1042390500, 1042397500), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042390700)
    DisableBackread(1042390180)


@RestartOnRest(1042392145)
def Event_1042392145():
    """Event 1042392145"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EnableBackread(1042390700)
    SetTeamType(1042390700, TeamType.Human)
    DeleteObjectVFX(1042391700)
    CreateObjectVFX(1042391700, vfx_id=200, model_point=806700)


@RestartOnRest(1042392200)
def Event_1042392200(_, character: uint, region: uint, owner_entity: uint, flag: uint):
    """Event 1042392200"""
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=PLAYER)
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
    EnableFlag(flag)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    IfCharacterHollow(OR_7, PLAYER)
    IfCharacterWhitePhantom(OR_7, PLAYER)
    IfCharacterOutsideRegion(AND_11, character=PLAYER, region=region)
    IfConditionTrue(AND_11, input_condition=OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    EnableCharacter(character)
    ForceAnimation(character, 20011, unknown2=1.0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    CancelSpecialEffect(character, 8090)


@RestartOnRest(1042392300)
def Event_1042392300():
    """Event 1042392300"""
    EndIfFlagEnabled(1042399710)
    EndIfFlagEnabled(1042399700)
    EndIfTryingToCreateSession()
    DisableCharacter(1042390700)
    CreateObjectVFX(1042391701, vfx_id=100, model_point=30010)
    IfFlagDisabled(AND_1, 1042399700)
    IfActionButtonParamActivated(AND_1, action_button_id=9000, entity=1042391701)
    IfLeavingSession(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(1042391701)
    Wait(1.0)
    AddSpecialEffect(PLAYER, 15)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(1042392301)
def Event_1042392301():
    """Event 1042392301"""
    EndIfFlagEnabled(1042399710)
    EndIfFlagDisabled(1042399700)
    EnableCharacter(1042390700)
    UnknownMap_11(unk_0_4=0, unk_4_8=0.0)
    SetTeamType(1042390700, TeamType.Enemy)
    DisableFlag(1042399700)
    IfCharacterDead(AND_1, 1042390700)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042399710)
    UnknownMap_12(unk_0_4=10.0)
    DisplayBanner(BannerType.Unknown)
    Unknown_2003_77(entity_id=1042392721)
    Unknown_2003_74(unk_0_4=1)


@RestartOnRest(1042392302)
def Event_1042392302():
    """Event 1042392302"""
    GotoIfFlagEnabled(Label.L1, flag=1042399710)
    GotoIfFlagDisabled(Label.L0, flag=1042399700)
    EnableObject(1042391700)
    CreateObjectVFX(1042391700, vfx_id=200, model_point=806700)
    DeleteObjectVFX(1042391701)
    IfCharacterDead(AND_1, 1042390700)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteObjectVFX(1042391701)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1042391700)


@RestartOnRest(1042392600)
def Event_1042392600(_, attacked_entity: uint, region: uint):
    """Event 1042392600"""
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


@RestartOnRest(1042393700)
def Event_1042393700():
    """Event 1042393700"""
    WaitFrames(frames=1)
    EnableFlag(1042399250)
    EndIfFlagDisabled(16009208)
    DisableFlag(1042399250)
    End()


@RestartOnRest(1042393710)
def Event_1042393710():
    """Event 1042393710"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(400073)
    EnableFlag(1042399300)
    End()
