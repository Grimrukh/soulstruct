"""
War-Dead Catacombs

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
from .enums.m30_16_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301600, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, dummy_id=100, vfx_id=800, right=0)
    Event_30162800()
    Event_30162810()
    Event_30162849()
    Event_30162811()
    CommonFunc_90005200(
        0,
        character=Characters.RedmaneKnight4,
        animation_id=30000,
        animation_id_1=20000,
        region=30162316,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.RedmaneKnight2,
        animation_id=30001,
        animation_id_1=20001,
        region=30162242,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30162622()
    CommonFunc_90005250(0, character=30160221, region=30162221, seconds=0.0, animation_id=-1)
    CommonFunc_90005650(
        0,
        flag=30160540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30163541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30160540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005646(
        0,
        flag=30160800,
        left_flag=30162840,
        cancel_flag__right_flag=30162841,
        asset=Assets.AEG099_065_9000,
        player_start=30162840,
        area_id=30,
        block_id=16,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.RadahnSoldier2,
        animation_id=30008,
        animation_id_1=20008,
        region=30162212,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RadahnFootSoldier0,
        animation_id=30010,
        animation_id_1=20010,
        region=30162230,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RadahnFootSoldier1,
        animation_id=30010,
        animation_id_1=20010,
        region=30162230,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RadahnSoldier5,
        animation_id=30008,
        animation_id_1=20008,
        region=30162216,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.RadahnSoldier6, region=30162221, seconds=0.0, animation_id=3006)
    CommonFunc_90005200(
        0,
        character=Characters.Imp4,
        animation_id=30002,
        animation_id_1=20002,
        region=30162204,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp5, region=30162205, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=30162206,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp0,
        animation_id=30010,
        animation_id_1=20010,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp1,
        animation_id=30010,
        animation_id_1=20010,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp3,
        animation_id=30010,
        animation_id_1=20010,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight4,
        animation_id=30003,
        animation_id_1=20003,
        region=30162244,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight1,
        animation_id=30003,
        animation_id_1=20003,
        region=30162301,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight0,
        animation_id=30003,
        animation_id_1=20003,
        region=30162244,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight2,
        animation_id=30003,
        animation_id_1=20003,
        region=30162302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight5,
        animation_id=30003,
        animation_id_1=20003,
        region=30162210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight3,
        animation_id=30003,
        animation_id_1=20003,
        region=30162210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RadahnSoldier0,
        animation_id=30008,
        animation_id_1=20008,
        region=30162210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RadahnSoldier1,
        animation_id=30008,
        animation_id_1=20008,
        region=30162210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RedmaneKnight1,
        animation_id=30001,
        animation_id_1=20001,
        region=30162210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30162602(0, character=Characters.RedmaneKnight0, character_1=Characters.RedmaneKnight1, animation_id=20001)
    Event_30162602(1, character=Characters.RedmaneKnight3, character_1=Characters.RedmaneKnight0, animation_id=20001)
    Event_30162621(0, character=30165290)


@RestartOnRest(30162601)
def Event_30162601(_, region: Region | int, entity: uint):
    """Event 30162601"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=entity)
    EnableThisNetworkSlotFlag()


@RestartOnRest(30162602)
def Event_30162602(_, character: uint, character_1: Character | int, animation_id: int):
    """Event 30162602"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    
    MAIN.Await(CharacterDead(character_1))
    
    EnableCharacter(character)
    ForceAnimation(character, animation_id)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)


@RestartOnRest(30162511)
def Event_30162511(_, character: Character | int, special_effect: int, region: Region | int):
    """Event 30162511"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect)


