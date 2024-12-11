"""
Land of Shadow 12-10 NW NE

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
    RegisterGrace(grace_flag=2049430000, asset=2049431950)
    RegisterGrace(grace_flag=2049430001, asset=2049431951)
    RegisterGrace(grace_flag=2049430002, asset=2049431952)
    CommonFunc_90005860(0, flag=2049430800, left=0, character=2049430800, left_1=1, item_lot=30945, seconds=0.0)
    Event_2049432314()
    Event_2049430830(
        0,
        attacker__character=2049430800,
        name=905860603,
        bgm_boss_conv_param_id=920300,
        radius=60.0,
        radius_1=105.0,
        flag=2049432822,
        character=2049435100,
    )
    Event_2049432300(0, attacker__character=2049430810, region=2049432300)
    Event_2049432300(1, attacker__character=2049430811, region=2049432300)
    Event_2049432300(2, attacker__character=2049430812, region=2049432300)
    Event_2049432300(3, attacker__character=2049430813, region=2049432300)
    Event_2049432300(4, attacker__character=2049440810, region=2049432300)
    Event_2049432300(5, attacker__character=2049440811, region=2049432300)
    Event_2049432300(6, attacker__character=2049440812, region=2049432300)
    Event_2049432300(7, attacker__character=2049440813, region=2049432300)
    Event_2049432300(8, attacker__character=2049440814, region=2049432300)
    Event_2049432300(9, attacker__character=2049440815, region=2049432300)
    Event_2049432300(10, attacker__character=2049440816, region=2049432300)
    Event_2049432300(11, attacker__character=2049440817, region=2049432300)
    Event_2049432300(12, attacker__character=2049440818, region=2049432300)
    Event_2049432300(13, attacker__character=2049430800, region=2049432300)
    CommonFunc_90005870(0, character=2049430850, name=905840500, npc_threat_level=12)
    CommonFunc_90005860(0, flag=2049430850, left=0, character=2049430850, left_1=0, item_lot=30965, seconds=0.0)
    CommonFunc_90005250(0, character=2049430850, region=2049432850, seconds=0.5, animation_id=0)
    CommonFunc_90005872(0, character=2049430850, npc_threat_level=12, right=0)
    Event_2049432322(0, character=2049430322, region=2049432322, radius=1.5, seconds=0.0, animation_id=3008)
    CommonFunc_90005250(0, character=2049430320, region=2049432320, seconds=0.0, animation_id=0)
    Event_2049432330(
        0,
        character=2049430331,
        animation_id=30000,
        animation_id_1=20010,
        character_1=2049430330,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005250(0, character=2049430200, region=2049432200, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=2049430209, region=2049432209, seconds=0.0, animation_id=3026)
    CommonFunc_90005250(0, character=2049430201, region=2049432201, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2049430202, region=2049432201, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2049430203, region=2049432203, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2049430204, region=2049432212, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=2049430205, region=2049432212, seconds=1.0, animation_id=3001)
    CommonFunc_90005250(0, character=2049430211, region=2049432212, seconds=0.0, animation_id=3010)
    CommonFunc_90005250(0, character=2049430212, region=2049432212, seconds=0.0, animation_id=3020)
    Event_2049462580()
    Event_2049432690()
    CommonFunc_900005610(0, asset=2049431201, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2049431200, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(2049432690)
def Event_2049432690():
    """Event 2049432690"""
    if FlagEnabled(4925):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=2049432690))
    
    EnableFlag(4925)


@RestartOnRest(2049432300)
def Event_2049432300(_, attacker__character: uint, region: Region | int):
    """Event 2049432300"""
    if FlagEnabled(2049430800):
        DisableCharacter(attacker__character)
        DisableAnimations(attacker__character)
        Kill(attacker__character)
        End()
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Forced)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5662)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=30.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=30.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(attacker__character))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Forced)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5662)


@RestartOnRest(2049432314)
def Event_2049432314():
    """Event 2049432314"""
    AND_1.Add(CharacterDead(2049430800))
    if AND_1:
        return
    if PlayerNotInOwnWorld():
        return
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2049430800, radius=40.0))
    AND_2.Add(HealthRatio(2049430800) <= 0.8500000238418579)
    
    MAIN.Await(AND_2)
    
    SetCharacterEventTarget(2049430800, entity=2049430830)
    AddSpecialEffect(2049430800, 20011655)


@ContinueOnRest(2049430830)
def Event_2049430830(
    _,
    attacker__character: uint,
    name: NPCName | int,
    bgm_boss_conv_param_id: int,
    radius: float,
    radius_1: float,
    flag: Flag | int,
    character: Character | int,
):
    """Event 2049430830"""
    DisableNetworkSync()
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5662)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    if OR_1:
        return
    AND_2.Add(HasAIStatus(attacker__character, ai_status=AIStatusType.Battle))
    AND_2.Add(FlagDisabled(9000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=radius))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=radius))
    AND_2.Add(OR_2)
    OR_3.Add(AND_2)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)
    
    RemoveSpecialEffect(character, 4800)
    RemoveSpecialEffect(character, 5662)
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    EnableFlag(9290)
    EnableNetworkFlag(flag)
    Wait(1.0)
    EnableBossHealthBar(attacker__character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(attacker__character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_3.Add(HasAIStatus(attacker__character, ai_status=AIStatusType.Battle))
    OR_2.Add(not AND_3)
    OR_4.Add(CharacterDead(attacker__character))
    OR_4.Add(FlagEnabled(9000))
    OR_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=radius_1))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.Invader))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.Invader3))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.Invader2))
    AND_11.Add(not OR_11)
    AND_11.Add(EntityWithinDistance(entity=CLIENT_PLAYER_1, other_entity=attacker__character, radius=radius_1))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.BlackPhantom))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader3))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader2))
    AND_12.Add(not OR_12)
    AND_12.Add(EntityWithinDistance(entity=CLIENT_PLAYER_2, other_entity=attacker__character, radius=radius_1))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.BlackPhantom))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader3))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader2))
    AND_13.Add(not OR_13)
    AND_13.Add(EntityWithinDistance(entity=CLIENT_PLAYER_3, other_entity=attacker__character, radius=radius_1))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.BlackPhantom))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader3))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader2))
    AND_14.Add(not OR_14)
    AND_14.Add(EntityWithinDistance(entity=CLIENT_PLAYER_4, other_entity=attacker__character, radius=radius_1))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader2))
    AND_15.Add(not OR_15)
    AND_15.Add(EntityWithinDistance(entity=CLIENT_PLAYER_4, other_entity=attacker__character, radius=radius_1))
    OR_5.Add(AND_11)
    OR_5.Add(AND_12)
    OR_5.Add(AND_13)
    OR_5.Add(AND_14)
    OR_5.Add(AND_15)
    OR_5.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=radius_1))
    OR_4.Add(not OR_5)
    OR_4.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_4)
    
    AddSpecialEffect(character, 4800)
    AddSpecialEffect(character, 5662)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
    DisableNetworkFlag(flag)
    OR_10.Add(CharacterDead(attacker__character))
    SkipLinesIfConditionFalse(3, OR_10)
    SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(attacker__character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    End()
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(attacker__character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(
            attacker__character,
            is_fixed=False,
            update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames,
        )
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    EnableFlag(9291)
    EnableNetworkFlag(flag)
    Wait(1.0)
    EnableBossHealthBar(attacker__character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(attacker__character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_3.Add(HasAIStatus(attacker__character, ai_status=AIStatusType.Battle))
    OR_2.Add(not AND_3)
    OR_4.Add(CharacterDead(attacker__character))
    OR_4.Add(FlagEnabled(9000))
    OR_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=radius_1))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.Invader))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.Invader3))
    OR_11.Add(CharacterIsType(CLIENT_PLAYER_1, character_type=CharacterType.Invader2))
    AND_11.Add(not OR_11)
    AND_11.Add(EntityWithinDistance(entity=CLIENT_PLAYER_1, other_entity=attacker__character, radius=radius_1))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.BlackPhantom))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader3))
    OR_12.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader2))
    AND_12.Add(not OR_12)
    AND_12.Add(EntityWithinDistance(entity=CLIENT_PLAYER_2, other_entity=attacker__character, radius=radius_1))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.BlackPhantom))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader3))
    OR_13.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader2))
    AND_13.Add(not OR_13)
    AND_13.Add(EntityWithinDistance(entity=CLIENT_PLAYER_3, other_entity=attacker__character, radius=radius_1))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.BlackPhantom))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader3))
    OR_14.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader2))
    AND_14.Add(not OR_14)
    AND_14.Add(EntityWithinDistance(entity=CLIENT_PLAYER_4, other_entity=attacker__character, radius=radius_1))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader2))
    AND_15.Add(not OR_15)
    AND_15.Add(EntityWithinDistance(entity=CLIENT_PLAYER_4, other_entity=attacker__character, radius=radius_1))
    OR_5.Add(AND_11)
    OR_5.Add(AND_12)
    OR_5.Add(AND_13)
    OR_5.Add(AND_14)
    OR_5.Add(AND_15)
    OR_5.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=radius_1))
    OR_4.Add(not OR_5)
    OR_4.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_4)
    
    AddSpecialEffect(character, 4800)
    AddSpecialEffect(character, 5662)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
    DisableNetworkFlag(flag)
    OR_10.Add(CharacterDead(attacker__character))
    SkipLinesIfConditionFalse(3, OR_10)
    SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(attacker__character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    End()
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(attacker__character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(
            attacker__character,
            is_fixed=False,
            update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames,
        )
    DisableFlag(9291)
    Restart()


@RestartOnRest(2049432322)
def Event_2049432322(_, character: uint, region: Region | int, radius: float, seconds: float, animation_id: int):
    """Event 2049432322"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    SkipLinesIfConditionTrue(1, OR_4)
    ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(2049432330)
def Event_2049432330(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    character_1: Character | int,
    seconds: float,
    left: uint,
):
    """Event 2049432330"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(HealthRatio(character_1) <= 0.699999988079071)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2049432331))
    OR_2.Add(AND_1)
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
    SetSpecialStandbyEndedFlag(character=character, state=True)
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


@RestartOnRest(2049432500)
def Event_2049432500():
    """Event 2049432500"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2049432500))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(2049432500):
        return
    EnableFlag(2049432500)
    PlaySoundEffect(2049432500, 990000021, sound_type=SoundType.m_Music)


@ContinueOnRest(2049462580)
def Event_2049462580():
    """Event 2049462580"""
    RegisterLadder(start_climbing_flag=2049430580, stop_climbing_flag=2049430581, asset=2049431580)
    RegisterLadder(start_climbing_flag=2049430582, stop_climbing_flag=2049430583, asset=2049431582)
    RegisterLadder(start_climbing_flag=2049430584, stop_climbing_flag=2049430585, asset=2049431584)
    RegisterLadder(start_climbing_flag=2049430586, stop_climbing_flag=2049430587, asset=2049431586)
    RegisterLadder(start_climbing_flag=2049430588, stop_climbing_flag=2049430589, asset=2049431588)
