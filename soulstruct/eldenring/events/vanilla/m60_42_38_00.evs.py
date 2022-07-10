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
    RegisterGrace(grace_flag=1042380000, obj=1042381950, unknown=5.0)
    RunCommonEvent(0, 90005860, args=(1042380800, 0, 1042380800, 0, 1042380400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(1042380800, 904980601, 24), arg_types="IiI")
    Event_1042382350()
    RunCommonEvent(0, 90005460, args=(1042380210,))
    RunCommonEvent(0, 90005461, args=(1042380210,))
    RunCommonEvent(0, 90005462, args=(1042380210,))
    RunCommonEvent(0, 90005760, args=(1042380850, 1042380850, 1042382360, 1042382718), arg_types="IIII")
    RunCommonEvent(0, 90005770, args=(1042380701,))
    RunCommonEvent(0, 90005860, args=(1042380850, 0, 1042380850, 0, 1042380410, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(1042380850, 903100600, 10), arg_types="IiI")
    RunCommonEvent(0, 90005872, args=(1042380850, 10, 0), arg_types="III")
    Event_1042383700(0, character=1042380710)
    RunCommonEvent(0, 90005704, args=(1042380710, 3881, 3880, 1042389251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1042380710, 3881, 3882, 1042389251, 3881, 3880, 3884, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1042380710, 3883, 3880, 3884), arg_types="IIII")
    RunCommonEvent(0, 90005630, args=(61423800, 1042381500, 127), arg_types="IIi")
    RunCommonEvent(0, 90005560, args=(1042380600, 1042381600, 0), arg_types="IIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042380710)
    RunCommonEvent(0, 90005251, args=(1042380220, 40.0, 0.0, 3011), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1042380240, 1042382240, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380241, 1042382240, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380242, 1042382240, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380243, 1042382240, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380254, 1042382254, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380255, 1042382254, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380256, 1042382254, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380262, 1042382254, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042380263, 1042382254, 1.0, 0.0, -1), arg_types="IIffi")
    Event_1042382300()
    RunCommonEvent(
        0,
        90005211,
        args=(1042380800, 30000, 20000, 1042382340, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@NeverRestart(200)
def Event_200():
    """Event 200"""
    Event_1042382290()


@RestartOnRest(1042382290)
def Event_1042382290():
    """Event 1042382290"""
    DisableNetworkSync()
    EndIfCharacterInsideRegion(character=PLAYER, region=1043392396)
    GotoIfFlagEnabled(Label.L0, flag=1042372800)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382290)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382291)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382292)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382293)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382294)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382295)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382296)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382297)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1042382298)
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4211)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(1.0)
    Restart()


@RestartOnRest(1042382300)
def Event_1042382300():
    """Event 1042382300"""
    DropMandatoryTreasure(1042385200)


@RestartOnRest(1042382340)
def Event_1042382340(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 1042382340"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfTimeOfDay(AND_3, earliest=(20, 0, 0), latest=(5, 0, 0))
    IfConditionTrue(AND_1, input_condition=AND_3)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1042382350)
def Event_1042382350():
    """Event 1042382350"""
    GotoIfUnknown_1004_05(Label.L0, character=1042380350, unk_8_12=True)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1042382350)
    IfAttackedWithDamageType(OR_3, attacked_entity=1042380350, attacker=0)
    IfUnknownCharacterCondition_34(OR_3, character=1042380350, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1042380350, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1042380350, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1042380350, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1042380350, unk_8_12=260, unk_12_16=1)
    IfHasAIStatus(OR_3, 1042380350, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1042382351)
    IfConditionTrue(AND_2, input_condition=OR_3)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfCharacterHasSpecialEffect(AND_4, 1042380350, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1042380350, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1042380350, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1042380350, 90160)
    IfCharacterHasSpecialEffect(AND_5, 1042380350, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1042380350, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1042380350, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1042380350, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1042380350, 90162)
    IfCharacterHasSpecialEffect(AND_6, 1042380350, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1042380350, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1042380350, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1042380350, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1042380350, 90161)
    IfCharacterHasSpecialEffect(AND_7, 1042380350, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1042380350, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1042380350, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1042380350, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1042380350, 90162)
    IfCharacterHasSpecialEffect(AND_8, 1042380350, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1042380350, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1042380350, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1042380350, 90160)
    IfConditionTrue(OR_4, input_condition=AND_4)
    IfConditionTrue(OR_4, input_condition=AND_5)
    IfConditionTrue(OR_4, input_condition=AND_6)
    IfConditionTrue(OR_4, input_condition=AND_7)
    IfConditionTrue(OR_4, input_condition=AND_8)
    IfConditionTrue(OR_4, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=1042380350, unk_4_8=1)
    ForceAnimation(1042380350, 20016, wait_for_completion=True, unknown2=1.0)
    ChangePatrolBehavior(1042380350, patrol_information_id=1042383350)


