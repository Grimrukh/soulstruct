"""
Land of Shadow 13-09 NE NW

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
    RegisterGrace(grace_flag=2054390000, asset=2054391950)
    CommonFunc_900005610(0, asset=2054391501, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2054391502, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2054391503, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2054391504, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2054391505, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2054391506, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005201(
        0,
        character=2054390850,
        animation_id=30010,
        animation_id_1=20010,
        radius=60.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=2054390850, name=905370600, npc_threat_level=28)
    CommonFunc_90005860(0, flag=2054390850, left=0, character=2054390850, left_1=1, item_lot=30805, seconds=0.0)
    Event_2054392800()
    Event_2054392810()
    Event_2054390811()
    Event_2054392849()
    Event_2054392815()
    Event_2054392816()
    Event_2054392300()
    Event_2054392400(0, character=2054390400, region=2054392400)
    Event_2054392400(1, character=2054390401, region=2054392400)
    Event_2054392400(2, character=2054390402, region=2054392400)
    Event_2054392400(3, character=2054390403, region=2054392400)
    Event_2054392400(4, character=2054390404, region=2054392400)
    CommonFunc_90005211(
        0,
        character=2054390400,
        animation_id=30001,
        animation_id_1=20001,
        region=2054392401,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2054390402,
        animation_id=30001,
        animation_id_1=20001,
        region=2054392402,
        radius=5.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2054390404,
        animation_id=30001,
        animation_id_1=20001,
        region=2054392402,
        radius=5.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_2054392201(0, source_entity=2054390201, region=2054392201)
    Event_2054392201(1, source_entity=2054390202, region=2054392201)
    Event_2054392201(2, source_entity=2054390204, region=2054392201)
    Event_2054392201(3, source_entity=2054390205, region=2054392201)
    Event_2054392201(4, source_entity=2054390206, region=2054392201)
    Event_2054392480()
    Event_2054392481(0, character=2054390700)
    Event_2054392482()
    Event_2054392483(0, character=2054390700)
    Event_2054392484(0, character=2054390700)
    Event_2054390700(0, flag=2054392485, character=2054390700, distance=100.0, flag_1=2054392700, flag_2=2054390800)
    Event_2054390701(
        0,
        flag=2054392701,
        flag_1=2054390800,
        attacker=2054390700,
        attacked_entity=2054390800,
        flag_2=2054392706,
        flag_3=2054392707,
    )
    Event_2054390702(0, character=2054390700, flag=2054392702, flag_1=2054390800, seconds=15.0)
    Event_2054390703(0, character=2054390700, flag=2054392703, flag_1=2054390800, seconds=8.0)
    Event_2054390704(0, flag=2054390800, flag_1=4278, flag_2=2048429222)
    Event_2054390706(0, character=2054390710, flag=2054390800, character_1=2054390800)
    Event_2054390705(0, flag=2052409231, item=2008003, flag_1=2054390800, flag_2=2054390801)


@RestartOnRest(2054392201)
def Event_2054392201(_, source_entity: uint, region: Region | int):
    """Event 2054392201"""
    if FlagEnabled(2054390800):
        return
    DisableNetworkSync()
    CreateProjectileOwner(entity=source_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    GotoIfFlagEnabled(Label.L0, flag=70)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008500,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008510,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008520,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008530,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008540,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008550,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008560,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008570,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018500,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018510,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018520,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018530,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018540,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018550,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018560,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018570,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(2.0)
    Restart()


@RestartOnRest(2054392300)
def Event_2054392300():
    """Event 2054392300"""
    DisableCharacter(2054395421)
    DisableGravity(2054395411)
    DisableAI(2054395411)
    if FlagDisabled(2054390850):
        return
    EnableCharacter(2054395421)
    DisableCharacter(2054395411)


@RestartOnRest(2054392400)
def Event_2054392400(_, character: Character | int, region: Region | int):
    """Event 2054392400"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4080)
    AddSpecialEffect(character, 4085)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4080)
    RemoveSpecialEffect(character, 4085)
    Restart()


@RestartOnRest(2054392800)
def Event_2054392800():
    """Event 2054392800"""
    if FlagEnabled(2054390800):
        return
    
    MAIN.Await(HealthValue(2054390800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2054390800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2054390800))
    
    KillBossAndDisplayBanner(character=2054390800, banner_type=BannerType.LegendFelled)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    DeleteAssetVFX(2054391810)
    ForceAnimation(2054391811, 1)
    DeleteAssetVFX(2054396800)
    EnableFlag(2054390800)
    if PlayerInOwnWorld():
        EnableFlag(61163)
    EnableFlag(9163)
    if PlayerNotInOwnWorld():
        return
    Wait(5.0)
    ForceAnimation(2054391811, 3)
    End()