@RestartOnRest(30162622)
def Event_30162622():
    """Event 30162622"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30162245))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ChangePatrolBehavior(Characters.RedmaneKnight2, patrol_information_id=30163314)


@RestartOnRest(30162621)
def Event_30162621(_, character: uint):
    """Event 30162621"""
    ReturnIfFlagState(EventReturnType.End, FlagSetting.On, FlagType.RelativeToThisEventSlot, 30162621)
    AddSpecialEffect(character, 4802)
    AddSpecialEffect(character, 4800)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.CleanrotKnight3, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.CleanrotKnight5, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RadahnSoldier0, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RadahnSoldier1, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RedmaneKnight1, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RedmaneKnight0, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RedmaneKnight3, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.CleanrotKnight3, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.CleanrotKnight5, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RadahnSoldier0, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RadahnSoldier1, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RedmaneKnight1, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RedmaneKnight0, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.RedmaneKnight3, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=character, radius=5.0))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 30162621, state=FlagSetting.On)
    RemoveSpecialEffect(character, 4800)
    AddSpecialEffect(character, 4802)
    Wait(90.0)
    AND_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_10.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_15.Add(AND_10)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(OR_15)
    AND_5.Add(OR_15)
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=30162256))
    SkipLinesIfConditionFalse(1, AND_4)
    ForceSpawnerToSpawn(spawner=30163256)
    AND_5.Add(CharacterInsideRegion(character=PLAYER, region=30162258))
    SkipLinesIfConditionFalse(1, AND_5)
    ForceSpawnerToSpawn(spawner=30163258)
    Restart()


@RestartOnRest(30162520)
def Event_30162520(_, flag: Flag | int, asset: Asset | int, flag_1: Flag | int):
    """Event 30162520"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@RestartOnRest(30162800)
def Event_30162800():
    """Event 30162800"""
    if FlagEnabled(30160800):
        return
    
    MAIN.Await(HealthValue(Characters.UlceratedTreeSpirit) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.UlceratedTreeSpirit, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.UlceratedTreeSpirit))
    
    KillBossAndDisplayBanner(character=Characters.UlceratedTreeSpirit, banner_type=BannerType.EnemyFelled)
    EnableFlag(30160800)
    if PlayerInOwnWorld():
        EnableFlag(61216)
    EnableFlag(9216)


@RestartOnRest(30162810)
def Event_30162810():
    """Event 30162810"""
    GotoIfFlagDisabled(Label.L0, flag=30160800)
    DisableCharacter(Characters.UlceratedTreeSpirit)
    DisableAnimations(Characters.UlceratedTreeSpirit)
    Kill(Characters.UlceratedTreeSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.UlceratedTreeSpirit)
    DisableHealthBar(Characters.UlceratedTreeSpirit)
    ForceAnimation(Characters.UlceratedTreeSpirit, 30002, loop=True)
    AND_2.Add(FlagEnabled(30162805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30162800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.UlceratedTreeSpirit, 20002)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.UlceratedTreeSpirit)
    SetNetworkUpdateRate(Characters.UlceratedTreeSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(4.300000190734863)
    EnableBossHealthBar(Characters.UlceratedTreeSpirit, name=904640300)
    EnableNetworkFlag(30162803)


@RestartOnRest(30162811)
def Event_30162811():
    """Event 30162811"""
    if FlagEnabled(30160800):
        return
    AND_1.Add(HealthRatio(Characters.UlceratedTreeSpirit) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30162802)


@RestartOnRest(30162849)
def Event_30162849():
    """Event 30162849"""
    CommonFunc_9005800(
        0,
        flag=30160800,
        entity=Assets.AEG099_001_9000,
        region=30162800,
        flag_1=30162805,
        character=30165800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30160800,
        entity=Assets.AEG099_001_9000,
        region=30162800,
        flag_1=30162805,
        flag_2=30162806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30160800, asset=Assets.AEG099_001_9000, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30160800,
        bgm_boss_conv_param_id=920600,
        flag_1=30162805,
        flag_2=30162806,
        right=30162803,
        flag_3=30162802,
        left=0,
        left_1=0,
    )


@RestartOnRest(30162900)
def Event_30162900():
    """Event 30162900"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(30160800))
    
    CreateAssetVFX(30161900, dummy_id=90, vfx_id=1300)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9000, entity=30161900))
    
    WarpToMap(game_map=MOHGWYN_PALACE, player_start=12052900)
