"""
Northwest Liurnia (NE) (SW)

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
from .enums.m60_34_50_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034500000, asset=Assets.AEG099_060_9000)
    CommonFunc_9005810(
        0,
        flag=1034500703,
        grace_flag=1034500001,
        character=Characters.TalkDummy3,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005100(
        0,
        flag=76247,
        flag_1=76247,
        asset=Assets.AEG099_090_9000,
        source_flag=77230,
        value=0,
        flag_2=78230,
        flag_3=78231,
        flag_4=78232,
        flag_5=78233,
        flag_6=78234,
        flag_7=78235,
        flag_8=78236,
        flag_9=78237,
        flag_10=78238,
        flag_11=78239,
    )
    CommonFunc_900055278(
        0,
        flag=1034500739,
        asset=Assets.AEG099_251_2000,
        dummy_id=1506,
        action_button_id=9320,
        text=30050,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_900055278(
        0,
        flag=1034500739,
        asset=Assets.AEG099_251_2001,
        dummy_id=1506,
        action_button_id=9320,
        text=30050,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_900055278(
        0,
        flag=1034500739,
        asset=Assets.AEG099_251_2002,
        dummy_id=1506,
        action_button_id=9320,
        text=30050,
        left=0,
        left_1=0,
        left_2=0,
    )
    Event_1034503600(0, region=1034502500, flag=1034500738)
    Event_1034502610()
    Event_1034502620()
    CommonFunc_FieldBattleHealthBar(0, boss=Characters.GlintstoneDragon, name=904502601, npc_threat_level=25)
    CommonFunc_90005860(
        0,
        flag=1034500800,
        left=0,
        character=Characters.GlintstoneDragon,
        left_1=1,
        item_lot=0,
        seconds=0.0,
    )
    Event_1034502800()
    Event_1034502801()
    Event_1034502804()
    Event_1034502802()
    Event_1034502803()
    CommonFunc_90005300(0, flag=1035510200, character=Characters.Scarab, item_lot=40200, seconds=0.0, item_is_dropped=0)
    CommonFunc_90005525(0, flag=1034500620, asset=1034501620)
    CommonFunc_90005525(0, flag=1034500621, asset=1034501621)
    Event_1034502580()
    Event_1034502510()
    CommonFunc_90005501(
        0,
        flag=1034500510,
        flag_1=1034500511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        asset_2=Assets.AEG099_182_2000,
        flag_2=1034500512,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SorceressSellen,
        flag=1034509258,
        flag_1=3460,
        flag_2=1034502711,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.SorceressSellen,
        flag=3461,
        flag_1=3462,
        flag_2=1034502711,
        flag_3=1034509258,
        first_flag=3460,
        last_flag=3463,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.SorceressSellen, flag=3463, first_flag=3460, last_flag=3463)
    Event_1034503705(0, character=Characters.SorceressSellen)
    Event_1034503706()
    Event_1034503707()
    Event_1034500730(0, character=Characters.Ranni, asset=Assets.AEG110_347_2000)
    CommonFunc_90005704(0, attacked_entity=Characters.Ranni, flag=3743, flag_1=3740, flag_2=1034509401, right=3)
    CommonFunc_90005707(
        0,
        character=Characters.Ranni,
        flag=3741,
        flag_1=3742,
        flag_2=1034509401,
        flag_3=1034500738,
        first_flag=3740,
        last_flag=3743,
        right=0,
        animation_id=20003,
        left=1034502742,
        flag_4=1034502743,
    )
    CommonFunc_90005709(0, attacked_entity=Characters.Ranni, dummy_id=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.Ranni, dummy_id=960, vfx_id=603050)
    CommonFunc_90005708(0, character=Characters.Ranni, flag=3740, left=0)
    Event_1034500731()
    Event_1034500732(0, character=Characters.Ranni)
    Event_1034500733(0, character=Characters.Ranni)
    Event_1034500734()
    Event_1034500735()
    Event_1034500710(0, character=Characters.Iji)
    Event_1034500700(0, character=Characters.Blaidd0)
    Event_1034500701(
        0,
        character=Characters.Blaidd1,
        character_1=Characters.BlackKnifeAssassin0,
        character_2=Characters.BlackKnifeAssassin1,
        character_3=Characters.BlackKnifeAssassin2,
        character_4=Characters.BlackKnifeAssassin3,
    )
    CommonFunc_90005702(0, character=Characters.Blaidd1, flag=3603, first_flag=3600, last_flag=3603)
    Event_1034500702(0, character=Characters.Blaidd1)
    Event_1034500715(0, character=Characters.PreceptorSeluvis0)
    Event_1034500716(0, character=Characters.PreceptorSeluvis1)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.PreceptorSeluvis1,
        flag=3561,
        flag_1=3560,
        flag_2=1034509301,
        right=3,
    )
    CommonFunc_90005707(
        0,
        character=Characters.PreceptorSeluvis1,
        flag=3561,
        flag_1=3562,
        flag_2=1034509301,
        flag_3=3563,
        first_flag=3560,
        last_flag=3563,
        right=0,
        animation_id=90201,
        left=1034502722,
        flag_4=1034502723,
    )
    CommonFunc_90005709(0, attacked_entity=Characters.PreceptorSeluvis1, dummy_id=905, vfx_id=603001)
    CommonFunc_90005709(0, attacked_entity=Characters.PreceptorSeluvis1, dummy_id=200, vfx_id=603051)
    Event_1034500717(0, character=Characters.PreceptorSeluvis2)
    Event_1034500718(0, value=2)
    Event_1034500719()
    CommonFunc_90005773(0, flag=1034509347)
    Event_1034500712(
        0,
        character=Characters.NoxFighter,
        character_1=Characters.Omenkiller,
        character_2=Characters.FingerMaidenTherolina,
        character_3=Characters.DolorestheSleepingArrow,
        character_4=Characters.Jarwight,
    )
    Event_1034500713(0, character=Characters.NepheliLoux)
    Event_1034500714(0, character=Characters.DungEater)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9001,
        action_button_id=4110,
        item_lot=101480,
        first_flag=400148,
        last_flag=400148,
        flag=3569,
        dummy_id=0,
    )
    Event_1034503740()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.PreceptorSeluvis0)
    DisableBackread(Characters.PreceptorSeluvis1)
    DisableBackread(Characters.PreceptorSeluvis2)
    DisableBackread(Characters.NoxFighter)
    DisableBackread(Characters.SorceressSellen)
    DisableBackread(Characters.Ranni)
    DisableBackread(Characters.Omenkiller)
    DisableBackread(Characters.FingerMaidenTherolina)
    DisableBackread(Characters.DolorestheSleepingArrow)
    DisableBackread(Characters.Jarwight)
    DisableBackread(Characters.NepheliLoux)
    DisableBackread(Characters.Iji)
    DisableBackread(Characters.DungEater)
    DisableBackread(Characters.Blaidd0)
    DisableBackread(Characters.Blaidd1)
    DisableBackread(Characters.BlackKnifeAssassin0)
    DisableBackread(Characters.BlackKnifeAssassin1)
    DisableBackread(Characters.BlackKnifeAssassin2)
    DisableBackread(Characters.BlackKnifeAssassin3)
    EnableAssetInvulnerability(Assets.AEG110_347_2000)
    Event_1034500519()


@RestartOnRest(1034502340)
def Event_1034502340(_, character: uint):
    """Event 1034502340"""
    Kill(character, award_runes=True)


@ContinueOnRest(1034502580)
def Event_1034502580():
    """Event 1034502580"""
    RegisterLadder(start_climbing_flag=1034500580, stop_climbing_flag=1034500581, asset=Assets.AEG110_119_2000)


@RestartOnRest(1034502510)
def Event_1034502510():
    """Event 1034502510"""
    CommonFunc_90005500(
        0,
        flag=1034500510,
        flag_1=1034500511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        obj_act_id=1034503511,
        asset_2=Assets.AEG099_182_2000,
        obj_act_id_1=1034503512,
        region=1034502511,
        region_1=1034502512,
        flag_2=1034500512,
        flag_3=1034500513,
        left_1=0,
    )


@ContinueOnRest(1034500519)
def Event_1034500519():
    """Event 1034500519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1034500510)
    EnableThisSlotFlag()


