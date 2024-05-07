"""
Sellia Crystal Tunnel

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
from .enums.m32_08_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32080000, asset=Assets.AEG099_060_9000)
    Event_32082800()
    Event_32082810()
    Event_32082811()
    Event_32082849()
    Event_32082580()
    CommonFunc_90005520(
        0,
        flag=32080588,
        asset=Assets.AEG027_035_0500,
        start_climbing_flag=32080586,
        stop_climbing_flag=32080587,
    )
    Event_32082498()
    CommonFunc_90005646(
        0,
        flag=32080800,
        left_flag=32082840,
        cancel_flag__right_flag=32082841,
        asset=Assets.AEG099_065_9000,
        player_start=32082840,
        area_id=32,
        block_id=8,
        cc_id=0,
        dd_id=0,
    )
    Event_32082650()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)
    Event_32082200(
        0,
        character=Characters.GlintstoneMiner0,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9000,
        asset_1=Assets.AEG099_780_9001,
        asset_2=Assets.AEG099_780_9002,
        asset_3=0,
    )
    Event_32082200(
        1,
        character=Characters.GlintstoneMiner1,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9003,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32082200(
        2,
        character=Characters.GlintstoneMiner2,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9004,
        asset_1=Assets.AEG099_780_9005,
        asset_2=0,
        asset_3=0,
    )
    Event_32082200(
        3,
        character=Characters.GlintstoneMiner3,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9015,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32082200(
        4,
        character=Characters.GlintstoneMiner4,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9016,
        asset_1=Assets.AEG099_780_9017,
        asset_2=0,
        asset_3=0,
    )
    Event_32082200(
        5,
        character=32080205,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9018,
        asset_1=Assets.AEG099_780_9019,
        asset_2=0,
        asset_3=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32082820()
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.GlintstoneMiner5, region=32082211, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.GlintstoneMiner6, region=32082302, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.GlintstoneMiner7, region=32082217, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.GlintstoneMiner8, region=32082217, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.BigGlintstoneMiner, region=32082250, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.KindredofRot0,
        animation_id=30009,
        animation_id_1=20029,
        region=32082300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.KindredofRot1,
        animation_id=30009,
        animation_id_1=20029,
        region=32082301,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.KindredofRot2,
        animation_id=30009,
        animation_id_1=20029,
        region=32082302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.KindredofRot3,
        animation_id=30009,
        animation_id_1=20029,
        region=32082303,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=32080305, region=32082305, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.KindredofRot4, region=32082306, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.KindredofRot5, region=32082306, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.KindredofRot6, region=32082308, seconds=0.0, animation_id=3008)


@RestartOnRest(32082580)
def Event_32082580():
    """Event 32082580"""
    RegisterLadder(start_climbing_flag=32080580, stop_climbing_flag=32080581, asset=Assets.AEG027_045_0500)
    RegisterLadder(start_climbing_flag=32080582, stop_climbing_flag=32080583, asset=Assets.AEG027_048_0500)
    RegisterLadder(start_climbing_flag=32080584, stop_climbing_flag=32080585, asset=Assets.AEG027_048_0501)


@RestartOnRest(32082498)
def Event_32082498():
    """Event 32082498"""
    GotoIfFlagEnabled(Label.L0, flag=32080588)
    EnableNavmeshType(navmesh_id=32082498, navmesh_type=NavmeshType.Disable)
    
    MAIN.Await(FlagEnabled(32080588))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=32082498, navmesh_type=NavmeshType.Disable)
    End()


@RestartOnRest(32082200)
def Event_32082200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
):
    """Event 32082200"""
    if ThisEventSlotFlagEnabled():
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(32082650)
def Event_32082650():
    """Event 32082650"""
    MAIN.Await(FlagEnabled(32080650))
    
    ForceAnimation(PLAYER, 60131)
    EnableFlag(9080)
    DisableFlag(32080650)


@RestartOnRest(32082800)
def Event_32082800():
    """Event 32082800"""
    if FlagEnabled(32080800):
        return
    
    MAIN.Await(HealthValue(Characters.FallingstarBeast) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.FallingstarBeast))
    
    KillBossAndDisplayBanner(character=Characters.FallingstarBeast, banner_type=BannerType.EnemyFelled)
    EnableFlag(32080800)
    EnableFlag(9267)
    if PlayerInOwnWorld():
        EnableFlag(61267)


@RestartOnRest(32082810)
def Event_32082810():
    """Event 32082810"""
    GotoIfFlagDisabled(Label.L0, flag=32080800)
    DisableCharacter(Characters.FallingstarBeast)
    DisableAnimations(Characters.FallingstarBeast)
    Kill(Characters.FallingstarBeast)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.FallingstarBeast)
    EnableInvincibility(Characters.FallingstarBeast)
    GotoIfFlagEnabled(Label.L1, flag=32080801)
    ForceAnimation(Characters.FallingstarBeast, 30008, loop=True)
    AND_2.Add(FlagEnabled(32082805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32082800))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(32080801)
    ForceAnimation(Characters.FallingstarBeast, 20008)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(Characters.FallingstarBeast, 30008, loop=True)
    AND_2.Add(FlagEnabled(32082805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32082800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.FallingstarBeast, 20008)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.FallingstarBeast)
    DisableInvincibility(Characters.FallingstarBeast)
    SetNetworkUpdateRate(Characters.FallingstarBeast, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.FallingstarBeast, name=904680320)


@RestartOnRest(32082811)
def Event_32082811():
    """Event 32082811"""
    if FlagEnabled(32080800):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.FallingstarBeast, 16495))
    
    MAIN.Await(AND_1)
    
    EnableFlag(32082802)


@RestartOnRest(32082820)
def Event_32082820():
    """Event 32082820"""
    if FlagEnabled(32080800):
        return
    if FlagEnabled(32080801):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(32088590):
        return
    DisableFlag(32088590)


@RestartOnRest(32082849)
def Event_32082849():
    """Event 32082849"""
    CommonFunc_9005800(
        0,
        flag=32080800,
        entity=Assets.AEG099_003_9000,
        region=32082800,
        flag_1=32082805,
        character=32085800,
        action_button_id=10000,
        left=32080801,
        region_1=32082801,
    )
    CommonFunc_9005801(
        0,
        flag=32080800,
        entity=Assets.AEG099_003_9000,
        region=32082800,
        flag_1=32082805,
        flag_2=32082806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32080800, asset=Assets.AEG099_003_9000, dummy_id=7, right=32080801)
    CommonFunc_9005822(
        0,
        flag=32080800,
        bgm_boss_conv_param_id=920800,
        flag_1=32082805,
        flag_2=32082806,
        right=0,
        flag_3=32082802,
        left=0,
        left_1=0,
    )
