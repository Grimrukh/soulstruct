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
    Event_10012682()
    Event_10012800()
    Event_10012810()
    Event_10012811()
    Event_10012849()
    Event_10012500()
    Event_10010790()
    Event_10010791()
    Event_10010792()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(10011700)
    Event_10010020()
    Event_10010030()
    Event_10010031()
    Event_10012502()
    Event_10012560()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(100)
    EndIfFlagEnabled(102)
    EndIfOutsideMap(game_map=CHAPEL_OF_ANTICIPATION)
    UnknownTimer_04(
        hours=23,
        minutes=45,
        seconds=0,
        unknown1=0,
        unknown2=0,
        unknown3=0,
        unknown4=0,
        unknown5=0,
        unknown6=0,
    )


@RestartOnRest(10010020)
def Event_10010020():
    """Event 10010020"""
    EndIfThisEventSlotFlagEnabled()
    EndIfOutsideMap(game_map=CHAPEL_OF_ANTICIPATION)
    SetAreaWelcomeMessageState(state=False)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    SetUnknownVFX_06(vfx_id=-1)
    Unknown_2004_75(character=PLAYER, unknown1=0, unknown2=-1)
    Unknown_2004_75(character=PLAYER, unknown1=1, unknown2=-1)
    UnknownCutscene_10(
        cutscene_id=10000040,
        cutscene_flags=0,
        player_id=10000,
        hours=0,
        unknown1=0,
        unknown2=0.0,
        unknown3=1,
        unknown4=23,
        unknown5=45,
    )
    WaitFramesAfterCutscene(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetRespawnPoint(respawn_point=10012020)
    SaveRequest()
    DisableThisSlotFlag()
    EnableFlag(100)


@NeverRestart(10010030)
def Event_10010030():
    """Event 10010030"""
    IfThisEventSlotFlagEnabled(AND_15)
    IfFlagEnabled(AND_15, 101)
    EndIfConditionTrue(input_condition=AND_15)
    EndIfOutsideMap(game_map=CHAPEL_OF_ANTICIPATION)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 10010801)
    IfHealthValueGreaterThan(AND_2, 10010800, value=0)
    IfHealthValueEqual(AND_2, PLAYER, value=1)
    IfCharacterDead(AND_3, PLAYER)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetRespawnPoint(respawn_point=18002020)
    SaveRequest()
    Unknown_2003_80(unk_0_4=0)
    EndIfFinishedConditionTrue(input_condition=AND_3)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    Wait(1.0)
    AddSpecialEffect(PLAYER, 4790)
    EnableFlag(9021)
    UnknownSound_2010_10(unk_0_4=920900, unk_4_8=-1)
    UnknownCutscene_12(
        cutscene_id=10010000,
        cutscene_flags=0,
        respawn_point=18002020,
        move_to_region=18000000,
        player_id=10000,
        unk_20_24=10010,
        unk_24_25=0,
        unk_25_26=1,
        unk_26_27=0,
        unk_28_32=-1.0,
        unk_32_36=1968641,
    )
    WaitFramesAfterCutscene(frames=1)


@NeverRestart(10010031)
def Event_10010031():
    """Event 10010031"""
    EndIfOutsideMap(game_map=CHAPEL_OF_ANTICIPATION)
    EndIfFlagEnabled(101)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 10012805)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableImmortality(PLAYER)
    IfCharacterOutsideRegion(OR_2, character=PLAYER, region=10012031)
    IfCharacterDead(OR_2, 10010800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DisableImmortality(PLAYER)


@RestartOnRest(10012500)
def Event_10012500():
    """Event 10012500"""
    GotoIfFlagDisabled(Label.L0, flag=10010500)
    DisableObject(10011500)
    DisableObject(10011501)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10012500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(10011500)
    EnableFlag(10010500)


@RestartOnRest(10012501)
def Event_10012501():
    """Event 10012501"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(100)
    EndIfFlagEnabled(102)
    EndIfOutsideMap(game_map=CHAPEL_OF_ANTICIPATION)
    SetUnknownVFX_06(vfx_id=808004)
    AddSpecialEffect(PLAYER, 4200)


@RestartOnRest(10012502)
def Event_10012502():
    """Event 10012502"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(10010502)
    EndIfOutsideMap(game_map=CHAPEL_OF_ANTICIPATION)
    SetAreaWelcomeMessageState(state=False)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=10012502)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetAreaWelcomeMessageState(state=True)
    DisplayUnknownMessage_14(text=10010)
    EnableFlag(10010502)


@RestartOnRest(10012504)
def Event_10012504():
    """Event 10012504"""
    EndIfFlagEnabled(10018540)
    EndIfFlagEnabled(60210)
    DisableObjectActivation(10011540, obj_act_id=-1)
    IfFlagEnabled(AND_1, 60210)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableObjectActivation(10011540, obj_act_id=-1)