@RestartOnRest(2054392810)
def Event_2054392810():
    """Event 2054392810"""
    GotoIfFlagDisabled(Label.L0, flag=2054390800)
    DisableCharacter(2054390800)
    DisableAnimations(2054390800)
    Kill(2054390800)
    DisableAsset(2054391810)
    ForceAnimation(2054391811, 3)
    DisableAsset(2054396800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2054390800)
    SetTeamType(2054390800, TeamType.Enemy)
    ForceAnimation(2054391811, 3)
    DisableAnimations(2054390800)
    AddSpecialEffect(2054390102, 9531)
    GotoIfFlagEnabled(Label.L1, flag=2054390801)
    EnableAI(2054390800)
    ForceAnimation(2054390800, 30000, loop=True)
    DisableHealthBar(2054390800)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2054392817))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=2054390800, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(2054390801)
    AddSpecialEffect(2054390102, 9532)
    ForceAnimation(2054390800, 20000, skip_transition=True)
    Wait(7.0)
    EnableHealthBar(2054390800)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(2054390800, destination=2054392802, destination_type=CoordEntityType.Region, copy_draw_parent=2054390800)
    AddSpecialEffect(2054390800, 20010830)
    AND_2.Add(FlagEnabled(2054392805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2054392800))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(2054390800, 20010827)
    AddSpecialEffect(2054390102, 9532)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAnimations(2054390800)
    EnableAI(2054390800)
    SetNetworkUpdateRate(2054390800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(2054390800, name=905120000)


@RestartOnRest(2054390811)
def Event_2054390811():
    """Event 2054390811"""
    if FlagEnabled(2054390800):
        return
    AND_1.Add(CharacterHasSpecialEffect(2054390800, 20010826))
    
    MAIN.Await(AND_1)
    
    EnableFlag(2054392802)
    Wait(5.0)
    CreateAssetVFX(2054391810, dummy_id=200, vfx_id=861685)
    CreateAssetVFX(2054396800, dummy_id=200, vfx_id=861956)
    ForceAnimation(2054391811, 2, wait_for_completion=True)
    ForceAnimation(2054391811, 0, wait_for_completion=True)


@RestartOnRest(2054392815)
def Event_2054392815():
    """Event 2054392815"""
    if FlagEnabled(2054390801):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2054392818))
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(2054392819, 512008300, sound_type=SoundType.c_CharacterMotion)
    End()


@RestartOnRest(2054392816)
def Event_2054392816():
    """Event 2054392816"""
    if FlagEnabled(2054390800):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(2054390800, 20010827))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2054392801))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=5126, locked_camera_id=-1)
    End()


@RestartOnRest(2054392849)
def Event_2054392849():
    """Event 2054392849"""
    CommonFunc_9005800(
        0,
        flag=2054390800,
        entity=2054391800,
        region=2054392800,
        flag_1=2054392805,
        character=2054395800,
        action_button_id=10000,
        left=2054390801,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2054390800,
        entity=2054391800,
        region=2054392800,
        flag_1=2054392805,
        flag_2=2054392806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2054390800, asset=2054391800, vfx_id=1560, right=2054390801)
    CommonFunc_9005822(
        0,
        flag=2054390800,
        bgm_boss_conv_param_id=512000,
        flag_1=2054392805,
        flag_2=2054392806,
        right=0,
        flag_3=2054392802,
        left=0,
        left_1=0,
    )
    PlaySoundEffect(0, 0, sound_type=SoundType.a_Ambient)


@RestartOnRest(2054392480)
def Event_2054392480():
    """Event 2054392480"""
    if FlagEnabled(2054390800):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L10, flag=2052409231)
    AND_1.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(2052409231))
    AND_3.Add(ActionButtonParamActivated(action_button_id=209520, entity=2054391480))
    OR_1.Add(FlagEnabled(2054390800))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(2054390800):
        return
    AwaitDialogResponse(
        message=2080800,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2054391480,
        display_distance=3.0,
        left_flag=2054392488,
        right_flag=2054392489,
        cancel_flag=2054392489,
    )
    if FlagDisabled(2054392488):
        return RESTART

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    Wait(1.0)
    EnableNetworkFlag(2054392481)
    EnableNetworkFlag(2054392485)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(2052409231))
    
    Restart()


