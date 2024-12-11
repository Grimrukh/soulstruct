"""
Land of Shadow 12-11 NE NW

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
    CommonFunc_90005250(0, character=2050470800, region=2050472800, seconds=0.0, animation_id=-1)
    Event_2050472810(0, character=2050470800, name=906251600, npc_threat_level=12)
    Event_2050472811(0, character=2050480860, name=906251601, npc_threat_level=12)
    Event_2050472400()
    Event_2050472820(0, flag=2050470800, left=0, character=2050470800, seconds=0.0, item_lot=30935, seconds_1=0.0)
    Event_2050472821(1, flag=2050480860, left=0, character=2050480860, seconds=0.0, item_lot=30950, seconds_1=0.0)
    Event_2050472800()
    CommonFunc_90005250(0, character=2050470309, region=2050472309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2050470310, region=2050472309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2050470311, region=2050472309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2050470312, region=2050472309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2050470313, region=2050472309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2050470314, region=2050472309, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=2050470315,
        animation_id=30016,
        animation_id_1=20016,
        region=2050472315,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2050470316,
        animation_id=30014,
        animation_id_1=20014,
        region=2050472315,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2050470317,
        animation_id=30014,
        animation_id_1=20014,
        region=2050472315,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005271(1, character=2050470351, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(2, character=2050470352, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(3, character=2050470353, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(6, character=2050470356, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(7, character=2050470357, seconds=0.0, animation_id=-1)
    Event_2050472205(
        0,
        character=2050470250,
        region=2050472250,
        region_1=2050472270,
        radius=2.0,
        character_1=2050470251,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=2050470180,
        summon_flag=2050472181,
        dismissal_flag=2050472182,
        character=2050470710,
        sign_type=23,
        region=2050472710,
        region_1=2050472711,
        seconds=0.0,
        right_1=2045429292,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2050470180, flag_1=2050472181, flag_2=2050472182, character=2050470710)
    CommonFunc_90005792(
        0,
        flag=2050470180,
        flag_1=2050472181,
        flag_2=2050472182,
        character=2050470710,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2050470180,
        flag_1=2050472181,
        flag_2=2050472182,
        character=2050470710,
        other_entity=2050472710,
        region=0,
        left=0,
    )
    CommonFunc_90005774(0, flag=2050470180, item_lot=116401, flag_1=400645)
    CommonFunc_90005780(
        0,
        flag=2050470400,
        summon_flag=2050472160,
        dismissal_flag=2050472161,
        character=2050470720,
        sign_type=20,
        region=2050472721,
        right=2051459752,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=2050470400, flag_1=2050472160, flag_2=2050472161, character=2050470720)
    CommonFunc_90005783(
        0,
        flag=2050470400,
        flag_1=2050472160,
        flag_2=2050472161,
        character=2050470720,
        other_entity=2050472720,
        region=2050472400,
        left=0,
    )
    CommonFunc_90005757(
        0,
        character=2050470700,
        character_1=2050470701,
        flag=4385,
        flag_1=4952,
        flag_2=2045422710,
        flag_3=4383,
    )
    CommonFunc_90005759(
        0,
        flag=2045429280,
        flag_1=4385,
        flag_2=4962,
        character=2050470700,
        flag_3=4952,
        flag_4=2045429292,
        first_flag=4950,
        last_flag=4956,
        flag_5=2045429281,
        flag_6=2045429282,
        flag_7=4901,
        seconds=1.0,
        flag_8=2045429342,
        radius=30.0,
    )
    CommonFunc_90005778(0, flag=2050472700, flag_1=4952, flag_2=400752, attacked_entity=2050470700)
    CommonFunc_90005779(0, character=2050470700, flag=4952, animation_id=20016, flag_1=4385, flag_2=4383)
    CommonFunc_90005744(0, entity=2050470700, flag=2050479200, flag_1=2050479200, animation_id=20015)
    CommonFunc_90005766(0, flag=2050472181, character=2050470710, distance=100.0, flag_1=2045429277, flag_2=4962)
    CommonFunc_90005767(
        0,
        flag=2045429280,
        first_flag=4380,
        last_flag=4383,
        character=2050470710,
        flag_1=4901,
        character_1=2050470711,
        flag_2=2045429297,
    )
    CommonFunc_90005777(0, character=2050470711, flag=4962, flag_1=4383, flag_2=2050472181)
    CommonFunc_90005774(0, flag=2045429297, item_lot=116401, flag_1=400645)
    Event_2050470705()


@RestartOnRest(2050472205)
def Event_2050472205(
    _,
    character: uint,
    region: Region | int,
    region_1: Region | int,
    radius: float,
    character_1: uint,
):
    """Event 2050472205"""
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=20011469):
        AddSpecialEffect(character, 20011469)
    DisableGravity(character)
    DisableAnimations(character_1)
    DisableGravity(character_1)
    DisableAI(character_1)
    SetLockOnPoint(character=character_1, lock_on_dummy_id=220, state=False)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_4.Add(OR_2)
    GotoIfConditionFalse(Label.L0, input_condition=OR_4)
    AddSpecialEffect(character_1, 20013351)
    ForceAnimation(character, 3020)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 20011467)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5025):
        ForceAnimation(character, 3000)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(2050472400)
def Event_2050472400():
    """Event 2050472400"""
    if FlagEnabled(2050470400):
        return
    AND_1.Add(FlagEnabled(2050470800))
    AND_1.Add(FlagEnabled(2050480800))
    
    MAIN.Await(AND_1)
    
    EnableFlag(2050470400)


@ContinueOnRest(2050472800)
def Event_2050472800():
    """Event 2050472800"""
    DisableNetworkSync()
    AND_5.Add(HealthRatio(2050470800) <= 0.550000011920929)
    AND_5.Add(CharacterAlive(2050470800))
    OR_1.Add(AND_5)
    AND_6.Add(HealthRatio(2050480860) <= 0.550000011920929)
    AND_6.Add(CharacterAlive(2050480860))
    OR_1.Add(AND_6)
    AND_1.Add(OR_1)
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=12))
    
    MAIN.Await(AND_1)
    
    EnableFieldBattleMusicHeatUp(npc_threat_level=12)
    AND_2.Add(CharacterDead(2050470800))
    AND_2.Add(CharacterDead(2050480860))
    OR_2.Add(AND_2)
    OR_2.Add(FieldBattleMusicDisabled(npc_threat_level=12))
    
    MAIN.Await(OR_2)
    
    DisableFieldBattleMusicHeatUp(npc_threat_level=12)
    Wait(0.30000001192092896)
    Restart()


@ContinueOnRest(2050472810)
def Event_2050472810(_, character: uint, name: NPCName | int, npc_threat_level: uint):
    """Event 2050472810"""
    DisableNetworkSync()
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    AND_1.Add(FlagDisabled(9000))
    AND_1.Add(FlagDisabled(character))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_2.Add(not AND_2)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9290)
    Restart()


@ContinueOnRest(2050472811)
def Event_2050472811(_, character: uint, name: NPCName | int, npc_threat_level: uint):
    """Event 2050472811"""
    DisableNetworkSync()
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    AND_1.Add(FlagDisabled(9000))
    AND_1.Add(FlagDisabled(character))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_2.Add(not AND_2)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9291)
    Restart()


@RestartOnRest(2050472820)
def Event_2050472820(
    _,
    flag: Flag | int,
    left: Flag | int,
    character: uint,
    seconds: float,
    item_lot: int,
    seconds_1: float,
):
    """Event 2050472820"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(character) <= 0)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(character))
    
    AND_14.Add(CharacterDead(2050470800))
    AND_14.Add(CharacterDead(2050480860))
    SkipLinesIfConditionTrue(2, AND_14)
    DisplayBanner(BannerType.EnemyFelled)
    Goto(Label.L7)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)

    # --- Label 7 --- #
    DefineLabel(7)
    AND_15.Add(HasAIStatus(2050480860, ai_status=AIStatusType.Battle))
    AND_15.Add(FieldBattleMusicEnabled(npc_threat_level=12))
    SkipLinesIfConditionFalse(1, AND_15)
    EnableBossHealthBar(2050480860, name=906251601, bar_slot=1)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds_1)
    Wait(seconds)