@RestartOnRest(1034503600)
def Event_1034503600(_, region: uint, flag: uint):
    """Event 1034503600"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=20000, region=region))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_3.Add(CharacterOutsideRegion(character=20000, region=region))
    OR_3.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_3)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1034502610)
def Event_1034502610():
    """Event 1034502610"""
    DisableAsset(Assets.AEG099_254_2000)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034500737):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1034500738))
    AND_1.Add(FlagDisabled(1034500737))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(1034500736):
        SetRespawnPoint(respawn_point=1034502610)
        SaveRequest()
        EnableFlag(1034500736)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AddSpecialEffect(PLAYER, 514)
    DisableCharacter(1034505610)
    EnableAsset(Assets.AEG099_254_2000)
    OR_1.Add(FlagDisabled(1034500738))
    OR_1.Add(FlagEnabled(1034500737))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    RemoveSpecialEffect(PLAYER, 514)
    EnableCharacter(1034505610)
    DisableAsset(Assets.AEG099_254_2000)


@RestartOnRest(1034502620)
def Event_1034502620():
    """Event 1034502620"""
    if FlagDisabled(3617):
        return
    AND_1.Add(FlagEnabled(3617))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(1034505610)
    Wait(1.0)
    Restart()


@RestartOnRest(1034502800)
def Event_1034502800():
    """Event 1034502800"""
    if FlagEnabled(1034500800):
        return
    AddSpecialEffect(Characters.GlintstoneDragon, 10247)


@RestartOnRest(1034502801)
def Event_1034502801():
    """Event 1034502801"""
    if FlagEnabled(1034500800):
        return
    if CharacterHasSpecialEffect(character=Characters.GlintstoneDragon, special_effect=10207):
        return
    EnableImmortality(Characters.GlintstoneDragon)
    OR_1.Add(HealthRatio(Characters.GlintstoneDragon) < 0.5)
    
    MAIN.Await(OR_1)
    
    Wait(0.5)
    OR_2.Add(HealthRatio(Characters.GlintstoneDragon) < 0.5)
    SkipLinesIfConditionTrue(1, OR_2)
    Restart()
    EnableInvincibility(Characters.GlintstoneDragon)
    ReplanAI(Characters.GlintstoneDragon)
    ForceAnimation(Characters.GlintstoneDragon, 20009)
    if CharacterHasSpecialEffect(character=Characters.GlintstoneDragon, special_effect=10207):
        return
    Wait(1.0)
    Restart()


@RestartOnRest(1034502802)
def Event_1034502802():
    """Event 1034502802"""
    if FlagEnabled(1034500800):
        return
    
    MAIN.Await(FlagEnabled(1034420800))
    
    MAIN.Await(OR_1)
    
    DisableCharacter(Characters.GlintstoneDragon)
    EnableFlag(1034500800)


@RestartOnRest(1034502803)
def Event_1034502803():
    """Event 1034502803"""
    DisableNetworkSync()
    if FlagEnabled(1034500800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.GlintstoneDragon, region=1034502800))
    
    AddSpecialEffect(Characters.GlintstoneDragon, 10285)
    Wait(1.0)
    Restart()


@RestartOnRest(1034502804)
def Event_1034502804():
    """Event 1034502804"""
    if FlagEnabled(1034500800):
        return
    AND_1.Add(HealthRatio(Characters.GlintstoneDragon) < 0.5)
    AND_1.Add(CharacterHasSpecialEffect(Characters.GlintstoneDragon, 10207))
    
    MAIN.Await(AND_1)
    
    Wait(4.699999809265137)
    EnableFlag(1034500800)
    DisableCharacter(Characters.GlintstoneDragon)


@RestartOnRest(1034500700)
def Event_1034500700(_, character: uint):
    """Event 1034500700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L9, flag=3609)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3609))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3609))
    
    Restart()


