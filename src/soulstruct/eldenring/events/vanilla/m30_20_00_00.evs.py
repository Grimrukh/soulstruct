"""
Hidden Path to the Haligtree

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
from .enums.m30_20_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=30200000, asset=Assets.AEG099_060_9000)
    Event_30202800()
    Event_30202810()
    Event_30202811()
    Event_30202829()
    CommonFunc_90005616(0, flag=30207910, region=30202700)
    CommonFunc_90005211(
        0,
        character=Characters.GiantOctopus0,
        animation_id=30002,
        animation_id_1=20002,
        region=30202200,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GiantOctopus1,
        animation_id=30002,
        animation_id_1=20002,
        region=30202201,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GiantOctopus2,
        animation_id=30002,
        animation_id_1=20002,
        region=30202202,
        radius=1.0,
        seconds=1.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Octopus0,
        region=30202200,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Octopus1,
        region=30202200,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Octopus4,
        region=30202257,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Octopus5,
        region=30202257,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Octopus6, region=30202257, radius=1.0, seconds=0.5, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.Octopus7,
        region=30202257,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Octopus8,
        region=30202257,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia2,
        animation_id=30002,
        animation_id_1=20002,
        region=30202243,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia3,
        animation_id=30002,
        animation_id_1=20002,
        region=30202243,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia4,
        animation_id=30002,
        animation_id_1=20002,
        region=30202243,
        radius=1.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia6,
        animation_id=30002,
        animation_id_1=20002,
        region=30202250,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia7,
        animation_id=30002,
        animation_id_1=20002,
        region=30202250,
        radius=2.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia8,
        animation_id=30000,
        animation_id_1=20000,
        region=30202250,
        radius=2.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia9,
        region=30202253,
        radius=0.0,
        seconds=0.800000011920929,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia10,
        region=30202254,
        radius=0.0,
        seconds=0.800000011920929,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia11,
        animation_id=30001,
        animation_id_1=20001,
        region=30202202,
        radius=1.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.VulgarMilitia12,
        animation_id=30001,
        animation_id_1=20001,
        region=30202202,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia13,
        region=30202257,
        radius=0.0,
        seconds=0.800000011920929,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia14,
        region=30202260,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia15,
        region=30202260,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia16,
        region=30202260,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia17,
        region=30202260,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005646(
        0,
        flag=30200800,
        left_flag=30202840,
        cancel_flag__right_flag=30202841,
        asset=Assets.AEG099_065_9000,
        player_start=30202840,
        area_id=30,
        block_id=20,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005525(0, flag=30200560, asset=Assets.AEG027_157_9000)
    CommonFunc_90005501(
        0,
        flag=30200510,
        flag_1=30200511,
        left=4,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=30200512,
    )
    Event_30202510()
    CommonFunc_90005650(
        0,
        flag=30200540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_9000,
        obj_act_id=30203541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30200540, anchor_entity=Assets.AEG027_041_0500)
    Event_30202200()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005460(0, character=Characters.GiantOctopus0)
    CommonFunc_90005461(0, character=Characters.GiantOctopus0)
    CommonFunc_90005462(0, character=Characters.GiantOctopus0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus1)
    CommonFunc_90005461(0, character=Characters.GiantOctopus1)
    CommonFunc_90005462(0, character=Characters.GiantOctopus1)
    CommonFunc_90005460(0, character=Characters.GiantOctopus2)
    CommonFunc_90005461(0, character=Characters.GiantOctopus2)
    CommonFunc_90005462(0, character=Characters.GiantOctopus2)


@ContinueOnRest(30202510)
def Event_30202510():
    """Event 30202510"""
    CommonFunc_90005500(
        0,
        flag=30200510,
        flag_1=30200511,
        left=4,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0500,
        obj_act_id=30203511,
        asset_2=Assets.AEG027_002_0501,
        obj_act_id_1=30203512,
        region=30202511,
        region_1=30202512,
        flag_2=30200512,
        flag_3=30200513,
        left_1=0,
    )


@RestartOnRest(30202520)
def Event_30202520(_, flag: Flag | int, asset: Asset | int, flag_1: Flag | int):
    """Event 30202520"""
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


@RestartOnRest(30202200)
def Event_30202200():
    """Event 30202200"""
    DisableAsset(Assets.AEG020_940_1000)
    End()


@RestartOnRest(30202800)
def Event_30202800():
    """Event 30202800"""
    if FlagEnabled(30200800):
        return
    
    MAIN.Await(HealthValue(Characters.StrayMimicTear) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(30208000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.StrayMimicTear))
    
    KillBossAndDisplayBanner(character=Characters.StrayMimicTear, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG099_630_9001, obj_act_id=-1)
    EnableFlag(30200800)
    EnableFlag(9220)
    if PlayerInOwnWorld():
        EnableFlag(61220)


@RestartOnRest(30202810)
def Event_30202810():
    """Event 30202810"""
    GotoIfFlagDisabled(Label.L0, flag=30200800)
    DisableCharacter(30205800)
    DisableAnimations(30205800)
    Kill(30205800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30205800)
    DisableCharacter(Characters.StrayMimicTear)
    DisableAnimations(Characters.StrayMimicTear)
    DisableHealthBar(Characters.StrayMimicTear)
    DisableAssetActivation(Assets.AEG099_630_9001, obj_act_id=-1)
    AND_2.Add(FlagEnabled(30202805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30202800))
    
    MAIN.Await(AND_2)
    
    SetNetworkUpdateRate(Characters.StrayMimicTear, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.SilverTear, 20010)
    CopyPlayerCharacterData(source_character=PLAYER, dest_character=Characters.StrayMimicTear)
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.SilverTear, 16307))
    
    EnableCharacter(Characters.StrayMimicTear)
    EnableAnimations(Characters.StrayMimicTear)
    DisableAnimations(Characters.SilverTear)
    Wait(0.5)
    Move(
        Characters.StrayMimicTear,
        destination=Characters.SilverTear,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=Characters.SilverTear,
    )
    ForceAnimation(Characters.StrayMimicTear, 63010, skip_transition=True)
    Wait(4.0)
    EnableAI(30205800)
    SetNetworkUpdateRate(30205800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.StrayMimicTear, name=903320300)


@RestartOnRest(30202811)
def Event_30202811():
    """Event 30202811"""
    if FlagEnabled(30200800):
        return
    AND_1.Add(HealthRatio(Characters.StrayMimicTear) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30202802)


@RestartOnRest(30202829)
def Event_30202829():
    """Event 30202829"""
    CommonFunc_9005800(
        0,
        flag=30200800,
        entity=Assets.AEG099_001_9000,
        region=30202800,
        flag_1=30202805,
        character=30205800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30200800,
        entity=Assets.AEG099_001_9000,
        region=30202800,
        flag_1=30202805,
        flag_2=30202806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30200800, asset=Assets.AEG099_001_9000, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30200800,
        bgm_boss_conv_param_id=921100,
        flag_1=30202805,
        flag_2=30202806,
        right=0,
        flag_3=30202802,
        left=0,
        left_1=0,
    )
