"""
Astel Arena

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
from .entities.m12_04_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=12040800,
        grace_flag=71240,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_12042680()
    Event_12042400()
    Event_12042849()
    Event_12042800()
    Event_12042810()


@ContinueOnRest(12042400)
def Event_12042400():
    """Event 12042400"""
    GotoIfFlagDisabled(Label.L0, flag=114)
    DisableAsset(Assets.AEG099_002_9002)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerNotInOwnWorld():
        Goto(Label.L10)
    if ThisEventSlotFlagDisabled():
        DeleteVFX(12041400)
        CreateAssetVFX(Assets.AEG099_002_9002, vfx_id=101, model_point=1507)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9506, entity=Assets.AEG099_002_9002))
    AND_2.Add(FlagEnabled(114))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFlagEnabled(Label.L1, flag=114)
    if PlayerInOwnWorld():
        DisplayDialog(text=20006, anchor_entity=0, display_distance=5.0)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteVFX(12041400)
    DisableAsset(Assets.AEG099_002_9002)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteVFX(12041400)
    CreateAssetVFX(Assets.AEG099_002_9002, vfx_id=101, model_point=1507)
    OR_9.Add(FlagEnabled(114))
    
    MAIN.Await(OR_9)
    
    DeleteVFX(12041400)
    DisableAsset(Assets.AEG099_002_9002)
    End()


@RestartOnRest(12042680)
def Event_12042680():
    """Event 12042680"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        DeleteVFX(12043680, erase_root_only=False)
    AND_1.Add(OutsideMap(game_map=ASTEL_ARENA))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12042680))
    OR_1.Add(AND_1)
    AND_2.Add(InsideMap(game_map=ASTEL_ARENA))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=1034412680))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    CreateVFX(12043680)
    Wait(1.0)
    AND_10.Add(InsideMap(game_map=ASTEL_ARENA))
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=1034412680))
    OR_10.Add(AND_10)
    AND_11.Add(OutsideMap(game_map=ASTEL_ARENA))
    AND_11.Add(CharacterOutsideRegion(character=PLAYER, region=12042680))
    OR_10.Add(AND_11)
    
    MAIN.Await(OR_10)
    
    DeleteVFX(12043680)
    Wait(1.0)
    Restart()


@ContinueOnRest(12042800)
def Event_12042800():
    """Event 12042800"""
    if FlagEnabled(12040800):
        return
    
    MAIN.Await(HealthRatio(Characters.MalformedStar) <= 0.0)
    
    Wait(5.0)
    PlaySoundEffect(Characters.MalformedStar, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.MalformedStar))
    
    KillBossAndDisplayBanner(character=Characters.MalformedStar, banner_type=BannerType.LegendFelled)
    EnableFlag(12040800)
    EnableFlag(9108)
    if PlayerInOwnWorld():
        EnableFlag(61108)


@RestartOnRest(12042810)
def Event_12042810():
    """Event 12042810"""
    GotoIfFlagDisabled(Label.L0, flag=12040800)
    DisableCharacter(Characters.MalformedStar)
    DisableAnimations(Characters.MalformedStar)
    Kill(Characters.MalformedStar)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MalformedStar)
    EnableNavmeshType(navmesh_id=12044300, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=12044301, navmesh_type=NavmeshType.Solid)
    AND_2.Add(FlagEnabled(12042805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12042800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MalformedStar)
    SetNetworkUpdateRate(Characters.MalformedStar, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MalformedStar, name=904620001)
    SetCharacterEventTarget(Characters.MalformedStar, entity=Characters.TalkDummy2)


@ContinueOnRest(12042849)
def Event_12042849():
    """Event 12042849"""
    CommonFunc_9005811(0, flag=12040800, asset=Assets.AEG099_002_9001, model_point=8, right=0)
    CommonFunc_9005800(
        0,
        flag=12040800,
        entity=Assets.AEG099_002_9000,
        region=12042800,
        flag_1=12042805,
        character=12045800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=12040800,
        entity=Assets.AEG099_002_9000,
        region=12042800,
        flag_1=12042805,
        flag_2=12042806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12040800, asset=Assets.AEG099_002_9000, model_point=8, right=0)
    CommonFunc_9005822(
        0,
        flag=12040800,
        bgm_boss_conv_param_id=920700,
        flag_1=12042805,
        flag_2=12042806,
        right=0,
        flag_3=12042802,
        left=0,
        left_1=0,
    )
