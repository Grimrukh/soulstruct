"""
Southwest Liurnia (NE) (SW)

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
from .entities.m60_34_42_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034420000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005870(0, character=Characters.GlintstoneDragon0, name=904502602, npc_threat_level=25)
    CommonFunc_90005860(
        0,
        flag=1034420800,
        left=0,
        character=Characters.GlintstoneDragon0,
        left_1=1,
        item_lot__item_lot_param_id=30260,
        seconds=0.0,
    )
    Event_1034422800()
    Event_1034422801()
    Event_1034422802()
    CommonFunc_90005201(
        0,
        character=Characters.GlintstoneDragon1,
        animation_id=30000,
        animation_id_1=20000,
        radius=17.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.GlintstoneDragon1, radius=17.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(
        0,
        flag=1034420340,
        character=Characters.GlintstoneDragon1,
        item_lot_param_id=1034420400,
        seconds=0.0,
        left=0,
    )
    Event_1034422600(0, asset=Assets.AEG099_045_9000, flag=1034422600, owner_entity=Characters.Dummy)
    Event_1034422600(1, asset=Assets.AEG099_045_9001, flag=1034422601, owner_entity=Characters.Dummy)
    Event_1034422600(2, asset=Assets.AEG099_045_9002, flag=1034422602, owner_entity=Characters.Dummy)
    Event_1034422600(3, asset=Assets.AEG099_045_9003, flag=1034422603, owner_entity=Characters.Dummy)
    Event_1034422600(4, asset=Assets.AEG099_045_9004, flag=1034422604, owner_entity=Characters.Dummy)
    Event_1034422600(5, asset=Assets.AEG099_045_9005, flag=1034422605, owner_entity=Characters.Dummy)
    Event_1034422600(6, asset=Assets.AEG099_045_9006, flag=1034422606, owner_entity=Characters.Dummy)
    Event_1034422600(7, asset=Assets.AEG099_045_9007, flag=1034422607, owner_entity=Characters.Dummy)
    Event_1034422600(8, asset=Assets.AEG099_045_9008, flag=1034422608, owner_entity=Characters.Dummy)
    Event_1034422600(9, asset=Assets.AEG099_045_9009, flag=1034422609, owner_entity=Characters.Dummy)
    CommonFunc_90005525(0, flag=1034420650, asset=Assets.AEG004_983_1000)
    CommonFunc_90005706(0, character=Characters.Commoner, animation_id=930023, left=0)
    Event_1034420700(0, character=Characters.NepheliLoux, asset=Assets.AEG007_360_2000)
    CommonFunc_90005704(0, attacked_entity=Characters.NepheliLoux, flag=4221, flag_1=4220, flag_2=10009701, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.NepheliLoux,
        flag=4221,
        flag_1=4222,
        flag_2=10009701,
        flag_3=4221,
        first_flag=4220,
        last_flag=4224,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.NepheliLoux, flag=4223, first_flag=4220, last_flag=4224)
    Event_1034420701()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.NepheliLoux)
    DisableBackread(Characters.Commoner)
    Event_1034422230()
    CommonFunc_90005251(0, character=Characters.AlbinauricLookout0, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AlbinauricLookout2, region=1034422203, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.AlbinauricLookout3, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AlbinauricLookout4, region=1034422208, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AlbinauricLookout5, region=1034422208, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AlbinauricLookout6, region=1034422208, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1034420222, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1034420228, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.LargeCrabSnow0,
        animation_id=30003,
        animation_id_1=20003,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.LargeCrabSnow1, radius=16.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, 1034420390, 30.0, 0.0, -1)


@RestartOnRest(1034422230)
def Event_1034422230():
    """Event 1034422230"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(Characters.AlbinauricLookout7)
    DisableAI(Characters.AlbinauricLookout8)
    DisableAI(Characters.AlbinauricLookout9)
    DisableAI(Characters.AlbinauricLookout12)
    DisableAI(Characters.AlbinauricLookout13)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout1, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout7, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout8, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout9, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout11, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout12, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout13, attacker=0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.AlbinauricLookout14, attacker=0))
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableAI(Characters.AlbinauricLookout7)
    EnableAI(Characters.AlbinauricLookout8)
    EnableAI(Characters.AlbinauricLookout9)
    EnableAI(Characters.AlbinauricLookout12)
    EnableAI(Characters.AlbinauricLookout13)


@RestartOnRest(1034422600)
def Event_1034422600(_, asset: uint, flag: uint, owner_entity: uint):
    """Event 1034422600"""
    if FlagEnabled(flag):
        return
    if AssetDestroyed(asset):
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(EntityWithinDistance(entity=asset, other_entity=20000, radius=2.0))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DestroyAsset(asset, request_slot=0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402210,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402220,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402230,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402240,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402250,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402260,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402270,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    End()


@RestartOnRest(1034422800)
def Event_1034422800():
    """Event 1034422800"""
    if FlagEnabled(1034420800):
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.GlintstoneDragon0)
    DisableCharacter(Characters.GlintstoneDragon0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GlintstoneDragon0, attacker=PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1034422800))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneDragon0, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneDragon0, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneDragon0, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneDragon0, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneDragon0, state_info=260))
    AND_4.Add(CharacterHasSpecialEffect(Characters.GlintstoneDragon0, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.GlintstoneDragon0, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.GlintstoneDragon0, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.GlintstoneDragon0, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.GlintstoneDragon0, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneDragon0, 90160))
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(1034422800)
    SetSpecialStandbyEndedFlag(character=Characters.GlintstoneDragon0, state=True)
    EnableCharacter(Characters.GlintstoneDragon0)
    ForceAnimation(Characters.GlintstoneDragon0, 20008)


@RestartOnRest(1034422801)
def Event_1034422801():
    """Event 1034422801"""
    DisableNetworkSync()
    if FlagEnabled(1034420800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.GlintstoneDragon0, region=1034422801))
    
    AddSpecialEffect(Characters.GlintstoneDragon0, 10285)
    Wait(1.0)
    Restart()


@RestartOnRest(1034422802)
def Event_1034422802():
    """Event 1034422802"""
    DisableNetworkSync()
    if FlagEnabled(1034420800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.GlintstoneDragon0, region=1034422802))
    
    AddSpecialEffect(Characters.GlintstoneDragon0, 10286)
    Wait(1.0)
    Restart()


@RestartOnRest(1034420700)
def Event_1034420700(_, character: uint, asset: uint):
    """Event 1034420700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagDisabled(4220):
        DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(4227))
    OR_1.Add(FlagDisabled(1035422160))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    AND_2.Add(FlagEnabled(4227))
    OR_2.Add(FlagDisabled(1035422160))
    AND_2.Add(OR_2)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagDisabled(4227))
    OR_15.Add(FlagEnabled(1035422160))
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(1034420701)
def Event_1034420701():
    """Event 1034420701"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4221, 4223)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034429209)
    End()
