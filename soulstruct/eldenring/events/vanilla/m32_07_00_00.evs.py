"""
Gael Tunnel

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
from .entities.m32_07_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32070000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=32070001, asset=Assets.AEG099_060_9001)
    Event_32072810()
    Event_32072800()
    Event_32072811()
    Event_32072849()
    Event_32072200(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30004,
        animation_id_1=20004,
        character_1=Characters.RadahnSoldier7,
        special_effect=16576,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9008,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32072200(
        1,
        character=Characters.TunnelMiner1,
        animation_id=30000,
        animation_id_1=20000,
        character_1=Characters.RadahnSoldier7,
        special_effect=16572,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9009,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32072200(
        2,
        character=Characters.TunnelMiner2,
        animation_id=30004,
        animation_id_1=20004,
        character_1=Characters.RadahnSoldier7,
        special_effect=16576,
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
    Event_32072200(
        3,
        character=Characters.TunnelMiner3,
        animation_id=30002,
        animation_id_1=20002,
        character_1=Characters.RadahnSoldier7,
        special_effect=16574,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9002,
        asset_1=Assets.AEG099_780_9003,
        asset_2=Assets.AEG099_780_9004,
        asset_3=0,
    )
    Event_32072200(
        4,
        character=Characters.TunnelMiner7,
        animation_id=30002,
        animation_id_1=20002,
        character_1=Characters.RadahnSoldier9,
        special_effect=16574,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9010,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    CommonFunc_90005511(0, flag=32070560, asset=Assets.AEG027_043_0500, obj_act_id=32073560, obj_act_id_1=27043, left=0)
    CommonFunc_90005512(0, flag=32070560, region=32072560, region_1=32072561)
    Event_32072580()
    CommonFunc_90005646(
        0,
        flag=32070800,
        left_flag=32072840,
        cancel_flag__right_flag=32072841,
        asset=Assets.AEG099_065_9000,
        player_start=32072840,
        area_id=32,
        block_id=7,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot,
        flag=3661,
        flag_1=3662,
        flag_2=1043399301,
        flag_3=3661,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.LivingPot, flag=3661, flag_1=3660, flag_2=1043399301, right=3)
    CommonFunc_90005702(0, character=Characters.LivingPot, flag=3663, first_flag=3660, last_flag=3663)
    Event_32073700(0, character=Characters.LivingPot)
    Event_32073701()
    Event_32073702()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32072820()
    CommonFunc_90005250(0, character=Characters.TunnelMiner4, region=32072204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Octopus, region=32072306, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier0, region=32072300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier1, region=32072300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier3, region=32072306, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier4, region=32072306, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier5, region=32072308, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier6, region=32072309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier7, region=32072309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier8, region=32072315, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier9, region=32072316, seconds=0.0, animation_id=-1)


@RestartOnRest(32072580)
def Event_32072580():
    """Event 32072580"""
    RegisterLadder(start_climbing_flag=32070530, stop_climbing_flag=32070531, asset=Assets.AEG027_049_0500)
    RegisterLadder(start_climbing_flag=32070532, stop_climbing_flag=32070533, asset=32071532)


@RestartOnRest(32072200)
def Event_32072200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    character_1: uint,
    special_effect: int,
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
    """Event 32072200"""
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
    AND_12.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    AND_12.Add(CharacterHasSpecialEffect(PLAYER, 10004))
    OR_2.Add(AND_12)
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


@RestartOnRest(32072800)
def Event_32072800():
    """Event 32072800"""
    if FlagEnabled(32070800):
        return
    
    MAIN.Await(HealthValue(Characters.MagmaWyrm) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.MagmaWyrm))
    
    KillBossAndDisplayBanner(character=Characters.MagmaWyrm, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(32070800)
    EnableFlag(9266)
    if PlayerInOwnWorld():
        EnableFlag(61266)


@RestartOnRest(32072810)
def Event_32072810():
    """Event 32072810"""
    GotoIfFlagDisabled(Label.L0, flag=32070800)
    DisableCharacter(Characters.MagmaWyrm)
    DisableAnimations(Characters.MagmaWyrm)
    Kill(Characters.MagmaWyrm)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MagmaWyrm)
    GotoIfFlagEnabled(Label.L1, flag=32070801)
    ForceAnimation(Characters.MagmaWyrm, 30000, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32072801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.MagmaWyrm, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(32070801)
    Wait(0.30000001192092896)
    ForceAnimation(Characters.MagmaWyrm, 20000)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(Characters.MagmaWyrm, 30000, loop=True)
    AND_2.Add(FlagEnabled(32072805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32072800))
    
    MAIN.Await(AND_2)
    
    Wait(0.30000001192092896)
    ForceAnimation(Characters.MagmaWyrm, 20000)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MagmaWyrm)
    SetNetworkUpdateRate(Characters.MagmaWyrm, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MagmaWyrm, name=904910320)


@RestartOnRest(32072811)
def Event_32072811():
    """Event 32072811"""
    if FlagEnabled(32070800):
        return
    AND_1.Add(HealthRatio(Characters.MagmaWyrm) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32072802)


@RestartOnRest(32072820)
def Event_32072820():
    """Event 32072820"""
    if FlagEnabled(32070800):
        return
    if FlagEnabled(32070801):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(32078540):
        return
    DisableFlag(32078540)


@RestartOnRest(32072849)
def Event_32072849():
    """Event 32072849"""
    CommonFunc_9005800(
        0,
        flag=32070800,
        entity=Assets.AEG099_001_9000,
        region=32072800,
        flag_1=32072805,
        character=32075800,
        action_button_id=10000,
        left=32070801,
        region_1=32072801,
    )
    CommonFunc_9005801(
        0,
        flag=32070800,
        entity=Assets.AEG099_001_9000,
        region=32072800,
        flag_1=32072805,
        flag_2=32072806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32070800, asset=Assets.AEG099_001_9000, model_point=7, right=32070801)
    CommonFunc_9005822(
        0,
        flag=32070800,
        bgm_boss_conv_param_id=920900,
        flag_1=32072805,
        flag_2=32072806,
        right=0,
        flag_3=32072802,
        left=0,
        left_1=0,
    )


@RestartOnRest(32073700)
def Event_32073700(_, character: uint):
    """Event 32073700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3666)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3666))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3666))
    
    Restart()


@RestartOnRest(32073701)
def Event_32073701():
    """Event 32073701"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(3666, 3671))
    OR_1.Add(CharacterInsideRegion(character=20000, region=32072700))
    AwaitConditionTrue(OR_1)
    EnableFlag(32009203)
    EnableFlag(3678)
    End()


@RestartOnRest(32073702)
def Event_32073702():
    """Event 32073702"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(3666, 3671))
    AND_1.Add(CharacterInsideRegion(character=20000, region=32072701))
    AND_1.Add(FlagDisabled(1043399305))
    OR_1.Add(AND_1)
    AwaitConditionTrue(OR_1)
    EnableFlag(32009203)
    End()
