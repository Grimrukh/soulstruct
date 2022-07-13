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
    Event_1051362580()
    RunCommonEvent(0, 9005810, args=(1051360800, 1051360000, 1051360950, 1051361950, 5.0), arg_types="IIIIf")
    RunCommonEvent(
        0,
        90005100,
        args=(76458, 76419, 1051361981, 77410, 4, 78410, 78411, 78412, 78413, 78414, 78415, 78416, 78417, 78418, 78419),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1051360001, obj=1051361951, unknown=10.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76458, 76420, 1051361980, 77410, 3, 78410, 78411, 78412, 78413, 78414, 78415, 78416, 78417, 78418, 78419),
        arg_types="IIIIIIIIIIIIIII",
    )
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004070, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004060, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004050, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004040, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004030, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004020, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004010, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005695, args=(1051362501, 1051361501, 200, 0, 802004000, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004070, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004060, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004050, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004040, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004030, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004020, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004010, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005695, args=(1051362503, 1051361503, 200, 0, 802004000, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    Event_1051362216(0, 1051362500, 1051361500, 200, 0, 802004000, 1.0, 0.0, 1.0, 50)
    Event_1051362216(1, 1051362500, 1051361500, 200, 0, 802004010, 1.0, 0.0, 1.0, 51)
    Event_1051362216(2, 1051362500, 1051361500, 200, 0, 802004020, 1.0, 0.0, 1.0, 52)
    Event_1051362216(3, 1051362500, 1051361500, 200, 0, 802004030, 1.0, 0.0, 1.0, 53)
    Event_1051362216(4, 1051362500, 1051361500, 200, 0, 802004040, 1.0, 0.0, 1.0, 54)
    Event_1051362216(5, 1051362500, 1051361500, 200, 0, 802004050, 1.0, 0.0, 1.0, 55)
    Event_1051362216(6, 1051362500, 1051361500, 200, 0, 802004060, 1.0, 0.0, 1.0, 56)
    Event_1051362216(7, 1051362500, 1051361500, 200, 0, 802004070, 1.0, 0.0, 1.0, 57)
    RunCommonEvent(0, 900005610, args=(1051361650, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1051361651, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1051361652, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1051361653, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1051361654, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1051361656, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1051361657, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005605,
        args=(1051361600, 60, 50, 36, 0, 1050360600, 0, 1051362650, 1051362651, 1051362652, 9410, 30040, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_1051362800()
    Event_1051362810()
    Event_1051362849()
    Event_1051362630(0, obj=1051361630)
    Event_1051362630(1, obj=1051361631)
    Event_1051362630(2, obj=1051361632)
    Event_1051362630(3, obj=1051361633)
    Event_1051362210()
    Event_1051362215()
    Event_1051362200()
    Event_1051362220()
    Event_1051362230()
    RunCommonEvent(0, 90005261, args=(1051360200, 1051362200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1051360210, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1051360211, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1051360291, 1051360291, 1051360700, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1051360292, 1051360292, 1051360800, 0.0, 0), arg_types="IIifi")
    Event_1051362340(0, character=1051360340)
    RunCommonEvent(0, 90005250, args=(1051360422, 1051362422, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051360474, 1051362422, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051360475, 1051362422, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051360476, 1051362422, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051360490, 1051362490, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005501,
        args=(1051360510, 1051360511, 0, 1051361510, 1051361511, 1051361512, 1051360512),
        arg_types="IIIIIII",
    )
    Event_1051362510()
    RunCommonEvent(0, 90005490, args=(1051360400, 1051360401, 1051361400, 0, 0, 1051362400, 1), arg_types="IIIIIII")
    RunCommonEvent(0, 90005490, args=(1051360402, 1051360403, 1051361402, 0, 0, 1051362402, 1), arg_types="IIIIIII")
    RunCommonEvent(0, 90005511, args=(1051360560, 1051361560, 1051363560, 99020, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1051360560, 1051362560, 1051362561), arg_types="III")
    RunCommonEvent(0, 1051362560, args=(1051361562,))
    RunCommonEvent(1, 1051362560, args=(1051361564,))
    RunCommonEvent(2, 1051362560, args=(1051361566,))
    RunCommonEvent(3, 1051362560, args=(1051361568,))
    Event_1051363710(0, character=1051360705)
    Event_1051363711()
    Event_1051360720(0, character=1051360720)
    Event_1051360721()
    Event_1051363725(0, character__obj=1051360700)
    Event_1051363726(0, character__obj=1051360701)
    Event_1051363727()
    RunCommonEvent(0, 90005708, args=(1051360700, 3360, 1051362700), arg_types="III")
    Event_1051360730(0, character=1051360715, animation_id=0, left=1)
    Event_1051360730(1, character=1051360730, animation_id=90100, left=1)
    Event_1051360730(2, character=1051360735, animation_id=90101, left=0)
    Event_1051360734(0, character=1051360735)
    Event_1051360735(0, character=1051360725, animation_id=0, left=1)
    Event_1051362500()
    Event_1051362490(0, 1051362710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1051360700)
    DisableBackread(1051360701)
    DisableBackread(1051360702)
    DisableBackread(1051360705)
    DisableBackread(1051360715)
    DisableBackread(1051360720)
    DisableBackread(1051360725)
    DisableBackread(1051360730)
    DisableBackread(1051360735)
    EnableObjectInvulnerability(1051361700)
    Event_1051362519()


@RestartOnRest(1051362200)
def Event_1051362200():
    """Event 1051362200"""
    SkipLinesIfFlagDisabled(4, 9413)
    EnableCharacter(1051365200)
    EnableObject(1051361400)
    EnableObject(1051361402)
    End()
    EndIfFlagDisabled(9410)
    IfFlagEnabled(MAIN, 9410)
    DisableCharacter(1051365200)
    DisableObject(1051361400)
    DisableObject(1051361402)


@RestartOnRest(1051362210)
def Event_1051362210():
    """Event 1051362210"""
    IfFlagDisabled(OR_1, 9410)
    IfFlagEnabled(OR_1, 9413)
    EndIfConditionTrue(input_condition=OR_1)
    DisableObject(1051361800)
    DisableObject(1051361801)


@RestartOnRest(1051362215)
def Event_1051362215():
    """Event 1051362215"""
    IfFlagEnabled(AND_1, 9410)
    IfFlagDisabled(AND_1, 9413)
    EndIfConditionTrue(input_condition=AND_1)
    DisableObject(1051361500)


@RestartOnRest(1051362216)
def Event_1051362216(
    _,
    obj__obj_flag: uint,
    obj: uint,
    model_point__model_point_start: int,
    model_point_end: int,
    behavior_param_id__behaviour_id: int,
    radius: float,
    life: float,
    repetition_time: float,
    flag: uint,
):
    """Event 1051362216"""
    EndIfFlagDisabled(flag)
    RemoveObjectFlag(obj_flag=obj__obj_flag)
    IfFlagDisabled(OR_1, 9410)
    IfFlagEnabled(OR_1, 9413)
    EndIfConditionTrue(input_condition=OR_1)
    EndIfObjectDestroyed(obj)
    SkipLinesIfValueNotEqual(2, left=0, right=model_point_end)
    CreateHazard(
        obj_flag=obj__obj_flag,
        obj=obj,
        model_point=model_point__model_point_start,
        behavior_param_id=behavior_param_id__behaviour_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )
    SkipLines(1)
    CreateBigHazardousObject(
        obj_flag=obj__obj_flag,
        obj=obj,
        model_point_start=model_point__model_point_start,
        model_point_end=model_point_end,
        behaviour_id=behavior_param_id__behaviour_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )
    IfObjectDestroyed(MAIN, obj__obj_flag)
    RemoveObjectFlag(obj_flag=obj__obj_flag)


@RestartOnRest(1051362220)
def Event_1051362220():
    """Event 1051362220"""
    DisableObject(1051361690)
    DeleteObjectVFX(1051361690)
    EndOfAnimation(obj=1051361520, animation_id=0)
    IfFlagEnabled(AND_9, 1051360230)
    GotoIfConditionTrue(Label.L2, input_condition=AND_9)
    IfFlagEnabled(OR_9, 9412)
    IfFlagEnabled(OR_9, 9413)
    IfFlagEnabled(OR_9, 1252380800)
    EndIfConditionTrue(input_condition=OR_9)
    GotoIfFlagEnabled(Label.L1, flag=9411)
    IfFlagEnabled(MAIN, 9411)
    EnableFlag(9021)
    PlayCutscene(60510000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFramesAfterCutscene(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=1051361520, animation_id=2)
    EnableObject(1051361690)
    CreateObjectVFX(1051361690, vfx_id=101, model_point=5)
    UnknownTimer_04(
        hours=3,
        minutes=30,
        seconds=0,
        unknown1=0,
        unknown2=0,
        unknown3=0,
        unknown4=0,
        unknown5=0,
        unknown6=0,
    )
    Unknown_2003_68(unknown1=0, unknown2=-1.0, unknown3=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EndOfAnimation(obj=1051361520, animation_id=2)
    End()


@RestartOnRest(1051362230)
def Event_1051362230():
    """Event 1051362230"""
    EndIfFlagEnabled(1051360230)
    IfFlagEnabled(AND_1, 9412)
    IfFlagEnabled(AND_1, 1051360800)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1051362230)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndOfAnimation(obj=1051361520, animation_id=2)
    EnableFlag(1051360230)
    End()


@RestartOnRest(1051362340)
def Event_1051362340(_, character: uint):
    """Event 1051362340"""
    EndIfFlagEnabled(1051362340)
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1051362340)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=1051360340, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableFlag(1051362340)
    EnableAI(character)
    ForceAnimation(1051360340, 20016, wait_for_completion=True, unknown2=1.0)
    SetNest(1051360340, region=1051362341)


@RestartOnRest(1051362490)
def Event_1051362490(_, region: uint):
    """Event 1051362490"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_3, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Wait(0.10000000149011612)
    IfFlagEnabled(AND_4, 9410)
    IfFlagDisabled(AND_4, 9413)
    IfCharacterInsideRegion(AND_4, character=20000, region=1051362500)
    SkipLinesIfConditionTrue(1, AND_4)
    CancelSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1051362500)
def Event_1051362500():
    """Event 1051362500"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=9413)
    IfCharacterInsideRegion(AND_1, character=20000, region=1051362500)
    IfFlagEnabled(AND_1, 9410)
    IfFailedToCreateSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=9413)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(OR_2, character=20000, region=1051362500)
    IfFailedToCreateSession(OR_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SkipLinesIfCharacterInsideRegion(line_count=1, character=20000, region=1051362710)
    CancelSpecialEffect(20000, 9621)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(20000, 9621)
    End()


@NeverRestart(1051362510)
def Event_1051362510():
    """Event 1051362510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1051360510,
            1051360511,
            0,
            1051361510,
            1051361511,
            1051363511,
            1051361512,
            1051363512,
            1051362511,
            1051362512,
            1051360512,
            1051360513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1051362519)
def Event_1051362519():
    """Event 1051362519"""
    EndIfFlagEnabled(1051360514)
    EnableFlag(1051360514)
    DisableFlag(1051360519)
    EnableFlag(1051360510)


@NeverRestart(1051362560)
def Event_1051362560(_, obj: uint):
    """Event 1051362560"""
    GotoIfFlagEnabled(Label.L0, flag=9413)
    GotoIfFlagEnabled(Label.L1, flag=9410)

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EndIfFlagEnabled(9413)
    EndOfAnimation(obj=obj, animation_id=2)


@RestartOnRest(1051362580)
def Event_1051362580():
    """Event 1051362580"""
    RegisterLadder(start_climbing_flag=1051360580, stop_climbing_flag=1051360581, obj=1051361580)
    RegisterLadder(start_climbing_flag=1051360582, stop_climbing_flag=1051360583, obj=1051361582)
    RegisterLadder(start_climbing_flag=1051360584, stop_climbing_flag=1051360585, obj=1051361584)
    RegisterLadder(start_climbing_flag=1051360588, stop_climbing_flag=1051360589, obj=1051361588)
    RegisterLadder(start_climbing_flag=1051360590, stop_climbing_flag=1051360591, obj=1051361590)
    RegisterLadder(start_climbing_flag=1051360592, stop_climbing_flag=1051360593, obj=1051361592)
    RegisterLadder(start_climbing_flag=1051360594, stop_climbing_flag=1051360595, obj=1051361594)


@RestartOnRest(1051362630)
def Event_1051362630(_, obj: uint):
    """Event 1051362630"""
    DisableObject(obj)


@RestartOnRest(1051362650)
def Event_1051362650(
    _,
    flag: uint,
    flag_1: uint,
    obj: uint,
    source_flag: uint,
    value: uint,
    flag_2: uint,
    flag_3: uint,
    flag_4: uint,
    flag_5: uint,
    flag_6: uint,
    flag_7: uint,
):
    """Event 1051362650"""
    IfFlagEnabled(MAIN, 1051360800)
    DeleteObjectVFX(obj, erase_root=False)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    IfEventValueGreaterThan(AND_10, flag=source_flag, bit_count=3, value=value)
    EndIfConditionTrue(input_condition=AND_10)
    SkipLinesIfFlagEnabled(1, 9000)
    CreateObjectVFX(obj, vfx_id=100, model_point=6400)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 9000)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    RestartIfFlagEnabled(flag)
    IfEventValueGreaterThan(AND_11, flag=source_flag, bit_count=3, value=value)
    RestartIfConditionTrue(input_condition=AND_11)
    CreateObjectVFX(obj, vfx_id=100, model_point=6400)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=0)
    EnableFlag(flag_2)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=0,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_2)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=1)
    EnableFlag(flag_3)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_3)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=2)
    EnableFlag(flag_4)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_4)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=3)
    EnableFlag(flag_5)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_5)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=4)
    EnableFlag(flag_6)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=4,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_6)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=5)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=5,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    IfEventValueNotEqual(OR_2, flag=source_flag, bit_count=3, value=value)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1051362800)
def Event_1051362800():
    """Event 1051362800"""
    EndIfFlagEnabled(1051360800)
    IfFlagEnabled(AND_3, 9410)
    IfFlagDisabled(AND_3, 9413)
    EndIfConditionTrue(input_condition=AND_3)
    IfHealthValueLessThanOrEqual(AND_1, 1051360800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 1051360801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(1051360800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 1051360800)
    IfCharacterDead(AND_2, 1051360801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=1051360800, banner_type=BannerType.Unknown)
    EnableFlag(1051360800)
    EnableFlag(9183)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61183)


@RestartOnRest(1051362810)
def Event_1051362810():
    """Event 1051362810"""
    GotoIfFlagDisabled(Label.L0, flag=1051360800)
    DisableCharacter(1051360800)
    DisableAnimations(1051360800)
    Kill(1051360800)
    DisableCharacter(1051360801)
    DisableAnimations(1051360801)
    Kill(1051360801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L5, flag=9410)
    GotoIfFlagEnabled(Label.L5, flag=9413)
    DisableCharacter(1051360800)
    DisableAnimations(1051360800)
    Kill(1051360800)
    DisableCharacter(1051360801)
    DisableAnimations(1051360801)
    Kill(1051360801)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableAI(1051360801)
    DisableAI(1051360800)
    IfFlagEnabled(AND_2, 1051362805)
    IfConditionTrue(AND_2, input_condition=OR_15)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1051362800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(1051360801)
    SetNetworkUpdateRate(1051360801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1051360801, name=903460501)
    IfHealthRatioLessThan(OR_1, 1051360801, value=0.5)
    IfCharacterDead(OR_1, 1051360801)
    IfTimeElapsed(OR_1, seconds=30.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1051360800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    ForceAnimation(1051360800, 20011, unknown2=1.0)
    EnableAI(1051360800)
    SetNetworkUpdateRate(1051360800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1051360800, name=902500500, bar_slot=1)
    SetNest(1051360800, region=1051362299)


@RestartOnRest(1051362849)
def Event_1051362849():
    """Event 1051362849"""
    IfFlagEnabled(AND_3, 9410)
    IfFlagDisabled(AND_3, 9413)
    EndIfConditionTrue(input_condition=AND_3)
    RunCommonEvent(
        0,
        9005800,
        args=(1051360800, 1051361800, 1051362800, 1051362805, 1051365800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1051360800, 1051361800, 1051362800, 1051362805, 1051362806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1051360800, 1051361800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(1051360800, 1051361801, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1051360800, 920200, 1051362805, 1051362806, 0, 1051362802, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(1051363700)
def Event_1051363700():
    """Event 1051363700"""
    IfFlagEnabled(AND_1, 1051362702)
    IfFlagEnabled(AND_1, 9410)
    IfFlagDisabled(AND_1, 9411)
    AwaitConditionTrue(AND_1)
    PlayCutscene(60510000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(9411)
    End()


@RestartOnRest(1051363710)
def Event_1051363710(_, character: uint):
    """Event 1051363710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3667)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3667)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3667)
    Restart()


@RestartOnRest(1051363711)
def Event_1051363711():
    """Event 1051363711"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(9412)
    IfFlagEnabled(AND_1, 9410)
    AwaitConditionTrue(AND_1)
    EnableFlag(3678)
    End()


@RestartOnRest(1051360720)
def Event_1051360720(_, character: uint):
    """Event 1051360720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3600)
    DisableFlag(1051369352)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L11, flag=3611)
    GotoIfFlagEnabled(Label.L12, flag=3612)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3611, 3612))
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)

    # --- Label 12 --- #
    DefineLabel(12)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3602)
    GotoIfFlagEnabled(Label.L3, flag=3603)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(character)
    DisableCharacter(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3611, 3612))
    Restart()


