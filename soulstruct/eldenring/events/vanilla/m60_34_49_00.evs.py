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
    RegisterGrace(grace_flag=1034490000, obj=1034491950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76214, 76213, 1034491980, 77220, 3, 78220, 78221, 78222, 78223, 78224, 78225, 78226, 78227, 78228, 78229),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1034492290(
        0,
        source_entity=1034491333,
        region=1034492200,
        flag=1034492281,
        flag_1=1034492282,
        flag_2=1034492283,
        frames=2
    )
    Event_1034492290(
        1,
        source_entity=1034491301,
        region=1034492201,
        flag=1034492282,
        flag_1=1034492283,
        flag_2=6001,
        frames=1
    )
    Event_1034492290(2, source_entity=1035491500, region=1035492200, flag=1034492283, flag_1=6001, flag_2=6001, frames=0)
    Event_1034492270(0, 4.300000190734863, 1034492281)
    Event_1034492270(1, 2.5, 1034492282)
    Event_1034492270(2, 2.5, 1034492283)
    Event_1034492270(3, 2.4000000953674316, 1034492284)
    RunCommonEvent(0, 90005704, args=(1034490700, 3761, 3760, 1034499201, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005707,
        args=(1034490700, 3761, 3762, 1034499201, 3763, 3760, 3763, -1, 20046, 1034492703, 1034492704),
        arg_types="IIIIIIIiiII",
    )
    Event_1034490700(0, character=1034490700)
    RunCommonEvent(0, 90005709, args=(1034490700, 905, 603002), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1034490700, 960, 603052), arg_types="Iii")
    RunCommonEvent(0, 90005704, args=(1034490711, 3761, 3760, 1034499203, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005707,
        args=(1034490711, 3761, 3762, 1034499203, 3763, 3760, 3763, -1, 20046, 1034492703, 1034492704),
        arg_types="IIIIIIIiiII",
    )
    Event_1034490701(
        0,
        character=1034490711,
        destination=1034492700,
        character_1=1034490701,
        character_2=1034490702,
        character_3=1034490703
    )
    RunCommonEvent(0, 90005709, args=(1034490711, 905, 603002), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1034490711, 960, 603052), arg_types="Iii")
    RunCommonEvent(0, 90005708, args=(1034490700, 3760, 0), arg_types="III")
    RunCommonEvent(0, 90005708, args=(1034490711, 3760, 0), arg_types="III")
    RunCommonEvent(0, 90005750, args=(1034491700, 6361, 102400, 400240, 400241, 3768, 0), arg_types="IiiIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1034490700)
    DisableBackread(1034490701)
    DisableBackread(1034490702)
    DisableBackread(1034490703)
    DisableBackread(1034490711)
    Event_1034492210(0, 1034490301)


@RestartOnRest(1034492210)
def Event_1034492210(_, character__unk_0_4: uint):
    """Event 1034492210"""
    EnableNetworkSync()
    SetBackreadStateAlternate(character__unk_0_4, True)
    Unknown_2004_63(unk_0_4=character__unk_0_4, unk_4_8=230.0)
    Unknown_2004_69(unk_0_4=character__unk_0_4, unk_4_8=0)
    Unknown_2004_70(unk_0_4=character__unk_0_4, unk_4_8=1)
    DisableGravity(character__unk_0_4)


@RestartOnRest(1034492270)
def Event_1034492270(_, seconds: float, flag: uint):
    """Event 1034492270"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkSync()
    EndIfFlagEnabled(1035500800)
    IfFlagDisabled(MAIN, flag)
    Wait(seconds)
    EnableNetworkFlag(flag)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1034492290)
def Event_1034492290(_, source_entity: uint, region: uint, flag: uint, flag_1: uint, flag_2: uint, frames: int):
    """Event 1034492290"""
    EnableNetworkSync()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, 1034492284)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(1035500800)
    WaitFramesAfterCutscene(frames=frames)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    GotoIfFlagDisabled(Label.L1, flag=flag_2)
    IfNewGameCycleEqual(AND_2, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_3, completion_count=1)
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_4, completion_count=2)
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_5, completion_count=3)
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_6, completion_count=4)
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_7, completion_count=5)
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_8, completion_count=6)
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleGreaterThanOrEqual(AND_10, completion_count=7)
    SkipLinesIfConditionFalse(2, AND_10)
    ShootProjectile(
        owner_entity=1034490301,
        source_entity=source_entity,
        model_point=90,
        behavior_id=802600070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkFlag(flag)
    DisableNetworkFlag(1034492284)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()


@RestartOnRest(1034492340)
def Event_1034492340(_, character: uint):
    """Event 1034492340"""
    Kill(character, award_souls=True)


@RestartOnRest(1034490700)
def Event_1034490700(_, character: uint):
    """Event 1034490700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3760)
    DisableFlag(1034499202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=3765)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3765)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3760)
    GotoIfFlagEnabled(Label.L1, flag=3761)
    GotoIfFlagEnabled(Label.L2, flag=3762)
    GotoIfFlagEnabled(Label.L3, flag=3763)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    ForceAnimation(character, 930017, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3765)
    Restart()


@RestartOnRest(1034490701)
def Event_1034490701(_, character: uint, destination: uint, character_1: uint, character_2: uint, character_3: uint):
    """Event 1034490701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3760)
    DisableFlag(1034499204)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3766)
    GotoIfFlagEnabled(Label.L7, flag=3767)
    GotoIfFlagEnabled(Label.L8, flag=3768)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3766, 3768))
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 7 --- #
    DefineLabel(7)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    GotoIfFlagEnabled(Label.L0, flag=3760)
    GotoIfFlagEnabled(Label.L1, flag=3761)
    GotoIfFlagEnabled(Label.L2, flag=3762)
    GotoIfFlagEnabled(Label.L3, flag=3763)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    ForceAnimation(character, 930017, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3766, 3767))
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 930019, unknown2=1.0)
    SetTeamType(character, TeamType.NoTeam)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 930002, unknown2=1.0)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    ForceAnimation(character_2, 930002, unknown2=1.0)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    ForceAnimation(character_3, 930002, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3768)
    Restart()


@RestartOnRest(1034493704)
def Event_1034493704(_, character: uint):
    """Event 1034493704"""
    IfFlagEnabled(OR_1, 1034499236)
    IfFlagEnabled(OR_1, 1034499237)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetTeamType(character, TeamType.FriendlyNPC)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    SkipLinesIfFlagDisabled(1, 1034499236)
    CreateTemporaryVFX(vfx_id=646060, anchor_entity=character, model_point=960, anchor_type=CoordEntityType.Character)
    SkipLinesIfFlagDisabled(1, 1034499237)
    CreateTemporaryVFX(vfx_id=641111, anchor_entity=character, model_point=960, anchor_type=CoordEntityType.Character)
    Restart()
