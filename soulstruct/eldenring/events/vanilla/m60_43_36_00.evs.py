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
    Event_1043362210(1, 1043360213, 30.0, 430008500)
    Event_1043362210(2, 1043360214, 30.0, 430008501)
    Event_1043362210(3, 1043360215, 30.0, 430008502)
    Event_1043362210(5, 1043360217, 30.0, 430008503)
    Event_1043362210(6, 1043360218, 30.0, 430008501)
    Event_1043362210(7, 1043360219, 30.0, 430008502)
    RunCommonEvent(
        0,
        90005633,
        args=(580300, 580000, 1043360220, 30015, 20015, 1043361220, 1043361610),
        arg_types="IIIiiII",
    )
    Event_1043362340(0, character=1043360800, region=1043362340, destination=1043362360)
    Event_1043362340(1, character=1043360800, region=1043362341, destination=1043362361)
    Event_1043362340(2, character=1043360800, region=1043362342, destination=1043362362)
    Event_1043362340(3, character=1043360800, region=1043362343, destination=1043362363)
    Event_1043362340(4, character=1043360800, region=1043362344, destination=1043362364)
    Event_1043362340(5, character=1043360800, region=1043362345, destination=1043362365)
    Event_1043362340(6, character=1043360800, region=1043362346, destination=1043362366)
    Event_1043362340(7, character=1043360800, region=1043362347, destination=1043362367)
    Event_1043362340(8, character=1043360800, region=1043362348, destination=1043362368)
    Event_1043362340(9, character=1043360800, region=1043362349, destination=1043362369)
    Event_1043362340(10, character=1043360800, region=1043362350, destination=1043362370)
    Event_1043362340(11, character=1043360800, region=1043362351, destination=1043362371)
    Event_1043362340(12, character=1043360800, region=1043362352, destination=1043362372)
    RunCommonEvent(0, 90005861, args=(1043360800, 0, 1043360800, 1, 30110, 30060, 0.0), arg_types="IIIIiif")
    RunCommonEvent(0, 90005870, args=(1043360800, 904500600, 25), arg_types="IiI")
    Event_1043362380()
    Event_1043362510(0, obj=1043361510, region=1043362510, flag=1043362500, obj_act_id=1043363600)
    RunCommonEvent(0, 90005781, args=(1043360800, 1043362700, 1043362701, 1043360700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005780,
        args=(1043360800, 1043362700, 1043362701, 1043360700, 20, 1043362700, 1043369200, 0, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(
        0,
        90005783,
        args=(1043360800, 1043362700, 1043362701, 1043360700, 1043362700, 1043362100, 0),
        arg_types="IIIIIIi",
    )
    Event_1043363700()
    Event_1043363701(0, character=1043360700)
    Event_1043363702(0, entity=1043360700)
    Event_1043363704()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043360700)
    RunCommonEvent(0, 90005251, args=(1043360212, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360213, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360214, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360215, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360216, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360217, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360218, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360219, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1043360200, 5.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1043362210)
def Event_1043362210(_, character: uint, radius: float, sound_id: int):
    """Event 1043362210"""
    DisableNetworkSync()
    WaitRandomSeconds(min_seconds=4.0, max_seconds=18.0)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterDead(AND_1, character, target_comparison_type=ComparisonType.NotEqual)
    IfHasAIStatus(AND_1, character, ai_status=AIStatusType.Normal)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    PlaySoundEffect(character, sound_id, sound_type=SoundType.c_CharacterMotion)
    WaitRandomSeconds(min_seconds=4.0, max_seconds=18.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(1043362220)
def Event_1043362220(
    _,
    character: uint,
    obj: uint,
    flag: uint,
    flag_1: uint,
    radius: float,
    animation_id: int,
    obj_1: uint,
):
    """Event 1043362220"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableTreasure(obj=obj)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableTreasure(obj=obj)
    AddSpecialEffect(character, 10124)
    DisableInvincibility(character)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=radius)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableObject(obj)
    EnableObject(obj_1)
    EnableTreasure(obj=obj)
    CancelSpecialEffect(character, 10124)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()


@RestartOnRest(1043362221)
def Event_1043362221(_, character: uint, flag: uint, flag_1: uint, animation_id: int, obj: uint):
    """Event 1043362221"""
    EndIfFlagEnabled(flag)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfCharacterHuman(AND_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=7.0)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, animation_id, unknown2=1.0)
    ForceAnimation(obj, 1, unknown2=1.0)
    Wait(3.799999952316284)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableObject(obj)
    EnableFlag(flag)
    End()


@RestartOnRest(1043362340)
def Event_1043362340(_, character: uint, region: uint, destination: uint):
    """Event 1043362340"""
    SkipLinesIfFlagDisabled(4, 1043360340)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableNetworkFlag(1043362379)
    End()
    DisableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, 30005, loop=True, unknown2=1.0)
    IfFlagDisabled(AND_1, 1043360340)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20005, loop=True, unknown2=1.0)
    EnableNetworkFlag(1043360340)
    End()


@RestartOnRest(1043362380)
def Event_1043362380():
    """Event 1043362380"""
    GotoIfFlagDisabled(Label.L0, flag=1043360380)
    DisableCharacter(1043365340)
    DisableAnimations(1043365340)
    DisableAI(1043365340)
    DisableGravity(1043365340)
    PostDestruction(1043361300)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_1, 1043362379)
    IfFlagEnabled(OR_1, 1043360341)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableCharacter(1043365340)
    DisableAnimations(1043365340)
    DisableAI(1043365340)
    DisableGravity(1043365340)
    PostDestruction(1043361300)
    EnableFlag(1043360380)


@RestartOnRest(1043362510)
def Event_1043362510(_, obj: uint, region: uint, flag: uint, obj_act_id: uint):
    """Event 1043362510"""
    DisableNetworkSync()
    GotoIfTryingToJoinSession(Label.L1)
    GotoIfTryingToCreateSession(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id)
    IfTryingToJoinSession(OR_1)
    IfTryingToCreateSession(OR_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfTryingToJoinSession(Label.L1)
    GotoIfTryingToCreateSession(Label.L1)
    EnableFlag(flag)
    Wait(1.2999999523162842)
    Wait(0.8999999761581421)
    GotoIfTryingToJoinSession(Label.L2)
    GotoIfTryingToCreateSession(Label.L2)
    IfHealthValueEqual(AND_1, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    GotoIfCharacterOutsideRegion(Label.L20, character=PLAYER, region=region)
    GotoIfTryingToJoinSession(Label.L2)
    GotoIfTryingToCreateSession(Label.L2)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=1, unknown4=-1.0)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(0.699999988079071)
    AddSpecialEffect(PLAYER, 4090)
    PlaySoundEffect(PLAYER, 8700, sound_type=SoundType.c_CharacterMotion)
    Wait(2.700000047683716)
    DisableCharacter(PLAYER)
    IfHealthValueEqual(AND_3, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_3)
    GotoIfTryingToJoinSession(Label.L3)
    GotoIfTryingToCreateSession(Label.L3)
    AddSpecialEffect(PLAYER, 4091)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)
    EnableFlag(32080650)
    WarpToMap(game_map=SELLIA_CRYSTAL_TUNNEL, player_start=32082650, unknown1=60)
    SaveRequest()
    SetRespawnPoint(respawn_point=32082650)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)
    Wait(4.400000095367432)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    DisableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=2)
    DisableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableObjectActivation(obj, obj_act_id=-1)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    ForceAnimation(PLAYER, 60131, unknown2=1.0)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableObjectActivation(obj, obj_act_id=-1)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    DisableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObjectActivation(obj, obj_act_id=-1)
    IfTryingToJoinSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfTryingToCreateSession(OR_3)
    IfConditionFalse(AND_2, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableObjectActivation(obj, obj_act_id=-1)
    Restart()


@RestartOnRest(1043362651)
def Event_1043362651(_, tutorial_param_id: int, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1043362651"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag_2, bit_count=1)


@RestartOnRest(1043362652)
def Event_1043362652(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043362652"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
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
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9530)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SE_SE)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(flag)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag_1, bit_count=1)


@RestartOnRest(1043362653)
def Event_1043362653(_, tutorial_param_id: int, flag: uint, flag_1: uint, tutorial_param_id_1: int):
    """Event 1043362653"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SE_SE)
    IfPlayerDoesNotHaveGood(AND_1, 9116, including_storage=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag_1)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=flag, bit_count=1)


@RestartOnRest(1043362654)
def Event_1043362654(_, tutorial_param_id: int, flag: uint):
    """Event 1043362654"""
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
    IfLeavingSession(AND_1)
    IfPlayerDoesNotHaveGood(AND_1, 9111, including_storage=True)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SE_SE)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(1043363700)
def Event_1043363700():
    """Event 1043363700"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043359258)
    EndIfFlagEnabled(1043360800)
    IfAttackedWithDamageType(MAIN, attacked_entity=1043360800, attacker=PLAYER)
    EnableFlag(1043359258)
    End()


@RestartOnRest(1043363701)
def Event_1043363701(_, character: uint):
    """Event 1043363701"""
    DisableCharacter(character)
    EnableBackread(character)
    SkipLinesIfFlagDisabled(1, 1043360800)
    DisableBackread(character)
    End()


@RestartOnRest(1043363702)
def Event_1043363702(_, entity: uint):
    """Event 1043363702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043360800)
    IfFlagEnabled(OR_1, 3625)
    IfFlagEnabled(OR_1, 3626)
    SkipLinesIfConditionTrue(2, OR_1)
    DisableFlag(1043369200)
    End()
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=20000, radius=10.0)
    IfFlagEnabled(AND_1, 1043360340)
    IfFlagEnabled(AND_1, 1043359256)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagDisabled(3620)
    EndIfFlagEnabled(1043360800)
    EnableFlag(1043369200)
    End()


@RestartOnRest(1043363703)
def Event_1043363703(_, unk_0_4: uint, other_entity: uint):
    """Event 1043363703"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043360800)
    IfFlagEnabled(OR_1, 3625)
    IfFlagEnabled(OR_1, 3626)
    EndIfConditionFalse(input_condition=OR_1)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=other_entity, radius=80.0)
    IfFlagEnabled(AND_1, 1043362700)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, 1043360800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EndIfFlagEnabled(1043360800)
    Unknown_2003_79(unk_0_4=unk_0_4)
    DisableFlag(1043369200)
    End()


@RestartOnRest(1043363704)
def Event_1043363704():
    """Event 1043363704"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043360800)
    IfFlagEnabled(OR_1, 3625)
    IfFlagEnabled(OR_1, 3626)
    EndIfConditionFalse(input_condition=OR_1)
    IfFlagEnabled(MAIN, 1043360800)
    SkipLinesIfFlagDisabled(1, 1043362700)
    EnableFlag(1043369201)
    DisableFlag(1043369200)
    End()
