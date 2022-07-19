"""
West Limgrave (NE) (NE)

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
from .entities.m60_43_39_00_entities import *
from .entities.m30_11_00_00_entities import Assets as m30_11_Assets


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043390000, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=1043398540)
    CommonFunc_90005460(0, character=Characters.GiantOctopus0)
    CommonFunc_90005461(0, character=Characters.GiantOctopus0)
    CommonFunc_90005462(0, character=Characters.GiantOctopus0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus1)
    CommonFunc_90005461(0, character=Characters.GiantOctopus1)
    CommonFunc_90005462(0, character=Characters.GiantOctopus1)
    CommonFunc_90005460(0, character=Characters.GiantOctopus2)
    CommonFunc_90005461(0, character=Characters.GiantOctopus2)
    CommonFunc_90005462(0, character=Characters.GiantOctopus2)
    CommonFunc_90005460(0, character=Characters.GiantOctopus3)
    CommonFunc_90005461(0, character=Characters.GiantOctopus3)
    CommonFunc_90005462(0, character=Characters.GiantOctopus3)
    CommonFunc_90005460(0, character=Characters.GiantOctopus4)
    CommonFunc_90005461(0, character=Characters.GiantOctopus4)
    CommonFunc_90005462(0, character=Characters.GiantOctopus4)
    Event_1043392600(0, attacked_entity=Assets.AEG099_280_9000, region=1043392610)
    Event_1043392600(1, attacked_entity=Assets.AEG099_280_9001, region=1043392611)
    CommonFunc_90005683(0, flag=62104, asset=Assets.AEG099_055_1000, vfx_id=210, flag_1=78192, flag_2=78192)
    Event_1043393700(0, character=1043390700, character_1=1043390701, character_2=1043390702, asset=1043396700)
    Event_1043393703(0, character=1043390700)
    Event_1043393705(0, character=1043390700)
    Event_1043393702(0, character=1043390700)
    CommonFunc_90005700(
        0,
        character=1043390700,
        flag=4741,
        flag_1=4742,
        flag_2=1043399249,
        value=0.6499999761581421,
        first_flag=4740,
        last_flag=4743,
        right=0,
    )
    CommonFunc_90005701(0, attacked_entity=1043390700, flag=4741, flag_1=4742, flag_2=1043399249, right=3)
    CommonFunc_90005702(0, character=1043390700, flag=4743, first_flag=4740, last_flag=4743)
    Event_1043393704()
    CommonFunc_90005700(
        0,
        character=1043390701,
        flag=1043399246,
        flag_1=1043399246,
        flag_2=1043399247,
        value=0.6499999761581421,
        first_flag=1043399246,
        last_flag=1043399246,
        right=0,
    )
    CommonFunc_90005701(0, attacked_entity=1043390701, flag=4741, flag_1=4742, flag_2=1043399249, right=3)
    RunCommonEvent(1043393706, slot=0, args=(1043390700, 1043390701), arg_types="II")
    Event_1043393707(
        0,
        character=1043390700,
        first_flag=4740,
        flag=4741,
        flag_1=4742,
        last_flag=4743,
        character_1=1043390701,
        flag_2=1043399246,
    )
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930025, left=0)
    CommonFunc_90005703(0, 1043390710, 3661, 3662, 1043399301, 1043399314, 3660, 3663, -1)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.LivingPot,
        flag=1043399314,
        flag_1=3660,
        flag_2=1043399301,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.LivingPot, flag=3663, first_flag=3660, last_flag=3663)
    Event_1043393720(0, character=Characters.LivingPot)
    Event_1043393721()
    Event_1043393722()
    Event_1043390724()
    Event_1043393750(0, character=1043390705)
    Event_1043392390()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1043392200()
    CommonFunc_90005261(0, character=1043390220, region=1043392220, radius=3.0, seconds=0.0, animation_id=3010)
    CommonFunc_90005251(0, 1043390220, 5.0, 0.0, -1)


@RestartOnRest(1043392600)
def Event_1043392600(_, attacked_entity: uint, region: uint):
    """Event 1043392600"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(1043392200)
def Event_1043392200():
    """Event 1043392200"""
    DropMandatoryTreasure(1043395200)


@RestartOnRest(1043392390)
def Event_1043392390():
    """Event 1043392390"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1042372800)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1043392390))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=1043392391))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=1043392392))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=1043392393))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=1043392394))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()


@RestartOnRest(1043392670)
def Event_1043392670(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043392670"""
    if Multiplayer():
        return
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(PlayerDoesNotHaveGood(9109))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_NE_NE))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100690))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag_1, bit_count=1)


@RestartOnRest(1043392671)
def Event_1043392671(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043392671"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_NE_NE))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9120, flag=flag_1, bit_count=1)


@RestartOnRest(1043393700)
def Event_1043393700(_, character: uint, character_1: uint, character_2: uint, asset: uint):
    """Event 1043393700"""
    WaitFrames(frames=1)
    DisableFlag(1043399200)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_10.Add(FlagEnabled(4740))
    AND_10.Add(FlagEnabled(1041369248))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1041369248)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    OR_1.Add(FlagEnabled(4745))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4747))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1043399221))
    GotoIfConditionFalse(Label.L20, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L1, flag=4740)
    GotoIfFlagEnabled(Label.L2, flag=4741)
    GotoIfFlagEnabled(Label.L4, flag=4743)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    if FlagEnabled(4980):
        ForceAnimation(character, 30001)
    SkipLinesIfFlagRangeAllDisabled(1, (4982, 4983))
    ForceAnimation(character, 30002)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    if FlagEnabled(4980):
        ForceAnimation(character, 30001)
    SkipLinesIfFlagRangeAllDisabled(2, (4982, 4983))
    ForceAnimation(character, 30002)
    DisableAI(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L20, flag=1043399222)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(1043399200))
    
    Restart()


