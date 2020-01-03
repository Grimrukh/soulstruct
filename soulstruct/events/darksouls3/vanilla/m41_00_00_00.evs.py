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
from soulstruct.events.darksouls3 import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(14100000, obj=4101950, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(14100001, obj=4101951, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunEvent(14100100)
    RunEvent(14100101)
    RunEvent(14105500)
    RunEvent(14105200)
    RunEvent(14100800)
    RunEvent(14105810)
    RunEvent(14105811)
    RunEvent(14105812)
    RunEvent(14005829)
    RunCommonEvent(20005840, args=(4101800,))
    RunCommonEvent(20005841, args=(4101800,))
    RunEvent(14105520, slot=1, args=(10012051, 4101521))
    RunEvent(14105520, slot=2, args=(10012052, 4101522))
    RunEvent(14105520, slot=3, args=(10012053, 4101523))
    RunEvent(14105520, slot=4, args=(10012054, 4101524))
    RunEvent(14105520, slot=5, args=(10012055, 4101525))
    RunCommonEvent(20005701, args=(14100800, 14104190, 14105190, 4100190, 4102190, 70000001))
    RunCommonEvent(20005720, args=(14104190, 14105190, 14100800, 4100190))
    RunCommonEvent(20005711, args=(14104190, 14105805, 4100190, 4102800, 4102805, 14100801))
    RunCommonEvent(20005713, args=(74000640, 14100800, 14104190, 14105190, 4100190))
    RunCommonEvent(20005714, args=(14104190, 14105805, 4100190, 4102806, 14100801))
    RunCommonEvent(20005701, args=(14100800, 14104191, 14105191, 4100191, 4102191, 70000003))
    RunCommonEvent(20005720, args=(14104191, 14105191, 14100800, 4100191))
    RunCommonEvent(20005711, args=(14104191, 14105805, 4100191, 4102800, 4102805, 14100801))
    RunCommonEvent(20005714, args=(14104191, 14105805, 4100191, 4102806, 14100801))


def Preconstructor():
    """ 50: Event 50 """
    DisableSoundEvent(4104800)
    DisableSoundEvent(4104801)
    DisableSoundEvent(4104802)
    DisableFlag(14105100)
    RunEvent(14105510)


def Event14100100():
    """ 14100100: Event 14100100 """
    DisableCollision(4104101)
    DisableCharacter(4100100)
    DisableAnimations(4100100)
    DisableFlag(74100100)
    DisableFlag(100)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyOn((9920, 9923))
    IfFlagOff(1, 50006020)
    IfFlagOn(1, 14101100)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(1, 14105100)
    CreateObjectFX(30001, obj=4101100, model_point=0)
    IfFlagOff(2, 101)
    IfLeavingSession(2)
    IfActionButtonInRegion(2, action_button_id=9341, region=4101100)
    IfConditionTrue(0, input_condition=2)
    DisplayDialogAndSetFlags(message=10012020, button_type=ButtonType.Yes_or_No, 
                             number_buttons=NumberButtons.TwoButton, anchor_entity=4101100, display_distance=3.0, 
                             left_flag=100, right_flag=14105100, cancel_flag=14105100)
    RestartIfFlagOff(100)
    EnableFlag(100)
    DisableFlag(101)
    AddSpecialEffect(PLAYER, 4900)
    AddSpecialEffect(PLAYER, 4901)
    EnableImmortality(PLAYER)
    EnableImmortality(4100100)
    DeleteObjectFX(4101100, erase_root=True)
    DisableCollision(4104100)
    EnableCollision(4104103)
    WaitFrames(1)
    PlayCutsceneAndMovePlayer_WithUnknowns(cutscene=41000060, cutscene_type=CutsceneType.Skippable, region=4102110, 
                                           game_map=KILN_OF_THE_FIRST_FLAME, player_id=10000, unknown1=0, unknown2=0)
    WaitFrames(1)
    EnableCharacter(4100100)
    EnableAnimations(4100100)
    ForceAnimation(4100100, 30004, loop=True)
    DisableObject(4101952)
    ForceAnimation(PLAYER, 0)
    DisableCollision(4104103)
    EnableCollision(4104101)
    EnableCollision(4104102)
    WaitFrames(1)
    ForceAnimation(4100100, 30004, loop=True)
    IfOngoingCutsceneFinished(0, 4102110)
    IfDamageType(-2, attacked_entity=4100100, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=-2)
    IfTimeElapsed(-3, 10.0)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(1, -2)
    EnableFlag(74100100)
    AddSpecialEffect(PLAYER, 4902)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    Wait(4.199999809265137)
    AwardAchievement(2)
    DisableLoadingScreenTips()
    DisableHUDVisibility()
    SetNetworkInteractionState(state=True)
    EnableFlag(110)
    EnableFlag(9922)
    EnableFlag(22)
    EnableFlag(6400)
    CancelSpecialEffect(PLAYER, 4902)
    End()

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(41000070, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableHUDVisibility()
    SetNetworkInteractionState(state=True)
    DisableLoadingScreenTips()
    EnableFlag(110)
    EnableFlag(9923)
    EnableFlag(23)
    EnableFlag(6400)
    CancelSpecialEffect(PLAYER, 4902)
    End()


def Event14100101():
    """ 14100101: Event 14100101 """
    DisableFlag(101)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyOn((9920, 9923))
    IfFlagOn(1, 14101100)
    IfConditionTrue(0, input_condition=1)
    EnableObject(4101952)
    ForceAnimation(4101952, 11, loop=True)
    IfFlagOff(2, 100)
    IfLeavingSession(2)
    IfActionButtonInRegion(2, action_button_id=9342, region=4101952)
    IfConditionTrue(0, input_condition=2)
    DisplayDialogAndSetFlags(message=10012021, button_type=ButtonType.Yes_or_No, 
                             number_buttons=NumberButtons.TwoButton, anchor_entity=4101952, display_distance=3.0, 
                             left_flag=101, right_flag=14105101, cancel_flag=14105101)
    RestartIfFlagOff(101)
    EnableFlag(101)
    DisableFlag(100)
    ForceAnimation(4101952, 1)
    StoreItemAmountSpecifiedByFlagValue(ItemType.Good, 490, 9230, 4)
    WaitFrames(1)
    IfEventValueEqual(9, 9230, bit_count=4, value=8)
    GotoIfConditionTrue(Label.L0, input_condition=9)
    PlayCutscene(41000000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(1)
    DisableLoadingScreenTips()
    EnableFlag(9920)
    EnableFlag(20)
    EnableFlag(110)
    EnableFlag(6400)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagOff(2, 9013)
    PlayCutscene(41000050, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(41000051, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(3)
    DisableLoadingScreenTips()
    EnableFlag(9921)
    EnableFlag(21)
    EnableFlag(110)
    EnableFlag(6400)
    End()


def Event14105520(arg_0_3: int, arg_4_7: int):
    """ 14105520: Event 14105520 """
    DisableNetworkSync()
    IfActionButtonInRegion(0, action_button_id=9356, region=arg_4_7)
    DisplayDialog(arg_0_3, anchor_entity=arg_4_7, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Wait(3.0)
    Restart()


def Event14105500():
    """ 14105500: Event 14105500 """
    IfActionButtonInRegion(0, action_button_id=9343, region=4101101)
    RotateToFaceEntity(PLAYER, 4101101, animation=91040, wait_for_completion=False)
    Wait(3.0)
    WarpToMap(game_map=KILN_OF_THE_FIRST_FLAME, destination_player_id=4100120)


@RestartOnRest
def Event14105510():
    """ 14105510: Event 14105510 """
    DisableObject(4106102)
    IfFlagOn(1, 14100511)
    EndIfConditionFalse(1)
    EnableObject(4106102)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagOn(1, 14100512)
    EnableFlag(14100512)
    IfPlayerInOwnWorld(2)
    IfLeavingSession(2)
    IfActionButtonInRegion(2, action_button_id=9344, region=4101102)
    IfConditionTrue(0, input_condition=2)
    BanishPhantoms(unknown=0)
    RotateToFaceEntity(PLAYER, 4101102, animation=91040, wait_for_completion=False)
    Wait(3.0)
    WarpToMap(game_map=DREG_HEAP, destination_player_id=5002110)
    EnableFlag(14100510)


@RestartOnRest
def Event14105200():
    """ 14105200: Event 14105200 """
    DisableCharacter(4100200)


def Event14100800():
    """ 14100800: Event 14100800 """
    EndIfFlagOn(14100800)
    IfHealthComparison(0, character=4100800, comparison_type=ComparisonType.LessThanOrEqual, value=0.0)
    Wait(3.0)
    PlaySoundEffect(anchor_entity=4100800, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 4100800)
    HandleBossDefeatAndDisplayBanner(boss=4100800, banner=BannerType.UnknownBossDefeat)
    EnableFlag(14100800)
    EnableFlag(14101100)
    EnableFlag(9321)
    EnableFlag(6321)
    CreateTemporaryFX(1060, anchor_entity=4101952, anchor_type=CoordEntityType.Object, model_point=200)


@RestartOnRest
def Event14105810():
    """ 14105810: Event 14105810 """
    GotoIfFlagOff(Label.L0, 14100800)
    Kill(4100800, award_souls=False)
    DisableCharacter(4100800)
    DisableAI(4100800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(4100800)
    GotoIfFlagOn(Label.L1, 14100801)
    IfPlayerInOwnWorld(1)
    IfEntityWithinDistance(1, 4100800, PLAYER, radius=40.0)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagState(flag=14100801, state=FlagState.On)
    ForceAnimation(4100800, 1700, wait_for_completion=True)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(1, 14105805)
    IfCharacterInsideRegion(1, PLAYER, region=4102800)
    IfConditionTrue(0, input_condition=1)

    # --- 2 --- #
    DefineLabel(2)
    SetNetworkConnectedFlagState(flag=14100801, state=FlagState.On)
    SetNetworkConnectedFlagState(flag=14105807, state=FlagState.On)
    EnableAI(4100800)
    EnableBossHealthBar(4100800, name=905280)
    SetNetworkUpdateRate(4100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EndIfPlayerNotInOwnWorld()
    SetNetworkUpdateAuthority(4100800, UpdateAuthority.Forced)


@RestartOnRest
def Event14105811():
    """ 14105811: Event 14105811 """
    EndIfFlagOn(14100800)
    EndIfFlagOn(14105802)
    EnableImmortality(4100800)
    IfHealthComparison(1, character=4100800, comparison_type=ComparisonType.LessThanOrEqual, value=0.05000000074505806)
    IfDamageType(1, attacked_entity=4100800, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagState(flag=14105803, state=FlagState.On)
    ForceAnimation(4100800, 20010, wait_for_completion=True)
    ForceAnimation(4100800, 20005, wait_for_completion=True)
    SetNetworkConnectedFlagState(flag=14105802, state=FlagState.On)
    DisableImmortality(4100800)


@RestartOnRest
def Event14105812():
    """ 14105812: Event 14105812 """
    EndIfFlagOn(14100800)
    GotoIfFlagOn(Label.L0, 14100801)
    GotoIfFlagOn(Label.L0, 14100801)
    ForceAnimation(4100800, 700)

    # --- 0 --- #
    DefineLabel(0)
    IfObjectBackreadEnabled(0, obj=4101952)
    WaitFrames(1)
    ForceAnimation(4101952, 100000)


@RestartOnRest
def Event14105813(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int):
    """ 14105813: Event 14105813 """
    DisableNetworkSync()
    DisableSoundEvent(arg_16_19)
    DisableSoundEvent(arg_20_23)
    EndIfFlagOn(arg_0_3)
    IfFlagOn(1, arg_4_7)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.Equal, value=0)
    IfFlagOn(1, arg_8_11)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(arg_16_19)
    Unknown_2010_07(entity=arg_20_23)
    IfFlagOn(-1, arg_24_27)
    IfFlagOn(-1, arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFlagOn(Label.L0, arg_0_3)
    EnableBossMusic(arg_20_23)
    IfFlagOn(0, arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    DisableBossMusic(-1)


@RestartOnRest
def Event14005829():
    """ 14005829: Event 14005829 """
    RunCommonEvent(20005800, args=(14100800, 4101800, 4102800, 14105805, 4101800, 4100800, 14100801, 0))
    RunCommonEvent(20005801, args=(14100800, 4101800, 4102800, 14105805, 4101800, 14105806))
    SkipLinesIfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, 
                                         value=0)
    RunCommonEvent(20001836, args=(14100800, 14105805, 14105806, 14105807, 4104800, 4104801, 14105802))
    SkipLines(1)
    RunCommonEvent(20005831, args=(14100800, 14105805, 14105806, 4102800, 4104800, 4104801, 14105802))
    RunCommonEvent(20005820, args=(14100800, 4101800, 4, 14100801))
    RunCommonEvent(20005810, args=(14100800, 4101800, 4102800, 10000))


@RestartOnRest
def Event14005900():
    """ 14005900: Event 14005900 """
    EnableFlag(74000120)
    EnableFlag(14101100)
    CancelSpecialEffect(PLAYER, 4900)
    CancelSpecialEffect(PLAYER, 4901)
    SetNetworkInteractionState(state=True)
    DisableHUDVisibility()
    IfFlagOn(-1, 100)
    IfFlagOn(-1, 101)
    IfConditionTrue(0, input_condition=-1)
    DisableCharacter(4100800)
    DisableAnimations(4100800)
