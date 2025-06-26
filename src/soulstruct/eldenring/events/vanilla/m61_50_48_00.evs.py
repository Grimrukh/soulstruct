"""
Land of Shadow 12-12 SE SW

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
    RegisterGrace(grace_flag=2050480000, asset=2050481950)
    CommonFunc_9005810(
        0,
        flag=2050480800,
        grace_flag=2050480001,
        character=2050480951,
        asset=2050481951,
        enemy_block_distance=5.0,
    )
    Event_2050480800()
    Event_2050482810()
    Event_2050482811()
    Event_2050482812()
    Event_2050482815(0, character=2050480801)
    Event_2050482815(1, character=2050480802)
    Event_2050482820()
    Event_2050482821()
    Event_2050482825(0, character=2050480800, character_1=2050480810)
    Event_2050482825(1, character=2050480801, character_1=2050480811)
    Event_2050482825(2, character=2050480802, character_1=2050480812)
    Event_2050482830(0, character=2050480800, character_1=2050480810)
    Event_2050482830(1, character=2050480801, character_1=2050480811)
    Event_2050482830(2, character=2050480802, character_1=2050480812)
    Event_2050482849()
    Event_2050482500(0, entity=2050486500)
    Event_2050482501()
    Event_2050482505()


@RestartOnRest(2050482500)
def Event_2050482500(_, entity: uint):
    """Event 2050482500"""
    if FlagEnabled(2050480800):
        ForceAnimation(entity, 2)
        End()
    OR_1.Add(FlagEnabled(2050480800))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1)
    End()


@RestartOnRest(2050482501)
def Event_2050482501():
    """Event 2050482501"""
    DisableNetworkSync()
    if FlagEnabled(2050480800):
        return
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagEnabled(2050482805))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    ChangeCamera(normal_camera_id=5232, locked_camera_id=5230)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(2050482806))
    
    MAIN.Await(AND_2)
    
    ChangeCamera(normal_camera_id=5232, locked_camera_id=5230)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(2050480800))
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@ContinueOnRest(2050482505)
def Event_2050482505():
    """Event 2050482505"""
    if FlagEnabled(2050480801):
        return
    AddSpecialEffect(2050480104, 9531)
    AwaitFlagEnabled(flag=2050480801)
    AddSpecialEffect(2050480104, 9532)


@ContinueOnRest(2050480800)
def Event_2050480800():
    """Event 2050480800"""
    GotoIfFlagDisabled(Label.L0, flag=2050480800)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L1, flag=126)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(2050480800) <= 0)
    
    if CharacterDoesNotHaveSpecialEffect(character=2050480802, special_effect=20011445):
        ForceAnimation(2050480800, 20002)
    else:
        ForceAnimation(2050480800, 20003)
    Wait(1.0)
    PlaySoundEffect(2050480800, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(2050480800))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(2050480800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=2050480800, banner_type=BannerType.LegendFelled)
    EnableNetworkFlag(2050480800)
    EnableFlag(9162)
    if PlayerInOwnWorld():
        EnableFlag(61162)


@RestartOnRest(2050482810)
def Event_2050482810():
    """Event 2050482810"""
    GotoIfFlagDisabled(Label.L0, flag=2050480800)
    DisableCharacter(2050485801)
    DisableCharacter(2050485811)
    DisableAnimations(2050485801)
    DisableAnimations(2050485811)
    Kill(2050485801)
    Kill(2050485811)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2050485801)
    DisableAI(2050485811)
    DisableHealthBar(2050485801)
    DisableHealthBar(2050485811)
    DisableAnimations(2050485801)
    DisableAnimations(2050485811)
    GotoIfFlagEnabled(Label.L1, flag=2050480801)
    ForceAnimation(2050480802, 30010)
    EnableAnimations(2050480802)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2050482801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=2050482800, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(2050480801)
    ForceAnimation(2050480802, 20010)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(2050482805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2050482800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(2050480802)
    SetNetworkUpdateRate(2050480802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAnimations(2050480802)
    ReferDamageToEntity(2050480802, target_entity=2050480812)
    Wait(0.5)
    EnableBossHealthBar(2050480812, name=905230001)


@ContinueOnRest(2050482811)
def Event_2050482811():
    """Event 2050482811"""
    if FlagEnabled(2050480800):
        return
    AND_1.Add(HealthValue(2050480812) <= 0)
    
    MAIN.Await(AND_1)
    
    if CharacterDoesNotHaveSpecialEffect(character=2050480802, special_effect=20011445):
        ForceAnimation(2050480802, 20004)
    ReferDamageToEntity(2050480801, target_entity=2050480811)
    EnableCharacter(2050480801)
    SetNetworkUpdateRate(2050480801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    OR_10.Add(CharacterDead(2050480802))
    
    MAIN.Await(OR_10)
    
    EnableFlag(2050482802)
    Wait(2.0)
    DisableBossHealthBar(2050480812, name=905230001)
    Wait(3.0)
    EnableCharacter(2050480801)
    EnableAnimations(2050480801)
    Move(2050480801, destination=2050482802, destination_type=CoordEntityType.Region, short_move=True)
    EnableAI(2050480801)
    AddSpecialEffect(2050480801, 20011443)
    Wait(3.5)
    EnableBossHealthBar(2050480811, name=905230002)


@ContinueOnRest(2050482812)
def Event_2050482812():
    """Event 2050482812"""
    if FlagEnabled(2050480800):
        return
    AND_1.Add(HealthValue(2050480811) <= 0)
    
    MAIN.Await(AND_1)
    
    if CharacterDoesNotHaveSpecialEffect(character=2050480801, special_effect=20011445):
        ForceAnimation(2050480801, 20004)
    ReferDamageToEntity(2050480800, target_entity=2050480810)
    EnableCharacter(2050480800)
    SetNetworkUpdateRate(2050480800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_10.Add(CharacterDead(2050480801))
    
    MAIN.Await(AND_10)
    
    EnableFlag(2050482803)
    Wait(2.0)
    DisableBossHealthBar(2050480811, name=905230002)
    Wait(3.0)
    EnableCharacter(2050480800)
    EnableAnimations(2050480800)
    Move(2050480800, destination=2050482802, destination_type=CoordEntityType.Region, short_move=True)
    EnableAI(2050480800)
    AddSpecialEffect(2050480800, 20011443)
    Wait(3.5)
    EnableBossHealthBar(2050480810, name=905230000)


@RestartOnRest(2050482815)
def Event_2050482815(_, character: Character | int):
    """Event 2050482815"""
    if FlagEnabled(2050480800):
        return
    EnableImmortality(character)
    AND_1.Add(CharacterHasSpecialEffect(character, 20011445))
    
    MAIN.Await(AND_1)
    
    DisableImmortality(character)
    AND_11.Add(CharacterDoesNotHaveSpecialEffect(character, 20011445))
    
    MAIN.Await(AND_11)
    
    Restart()


@RestartOnRest(2050482820)
def Event_2050482820():
    """Event 2050482820"""
    if FlagEnabled(2050480800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(2050480802, 20011445))
    AND_1.Add(CharacterHasSpecialEffect(2050480802, 20011448))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2050480801, 4403)
    End()


@RestartOnRest(2050482821)
def Event_2050482821():
    """Event 2050482821"""
    if FlagEnabled(2050480800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(2050480801, 20011445))
    AND_1.Add(CharacterHasSpecialEffect(2050480801, 20011448))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2050480800, 4403)
    End()


@RestartOnRest(2050482825)
def Event_2050482825(_, character: Character | int, character_1: Character | int):
    """Event 2050482825"""
    if FlagEnabled(2050480800):
        return
    
    MAIN.Await(HealthValue(character) == 0)
    
    Kill(character_1)
    End()


@RestartOnRest(2050482830)
def Event_2050482830(_, character: Character | int, character_1: Character | int):
    """Event 2050482830"""
    if FlagEnabled(2050480800):
        return
    
    MAIN.Await(HealthValue(character_1) == 0)
    
    Kill(character)
    End()


@RestartOnRest(2050482849)
def Event_2050482849():
    """Event 2050482849"""
    CommonFunc_9005800(
        0,
        flag=2050480800,
        entity=2050481800,
        region=2050482800,
        flag_1=2050482805,
        character=2050485800,
        action_button_id=10000,
        left=2050480801,
        region_1=2050482801,
    )
    CommonFunc_9005801(
        0,
        flag=2050480800,
        entity=2050481800,
        region=2050482800,
        flag_1=2050482805,
        flag_2=2050482806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2050480800, asset=2050481800, vfx_id=5, right=2050480801)
    CommonFunc_9005824(
        0,
        flag=2050480800,
        bgm_boss_conv_param_id=523000,
        flag_1=2050482805,
        flag_2=2050482806,
        right=0,
        flag_3=2050482802,
        flag_4=2050482803,
        left=0,
        left_1=0,
    )
