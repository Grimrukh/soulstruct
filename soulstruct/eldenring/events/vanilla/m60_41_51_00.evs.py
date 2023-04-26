"""
South Altus Plateau (NW) (NE)

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
from .enums.m60_41_51_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=Characters.TreeSentinel0, name=903251600, npc_threat_level=12)
    CommonFunc_90005870(0, character=Characters.TreeSentinel1, name=903251600, npc_threat_level=12)
    Event_1041512800(
        0,
        flag=1041510800,
        left=0,
        character=Characters.TreeSentinel0,
        left_1=0,
        item_lot=30335,
        character_1=Characters.TreeSentinel1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.TreeSentinel0,
        region=1041512500,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.TreeSentinel1,
        region=1041512500,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1041512310(0, character=Characters.TreeSentinel0, character_1=Characters.TreeSentinel1)
    Event_1041512321(
        0,
        character=Characters.TreeSentinel0,
        character_1=Characters.TreeSentinel1,
        npc_threat_level=12,
        flag=1041512815,
    )
    Event_1041512320(0, character=Characters.TreeSentinel0, character_1=Characters.TreeSentinel1)
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellKnight2,
        region=1041512202,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1041512200(0, character=Characters.LeyndellKnight0)
    Event_1041512200(1, character=Characters.LeyndellKnight1)
    CommonFunc_90005300(0, flag=1041510410, character=Characters.GiantMirandaFlower, item_lot=0, seconds=0.0, left=0)
    Event_1041512270()
    Event_1041512270(slot=1)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, character=Characters.GiantMirandaFlower, region=1041512410, seconds=0.0, animation_id=700)
    CommonFunc_90005201(
        0,
        character=Characters.GraveSkeleton2,
        animation_id=30016,
        animation_id_1=20016,
        radius=100.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GraveSkeleton0,
        animation_id=30017,
        animation_id_1=20017,
        region=1041512450,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GraveSkeleton1,
        animation_id=30017,
        animation_id_1=20017,
        region=1041512450,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.GraveSkeleton3,
        animation_id=30016,
        animation_id_1=20016,
        region=1041512453,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(1041512200)
def Event_1041512200(_, character: uint):
    """Event 1041512200"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8092)
    EnableThisNetworkSlotFlag()


@RestartOnRest(1041512270)
def Event_1041512270():
    """Event 1041512270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1041512270))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1041512310)
def Event_1041512310(_, character: uint, character_1: uint):
    """Event 1041512310"""
    if FlagEnabled(1041510800):
        return
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    Wait(30.0)
    EnableAI(character)
    EnableAI(character_1)
    SetCharacterEventTarget(character, entity=character_1)
    SetCharacterEventTarget(character_1, entity=character)
    Restart()


@RestartOnRest(1041512320)
def Event_1041512320(_, character: uint, character_1: uint):
    """Event 1041512320"""
    if FlagEnabled(1041510800):
        return
    OR_1.Add(CharacterDead(character))
    OR_1.Add(CharacterDead(character_1))
    OR_2.Add(OR_1)
    AND_1.Add(HealthRatio(character) <= 0.5)
    AND_1.Add(HealthRatio(character_1) <= 0.5)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(1041512815)


@ContinueOnRest(1041512321)
def Event_1041512321(_, character: uint, character_1: uint, npc_threat_level: uint, flag: uint):
    """Event 1041512321"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(AND_1)
    
    EnableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    AND_2.Add(CharacterDead(character))
    AND_2.Add(CharacterDead(character_1))
    OR_2.Add(AND_2)
    OR_2.Add(FieldBattleMusicDisabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(OR_2)
    
    DisableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(1041512800)
def Event_1041512800(_, flag: uint, left: uint, character: uint, left_1: uint, item_lot: int, character_1: uint):
    """Event 1041512800"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableAnimations(character)
    DisableAnimations(character_1)
    Kill(character)
    Kill(character_1)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableAnimations(character)
    EnableAnimations(character_1)
    AND_15.Add(HealthValue(character) <= 0)
    AND_15.Add(HealthValue(character_1) <= 0)
    
    MAIN.Await(AND_15)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    AND_14.Add(CharacterDead(character))
    AND_14.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_14)
    
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.GreatEnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.LegendFelled)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot, host_only=True)
    End()
