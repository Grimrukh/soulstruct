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
    RegisterGrace(grace_flag=1035470000, obj=1035471950, unknown=5.0)
    Event_1035472580()
    Event_1035472205()
    Event_1035472206(0, flag=1035470201, attacked_entity=1035470201)
    Event_1035472206(1, flag=1035470202, attacked_entity=1035470202)
    Event_1035472207(0, flag=1035475200, character=1035470200)
    Event_1035472207(1, flag=1035475201, character=1035470201)
    Event_1035472207(2, flag=1035475202, character=1035470202)
    Event_1035472220()
    Event_1035472221()
    Event_1035472222()
    Event_1035472200()
    Event_1035472210()
    RunCommonEvent(0, 90005300, args=(1035470200, 1035470200, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1035470201, 1035470201, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1035470202, 1035470202, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1035470220, 1035470220, 0, 0.0, 0), arg_types="IIifi")
    Event_1035472240(
        0,
        character=1035470260,
        special_effect=12603,
        region=1035472240,
        region_1=1035472241,
        region_2=1035472242
    )
    RunCommonEvent(0, 90005300, args=(1035470260, 1035470260, 40210, 0.0, 0), arg_types="IIifi")
    Event_1035472270()
    Event_1035472270(slot=1)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005251, args=(1035470201, 3.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035470202, 3.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035470210, 3.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035470211, 3.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035470212, 3.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035470218, 3.0, 0.0, 0), arg_types="Iffi")


@NeverRestart(1035472200)
def Event_1035472200():
    """Event 1035472200"""
    DisableNetworkSync()
    SkipLinesIfFlagDisabled(2, 1035470215)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    End()
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=1035472200)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfUnknownCondition_31(OR_1, hours=11, unknown1=0.0, unknown2=0)
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    Unknown_2003_68(unknown1=11, unknown2=-1.0, unknown3=0)

    # --- Label 1 --- #
    DefineLabel(1)
    Restart()


@RestartOnRest(1035472205)
def Event_1035472205():
    """Event 1035472205"""
    EndIfFlagEnabled(1035470200)
    ForceAnimation(1035470200, 30006, unknown2=1.0)
    EnableImmortality(1035470220)
    DisableHealthBar(1035470220)
    IfAttackedWithDamageType(OR_15, attacked_entity=1035470200, attacker=PLAYER)
    IfAttackedWithDamageType(OR_15, attacked_entity=1035470220, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_15)
    ForceAnimation(1035470200, 20006, unknown2=1.0)
    DisableCharacter(1035470220)
    EnableFlag(1035470200)
    EnableFlag(1035470220)
    End()


