"""
Land of Shadow 13-10 SW SW

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
    RegisterGrace(grace_flag=2052400000, asset=2052401950)
    CommonFunc_90005860(0, flag=2052400800, left=0, character=2052400800, left_1=1, item_lot=30800, seconds=0.0)
    Event_2052400202(
        0,
        attacker__character=2052400800,
        name=905580600,
        bgm_boss_conv_param_id=920300,
        radius=70.0,
        radius_1=120.0,
        character=2052400200,
    )
    Event_2052402812()
    Event_2052402800(0, character=2052400800)
    Event_2052402203(0, character=2052400800)
    Event_2052402203(1, character=2052400200)
    Event_2052402811()
    Event_2052402201(0, character=2052400200)
    Event_2052402200(0, attacker__character=2052405200, region=2052402200)
    Event_2052400700(
        0,
        character=2052400700,
        flag=4260,
        flag_1=4261,
        flag_2=4262,
        flag_3=4263,
        flag_4=4267,
        flag_5=4268,
        flag_6=2052409202,
        distance=200.0,
        flag_7=2052409211,
    )
    Event_2052400702(
        0,
        flag=4267,
        flag_1=4261,
        animation_id=90405,
        attacked_entity=2052400700,
        flag_2=4263,
        radius=7.0,
        seconds=2.0,
    )
    CommonFunc_90005744(0, entity=2052400700, flag=2052409209, flag_1=4268, animation_id=90207)
    Event_2052400701(
        0,
        flag=2052409209,
        flag_1=2052402703,
        flag_2=2052402705,
        seconds=10.0,
        flag_3=4261,
        flag_4=4263,
        flag_5=2052402706,
        flag_6=2052402707,
    )
    CommonFunc_90005703(
        0,
        character=2052400700,
        flag=4261,
        flag_1=4262,
        flag_2=2052409201,
        flag_3=4261,
        first_flag=4260,
        last_flag=4264,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=2052400700, flag=4261, flag_1=4260, flag_2=2052409201, right=3)
    CommonFunc_90005702(0, character=2052400700, flag=4263, first_flag=4260, last_flag=4264)
    CommonFunc_90005750(
        0,
        asset=2052401700,
        action_button_id=4350,
        item_lot=107110,
        first_flag=400712,
        last_flag=400712,
        flag=2052409211,
        vfx_id=6102,
    )
    CommonFunc_90005750(
        0,
        asset=2052401700,
        action_button_id=4350,
        item_lot=107120,
        first_flag=400714,
        last_flag=400714,
        flag=2052409212,
        vfx_id=6102,
    )
    Event_2052400704(0, flag=2052400800, flag_1=4278, flag_2=4265)
    Event_2052400703(0, character=2052400701, flag=4260, flag_1=4261, flag_2=4262, flag_3=4263, flag_4=4268)


@RestartOnRest(2052402200)
def Event_2052402200(_, attacker__character: uint, region: Region | int):
    """Event 2052402200"""
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5651)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(attacker__character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(attacker__character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    RemoveSpecialEffect(attacker__character, 5651)
    RemoveSpecialEffect(attacker__character, 4800)


@RestartOnRest(2052402201)
def Event_2052402201(_, character: uint):
    """Event 2052402201"""
    if FlagEnabled(2052400800):
        DisableCharacter(character)
        DisableAnimations(character)
        Kill(character)
        End()
    DisableHealthBar(character)
    AddSpecialEffect(character, 4403)
    AddSpecialEffect(character, 20012700)
    SetTeamType(character, TeamType.Unknown67)
    Wait(3.0)
    EnableHealthBar(character)
    
    MAIN.Await(CharacterDead(2052400800))
    
    AddSpecialEffect(character, 20012700)


@ContinueOnRest(2052400202)
def Event_2052400202(
    _,
    attacker__character: uint,
    name: NPCName | int,
    bgm_boss_conv_param_id: int,
    radius: float,
    radius_1: float,
    character: Character | int,
):
    """Event 2052400202"""
    DisableNetworkSync()
    AND_2.Add(HasAIStatus(attacker__character, ai_status=AIStatusType.Battle))
    AND_2.Add(FlagDisabled(9000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=radius))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=radius))
    AND_2.Add(OR_2)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    AddSpecialEffect(attacker__character, 20012704)
    RemoveSpecialEffect(character, 4800)
    RemoveSpecialEffect(attacker__character, 4800)
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    EnableFlag(9290)
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
    
    MAIN.Await(OR_4)
    
    AddSpecialEffect(character, 4800)
    AddSpecialEffect(attacker__character, 4800)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
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


@RestartOnRest(2052402800)
def Event_2052402800(_, character: Character | int):
    """Event 2052402800"""
    if FlagEnabled(2052400800):
        return
    AddSpecialEffect(character, 20012700)
    SetTeamType(character, 67)
    
    MAIN.Await(CharacterDead(2052400200))
    
    AddSpecialEffect(character, 20012700)


@RestartOnRest(2052402811)
def Event_2052402811():
    """Event 2052402811"""
    if FlagEnabled(2052400800):
        return
    AddSpecialEffect(2052400800, 20012706)
    Wait(20.100000381469727)
    Restart()


@RestartOnRest(2052402812)
def Event_2052402812():
    """Event 2052402812"""
    SetCharacterEnableDistanceWithUnknown(character=2052400800, enable_distance=300.0, unknown_distance=100.0)
    SetCharacterEnableDistanceWithUnknown(character=2052400200, enable_distance=300.0, unknown_distance=100.0)


@RestartOnRest(2052402203)
def Event_2052402203(_, character: Character | int):
    """Event 2052402203"""
    OR_2.Add(CharacterDead(2052400200))
    OR_2.Add(CharacterDead(2052400800))
    if OR_2:
        return
    AND_1.Add(CharacterOutsideRegion(character=character, region=2052402803))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 20011655))
    
    MAIN.Await(AND_1)
    
    SetCharacterEventTarget(character, entity=2052400803)
    AddSpecialEffect(character, 20011655)
    Restart()


@RestartOnRest(2052400700)
def Event_2052400700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    distance: float,
    flag_7: Flag | int,
):
    """Event 2052400700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DisableFlag(flag_6)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(flag_4))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    if FlagEnabled(flag_4):
        SetCharacterTalkRange(character=character, distance=distance)
        ForceAnimation(character, 90102)
    if FlagEnabled(flag_5):
        SetTeamType(character, TeamType.NoTeam)
        ForceAnimation(character, 90103)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 90102)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 90102)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    if FlagDisabled(flag_7):
        DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(flag_4))
    OR_15.Add(FlagEnabled(flag_5))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(2052400701)
