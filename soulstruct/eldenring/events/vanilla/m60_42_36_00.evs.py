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
    RegisterGrace(grace_flag=1042360000, obj=1042361950, unknown=5.0)
    RegisterGrace(grace_flag=1042360001, obj=1042361951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(71001, 76100, 1042361980, 77100, 1, 78100, 78101, 78102, 78103, 78104, 78105, 78106, 78107, 78108, 78109),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005100,
        args=(71001, 76101, 1042361981, 77100, 0, 78100, 78101, 78102, 78103, 78104, 78105, 78106, 78107, 78108, 78109),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005870, args=(1042360800, 903251600, 12), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1042360800, 0, 1042360800, 0, 30100, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1042360800, 12, 0), arg_types="III")
    RunCommonEvent(0, 90005683, args=(62103, 1042361684, 210, 78190, 78190), arg_types="IIiII")
    Event_1042363700(0, character=1042360700, obj=1042361701)
    RunCommonEvent(0, 90005704, args=(1042360700, 3181, 3180, 1042369201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1042360700, 3181, 3182, 1042369201, 3181, 3180, 3183, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1042360700, 3183, 3180, 3183), arg_types="IIII")
    RunCommonEvent(0, 1042363701)
    RunCommonEvent(0, 1042363702)
    RunCommonEvent(0, 1042363703)
    Event_1042360710(0, character=1042360730, obj=1042361711)
    RunCommonEvent(0, 90005704, args=(1042360730, 1042369401, 3746, 1042369401, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005709, args=(1042360730, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1042360730, 960, 603050), arg_types="Iii")
    Event_1042360711(0, character=1042360750)
    Event_1042360712(0, entity=1042360730, obj=1042361711)
    Event_1042360713(0, entity=1042360730, obj=1042361711, character=1042360750)
    RunCommonEvent(0, 90005750, args=(1042361710, 4350, 103900, 400390, 400390, 1042369413, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005708, args=(1042360730, 3746, 0), arg_types="III")
    Event_1042363720(0, character=1042360710, character_1=1042360711)
    RunCommonEvent(0, 90005704, args=(1042360710, 4701, 4700, 1042369301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1042360710, 4701, 4702, 1042369301, 4701, 4700, 4704, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1042360710, 4703, 4700, 4704), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1042360711, 4701, 4700, 1042369327, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1042360711, 4701, 4702, 1042369327, 4701, 4700, 4704, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005728, args=(1042360711, 1042362715, 1042362716), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4701, 1042360710, 1042360711, 4700, 4703), arg_types="IIIII")
    Event_1042360724(0, character=1042360710, character_1=1042360711)
    Event_1042363730(0, character=1042360720)
    Event_1042363740(0, flag=78100, other_entity=1042360951, flag_1=1042369450)
    Event_1042363741(0, flag=78101, other_entity=1042360950, flag_1=1042369452)
    Event_1042363742(0, other_entity=1042360951, flag=1042369450)
    Event_1042363743(0, other_entity=1042360951, flag=1042369451)
    Event_1042363744(0, other_entity=1042360950, flag=1042369452)
    Event_1042363745(0, other_entity=1042360950, flag=1042369453)
    Event_1042363746(0, other_entity=1042360951, flag=1042369451)
    Event_1042363747(0, other_entity=1042360950, flag=1042369453)
    Event_1042360750(0, character=1042360740)
    Event_1042362215(0, character=1042360215, region=1042362215)
    Event_1042362215(1, character=1042360216, region=1042362215)
    Event_1042362215(2, character=1042360217, region=1042362217)
    Event_1042362650(0, tutorial_param_id=1500, flag=710500, flag_1=69070)
    Event_1042362652(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370
    )
    Event_1042362656(0, tutorial_param_id=1740, flag=710740, flag_1=69310)
    Event_1042362660(0, 1730, 710730, 69300)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042360700)
    DisableBackread(1042360710)
    DisableBackread(1042360711)
    DisableBackread(1042360730)
    RunCommonEvent(0, 90005300, args=(1042360200, 1042365200, 0, 0.0, 0), arg_types="IIifi")


@RestartOnRest(1042362200)
def Event_1042362200(_, character: uint):
    """Event 1042362200"""
    EndIfFlagDisabled(1042360000)
    DisableCharacter(character)
    DisableAnimations(character)


