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
    RegisterGrace(grace_flag=11100000, obj=11101950, unknown=1.0)
    Event_11100020()
    Event_11100030()
    Event_11100031()
    RunCommonEvent(
        0,
        90005790,
        args=(0, 11100180, 11102180, 11102181, 11100785, 23, 11102385, 11102386, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(11100180, 11102180, 11102181, 11100785), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(11100180, 11102180, 11102181, 11100785, 11100800, 0.0), arg_types="IIIIif")
    Event_11102600()
    Event_11102602()
    Event_11102605()
    Event_11102606()
    Event_11102620(
        0,
        flag=11100180,
        left_flag=11102621,
        cancel_flag__right_flag=11102622,
        obj=11101620,
        player_start=11102620,
        area_id=11,
        block_id=10,
        cc_id=0,
        dd_id=0
    )
    RunCommonEvent(
        0,
        90005620,
        args=(11100570, 11101570, 11101571, 0, 11102570, 11102571, 11102572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(11100570, 11101573), arg_types="II")
    RunCommonEvent(
        0,
        90005620,
        args=(11100575, 11101575, 11101576, 11101577, 11102575, 11102576, 11102577),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(11100575, 11101578), arg_types="II")
    Event_11102680()
    Event_11103700(0, character=11100715)
    RunCommonEvent(0, 11103702)
    RunCommonEvent(0, 11103703)
    Event_11103705(0, character=11100705)
    RunCommonEvent(0, 90005708, args=(11100705, 3480, 0), arg_types="III")
    Event_11103706(0, entity=11100720)
    Event_11103707(0, entity=11100720)
    RunCommonEvent(0, 90005708, args=(11100705, 11109355, 0), arg_types="III")
    Event_11103710(0, character=11100710)
    Event_11103711(0, character=11100711)
    Event_11103712(0, character=11100712)
    Event_11103713()
    Event_11103714(0, entity=11100711)
    Event_11100704()
    Event_11103715(0, character=11100725)
    Event_11103716(0, character=11100726)
    Event_11103720(0, character=11100730)
    Event_11100730(0, character=11100735, obj=11101730)
    Event_11100731(0, character=11100736, obj=11101717, entity=11101562)
    Event_11100732()
    RunCommonEvent(0, 90005708, args=(11100735, 4110, 0), arg_types="III")
    RunCommonEvent(0, 90005750, args=(11101716, 4110, 103400, 400349, 400349, 4048, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005775, args=(81463900, 1045399206, -1.0), arg_types="iIf")
    Event_11100735(0, character=11100740)
    Event_11100736(0, character=11100741)
    RunCommonEvent(
        0,
        90005740,
        args=(
            11102845,
            11102846,
            11102847,
            11100740,
            702,
            11101741,
            702,
            0.4000000059604645,
            90300,
            90302,
            -1,
            1.2999999523162842,
        ),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(
        0,
        90005741,
        args=(11102848, 11102849, 11102847, 11100740, 90320, 0, 90322, -1, 0.5),
        arg_types="IIIIiIiif",
    )
    Event_11100737(0, entity=11100741)
    RunCommonEvent(0, 90005733, args=(11102844,))
    Event_11100750(0, character=11100755, obj=11101715)
    RunCommonEvent(0, 90005708, args=(11100755, 3900, 0), arg_types="III")
    RunCommonEvent(0, 90005708, args=(11100755, 3903, 0), arg_types="III")
    RunCommonEvent(0, 90005750, args=(11101755, 4110, 103590, 400359, 400359, 3909, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(11101755, 4110, 103580, 400356, 400358, 400359, 0), arg_types="IiiIIIi")
    Event_11100740(0, character=11100750)
    Event_11100741(0, character=11100751)
    RunCommonEvent(0, 90005775, args=(85495300, 11109687, -1.0), arg_types="iIf")
    Event_11100745(0, character=11100770)
    Event_11100755(0, character=11100745)
    Event_11100756(0, character=11100746)
    Event_11100760(0, character=11100780)
    Event_11100761(0, character=11100781)
    Event_11100765(0, character=11100765)
    RunCommonEvent(0, 90005774, args=(11109656, 11100900, 11107900), arg_types="IiI")
    RunCommonEvent(0, 90005750, args=(11101765, 4110, 104900, 400490, 400490, 11109656, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 11103770)
    RunCommonEvent(0, 11103771)
    RunCommonEvent(0, 11103772)
    Event_11103775()
    Event_11100790()
    Event_11100791(0, flag=400282, flag_1=11109770)
    Event_11100791(1, flag=400283, flag_1=11109771)
    Event_11100791(2, flag=68210, flag_1=11109772)
    Event_11100791(3, flag=400285, flag_1=11109773)
    Event_11100795()
    Event_11100796()
    Event_11100797()
    Event_11102651(0, flag=710700, tutorial_param_id=1700, item=9125, flag_1=69250)
    Event_11102650(0, flag=710720, tutorial_param_id=1720, item=9128, flag_1=69280)
    Event_11102652(0, 710780, 1780, 9132, 69320)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(11100705)
    DisableBackread(11100710)
    DisableBackread(11100711)
    DisableBackread(11100715)
    DisableBackread(11100725)
    DisableBackread(11100726)
    DisableBackread(11100735)
    DisableBackread(11100736)
    DisableBackread(11100740)
    DisableBackread(11100741)
    DisableBackread(11100745)
    DisableBackread(11100746)
    DisableBackread(11100750)
    DisableBackread(11100751)
    DisableBackread(11100755)
    DisableBackread(11100765)
    DisableBackread(11100766)
    DisableBackread(11100770)
    DisableBackread(11100780)
    DisableBackread(11100781)
    DisableBackread(11100785)
    EnableObjectInvulnerability(11101715)
    EnableObjectInvulnerability(11101730)
    Event_11002548()
    Event_11100680()
    Event_11102100()


@NeverRestart(11100020)
def Event_11100020():
    """Event 11100020"""
    EndIfThisEventSlotFlagEnabled()
    IfPlayerInOwnWorld(AND_1)
    IfInsideMap(AND_1, game_map=ROUNDTABLE_HOLD)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(71190)
    Unknown_2003_78(unk_0_4=111000, unk_4_8=100.0)
    EnableFlag(105)


@RestartOnRest(11100030)
def Event_11100030():
    """Event 11100030"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 3001)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30)


@NeverRestart(11100031)
def Event_11100031():
    """Event 11100031"""
    EndIfFlagDisabled(120)
    EndIfFlagEnabled(121)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 120)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(71900)
    EnableFlag(121)


@NeverRestart(11102100)
def Event_11102100():
    """Event 11102100"""
    GotoIfFlagEnabled(Label.L1, flag=302)
    GotoIfFlagDisabled(Label.L0, flag=300)
    Unknown_2003_68(unknown1=12, unknown2=-1.0, unknown3=1)
    DeleteVFX(11102100, erase_root_only=False)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Unknown_2003_68(unknown1=5, unknown2=-1.0, unknown3=1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(11102101, erase_root_only=False)
    DeleteVFX(11102110, erase_root_only=False)
    DeleteVFX(11102111, erase_root_only=False)
    DeleteVFX(11102112, erase_root_only=False)
    DeleteVFX(11102113, erase_root_only=False)
    DeleteVFX(11102114, erase_root_only=False)
    DeleteVFX(11102115, erase_root_only=False)
    DeleteVFX(11102116, erase_root_only=False)
    DeleteVFX(11102117, erase_root_only=False)
    DeleteVFX(11102118, erase_root_only=False)
    DeleteVFX(11102119, erase_root_only=False)
    DeleteVFX(11102120, erase_root_only=False)
    DeleteVFX(11102121, erase_root_only=False)
    DeleteVFX(11102122, erase_root_only=False)
    DeleteVFX(11102123, erase_root_only=False)
    DeleteVFX(11102124, erase_root_only=False)
    DeleteVFX(11102125, erase_root_only=False)
    DeleteVFX(11102126, erase_root_only=False)
    DeleteVFX(11102127, erase_root_only=False)
    DeleteVFX(11102128, erase_root_only=False)
    DeleteVFX(11102129, erase_root_only=False)
    DeleteVFX(11102130, erase_root_only=False)
    DeleteVFX(11102131, erase_root_only=False)
    DeleteVFX(11102132, erase_root_only=False)
    DeleteVFX(11102133, erase_root_only=False)
    DeleteVFX(11102134, erase_root_only=False)
    DeleteVFX(11102135, erase_root_only=False)
    DeleteVFX(11102136, erase_root_only=False)
    DeleteVFX(11102137, erase_root_only=False)
    DeleteVFX(11102138, erase_root_only=False)
    DeleteVFX(11102139, erase_root_only=False)
    DeleteVFX(11102140, erase_root_only=False)
    DeleteVFX(11102141, erase_root_only=False)
    DeleteVFX(11102142, erase_root_only=False)
    DeleteVFX(11102143, erase_root_only=False)
    DeleteVFX(11102144, erase_root_only=False)
    DeleteVFX(11102145, erase_root_only=False)
    DeleteVFX(11102146, erase_root_only=False)
    DeleteVFX(11102147, erase_root_only=False)
    End()


@RestartOnRest(11002548)
def Event_11002548():
    """Event 11002548"""
    EndIfFlagEnabled(11108548)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 181)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(11108548)


@RestartOnRest(11102600)
def Event_11102600():
    """Event 11102600"""
    DisableNetworkSync()
    CancelSpecialEffect(PLAYER, 9621)
    IfInsideMap(AND_1, game_map=ROUNDTABLE_HOLD)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=11102600)
    IfUnknownCondition_35(AND_1, unk_1_2=0, unk_4_8=20)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 9621)
    Wait(1.0)
    IfInsideMap(AND_2, game_map=ROUNDTABLE_HOLD)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=11102600)
    IfUnknownCondition_35(AND_2, unk_1_2=0, unk_4_8=20)
    IfConditionFalse(MAIN, input_condition=AND_2)
    Restart()


@RestartOnRest(11102602)
def Event_11102602():
    """Event 11102602"""
    EndIfOutsideMap(game_map=ROUNDTABLE_HOLD)
    Unknown_2003_76(
        unk_0_4=168493312,
        unk_4_8=0,
        unk_8_12=-305.70001220703125,
        unk_12_16=-20.579999923706055,
        unk_16_20=-298.1000061035156,
    )


@RestartOnRest(11102605)
def Event_11102605():
    """Event 11102605"""
    AwaitFlagEnabled(flag=3063)
    EndOfAnimation(obj=11101560, animation_id=2)
    End()


@RestartOnRest(11102606)
def Event_11102606():
    """Event 11102606"""
    IfFlagEnabled(AND_1, 11109659)
    IfFlagEnabled(AND_1, 3966)
    IfFlagEnabled(AND_2, 11109358)
    IfFlagEnabled(AND_2, 11109660)
    IfFlagEnabled(AND_2, 3967)
    IfFlagEnabled(AND_3, 110)
    IfFlagEnabled(AND_3, 3967)
    IfFlagEnabled(OR_1, 11109358)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=AND_3)
    AwaitConditionTrue(OR_1)
    EndOfAnimation(obj=11101750, animation_id=2)
    End()


@NeverRestart(11102620)
def Event_11102620(
    _,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    obj: uint,
    player_start: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
):
    """Event 11102620"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(obj, vfx_id=190, model_point=1300)
    IfTryingToJoinSession(OR_2)
    IfTryingToCreateSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9290, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisplayDialogAndSetFlags(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(PLAYER, 11101620, wait_for_completion=True)
    ForceAnimation(PLAYER, 60460, unknown2=1.0)
    Wait(2.5)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unknown1=-11100)


@RestartOnRest(11102650)
def Event_11102650(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 11102650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 104)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(11102651)
def Event_11102651(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 11102651"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 105)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(11102652)
def Event_11102652(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 11102652"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, flag)
    IfInsideMap(AND_1, game_map=ROUNDTABLE_HOLD)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(2.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@NeverRestart(11100680)
def Event_11100680():
    """Event 11100680"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EndIfFlagEnabled(11109656)
    DisableHealthBar(11100140)
    UnknownMap_11(unk_0_4=1, unk_4_8=0.0)
    SetTeamType(11100766, TeamType.Enemy)
    EndOfAnimation(obj=1110548, animation_id=0)
    IfCharacterDead(AND_1, 11100766)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(11109656)
    DisplayBanner(BannerType.Unknown)
    DisableFlag(1035429211)
    Unknown_2003_77(entity_id=11102766)
    AddSpecialEffect(20000, 4820)
    Unknown_2003_74(unk_0_4=1)


@NeverRestart(11102680)
def Event_11102680():
    """Event 11102680"""
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=False,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    EndIfFlagEnabled(11109656)
    EnableBackread(11100766)
    DisableAI(11100766)
    IfCharacterOutsideRegion(OR_1, character=PLAYER, region=11102681)
    IfTimeElapsed(OR_1, seconds=5.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=11100766, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_1, character=11000766, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=11000766, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=11000766, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=11000766, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableAI(11100766)


@RestartOnRest(11103700)
def Event_11103700(_, character: uint):
    """Event 11103700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3220)
    DisableFlag(11009248)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(11101740)
    DisableObject(11101742)
    IfFlagEnabled(OR_1, 3225)
    IfFlagEnabled(OR_1, 3226)
    IfFlagEnabled(OR_1, 3227)
    IfFlagEnabled(OR_1, 3228)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3225)
    IfFlagEnabled(OR_2, 3226)
    IfFlagEnabled(OR_2, 3227)
    IfFlagEnabled(OR_2, 3228)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()
    SetCharacterTalkRange(character=character, distance=50.0)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3220)
    GotoIfFlagEnabled(Label.L2, flag=3221)
    GotoIfFlagEnabled(Label.L4, flag=3223)

    # --- Label 1 --- #
    DefineLabel(1)
    IfUnknownCondition_35(AND_5, unk_1_2=1, unk_4_8=20)
    IfFlagEnabled(AND_5, 1035429211)
    SkipLinesIfConditionTrue(6, AND_5)
    DeleteObjectVFX(11101702)
    CreateObjectVFX(11101702, vfx_id=100, model_point=803450)
    SkipLinesIfFlagDisabled(1, 110)
    EnableObject(11101742)
    SkipLinesIfFlagEnabled(1, 110)
    EnableObject(11101740)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    IfFlagEnabled(AND_10, 3225)
    IfFlagEnabled(AND_10, 11109205)
    IfFlagDisabled(AND_10, 11109209)
    IfFlagEnabled(AND_10, 11109206)
    SkipLinesIfConditionFalse(1, AND_10)
    ForceAnimation(character, 930013, unknown2=1.0)
    IfFlagEnabled(AND_11, 3225)
    IfFlagEnabled(AND_11, 11109209)
    IfFlagDisabled(AND_11, 11109339)
    IfFlagEnabled(AND_11, 11109340)
    SkipLinesIfConditionFalse(1, AND_11)
    ForceAnimation(character, 930015, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 920015, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_3, 3225)
    IfFlagEnabled(OR_3, 3226)
    IfFlagEnabled(OR_3, 3227)
    IfFlagEnabled(OR_3, 3228)
    IfConditionFalse(MAIN, input_condition=OR_3)
    Restart()


@RestartOnRest(11103702)
def Event_11103702():
    """Event 11103702"""
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=11102700)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=11100715, radius=8.0)
    IfFlagEnabled(AND_1, 3225)
    IfFlagEnabled(AND_1, 11109205)
    IfFlagDisabled(AND_1, 11102702)
    IfFlagDisabled(AND_1, 11109209)
    IfFlagEnabled(AND_1, 11109206)
    IfConditionTrue(AND_1, input_condition=OR_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11102704)
    End()


@RestartOnRest(11103703)
def Event_11103703():
    """Event 11103703"""
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=11102700)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=11100715, radius=8.0)
    IfFlagEnabled(AND_1, 3225)
    IfFlagEnabled(AND_1, 11109205)
    IfFlagDisabled(AND_1, 11102702)
    IfFlagEnabled(AND_1, 11109209)
    IfFlagDisabled(AND_1, 11109339)
    IfFlagEnabled(AND_1, 11109340)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(11102708)
    End()


@RestartOnRest(11100704)
def Event_11100704():
    """Event 11100704"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11109213)
    IfFlagEnabled(MAIN, 11109213)
    EnableFlag(10007450)
    DisableFlag(10007452)


@RestartOnRest(11103705)
def Event_11103705(_, character: uint):
    """Event 11103705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3480)
    DisableFlag(11109355)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=3489)
    IfFlagEnabled(OR_1, 3485)
    IfFlagEnabled(OR_1, 3486)
    IfFlagEnabled(OR_1, 3487)
    IfFlagEnabled(OR_1, 3488)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3485)
    IfFlagEnabled(OR_3, 3486)
    IfFlagEnabled(OR_3, 3487)
    IfFlagEnabled(OR_3, 3488)
    IfFlagEnabled(OR_3, 3489)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3480)
    GotoIfFlagEnabled(Label.L2, flag=3481)
    GotoIfFlagEnabled(Label.L3, flag=3482)
    GotoIfFlagEnabled(Label.L4, flag=3483)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3485)
    IfFlagEnabled(OR_4, 3486)
    IfFlagEnabled(OR_4, 3487)
    IfFlagEnabled(OR_4, 3488)
    IfFlagEnabled(OR_4, 3489)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(11103706)
