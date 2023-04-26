"""
North Altus Plateau (SW) (SE)

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
from .enums.m60_41_52_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76305, asset=Assets.AEG099_060_9002)
    Event_1041522320(0, character=Characters.AncientDragon, name=904510600, npc_threat_level=28)
    CommonFunc_90005860(
        0,
        flag=1041520800,
        left=0,
        character=Characters.AncientDragon,
        left_1=1,
        item_lot=30300,
        seconds=0.0,
    )
    Event_1041522270(0, owner_entity=Characters.Dummy0, region=1041522270, source_entity=1041522271)
    Event_1041522270(1, owner_entity=Characters.Dummy0, region=1041522270, source_entity=1041522271)
    Event_1041522270(2, owner_entity=Characters.Dummy1, region=1041522280, source_entity=1041522281)
    Event_1041522270(3, owner_entity=Characters.Dummy1, region=1041522280, source_entity=1041522281)
    CommonFunc_90005633(
        0,
        character=580320,
        flag=580020,
        character_1=Characters.WanderingNoble,
        animation_id=30015,
        animation_id_1=20015,
        asset=Assets.AEG099_166_9000,
        asset_1=Assets.AEG099_990_9000,
    )
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1001, text=61030)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1041522300(0, character=Characters.AncientDragon)


@RestartOnRest(1041522270)
def Event_1041522270(_, owner_entity: uint, region: uint, source_entity: uint):
    """Event 1041522270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=900,
            behavior_id=802103070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1041522300)
def Event_1041522300(_, character: uint):
    """Event 1041522300"""
    GotoIfFlagEnabled(Label.L0, flag=1041520800)
    GotoIfFlagEnabled(Label.L0, flag=1037510800)
    GotoIfFlagEnabled(Label.L1, flag=1041522810)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1041522800))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1041520820)
    EnableFlag(1041522810)
    SetCharacterFadeOnEnable(character=character, state=True)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20019)

    # --- Label 1 --- #
    DefineLabel(1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@ContinueOnRest(1041522320)
def Event_1041522320(_, character: uint, name: int, npc_threat_level: uint):
    """Event 1041522320"""
    DisableNetworkSync()
    DisableHealthBar(character)
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    AND_1.Add(FlagDisabled(9000))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    if FlagEnabled(1037510810):
        AddSpecialEffect(character, 4401)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_2.Add(not AND_2)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    if FlagEnabled(1037510810):
        AddSpecialEffect(character, 4401)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_12.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_12.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_12.Add(not AND_12)
    OR_12.Add(CharacterDead(character))
    OR_12.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_12)
    
    OR_13.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9291)
    Restart()
