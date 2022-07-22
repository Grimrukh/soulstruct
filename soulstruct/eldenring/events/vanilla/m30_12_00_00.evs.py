"""
Unsightly Catacombs

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
from .entities.m30_12_00_00_entities import *
from .entities.m30_10_00_00_entities import Characters as m30_10_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301200, asset=Assets.AEG099_060_9001)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005201(
        0,
        character=Characters.Misbegotten0,
        animation_id=30000,
        animation_id_1=20000,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten1,
        animation_id=30000,
        animation_id_1=20000,
        region=30122201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.ScalyMisbegotten1, region=30122250, seconds=0.0, animation_id=0)
    CommonFunc_90005250(1, character=Characters.ScalyMisbegotten2, region=30122250, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Misbegotten2, region=30122205, seconds=0.0, animation_id=3000)
    CommonFunc_90005250(0, character=Characters.Misbegotten3, region=30122208, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.Misbegotten4, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.Misbegotten5, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.Misbegotten6, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.Misbegotten7, seconds=0.0, animation_id=-1)
    Event_30122300(0, character=Characters.Misbegotten8)
    Event_30122300(1, character=Characters.Misbegotten9)
    Event_30122300(2, character=Characters.Misbegotten10)
    Event_30122300(3, character=Characters.Misbegotten11)
    Event_30122300(4, character=Characters.Misbegotten12)
    Event_30122300(5, character=Characters.Misbegotten13)
    Event_30122300(6, character=Characters.Misbegotten14)
    Event_30122300(7, character=Characters.Misbegotten15)
    Event_30122300(8, character=Characters.Misbegotten16)
    Event_30122300(9, character=Characters.Misbegotten17)
    Event_30122300(10, character=Characters.Misbegotten18)
    Event_30122300(11, character=Characters.Misbegotten19)
    Event_30122502(0, character=Characters.Omen, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Omen, region=30122502, seconds=0.0, animation_id=0)
    Event_30122500()
    Event_30122501()
    CommonFunc_90005650(
        0,
        flag=30120540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30123541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30120540, anchor_entity=Assets.AEG027_041_0500)
    Event_30122800()
    Event_30122810()
    Event_30122849()
    Event_30122811()
    CommonFunc_90005646(
        0,
        flag=30120800,
        left_flag=30122840,
        cancel_flag__right_flag=30122841,
        asset=Assets.AEG099_065_9000,
        player_start=30122840,
        area_id=30,
        block_id=12,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, 30122800, 30121695, 5)


@RestartOnRest(30122520)
def Event_30122520(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30122520"""
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


@RestartOnRest(30122300)
def Event_30122300(_, character: uint):
    """Event 30122300"""
    Kill(character)
    End()


@RestartOnRest(30122500)
def Event_30122500():
    """Event 30122500"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30122500))
    AND_1.Add(CharacterBackreadEnabled(Characters.Omen))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(30122501)
def Event_30122501():
    """Event 30122501"""
    if FlagEnabled(30122502):
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30122501))
    AND_1.Add(CharacterBackreadEnabled(Characters.Omen))
    AND_1.Add(FlagEnabled(30122500))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(30122502)
    Wait(0.0)
    ForceAnimation(Characters.Omen, 3024, loop=True, wait_for_completion=True)
    EnableAI(Characters.Omen)
    End()


@RestartOnRest(30122502)
def Event_30122502(_, character: uint, seconds: float, animation_id: int):
    """Event 30122502"""
    if FlagEnabled(30122502):
        return
    DisableAI(character)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(30122502)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(30122800)
def Event_30122800():
    """Event 30122800"""
    if FlagEnabled(30120800):
        return
    AND_1.Add(HealthValue(Characters.LeonineMisbegotten) <= 0)
    AND_1.Add(HealthValue(Characters.DepravedPerfurmer) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(m30_10_Characters.CrucibleKnight0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.LeonineMisbegotten))
    AND_2.Add(CharacterDead(Characters.DepravedPerfurmer))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.LeonineMisbegotten, banner_type=BannerType.EnemyFelled)
    EnableFlag(30120800)
    EnableFlag(9211)
    if PlayerInOwnWorld():
        EnableFlag(61211)


@RestartOnRest(30122810)
def Event_30122810():
    """Event 30122810"""
    GotoIfFlagDisabled(Label.L0, flag=30120800)
    DisableCharacter(Characters.LeonineMisbegotten)
    DisableAnimations(Characters.LeonineMisbegotten)
    Kill(Characters.LeonineMisbegotten)
    DisableCharacter(Characters.DepravedPerfurmer)
    DisableAnimations(Characters.DepravedPerfurmer)
    Kill(Characters.DepravedPerfurmer)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.LeonineMisbegotten)
    DisableAI(Characters.DepravedPerfurmer)
    ForceAnimation(Characters.LeonineMisbegotten, 30001, loop=True)
    AND_2.Add(FlagEnabled(30122805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30122800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.LeonineMisbegotten, 20001)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.LeonineMisbegotten)
    SetNetworkUpdateRate(Characters.LeonineMisbegotten, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.LeonineMisbegotten, name=903460300)
    EnableAI(Characters.DepravedPerfurmer)
    SetNetworkUpdateRate(Characters.DepravedPerfurmer, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DepravedPerfurmer, name=903700300, bar_slot=1)


@RestartOnRest(30122811)
def Event_30122811():
    """Event 30122811"""
    if FlagEnabled(30120800):
        return
    OR_1.Add(HealthRatio(Characters.LeonineMisbegotten) <= 0.6000000238418579)
    OR_1.Add(CharacterDead(Characters.DepravedPerfurmer))
    
    MAIN.Await(OR_1)
    
    EnableFlag(30122802)


@RestartOnRest(30122849)
def Event_30122849():
    """Event 30122849"""
    CommonFunc_9005800(
        0,
        flag=30120800,
        entity=Assets.AEG099_001_9001,
        region=30122800,
        flag_1=30122805,
        character=30125800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30120800,
        entity=Assets.AEG099_001_9001,
        region=30122800,
        flag_1=30122805,
        flag_2=30122806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30120800, asset=Assets.AEG099_001_9001, model_point=3, right=0)
    CommonFunc_9005822(0, 30120800, 930000, 30122805, 30122806, 0, 30122802, 0, 0)