def Event_11103706(_, entity: uint):
    """Event 11103706"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(60843)
    IfActionButtonParamActivated(MAIN, action_button_id=6321, entity=entity)
    EnableFlag(60843)
    Unknown_2003_71(unk_0_4=102)
    End()


@RestartOnRest(11103707)
def Event_11103707(_, entity: uint):
    """Event 11103707"""
    ForceAnimation(entity, 930001, unknown2=1.0)
    WaitFrames(frames=1)
    EndIfFlagEnabled(3485)
    EndIfFlagEnabled(3486)
    ForceAnimation(entity, 930000, unknown2=1.0)
    End()


@RestartOnRest(11103710)
def Event_11103710(_, character: uint):
    """Event 11103710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3707)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_2, 3707)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3707)
    Restart()


@RestartOnRest(11103711)
def Event_11103711(_, character: uint):
    """Event 11103711"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3708)
    IfFlagEnabled(AND_1, 3709)
    IfFlagEnabled(AND_1, 11109279)
    IfConditionTrue(OR_1, input_condition=AND_1)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_5, 3709)
    IfFlagDisabled(AND_5, 11109279)
    SkipLinesIfConditionTrue(1, AND_5)
    DisableObject(11101720)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(11101720)
    ForceAnimation(character, 90104, unknown2=1.0)
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
    IfFlagDisabled(AND_15, 3708)
    IfFlagDisabled(AND_15, 3709)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(11103712)
def Event_11103712(_, character: uint):
    """Event 11103712"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 3709)
    IfFlagDisabled(AND_1, 11109279)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103, unknown2=1.0)
    EnableNetworkFlag(11102719)
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
    IfFlagDisabled(MAIN, 3709)
    Restart()


