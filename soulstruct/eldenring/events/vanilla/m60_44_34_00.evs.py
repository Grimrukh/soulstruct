"""
East Weeping Peninsula (NW) (SW)

linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_44_34_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044340000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76161,
        flag_1=76157,
        asset=Assets.AEG099_090_9000,
        source_flag=77110,
        value=1,
        flag_2=78110,
        flag_3=78111,
        flag_4=78112,
        flag_5=78113,
        flag_6=78114,
        flag_7=78115,
        flag_8=78116,
        flag_9=78117,
        flag_10=78118,
        flag_11=78119,
    )
    CommonFunc_90005637(0, flag=31018600, character=Characters.WanderingNoble, region=1044341620)
    CommonFunc_90005636(
        0,
        flag=31018600,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect=4470,
        destination=1044342620,
        region=1044342621,
        flag_1=1044342620,
        patrol_information_id=1044343620,
        right=-1,
    )
    Event_1044342502()
    Event_1044342200()
    Event_1044340650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )
    Event_1044342300(0, character=Characters.DemiHuman4, asset=1044341300, region=1044342300)
    Event_1044342300(1, character=Characters.DemiHuman5, asset=1044341302, region=1044342301)
    Event_1044342300(2, character=Characters.DemiHuman6, asset=1044341301, region=1044342301)
    Event_1044342203(0, character=Characters.GodrickFootSoldier1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.GodrickFootSoldier1, region=1044342280, seconds=0.0, animation_id=-1)
    Event_1044342280()
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten0,
        region=1044342270,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten1,
        region=1044342270,
        radius=5.0,
        seconds=1.5,
        animation_id=-1,
    )
    Event_1044342230(0, character=1044340230)
    Event_1044342230(1, character=1044340231)
    Event_1044342230(2, character=1044340232)
    Event_1044342230(3, character=1044340240)
    CommonFunc_90005251(0, character=Characters.GodrickFootSoldier2, radius=8.0, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.GodrickFootSoldier0, region=1044342600, seconds=0.0, animation_id=-1)
    CommonFunc_90005630(0, far_view_id=61443400, asset=1044341500, dummy_id=127)
    Event_1044343700(0, character=1044340700, character_1=1044340701, character_2=1044340702, asset=1044346700)
    Event_1044343702(0, character=1044340700)
    Event_1044343704(0, character=1044340700)
    Event_1044343701(0, character=1044340700)
    CommonFunc_90005700(
        0,
        character=1044340700,
        flag=4741,
        flag_1=4742,
        flag_2=1044349249,
        value=0.6499999761581421,
        first_flag=4740,
        last_flag=4743,
        right=0,
    )
    CommonFunc_90005701(0, attacked_entity=1044340700, flag=4741, flag_1=4742, flag_2=1044349249, right=3)
    CommonFunc_90005702(0, character=1044340700, flag=4743, first_flag=4740, last_flag=4743)
    Event_1044343703()
    CommonFunc_90005700(
        0,
        character=1044340701,
        flag=1044349246,
        flag_1=1044349246,
        flag_2=1044349247,
        value=0.6499999761581421,
        first_flag=1044349246,
        last_flag=1044349246,
        right=0,
    )
    CommonFunc_90005701(0, attacked_entity=1044340701, flag=4741, flag_1=4742, flag_2=1044349249, right=3)
    RunCommonEvent(1044343705, slot=0, args=(1044340700, 1044340701), arg_types="II")
    Event_1044343706(
        0,
        character=1044340700,
        first_flag=4740,
        flag=4741,
        flag_1=4742,
        last_flag=4743,
        character_1=1044340701,
        flag_2=1044349246,
    )
    Event_1044343707(0, flag=4740, flag_1=1041369201, flag_2=1044349226)
    CommonFunc_90005704(0, attacked_entity=Characters.Blaidd, flag=3601, flag_1=3600, flag_2=1044349251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Blaidd,
        flag=3601,
        flag_1=3602,
        flag_2=1044349251,
        flag_3=3603,
        first_flag=3600,
        last_flag=3603,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Blaidd, flag=3603, first_flag=3600, last_flag=3604)
    Event_1044343710(0, character=Characters.Blaidd)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Blaidd)


@RestartOnRest(1044342502)
def Event_1044342502():
    """Event 1044342502"""
    RegisterLadder(start_climbing_flag=44340580, stop_climbing_flag=44340851, asset=Assets.AEG110_012_1000)
    RegisterLadder(start_climbing_flag=44340582, stop_climbing_flag=44340853, asset=Assets.AEG110_012_1001)
    RegisterLadder(start_climbing_flag=44340584, stop_climbing_flag=44340855, asset=Assets.AEG110_012_1002)


@RestartOnRest(1044342200)
def Event_1044342200():
    """Event 1044342200"""
    DisableAsset(1044346200)


@RestartOnRest(1044342203)
def Event_1044342203(_, character: uint):
    """Event 1044342203"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AddSpecialEffect(character, 8089)
    SetTeamType(character, TeamType.CoopNPC)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1044342281))
    
    MAIN.Await(AND_2)
    
    SetTeamType(character, TeamType.Enemy2)
    End()


