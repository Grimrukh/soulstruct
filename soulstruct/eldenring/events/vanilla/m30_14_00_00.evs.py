"""
Minor Erdtree Catacombs

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
from .entities.m30_14_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301400, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    Event_30142800()
    Event_30142801()
    Event_30142849()
    Event_30142811()
    CommonFunc_90005200(
        0,
        character=Characters.Imp0,
        animation_id=30001,
        animation_id_1=20001,
        region=30142262,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        region=30142201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30140268, 30142251, 0.0, -1)
    CommonFunc_90005250(0, 30140202, 30142202, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.Imp4,
        animation_id=30001,
        animation_id_1=20001,
        region=30142256,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp5, region=30142264, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, character=30140253, region=30142261, seconds=0.5, animation_id=3004)
    CommonFunc_90005200(
        0,
        character=30140269,
        animation_id=30001,
        animation_id_1=20001,
        region=30142265,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallCrab0,
        animation_id=30001,
        animation_id_1=20001,
        region=30142265,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallCrab1,
        animation_id=30001,
        animation_id_1=20001,
        region=30142265,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallCrab2,
        animation_id=30001,
        animation_id_1=20001,
        region=30142265,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp7,
        animation_id=30000,
        animation_id_1=20000,
        region=30142258,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=30142258,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp8,
        animation_id=30010,
        animation_id_1=20010,
        region=30142258,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=30140213,
        animation_id=30009,
        animation_id_1=20009,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=30140214,
        animation_id=30009,
        animation_id_1=20009,
        radius=4.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30140216, 30142215, 0.0, -1)
    CommonFunc_90005250(0, 30140217, 30142215, 0.0, -1)
    CommonFunc_90005250(0, 30140264, 30142215, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass2,
        animation_id=30000,
        animation_id_1=20000,
        region=30142210,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass5,
        animation_id=30000,
        animation_id_1=20000,
        region=30142210,
        seconds=3.299999952316284,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass1,
        animation_id=30000,
        animation_id_1=20000,
        region=30142210,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30140219,
        animation_id=30009,
        animation_id_1=20009,
        region=30142219,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30140220,
        animation_id=30009,
        animation_id_1=20009,
        region=30142219,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30140222,
        animation_id=30009,
        animation_id_1=20009,
        region=30142219,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30140219, 30142219, 1.0, -1)
    CommonFunc_90005250(0, 30140220, 30142219, 0.0, -1)
    CommonFunc_90005250(0, 30140222, 30142219, 0.5, -1)
    CommonFunc_90005250(0, 30140223, 30142223, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass0,
        animation_id=30000,
        animation_id_1=20000,
        region=30142257,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass6,
        animation_id=30000,
        animation_id_1=20000,
        region=30142263,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass4,
        animation_id=30000,
        animation_id_1=20000,
        region=30142263,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass3,
        animation_id=30000,
        animation_id_1=20000,
        region=30142263,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005650(
        0,
        flag=30140540,
        asset=Assets.AEG027_041_0500,
        asset_1=30141541,
        obj_act_id=30143541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30140540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005501(
        0,
        flag=30140510,
        flag_1=30141510,
        left=0,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0502,
        asset_2=Assets.AEG027_002_0501,
        flag_2=30140511,
    )
    Event_30142510()
    Event_30142580()
    CommonFunc_90005646(
        0,
        flag=30140800,
        left_flag=30142840,
        cancel_flag__right_flag=30142841,
        asset=Assets.AEG099_065_9000,
        player_start=30142840,
        area_id=30,
        block_id=14,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, 30142800, 30141695, 5)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30140519()


@NeverRestart(30142510)
def Event_30142510():
    """Event 30142510"""
    CommonFunc_90005500(
        0,
        30140510,
        30141510,
        0,
        30141510,
        30141511,
        30143511,
        30141512,
        30143512,
        30142511,
        30142512,
        30140511,
        30142512,
        0,
    )


@NeverRestart(30140519)
def Event_30140519():
    """Event 30140519"""
    if FlagEnabled(30140519):
        return
    EnableFlag(30140510)


@RestartOnRest(30142520)
def Event_30142520(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30142520"""
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


@NeverRestart(30142580)
def Event_30142580():
    """Event 30142580"""
    RegisterLadder(start_climbing_flag=30140580, stop_climbing_flag=30140581, asset=Assets.AEG027_005_0500)


@RestartOnRest(30142800)
def Event_30142800():
    """Event 30142800"""
    if FlagEnabled(30140800):
        return
    AND_1.Add(HealthValue(Characters.ErdtreeBurialWatchdog0) <= 0)
    AND_1.Add(HealthValue(Characters.ErdtreeBurialWatchdog1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.ErdtreeBurialWatchdog0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.ErdtreeBurialWatchdog0))
    AND_2.Add(CharacterDead(Characters.ErdtreeBurialWatchdog1))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.ErdtreeBurialWatchdog0, banner_type=BannerType.EnemyFelled)
    EnableFlag(30140800)
    if PlayerInOwnWorld():
        EnableFlag(61214)
    EnableFlag(9214)


@RestartOnRest(30142801)
def Event_30142801():
    """Event 30142801"""
    GotoIfFlagDisabled(Label.L0, flag=30140800)
    DisableCharacter(Characters.ErdtreeBurialWatchdog0)
    DisableAnimations(Characters.ErdtreeBurialWatchdog0)
    Kill(Characters.ErdtreeBurialWatchdog0)
    DisableCharacter(Characters.ErdtreeBurialWatchdog1)
    DisableAnimations(Characters.ErdtreeBurialWatchdog1)
    Kill(Characters.ErdtreeBurialWatchdog1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.ErdtreeBurialWatchdog0)
    DisableAI(Characters.ErdtreeBurialWatchdog1)
    AND_2.Add(FlagEnabled(30142805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30142800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.ErdtreeBurialWatchdog0)
    SetNetworkUpdateRate(Characters.ErdtreeBurialWatchdog0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ErdtreeBurialWatchdog0, name=904260304)
    EnableAI(Characters.ErdtreeBurialWatchdog1)
    SetNetworkUpdateRate(Characters.ErdtreeBurialWatchdog1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ErdtreeBurialWatchdog1, name=904260305, bar_slot=1)


@RestartOnRest(30142811)
def Event_30142811():
    """Event 30142811"""
    if FlagEnabled(30140800):
        return
    AND_1.Add(HealthRatio(Characters.ErdtreeBurialWatchdog0) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30142802)


@RestartOnRest(30142849)
def Event_30142849():
    """Event 30142849"""
    CommonFunc_9005800(
        0,
        flag=30140800,
        entity=Assets.AEG099_001_9000,
        region=30142800,
        flag_1=30142805,
        character=30145800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30140800,
        entity=Assets.AEG099_001_9000,
        region=30142800,
        flag_1=30142805,
        flag_2=30142806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30140800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30140800, 930000, 30142805, 30142806, 0, 30142802, 0, 0)