@RestartOnRest(1034500701)
def Event_1034500701(_, character: uint, character_1: uint, character_2: uint, character_3: uint, character_4: uint):
    """Event 1034500701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L17, flag=3617)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    
    MAIN.Await(FlagEnabled(3617))
    
    Restart()

    # --- Label 17 --- #
    DefineLabel(17)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 30001)
    EnableBackread(character_2)
    EnableCharacter(character_2)
    ForceAnimation(character_2, 30002)
    EnableBackread(character_3)
    EnableCharacter(character_3)
    ForceAnimation(character_3, 30002)
    EnableBackread(character_4)
    EnableCharacter(character_4)
    ForceAnimation(character_4, 30001)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3602)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetCharacterTalkRange(character=character, distance=100.0)
    AddSpecialEffect(character, 9627)
    ForceAnimation(character, 930013)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3617))
    
    Restart()


@RestartOnRest(1034500702)
def Event_1034500702(_, character: uint):
    """Event 1034500702"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3603))
    AND_1.Add(FlagEnabled(3617))
    if AND_1:
        return
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    EnableFlag(1034502700)
    AddSpecialEffect(character, 9644)


@RestartOnRest(1034503705)
def Event_1034503705(_, character: uint):
    """Event 1034503705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3460):
        DisableFlag(1034509253)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3465))
    OR_1.Add(FlagEnabled(3466))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_2.Add(FlagEnabled(3465))
    OR_2.Add(FlagEnabled(3466))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagDisabled(Label.L1, flag=1034509256)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3463)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SkipLinesIfFlagDisabled(3, 1034509256)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(1034509258)
    ForceAnimation(character, 90100)
    SkipLinesIfFlagEnabled(3, 1034509256)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(1034509258)
    ForceAnimation(character, 90103)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagDisabled(3465))
    AND_15.Add(FlagDisabled(3466))
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1034503706)
def Event_1034503706():
    """Event 1034503706"""
    if FlagEnabled(3463):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(Characters.SorceressSellen) == 0)
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(Characters.SorceressSellen, True)
    AND_2.Add(TimeElapsed(seconds=20.0))
    
    MAIN.Await(AND_2)
    
    SetBackreadStateAlternate(Characters.SorceressSellen, False)


@RestartOnRest(1034503707)
def Event_1034503707():
    """Event 1034503707"""
    if FlagEnabled(1034509256):
        return
    SetTeamType(Characters.SorceressSellen, TeamType.NoTeam)
    AwaitFlagEnabled(flag=1034509256)
    SetTeamType(Characters.SorceressSellen, TeamType.FriendlyNPC)
    DisableNetworkConnectedFlagRange(flag_range=(3460, 3463))
    EnableNetworkFlag(3460)
    End()


@RestartOnRest(1034500710)
def Event_1034500710(_, character: uint):
    """Event 1034500710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L6, flag=3766)
    DisableCharacter(character)
    DisableBackread(character)
    EnableImmortality(character)
    
    MAIN.Await(FlagEnabled(3766))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930017)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3766))
    
    Restart()


