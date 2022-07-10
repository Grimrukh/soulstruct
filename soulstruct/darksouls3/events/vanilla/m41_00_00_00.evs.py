"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=14100000, obj=4101950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14100001, obj=4101951, reaction_distance=5.0)
    Event_14100100()
    Event_14100101()
    Event_14105500()
    Event_14105200()
    Event_14100800()
    Event_14105810()
    Event_14105811()
    Event_14105812()
    Event_14005829()
    RunCommonEvent(20005840, args=(4101800,))
    RunCommonEvent(20005841, args=(4101800,))
    Event_14105520(1, text=10012051, anchor_entity=4101521)
    Event_14105520(2, text=10012052, anchor_entity=4101522)
    Event_14105520(3, text=10012053, anchor_entity=4101523)
    Event_14105520(4, text=10012054, anchor_entity=4101524)
    Event_14105520(5, text=10012055, anchor_entity=4101525)
    RunCommonEvent(20005701, args=(14100800, 14104190, 14105190, 4100190, 4102190, 70000001))
    RunCommonEvent(20005720, args=(14104190, 14105190, 14100800, 4100190))
    RunCommonEvent(20005711, args=(14104190, 14105805, 4100190, 4102800, 4102805, 14100801))
    RunCommonEvent(20005713, args=(74000640, 14100800, 14104190, 14105190, 4100190))
    RunCommonEvent(20005714, args=(14104190, 14105805, 4100190, 4102806, 14100801))
    RunCommonEvent(20005701, args=(14100800, 14104191, 14105191, 4100191, 4102191, 70000003))
    RunCommonEvent(20005720, args=(14104191, 14105191, 14100800, 4100191))
    RunCommonEvent(20005711, args=(14104191, 14105805, 4100191, 4102800, 4102805, 14100801))
    RunCommonEvent(20005714, args=(14104191, 14105805, 4100191, 4102806, 14100801))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableSoundEvent(sound_id=4104800)
    DisableSoundEvent(sound_id=4104801)
    DisableSoundEvent(sound_id=4104802)
    DisableFlag(14105100)
    Event_14105510()