@RestartOnRest(10012560)
def Event_10012560():
    """Event 10012560"""
    GotoIfFlagEnabled(Label.L0, flag=10018560)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 102)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(10018560)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(10011560, obj_act_id=2219000, relative_index=0)
    DisableObjectActivation(10011560, obj_act_id=2219000, relative_index=1)
    DisableObjectActivation(10011560, obj_act_id=2219000, relative_index=2)
    DisableObjectActivation(10011560, obj_act_id=2219000, relative_index=3)


@RestartOnRest(10012680)
def Event_10012680():
    """Event 10012680"""
    DisableNetworkSync()
    EndIfFlagEnabled(18000020)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 10010020)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10012680)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(710000)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=True, unk_5_6=True)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=10012680)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=False, unk_5_6=True)


@RestartOnRest(10012682)
def Event_10012682():
    """Event 10012682"""
    DisableNetworkSync()
    EndIfFlagEnabled(18000020)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10012682)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(710000)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=True, unk_5_6=True)


@RestartOnRest(10012800)
def Event_10012800():
    """Event 10012800"""
    EndIfFlagEnabled(10010800)
    IfHealthValueLessThanOrEqual(MAIN, 10010800, value=0)
    Wait(4.0)
    PlaySoundEffect(10018000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 10010800)
    KillBossAndDisplayBanner(character=10010800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(10010800)
    EnableFlag(9103)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61103)


@RestartOnRest(10012810)
def Event_10012810():
    """Event 10012810"""
    GotoIfFlagDisabled(Label.L0, flag=10010800)
    DisableCharacter(10010800)
    DisableAnimations(10010800)
    Kill(10010800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(10010800)
    GotoIfFlagEnabled(Label.L1, flag=10010801)
    ForceAnimation(10010800, 30003, unknown2=1.0)
    DisableHealthBar(10010800)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=10012801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=10010800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(10010801)
    SetNetworkUpdateRate(10010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(10010800, 20003, unknown2=1.0)
    Wait(4.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAnimations(10010800)
    Move(10010800, destination=10012810, destination_type=CoordEntityType.Region, short_move=True)
    IfFlagEnabled(AND_2, 10012805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=10012800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAnimations(10010800)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(10010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(10010800)
    EnableBossHealthBar(10010800, name=904690000)
    EndIfFlagEnabled(10010030)
    AddSpecialEffect(PLAYER, 4290)


@RestartOnRest(10012811)
def Event_10012811():
    """Event 10012811"""
    EndIfFlagEnabled(10010800)
    IfCharacterHasSpecialEffect(AND_1, 10010800, 16265)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(10012802)


@RestartOnRest(10012849)
def Event_10012849():
    """Event 10012849"""
    SkipLinesIfFlagEnabled(2, 101)
    RunCommonEvent(
        0,
        9005800,
        args=(10010800, 10011800, 10012800, 10012805, 10015800, 10000, 10010801, 10012801),
        arg_types="IIIIIiII",
    )
    SkipLines(1)
    RunCommonEvent(
        0,
        9005800,
        args=(10010800, 10011801, 10012800, 10012805, 10015800, 10000, 10010801, 10012801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(10010800, 10011801, 10012800, 10012805, 10012806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(10010800, 10011800, 16, 10010801), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(10010800, 10011801, 16, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(10010800, 920900, 10012805, 10012806, 0, 10012802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(10010790)
def Event_10010790():
    """Event 10010790"""
    EnableBackread(10011700)
    EnableCharacter(10011700)
    ForceAnimation(10011700, 90100, unknown2=1.0)
    DisableAnimations(10011700)


@RestartOnRest(10010791)
def Event_10010791():
    """Event 10010791"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400033)
    EndIfFlagDisabled(400031)
    IfActionButtonParamActivated(MAIN, action_button_id=6471, entity=10011700)
    RemoveGoodFromPlayer(item=8154, quantity=1)
    AwardItemLot(100330, host_only=False)
    End()


@RestartOnRest(10010792)
def Event_10010792():
    """Event 10010792"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(50)
    EndIfFlagEnabled(10019200)
    IfPlayerHasGood(OR_1, 9500)
    IfTimeElapsed(OR_2, seconds=5.0)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    WaitFrames(frames=1)
    IfPlayerHasGood(OR_5, 9500)
    SkipLinesIfConditionFalse(3, OR_5)
    EnableFlag(66150)
    EnableFlag(66170)
    EnableFlag(66180)
    EnableFlag(10019200)
    End()


@NeverRestart(10012900)
def Event_10012900():
    """Event 10012900"""
    IfFlagEnabled(MAIN, 10010900)
    IncrementEventValue(10010910, bit_count=32, max_value=999999999)
    Restart()