@RestartOnRest(1044342230)
def Event_1044342230(_, character: uint):
    """Event 1044342230"""
    Kill(character)
    End()


@RestartOnRest(1044342280)
def Event_1044342280():
    """Event 1044342280"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterDead(1044345280))
    
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=Characters.DemiHuman0, unk_8_12=2)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=Characters.DemiHuman1, unk_8_12=2)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=Characters.DemiHuman2, unk_8_12=2)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=Characters.DemiHuman3, unk_8_12=2)
    End()


@RestartOnRest(1044342300)
def Event_1044342300(_, character: uint, asset: uint, region: uint):
    """Event 1044342300"""
    DisableCharacter(character)
    DisableAsset(asset)
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EnableAsset(asset)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
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
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableAsset(asset)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1044340650)
def Event_1044340650(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044340650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=EAST_WEEPING_PENINSULA_NW_SW))
    AND_1.Add(PlayerDoesNotHaveGood(9109))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100690))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_2):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1044343700)
def Event_1044343700(_, character: uint, character_1: uint, character_2: uint, asset: uint):
    """Event 1044343700"""
    WaitFrames(frames=1)
    DisableFlag(1044349200)
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
    AND_1.Add(FlagEnabled(1044349221))
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
    GotoIfFlagDisabled(Label.L20, flag=1044349222)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(1044349200))
    
    Restart()


@ContinueOnRest(1044343701)
def Event_1044343701(_, character: uint):
    """Event 1044343701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4743):
        return
    if FlagDisabled(1044349221):
        return
    
    MAIN.Await(CharacterDead(character))
    
    EnableNetworkFlag(1044349222)
    End()


@ContinueOnRest(1044343702)
def Event_1044343702(_, character: uint):
    """Event 1044343702"""
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
    
    if CharacterHasSpecialEffect(character=character, special_effect=9601):
        ForceAnimation(character, 20004)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9601))
    
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_7.Add(EntityBeyondDistance(entity=20000, other_entity=character, radius=6.0))
    OR_7.Add(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    MAIN.Await(OR_7)
    
    if CharacterHasSpecialEffect(character=character, special_effect=9603):
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
    
    if CharacterHasSpecialEffect(character=character, special_effect=9603):
        ForceAnimation(character, 20011)
        DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 9603))
    
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1044343703)
def Event_1044343703():
    """Event 1044343703"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1044349229):
        return
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=1044340700, radius=7.5))
    
    EnableNetworkFlag(1044349229)
    End()


@RestartOnRest(1044343704)
def Event_1044343704(_, character: uint):
    """Event 1044343704"""
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


@RestartOnRest(1044343705)
def Event_1044343705(_, character: uint, attacked_entity: uint):
    """Event 1044343705"""
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
    if CharacterHasSpecialEffect(character=character, special_effect=9601):
        ForceAnimation(character, 20004)
    if CharacterHasSpecialEffect(character=character, special_effect=9602):
        ForceAnimation(character, 20006)


@ContinueOnRest(1044343706)
def Event_1044343706(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1044343706"""
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
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_2)
    GotoIfLastConditionResultTrue(Label.L5, input_condition=OR_4)

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


@RestartOnRest(1044343707)
def Event_1044343707(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1044343707"""
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkFlag(flag_2)
    End()
    EnableNetworkFlag(flag_2)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_2)
    
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1044343710)
def Event_1044343710(_, character: uint):
    """Event 1044343710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(1044349252)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3607)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3607))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3602)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3607))
    
    Restart()