@RestartOnRest(2054392481)
def Event_2054392481(_, character: uint):
    """Event 2054392481"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetCharacterFadeOnEnable(character=character, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(2054390800):
        return
    DisableCharacter(character)
    AddSpecialEffect(character, 18677)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    AND_1.Add(FlagEnabled(2052409231))
    AND_1.Add(FlagEnabled(2054392481))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(2054390800):
        DisableCharacter(character)
        DisableAnimations(character)
        DisableCharacterCollision(character)
        DisableGravity(character)
        DisableAI(character)
        End()
    if PlayerInOwnWorld():
        DisplayNetworkMessage(text=4080100, unk_4_5=False)
    else:
        DisplayNetworkMessage(text=4080110, unk_4_5=False)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    CreateAssetVFX(2054391480, dummy_id=100, vfx_id=30320)
    RemoveSpecialEffect(character, 4380)
    RemoveSpecialEffect(character, 18677)
    EnableInvincibility(character)
    ForceAnimation(character, 90205, wait_for_completion=True)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableHealthBar(character)
    SetTeamType(character, TeamType.WhitePhantom)
    SetCharacterEventTarget(character, entity=2054390800)
    SkipLinesIfPlayerNotInOwnWorld(2)
    DisplayNetworkMessage(text=4080800, unk_4_5=False)
    SkipLinesIfPlayerInOwnWorld(1)
    DisplayNetworkMessage(text=4080801, unk_4_5=False)
    DeleteAssetVFX(2054391480)
    End()


@RestartOnRest(2054392482)
def Event_2054392482():
    """Event 2054392482"""
    GotoIfFlagEnabled(Label.L2, flag=2054390800)
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(2052409231))
    
    CreateAssetVFX(2054391480, dummy_id=100, vfx_id=30101)
    OR_1.Add(FlagEnabled(2054392481))
    OR_1.Add(FlagEnabled(2054390800))
    
    MAIN.Await(OR_1)
    
    DeleteAssetVFX(2054391480)
    End()


@RestartOnRest(2054392483)
def Event_2054392483(_, character: uint):
    """Event 2054392483"""
    if FlagEnabled(2054390800):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L1, flag=2054392481)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(2052409231))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2054391480, radius=1.5))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=2054390800)
    GotoIfFlagEnabled(Label.L1, flag=2054392481)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableAI(character)
    AddSpecialEffect(character, 4380)
    WaitFrames(frames=1)
    RemoveSpecialEffect(character, 18677)
    DisableInvincibility(character)
    DisableAnimations(character)
    DisableCharacterCollision(character)
    DisableGravity(character)
    WaitFrames(frames=1)
    ForceAnimation(character, 63040, loop=True)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2054391480, radius=1.5))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(2052409231))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=2054390800)
    GotoIfFlagEnabled(Label.L1, flag=2054392481)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(2054392484)
def Event_2054392484(_, character: uint):
    """Event 2054392484"""
    if FlagEnabled(2054390800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(2052409231))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(FlagEnabled(2054392481))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(FlagEnabled(2054390800))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(HealthRatio(character) <= 0.0)
    AND_3.Add(FlagEnabled(2054392481))
    AND_5.Add(FlagDisabled(2054392481))
    AND_5.Add(FlagEnabled(2054390800))
    OR_3.Add(AND_1)
    OR_3.Add(AND_3)
    OR_3.Add(AND_5)
    
    MAIN.Await(OR_3)
    
    DisableFlag(2054392485)
    EnableFlag(2054392486)
    if LastResult(AND_5):
        return
    AND_9.Add(HealthRatio(character) <= 0.0)
    SkipLinesIfConditionFalse(2, AND_9)
    DisplayNetworkMessage(text=4080802, unk_4_5=False)
    End()
    DisableAI(character)
    AND_10.Add(FlagEnabled(2054399208))
    
    MAIN.Await(AND_10)
    
    Wait(2.0)
    SetTeamType(character, TeamType.NoTeam)
    DisableAnimations(character)
    EnableInvincibility(character)
    AddSpecialEffect(character, 18677)
    ReplanAI(character)
    ClearTargetList(character)
    DisableInvincibility(character)
    ResetAnimation(character, disable_interpolation=True)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_10.Add(HealthRatio(character) <= 0.0)
    SkipLinesIfConditionFalse(2, AND_10)
    DisplayNetworkMessage(text=4080802, unk_4_5=False)
    End()


@RestartOnRest(2054390700)
def Event_2054390700(
    _,
    flag: Flag | int,
    character: Character | int,
    distance: float,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 2054390700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(flag_1)


@RestartOnRest(2054390701)
def Event_2054390701(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    attacker: Character | int,
    attacked_entity: Character | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 2054390701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L0, flag=flag_2)
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_2))
    AND_2.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=attacker))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag_2)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=attacker))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag_3)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=attacker))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag)


@RestartOnRest(2054390702)
def Event_2054390702(_, character: Character | int, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 2054390702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(HealthValue(character) != 0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    SetBackreadStateAlternate(character, True)
    Wait(seconds)
    SetBackreadStateAlternate(character, False)


@RestartOnRest(2054390703)
def Event_2054390703(_, character: Character | int, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 2054390703"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(HealthValue(character) <= 0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    SetBackreadStateAlternate(character, True)
    Wait(seconds)
    SetBackreadStateAlternate(character, False)


@RestartOnRest(2054390704)
def Event_2054390704(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2054390704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)


@RestartOnRest(2054390705)
def Event_2054390705(_, flag: Flag | int, item: BaseItemParam | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2054390705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    if FlagEnabled(flag_1):
        return
    AND_1.Add(PlayerHasGood(item))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(2054390706)
def Event_2054390706(_, character: Character | int, flag: Flag | int, character_1: uint):
    """Event 2054390706"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    EnableInvincibility(character)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(HealthValue(character_1) <= 0)
    
    EnableCharacter(character)
    WaitRealFrames(frames=1)
    Move(character, destination=character_1, destination_type=CoordEntityType.Character, dummy_id=10, short_move=True)
    Wait(20.0)
    DisableCharacter(character)