@RestartOnRest(11103713)
def Event_11103713():
    """Event 11103713"""
    EndIfFlagEnabled(11109266)
    AwaitFlagEnabled(flag=1041389415)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=10903, flag=1041389417, bit_count=10)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=10913, flag=1041389427, bit_count=10)
    DisableFlag(1041389415)
    EnableFlag(1041389416)
    Restart()


@RestartOnRest(11103714)
def Event_11103714(_, entity: uint):
    """Event 11103714"""
    EndIfFlagDisabled(11109265)
    IfFlagEnabled(AND_1, 11109266)
    IfFlagDisabled(AND_1, 11109267)
    EndIfConditionTrue(input_condition=AND_1)
    EndIfFlagDisabled(1041389411)
    IfFlagEnabled(AND_2, 3063)
    IfFlagDisabled(AND_2, 11109268)
    EndIfConditionTrue(input_condition=AND_2)
    IfFlagEnabled(AND_3, 11109268)
    IfFlagDisabled(AND_3, 35009306)
    EndIfConditionTrue(input_condition=AND_3)
    IfFlagEnabled(AND_4, 11109268)
    IfFlagEnabled(AND_4, 4247)
    IfFlagDisabled(AND_4, 11109270)
    EndIfConditionTrue(input_condition=AND_4)
    IfFlagEnabled(AND_5, 11109268)
    IfFlagEnabled(AND_5, 4248)
    IfFlagDisabled(AND_5, 11109272)
    EndIfConditionTrue(input_condition=AND_5)
    IfFlagEnabled(AND_6, 11109272)
    IfFlagEnabled(AND_6, 4249)
    IfFlagDisabled(AND_6, 11109271)
    EndIfConditionTrue(input_condition=AND_6)
    IfFlagEnabled(AND_10, 3708)
    IfCharacterInsideRegion(AND_10, character=PLAYER, region=11102700)
    IfFlagEnabled(AND_11, 3709)
    IfFlagEnabled(AND_11, 11109279)
    IfCharacterInsideRegion(AND_11, character=PLAYER, region=11102700)
    IfConditionTrue(OR_10, input_condition=AND_10)
    IfConditionTrue(OR_10, input_condition=AND_11)
    AwaitConditionTrue(OR_10)
    EnableRandomFlagInRange(flag_range=(11102710, 11102716))
    GotoIfFlagEnabled(Label.L1, flag=11102710)
    GotoIfFlagEnabled(Label.L2, flag=11102711)
    GotoIfFlagEnabled(Label.L3, flag=11102712)
    GotoIfFlagRangeAnyEnabled(Label.L20, flag_range=(11102713, 11102716))

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(entity, 90202, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(entity, 90203, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(entity, 90204, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(11103715)
def Event_11103715(_, character: uint):
    """Event 11103715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3440)
    IfFlagEnabled(AND_1, 11109405)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3445)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(MAIN, 3445)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagDisabled(MAIN, 3445)
    Restart()


@RestartOnRest(11103716)
def Event_11103716(_, character: uint):
    """Event 11103716"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3440)
    IfFlagEnabled(AND_1, 11109405)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3447)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(MAIN, 3447)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagDisabled(MAIN, 3447)
    Restart()


@RestartOnRest(11103720)
def Event_11103720(_, character: uint):
    """Event 11103720"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(11100730)
def Event_11100730(_, character: uint, obj: uint):
    """Event 11100730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=4047)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)
    DisableObject(obj)
    IfFlagEnabled(MAIN, 4047)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableCharacter(character)
    EnableBackread(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    EnableObject(obj)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4047)
    Restart()


