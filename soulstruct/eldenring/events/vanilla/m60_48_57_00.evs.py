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
    RunCommonEvent(0, 90005600, args=(1048570000, 1048571950, 5.0, 1048570480), arg_types="IIfI")
    RunCommonEvent(
        0,
        90005211,
        args=(1048570275, 30000, 20000, 1048572277, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1048570277, 30000, 20000, 1048572277, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1048570285, 30000, 20000, 1048572285, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005300, args=(1048570200, 1048570200, 40526, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1048570250, 1048570250, 1048570900, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1048570251, 1048570251, 1048570910, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1048570252, 1048570252, 1048570920, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1048570253, 1048570253, 1048570930, 0.0, 0), arg_types="IIifi")
    Event_1048572820(0, 1048570800, 30000, 20000, 1048572800, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005870, args=(1048570800, 904980607, 24), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1048570800, 0, 1048570800, 0, 1048570700, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005605,
        args=(1048571500, 15, 0, 0, 0, 15002600, 0, 1048572501, 1048572502, 1048572503, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_1048572300(
        0,
        anchor_entity=1048571300,
        obj=1048576300,
        obj_1=1048576301,
        character=1048575300,
        character_1=1048575301,
        region=1048572300
    )
    Event_1048572310()
    Event_1048572320(0, entity=1048571300)
    Event_1048572350()
    Event_1048572355()
    Event_1048572390()
    Event_1048572340(0, character=1048575310)
    Event_1048572370(0, obj=1048571370, obj_1=1048571360, flag=1048570370)
    Event_1048572370(1, obj=1048571371, obj_1=1048571361, flag=1048570371)
    Event_1048572370(2, obj=1048571372, obj_1=1048571362, flag=1048570372)
    Event_1048572370(3, obj=1048571373, obj_1=1048571363, flag=1048570373)
    RunCommonEvent(0, 90005261, args=(1048570250, 1048572250, 5.0, 0.0, -1), arg_types="IIffi")
    Event_1048572256()
    Event_1048572260()
    Event_1048572270()
    Event_1048572275(0, character=1048570255)
    Event_1048572580()
    Event_1048572400()


@RestartOnRest(1048572256)
def Event_1048572256():
    """Event 1048572256"""
    ForceAnimation(1048570256, 30001, loop=True, unknown2=1.0)


@RestartOnRest(1048572260)
def Event_1048572260():
    """Event 1048572260"""
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(AND_1, 20000, 416)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, 14508)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572270)
def Event_1048572270():
    """Event 1048572270"""
    IfCharacterHasSpecialEffect(AND_1, 1048570255, 14507)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(1048570254, 14507)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572275)
def Event_1048572275(_, character: uint):
    """Event 1048572275"""
    EnableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1048572300)