@RestartOnRest(1042362215)
def Event_1042362215(_, character: uint, region: uint):
    """Event 1042362215"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    IfCharacterDead(AND_5, character)
    EndIfConditionTrue(input_condition=AND_5)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
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
    IfCharacterHasSpecialEffect(AND_10, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, character, 90162)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(OR_3, input_condition=AND_10)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    AddSpecialEffect(character, 8080)
    Wait(5.0)
    CancelSpecialEffect(character, 8080)


@RestartOnRest(1042362650)
def Event_1042362650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1042362650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1042362657)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9107, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042362652)
def Event_1042362652(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1042362652"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SE_SW)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_2)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1042362656)
def Event_1042362656(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1042362656"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1042362656)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9131, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1042362660)
def Event_1042362660(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1042362660"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 76100)
    IfFlagDisabled(AND_1, flag)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(3.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9130, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@NeverRestart(1042360684)
def Event_1042360684(_, anchor_entity: uint, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1042360684"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9260, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=4210, anchor_entity=anchor_entity)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    EnableFlag(flag)
    EnableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    End()


@RestartOnRest(1042360690)
def Event_1042360690(_, obj: uint, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint):
    """Event 1042360690"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag_2)
    DeleteObjectVFX(obj)
    DisableFlag(flag)
    DisableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateObjectVFX(obj, vfx_id=210, model_point=800530)
    EnableFlag(flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()


@RestartOnRest(1042363700)
def Event_1042363700(_, character: uint, obj: uint):
    """Event 1042363700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3180)
    DisableFlag(1042369205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3185)
    GotoIfFlagEnabled(Label.L5, flag=3187)
    GotoIfFlagEnabled(Label.L5, flag=3191)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 3185)
    IfFlagEnabled(OR_3, 3187)
    IfFlagEnabled(OR_3, 3191)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableObject(obj)
    GotoIfFlagEnabled(Label.L1, flag=3180)
    GotoIfFlagEnabled(Label.L2, flag=3181)
    GotoIfFlagEnabled(Label.L3, flag=3182)
    GotoIfFlagEnabled(Label.L4, flag=3183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
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
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3185)
    IfFlagEnabled(OR_4, 3187)
    IfFlagEnabled(OR_4, 3191)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1042363701)
def Event_1042363701():
    """Event 1042363701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    DisableFlag(1042369249)
    IfFlagEnabled(OR_1, 3188)
    IfFlagEnabled(OR_1, 3189)
    IfFlagEnabled(OR_1, 3190)
    EndIfConditionFalse(input_condition=OR_1)
    EndIfFlagDisabled(3180)
    EnableFlag(1042369249)
    End()


@RestartOnRest(1042363702)
def Event_1042363702():
    """Event 1042363702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, 3185)
    IfFlagDisabled(AND_1, 3187)
    EndIfConditionTrue(input_condition=AND_1)
    EndIfFlagDisabled(181)
    EnableFlag(3198)
    End()


@RestartOnRest(1042363703)
def Event_1042363703():
    """Event 1042363703"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(60826)
    IfFlagEnabled(MAIN, 400035)
    EnableFlag(60826)
    Unknown_2003_71(unk_0_4=60)
    End()


@RestartOnRest(1042360710)
def Event_1042360710(_, character: uint, obj: uint):
    """Event 1042360710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3746)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3746)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    UnknownTimer_04(
        hours=22,
        minutes=30,
        seconds=0,
        unknown1=0,
        unknown2=0,
        unknown3=0,
        unknown4=0,
        unknown5=0,
        unknown6=0,
    )
    CreateObjectVFX(obj, vfx_id=100, model_point=800227)
    UnknownCamera_4(unknown1=0.0, unknown2=-115.86000061035156)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableBackread(character)
    EnableCharacter(character)
    SetCharacterTalkRange(character=character, distance=30.0)
    EnableImmortality(character)
    ForceAnimation(character, 930000, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3746)
    Restart()


@RestartOnRest(1042360711)
def Event_1042360711(_, character: uint):
    """Event 1042360711"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 4680)
    IfFlagDisabled(AND_1, 9000)
    IfEntityWithinDistance(AND_1, entity=1042361950, other_entity=20000, radius=5.0)
    IfHealthValueGreaterThan(AND_1, character, value=0)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    EnableFlag(1042369411)
    EnableFlag(3758)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)
    End()


@RestartOnRest(1042360712)
def Event_1042360712(_, entity: uint, obj: uint):
    """Event 1042360712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042369410)
    IfFlagEnabled(AND_1, 1042369401)
    IfFlagEnabled(OR_1, 1042362732)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1042369415)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_1)
    EnableFlag(1042369410)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=1)
    IfFlagDisabled(MAIN, 1042362733)
    EnableFlag(1042362734)
    ForceAnimation(entity, 20013, unknown2=1.0)
    EnableFlag(4718)
    DeleteObjectVFX(obj)
    Wait(6.0)
    EnableFlag(1042369413)
    EnableFlag(3758)


@RestartOnRest(1042360713)
def Event_1042360713(_, entity: uint, obj: uint, character: uint):
    """Event 1042360713"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042369410)
    IfFlagEnabled(AND_1, 3746)
    IfTimeOfDay(AND_1, earliest=(20, 0, 0), latest=(5, 30, 0))
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfCharacterOutsideRegion(OR_2, character=20000, region=1042362710)
    IfTimeOfDay(OR_2, earliest=(5, 30, 0), latest=(20, 0, 0))
    IfUnknownCharacterCondition_28(OR_2, character=1, unk_8_12=31, unk_12_16=3)
    IfFlagDisabled(AND_2, 1042362733)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagEnabled(AND_3, 1042369410)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFinishedConditionTrue(input_condition=AND_3)
    DisableFlag(1042369415)
    ForceAnimation(entity, 20013, unknown2=1.0)
    DeleteObjectVFX(obj)
    EnableFlag(4718)
    Kill(character)
    Wait(6.0)
    EnableFlag(3758)


