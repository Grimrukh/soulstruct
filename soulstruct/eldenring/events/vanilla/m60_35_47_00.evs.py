"""
West Liurnia (NE) (NE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_35_47_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1035470000, asset=Assets.AEG099_060_9000)
    Event_1035472580()
    Event_1035472205()
    Event_1035472206(0, flag=1035470201, attacked_entity=Characters.Turtle1)
    Event_1035472206(1, flag=1035470202, attacked_entity=Characters.Turtle2)
    Event_1035472207(0, flag=1035475200, character=Characters.Turtle0)
    Event_1035472207(1, flag=1035475201, character=Characters.Turtle1)
    Event_1035472207(2, flag=1035475202, character=Characters.Turtle2)
    Event_1035472220()
    Event_1035472221()
    Event_1035472222()
    Event_1035472200()
    Event_1035472210()
    CommonFunc_90005300(0, flag=1035470200, character=Characters.Turtle0, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1035470201, character=Characters.Turtle1, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1035470202, character=Characters.Turtle2, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1035470220, character=Characters.Scarab1, item_lot=0, seconds=0.0, left=0)
    Event_1035472240(
        0,
        character=Characters.Scarab0,
        special_effect=12603,
        region=1035472240,
        region_1=1035472241,
        region_2=1035472242,
    )
    CommonFunc_90005300(0, flag=1035470260, character=Characters.Scarab0, item_lot=40210, seconds=0.0, left=0)
    Event_1035472270()
    Event_1035472270(slot=1)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005251(0, character=Characters.Turtle1, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.Turtle2, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.PutridCorpse0, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.PutridCorpse1, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.PutridCorpse2, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, 1035470218, 3.0, 0.0, 0)


@ContinueOnRest(1035472200)
def Event_1035472200():
    """Event 1035472200"""
    DisableNetworkSync()
    if FlagEnabled(1035470215):
        SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
        End()
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=1035472200)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(WeatherState(weather=Weather.HeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    SetWeather(weather=Weather.HeavyFog, duration=-1.0, immediate_change=False)

    # --- Label 1 --- #
    DefineLabel(1)
    Restart()


@RestartOnRest(1035472205)
def Event_1035472205():
    """Event 1035472205"""
    if FlagEnabled(1035470200):
        return
    ForceAnimation(Characters.Turtle0, 30006)
    EnableImmortality(Characters.Scarab1)
    DisableHealthBar(Characters.Scarab1)
    OR_15.Add(AttackedWithDamageType(attacked_entity=Characters.Turtle0, attacker=PLAYER))
    OR_15.Add(AttackedWithDamageType(attacked_entity=Characters.Scarab1, attacker=PLAYER))
    
    MAIN.Await(OR_15)
    
    ForceAnimation(Characters.Turtle0, 20006)
    DisableCharacter(Characters.Scarab1)
    EnableFlag(1035470200)
    EnableFlag(1035470220)
    End()


@RestartOnRest(1035472206)
def Event_1035472206(_, flag: uint, attacked_entity: uint):
    """Event 1035472206"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    DisableAnimations(attacked_entity)
    ForceAnimation(attacked_entity, 20008)
    EnableFlag(flag)


@RestartOnRest(1035472207)
def Event_1035472207(_, flag: uint, character: uint):
    """Event 1035472207"""
    DisableCharacter(character)
    DisableCharacter(Characters.Scarab1)
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        EnableInvincibility(character)
        EnableInvincibility(Characters.Scarab1)
    AND_1.Add(FlagEnabled(1035472211))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    EnableCharacter(Characters.Scarab1)


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
    DisableCharacter(Characters.PutridCorpse0)
    DisableCharacter(Characters.PutridCorpse1)
    DisableCharacter(Characters.PutridCorpse2)
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
    AND_1.Add(FlagEnabled(1035472211))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(Characters.PutridCorpse0)
    EnableCharacter(Characters.PutridCorpse1)
    EnableCharacter(Characters.PutridCorpse2)
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
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_251_2000)
    CreateAssetVFX(Assets.AEG099_251_2000, vfx_id=200, model_point=1500)
    AND_1.Add(FlagEnabled(1035470200))
    AND_1.Add(FlagEnabled(1035470201))
    AND_1.Add(FlagEnabled(1035470202))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1035470215)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
    PlaySoundEffect(Assets.AEG099_251_2000, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(Assets.AEG099_251_2000)
    DeleteAssetVFX(Assets.AEG099_251_2000)
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
    if FlagEnabled(1035470215):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=Assets.AEG099_251_2000))
    OR_1.Add(FlagEnabled(1035470215))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1035470215):
        return
    DisplayDialog(text=20200, anchor_entity=Assets.AEG099_251_2000)
    Wait(1.0)
    Restart()


@RestartOnRest(1035472222)
def Event_1035472222():
    """Event 1035472222"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9210, entity=Assets.AEG099_004_2000))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=60011, anchor_entity=Assets.AEG099_004_2000)
    if PlayerInOwnWorld():
        EnableNetworkFlag(1035472211)
    Wait(1.0)
    Restart()


@ContinueOnRest(1035472240)
def Event_1035472240(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1035472240"""
    if FlagEnabled(1035470260):
        return
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
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
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1035472241)
    SkipLines(3)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1035472241)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
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
    CreateProjectileOwner(entity=Characters.Dummy)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1035472270))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1035472271,
            model_point=900,
            behavior_id=802102060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy,
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
    RegisterLadder(start_climbing_flag=1035470580, stop_climbing_flag=1035470581, asset=Assets.AEG110_119_2000)
