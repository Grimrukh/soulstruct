"""
Divine Tower of West Altus

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
from .enums.m34_12_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=34120000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=34120001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=34120002, asset=Assets.AEG099_060_9002)
    Event_34122800()
    Event_34122810()
    Event_34122811()
    Event_34122849()
    Event_34122510()
    Event_34122515()
    CommonFunc_90005501(
        0,
        flag=34120510,
        flag_1=34120511,
        left=0,
        asset=Assets.AEG027_001_7000,
        asset_1=Assets.AEG027_080_7000,
        asset_2=Assets.AEG027_080_7001,
        flag_2=34120512,
    )
    CommonFunc_90005508(
        0,
        flag=34120515,
        flag_1=34121515,
        left=0,
        entity=Assets.AEG027_070_0500,
        asset=Assets.AEG027_203_0501,
        asset_1=Assets.AEG027_203_0500,
        flag_2=34120516,
    )
    Event_34122580()
    CommonFunc_90005646(
        0,
        flag=34120800,
        left_flag=34122840,
        cancel_flag__right_flag=34122841,
        asset=Assets.AEG099_065_9000,
        player_start=34122840,
        area_id=34,
        block_id=12,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005560(0, flag=34120650, asset=Assets.AEG099_635_9000, left=0)
    CommonFunc_90005525(0, flag=34120590, asset=Assets.AEG027_069_0500)
    CommonFunc_90005525(0, flag=34120591, asset=Assets.AEG027_069_0501)
    CommonFunc_90005525(0, flag=34120592, asset=Assets.AEG027_069_0502)
    CommonFunc_90005525(0, flag=34120593, asset=Assets.AEG027_069_0503)
    CommonFunc_90005525(0, flag=34120594, asset=Assets.AEG027_069_0504)
    CommonFunc_90005110(
        0,
        flag=194,
        flag_1=9122,
        asset=Assets.AEG099_991_9000,
        item_lot=34120500,
        item=8151,
        vfx_id=806936,
        action_button_id=9083,
        animation_id=60523,
        left=0,
    )
    Event_32012200(
        0,
        character=Characters.TunnelMiner1,
        animation_id=30000,
        animation_id_1=20000,
        special_effect=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9000,
        asset_1=Assets.AEG099_780_9001,
        asset_2=0,
        asset_3=0,
    )
    Event_32012200(
        1,
        character=Characters.TunnelMiner2,
        animation_id=30002,
        animation_id_1=20002,
        special_effect=16574,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9002,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32012200(
        2,
        character=Characters.TunnelMiner3,
        animation_id=30000,
        animation_id_1=20000,
        special_effect=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9003,
        asset_1=Assets.AEG099_780_9004,
        asset_2=0,
        asset_3=0,
    )
    Event_32012200(
        3,
        character=34120304,
        animation_id=30000,
        animation_id_1=20000,
        special_effect=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=34121610,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_34122400(0, character=34120200, region=34122200)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_34120519()
    CommonFunc_90005250(0, character=Characters.VulgarMilitia0, region=34122201, seconds=0.5, animation_id=3020)
    CommonFunc_90005251(0, character=Characters.VulgarMilitia0, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia1,
        region=34122210,
        radius=8.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.VulgarMilitia2, region=34122211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.VulgarMilitia3, region=34122211, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.VulgarMilitia4, radius=16.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005250(0, character=Characters.VulgarMilitia5, region=34122210, seconds=0.5, animation_id=3020)
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia6,
        region=34122216,
        radius=15.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=34120250, region=34122250, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=34120251, region=34122250, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=34120255, region=34122255, seconds=0.20000000298023224, animation_id=-1)
    CommonFunc_90005250(0, character=34120256, region=34122255, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=34120257, region=34122255, seconds=0.5, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster0, region=34122258, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster1, region=34122258, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster2, region=34122260, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster3, region=34122261, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster4, region=34122263, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster5, region=34122263, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster6, region=34122263, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(
        0,
        character=Characters.AbnormalStoneCluster7,
        region=34122265,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005260(
        0,
        character=Characters.AbnormalStoneCluster8,
        region=34122265,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005260(
        0,
        character=Characters.AbnormalStoneCluster9,
        region=34122265,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster10, region=34122268, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster11, region=34122270, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster12, region=34122270, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster13, region=34122270, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.AbnormalStoneCluster14, region=34122270, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner0, region=34122300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner4, region=34122305, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.IronVirgin, region=34122350, seconds=0.0, animation_id=-1)


@ContinueOnRest(34122510)
def Event_34122510():
    """Event 34122510"""
    CommonFunc_90005500(
        0,
        flag=34120510,
        flag_1=34120511,
        left=0,
        asset=Assets.AEG027_001_7000,
        asset_1=Assets.AEG027_080_7000,
        obj_act_id=34123511,
        asset_2=Assets.AEG027_080_7001,
        obj_act_id_1=34123512,
        region=34122511,
        region_1=34122512,
        flag_2=34120512,
        flag_3=34120513,
        left_1=0,
    )


@ContinueOnRest(34122515)
def Event_34122515():
    """Event 34122515"""
    CommonFunc_90005507(
        0,
        flag=34120515,
        flag_1=34121515,
        left=0,
        asset=Assets.AEG027_070_0500,
        entity=Assets.AEG027_203_0501,
        region=34122518,
        entity_1=Assets.AEG027_203_0500,
        region_1=34122519,
        region_2=34122516,
        region_3=34122517,
        flag_2=34120516,
        flag_3=34122517,
        left_1=0,
    )


@ContinueOnRest(34120519)
def Event_34120519():
    """Event 34120519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(34120510)
    EnableThisSlotFlag()