@RestartOnRest(1035472206)
def Event_1035472206(_, flag: uint, attacked_entity: uint):
    """Event 1035472206"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=PLAYER)
    DisableAnimations(attacked_entity)
    ForceAnimation(attacked_entity, 20008, unknown2=1.0)
    EnableFlag(flag)


@RestartOnRest(1035472207)
def Event_1035472207(_, flag: uint, character: uint):
    """Event 1035472207"""
    DisableCharacter(character)
    DisableCharacter(1035470220)
    EndIfFlagEnabled(flag)
    SkipLinesIfPlayerInOwnWorld(2)
    EnableInvincibility(character)
    EnableInvincibility(1035470220)
    IfFlagEnabled(AND_1, 1035472211)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    EnableCharacter(1035470220)


@RestartOnRest(1035472210)
def Event_1035472210():
    """Event 1035472210"""
    GotoIfFlagDisabled(Label.L0, flag=1035470215)
    DisableCharacter(1035475210)
    DisableSpawner(entity=1035473210)
    DisableSpawner(entity=1035473211)
    DisableSpawner(entity=1035473212)
    DisableSpawner(entity=1035473213)
    DisableSpawner(entity=1035473214)
    DisableSpawner(entity=1035473215)
    DisableSpawner(entity=1035473216)
    DisableSpawner(entity=1035473217)
    DisableSpawner(entity=1035473218)
    DisableSpawner(entity=1035473219)
    DisableSpawner(entity=1035473220)
    DisableSpawner(entity=1035473221)
    DisableSpawner(entity=1035473222)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(1035470210)
    DisableCharacter(1035470211)
    DisableCharacter(1035470212)
    DisableSpawner(entity=1035473210)
    DisableSpawner(entity=1035473211)
    DisableSpawner(entity=1035473212)
    DisableSpawner(entity=1035473213)
    DisableSpawner(entity=1035473214)
    DisableSpawner(entity=1035473215)
    DisableSpawner(entity=1035473216)
    DisableSpawner(entity=1035473217)
    DisableSpawner(entity=1035473218)
    DisableSpawner(entity=1035473219)
    DisableSpawner(entity=1035473220)
    DisableSpawner(entity=1035473221)
    DisableSpawner(entity=1035473222)
    IfFlagEnabled(AND_1, 1035472211)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(1035470210)
    EnableCharacter(1035470211)
    EnableCharacter(1035470212)
    EnableSpawner(entity=1035473210)
    EnableSpawner(entity=1035473211)
    EnableSpawner(entity=1035473212)
    EnableSpawner(entity=1035473213)
    EnableSpawner(entity=1035473214)
    EnableSpawner(entity=1035473215)
    EnableSpawner(entity=1035473216)
    EnableSpawner(entity=1035473217)
    EnableSpawner(entity=1035473218)
    EnableSpawner(entity=1035473219)
    EnableSpawner(entity=1035473220)
    EnableSpawner(entity=1035473221)
    EnableSpawner(entity=1035473222)
    End()


@RestartOnRest(1035472220)
def Event_1035472220():
    """Event 1035472220"""
    GotoIfFlagDisabled(Label.L0, flag=1035470215)
    DisableObject(1035471210)
    DeleteObjectVFX(1035471210)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(1035471210)
    CreateObjectVFX(1035471210, vfx_id=200, model_point=1500)
    IfFlagEnabled(AND_1, 1035470200)
    IfFlagEnabled(AND_1, 1035470201)
    IfFlagEnabled(AND_1, 1035470202)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1035470215)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
    PlaySoundEffect(1035471210, 1500, sound_type=SoundType.s_SFX)
    DisableObject(1035471210)
    DeleteObjectVFX(1035471210)
    Kill(1035475210)
    DisableSpawner(entity=1035473210)
    DisableSpawner(entity=1035473211)
    DisableSpawner(entity=1035473212)
    DisableSpawner(entity=1035473213)
    DisableSpawner(entity=1035473214)
    DisableSpawner(entity=1035473215)
    DisableSpawner(entity=1035473216)
    DisableSpawner(entity=1035473217)
    DisableSpawner(entity=1035473218)
    DisableSpawner(entity=1035473219)
    DisableSpawner(entity=1035473220)
    DisableSpawner(entity=1035473221)
    DisableSpawner(entity=1035473222)
    End()


@RestartOnRest(1035472221)
def Event_1035472221():
    """Event 1035472221"""
    DisableNetworkSync()
    EndIfFlagEnabled(1035470215)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=1035471210)
    IfFlagEnabled(OR_1, 1035470215)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1035470215)
    DisplayDialog(text=20200, anchor_entity=1035471210)
    Wait(1.0)
    Restart()


@RestartOnRest(1035472222)
def Event_1035472222():
    """Event 1035472222"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9210, entity=1035471211)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=60011, anchor_entity=1035471211)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(1035472211)
    Wait(1.0)
    Restart()


@NeverRestart(1035472240)
def Event_1035472240(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1035472240"""
    EndIfFlagEnabled(1035470260)
    IfCharacterHasSpecialEffect(AND_2, character, special_effect)
    IfCharacterAlive(AND_2, character)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableFlag(1035472241)
    DisableFlag(1035472242)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1035472241, 1035472242))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1035472241)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1035472241)
    SkipLines(3)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1035472241)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1035472270)
def Event_1035472270():
    """Event 1035472270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1035470270)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1035472270)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1035470270,
        source_entity=1035472271,
        model_point=900,
        behavior_id=802102070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1035472580)
def Event_1035472580():
    """Event 1035472580"""
    RegisterLadder(start_climbing_flag=1035470580, stop_climbing_flag=1035470581, obj=1035471580)