@NeverRestart(14100100)
def Event_14100100():
    """Event 14100100"""
    DisableMapCollision(collision=4104101)
    DisableCharacter(4100100)
    DisableAnimations(4100100)
    DisableFlag(74100100)
    DisableFlag(100)
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(9920, 9923))
    AND_1.Add(FlagDisabled(50006020))
    AND_1.Add(FlagEnabled(14101100))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(14105100):
        CreateObjectVFX(4101100, vfx_id=0, model_point=30001)
    AND_2.Add(FlagDisabled(101))
    AND_2.Add(LeavingSession())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9341, entity=4101100))
    
    MAIN.Await(AND_2)
    
    DisplayDialogAndSetFlags(
        message=10012020,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=4101100,
        display_distance=3.0,
        left_flag=100,
        right_flag=14105100,
        cancel_flag=14105100,
    )
    if FlagDisabled(100):
        return RESTART
    EnableFlag(100)
    DisableFlag(101)
    AddSpecialEffect(PLAYER, 4900)
    AddSpecialEffect(PLAYER, 4901)
    EnableImmortality(PLAYER)
    EnableImmortality(4100100)
    DeleteObjectVFX(4101100)
    DisableMapCollision(collision=4104100)
    EnableMapCollision(collision=4104103)
    WaitFrames(frames=1)
    PlayCutsceneAndMoveSpecificPlayer_WithUnknowns(
        cutscene_id=41000060,
        cutscene_flags=0,
        move_to_region=4102110,
        game_map=KILN_OF_THE_FIRST_FLAME,
        player_id=10000,
        unknown1=0,
        unknown2=0,
    )
    WaitFrames(frames=1)
    EnableCharacter(4100100)
    EnableAnimations(4100100)
    ForceAnimation(4100100, 30004, loop=True, unknown2=1.0)
    DisableObject(4101952)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    DisableMapCollision(collision=4104103)
    EnableMapCollision(collision=4104101)
    EnableMapCollision(collision=4104102)
    WaitFrames(frames=1)
    ForceAnimation(4100100, 30004, loop=True, unknown2=1.0)
    
    MAIN.Await(OngoingCutsceneFinished(cutscene_id=4102110))
    
    OR_2.Add(AttackedWithDamageType(attacked_entity=4100100, attacker=PLAYER))
    OR_3.Add(OR_2)
    OR_3.Add(TimeElapsed(seconds=10.0))
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=OR_2)
    EnableFlag(74100100)
    AddSpecialEffect(PLAYER, 4902)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    Wait(4.199999809265137)
    AwardAchievement(achievement_id=2)
    DisableLoadingScreenTips()
    DisableHUDVisibility()
    SetNetworkInteractionState(state=True)
    EnableFlag(110)
    EnableFlag(9922)
    EnableFlag(22)
    EnableFlag(6400)
    CancelSpecialEffect(PLAYER, 4902)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    PlayCutscene(41000070, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableHUDVisibility()
    SetNetworkInteractionState(state=True)
    DisableLoadingScreenTips()
    EnableFlag(110)
    EnableFlag(9923)
    EnableFlag(23)
    EnableFlag(6400)
    CancelSpecialEffect(PLAYER, 4902)
    End()


@NeverRestart(14100101)
def Event_14100101():
    """Event 14100101"""
    DisableFlag(101)
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(9920, 9923))
    AND_1.Add(FlagEnabled(14101100))
    
    MAIN.Await(AND_1)
    
    EnableObject(4101952)
    ForceAnimation(4101952, 11, loop=True, unknown2=1.0)
    AND_2.Add(FlagDisabled(100))
    AND_2.Add(LeavingSession())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9342, entity=4101952))
    
    MAIN.Await(AND_2)
    
    DisplayDialogAndSetFlags(
        message=10012021,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=4101952,
        display_distance=3.0,
        left_flag=101,
        right_flag=14105101,
        cancel_flag=14105101,
    )
    if FlagDisabled(101):
        return RESTART
    EnableFlag(101)
    DisableFlag(100)
    ForceAnimation(4101952, 1, unknown2=1.0)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=490, flag=9230, bit_count=4)
    WaitFrames(frames=1)
    AND_9.Add(EventValueEqual(flag=9230, bit_count=4, value=8))
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    PlayCutscene(41000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=1)
    DisableLoadingScreenTips()
    EnableFlag(9920)
    EnableFlag(20)
    EnableFlag(110)
    EnableFlag(6400)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(9013):
        PlayCutscene(41000050, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    else:
        PlayCutscene(41000051, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=3)
    DisableLoadingScreenTips()
    EnableFlag(9921)
    EnableFlag(21)
    EnableFlag(110)
    EnableFlag(6400)
    End()


@NeverRestart(14105520)
def Event_14105520(_, text: int, anchor_entity: int):
    """Event 14105520"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9356, entity=anchor_entity))
    
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(3.0)
    Restart()


@NeverRestart(14105500)
def Event_14105500():
    """Event 14105500"""
    MAIN.Await(ActionButtonParamActivated(action_button_id=9343, entity=4101101))
    
    RotateToFaceEntity(PLAYER, 4101101, animation=91040)
    Wait(3.0)
    WarpToMap(game_map=KILN_OF_THE_FIRST_FLAME, player_start=4100120)


@RestartOnRest(14105510)
def Event_14105510():
    """Event 14105510"""
    DisableObject(4106102)
    AND_1.Add(FlagEnabled(14100511))
    if not AND_1:
        return
    EnableObject(4106102)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(14100512):
        EnableFlag(14100512)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(LeavingSession())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9344, entity=4101102))
    
    MAIN.Await(AND_2)
    
    BanishPhantoms(unknown=0)
    RotateToFaceEntity(PLAYER, 4101102, animation=91040)
    Wait(3.0)
    WarpToMap(game_map=DREG_HEAP, player_start=5002110)
    EnableFlag(14100510)


@RestartOnRest(14105200)
def Event_14105200():
    """Event 14105200"""
    DisableCharacter(4100200)


@NeverRestart(14100800)
def Event_14100800():
    """Event 14100800"""
    if FlagEnabled(14100800):
        return
    
    MAIN.Await(HealthRatioLessThanOrEqual(4100800, value=0.0))
    
    Wait(3.0)
    PlaySoundEffect(4100800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(4100800))
    
    HandleBossDefeatAndDisplayBanner(boss=4100800, banner=BannerType.UnknownBossDefeat)
    EnableFlag(14100800)
    EnableFlag(14101100)
    EnableFlag(9321)
    EnableFlag(6321)
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=4101952, model_point=200, anchor_type=CoordEntityType.Object)


@RestartOnRest(14105810)
def Event_14105810():
    """Event 14105810"""
    GotoIfFlagDisabled(Label.L0, flag=14100800)
    Kill(4100800)
    DisableCharacter(4100800)
    DisableAI(4100800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(4100800)
    GotoIfFlagEnabled(Label.L1, flag=14100801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=4100800, other_entity=PLAYER, radius=40.0))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=14100801, state=FlagSetting.On)
    ForceAnimation(4100800, 1700, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(14105805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4102800))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkConnectedFlagState(flag=14100801, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=14105807, state=FlagSetting.On)
    EnableAI(4100800)
    EnableBossHealthBar(4100800, name=905280)
    SetNetworkUpdateRate(4100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    if PlayerNotInOwnWorld():
        return
    SetNetworkUpdateAuthority(4100800, authority_level=UpdateAuthority.Forced)


@RestartOnRest(14105811)
def Event_14105811():
    """Event 14105811"""
    if FlagEnabled(14100800):
        return
    if FlagEnabled(14105802):
        return
    EnableImmortality(4100800)
    AND_1.Add(HealthRatioLessThanOrEqual(4100800, value=0.05000000074505806))
    AND_1.Add(AttackedWithDamageType(attacked_entity=4100800, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=14105803, state=FlagSetting.On)
    ForceAnimation(4100800, 20010, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(4100800, 20005, wait_for_completion=True, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=14105802, state=FlagSetting.On)
    DisableImmortality(4100800)


@RestartOnRest(14105812)
def Event_14105812():
    """Event 14105812"""
    if FlagEnabled(14100800):
        return
    GotoIfFlagEnabled(Label.L0, flag=14100801)
    GotoIfFlagEnabled(Label.L0, flag=14100801)
    ForceAnimation(4100800, 700, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectBackreadEnabled(obj=4101952))
    
    WaitFrames(frames=1)
    ForceAnimation(4101952, 100000, unknown2=1.0)


@RestartOnRest(14105813)
def Event_14105813(_, flag: int, flag_1: int, flag_2: int, region: int, sound_id: int, sound_id_1: int, flag_3: int):
    """Event 14105813"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=sound_id)
    DisableSoundEvent(sound_id=sound_id_1)
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=sound_id)
    Unknown_2010_07(sound_id=sound_id_1)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EnableBossMusic(sound_id=sound_id_1)
    
    MAIN.Await(FlagEnabled(flag))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBossMusic(sound_id=-1)


