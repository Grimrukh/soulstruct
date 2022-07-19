"""
Northeast Caelid (SW) (NW)

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
from .entities.m60_52_41_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052410000, asset=Assets.AEG099_060_9000)
    Event_1052412220()
    Event_1052412270()
    Event_1052412270(slot=1)
    Event_1052412200(0, character=Characters.GiantBall, asset=Assets.AEG099_090_9000, region=1052412210)
    CommonFunc_90005300(
        0,
        flag=1052410850,
        character=Characters.NightsCavalryHorse,
        item_lot_param_id=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005476(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    Event_1052412291(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry,
        name=903150606,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse,
    )
    CommonFunc_90005860(
        0,
        flag=1052410850,
        left=0,
        character=Characters.NightsCavalry,
        left_1=0,
        item_lot__item_lot_param_id=1052410100,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.NightsCavalry, npc_threat_level=10, right=0)
    Event_1052412510()
    CommonFunc_90005501(
        0,
        flag=1052410510,
        flag_1=1052410511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        asset_2=Assets.AEG099_182_2000,
        flag_2=1052410512,
    )
    CommonFunc_90005870(0, character=Characters.FlyingDragon, name=904500601, npc_threat_level=25)
    CommonFunc_90005860(
        0,
        flag=1052410800,
        left=0,
        character=Characters.FlyingDragon,
        left_1=1,
        item_lot__item_lot_param_id=30420,
        seconds=0.0,
    )
    Event_1052412230()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1052410519()


@RestartOnRest(1052412200)
def Event_1052412200(_, character: uint, asset: uint, region: uint):
    """Event 1052412200"""
    DisableCharacter(character)
    if FlagEnabled(region):
        return
    AND_3.Add(CharacterDead(character))
    if AND_3:
        return
    DisableHealthBar(character)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(OR_1)
    
    MAIN.Await(AND_2)
    
    CreateAssetVFX(asset, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    EnableNetworkFlag(region)
    Wait(2.0)
    DeleteAssetVFX(asset)
    ForceAnimation(character, 20001)
    Wait(1.899999976158142)
    ForceAnimation(character, 20004)
    Wait(2.0)
    ForceAnimation(character, 20004)
    Wait(1.0)
    DisableCharacter(character)
    Kill(character)
    End()


@RestartOnRest(1052412220)
def Event_1052412220():
    """Event 1052412220"""
    CreateAssetVFX(Assets.AEG099_251_2000, vfx_id=200, model_point=1500)


@RestartOnRest(1052412230)
def Event_1052412230():
    """Event 1052412230"""
    SetCharacterEnableDistanceWithUnknown(
        character=Characters.FlyingDragon,
        enable_distance=220.0,
        unknown_distance=40.0,
    )


@RestartOnRest(1052412291)
def Event_1052412291(_, character: uint, character_1: uint):
    """Event 1052412291"""
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(character, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_3)
    
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_4)
    
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@NeverRestart(1052412510)
def Event_1052412510():
    """Event 1052412510"""
    CommonFunc_90005500(
        0,
        1052410510,
        1052410511,
        0,
        1052411510,
        1052411511,
        1052413511,
        1052411512,
        1052413512,
        1052412511,
        1052412512,
        1052410512,
        1052410513,
        0,
    )


@NeverRestart(1052410519)
def Event_1052410519():
    """Event 1052410519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1052410510)


@RestartOnRest(1052412270)
def Event_1052412270():
    """Event 1052412270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=Characters.Dummy, radius=60.0))
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=8.0)
    AND_2.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_3.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_4.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_5.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_6.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_7.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_8.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_10.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_10)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=1052412271,
        model_point=900,
        behavior_id=802104270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()