def Event_1048572300(_, anchor_entity: uint, obj: uint, obj_1: uint, character: uint, character_1: uint, region: uint):
    """Event 1048572300"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L5, flag=1048572308)
    GotoIfFlagEnabled(Label.L6, flag=1048572309)
    UnknownMap_12(unk_0_4=0.0)
    DisableObject(obj)
    EnableObject(obj_1)
    EnableCharacter(character)
    DisableInvincibility(character)
    DisableCharacter(character_1)
    EnableInvincibility(character_1)
    CancelSpecialEffect(PLAYER, 190)
    EnableTreasure(obj=1048571256)
    EnableFlag(1048572308)
    DisableFlag(1048572309)
    EnableFlag(1048572305)
    EnableFlag(1048572308)
    DisableFlag(1048572309)
    Wait(1.0)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EndIfFlagEnabled(1048572309)
    UnknownMap_12(unk_0_4=0.0)
    DisableObject(obj)
    EnableObject(obj_1)
    EnableCharacter(character)
    DisableInvincibility(character)
    DisableCharacter(character_1)
    EnableInvincibility(character_1)
    CancelSpecialEffect(PLAYER, 190)
    EnableTreasure(obj=1048571256)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    UnknownMap_11(unk_0_4=0, unk_4_8=0.0)
    EnableObject(obj)
    DisableObject(obj_1)
    DisableCharacter(character)
    EnableInvincibility(character)
    EnableCharacter(character_1)
    DisableInvincibility(character_1)
    AddSpecialEffect(PLAYER, 190)
    DisableTreasure(obj=1048571256)
    DeleteObjectVFX(1048571950)
    AddSpecialEffect(PLAYER, 514)

    # --- Label 7 --- #
    DefineLabel(7)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1048572309)
    EndIfFlagEnabled(1048570350)
    AwaitFlagEnabled(flag=1048570310)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfLeavingSession(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9527, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=30021,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=1048572306,
        right_flag=1048572307,
        cancel_flag=0,
    )
    GotoIfFlagEnabled(Label.L2, flag=1048572306)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfTryingToCreateSession(OR_3)
    IfTryingToJoinSession(OR_3)
    RestartIfConditionTrue(input_condition=OR_3)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60450, unknown2=1.0)
    Wait(1.0)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=region,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=0,
        unknown4=1,
    )
    Wait(1.0)
    ForceAnimation(PLAYER, 60451, skip_transition=True, unknown2=1.0)
    EnableFlag(1048572305)
    UnknownMap_11(unk_0_4=0, unk_4_8=1.5)
    ShootProjectile(
        owner_entity=1048570310,
        source_entity=1048572310,
        model_point=100,
        behavior_id=100930,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    EnableObject(obj)
    DisableObject(obj_1)
    DisableCharacter(character)
    DisableCharacter(1248550350)
    DisableCharacter(1248550351)
    DisableCharacter(1248550360)
    DisableCharacter(1248550361)
    EnableInvincibility(character)
    EnableInvincibility(1248550350)
    EnableInvincibility(1248550351)
    EnableInvincibility(1248550360)
    EnableInvincibility(1248550361)
    EnableCharacter(character_1)
    DisableInvincibility(character_1)
    AddSpecialEffect(PLAYER, 190)
    DisableTreasure(obj=1048571256)
    DeleteObjectVFX(1048571950)
    AddSpecialEffect(PLAYER, 514)
    DisableFlag(1048572308)
    EnableFlag(1048572309)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(1048572306)
    DisableFlag(1048572307)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572310)
def Event_1048572310():
    """Event 1048572310"""
    DisableNetworkSync()
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9210, entity=1048571310)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=60100, anchor_entity=1048571310)
    Wait(1.0)
    EnableNetworkFlag(1048570310)
    Restart()


@RestartOnRest(1048572320)
def Event_1048572320(_, entity: uint):
    """Event 1048572320"""
    ForceAnimation(entity, 0, loop=True, unknown2=1.0)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1048570350)
    ForceAnimation(entity, 10, loop=True, unknown2=1.0)
    AwaitFlagEnabled(flag=1048570310)
    EndIfFlagEnabled(1048572309)
    IfLeavingSession(AND_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfFlagEnabled(AND_1, 1048570310)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    ForceAnimation(entity, 1, loop=True, unknown2=1.0)
    IfLeavingSession(AND_11)
    IfTryingToJoinSession(AND_12)
    IfConditionFalse(AND_11, input_condition=AND_12)
    IfConditionFalse(OR_1, input_condition=AND_11)
    IfFlagEnabled(OR_1, 1048572309)
    IfConditionTrue(MAIN, input_condition=OR_1)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1048572340)
def Event_1048572340(_, character: uint):
    """Event 1048572340"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1048572350)
def Event_1048572350():
    """Event 1048572350"""
    GotoIfFlagEnabled(Label.L0, flag=1048570350)
    DeleteObjectVFX(1048571350, erase_root=False)
    CreateObjectVFX(1048571350, vfx_id=200, model_point=1505)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1048570370)
    IfFlagEnabled(AND_1, 1048570371)
    IfFlagEnabled(AND_1, 1048570372)
    IfFlagEnabled(AND_1, 1048570373)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1048570350)
    Wait(2.299999952316284)
    DisplayDialog(text=30020, anchor_entity=0, display_distance=5.0)
    DisableObject(1048571350)
    DeleteObjectVFX(1048571350)
    PlaySoundEffect(1048571350, 1500, sound_type=SoundType.s_SFX)
    AddSpecialEffect(20000, 8870)
    Wait(4.5)
    WarpToMap(game_map=NORTHWEST_MOUNTAINTOPS_SW_NW, player_start=1048572301)
    End()
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1048571350)
    DeleteObjectVFX(1048571350)
    PlaySoundEffect(1048571350, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1048572355)
