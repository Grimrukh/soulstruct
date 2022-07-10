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
    RegisterGrace(grace_flag=71231, obj=12031951, unknown=5.0)
    RegisterGrace(grace_flag=71232, obj=12031952, unknown=5.0)
    RegisterGrace(grace_flag=71233, obj=12031953, unknown=5.0)
    RegisterGrace(grace_flag=71234, obj=12031954, unknown=5.0)
    RegisterGrace(grace_flag=71235, obj=12031955, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(12030800, 71230, 12030950, 12031950, 5.0), arg_types="IIIIf")
    Event_12032800()
    Event_12032810()
    Event_12032811()
    Event_12032812()
    Event_12032849()
    Event_12032841()
    Event_12032850()
    Event_12032860()
    Event_12032859()
    Event_12032899()
    Event_12032861()
    Event_12032862()
    Event_12032310(0, character=12030240)
    Event_12032310(1, character=12030241)
    Event_12032310(2, character=12030242)
    Event_12032310(3, character=12030243)
    Event_12032310(4, character=12030244)
    Event_12032310(5, character=12030245)
    Event_12032310(6, character=12030246)
    Event_12032310(7, character=12030247)
    Event_12032310(8, character=12030248)
    Event_12032310(9, character=12030249)
    Event_12032310(10, character=12030250)
    Event_12032310(11, character=12030251)
    Event_12032310(12, character=12030252)
    Event_12032310(13, character=12030253)
    Event_12032310(14, character=12030254)
    Event_12032310(15, character=12030255)
    Event_12032310(16, character=12030256)
    Event_12032310(17, character=12030257)
    Event_12032241(0, 12030242, 0.0)
    Event_12032241(1, 12030243, 0.0)
    Event_12032241(2, 12030244, 8.0)
    Event_12032241(3, 12030245, 0.0)
    Event_12032241(4, 12030246, 9.0)
    Event_12032241(5, 12030247, 9.0)
    Event_12032241(6, 12030248, 15.5)
    Event_12032241(7, 12030249, 16.0)
    Event_12032241(8, 12030250, 16.0)
    Event_12032241(9, 12030251, 28.0)
    Event_12032241(10, 12030252, 28.0)
    Event_12032241(11, 12030253, 28.0)
    Event_12032241(12, 12030254, 25.0)
    Event_12032241(13, 12030255, 20.0)
    RunCommonEvent(0, 90005261, args=(12030200, 12032200, 50.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12030210, 12032200, 50.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12030211, 12032200, 50.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12030212, 12032200, 50.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12030213, 12032200, 50.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(12030214, 12032200, 50.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005300, args=(12030240, 12030240, 12030800, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030241, 12030241, 12030810, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030256, 12030256, 12030820, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030257, 12030257, 12030830, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030297, 12030297, 12030840, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030201, 12030201, 12030850, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005251, args=(12030303, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(12030350, 12030350, 40660, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030354, 12030354, 40668, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12030355, 12030355, 40670, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005860, args=(12030390, 0, 12030390, 1, 12030950, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(12030390, 902500600, 12), arg_types="IiI")
    RunCommonEvent(0, 90005872, args=(12030390, 12, 0), arg_types="III")
    RunCommonEvent(0, 90005300, args=(12030391, 12030391, 12030960, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005250, args=(12030391, 12032391, 0.0, -1), arg_types="IIfi")
    Event_12032504()
    Event_12032509()
    RunCommonEvent(0, 90005251, args=(12030400, 200.0, 10.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005451, args=(12030400, 12036420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(12030400, 12030400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(12030400, 12032400, 12030400), arg_types="III")
    RunCommonEvent(0, 90005456, args=(12030400, 12031410, 12031418, 12030400), arg_types="IIII")
    RunCommonEvent(0, 90005458, args=(12030400, 12031401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(12030400, 12031420, 60, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(12030400, 12031421, 61, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031422, 62, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031423, 63, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031424, 64, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031425, 65, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031426, 66, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031427, 67, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031428, 68, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031429, 69, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031430, 70, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031431, 71, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031432, 72, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031433, 73, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031434, 74, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(12030400, 12031435, 75, 0.5), arg_types="IIif")
    Event_12032300(0, 12035380, 1.0)
    Event_12032500()
    Event_12030050()
    RunCommonEvent(0, 90005704, args=(12030710, 4061, 4060, 12039001, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(12030710, 4061, 4062, 12039001, 4061, 4060, 4063, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(12030710, 4063, 4060, 4063), arg_types="IIII")
    Event_12030710(0, character=12030710)
    RunCommonEvent(0, 90005750, args=(12031720, 4350, 103410, 400348, 400348, 4067, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005704, args=(12030702, 4121, 4120, 12039051, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(12030702, 4121, 4122, 12039051, 4121, 4120, 4123, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(12030702, 4123, 4120, 4123), arg_types="IIII")
    Event_12030700(0, character=12030702)
    Event_12030701(0, character=12030700, obj=12031730)
    Event_12030702(0, character=12030703)
    Event_12030703(0, character=12030701, obj=12031701, obj_1=12031702)
    Event_12030709(0, flag=12039179)
    Event_12030704()
    Event_12030705()
    Event_12030706()
    RunCommonEvent(
        0,
        90005740,
        args=(
            12032715,
            12032716,
            12032717,
            12030702,
            702,
            12031731,
            702,
            0.4000000059604645,
            90305,
            90307,
            -1,
            1.2999999523162842,
        ),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(
        0,
        90005741,
        args=(12032718, 12032719, 12032717, 12030702, 90330, 0, 90332, -1, 0.5),
        arg_types="IIIIiIiif",
    )
    Event_12030707()
    Event_12030708(0, entity=12030702)
    RunCommonEvent(0, 90005750, args=(12031710, 6460, 103350, 9502, 9502, 4131, 806781), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(12031710, 4110, 113300, 400339, 400339, 12039162, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005733, args=(12032714,))
    RunCommonEvent(
        0,
        90005740,
        args=(12032725, 12032726, 0, 12030700, 0, 0, 0, 1.2999999523162842, 90305, 90307, -1, 1.2999999523162842),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(0, 90005752, args=(12031730, 200, 120, 3.0), arg_types="Iiif")
    Event_12030720(0, 12030725)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12030700)
    DisableBackread(12030701)
    DisableBackread(12030702)
    DisableBackread(12030703)
    DisableBackread(12030705)
    DisableBackread(12030710)
    DisableBackread(12030715)
    DisableBackread(12030720)
    DisableBackread(12030721)
    DisableBackread(12030725)
    DisableObject(12031730)
    Event_12032820()
    RunCommonEvent(0, 90005450, args=(12030400, 12031400, 12031410, 12031418), arg_types="IIII")


@RestartOnRest(12030050)
def Event_12030050():
    """Event 12030050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(12030401)
    DisableFlag(12030402)


@RestartOnRest(12032400)
def Event_12032400():
    """Event 12032400"""
    EndIfThisEventSlotFlagEnabled()
    SetNetworkUpdateRate(12030400, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(12032500)
def Event_12032500():
    """Event 12032500"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(12032501)
    DisableFlag(12032502)
    DisableFlag(12032504)
    SkipLinesIfThisEventSlotFlagEnabled(3)
    DeleteObjectVFX(12031500)
    DisableFlag(12032503)
    WaitFrames(frames=1)
    IfTryingToCreateSession(OR_11)
    IfTryingToJoinSession(OR_11)
    SkipLinesIfConditionFalse(1, OR_11)
    EnableFlag(12032504)
    IfTryingToCreateSession(OR_10)
    IfTryingToJoinSession(OR_10)
    IfFlagDisabled(OR_10, 182)
    IfFlagDisabled(OR_10, 105)
    IfFlagEnabled(OR_10, 300)
    IfFlagDisabled(OR_10, 12030800)
    IfFlagEnabled(OR_10, 12032870)
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    GotoIfFlagEnabled(Label.L1, flag=12032503)
    CreateObjectVFX(12031500, vfx_id=200, model_point=806870)
    EnableFlag(12032503)

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerInOwnWorld(AND_1)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=12031500)
    IfTryingToCreateSession(OR_4)
    IfTryingToJoinSession(OR_4)
    IfFlagDisabled(OR_4, 182)
    IfFlagDisabled(OR_4, 105)
    IfFlagEnabled(OR_4, 300)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, 12032503)
    IfFlagEnabled(AND_7, 12032504)
    IfTryingToCreateSession(OR_8)
    IfTryingToJoinSession(OR_8)
    IfConditionFalse(AND_7, input_condition=OR_8)
    IfFlagDisabled(AND_7, 12032503)
    IfFlagState(OR_9, FlagSetting.Change, FlagType.Absolute, 182)
    IfFlagState(OR_9, FlagSetting.Change, FlagType.Absolute, 105)
    IfFlagState(OR_9, FlagSetting.Change, FlagType.Absolute, 300)
    IfFlagState(OR_9, FlagSetting.Change, FlagType.Absolute, 12032870)
    IfFlagState(OR_9, FlagSetting.Change, FlagType.Absolute, 12030800)
    IfConditionTrue(AND_9, input_condition=OR_9)
    IfConditionTrue(OR_14, input_condition=AND_1)
    IfConditionTrue(OR_14, input_condition=AND_4)
    IfConditionTrue(OR_14, input_condition=AND_7)
    IfConditionTrue(OR_14, input_condition=AND_9)
    IfConditionTrue(MAIN, input_condition=OR_14)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_4)
    DeleteObjectVFX(12031500)
    DisableFlag(12032503)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.032999999821186066)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L10, flag=12030800)
    GotoIfFlagEnabled(Label.L10, flag=12032870)
    GotoIfFlagEnabled(Label.L10, flag=300)
    GotoIfFlagDisabled(Label.L4, flag=182)
    GotoIfFlagEnabled(Label.L5, flag=105)

    # --- Label 4 --- #
    DefineLabel(4)
    DisplayDialog(text=20004, anchor_entity=12031500, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    DisplayDialog(text=30040, anchor_entity=12031500, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=12031500,
        display_distance=3.0,
        left_flag=12032501,
        right_flag=12032502,
        cancel_flag=12032502,
    )
    GotoIfFlagEnabled(Label.L6, flag=12032501)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    IfTryingToCreateSession(OR_15)
    IfTryingToJoinSession(OR_15)
    RestartIfConditionTrue(input_condition=OR_15)
    RotateToFaceEntity(PLAYER, 12031500, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    EnableFlag(11000600)
    EnableFlag(11000603)
    Wait(3.0)
    WarpToMap(game_map=LEYNDELL_ROYAL_CAPITAL, player_start=11002500)
    Restart()

    # --- Label 16 --- #
    DefineLabel(16)
    IfFlagEnabled(MAIN, 12030800)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DeleteObjectVFX(12031500)
    IfFlagDisabled(MAIN, 12032870)
    Restart()


@NeverRestart(12032504)
def Event_12032504():
    """Event 12032504"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkSync()
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9710, entity=12031504)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.10000000149011612)
    EnableFlag(9021)
    BanishPhantoms(unknown=0)

    # --- Label 5 --- #
    DefineLabel(5)
    Wait(1.0)
    GotoIfTryingToCreateSession(Label.L5)
    SetRespawnPoint(respawn_point=12012504)
    SaveRequest()
    UnknownCutscene_11(
        cutscene_id=12030010,
        cutscene_flags=0,
        move_to_region=12012504,
        map_base_id=12010000,
        player_id=10000,
        unknown2=12030000,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutscene(12030011, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Wait(1.0)
    DisplayUnknownMessage_14(text=12010)


@NeverRestart(12032509)
def Event_12032509():
    """Event 12032509"""
    DisableNetworkSync()
    IfFlagEnabled(AND_2, 12020800)
    IfPlayerInOwnWorld(AND_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9710, entity=12021502)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(12020502)
    Wait(0.10000000149011612)
    EnableFlag(9021)
    SetRespawnPoint(respawn_point=12032502)
    SaveRequest()
    UnknownCutscene_11(
        cutscene_id=12020000,
        cutscene_flags=0,
        move_to_region=12032502,
        map_base_id=12030000,
        player_id=10000,
        unknown2=12020000,
        unknown3=0,
    )
    PlayCutscene(12020001, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFrames(frames=1)
    Wait(1.0)
    DisplayUnknownMessage_14(text=12030)


@RestartOnRest(12032300)
def Event_12032300(_, character: uint, seconds: float):
    """Event 12032300"""
    GotoIfFlagDisabled(Label.L0, flag=12030400)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_1, 12030400)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(seconds)
    Kill(character)


@RestartOnRest(12032310)
def Event_12032310(_, character: uint):
    """Event 12032310"""
    EndIfFlagEnabled(12032240)
    DisableFlag(12032240)
    AddSpecialEffect(character, 10949)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=12032240)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableFlag(12032240)


@RestartOnRest(12032241)
def Event_12032241(_, character: uint, seconds: float):
    """Event 12032241"""
    SetTeamType(12035240, TeamType.Enemy)
    SetTeamType(12035241, TeamType.Enemy)
    SetTeamType(12035256, TeamType.Enemy)
    SetTeamType(12035257, TeamType.Enemy)
    SetTeamType(character, TeamType.Enemy)
    AddSpecialEffect(character, 2900)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfFlagEnabled(OR_2, 12032240)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    Wait(seconds)
    ForceAnimation(character, 20001, loop=True, unknown2=1.0)
    End()


@RestartOnRest(12032800)
def Event_12032800():
    """Event 12032800"""
    EndIfFlagEnabled(12030800)
    IfHealthValueLessThanOrEqual(AND_1, 12030800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 12030810, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 12030811, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 12030812, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 12030813, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    PlaySoundEffect(12030800, 888880000, sound_type=SoundType.s_SFX)
    DisableCharacter(12030814)
    IfCharacterDead(AND_2, 12030800)
    IfCharacterDead(AND_2, 12030810)
    IfCharacterDead(AND_2, 12030811)
    IfCharacterDead(AND_2, 12030812)
    IfCharacterDead(AND_2, 12030813)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=12030800, banner_type=BannerType.Unknown)
    EnableFlag(12030800)
    EnableTreasure(obj=12031490)
    DisableObject(12031810)
    DeleteObjectVFX(12031810)
    EnableFlag(9135)
    EnableFlag(61135)


@RestartOnRest(12032810)
def Event_12032810():
    """Event 12032810"""
    GotoIfFlagDisabled(Label.L0, flag=12030800)
    DisableCharacter(12030800)
    DisableAnimations(12030800)
    Kill(12030800)
    DisableCharacter(12030810)
    DisableAnimations(12030810)
    Kill(12030810)
    DisableCharacter(12030811)
    DisableAnimations(12030811)
    Kill(12030811)
    DisableCharacter(12030812)
    DisableAnimations(12030812)
    Kill(12030812)
    DisableCharacter(12030813)
    DisableAnimations(12030813)
    Kill(12030813)
    DisableCharacter(12030814)
    DisableAnimations(12030814)
    Kill(12030814)
    EnableTreasure(obj=12031490)
    DisableObject(12031810)
    DeleteObjectVFX(12031810, erase_root=False)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12030800)
    DisableAI(12030810)
    DisableAI(12030811)
    DisableAI(12030812)
    DisableAI(12030813)
    DisableAI(12030814)
    DisableCharacter(12030800)
    DisableCharacter(12030810)
    DisableCharacter(12030811)
    DisableCharacter(12030812)
    DisableCharacter(12030813)
    DisableCharacter(12030814)
    DisableTreasure(obj=12031490)
    DisableObject(12031810)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=12032801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(12030801)
    EnableFlag(12032803)
    DeleteObjectVFX(12031810)
    EnableObject(12031810)
    CreateObjectVFX(12031810, vfx_id=200, model_point=806700)
    CreateTemporaryVFX(vfx_id=600940, anchor_entity=12030800, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    SkipLinesIfFlagDisabled(2, 50)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23611, unk_8_12=12030800)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 51)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23612, unk_8_12=12030800)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 52)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23613, unk_8_12=12030800)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 52)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23614, unk_8_12=12030800)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 54)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23615, unk_8_12=12030800)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 55)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23616, unk_8_12=12030800)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 56)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23617, unk_8_12=12030800)
    Goto(Label.L8)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23618, unk_8_12=12030800)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFrames(frames=1)
    EnableCharacter(12030800)
    EnableCharacter(12030814)
    WaitFrames(frames=1)
    ForceAnimation(12030800, 63010, unknown2=1.0)
    EnableAI(12030800)
    SetNetworkUpdateRate(12030800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(3.0)
    EnableBossHealthBar(12030800, name=136100)
    WaitFrames(frames=1)
    EnableNetworkFlag(12032810)


@RestartOnRest(12032811)
def Event_12032811():
    """Event 12032811"""
    EndIfFlagEnabled(12030800)
    IfCharacterDead(AND_1, 12030800)
    IfFlagEnabled(AND_1, 12032810)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    DisableBossHealthBar(12030800, name=136100)
    CreateTemporaryVFX(vfx_id=600940, anchor_entity=12030810, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    EnableCharacter(12030810)
    WaitFrames(frames=1)
    ForceAnimation(12030810, 63010, unknown2=1.0)
    EnableAI(12030810)
    SetNetworkUpdateRate(12030810, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    EnableNetworkFlag(12032811)
    Wait(3.0)
    EnableBossHealthBar(12030810, name=132500)


@RestartOnRest(12032812)
def Event_12032812():
    """Event 12032812"""
    EndIfFlagEnabled(12030800)
    IfCharacterDead(AND_1, 12030810)
    IfFlagEnabled(AND_1, 12032811)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    DisableBossHealthBar(12030810, name=132500)
    CreateTemporaryVFX(vfx_id=600940, anchor_entity=12030811, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    CreateTemporaryVFX(vfx_id=600940, anchor_entity=12030813, model_point=900, anchor_type=CoordEntityType.Character)
    EnableCharacter(12030811)
    WaitFrames(frames=1)
    ForceAnimation(12030811, 63010, unknown2=1.0)
    EnableAI(12030811)
    SetNetworkUpdateRate(12030811, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreateTemporaryVFX(vfx_id=600940, anchor_entity=12030812, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    SkipLinesIfFlagDisabled(2, 50)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23701, unk_8_12=12030813)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 51)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23702, unk_8_12=12030813)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 52)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23703, unk_8_12=12030813)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 53)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23704, unk_8_12=12030813)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 54)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23705, unk_8_12=12030813)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 55)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23706, unk_8_12=12030813)
    Goto(Label.L8)
    SkipLinesIfFlagDisabled(2, 56)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23707, unk_8_12=12030813)
    Goto(Label.L8)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23708, unk_8_12=12030813)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFrames(frames=1)
    EnableCharacter(12030813)
    WaitFrames(frames=1)
    ForceAnimation(12030813, 63010, unknown2=1.0)
    EnableAI(12030813)
    SetNetworkUpdateRate(12030813, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.5)
    SkipLinesIfFlagDisabled(2, 50)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23711, unk_8_12=12030812)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 51)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23712, unk_8_12=12030812)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 52)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23713, unk_8_12=12030812)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 53)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23714, unk_8_12=12030812)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 54)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23715, unk_8_12=12030812)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 55)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23716, unk_8_12=12030812)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 56)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23717, unk_8_12=12030812)
    Goto(Label.L9)
    Unknown_2004_78(unk_0_4=0, unk_4_8=23718, unk_8_12=12030812)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)
    EnableCharacter(12030812)
    WaitFrames(frames=1)
    ForceAnimation(12030812, 63010, unknown2=1.0)
    EnableAI(12030812)
    SetNetworkUpdateRate(12030812, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)
    EnableBossHealthBar(12030811, name=132900)
    EnableBossHealthBar(12030813, name=137000, bar_slot=1)
    EnableBossHealthBar(12030812, name=137100, bar_slot=2)


@NeverRestart(12032820)
def Event_12032820():
    """Event 12032820"""
    EndIfPlayerNotInOwnWorld()
    IfInsideMap(MAIN, game_map=DEEPROOT_DEPTHS)
    Unknown_2004_79(unk_0_4=0, unk_4_8=3)


@RestartOnRest(12032830)
def Event_12032830(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    seconds: float,
    flag_2: uint,
    region_1: uint,
):
    """Event 12032830"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L0, flag=flag_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(1, left=region_1, right=0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    SkipLinesIfFlagEnabled(1, flag_2)
    BanishInvaders(unknown=0)
    RestartIfFlagEnabled(flag)
    Goto(Label.L1)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(flag)
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    EndIfPlayerNotInOwnWorld()
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, flag)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()
    Wait(seconds)


@RestartOnRest(12032840)
def Event_12032840():
    """Event 12032840"""
    DisableNetworkSync()
    EndIfFlagEnabled(12030800)
    IfFlagDisabled(AND_1, 12030800)
    IfFlagEnabled(AND_1, 12032805)
    IfCharacterWhitePhantom(AND_1, PLAYER)
    IfActionButtonParamActivated(AND_1, action_button_id=10000, entity=12031800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_11(unk_0_4=5.0)
    RotateToFaceEntity(PLAYER, 12032800, animation=60060, wait_for_completion=True)
    IfCharacterWhitePhantom(AND_2, PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=12032800)
    IfTimeElapsed(OR_1, seconds=3.0)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(1.0)
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    EnableFlag(12032806)
    DisplayUnknownMessage_16(text=2920000, unknown2=0)
    Wait(4.0)
    Unknown_2004_74(character=PLAYER, unknown1=1, region=12032806, unknown2=-1, character_2=0, unknown3=0, unknown4=0)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 63010, unknown2=1.0)
    Wait(0.5)
    CreateTemporaryVFX(vfx_id=30320, anchor_entity=PLAYER, model_point=900, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12032841)
def Event_12032841():
    """Event 12032841"""
    IfPlayerInOwnWorld(AND_14)
    IfCharacterInsideRegion(AND_14, character=PLAYER, region=12032807)
    IfConditionTrue(MAIN, input_condition=AND_14)
    BanishInvaders(unknown=0)
    Wait(1.0)
    Restart()


@RestartOnRest(12032842)
def Event_12032842(_, flag: uint, obj: uint, model_point: int, right: uint):
    """Event 12032842"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfCharacterType(OR_2, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagDisabled(AND_2, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_3, right)
    IfFlagDisabled(AND_3, flag)
    IfFailedToCreateSession(OR_4)
    IfMultiplayerState(OR_4, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, flag)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=AND_3)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    SkipLinesIfPlayerInOwnWorld(3)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionTrue(AND_11, input_condition=OR_11)
    IfFlagDisabled(AND_11, flag)
    IfCharacterWhitePhantom(OR_12, PLAYER)
    IfCharacterType(OR_12, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_12, input_condition=OR_12)
    IfFlagDisabled(AND_12, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_13, right)
    IfFlagDisabled(AND_13, flag)
    IfFailedToCreateSession(OR_14)
    IfMultiplayerState(OR_14, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_14, input_condition=OR_14)
    IfFlagEnabled(AND_14, flag)
    IfConditionFalse(AND_15, input_condition=AND_11)
    IfConditionFalse(AND_15, input_condition=AND_12)
    IfConditionFalse(AND_15, input_condition=AND_13)
    IfConditionFalse(AND_15, input_condition=AND_14)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(12032849)
def Event_12032849():
    """Event 12032849"""
    Event_12032830(0, 12030800, 12031800, 12032800, 12032805, 12035800, 0.0, 12030801, 12032801)
    Event_12032840()
    RunCommonEvent(0, 12032842, args=(12030800, 12031800, 5, 12030801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(12030800, 921100, 12032805, 12032806, 12032803, 0, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(12032859)
def Event_12032859():
    """Event 12032859"""
    DisableCharacter(12030850)
    EndIfFlagEnabled(12030850)
    IfFlagEnabled(MAIN, 12032859)
    EnableFlag(9021)
    Wait(1.0)
    Unknown_2004_77(unknown1=1.0, unknown2=1.0, unknown3=1, unknown4=1.0)
    Wait(1.0)
    Unknown_2003_68(unknown1=7, unknown2=-1.0, unknown3=1)
    UnknownCutscene_11(
        cutscene_id=12030020,
        cutscene_flags=0,
        move_to_region=12032859,
        map_base_id=12030000,
        player_id=10000,
        unknown2=12030000,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=0.0)
    WaitFramesAfterCutscene(frames=1)
    EnableCharacter(12030850)
    DisableCharacter(12030950)
    DisableObject(12031950)
    EnableFlag(12032858)


@RestartOnRest(12032850)
def Event_12032850():
    """Event 12032850"""
    GotoIfFlagDisabled(Label.L10, flag=12030850)
    EnableCharacter(12030950)
    EnableObject(12031950)
    DisableObject(12031850)
    DeleteObjectVFX(12031850)
    DisableObject(12031106)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagEnabled(AND_8, 12032859)
    IfHealthValueLessThanOrEqual(AND_8, 12030850, value=0)
    IfConditionTrue(MAIN, input_condition=AND_8)
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=0)
    Wait(4.0)
    PlaySoundEffect(12030850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 12030850)
    KillBossAndDisplayBanner(character=12030850, banner_type=BannerType.HollowArenaWin)
    EnableFlag(12030850)
    EnableFlag(9111)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61111)
    SkipLinesIfPlayerNotInOwnWorld(2)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    Wait(9.0)
    UnknownCutscene_11(
        cutscene_id=12030021,
        cutscene_flags=0,
        move_to_region=12032858,
        map_base_id=12030000,
        player_id=10000,
        unknown2=0,
        unknown3=1,
    )
    WaitFramesAfterCutscene(frames=1)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=1)
    DisableObject(12031850)
    DeleteObjectVFX(12031850)
    EnableCharacter(12030950)
    EnableObject(12031950)
    DisableObject(12031106)
    SkipLinesIfPlayerNotInOwnWorld(2)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    Wait(0.10000000149011612)
    DisableNetworkFlag(12032870)


@RestartOnRest(12032860)
def Event_12032860():
    """Event 12032860"""
    GotoIfFlagDisabled(Label.L0, flag=12030850)
    DisableCharacter(12030850)
    DisableAnimations(12030850)
    Kill(12030850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12030850)
    DisableObject(12031850)
    DeleteObjectVFX(12031850)
    DisableObject(12031106)
    IfFlagEnabled(MAIN, 12032858)
    DeleteObjectVFX(12031850)
    EnableObject(12031850)
    CreateObjectVFX(12031850, vfx_id=101, model_point=5)
    EnableObject(12031106)
    EnableNetworkFlag(12030852)
    EnableAI(12030850)
    SetNetworkUpdateRate(12030850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(12030850, name=904510000)
    ActivateMultiplayerBuffs(12035850)
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=1)
    EndIfPlayerNotInOwnWorld()
    EnableNetworkFlag(12032860)
    SetNetworkUpdateAuthority(12035850, authority_level=UpdateAuthority.Unknown8192)
    NotifyBossBattleStart()
    Wait(0.10000000149011612)
    EnableNetworkFlag(12032870)


@RestartOnRest(12032896)
def Event_12032896(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 12032896"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterWhitePhantom(AND_1, PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(12032899)
def Event_12032899():
    """Event 12032899"""
    RunCommonEvent(0, 12032896, args=(12030850, 12032860, 12032856), arg_types="III")
    RunCommonEvent(
        0,
        9005822,
        args=(12030850, 451000, 12032860, 12032856, 12030852, 12032852, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(12032861)
def Event_12032861():
    """Event 12032861"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(AND_1, 20000, 14898)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 20000, 14899)
    IfEntityWithinDistance(AND_1, entity=12030850, other_entity=20000, radius=15.0)
    IfCharacterHasSpecialEffect(AND_1, 12030850, 14896)
    IfCharacterAlive(AND_1, 12030850)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=3.0)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=20000, special_effect=14898)
    AddSpecialEffect(20000, 14899)
    ShootProjectile(
        owner_entity=12030850,
        source_entity=12030850,
        model_point=900,
        behavior_id=1131,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitRandomSeconds(min_seconds=2.0, max_seconds=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(12032862)
def Event_12032862():
    """Event 12032862"""
    IfCharacterHasSpecialEffect(MAIN, 12030850, 14875)
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=0)
    EnableFlag(12032852)
    Wait(7.0)
    IfHealthEqual(OR_10, 12030850, value=0.0)
    SkipLinesIfConditionTrue(2, OR_10)
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=1)
    Goto(Label.L0)
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(12030700)
def Event_12030700(_, character: uint):
    """Event 12030700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4120)
    DisableFlag(12039152)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L8, flag=4128)
    GotoIfFlagEnabled(Label.L9, flag=4129)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(4128, 4129))
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=4120)
    GotoIfFlagEnabled(Label.L1, flag=4121)
    GotoIfFlagEnabled(Label.L3, flag=4123)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 90103, unknown2=1.0)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(4128, 4129))
    Restart()


@RestartOnRest(12030701)
def Event_12030701(_, character: uint, obj: uint):
    """Event 12030701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L9, flag=4130)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(MAIN, 4130)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90104, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4130)
    Restart()


@RestartOnRest(12030702)
def Event_12030702(_, character: uint):
    """Event 12030702"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L10, flag=4131)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4131)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90106, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4131)
    Restart()


@RestartOnRest(12030703)
def Event_12030703(_, character: uint, obj: uint, obj_1: uint):
    """Event 12030703"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L11, flag=4132)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    DisableObject(obj_1)
    IfFlagEnabled(MAIN, 4132)
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(obj)
    EnableObject(obj_1)
    ForceAnimation(character, 90106, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4132)
    Restart()


@RestartOnRest(12030704)
def Event_12030704():
    """Event 12030704"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12030800)
    IfFlagEnabled(AND_1, 12030800)
    IfFlagEnabled(AND_1, 4127)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(4138)


@RestartOnRest(12030705)
def Event_12030705():
    """Event 12030705"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12030850)
    IfFlagEnabled(AND_1, 12032870)
    IfFlagEnabled(AND_1, 4130)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(4138)


@RestartOnRest(12030706)
def Event_12030706():
    """Event 12030706"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12030850)
    IfFlagEnabled(OR_1, 4130)
    IfFlagEnabled(OR_1, 4137)
    IfFlagEnabled(AND_1, 12030850)
    IfFlagDisabled(AND_1, 12032870)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(4138)


@RestartOnRest(12030707)
def Event_12030707():
    """Event 12030707"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(12032720)
    IfFlagEnabled(MAIN, 12032720)
    ForceAnimation(PLAYER, 90207, wait_for_completion=True, unknown2=1.0)
    EnableFlag(12032721)
    Restart()


@RestartOnRest(12030708)
def Event_12030708(_, entity: uint):
    """Event 12030708"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(12032723)
    IfFlagEnabled(MAIN, 12032723)
    ForceAnimation(entity, 90208, wait_for_completion=True, unknown2=1.0)
    EnableFlag(12032724)
    Restart()


@RestartOnRest(12030709)
def Event_12030709(_, flag: uint):
    """Event 12030709"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(MAIN, flag)
    IfFlagEnabled(MAIN, flag)
    DisableNetworkConnectedFlagRange(flag_range=(4120, 4124))
    EnableNetworkFlag(4120)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4130)
    IfFlagDisabled(MAIN, flag)
    DisableNetworkConnectedFlagRange(flag_range=(4120, 4137))
    EnableFlag(4138)
    Restart()


@RestartOnRest(12030710)
def Event_12030710(_, character: uint):
    """Event 12030710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4060)
    DisableFlag(12039002)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4066)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4066)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L0, flag=4060)
    GotoIfFlagEnabled(Label.L1, flag=4061)
    GotoIfFlagEnabled(Label.L3, flag=4063)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90102, unknown2=1.0)
    SetCharacterTalkRange(character=character, distance=100.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4066)
    Restart()


@RestartOnRest(12030720)
def Event_12030720(_, character: uint):
    """Event 12030720"""
    WaitFrames(frames=1)
    ForceAnimation(character, 930013, unknown2=1.0)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAnimations(character)
    EndIfPlayerNotInOwnWorld()
    EnableImmortality(character)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    ForceAnimation(character, 20025, unknown2=1.0)
    DisableAnimations(character)
    Wait(10.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()