def Event_2052400701(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    seconds: float,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 2052400701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_3):
        return
    if FlagEnabled(flag_4):
        return
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_10.Add(FlagEnabled(flag_1))
    AND_10.Add(FlagDisabled(flag_2))
    
    MAIN.Await(AND_10)
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(flag_5):
        DisableFlag(flag_5)
    OR_11.Add(TimeElapsed(seconds=seconds))
    OR_11.Add(FlagEnabled(flag_3))
    OR_11.Add(FlagEnabled(flag_4))
    OR_11.Add(FlagEnabled(flag_5))
    OR_11.Add(FlagEnabled(flag_6))
    
    MAIN.Await(OR_11)
    
    if FlagEnabled(flag_3):
        return
    if FlagEnabled(flag_4):
        return
    if FlagEnabled(flag_5):
        return RESTART
    if FlagEnabled(flag_6):
        DisableFlag(flag_1)
        DisableFlag(flag_2)
        DisableFlag(flag_6)
        Restart()
    EnableFlag(flag_2)
    DisableFlag(flag_1)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(2052400702)
def Event_2052400702(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    attacked_entity: uint,
    flag_2: Flag | int,
    radius: float,
    seconds: float,
):
    """Event 2052400702"""
    WaitFrames(frames=2)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    AwaitFlagEnabled(flag=flag)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=attacked_entity, radius=radius))
    AND_2.Add(TimeElapsed(seconds=seconds))
    OR_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_10.Add(AND_2)
    AND_1.Add(OR_10)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(attacked_entity, animation_id, loop=True)
    Wait(5.5)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_13)
    
    ForceAnimation(attacked_entity, animation_id, loop=True)
    Wait(5.5)
    Restart()


@RestartOnRest(2052400703)
def Event_2052400703(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """Event 2052400703"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(flag_4))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SetTeamType(character, TeamType.NoTeam)
    ForceAnimation(character, 90103)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(flag_4))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(2052400704)
def Event_2052400704(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2052400704"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_2):
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)


@RestartOnRest(2052400705)
def Event_2052400705(_, flag: Flag | int, item: BaseItemParam | int, flag_1: Flag | int):
    """Event 2052400705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(PlayerHasGood(item))
    
    EnableFlag(flag)


@RestartOnRest(2052400706)
def Event_2052400706(
    _,
    asset: uint,
    action_button_id: int,
    item_lot: int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    vfx_id: int,
    flag_1: Flag | int,
):
    """Event 2052400706"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    if ValueNotEqual(left=vfx_id, right=0):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id)
    else:
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6101)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_2)
    DeleteAssetVFX(asset)
    AwardItemLot(item_lot, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()