@RestartOnRest(11100731)
def Event_11100731(_, character: uint, obj: uint, entity: uint):
    """Event 11100731"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L8, flag=4048)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(MAIN, 4048)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    ForceAnimation(entity, 2, unknown2=1.0)
    GotoIfFlagRangeAllEnabled(Label.L3, flag_range=(400349, 400349))
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    ForceAnimation(character, 90104, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4048)
    Restart()


@RestartOnRest(11100732)
def Event_11100732():
    """Event 11100732"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11109609)
    IfFlagEnabled(MAIN, 4046)
    EnableFlag(11109609)
    EnableFlag(4058)


@RestartOnRest(11100735)
def Event_11100735(_, character: uint):
    """Event 11100735"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=4125)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4125)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4125)
    Restart()


@RestartOnRest(11100736)
def Event_11100736(_, character: uint):
    """Event 11100736"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4126)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4126)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4126)
    Restart()


@RestartOnRest(11100737)
def Event_11100737(_, entity: uint):
    """Event 11100737"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 4126)
    IfFlagEnabled(AND_1, 11109015)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 90207, unknown2=1.0)


@RestartOnRest(11100740)
def Event_11100740(_, character: uint):
    """Event 11100740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3965)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3965)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3960)
    GotoIfFlagEnabled(Label.L2, flag=3961)
    GotoIfFlagEnabled(Label.L4, flag=3963)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3965)
    Restart()


