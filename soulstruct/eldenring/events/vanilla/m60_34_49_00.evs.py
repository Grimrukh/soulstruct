"""
Northwest Liurnia (SE) (NW)

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
from .enums.m60_34_49_00_enums import *
from .enums.m60_35_49_00_enums import Assets as m60_35_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034490000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76214,
        flag_1=76213,
        asset=Assets.AEG099_090_9262,
        source_flag=77220,
        value=3,
        flag_2=78220,
        flag_3=78221,
        flag_4=78222,
        flag_5=78223,
        flag_6=78224,
        flag_7=78225,
        flag_8=78226,
        flag_9=78227,
        flag_10=78228,
        flag_11=78229,
    )
    Event_1034492290(
        0,
        source_entity=Assets.AEG099_090_9033,
        region=1034492200,
        flag=1034492281,
        flag_1=1034492282,
        flag_2=1034492283,
        frames=2,
    )
    Event_1034492290(
        1,
        source_entity=Assets.AEG099_090_9001,
        region=1034492201,
        flag=1034492282,
        flag_1=1034492283,
        flag_2=6001,
        frames=1,
    )
    Event_1034492290(
        2,
        source_entity=m60_35_Assets.AEG099_090_9000,
        region=1035492200,
        flag=1034492283,
        flag_1=6001,
        flag_2=6001,
        frames=0,
    )
    Event_1034492270(0, seconds=4.300000190734863, flag=1034492281)
    Event_1034492270(1, seconds=2.5, flag=1034492282)
    Event_1034492270(2, seconds=2.5, flag=1034492283)
    Event_1034492270(3, seconds=2.4000000953674316, flag=1034492284)
    CommonFunc_90005704(0, attacked_entity=Characters.Iji0, flag=3761, flag_1=3760, flag_2=1034499201, right=3)
    CommonFunc_90005707(
        0,
        character=Characters.Iji0,
        flag=3761,
        flag_1=3762,
        flag_2=1034499201,
        flag_3=3763,
        first_flag=3760,
        last_flag=3763,
        right=-1,
        animation_id=20046,
        left=1034492703,
        flag_4=1034492704,
    )
    Event_1034490700(0, character=Characters.Iji0)
    CommonFunc_90005709(0, attacked_entity=Characters.Iji0, dummy_id=905, vfx_id=603002)
    CommonFunc_90005709(0, attacked_entity=Characters.Iji0, dummy_id=960, vfx_id=603052)
    CommonFunc_90005704(0, attacked_entity=Characters.Iji1, flag=3761, flag_1=3760, flag_2=1034499203, right=3)
    CommonFunc_90005707(
        0,
        character=Characters.Iji1,
        flag=3761,
        flag_1=3762,
        flag_2=1034499203,
        flag_3=3763,
        first_flag=3760,
        last_flag=3763,
        right=-1,
        animation_id=20046,
        left=1034492703,
        flag_4=1034492704,
    )
    Event_1034490701(
        0,
        character=Characters.Iji1,
        destination=1034492700,
        character_1=Characters.BlackKnifeAssassin0,
        character_2=Characters.BlackKnifeAssassin1,
        character_3=Characters.BlackKnifeAssassin2,
    )
    CommonFunc_90005709(0, attacked_entity=Characters.Iji1, dummy_id=905, vfx_id=603002)
    CommonFunc_90005709(0, attacked_entity=Characters.Iji1, dummy_id=960, vfx_id=603052)
    CommonFunc_90005708(0, character=Characters.Iji0, flag=3760, left=0)
    CommonFunc_90005708(0, character=Characters.Iji1, flag=3760, left=0)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9000,
        action_button_id=6361,
        item_lot=102400,
        first_flag=400240,
        last_flag=400241,
        flag=3768,
        dummy_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Iji0)
    DisableBackread(Characters.BlackKnifeAssassin0)
    DisableBackread(Characters.BlackKnifeAssassin1)
    DisableBackread(Characters.BlackKnifeAssassin2)
    DisableBackread(Characters.Iji1)
    Event_1034492210(0, character=Characters.BulletDummy)


@RestartOnRest(1034492210)
def Event_1034492210(_, character: uint):
    """Event 1034492210"""
    EnableNetworkSync()
    SetBackreadStateAlternate(character, True)
    SetCharacterEnableDistance(character=character, distance=230.0)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)
    DisableGravity(character)


@RestartOnRest(1034492270)
def Event_1034492270(_, seconds: float, flag: uint):
    """Event 1034492270"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    if FlagEnabled(1035500800):
        return
    
    MAIN.Await(FlagDisabled(flag))
    
    Wait(seconds)
    EnableNetworkFlag(flag)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1034492290)
def Event_1034492290(_, source_entity: uint, region: uint, flag: uint, flag_1: uint, flag_2: uint, frames: int):
    """Event 1034492290"""
    EnableNetworkSync()
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(1034492284))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(1035500800):
        return
    WaitFramesAfterCutscene(frames=frames)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    GotoIfFlagDisabled(Label.L1, flag=flag_2)
    AND_2.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_3.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_4.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_5.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_6.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_7.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_8.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
        behavior_id=802600060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_10.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_10)
    ShootProjectile(
        owner_entity=Characters.BulletDummy,
        source_entity=source_entity,
        dummy_id=90,
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
    Kill(character, award_runes=True)


@RestartOnRest(1034490700)
def Event_1034490700(_, character: uint):
    """Event 1034490700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3760):
        DisableFlag(1034499202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=3765)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3765))
    
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
    ForceAnimation(character, 930017)
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
    
    MAIN.Await(FlagDisabled(3765))
    
    Restart()


@RestartOnRest(1034490701)
def Event_1034490701(_, character: uint, destination: uint, character_1: uint, character_2: uint, character_3: uint):
    """Event 1034490701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3760):
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
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3766, 3768)))
    
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
    ForceAnimation(character, 930017)
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
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3766, 3767)))
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 930019)
    SetTeamType(character, TeamType.NoTeam)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 930002)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    ForceAnimation(character_2, 930002)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    ForceAnimation(character_3, 930002)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3768))
    
    Restart()


@RestartOnRest(1034493704)
def Event_1034493704(_, character: uint):
    """Event 1034493704"""
    OR_1.Add(FlagEnabled(1034499236))
    OR_1.Add(FlagEnabled(1034499237))
    
    MAIN.Await(OR_1)
    
    SetTeamType(character, TeamType.FriendlyNPC)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    if FlagEnabled(1034499236):
        CreateTemporaryVFX(
            vfx_id=646060,
            anchor_entity=character,
            dummy_id=960,
            anchor_type=CoordEntityType.Character,
        )
    if FlagEnabled(1034499237):
        CreateTemporaryVFX(
            vfx_id=641111,
            anchor_entity=character,
            dummy_id=960,
            anchor_type=CoordEntityType.Character,
        )
    Restart()