@RestartOnRest(1051360721)
def Event_1051360721():
    """Event 1051360721"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(9412)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3605, 3610))
    IfFlagEnabled(AND_1, 9410)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1051362739)
    EnableFlag(3618)


@RestartOnRest(1051363725)
def Event_1051363725(_, character__obj: uint):
    """Event 1051363725"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3360)
    IfFlagEnabled(AND_1, 1051369203)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1051369203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObjectInvulnerability(1051361700)
    IfFlagEnabled(OR_1, 3365)
    IfFlagEnabled(OR_1, 3367)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3365)
    IfFlagEnabled(OR_2, 3367)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 90100, unknown2=1.0)
    DisableGravity(character__obj)
    EnableObjectInvulnerability(1051361700)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character__obj)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3365)
    IfFlagEnabled(OR_15, 3367)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1051363726)
def Event_1051363726(_, character__obj: uint):
    """Event 1051363726"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3360)
    IfFlagEnabled(AND_1, 1051369203)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1051369203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    IfFlagEnabled(OR_1, 3366)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3366)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character__obj)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3366)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1051363727)
def Event_1051363727():
    """Event 1051363727"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=1051360701, distance=17.0)
    EndIfFlagEnabled(9413)
    SetCharacterTalkRange(character=1051360701, distance=80.0)
    IfFlagEnabled(AND_1, 3366)
    IfFlagDisabled(AND_1, 1051362701)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1051362701)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1051362700)
    End()