def Event_1048572355():
    """Event 1048572355"""
    GotoIfFlagEnabled(Label.L0, flag=1048570350)
    DeleteObjectVFX(1048571380, erase_root=False)
    DeleteObjectVFX(1048571381, erase_root=False)
    DeleteObjectVFX(1048571382, erase_root=False)
    DeleteObjectVFX(1048571383, erase_root=False)
    DeleteObjectVFX(1048571384, erase_root=False)
    DeleteObjectVFX(1048571385, erase_root=False)
    CreateObjectVFX(1048571380, vfx_id=200, model_point=1503)
    CreateObjectVFX(1048571381, vfx_id=200, model_point=1503)
    CreateObjectVFX(1048571382, vfx_id=200, model_point=1503)
    CreateObjectVFX(1048571383, vfx_id=200, model_point=1503)
    CreateObjectVFX(1048571384, vfx_id=200, model_point=1503)
    CreateObjectVFX(1048571385, vfx_id=200, model_point=1503)
    IfFlagEnabled(AND_1, 1048572309)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1048571380)
    DisableObject(1048571381)
    DisableObject(1048571382)
    DisableObject(1048571383)
    DisableObject(1048571384)
    DisableObject(1048571385)
    DeleteObjectVFX(1048571380, erase_root=False)
    DeleteObjectVFX(1048571381, erase_root=False)
    DeleteObjectVFX(1048571382, erase_root=False)
    DeleteObjectVFX(1048571383, erase_root=False)
    DeleteObjectVFX(1048571384, erase_root=False)
    DeleteObjectVFX(1048571385, erase_root=False)
    End()


@RestartOnRest(1048572370)
def Event_1048572370(_, obj: uint, obj_1: uint, flag: uint):
    """Event 1048572370"""
    DeleteObjectVFX(obj)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AwaitFlagEnabled(flag=1048572309)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9528, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60550, unknown2=1.0)
    EnableFlag(flag)
    Wait(1.2000000476837158)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj_1)
    CreateObjectVFX(obj_1, vfx_id=200, model_point=806061)
    AwaitFlagEnabled(flag=1048572309)
    CreateObjectVFX(obj, vfx_id=200, model_point=806060)
    End()
    GotoIfFlagEnabled(Label.L0, flag=1048572309)


@RestartOnRest(1048572390)
def Event_1048572390():
    """Event 1048572390"""
    DisableNetworkSync()
    EndIfFlagEnabled(1048570350)
    IfActionButtonParamActivated(OR_1, action_button_id=9529, entity=1048571350)
    IfFlagEnabled(OR_1, 1048570350)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1048570350)
    DisplayDialog(text=30023, anchor_entity=1048571350)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572400)
def Event_1048572400():
    """Event 1048572400"""
    DisableObject(1048576305)


@RestartOnRest(1048572580)
def Event_1048572580():
    """Event 1048572580"""
    RegisterLadder(start_climbing_flag=1048570580, stop_climbing_flag=1048570581, obj=1048571580)
    RegisterLadder(start_climbing_flag=1048570582, stop_climbing_flag=1048570583, obj=1048571582)
    RegisterLadder(start_climbing_flag=1048570584, stop_climbing_flag=1048570585, obj=1048571584)
    RegisterLadder(start_climbing_flag=1048570586, stop_climbing_flag=1048570587, obj=1048571586)
    RegisterLadder(start_climbing_flag=1048570588, stop_climbing_flag=1048570589, obj=1048571588)
    RegisterLadder(start_climbing_flag=1048570590, stop_climbing_flag=1048570591, obj=1048571590)
    RegisterLadder(start_climbing_flag=1048570592, stop_climbing_flag=1048570593, obj=1048571592)
    RegisterLadder(start_climbing_flag=1048570594, stop_climbing_flag=1048570595, obj=1048571594)
    RegisterLadder(start_climbing_flag=1048570596, stop_climbing_flag=1048570597, obj=1048571596)


@RestartOnRest(1048572820)
def Event_1048572820(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1048572820"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()
