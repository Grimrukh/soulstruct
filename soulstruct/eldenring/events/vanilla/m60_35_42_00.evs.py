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
    Event_1035422150()
    RegisterGrace(grace_flag=1035420000, obj=1035421950, unknown=5.0)
    RunCommonEvent(0, 90005870, args=(1035420800, 904820600, 5), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1035420800, 0, 1035420800, 0, 30225, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005300, args=(1035420220, 1035420220, 40208, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005780,
        args=(1035420800, 1035422160, 1035422161, 1035420710, 20, 1035422700, 1034429209, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1035420800, 1035422160, 1035422161, 1035420710), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1035420800, 1035422160, 1035422161, 1035420710, 1035422700, 1035422160, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005704, args=(1035420700, 3541, 3540, 1035429201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1035420700, 3541, 3542, 1035429201, 3541, 3540, 3544, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1035420700, 3543, 3540, 3544), arg_types="IIII")
    Event_1035423700(0, character=1035420700, obj=1035421700)
    Event_1035420701(0, character=1035420700, obj=1035421700)
    Event_1035423702(0, character=1035420700)
    Event_1035423703(0, entity=1035420700)
    Event_1035420710(0, character=1035420706)
    RunCommonEvent(0, 90005704, args=(1035420706, 3741, 3740, 1035429251, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005707,
        args=(1035420706, 3741, 3742, 1035429251, 3741, 3740, 3743, 0, 20007, 1035422712, 1035422713),
        arg_types="IIIIIIIiiII",
    )
    RunCommonEvent(0, 90005709, args=(1035420706, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1035420706, 960, 603050), arg_types="Iii")
    RunCommonEvent(0, 90005750, args=(1035421710, 4350, 103930, 400393, 400393, 1035429255, 0), arg_types="IiiIIIi")
    Event_1035420711(0, entity=1035420706)
    Event_1035420712()
    Event_1035422151()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1035420700)
    DisableBackread(1035420705)
    DisableBackread(1035420706)
    RunCommonEvent(0, 90005260, args=(1035420800, 1035422800, 42.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1035420201, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1035420202, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035420203, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1035420204, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1035420205, 30004, 20004, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(1035420206, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035420207, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1035420208, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1035420209, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035420210, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035420211, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035420212, 1035422204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035420315, 1035422315, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035420317, 1035422317, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1035420370, 30003, 20003, 1035422370, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1035420374, 30003, 20003, 1035422374, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@NeverRestart(1035422150)
def Event_1035422150():
    """Event 1035422150"""
    GotoIfFlagDisabled(Label.L0, flag=1035420150)
    ForceAnimation(1035420150, 30011, unknown2=1.0)
    EnableInvincibility(1035420150)
    SetDisplayMask(1042350150, bit_index=10, switch_type=OnOffChange.Off)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableNetworkConnectedFlagRange(flag_range=(780000, 780009))
    ForceAnimation(1035420150, 30010, unknown2=1.0)
    EnableInvincibility(1035420150)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9630, entity=1035421152)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfUnknownCondition_34(OR_10, unk_4_8=90100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=91100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=630100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=631100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=890100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=900100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=901100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=902100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=903100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=960100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=961100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=962100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=990100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=991100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1000100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=963100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=964100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=220100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=221100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1990100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1991100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=290100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=291100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=292100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=390100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=430100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1010100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1011100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=293100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=294100, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=260200, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1070200, unk_8_12=-1)
    IfUnknownCondition_34(OR_10, unk_4_8=1890200, unk_8_12=-1)
    SkipLinesIfConditionTrue(3, OR_10)
    EnableNetworkFlag(780000)
    DisableNetworkFlag(780001)
    Goto(Label.L10)
    DisableNetworkFlag(780000)
    EnableNetworkFlag(780001)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=12060000,
        cutscene_flags=0,
        move_to_region=1035422152,
        map_base_id=60354200,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    PlayCutscene(12060000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    UnknownCamera_4(unknown1=34.79999923706055, unknown2=-136.3699951171875)
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    ForceAnimation(PLAYER, 67100, unknown2=1.0)
    DisableNetworkConnectedFlagRange(flag_range=(780000, 780009))
    RemoveGoodFromPlayer(item=8121, quantity=1)
    EnableFlag(1035420150)


@NeverRestart(1035422151)
def Event_1035422151():
    """Event 1035422151"""
    GotoIfFlagDisabled(Label.L0, flag=1035420150)
    DisableObject(1035421151)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(MAIN, 1035420150)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableObject(1035421151)


@NeverRestart(1035420200)
def Event_1035420200():
    """Event 1035420200"""
    IfOutsideMap(AND_2, game_map=SOUTHWEST_LIURNIA_NE_SE)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1035422300)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=1035422300)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    Unknown_2003_68(unknown1=11, unknown2=-1.0, unknown3=1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=1)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(1.0)
    Restart()


@RestartOnRest(1035423700)
def Event_1035423700(_, character: uint, obj: uint):
    """Event 1035423700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3540)
    DisableFlag(1035429205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3545)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 3545)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3540)
    GotoIfFlagEnabled(Label.L2, flag=3541)
    GotoIfFlagEnabled(Label.L3, flag=3542)
    GotoIfFlagEnabled(Label.L4, flag=3543)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L11, flag=1035420701)
    Goto(Label.L12)

    # --- Label 11 --- #
    DefineLabel(11)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableObject(obj)
    DisableAnimations(character)
    ForceAnimation(character, 930022, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 12 --- #
    DefineLabel(12)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930020, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3545)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1035420701)
def Event_1035420701(_, character: uint, obj: uint):
    """Event 1035420701"""
    DisableObject(1035421701)
    GotoIfFlagEnabled(Label.L1, flag=1035420701)
    EnableObject(1035421701)
    CreateObjectVFX(1035421701, vfx_id=100, model_point=600904)
    IfPlayerInOwnWorld(AND_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=obj, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1035420701)
    DisableGravity(character)
    DisableAnimations(character)
    EnableCharacterCollision(character)
    ForceAnimation(obj, 1, unknown2=1.0)
    Wait(1.0)
    DeleteObjectVFX(1035421701)
    ForceAnimation(character, 20042, unknown2=1.0)
    EnableCharacter(character)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=302603, anchor_entity=character, model_point=220, anchor_type=CoordEntityType.Character)
    Wait(1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)
    WaitFrames(frames=1)
    EnableGravity(character)
    EnableAnimations(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(1035423702)
def Event_1035423702(_, character: uint):
    """Event 1035423702"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3540)
    EndIfFlagDisabled(3545)
    IfFlagEnabled(MAIN, 1035429210)
    DisableAnimations(character)
    ForceAnimation(character, 20054, unknown2=1.0)
    Wait(5.0)
    DisableNetworkConnectedFlagRange(flag_range=(3540, 3544))
    EnableNetworkFlag(3543)
    SaveRequest()
    Wait(5.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1035423703)
def Event_1035423703(_, entity: uint):
    """Event 1035423703"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3545)
    EndIfFlagDisabled(3540)
    IfFlagEnabled(MAIN, 3541)
    ForceAnimation(entity, 20052, unknown2=1.0)
    Restart()


@RestartOnRest(1035420710)
def Event_1035420710(_, character: uint):
    """Event 1035420710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3740)
    DisableFlag(1035429252)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L10, flag=3750)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3750)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=3740)
    GotoIfFlagEnabled(Label.L1, flag=3741)
    GotoIfFlagEnabled(Label.L2, flag=3742)
    GotoIfFlagEnabled(Label.L3, flag=3743)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    SkipLinesIfFlagEnabled(2, 1035422714)
    ForceAnimation(character, 930002, unknown2=1.0)
    SkipLines(2)
    ForceAnimation(character, 20009, unknown2=1.0)
    Unknown_2004_73(entity=character, unk_4_8=0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    EnableImmortality(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3750)
    Restart()


@RestartOnRest(1035420711)
def Event_1035420711(_, entity: uint):
    """Event 1035420711"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509406)
    IfFlagEnabled(MAIN, 1034509406)
    ForceAnimation(entity, 20007, unknown2=1.0)
    Wait(6.0)
    EnableFlag(1035429255)


@RestartOnRest(1035420712)
def Event_1035420712():
    """Event 1035420712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1035420150)
    IfFlagEnabled(MAIN, 1035420150)
    EnableFlag(3758)
    EnableNetworkFlag(1035422714)


@RestartOnRest(1035420720)
def Event_1035420720(_, character: uint, obj: uint):
    """Event 1035420720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagEnabled(1, 4220)
    DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 4227)
    IfFlagDisabled(OR_1, 1035422160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(AND_2, 4227)
    IfFlagDisabled(OR_2, 1035422160)
    IfConditionTrue(AND_2, input_condition=OR_2)
    AwaitConditionTrue(AND_2)
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
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(OR_15, 4227)
    IfFlagEnabled(OR_15, 1035422160)
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(1035420721)
def Event_1035420721():
    """Event 1035420721"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(4221, 4223))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034429209)
    End()
