"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=11050002, obj=11051952, unknown=8.0)
    RegisterGrace(grace_flag=11050003, obj=11051953, unknown=8.0)
    RegisterGrace(grace_flag=11050004, obj=11051954, unknown=8.0)
    RegisterGrace(grace_flag=11050005, obj=11051955, unknown=8.0)
    RunCommonEvent(0, 9005810, args=(11050800, 11050000, 11050950, 11051950, 8.0), arg_types="IIIIf")
    RunCommonEvent(0, 9005810, args=(11050850, 11050001, 11050951, 11051951, 8.0), arg_types="IIIIf")
    Event_11052800()
    Event_11052810()
    Event_11052811()
    Event_11052830()
    Event_11052849()
    Event_11052850()
    Event_11052860()
    Event_11052861()
    Event_11052859()
    RunCommonEvent(
        0,
        90005780,
        args=(11050800, 11052160, 11052161, 11050740, 20, 11052160, 11059350, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(11050800, 11052160, 11052161, 11050740), arg_types="IIII")
    RunCommonEvent(0, 90005784, args=(11052160, 11052805, 11050740, 11052800, 11052805, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005780,
        args=(11050800, 11052164, 11052165, 11050750, 20, 11052164, 10009719, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(11050800, 11052164, 11052165, 11050750), arg_types="IIII")
    RunCommonEvent(0, 90005784, args=(11052164, 11052805, 11050750, 11052800, 11052805, 0), arg_types="IIIIIi")
    RunCommonEvent(
        0,
        90005501,
        args=(11050525, 11051525, 0, 11051525, 11051526, 11051527, 11050526),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11050530, 11051530, 0, 11051530, 11051531, 11051532, 11050531),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11050535, 11051535, 1, 11051535, 11051536, 11051537, 11050536),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(11050610, 11051610, 2, 11051610, 11051611, 11051612, 11050611),
        arg_types="IIIIIII",
    )
    Event_11052510()
    RunCommonEvent(0, 90005511, args=(11050560, 11051560, 11053560, 227010, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(11050560, 11052560, 11052561), arg_types="III")
    Event_11052580()
    RunCommonEvent(0, 90005520, args=(11050578, 11051578, 11052578, 11052579), arg_types="IIII")
    Event_11052691()
    Event_11052692()
    RunCommonEvent(
        0,
        90005605,
        args=(11051680, 34, 15, 0, 0, 34152692, 11050000, 11052680, 11052681, 11052682, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_11053700(0, 11050801, 11050800, 11050800, 11052805, 90.0)
    Event_11053705(0, character=11050710)
    RunCommonEvent(0, 90005704, args=(11050710, 4201, 4200, 1040529251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(11050710, 4201, 4202, 1040529251, 4201, 4200, 4203, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(11050710, 4203, 4200, 4204), arg_types="IIII")
    Event_11053706(0, character=11050705)
    RunCommonEvent(0, 90005750, args=(11051700, 6450, 4900, 9500, 9500, 11059206, 806780), arg_types="IiiIIIi")
    Event_11053707()
    RunCommonEvent(0, 90005750, args=(11051700, 4110, 105000, 400500, 400500, 11059305, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 11053708, args=(11051740, 4110, 103700, 400370, 400370, 4208, 0, 4203), arg_types="IiiIIIiI")
    RunCommonEvent(0, 90005706, args=(11050721, 930025, 0), arg_types="IiI")
    RunCommonEvent(0, 90005706, args=(11050720, 930010, 0), arg_types="IiI")
    Event_11053710(0, character=11050850)
    Event_11053720()
    RunCommonEvent(0, 90005703, args=(11050730, 3941, 3942, 1039409251, 3941, 3940, 3943, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(11050730, 3941, 3940, 1039409251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(11050730, 3943, 3940, 3944), arg_types="IIII")
    Event_11053730(0, character=11050730)
    Event_11053731(0, 11050730)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(11050705)
    DisableBackread(11050710)
    DisableBackread(11050715)
    DisableBackread(11050720)
    DisableBackread(11050721)
    Event_11052500()
    RunCommonEvent(0, 90005251, args=(11050202, 3.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(11050203, 3.5, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005221, args=(11050205, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11050206, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11050207, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005221, args=(11050208, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005261, args=(11050240, 11052240, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(11050250, 11052240, 1.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(11050250, 11052240, 1.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(11050300, 30002, 20002, 11052300, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11050301, 30002, 20002, 11052301, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(11050302, 30002, 20002, 11052302, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")


@NeverRestart(11052500)
def Event_11052500():
    """Event 11052500"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11050500)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 9116)
    IfInsideMap(AND_1, game_map=LEYNDELL_ASHEN_CAPITAL)
    IfConditionTrue(MAIN, input_condition=AND_1)
    PlayCutscene(13000060, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(11050500)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    Wait(1.0)
    DisplayUnknownMessage_14(text=11050)


@NeverRestart(11052510)
def Event_11052510():
    """Event 11052510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            11050525,
            11051525,
            0,
            11051525,
            11051526,
            11053526,
            11051527,
            11053527,
            11052526,
            11052527,
            11050526,
            11052527,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005505,
        args=(11050530, 11051530, 0, 11051530, 11051531, 11053531, 11051532, 11053532, 11050531, 11052532, 0),
        arg_types="IIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            11050610,
            11051610,
            2,
            11051610,
            11051611,
            11053611,
            11051612,
            11053612,
            11052611,
            11052612,
            11050611,
            11052612,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(11052580)
def Event_11052580():
    """Event 11052580"""
    RegisterLadder(start_climbing_flag=11050580, stop_climbing_flag=11050581, obj=11051580)
    RegisterLadder(start_climbing_flag=11050582, stop_climbing_flag=11050583, obj=11051582)
    RegisterLadder(start_climbing_flag=11050584, stop_climbing_flag=11050585, obj=11051584)
    RegisterLadder(start_climbing_flag=11050586, stop_climbing_flag=11050587, obj=11051586)
    RegisterLadder(start_climbing_flag=11050588, stop_climbing_flag=11050589, obj=11051588)
    RegisterLadder(start_climbing_flag=11050590, stop_climbing_flag=11050591, obj=11051590)
    RegisterLadder(start_climbing_flag=11050592, stop_climbing_flag=11050593, obj=11051592)
    RegisterLadder(start_climbing_flag=11050594, stop_climbing_flag=11050595, obj=11051594)
    RegisterLadder(start_climbing_flag=11050596, stop_climbing_flag=11050597, obj=11051596)


@RestartOnRest(11052691)
def Event_11052691():
    """Event 11052691"""
    EnableObjectInvulnerability(11051691)


@RestartOnRest(11052692)
def Event_11052692():
    """Event 11052692"""
    DisableObjectActivation(11051535, obj_act_id=-1)
    DisableObjectActivation(11051536, obj_act_id=-1)
    DisableObjectActivation(11051537, obj_act_id=-1)


@NeverRestart(11052800)
def Event_11052800():
    """Event 11052800"""
    EndIfFlagEnabled(11050800)
    IfHealthValueLessThanOrEqual(MAIN, 11050800, value=0)
    Wait(4.0)
    PlaySoundEffect(11058000, 888880000, sound_type=SoundType.s_SFX)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 11050800)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 11050800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    KillBossAndDisplayBanner(character=11050800, banner_type=BannerType.HollowArenaWin)
    EnableFlag(11050800)
    EnableNetworkFlag(11050800)
    EnableFlag(9107)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61107)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    IfCharacterInsideRegion(AND_9, character=PLAYER, region=11052840)
    IfConditionTrue(MAIN, input_condition=AND_9)
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=False)


@RestartOnRest(11052810)
def Event_11052810():
    """Event 11052810"""
    GotoIfFlagDisabled(Label.L0, flag=11050800)
    DisableCharacter(11055800)
    DisableAnimations(11055800)
    Kill(11055800)
    DisableObject(11051820)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(11055800)
    DisableGravity(11050800)
    DisableAnimations(11050800)
    EnableImmortality(11050801)
    DisableAnimations(11050801)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown18)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown17)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfFlagEnabled(Label.L1, flag=11050801)
    DisableAnimations(11050801)
    ForceAnimation(11050801, 30010, unknown2=1.0)
    IfFlagEnabled(AND_1, 11052805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=11052801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    BanishInvaders(unknown=0)
    WaitFrames(frames=1)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=11050010,
        cutscene_flags=0,
        move_to_region=11052811,
        map_base_id=11050000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(11050010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(11050801)
    SkipLinesIfPlayerInOwnWorld(1)
    UnknownSound_2010_10(unk_0_4=472000, unk_4_8=-1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=7.5, unknown2=-37.15999984741211)
    DisableObject(11051820)
    EnableCharacter(11050801)
    EnableAnimations(11050801)
    Move(11050801, destination=11052815, destination_type=CoordEntityType.Region, copy_draw_parent=11050801)
    ForceAnimation(11050801, 20020, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(11051820)
    IfFlagEnabled(AND_2, 11052805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=11052800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAnimations(11050801)
    EnableAI(11050801)
    SetNetworkUpdateRate(11050801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(11050801, target_entity=11050800)
    DisableHealthBar(11050801)
    EnableBossHealthBar(11050800, name=904720000)


@RestartOnRest(11052811)
def Event_11052811():
    """Event 11052811"""
    EndIfFlagEnabled(11050800)
    IfHealthValueLessThanOrEqual(AND_1, 11050801, value=1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableAnimations(11050801)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=11050020,
        cutscene_flags=0,
        move_to_region=11052816,
        map_base_id=11050000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(11050020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(11052802)
    DisableCharacter(11050801)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=8.09000015258789, unknown2=-37.15999984741211)
    EnableCharacter(11050800)
    WaitFrames(frames=1)
    EnableGravity(11050800)
    Move(11050800, destination=11052815, destination_type=CoordEntityType.Region, copy_draw_parent=11050800)
    WaitFrames(frames=1)
    EnableAnimations(11050800)
    ForceAnimation(11050800, 20020, unknown2=1.0)
    EnableAI(11050800)
    EnableBossHealthBar(11050800, name=904720001)


@RestartOnRest(11052830)
def Event_11052830():
    """Event 11052830"""
    DisableNetworkSync()
    EndIfFlagEnabled(11050800)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 11052805)
    IfFlagDisabled(AND_1, 11050800)
    IfPlayerNotInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, 11052806)
    IfFlagDisabled(AND_2, 11050800)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    ChangeCamera(normal_camera_id=4721, locked_camera_id=4721)
    IfCharacterHasSpecialEffect(AND_4, 11050800, 12298)
    IfFlagDisabled(AND_4, 11050800)
    IfConditionTrue(MAIN, input_condition=AND_4)
    ChangeCamera(normal_camera_id=4725, locked_camera_id=4725)
    IfCharacterHasSpecialEffect(AND_4, 11050800, 12298)
    IfFlagDisabled(AND_4, 11050800)
    IfConditionFalse(MAIN, input_condition=AND_4)
    Restart()


@RestartOnRest(11052849)
def Event_11052849():
    """Event 11052849"""
    RunCommonEvent(
        0,
        9005800,
        args=(11050800, 11051800, 11052800, 11052805, 11055800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(11050800, 11051800, 11052800, 11052805, 11052806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(11050800, 11051800, 17, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005813, args=(11050800, 11051801, 18, 11050801, 18), arg_types="IIiIi")
    RunCommonEvent(
        0,
        9005822,
        args=(11050800, 472000, 11052805, 11052806, 11050801, 11052802, 1, 1),
        arg_types="IiIIIIii",
    )


@RestartOnRest(11052850)
def Event_11052850():
    """Event 11052850"""
    EndIfFlagEnabled(11050850)
    IfHealthValueLessThanOrEqual(MAIN, 11050850, value=0)
    Wait(4.0)
    PlaySoundEffect(11058050, 888880000, sound_type=SoundType.s_SFX)
    AddSpecialEffect(20000, 1899)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 11050850)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9646)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, 11050850)
    IfConditionTrue(MAIN, input_condition=OR_2)
    KillBossAndDisplayBanner(character=11050850, banner_type=BannerType.Unknown)
    SetBackreadStateAlternate(11050850, False)
    EnableNetworkFlag(11050850)
    EnableFlag(9106)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61106)


@RestartOnRest(11052860)
def Event_11052860():
    """Event 11052860"""
    GotoIfFlagDisabled(Label.L0, flag=11050850)
    DisableCharacter(11055850)
    DisableAnimations(11055850)
    Kill(11055850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(11055851)
    DisableAnimations(11055851)
    DisableAI(11055850)
    SetBackreadStateAlternate(11050850, True)
    IfFlagEnabled(AND_8, 9120)
    IfFlagEnabled(AND_8, 9122)
    IfFlagEnabled(AND_8, 9112)
    GotoIfConditionTrue(Label.L8, input_condition=AND_8)
    IfFlagDisabled(AND_7, 9120)
    IfFlagEnabled(AND_7, 9122)
    IfFlagEnabled(AND_7, 9112)
    GotoIfConditionTrue(Label.L7, input_condition=AND_7)
    IfFlagEnabled(AND_6, 9120)
    IfFlagDisabled(AND_6, 9122)
    IfFlagEnabled(AND_6, 9112)
    GotoIfConditionTrue(Label.L6, input_condition=AND_6)
    IfFlagEnabled(AND_5, 9120)
    IfFlagEnabled(AND_5, 9122)
    IfFlagDisabled(AND_5, 9112)
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    IfFlagDisabled(AND_4, 9120)
    IfFlagDisabled(AND_4, 9122)
    IfFlagEnabled(AND_4, 9112)
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    IfFlagEnabled(AND_3, 9120)
    IfFlagDisabled(AND_3, 9122)
    IfFlagDisabled(AND_3, 9112)
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    IfFlagDisabled(AND_2, 9120)
    IfFlagEnabled(AND_2, 9122)
    IfFlagDisabled(AND_2, 9112)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L1)

    # --- Label 2 --- #
    DefineLabel(2)
    Unknown_2004_67(character=11050851, entity=11050850)
    Goto(Label.L1)

    # --- Label 3 --- #
    DefineLabel(3)
    Unknown_2004_67(character=11050852, entity=11050850)
    Goto(Label.L1)

    # --- Label 4 --- #
    DefineLabel(4)
    Unknown_2004_67(character=11050853, entity=11050850)
    Goto(Label.L1)

    # --- Label 5 --- #
    DefineLabel(5)
    Unknown_2004_67(character=11050854, entity=11050850)
    Goto(Label.L1)

    # --- Label 6 --- #
    DefineLabel(6)
    Unknown_2004_67(character=11050855, entity=11050850)
    Goto(Label.L1)

    # --- Label 7 --- #
    DefineLabel(7)
    Unknown_2004_67(character=11050856, entity=11050850)
    Goto(Label.L1)

    # --- Label 8 --- #
    DefineLabel(8)
    Unknown_2004_67(character=11050857, entity=11050850)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L1, flag=11050851)
    ForceAnimation(11050850, 90102, loop=True, unknown2=1.0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(11050854)
    IfPlayerInOwnWorld(AND_11)
    IfCharacterHasSpecialEffect(AND_11, 11050850, 9770)
    IfConditionTrue(OR_11, input_condition=AND_11)
    IfAttackedWithDamageType(OR_11, attacked_entity=11050850, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_11)
    EnableNetworkFlag(11050851)
    AddSpecialEffect(11050850, 9644)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_12, 11052855)
    IfCharacterInsideRegion(OR_12, character=PLAYER, region=11052850)
    IfCharacterInsideRegion(OR_12, character=PLAYER, region=11052855)
    IfConditionTrue(MAIN, input_condition=OR_12)
    IfConditionTrue(MAIN, input_condition=AND_12)

    # --- Label 10 --- #
    DefineLabel(10)
    SetTeamType(11050850, TeamType.Enemy)
    EnableAI(11050850)
    SetNetworkUpdateRate(11055850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(11050850, name=132400)


@RestartOnRest(11052861)
def Event_11052861():
    """Event 11052861"""
    EndIfFlagEnabled(11050850)
    IfHealthRatioLessThanOrEqual(AND_1, 11050850, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(11052852)


@RestartOnRest(11052859)
def Event_11052859():
    """Event 11052859"""
    RunCommonEvent(
        0,
        9005800,
        args=(11050850, 11051850, 11052850, 11052855, 11055850, 10000, 11050851, 0),
        arg_types="IIIIIiII",
    )
    SkipLinesIfFlagEnabled(2, 11050851)
    RunCommonEvent(
        0,
        9005800,
        args=(11050850, 11051851, 11052855, 11052855, 11055850, 10000, 6000, 0),
        arg_types="IIIIIiII",
    )
    SkipLines(1)
    RunCommonEvent(
        0,
        9005800,
        args=(11050850, 11051851, 11052855, 11052855, 11055850, 10000, 11050851, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(11050850, 11051850, 11052850, 11052855, 11052856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005801, args=(11050850, 11051851, 11052855, 11052855, 11052856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(11050850, 11051850, 5, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11050850, 11051851, 4, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11050850, 11051852, 4, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11050850, 11051853, 8, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11050850, 11051854, 4, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11050850, 11051855, 5, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(11050850, 11051856, 5, 11050854), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(11050850, 921100, 11052855, 11052856, 0, 11052852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(11053700)
def Event_11053700(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 11053700"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=character, distance=17.0)
    SkipLinesIfUnsignedEqual(1, left=0, right=character_1)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    EndIfFlagEnabled(flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, flag_1)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    SkipLinesIfUnsignedEqual(1, left=0, right=character_1)
    SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(11053705)
def Event_11053705(_, character: uint):
    """Event 11053705"""
    WaitFrames(frames=1)
    DisableFlag(11059200)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4210)
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90102, unknown2=1.0)
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
    IfFlagEnabled(MAIN, 11059200)
    Restart()


@RestartOnRest(11053706)
def Event_11053706(_, character: uint):
    """Event 11053706"""
    WaitFrames(frames=1)
    DisableFlag(11059200)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagDisabled(AND_1, 4203)
    IfFlagEnabled(OR_1, 4210)
    IfFlagEnabled(OR_1, 4211)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_2, 4203)
    IfFlagDisabled(AND_2, 4217)
    IfFlagEnabled(AND_2, 118)
    IfFlagEnabled(AND_2, 11009555)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    SkipLinesIfConditionTrue(5, OR_2)
    DisableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.NoTeam)
    ForceAnimation(character, 930002, unknown2=1.0)
    DisableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    EnableNetworkFlag(11059304)
    EnableNetworkFlag(11059206)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, 11059200)
    Restart()


@RestartOnRest(11053707)
def Event_11053707():
    """Event 11053707"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400500)
    EndIfFlagDisabled(9500)
    EnableNetworkFlag(11059305)
    End()


@NeverRestart(11053708)
def Event_11053708(
    _,
    obj: uint,
    action_button_id: int,
    item_lot_param_id: int,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    model_point: int,
    flag_1: uint,
):
    """Event 11053708"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagRangeAnyDisabled(AND_1, flag_range=(first_flag, last_flag))
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfValueEqual(2, left=model_point, right=0)
    CreateObjectVFX(obj, vfx_id=90, model_point=model_point)
    SkipLines(1)
    CreateObjectVFX(obj, vfx_id=90, model_point=6101)
    IfFlagDisabled(OR_2, flag)
    IfFlagRangeAllEnabled(OR_2, flag_range=(first_flag, last_flag))
    IfActionButtonParamActivated(OR_1, action_button_id=action_button_id, entity=obj)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    DeleteObjectVFX(obj)
    AwardItemLot(item_lot_param_id, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj)
    Restart()


@RestartOnRest(11053710)
def Event_11053710(_, character: uint):
    """Event 11053710"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.Off)
    IfThisEventSlotFlagEnabled(MAIN)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableNetworkFlag(11050854)

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Enemy)


@RestartOnRest(11053720)
def Event_11053720():
    """Event 11053720"""
    DisableFlag(11059350)
    WaitFrames(frames=1)
    EndIfFlagDisabled(3631)
    EndIfFlagEnabled(11050800)
    EndIfFlagDisabled(35000500)
    EndIfFlagEnabled(3621)
    EndIfFlagEnabled(1049539212)
    EndIfFlagEnabled(116)
    EnableFlag(11059350)
    End()


@RestartOnRest(11053730)
def Event_11053730(_, character: uint):
    """Event 11053730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SkipLinesIfFlagDisabled(1, 3940)
    DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3947)
    IfFlagEnabled(MAIN, 3947)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3957)
    SkipLinesIfFlagEnabled(3, 11109819)
    IfFlagEnabled(AND_6, 71122)
    IfFlagEnabled(AND_6, 9000)
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    EnableNetworkFlag(11109819)
    EnableNetworkFlag(3957)
    Goto(Label.L20)

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
    IfFlagDisabled(MAIN, 3947)
    Restart()


@RestartOnRest(11053731)
def Event_11053731(_, entity: uint):
    """Event 11053731"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 3943)
    IfFlagDisabled(OR_1, 3947)
    IfFlagEnabled(OR_1, 1039409259)
    EndIfConditionTrue(input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=20000, radius=4.0)
    IfCharacterHasSpecialEffect(AND_1, 20000, 9690)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()
