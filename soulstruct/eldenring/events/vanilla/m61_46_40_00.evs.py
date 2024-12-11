"""
Land of Shadow 11-10 SE SW

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2046400000, asset=2046401950, enemy_block_distance=0.0)
    CommonFunc_90005870(0, character=2046400800, name=905730600, npc_threat_level=16)
    CommonFunc_90005860(0, flag=2046400800, left=0, character=2046400800, left_1=0, item_lot=30845, seconds=0.0)
    CommonFunc_90005201(
        0,
        character=2046400300,
        animation_id=30000,
        animation_id_1=20000,
        radius=45.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2046400301, region=2046402301, seconds=0.0, animation_id=0)
    Event_2046402200(0, owner_entity=2046400200, region=2046402200, source_entity=2046402201)
    Event_2046402200(1, owner_entity=2046400201, region=2046402200, source_entity=2046402202)
    Event_2046402200(2, owner_entity=2046400202, region=2046402200, source_entity=2046402203)
    Event_2046402550(0, flag=580100, asset=2046401550, item_lot=80100)
    Event_2046400700(0, flag=4926, flag_1=4458)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_2046402500()
    Event_2046402502()


@RestartOnRest(2046400700)
def Event_2046400700(_, flag: Flag | int, flag_1: Flag | int):
    """Event 2046400700"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    EnableFlag(flag_1)


@RestartOnRest(2046402500)
def Event_2046402500():
    """Event 2046402500"""
    if FlagEnabled(2046400500):
        return
    if OutsideMap(game_map=LANDOFSHADOW_11_10_SE_SW):
        return
    SetCurrentTime(
        time=(8, 0, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )
    FreezeTime()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=2046402500))
    OR_9.Add(AND_1)
    AND_2.Add(PlayerNotInOwnWorld())
    OR_9.Add(AND_2)
    
    MAIN.Await(OR_9)
    
    GotoIfPlayerNotInOwnWorld(Label.L1)
    EnableNetworkFlag(2046400500)

    # --- Label 1 --- #
    DefineLabel(1)
    UnfreezeTime()


@RestartOnRest(2046402502)
def Event_2046402502():
    """Event 2046402502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2046400502):
        return
    if OutsideMap(game_map=LANDOFSHADOW_11_10_SE_SW):
        return
    SetAreaWelcomeMessageState(state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=2046402502))
    
    MAIN.Await(AND_1)
    
    SetAreaWelcomeMessageState(state=True)
    DisplayAreaWelcomeMessage(place_name_id=68000)
    EnableFlag(2046400502)


@RestartOnRest(2046402200)
def Event_2046402200(_, owner_entity: uint, region: Region | int, source_entity: uint):
    """Event 2046402200"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    GotoIfFlagEnabled(Label.L0, flag=70)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804508070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=804518070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()


@RestartOnRest(2046402550)
def Event_2046402550(_, flag: Flag | int, asset: uint, item_lot: int):
    """Event 2046402550"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    DeleteAssetVFX(asset, erase_root=False)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806845)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9310, entity=asset))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot, host_only=True)