@RestartOnRest(1051360730)
def Event_1051360730(_, character: uint, animation_id: int, left: uint):
    """Event 1051360730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    AddSpecialEffect(character, 5005)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 9410)
    IfFlagDisabled(AND_1, 9413)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_2, 9410)
    IfFlagDisabled(AND_2, 9413)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    DisableAnimations(character)
    IfFlagEnabled(AND_3, 9410)
    IfFlagDisabled(AND_3, 9413)
    IfConditionFalse(MAIN, input_condition=AND_3)
    Restart()


@RestartOnRest(1051360734)
def Event_1051360734(_, character: uint):
    """Event 1051360734"""
    EndIfPlayerNotInOwnWorld()
    AddSpecialEffect(character, 5005)
    IfFlagEnabled(AND_1, 9410)
    IfFlagDisabled(AND_1, 9413)
    IfActionButtonParamActivated(AND_1, action_button_id=6000, entity=character)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 90203, unknown2=1.0)
    Wait(2.5)
    SkipLinesIfFlagEnabled(2, 60801)
    Unknown_2003_71(unk_0_4=1)
    EnableFlag(60801)


@RestartOnRest(1051360735)
def Event_1051360735(_, character: uint, animation_id: int, left: uint):
    """Event 1051360735"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    AddSpecialEffect(character, 5005)
    SkipLinesIfFlagEnabled(1, 7606)
    EnableNetworkFlag(1051362735)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 9410)
    IfFlagDisabled(AND_1, 9413)
    IfFlagEnabled(AND_1, 1051362735)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_2, 9410)
    IfFlagDisabled(AND_2, 9413)
    IfFlagEnabled(AND_2, 1051362735)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    DisableAnimations(character)
    IfFlagEnabled(AND_3, 9410)
    IfFlagDisabled(AND_3, 9413)
    IfFlagEnabled(AND_3, 1051362735)
    IfConditionFalse(MAIN, input_condition=AND_3)
    Restart()