@RestartOnRest(1042363720)
def Event_1042363720(_, character: uint, character_1: uint):
    """Event 1042363720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4700)
    DisableFlag(1042369303)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4705)
    GotoIfFlagEnabled(Label.L17, flag=4717)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(OR_3, 4705)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4700)
    GotoIfFlagEnabled(Label.L2, flag=4701)
    GotoIfFlagEnabled(Label.L3, flag=4702)
    GotoIfFlagEnabled(Label.L4, flag=4703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character, 930003, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 4705)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()

    # --- Label 17 --- #
    DefineLabel(17)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character, TeamType.NoTeam)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character, 930011, unknown2=1.0)
    ForceAnimation(character_1, 930017, unknown2=1.0)
    IfFlagEnabled(OR_5, 4705)
    IfFlagEnabled(OR_5, 4717)
    IfConditionFalse(MAIN, input_condition=OR_5)
    Restart()


@RestartOnRest(1042363723)
def Event_1042363723(_, character: uint):
    """Event 1042363723"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4700)
    IfCharacterHasSpecialEffect(OR_1, character, 9603)
    IfCharacterHasSpecialEffect(OR_1, character, 9604)
    IfFlagEnabled(AND_1, 4701)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=9603)
    GotoIfCharacterHasSpecialEffect(Label.L4, character=character, special_effect=9604)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20009, unknown2=1.0)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(character, 20014, unknown2=1.0)
    End()


@NeverRestart(1042360724)
def Event_1042360724(_, character: uint, character_1: uint):
    """Event 1042360724"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042369410)
    IfFlagEnabled(AND_1, 4700)
    IfFlagEnabled(AND_1, 4717)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfFlagEnabled(MAIN, 4705)
    ForceAnimation(character, 20019, unknown2=1.0)
    ForceAnimation(character_1, 20017, unknown2=1.0)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)


@RestartOnRest(1042363730)
def Event_1042363730(_, character: uint):
    """Event 1042363730"""
    WaitFrames(frames=1)
    EnableBackread(character)
    EnableCharacter(character)
    WaitFrames(frames=1)
    ForceAnimation(character, 30021, unknown2=1.0)
    WaitFrames(frames=30)
    ForceAnimation(character, 30021, unknown2=1.0)


@RestartOnRest(1042363740)
def Event_1042363740(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1042363740"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372701)
    IfFlagDisabled(OR_1, flag)
    IfEntityBeyondDistance(OR_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1042363741)
def Event_1042363741(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1042363741"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372701)
    IfFlagDisabled(OR_1, flag)
    IfEntityBeyondDistance(OR_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1042363742)
def Event_1042363742(_, other_entity: uint, flag: uint):
    """Event 1042363742"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4680)
    IfFlagEnabled(MAIN, 4680)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363743)
def Event_1042363743(_, other_entity: uint, flag: uint):
    """Event 1042363743"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(MAIN, 1042379203)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363744)
def Event_1042363744(_, other_entity: uint, flag: uint):
    """Event 1042363744"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4680)
    IfFlagEnabled(MAIN, 4680)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363745)
def Event_1042363745(_, other_entity: uint, flag: uint):
    """Event 1042363745"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(MAIN, 1042379203)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042363746)
def Event_1042363746(_, other_entity: uint, flag: uint):
    """Event 1042363746"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379207)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372702)
    IfEntityBeyondDistance(MAIN, entity=20000, other_entity=other_entity, radius=5.0)
    DisableFlag(1042372702)
    Restart()


@RestartOnRest(1042363747)
def Event_1042363747(_, other_entity: uint, flag: uint):
    """Event 1042363747"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379207)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372702)
    IfEntityBeyondDistance(MAIN, entity=20000, other_entity=other_entity, radius=5.0)
    DisableFlag(1042372702)
    Restart()


@RestartOnRest(1042360750)
def Event_1042360750(_, character: uint):
    """Event 1042360750"""
    DisableGravity(character)
    DisableAnimations(character)