@RestartOnRest(14005829)
def Event_14005829():
    """Event 14005829"""
    RunCommonEvent(20005800, args=(14100800, 4101800, 4102800, 14105805, 4101800, 4100800, 14100801, 0))
    RunCommonEvent(20005801, args=(14100800, 4101800, 4102800, 14105805, 4101800, 14105806))
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    RunCommonEvent(20001836, args=(14100800, 14105805, 14105806, 14105807, 4104800, 4104801, 14105802))
    SkipLines(1)
    RunCommonEvent(20005831, args=(14100800, 14105805, 14105806, 4102800, 4104800, 4104801, 14105802))
    RunCommonEvent(20005820, args=(14100800, 4101800, 4, 14100801))
    RunCommonEvent(20005810, args=(14100800, 4101800, 4102800, 10000))


@RestartOnRest(14005900)
def Event_14005900():
    """Event 14005900"""
    EnableFlag(74000120)
    EnableFlag(14101100)
    CancelSpecialEffect(PLAYER, 4900)
    CancelSpecialEffect(PLAYER, 4901)
    SetNetworkInteractionState(state=True)
    DisableHUDVisibility()
    OR_1.Add(FlagEnabled(100))
    OR_1.Add(FlagEnabled(101))
    
    MAIN.Await(OR_1)
    
    DisableCharacter(4100800)
    DisableAnimations(4100800)