@RestartOnRest(1034500712)
def Event_1034500712(_, character: uint, character_1: uint, character_2: uint, character_3: uint, character_4: uint):
    """Event 1034500712"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    EnableBackread(character_3)
    EnableBackread(character_4)
    EnableImmortality(character)
    EnableImmortality(character_1)
    EnableImmortality(character_2)
    EnableImmortality(character_3)
    EnableImmortality(character_4)
    ForceAnimation(character, 930002)
    ForceAnimation(character_1, 930010)
    ForceAnimation(character_2, 90101)
    ForceAnimation(character_3, 90101)
    ForceAnimation(character_4, 90101)
    End()


@RestartOnRest(1034500713)
def Event_1034500713(_, character: uint):
    """Event 1034500713"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L10, flag=4230)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4230))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90101)
    
    MAIN.Await(FlagDisabled(4230))
    
    Restart()


@RestartOnRest(1034500714)
def Event_1034500714(_, character: uint):
    """Event 1034500714"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L11, flag=4251)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4251))
    
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90101)
    
    MAIN.Await(FlagDisabled(4251))
    
    Restart()


@RestartOnRest(1034500715)
def Event_1034500715(_, character: uint):
    """Event 1034500715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L6, flag=3566)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3566))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3566))
    
    Restart()


@RestartOnRest(1034500716)
def Event_1034500716(_, character: uint):
    """Event 1034500716"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3560):
        DisableFlag(1034509302)
    SkipLinesIfFlagDisabled(2, 1034509346)
    SkipLinesIfFlagDisabled(1, 1034509328)
    IncrementEventValue(1034509339, bit_count=3, max_value=7)
    SkipLinesIfFlagDisabled(2, 1034509346)
    SkipLinesIfFlagDisabled(1, 1034509336)
    IncrementEventValue(1034509342, bit_count=3, max_value=7)
    DisableFlag(1034509346)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3567)
    GotoIfFlagEnabled(Label.L8, flag=3568)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3567, 3568)))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3560)
    GotoIfFlagEnabled(Label.L1, flag=3561)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3567, 3568)))
    
    Restart()


@RestartOnRest(1034500717)
def Event_1034500717(_, character: uint):
    """Event 1034500717"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3569)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3569))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3569))
    
    Restart()