@RestartOnRest(2050472821)
def Event_2050472821(
    _,
    flag: Flag | int,
    left: Flag | int,
    character: uint,
    seconds: float,
    item_lot: int,
    seconds_1: float,
):
    """Event 2050472821"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(character) <= 0)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(character))
    
    AND_14.Add(CharacterDead(2050470800))
    AND_14.Add(CharacterDead(2050480860))
    SkipLinesIfConditionTrue(2, AND_14)
    DisplayBanner(BannerType.EnemyFelled)
    Goto(Label.L7)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)

    # --- Label 7 --- #
    DefineLabel(7)
    AND_15.Add(HasAIStatus(2050470800, ai_status=AIStatusType.Battle))
    AND_15.Add(FieldBattleMusicEnabled(npc_threat_level=12))
    SkipLinesIfConditionFalse(1, AND_15)
    EnableBossHealthBar(2050470800, name=906251600)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds_1)
    Wait(seconds)


@RestartOnRest(2050470705)
def Event_2050470705():
    """Event 2050470705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(2051459752)
    if FlagEnabled(2050470800):
        return
    AND_1.Add(FlagDisabled(2051459708))
    AND_1.Add(FlagDisabled(2051459719))
    AND_1.Add(FlagDisabled(2051459720))
    if AND_1:
        return
    OR_1.Add(FlagEnabled(25000800))
    if OR_1:
        return
    EnableFlag(2051459752)
    OR_10.Add(FlagEnabled(2050470800))
    OR_10.Add(FlagEnabled(25000800))
    
    MAIN.Await(OR_10)
    
    DisableFlag(2051459752)