@RestartOnRest(34122580)
def Event_34122580():
    """Event 34122580"""
    RegisterLadder(start_climbing_flag=34120530, stop_climbing_flag=34120531, asset=Assets.AEG027_034_7000)


@RestartOnRest(32012200)
def Event_32012200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: Asset | int,
    asset_1: Asset | int,
    asset_2: Asset | int,
    asset_3: Asset | int,
):
    """Event 32012200"""
    if ThisEventSlotFlagEnabled():
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_10.Add(AssetDestroyed(asset))
    OR_10.Add(AssetDestroyed(asset_1))
    OR_10.Add(AssetDestroyed(asset_2))
    OR_10.Add(AssetDestroyed(asset_3))
    AND_1.Add(OR_10)
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(34122400)
def Event_34122400(_, character: Character | int, region: Region | int):
    """Event 34122400"""
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    Wait(0.4000000059604645)
    Restart()


@RestartOnRest(34122800)
def Event_34122800():
    """Event 34122800"""
    if FlagEnabled(34120800):
        return
    
    MAIN.Await(HealthValue(Characters.OnyxLord) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(34128500, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.OnyxLord))
    
    KillBossAndDisplayBanner(character=Characters.OnyxLord, banner_type=BannerType.EnemyFelled)
    EnableFlag(34120800)
    EnableFlag(9264)
    if PlayerInOwnWorld():
        EnableFlag(61264)


@RestartOnRest(34122810)
def Event_34122810():
    """Event 34122810"""
    GotoIfFlagDisabled(Label.L0, flag=34120800)
    DisableCharacter(Characters.OnyxLord)
    DisableAnimations(Characters.OnyxLord)
    Kill(Characters.OnyxLord)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.OnyxLord)
    GotoIfFlagEnabled(Label.L1, flag=34120801)
    DisableCharacter(Characters.OnyxLord)
    ForceAnimation(Characters.OnyxLord, 30000, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34122801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.OnyxLord, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(34120801)
    EnableCharacter(Characters.OnyxLord)
    ForceAnimation(Characters.OnyxLord, 20000, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(34122805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=34122800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.OnyxLord)
    SetNetworkUpdateRate(Characters.OnyxLord, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.OnyxLord, name=903600320)


@RestartOnRest(34122811)
def Event_34122811():
    """Event 34122811"""
    if FlagEnabled(34120800):
        return
    AND_1.Add(HealthRatio(Characters.OnyxLord) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(34122802)


@RestartOnRest(34122849)
def Event_34122849():
    """Event 34122849"""
    CommonFunc_9005800(
        0,
        flag=34120800,
        entity=Assets.AEG099_003_9000,
        region=34122800,
        flag_1=34122805,
        character=34125800,
        action_button_id=10000,
        left=34120801,
        region_1=34122801,
    )
    CommonFunc_9005801(
        0,
        flag=34120800,
        entity=Assets.AEG099_003_9000,
        region=34122800,
        flag_1=34122805,
        flag_2=34122806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=34120800, asset=Assets.AEG099_003_9000, vfx_id=3, right=34120801)
    CommonFunc_9005822(
        0,
        flag=34120800,
        bgm_boss_conv_param_id=931000,
        flag_1=34122805,
        flag_2=34122806,
        right=0,
        flag_3=34122802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005811(0, flag=34120800, asset=Assets.AEG099_003_9001, vfx_id=3, right=34120801)