@RestartOnRest(1034500718)
def Event_1034500718(_, value: int):
    """Event 1034500718"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509345):
        return
    
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(130000, 130100)) >= value)
    
    EnableFlag(1034509345)


@RestartOnRest(1034500719)
def Event_1034500719():
    """Event 1034500719"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagDisabled(1034502726))
    
    if FlagDisabled(120790):
        OR_1.Add(FlagEnabled(120790))
    if FlagDisabled(120800):
        OR_1.Add(FlagEnabled(120800))
    if FlagDisabled(120810):
        OR_1.Add(FlagEnabled(120810))
    if FlagDisabled(120820):
        OR_1.Add(FlagEnabled(120820))
    if FlagDisabled(120830):
        OR_1.Add(FlagEnabled(120830))
    if FlagDisabled(120840):
        OR_1.Add(FlagEnabled(120840))
    OR_1.Add(FlagEnabled(6000))
    
    MAIN.Await(OR_1)
    
    EnableFlag(1034502726)
    Restart()


@RestartOnRest(1034500730)
def Event_1034500730(_, character: uint, asset: uint):
    """Event 1034500730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3740):
        DisableFlag(1034509403)
    if FlagEnabled(1034509429):
        EnableNetworkFlag(1034502745)
    DisableNetworkFlag(1034502748)
    AND_15.Add(FlagEnabled(1051369358))
    AND_15.Add(FlagEnabled(9410))
    AND_15.Add(FlagDisabled(9412))
    SkipLinesIfConditionFalse(1, AND_15)
    EnableNetworkFlag(1034502748)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(3747))
    AND_1.Add(FlagDisabled(1034502748))
    GotoIfConditionTrue(Label.L7, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L8, flag=3748)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAssetInvulnerability(asset)
    AND_2.Add(FlagEnabled(3747))
    AND_2.Add(FlagDisabled(1034502748))
    OR_2.Add(FlagEnabled(3748))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3740)
    GotoIfFlagEnabled(Label.L1, flag=3741)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    GotoIfFlagEnabled(Label.L19, flag=1034509416)
    GotoIfFlagDisabled(Label.L19, flag=1034509418)
    SetTeamType(character, TeamType.NoTeam)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(character, 930000)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_4.Add(FlagEnabled(3747))
    AND_4.Add(FlagDisabled(1034502748))
    
    MAIN.Await(not AND_4)
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3740)
    GotoIfFlagEnabled(Label.L1, flag=3741)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    EnableImmortality(character)
    if FlagDisabled(1034509429):
        ForceAnimation(character, 930004)
    else:
        ForceAnimation(character, 930000)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3748))
    
    Restart()


@RestartOnRest(1034500731)
def Event_1034500731():
    """Event 1034500731"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509419):
        return
    
    MAIN.Await(EntityWithinDistance(entity=20000, other_entity=Characters.Ranni, radius=10.0))
    
    EnableFlag(1034509419)
    EnableFlag(3758)


@RestartOnRest(1034500732)
def Event_1034500732(_, character: uint):
    """Event 1034500732"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509410):
        return
    
    MAIN.Await(FlagEnabled(1034509410))
    
    if FlagDisabled(9130):
        EnableFlag(1034509412)
    EnableFlag(3618)
    EnableFlag(3778)
    EnableFlag(3578)
    SetTeamType(character, TeamType.NoTeam)
    EnableNetworkFlag(1034500738)
    BanishPhantoms(unknown=0)


@RestartOnRest(1034500733)
def Event_1034500733(_, character: uint):
    """Event 1034500733"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509416):
        return
    GotoIfFlagDisabled(Label.L0, flag=1034509417)
    Wait(0.10000000149011612)
    EnableFlag(1034509416)
    EnableFlag(3758)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(1034509416))
    
    EnableFlag(3618)
    EnableFlag(3778)
    EnableFlag(3578)
    SetTeamType(character, TeamType.FriendlyNPC)
    DisableNetworkFlag(1034500738)
    EnableNetworkFlag(1034500739)


@RestartOnRest(1034500734)
def Event_1034500734():
    """Event 1034500734"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509417):
        return
    OR_1.Add(FlagEnabled(1034509205))
    OR_1.Add(FlagDisabled(1034509412))
    AND_1.Add(FlagEnabled(1034509306))
    AND_1.Add(FlagEnabled(1034509358))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1034509417)


@RestartOnRest(1034500735)
def Event_1034500735():
    """Event 1034500735"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509424):
        return
    
    MAIN.Await(FlagEnabled(1034509424))
    
    EnableFlag(3578)


@RestartOnRest(1034503740)
def Event_1034503740():
    """Event 1034503740"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy2, radius=3.0))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12012713)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy2, radius=3.0))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12012713)
    Restart()
