"""
Impaler's Catacombs

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
from .entities.m30_01_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=30010800,
        left_flag=30012840,
        cancel_flag__right_flag=30012841,
        asset=Assets.AEG099_065_9000,
        player_start=30012840,
        area_id=30,
        block_id=1,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=73001, asset=Assets.AEG099_060_9000)
    Event_30012800()
    Event_30012810()
    Event_30012849()
    Event_30012811()
    CommonFunc_90005211(
        0,
        character=Characters.Imp7,
        animation_id=30010,
        animation_id_1=20010,
        region=30012800,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp8,
        animation_id=30010,
        animation_id_1=20010,
        region=30012800,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp9,
        animation_id=30010,
        animation_id_1=20010,
        region=30012800,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp10,
        animation_id=30010,
        animation_id_1=20010,
        region=30012800,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005920(0, flag=30010520, asset=30011520, obj_act_id=30013520)
    CommonFunc_90005650(
        0,
        flag=30010540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_1000,
        obj_act_id=30013541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30010540, anchor_entity=Assets.AEG027_041_0500)
    Event_30012505()
    Event_30012506()
    CommonFunc_90005670(
        0,
        flag=30012500,
        flag_1=30012510,
        flag_2=30012511,
        entity=Assets.AEG027_004_1000,
        region=30012500,
        region_1=30012502,
        right=0,
    )
    Event_30012520()
    Event_30012580()
    Event_30010790(0, 30011520, 30010800)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=Characters.Imp0,
        animation_id=30004,
        animation_id_1=20004,
        region=30012200,
        radius=0.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp1,
        animation_id=30002,
        animation_id_1=20002,
        region=30012201,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp2,
        animation_id=30002,
        animation_id_1=20002,
        region=30012203,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp3,
        animation_id=30000,
        animation_id_1=20000,
        region=30012204,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp4,
        animation_id=30000,
        animation_id_1=20000,
        region=30012205,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp5,
        animation_id=30009,
        animation_id_1=20009,
        region=30012207,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp6,
        animation_id=30009,
        animation_id_1=20009,
        region=30012209,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse15,
        animation_id=30000,
        animation_id_1=20000,
        region=30012315,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse1,
        animation_id=30000,
        animation_id_1=20000,
        region=30012312,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30000,
        animation_id_1=20000,
        region=30012312,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30000,
        animation_id_1=20000,
        region=30012312,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse5,
        animation_id=30000,
        animation_id_1=20000,
        region=30012312,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse3,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse6,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse12,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=0.8999999761581421,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse8,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse7,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse10,
        animation_id=30000,
        animation_id_1=20000,
        region=30012322,
        radius=5.0,
        seconds=3.5999999046325684,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(0, 30010311, 30000, 20000, 30012322, 5.0, 3.9000000953674316, 0, 0, 0, 0)


@RestartOnRest(30012330)
def Event_30012330(_, character: uint, character_1: uint):
    """Event 30012330"""
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30012301))
    AND_5.Add(AND_1)
    AND_5.Add(CharacterAlive(character))
    
    MAIN.Await(AND_5)
    
    ForceSpawnerToSpawn(spawner=character_1)
    Restart()


@RestartOnRest(30012910)
def Event_30012910(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 30012910"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    EnableCharacter(character)
    EnableAnimations(character)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.30000001192092896)
    Move(
        Characters.ErdtreeBurialWatchdog,
        destination=30012901,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.ErdtreeBurialWatchdog,
    )
    EnableAI(character)


@ContinueOnRest(30012500)
def Event_30012500():
    """Event 30012500"""
    GotoIfFlagEnabled(Label.L0, flag=30010500)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30012500))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Assets.AEG027_004_1000, 12, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(AllPlayersOutsideRegion(region=30012500))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    EnableFlag(30010500)
    ForceAnimation(Assets.AEG027_004_1000, 20, wait_for_completion=True)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(30010500)
    ForceAnimation(Assets.AEG027_004_1000, 21, wait_for_completion=True)
    Restart()


@ContinueOnRest(30012505)
def Event_30012505():
    """Event 30012505"""
    AND_1.Add(FlagEnabled(30012510))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30012502))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4195))
    
    MAIN.Await(AND_1)
    
    MoveAssetToCharacter(Assets.AEG099_090_9000, character=PLAYER, model_point=93)
    WaitFrames(frames=1)
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301200,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301210,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301220,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301230,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301240,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301250,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301260,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=30013501,
            asset=Assets.AEG099_090_9000,
            model_point=100,
            behavior_param_id=801301270,
            target_type=DamageTargetType.Character,
            radius=2.0,
            life=0.10000000149011612,
            repetition_time=0.0,
        )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=30013501)
    Wait(0.5)
    Restart()


@ContinueOnRest(30012506)
def Event_30012506():
    """Event 30012506"""
    AND_1.Add(FlagEnabled(30012510))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30012501))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4195)
    Wait(0.5)
    Restart()


@EndOnRest(30012520)
def Event_30012520():
    """Event 30012520"""
    DisableFlag(30010500)
    End()


@ContinueOnRest(30012580)
def Event_30012580():
    """Event 30012580"""
    RegisterLadder(start_climbing_flag=30010580, stop_climbing_flag=30010581, asset=Assets.AEG027_005_1000)


@RestartOnRest(30010790)
def Event_30010790(_, asset: uint, flag: uint):
    """Event 30010790"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ThisEventSlotFlagDisabled())
    
    MAIN.Await(AND_1)
    
    DisableThisSlotFlag()
    EnableAssetActivation(asset, obj_act_id=-1)
    End()


@RestartOnRest(30012800)
def Event_30012800():
    """Event 30012800"""
    if FlagEnabled(30010800):
        return
    
    MAIN.Await(HealthValue(Characters.ErdtreeBurialWatchdog) <= 0)
    
    Kill(30015800)
    Wait(4.0)
    PlaySoundEffect(Characters.ErdtreeBurialWatchdog, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.ErdtreeBurialWatchdog))
    
    KillBossAndDisplayBanner(character=Characters.ErdtreeBurialWatchdog, banner_type=BannerType.EnemyFelled)
    EnableFlag(30010800)
    EnableFlag(9201)
    if PlayerInOwnWorld():
        EnableFlag(61201)


@RestartOnRest(30012810)
def Event_30012810():
    """Event 30012810"""
    GotoIfFlagDisabled(Label.L0, flag=30010800)
    DisableCharacter(30015800)
    DisableAnimations(30015800)
    Kill(30015800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.ErdtreeBurialWatchdog)
    AND_2.Add(FlagEnabled(30012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.ErdtreeBurialWatchdog)
    SetNetworkUpdateRate(Characters.ErdtreeBurialWatchdog, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ErdtreeBurialWatchdog, name=904260301)


@RestartOnRest(30012811)
def Event_30012811():
    """Event 30012811"""
    if FlagEnabled(30010800):
        return
    AND_1.Add(HealthRatio(Characters.ErdtreeBurialWatchdog) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30012802)


@RestartOnRest(30012849)
def Event_30012849():
    """Event 30012849"""
    CommonFunc_9005800(
        0,
        flag=30010800,
        entity=Assets.AEG099_001_9000,
        region=30012800,
        flag_1=30012805,
        character=30015800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30010800,
        entity=Assets.AEG099_001_9000,
        region=30012800,
        flag_1=30012805,
        flag_2=30012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30010800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30010800, 930000, 30012805, 30012806, 0, 30012802, 0, 0)
