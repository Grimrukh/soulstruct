"""
Dragonbarrow Cave

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
from .enums.m31_10_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31100000, asset=Assets.AEG099_060_9000)
    Event_31102800()
    Event_31102801()
    Event_31102802()
    Event_31102810()
    Event_31102811()
    Event_31102815()
    Event_31102849()
    Event_31102860()
    Event_31102830()
    CommonFunc_90005646(
        0,
        flag=31100800,
        left_flag=31102840,
        cancel_flag__right_flag=31102841,
        asset=Assets.AEG099_065_9000,
        player_start=31102840,
        area_id=31,
        block_id=10,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_31102255(0, character=Characters.Wolf2, patrol_information_id=31103252)
    Event_31102255(1, character=Characters.Wolf3, patrol_information_id=31103253)
    CommonFunc_90005261(
        0,
        character=Characters.WolfPackLeader,
        region=31102270,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Runebear, region=31102350, radius=2.0, seconds=0.0, animation_id=0)
    Event_31102360()
    CommonFunc_90005261(0, character=Characters.Deer0, region=31102201, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Deer1, region=31102201, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Deer2, region=31102205, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Springhare0, region=31102236, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Springhare1, region=31102236, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Springhare2, region=31102238, radius=2.0, seconds=0.0, animation_id=0)
    Event_31102200(1, character=Characters.Springhare2)


@RestartOnRest(31102200)
def Event_31102200(_, character: uint):
    """Event 31102200"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=2.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31102250)
def Event_31102250(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31102250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31102255)
def Event_31102255(_, character: uint, patrol_information_id: uint):
    """Event 31102255"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31102252))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown6))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()
    ClearTargetList(character)
    WaitFrames(frames=10)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@ContinueOnRest(31102360)
def Event_31102360():
    """Event 31102360"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31102365))
    OR_15.Add(HasAIStatus(Characters.Runebear, ai_status=AIStatusType.Battle))
    OR_15.Add(HasAIStatus(Characters.Runebear, ai_status=AIStatusType.Unknown5))
    
    MAIN.Await(OR_15)
    
    MAIN.Await(AND_1)
    
    SetNest(31102350, region=31102361)


@RestartOnRest(31102800)
def Event_31102800():
    """Event 31102800"""
    if FlagEnabled(31100800):
        return
    AND_1.Add(CharacterDead(Characters.BeastmanofFarumAzula0))
    AND_1.Add(CharacterDead(Characters.BeastmanofFarumAzula1))
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    KillBossAndDisplayBanner(character=Characters.BeastmanofFarumAzula0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31100800)
    EnableFlag(9244)
    if PlayerInOwnWorld():
        EnableFlag(61244)


@RestartOnRest(31102801)
def Event_31102801():
    """Event 31102801"""
    if FlagEnabled(31100800):
        return
    
    MAIN.Await(HealthValue(Characters.BeastmanofFarumAzula0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BeastmanofFarumAzula0, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31102802)
def Event_31102802():
    """Event 31102802"""
    if FlagEnabled(31100800):
        return
    
    MAIN.Await(HealthValue(Characters.BeastmanofFarumAzula1) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BeastmanofFarumAzula1, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31102830)
def Event_31102830():
    """Event 31102830"""
    if FlagEnabled(31100800):
        return
    
    MAIN.Await(HealthRatio(Characters.BeastmanofFarumAzula0) <= 0.8500000238418579)
    
    ChangePatrolBehavior(Characters.BeastmanofFarumAzula1, patrol_information_id=31103830)
    RemoveSpecialEffect(Characters.BeastmanofFarumAzula1, 8085)
    AddSpecialEffect(Characters.BeastmanofFarumAzula1, 8090)
    SetAIParamID(0, ai_param_id=0)


@RestartOnRest(31102810)
def Event_31102810():
    """Event 31102810"""
    GotoIfFlagDisabled(Label.L0, flag=31100800)
    DisableCharacter(Characters.BeastmanofFarumAzula0)
    DisableCharacter(Characters.BeastmanofFarumAzula1)
    DisableAnimations(Characters.BeastmanofFarumAzula0)
    DisableAnimations(Characters.BeastmanofFarumAzula1)
    Kill(Characters.BeastmanofFarumAzula0)
    Kill(Characters.BeastmanofFarumAzula1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=31100801)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.BeastmanofFarumAzula0, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.BeastmanofFarumAzula1, attacker=PLAYER))
    OR_1.Add(HasAIStatus(Characters.BeastmanofFarumAzula0, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(Characters.BeastmanofFarumAzula1, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31102805))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(31100801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.BeastmanofFarumAzula0, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.BeastmanofFarumAzula1, attacker=PLAYER))
    OR_2.Add(HasAIStatus(Characters.BeastmanofFarumAzula0, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.BeastmanofFarumAzula1, ai_status=AIStatusType.Battle))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31102805))
    AND_2.Add(FlagEnabled(31102805))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.BeastmanofFarumAzula0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.BeastmanofFarumAzula1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BeastmanofFarumAzula0, name=903970311)
    EnableBossHealthBar(Characters.BeastmanofFarumAzula1, name=903970312, bar_slot=1)