@RestartOnRest(11100741)
def Event_11100741(_, character: uint):
    """Event 11100741"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3966)
    IfFlagEnabled(OR_1, 3967)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_2, 3966)
    IfFlagEnabled(OR_2, 3967)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3960)
    GotoIfFlagEnabled(Label.L2, flag=3961)
    GotoIfFlagEnabled(Label.L4, flag=3963)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
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
    IfFlagDisabled(AND_1, 3966)
    IfFlagDisabled(AND_1, 3967)
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(11100745)
def Event_11100745(_, character: uint):
    """Event 11100745"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4205)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(MAIN, 4205)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagDisabled(MAIN, 4205)
    Restart()


@RestartOnRest(11100750)
def Event_11100750(_, character: uint, obj: uint):
    """Event 11100750"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 11109527)
    EnableFlag(11109529)
    SkipLinesIfFlagDisabled(1, 11109535)
    IncrementEventValue(11109545, bit_count=5, max_value=2)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3907)
    GotoIfFlagEnabled(Label.L8, flag=3908)
    GotoIfFlagEnabled(Label.L9, flag=3909)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)
    DisableObject(obj)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3907, 3909))
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3907)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 9 --- #
    DefineLabel(9)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SkipLinesIfFlagEnabled(1, 11109522)
    EnableFlag(400356)
    GotoIfFlagRangeAllEnabled(Label.L3, flag_range=(400356, 400359))
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90106, unknown2=1.0)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3908, 3909))
    Restart()


@RestartOnRest(11100755)
def Event_11100755(_, character: uint):
    """Event 11100755"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4245)
    IfFlagEnabled(AND_1, 4246)
    IfFlagDisabled(AND_1, 35009315)
    IfConditionTrue(OR_1, input_condition=AND_1)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 4245)
    IfFlagEnabled(AND_2, 4246)
    IfFlagDisabled(AND_2, 35009315)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 4245)
    IfFlagEnabled(AND_15, 4246)
    IfFlagDisabled(AND_15, 35009315)
    IfConditionTrue(OR_15, input_condition=AND_15)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(11100756)