@RestartOnRest(1042382600)
def Event_1042382600(_, flag: uint, obj: uint):
    """Event 1042382600"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    PostDestruction(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfObjectDestroyed(MAIN, obj)
    EnableNetworkFlag(flag)


@RestartOnRest(1042382650)
def Event_1042382650(_, tutorial_param_id: int, flag: uint):
    """Event 1042382650"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9530)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, 6580)
    IfFlagEnabled(AND_1, 710550)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_NE_SW)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag, bit_count=1)


@RestartOnRest(1042382651)
def Event_1042382651(_, tutorial_param_id: int, flag: uint):
    """Event 1042382651"""
    EndIfTryingToCreateSession()
    IfPlayerHasGood(OR_1, 215000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 240000, including_storage=True)
    IfPlayerHasGood(OR_1, 243000, including_storage=True)
    IfPlayerHasGood(OR_1, 234000, including_storage=True)
    IfPlayerHasGood(OR_1, 244000, including_storage=True)
    IfPlayerHasGood(OR_1, 236000, including_storage=True)
    IfPlayerHasGood(OR_1, 232000, including_storage=True)
    IfPlayerHasGood(OR_1, 212000, including_storage=True)
    IfPlayerHasGood(OR_1, 241000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 233000, including_storage=True)
    IfPlayerHasGood(OR_1, 245000, including_storage=True)
    IfPlayerHasGood(OR_1, 203000, including_storage=True)
    IfLeavingSession(AND_1)
    IfPlayerDoesNotHaveGood(AND_1, 9111, including_storage=True)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_NE_SW)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(1042383700)
def Event_1042383700(_, character: uint):
    """Event 1042383700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3880)
    DisableFlag(1042389253)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L19, flag=1042382719)
    DisableNetworkFlag(1042382718)
    IfFlagEnabled(OR_15, 1042380701)
    IfFlagEnabled(OR_15, 3881)
    IfFlagEnabled(OR_15, 3882)
    IfFlagEnabled(OR_15, 3883)
    IfFlagDisabled(OR_15, 3885)
    IfTimeOfDay(AND_15, earliest=(20, 0, 0), latest=(5, 30, 0))
    IfFlagDisabled(AND_15, 1042380850)
    IfConditionTrue(AND_15, input_condition=OR_15)
    GotoIfConditionFalse(Label.L19, input_condition=AND_15)
    EnableNetworkFlag(1042382718)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableNetworkFlag(1042382719)
    GotoIfFlagEnabled(Label.L5, flag=3885)
    GotoIfFlagEnabled(Label.L4, flag=3888)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3885)
    IfFlagEnabled(OR_3, 3888)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3880)
    GotoIfFlagEnabled(Label.L2, flag=3881)
    GotoIfFlagEnabled(Label.L3, flag=3882)
    GotoIfFlagEnabled(Label.L4, flag=3883)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(3, 1042382718)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagDisabled(3, 1042382718)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagDisabled(3, 1042382718)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)
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
    IfFlagEnabled(OR_4, 3885)
    IfFlagEnabled(OR_4, 3888)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()