@RestartOnRest(31102811)
def Event_31102811():
    """Event 31102811"""
    if FlagEnabled(31100800):
        return
    OR_15.Add(CharacterDead(Characters.BeastmanofFarumAzula0))
    OR_15.Add(CharacterDead(Characters.BeastmanofFarumAzula1))
    
    MAIN.Await(OR_15)
    
    EnableFlag(31102842)


@RestartOnRest(31102815)
def Event_31102815():
    """Event 31102815"""
    GotoIfFlagEnabled(Label.L10, flag=31100800)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=31100801, right=0)
    GotoIfFlagEnabled(Label.L0, flag=31100801)
    OR_1.Add(FlagState(FlagSetting.On, FlagType.RelativeToThisEventSlot, 31102810))
    OR_1.Add(FlagEnabled(31100801))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(31100800))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(31100800):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(31100800))
    AND_3.Add(ActionButtonParamActivated(action_button_id=10000, entity=Assets.AEG099_001_9000))
    OR_3.Add(FlagEnabled(31100800))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(31100800):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4250):
        RotateToFaceEntity(PLAYER, 31102800, animation=60060, wait_for_completion=True)
    else:
        RotateToFaceEntity(PLAYER, 31102800, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=31102805)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=31102800))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(31100800))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(31100800))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(31100800):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagDisabled(31100801):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(31105800, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(31105800)
    EnableNetworkFlag(31102805)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(31100800))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=Assets.AEG099_001_9000))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, 31102800, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31102860)
def Event_31102860():
    """Event 31102860"""
    if FlagEnabled(31100800):
        return
    AND_1.Add(FlagEnabled(31102805))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.BeastmanofFarumAzula0, attacker=PLAYER))
    OR_1.Add(HasAIStatus(Characters.BeastmanofFarumAzula0, ai_status=AIStatusType.Battle))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula0, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula0, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula0, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula0, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula0, state_info=260))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.BeastmanofFarumAzula1, attacker=PLAYER))
    OR_1.Add(HasAIStatus(Characters.BeastmanofFarumAzula1, ai_status=AIStatusType.Battle))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula1, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula1, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula1, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula1, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.BeastmanofFarumAzula1, state_info=260))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31102805))
    AND_1.Add(PlayerInOwnWorld())
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(31102865)
    NotifyBossBattleStart()


@RestartOnRest(31102849)
def Event_31102849():
    """Event 31102849"""
    CommonFunc_9005801(
        0,
        flag=31100800,
        entity=Assets.AEG099_001_9000,
        region=31102800,
        flag_1=31102865,
        flag_2=31102806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31100800, asset=Assets.AEG099_001_9000, dummy_id=3, right=31100801)
    CommonFunc_9005822(
        0,
        flag=31100800,
        bgm_boss_conv_param_id=931000,
        flag_1=31102805,
        flag_2=31102806,
        right=31102810,
        flag_3=31102842,
        left=0,
        left_1=0,
    )
