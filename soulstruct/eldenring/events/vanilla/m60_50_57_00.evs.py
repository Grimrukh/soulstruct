"""
Northwest Mountaintops (SE) (NW)

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
from .enums.m60_50_57_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=1050570000, asset=1050571950, enemy_block_distance=5.0, character=1050570480)
    Event_1050572820(
        0,
        character=Characters.DeathRiteBird,
        animation_id=30000,
        animation_id_1=20000,
        region=1050572800,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=Characters.DeathRiteBird, name=904980600, npc_threat_level=24)
    CommonFunc_90005860(
        0,
        flag=1050570800,
        left=0,
        character=Characters.DeathRiteBird,
        left_1=0,
        item_lot=30530,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.PutridAvatar, name=904811600, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1050570850,
        left=0,
        character=Characters.PutridAvatar,
        left_1=0,
        item_lot=30555,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.PutridAvatar, npc_threat_level=18, right=0)
    Event_1050572320(0, character=Characters.GiantSkeletonTorso, destination=1051570320, special_effect=5030)
    Event_1050572330(0, character=Characters.GiantSkeletonTorso, special_effect=5021)
    Event_1050572340(0, character=Characters.GiantSkeletonTorso, region=1050572320, flag=1050572330)
    Event_1050572200(0, character=1050575200)
    Event_1050572250()
    Event_1050572250(slot=1)


@RestartOnRest(1050572200)
def Event_1050572200(_, character: uint):
    """Event 1050572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1050572250)
def Event_1050572250():
    """Event 1050572250"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1050572250))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1050572251,
            model_point=900,
            behavior_id=802105070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1050572320)
def Event_1050572320(_, character: uint, destination: uint, special_effect: int):
    """Event 1050572320"""
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=90,
        copy_draw_parent=character,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1050572330)
def Event_1050572330(_, character: uint, special_effect: int):
    """Event 1050572330"""
    AddSpecialEffect(character, special_effect)


@RestartOnRest(1050572340)
def Event_1050572340(_, character: uint, region: uint, flag: uint):
    """Event 1050572340"""
    AND_15.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    AND_14.Add(CharacterBackreadEnabled(character))
    AwaitConditionTrue(AND_14)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_1)
    AND_2.Add(AllPlayersOutsideRegion(region=region))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(character, 15338)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_5.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_5.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_5.Add(AND_5)
    OR_5.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_5.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_5.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_6.Add(OR_5)
    AND_6.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_6.Add(AND_6)
    OR_6.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_6)
    
    DisableNetworkFlag(flag)
    AddSpecialEffect(character, 15339)
    Wait(3.0)
    Restart()


@RestartOnRest(1050572820)
def Event_1050572820(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1050572820"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()
