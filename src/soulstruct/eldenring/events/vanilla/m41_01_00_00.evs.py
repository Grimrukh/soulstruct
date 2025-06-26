"""
m41_01_00_00

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=41010800,
        left_flag=41012840,
        cancel_flag__right_flag=41012841,
        asset=41011840,
        player_start=41012840,
        area_id=41,
        block_id=1,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=41011500, dummy_id=100, vfx_id=800, right=0)
    RegisterGrace(grace_flag=41010000, asset=41011950, enemy_block_distance=8.0)
    Event_41012800()
    Event_41012810()
    Event_41012811()
    Event_41012849()
    Event_41012610()
    Event_41012612()
    CommonFunc_90005511(0, flag=41018560, asset=41011560, obj_act_id=41013560, obj_act_id_1=449009, left=0)
    CommonFunc_90005512(0, flag=41018560, region=41012560, region_1=41012561)
    CommonFunc_90005511(0, flag=41018562, asset=41011562, obj_act_id=41013562, obj_act_id_1=449009, left=0)
    CommonFunc_90005512(0, flag=41018562, region=41012562, region_1=41012563)
    Event_41012580()
    Event_41012570(0, character=0, asset=41011510)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005221(0, character=41010201, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41010202, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005271(0, character=41010203, seconds=0.0, animation_id=-1)
    Event_41012570(1, character=41010203, asset=41011203)
    CommonFunc_90005261(0, character=41010204, region=41012204, radius=3.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005261(0, character=41010205, region=41012205, radius=2.0, seconds=0.5, animation_id=3001)
    CommonFunc_90005261(0, character=41010206, region=41012205, radius=2.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005261(0, character=41010207, region=41012205, radius=2.0, seconds=0.5, animation_id=3003)
    CommonFunc_90005221(0, character=41010208, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41010210, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41010213, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41010212, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005250(0, character=41010211, region=41012211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=41010214, region=41012211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=41010215, region=41012215, seconds=0.0, animation_id=3003)
    CommonFunc_90005221(0, character=41010217, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41010218, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=41010220, region=41012220, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(0, character=41010221, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=41010225, region=41012225, radius=1.0, seconds=1.5, animation_id=3004)
    CommonFunc_90005271(0, character=41010231, seconds=0.0, animation_id=-1)
    Event_41012570(2, character=41010231, asset=41011231)
    CommonFunc_90005271(0, character=41010233, seconds=0.0, animation_id=-1)
    Event_41012570(3, character=41010233, asset=41011233)
    CommonFunc_90005261(0, character=41010235, region=41012235, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41010236, region=41012235, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41010330, region=41012330, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=41010331,
        animation_id=30002,
        animation_id_1=20002,
        region=41012331,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010337,
        animation_id=30000,
        animation_id_1=20000,
        region=41012337,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010300,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010301,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010302,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010303,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010305,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010306,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010307,
        animation_id=30000,
        animation_id_1=20000,
        region=41012300,
        radius=0.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010312,
        animation_id=30000,
        animation_id_1=20000,
        region=41012308,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010313,
        animation_id=30000,
        animation_id_1=20000,
        region=41012308,
        radius=0.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010314,
        animation_id=30000,
        animation_id_1=20000,
        region=41012308,
        radius=0.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010318,
        animation_id=30000,
        animation_id_1=20000,
        region=41012318,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41010251,
        animation_id=30000,
        animation_id_1=20000,
        region=41012251,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005445(
        0,
        character=41010252,
        animation_id=30002,
        animation_id_1=20002,
        region=41012252,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41011252,
    )
    CommonFunc_90005261(0, character=41010253, region=41012253, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005446(
        0,
        character=41010254,
        animation_id=30002,
        animation_id_1=20002,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41011254,
    )
    CommonFunc_90005445(
        0,
        character=41010255,
        animation_id=30004,
        animation_id_1=20004,
        region=41012255,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41011255,
    )
    CommonFunc_90005445(
        0,
        character=41010256,
        animation_id=30004,
        animation_id_1=20004,
        region=41012256,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41011256,
    )
    CommonFunc_90005211(
        0,
        character=41010257,
        animation_id=30000,
        animation_id_1=20000,
        region=41012257,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=41010258, region=41012258, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41010259, region=41012259, radius=2.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005445(
        0,
        character=41010263,
        animation_id=30004,
        animation_id_1=20004,
        region=41012264,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41011263,
    )
    CommonFunc_90005445(
        0,
        character=41010264,
        animation_id=30002,
        animation_id_1=20002,
        region=41012264,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41011264,
    )
    CommonFunc_90005261(0, character=41010267, region=41012267, radius=2.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005261(0, character=41010270, region=41012270, radius=2.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005261(0, character=41010350, region=41012350, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41010351, region=41012351, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41010352, region=41012351, radius=2.0, seconds=0.5, animation_id=-1)
    CommonFunc_90005261(0, character=41010360, region=41012351, radius=2.0, seconds=2.5, animation_id=-1)


@ContinueOnRest(41012580)
def Event_41012580():
    """Event 41012580"""
    RegisterLadder(start_climbing_flag=41010580, stop_climbing_flag=41010581, asset=41011580)


@RestartOnRest(41012550)
def Event_41012550(_, character: Character | int, asset: Asset | int):
    """Event 41012550"""
    if ThisEventSlotFlagEnabled():
        return
    EnableAssetInvulnerability(asset)
    AND_1.Add(SpecialStandbyEndedFlagEnabled(character=character))
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)


@RestartOnRest(41012570)
def Event_41012570(_, character: uint, asset: Asset | int):
    """Event 41012570"""
    if ThisEventSlotFlagEnabled():
        return
    if AssetDestroyed(asset):
        MAIN.Await(CharacterHasSpecialEffect(character, 9624))
    
        ForceAnimation(character, 0)
        EnableAI(character)
        End()
    EnableAssetInvulnerability(asset)
    if UnsignedEqual(left=character, right=0):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9624))
    
    OR_1.Add(SpecialStandbyEndedFlagEnabled(character=character))
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(character, 9624))
    
    MAIN.Await(OR_1)
    
    DisableAssetInvulnerability(asset)


@RestartOnRest(41012800)
def Event_41012800():
    """Event 41012800"""
    if FlagEnabled(41010800):
        return
    
    MAIN.Await(HealthValue(41010800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(41010800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(41010800))
    
    KillBossAndDisplayBanner(character=41010800, banner_type=BannerType.EnemyFelled)
    EnableFlag(41010800)
    EnableFlag(9276)
    if PlayerInOwnWorld():
        EnableFlag(61276)


@RestartOnRest(41012810)
def Event_41012810():
    """Event 41012810"""
    GotoIfFlagDisabled(Label.L0, flag=41010800)
    DisableCharacter(41010800)
    DisableAnimations(41010800)
    Kill(41010800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(41010800)
    AND_2.Add(FlagEnabled(41012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=41012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(41010800)
    SetNetworkUpdateRate(41010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(41010800, name=905040400)


@RestartOnRest(41012811)
def Event_41012811():
    """Event 41012811"""
    if FlagEnabled(41010800):
        return
    AND_1.Add(HealthRatio(41010800) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(41012802)


@RestartOnRest(41012849)
def Event_41012849():
    """Event 41012849"""
    CommonFunc_9005800(
        0,
        flag=41010800,
        entity=41011800,
        region=41012800,
        flag_1=41012805,
        character=41015800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=41010800,
        entity=41011800,
        region=41012800,
        flag_1=41012805,
        flag_2=41012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=41010800, asset=41011800, vfx_id=4, right=0)
    CommonFunc_9005822(
        0,
        flag=41010800,
        bgm_boss_conv_param_id=941000,
        flag_1=41012805,
        flag_2=41012806,
        right=0,
        flag_3=41012802,
        left=0,
        left_1=0,
    )


@RestartOnRest(41012610)
def Event_41012610():
    """Event 41012610"""
    ForceAnimation(41011600, 1000020, skip_transition=True)
    GotoIfFlagEnabled(Label.L9, flag=41012601)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=41012600))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=41012601))
    OR_1.Add(FlagEnabled(41012601))
    
    MAIN.Await(OR_1)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(41012601)
    ForceAnimation(41011601, 1000000, skip_transition=True)
    ForceAnimation(41011600, 1000021, wait_for_completion=True, skip_transition=True)
    ForceAnimation(41011600, 1000012, wait_for_completion=True, skip_transition=True)
    AND_2.Add(AllPlayersOutsideRegion(region=41012600))
    AND_2.Add(AllPlayersOutsideRegion(region=41012601))
    AND_2.Add(AssetBackreadEnabled(asset=41011600))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(41012601))
    
    MAIN.Await(OR_2)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(41012601)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(41012601))
    
    Restart()


@RestartOnRest(41012612)
def Event_41012612():
    """Event 41012612"""
    if FlagDisabled(41010610):
        ForceAnimation(41011602, 2000030, skip_transition=True)
    else:
        ForceAnimation(41011602, 2000020, skip_transition=True)
    GotoIfFlagEnabled(Label.L9, flag=41012602)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=41012602))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=41012603))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=41012610))
    AND_1.Add(FlagDisabled(41010610))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(41012602))
    
    MAIN.Await(OR_1)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(41012602)
    SkipLinesIfFlagEnabled(3, 41010610)
    EnableNetworkFlag(41010610)
    ForceAnimation(41011602, 2000032, wait_for_completion=True, skip_transition=True)
    SkipLinesIfLastConditionResultTrue(9, input_condition=AND_1)
    ForceAnimation(41011603, 2000000, skip_transition=True)
    ForceAnimation(41011602, 2000021, wait_for_completion=True, skip_transition=True)
    ForceAnimation(41011602, 2000012, wait_for_completion=True, skip_transition=True)
    AND_2.Add(AllPlayersOutsideRegion(region=41012602))
    AND_2.Add(AllPlayersOutsideRegion(region=41012603))
    AND_2.Add(AssetBackreadEnabled(asset=41011602))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(41012602))
    
    MAIN.Await(OR_2)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(41012602)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(41012602))
    
    Restart()
