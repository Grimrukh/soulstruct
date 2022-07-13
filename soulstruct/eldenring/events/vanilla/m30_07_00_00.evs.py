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
    RegisterGrace(grace_flag=300700, obj=30071950, unknown=5.0)
    RunCommonEvent(
        0,
        90005501,
        args=(30070515, 30070516, 3, 30071515, 30071516, 30071517, 30070517),
        arg_types="IIIIIII",
    )
    Event_30070510()
    RunCommonEvent(0, 90005650, args=(30070540, 30071540, 30071541, 30073541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30070540, 30071540), arg_types="II")
    Event_30072505(0, 30072502, 30073502, 30071502, 30072502, 0.0)
    Event_30072610(
        0,
        30070610,
        30071610,
        30072610,
        801020000,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072610(
        1,
        30070615,
        30071615,
        30072645,
        801020000,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072611(
        0,
        30070610,
        30071610,
        30072610,
        801020010,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072611(
        1,
        30070615,
        30071615,
        30072645,
        801020010,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072612(
        0,
        30070610,
        30071610,
        30072610,
        801020020,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072612(
        1,
        30070615,
        30071615,
        30072645,
        801020020,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072613(
        0,
        30070610,
        30071610,
        30072610,
        801020030,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072613(
        1,
        30070615,
        30071615,
        30072645,
        801020030,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072614(
        0,
        30070610,
        30071610,
        30072610,
        801020040,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072614(
        1,
        30070615,
        30071615,
        30072645,
        801020040,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072615(
        0,
        30070610,
        30071610,
        30072610,
        801020050,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072615(
        1,
        30070615,
        30071615,
        30072645,
        801020050,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072616(
        0,
        30070610,
        30071610,
        30072610,
        801020060,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072616(
        1,
        30070615,
        30071615,
        30072645,
        801020060,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072617(
        0,
        30070610,
        30071610,
        30072610,
        801020070,
        30072611,
        30072612,
        30072613,
        30072614,
        30072615,
        30072616,
        30072617,
        30072618,
        30072619,
        30072620,
        30072621,
        30072622,
        30072623,
    )
    Event_30072617(
        1,
        30070615,
        30071615,
        30072645,
        801020070,
        30072630,
        30072631,
        30072632,
        30072633,
        30072634,
        30072635,
        30072636,
        30072637,
        30072638,
        30072639,
        30072640,
        30072641,
        30072642,
    )
    Event_30072510()
    Event_30072515()
    Event_30072516()
    RunCommonEvent(0, 90005513, args=(30070542, 30071542, 30071543, 30073543, 27002, 0, 0), arg_types="IIIIiii")
    RunCommonEvent(
        0,
        90005620,
        args=(30070570, 30071570, 30071571, 0, 30072570, 30072571, 30072572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30070570, 30071573), arg_types="II")
    Event_30072580()
    RunCommonEvent(
        0,
        90005646,
        args=(30070800, 30072840, 30072841, 30071840, 30072840, 30, 7, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(30072800, 30071695, 5), arg_types="IIi")
    Event_30072800()
    Event_30072810()
    Event_30072849()
    Event_30072811()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005211, args=(30070200, 30010, 20010, 30072200, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(1, 90005211, args=(30070201, 30010, 20010, 30072200, 5.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(30070205, 30072205, 0.0, 3004), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(30070206, 30002, 20002, 30072205, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(30070210, 30001, 20001, 30072210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(30070214, 30072510, 7.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(30070215, 30072216, 0.0, -1), arg_types="IIfi")
    Event_30072500()
    Event_30072501()
    RunCommonEvent(0, 90005250, args=(30070219, 30072215, 1.0, 3005), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30070300, 30072300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30070301, 30072300, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(30070302, 30072300, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(3, 90005250, args=(30070303, 30072300, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(4, 90005250, args=(30070311, 30072300, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(5, 90005250, args=(30070312, 30072300, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30070307, 30000, 20000, 30072307, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30070308, 30000, 20000, 30072307, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(2, 90005200, args=(30070309, 30000, 20000, 30072307, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        3,
        90005200,
        args=(30070310, 30000, 20000, 30072307, 1.2999999523162842, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005250, args=(30070313, 30072313, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30070314, 30072313, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(30070315, 30072313, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(3, 90005250, args=(30070316, 30072313, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(30070320, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(30070321, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(30070322, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(30070323, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(30070324, 30004, 20004, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(30070350, 30000, 20000, 30072350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070351, 30000, 20000, 30072351, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070352, 30000, 20000, 30072352, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070353, 30000, 20000, 30072353, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070354, 30000, 20000, 30072354, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070355, 30000, 20000, 30072355, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070356, 30000, 20000, 30072356, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070357, 30000, 20000, 30072357, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30070358, 30000, 20000, 30072350, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        2,
        90005200,
        args=(30070359, 30000, 20000, 30072350, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005261, args=(30070400, 30072400, 4.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(30070410, 30001, 20001, 30072410, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30070411, 30001, 20001, 30072411, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30070519()
    Event_30072618()


@NeverRestart(30070510)
def Event_30070510():
    """Event 30070510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30070515,
            30070516,
            3,
            30071515,
            30071516,
            30073516,
            30071517,
            30073517,
            30072516,
            30072517,
            30070517,
            30070518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30070519)
def Event_30070519():
    """Event 30070519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30070515)


@RestartOnRest(30072520)
def Event_30072520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30072520"""
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


@RestartOnRest(30072341)
def Event_30072341(_, character: uint, seconds: float, region: uint, flag: uint, region_1: uint):
    """Event 30072341"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfPlayerInOwnWorld(OR_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 30001, unknown2=1.0)
    EnableFlag(flag)
    Wait(4.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfPlayerInOwnWorld(OR_2)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(seconds)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20001, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(30072500)
def Event_30072500():
    """Event 30072500"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30072215)
    IfCharacterBackreadEnabled(AND_1, 30070215)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(30072501)
def Event_30072501():
    """Event 30072501"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30072216)
    IfCharacterBackreadEnabled(AND_1, 30070215)
    IfFlagEnabled(AND_1, 30072500)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(0.0)
    ForceAnimation(30070215, 3017, loop=True, wait_for_completion=True, unknown2=1.0)
    DisableNetworkFlag(30072500)
    End()


@NeverRestart(30072505)
def Event_30072505(_, flag: uint, obj_flag: uint, obj: uint, region: uint, seconds: float):
    """Event 30072505"""
    IfUnknown_3_32(AND_10, unk_1_2=1, unk_4_8=0)
    IfFlagEnabled(AND_10, flag)
    GotoIfConditionFalse(Label.L10, input_condition=AND_10)
    DisableNetworkFlag(flag)
    EnableThisSlotFlag()

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region)
    IfThisEventSlotFlagEnabled(OR_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    Wait(seconds)
    ForceAnimation(obj, 3, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 50)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203200,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203210,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203220,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203230,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203240,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203250,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203260,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=801203270,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    Wait(1.0)
    RemoveObjectFlag(obj_flag=obj_flag)
    Wait(4.099999904632568)
    Wait(0.10000000149011612)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    Restart()


@NeverRestart(30072510)
def Event_30072510():
    """Event 30072510"""
    GotoIfFlagEnabled(Label.L0, flag=30070510)
    IfCharacterHuman(OR_9, PLAYER)
    IfCharacterType(OR_9, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_9, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_9)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30072510)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(30071510, 12, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    IfAllPlayersOutsideRegion(AND_1, region=30072510)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    EnableFlag(30070510)
    ForceAnimation(30071510, 20, wait_for_completion=True, unknown2=1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(30070510)
    ForceAnimation(30071510, 21, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072515)
def Event_30072515():
    """Event 30072515"""
    IfFlagEnabled(AND_1, 30070510)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30072512)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 4195)
    IfConditionTrue(MAIN, input_condition=AND_1)
    MoveObjectToCharacter(30071511, character=PLAYER, model_point=93)
    WaitFrames(frames=1)
    SkipLinesIfFlagDisabled(1, 50)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303200,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303220,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303230,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303240,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303250,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303260,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    CreateHazard(
        obj_flag=30073511,
        obj=30071511,
        model_point=100,
        behavior_param_id=801303270,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveObjectFlag(obj_flag=30073511)
    Wait(0.5)
    Restart()


@NeverRestart(30072516)
def Event_30072516():
    """Event 30072516"""
    IfFlagEnabled(AND_1, 30070510)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30072511)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4195)
    Wait(0.5)
    Restart()


@NeverRestart(30072580)
def Event_30072580():
    """Event 30072580"""
    RegisterLadder(start_climbing_flag=30070580, stop_climbing_flag=30070581, obj=30071580)


@NeverRestart(30072605)
def Event_30072605(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
):
    """Event 30072605"""
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(13, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(12)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(13, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(12)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(13, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(12)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072610)
def Event_30072610(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072610"""
    IfFlagDisabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072611)
def Event_30072611(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072611"""
    IfFlagEnabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072612)
def Event_30072612(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072612"""
    IfFlagEnabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072613)
def Event_30072613(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072613"""
    IfFlagEnabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagDisabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072614)
def Event_30072614(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072614"""
    IfFlagEnabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagDisabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072615)
def Event_30072615(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072615"""
    IfFlagEnabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagDisabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072616)
def Event_30072616(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072616"""
    IfFlagEnabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagDisabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072617)
def Event_30072617(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
    source_entity_3: uint,
    source_entity_4: uint,
    source_entity_5: uint,
    source_entity_6: uint,
    source_entity_7: uint,
    source_entity_8: uint,
    source_entity_9: uint,
    source_entity_10: uint,
    source_entity_11: uint,
    source_entity_12: uint,
):
    """Event 30072617"""
    IfFlagEnabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagDisabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(6, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(14, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(13)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_10,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_11,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_12,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30072618)
def Event_30072618():
    """Event 30072618"""
    SkipLinesIfFlagDisabled(2, 57)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020070, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020060, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020050, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020040, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020030, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020020, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(4)
    SkipLinesIfFlagDisabled(2, 51)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020010, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLines(1)
    RunCommonEvent(
        0,
        90005660,
        args=(30070600, 30071600, 30072600, 801020000, 30072601, 30072602, 30072603),
        arg_types="IIIiIII",
    )
    SkipLinesIfFlagDisabled(2, 57)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020070, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020060, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020050, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020040, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020030, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020020, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(4)
    SkipLinesIfFlagDisabled(2, 51)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020010, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )
    SkipLines(1)
    RunCommonEvent(
        0,
        90005660,
        args=(30070605, 30071605, 30072605, 801020000, 30072606, 30072607, 30072608),
        arg_types="IIIiIII",
    )


@RestartOnRest(30072800)
def Event_30072800():
    """Event 30072800"""
    EndIfFlagEnabled(30070800)
    IfHealthValueLessThanOrEqual(MAIN, 30070800, value=0)
    Wait(4.0)
    PlaySoundEffect(30070800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30070800)
    KillBossAndDisplayBanner(character=30070800, banner_type=BannerType.Unknown)
    EnableFlag(30070800)
    EnableFlag(9212)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61212)


@RestartOnRest(30072810)
def Event_30072810():
    """Event 30072810"""
    GotoIfFlagDisabled(Label.L0, flag=30070800)
    DisableCharacter(30070800)
    DisableAnimations(30070800)
    Kill(30070800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30070800)
    IfFlagEnabled(AND_2, 30072805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30072800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30070800)
    SetNetworkUpdateRate(30070800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30070800, name=904260303)


@RestartOnRest(30072811)
def Event_30072811():
    """Event 30072811"""
    EndIfFlagEnabled(30070800)
    IfHealthRatioLessThanOrEqual(AND_1, 30070800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30072802)


@RestartOnRest(30072849)
def Event_30072849():
    """Event 30072849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30070800, 30071800, 30072800, 30072805, 30075800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30070800, 30071800, 30072800, 30072805, 30072806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30070800, 30071800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30070800, 930000, 30072805, 30072806, 0, 30072802, 0, 0), arg_types="IiIIIIii")