@NeverRestart(1043393702)
def Event_1043393702(_, character: uint):
    """Event 1043393702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4743):
        return
    if FlagDisabled(1043399221):
        return
    
    MAIN.Await(CharacterDead(character))
    
    EnableNetworkFlag(1043399222)
    End()


@NeverRestart(1043393703)
def Event_1043393703(_, character: uint):
    """Event 1043393703"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(4745))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4747))
    OR_2.Add(FlagEnabled(4740))
    OR_2.Add(FlagEnabled(4741))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    if not AND_1:
        return
    GotoIfFlagEnabled(Label.L0, flag=4980)
    GotoIfFlagRangeAnyEnabled(Label.L10, flag_range=(4982, 4983))

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(CharacterHasSpecialEffect(character, 9601))
    OR_5.Add(CharacterHasSpecialEffect(character, 9603))
    
    MAIN.Await(OR_5)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=9601)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=9603)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_6.Add(EntityWithinDistance(entity=20000, other_entity=character, radius=4.0))
    OR_6.Add(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    MAIN.Await(OR_6)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_7.Add(EntityBeyondDistance(entity=20000, other_entity=character, radius=6.0))
    OR_7.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_7)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9603)
    ForceAnimation(character, 20010)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_10.Add(CharacterHasSpecialEffect(character, 9603))
    
    MAIN.Await(OR_10)
    
    GotoIfCharacterHasSpecialEffect(Label.L11, character=character, special_effect=9603)

    # --- Label 11 --- #
    DefineLabel(11)
    OR_11.Add(EntityBeyondDistance(entity=20000, other_entity=character, radius=6.0))
    OR_11.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_11)
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=9603)
    ForceAnimation(character, 20011)
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1043393704)
def Event_1043393704():
    """Event 1043393704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043399229):
        return
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=1043390700, radius=7.5))
    
    EnableNetworkFlag(1043399229)
    End()


@RestartOnRest(1043393705)
def Event_1043393705(_, character: uint):
    """Event 1043393705"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(4745))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4747))
    OR_2.Add(FlagEnabled(4740))
    OR_2.Add(FlagEnabled(4741))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    if not AND_1:
        return
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=9602)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9602))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(character)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9602))
    
    Restart()


@RestartOnRest(1043393706)
def Event_1043393706(_, character: uint, attacked_entity: uint):
    """Event 1043393706"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=40000))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1041362709))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1041362708)
    if FlagEnabled(4741):
        return
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9602)
    ForceAnimation(character, 20006)


@NeverRestart(1043393707)
def Event_1043393707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1043393707"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(first_flag):
        return
    DisableNetworkFlag(flag_2)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    AND_1.Add(HealthValue(character) < 1)
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_3.Add(FlagEnabled(flag_2))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=20000))
    AND_3.Add(HealthValue(character_1) < 1)
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    OR_5.Add(OR_2)
    OR_5.Add(OR_4)
    
    MAIN.Await(OR_5)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1043343700)
def Event_1043343700(_, character: uint):
    """Event 1043343700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023)
    End()


@RestartOnRest(1043343701)
def Event_1043343701(_, character: uint):
    """Event 1043343701"""
    GotoIfFlagEnabled(Label.L1, flag=30110800)
    
    MAIN.Await(FlagEnabled(30110800))

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1043343702)
def Event_1043343702():
    """Event 1043343702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043399356):
        return
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=m30_11_Assets.AEG099_060_9000, radius=15.0))
    AND_1.Add(FlagEnabled(1043399355))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1043399356)
    End()


@RestartOnRest(1043393720)
def Event_1043393720(_, character: uint):
    """Event 1043393720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3665)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3665))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    if FlagEnabled(1043399311):
        Move(character, destination=1043392700, destination_type=CoordEntityType.Region, short_move=True)
        GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    if FlagDisabled(1043399311):
        ForceAnimation(character, 930018)
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
    
    MAIN.Await(FlagDisabled(3665))
    
    Restart()


@RestartOnRest(1043393721)
def Event_1043393721():
    """Event 1043393721"""
    WaitFrames(frames=1)
    if FlagDisabled(3660):
        return
    EnableImmortality(Characters.LivingPot)
    DisableHealthBar(Characters.LivingPot)
    AwaitFlagEnabled(flag=1043399311)
    DisableImmortality(Characters.LivingPot)
    EnableHealthBar(Characters.LivingPot)
    End()


@RestartOnRest(1043393722)
def Event_1043393722():
    """Event 1043393722"""
    if FlagDisabled(3665):
        return
    DisableNetworkFlag(1043392712)
    DisableNetworkFlag(1043392713)
    AND_1.Add(FlagEnabled(3665))
    AND_1.Add(FlagDisabled(1043399305))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.LivingPot, radius=30.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1043392712)
    Wait(20.0)
    Restart()


@RestartOnRest(1043390724)
def Event_1043390724():
    """Event 1043390724"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043399311):
        return
    EnableFlag(1043399314)
    
    MAIN.Await(FlagEnabled(1043399311))
    
    DisableFlag(1043399314)
    End()


@RestartOnRest(1043393750)
def Event_1043393750(_, character: uint):
    """Event 1043393750"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)