def Event_11100756(_, character: uint):
    """Event 11100756"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4248)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(MAIN, 4248)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4248)
    Restart()


@RestartOnRest(11100760)
def Event_11100760(_, character: uint):
    """Event 11100760"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3966)
    IfFlagEnabled(OR_1, 3967)
    IfFlagEnabled(AND_1, 4226)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    IfFlagEnabled(AND_2, 4226)
    IfFlagEnabled(AND_2, 4223)
    GotoIfConditionTrue(Label.L4, input_condition=AND_2)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3966)
    IfFlagEnabled(OR_3, 3967)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfFlagEnabled(AND_3, 4226)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
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
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3966)
    IfFlagEnabled(OR_15, 3967)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, 4226)
    IfConditionFalse(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(11100761)
def Event_11100761(_, character: uint):
    """Event 11100761"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4228)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4228)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 4228)
    Restart()


@RestartOnRest(11100765)
def Event_11100765(_, character: uint):
    """Event 11100765"""
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 110)
    IfFlagEnabled(OR_1, 11109656)
    AwaitConditionFalse(OR_1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    End()


@RestartOnRest(11103770)
def Event_11103770():
    """Event 11103770"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 11109340)
    IfFlagEnabled(AND_1, 11109558)
    EndIfConditionTrue(input_condition=AND_1)
    IfFlagRangeAnyEnabled(OR_1, flag_range=(71100, 71108))
    IfFlagRangeAnyEnabled(OR_1, flag_range=(73500, 73504))
    AwaitConditionTrue(OR_1)
    EnableNetworkFlag(11109340)
    EnableNetworkFlag(11109558)
    End()


@RestartOnRest(11103771)
def Event_11103771():
    """Event 11103771"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11109559)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(71500, 71508))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109559)
    End()


@RestartOnRest(11103772)
def Event_11103772():
    """Event 11103772"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11109560)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(71250, 71253))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109560)
    End()


@NeverRestart(11103775)
def Event_11103775():
    """Event 11103775"""
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagDisabled(2, 11109786)
    DisableFlag(11109786)
    End()
    ReturnIfUnknown_208(
        return_type=EventReturnType.End,
        state=True,
        unk_2_3=0,
        unk_3_2=0,
        unk_4_3=20,
        unk_5_4=0,
        unk_6_5=0,
    )
    IfEntityWithinDistance(AND_15, entity=PLAYER, other_entity=11102020, radius=1.0)
    EndIfConditionFalse(input_condition=AND_15)
    Wait(0.10000000149011612)
    IfFlagEnabled(AND_1, 1034509254)
    IfFlagEnabled(AND_2, 11109785)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    DisableFlag(11109785)
    DisplayDialog(text=30120, anchor_entity=0, display_distance=5.0, number_buttons=NumberButtons.OneButton)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(1034509254)
    DisplayDialog(text=30130, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    End()


@RestartOnRest(11100790)
def Event_11100790():
    """Event 11100790"""
    EndIfPlayerNotInOwnWorld()
    EnableNetworkFlag(11102790)
    End()


@RestartOnRest(11100791)
def Event_11100791(_, flag: uint, flag_1: uint):
    """Event 11100791"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(OR_1, 3968)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SkipLinesIfFlagDisabled(3, 3968)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag_1)
    EnableFlag(11109785)
    End()


@RestartOnRest(11100795)
def Event_11100795():
    """Event 11100795"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9614)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9615)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 60540, unknown2=1.0)
    Wait(0.20000000298023224)
    Restart()


@NeverRestart(11100796)
def Event_11100796():
    """Event 11100796"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(182)
    IfFlagDisabled(AND_1, 60020)
    IfFlagDisabled(AND_1, 11109774)
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(11109774)
    EnableFlag(11109785)
    IfFlagDisabled(AND_2, 60120)
    IfFlagDisabled(AND_2, 11109775)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(11109775)
    EnableFlag(11109785)
    IfFlagDisabled(AND_3, 60130)
    IfFlagDisabled(AND_3, 11109776)
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(11109776)
    EnableFlag(11109785)
    End()


@NeverRestart(11100797)
def Event_11100797():
    """Event 11100797"""
    EndIfPlayerNotInOwnWorld()
    WaitFramesAfterCutscene(frames=1)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3487, 3489))
    IfFlagDisabled(AND_1, 60500)
    IfFlagDisabled(AND_1, 11109777)
    EndIfConditionFalse(input_condition=AND_1)
    EnableFlag(11109777)
    EnableFlag(11109785)
    End()
