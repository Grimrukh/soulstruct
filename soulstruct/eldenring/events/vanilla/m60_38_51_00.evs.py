"""
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
from .entities.m60_38_51_00_entities import *
from .entities.m60_38_50_00_entities import Characters as m60_38_Characters


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76302, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76302,
        asset=Assets.AEG099_060_9001,
        source_flag=77300,
        value=1,
        flag_2=78300,
        flag_3=78301,
        flag_4=78302,
        flag_5=78303,
        flag_6=78304,
        flag_7=78305,
        flag_8=78306,
        flag_9=78307,
        flag_10=78308,
        flag_11=78309,
    )
    Event_1038512800()
    Event_1038512810()
    Event_1038512849()
    Event_1038512500()
    CommonFunc_90005300(0, flag=1038510500, character=Characters.Scarab, item_lot_param_id=40302, seconds=0.0, left=0)
    Event_1038513700(0, character=Characters.RyatheScout, asset=Assets.AEG099_320_9000)
    CommonFunc_90005752(0, asset=Assets.AEG099_320_9000, vfx_id=200, model_point=120, seconds=3.0)
    Event_1038513701()
    Event_1038513702(0, attacked_entity=1038511700, other_entity=Characters.RyatheScout)
    Event_1038513703()
    CommonFunc_90005740(
        0,
        1038512725,
        1038512726,
        1038512727,
        1038510700,
        703,
        1038511701,
        703,
        0.20000000298023224,
        90203,
        -1,
        -1,
        1.2000000476837158,
    )
    CommonFunc_90005741(0, 1038512728, 1038512729, 1038512727, 1038510700, 90201, 0, -1, -1, 0.5)
    Event_1038513705(0, character=Characters.Millicent)
    CommonFunc_90005704(0, attacked_entity=Characters.Millicent, flag=4181, flag_1=4180, flag_2=1038519251, right=3)
    CommonFunc_90005703(0, 1038510705, 4181, 4182, 1038519251, 1059481190, 4180, 4184, -1)
    CommonFunc_90005702(0, character=Characters.Millicent, flag=4183, first_flag=4180, last_flag=4184)
    CommonFunc_90005771(0, 1038510950, 1038512700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.RyatheScout)
    DisableBackread(Characters.Millicent)
    DisableAsset(Assets.AEG099_320_9000)
    CommonFunc_90005261(0, 1038510301, 1038512301, 3.0, 0.0, -1)
    CommonFunc_90005261(0, character=1038510302, region=1038512301, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman0,
        animation_id=30002,
        animation_id_1=20002,
        region=1038512400,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman1,
        animation_id=30002,
        animation_id_1=20002,
        region=1038512400,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman2,
        animation_id=30002,
        animation_id_1=20002,
        region=1038512400,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanBeastman,
        region=1038512600,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005201(
        0,
        character=1038510602,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.DemiHumanShaman2, region=1038512482, seconds=0.0, animation_id=3005)
    Event_1038512405(
        0,
        character=Characters.DemiHuman4,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038512405(
        1,
        character=Characters.DemiHuman5,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038512405(
        2,
        character=Characters.LargeDemiHuman,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038512405(
        3,
        character=Characters.DemiHumanShaman0,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038512405(
        4,
        character=Characters.DemiHumanShaman3,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1038512405(5, 1038510490, 30002, 20002, 2.0, 0.0, 0, 0, 0, 0)


@RestartOnRest(1038512405)
def Event_1038512405(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1038512405"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_10.Add(CharacterHasSpecialEffect(Characters.DemiHuman3, 10530))
    OR_10.Add(CharacterHasSpecialEffect(Characters.DemiHuman6, 10530))
    OR_10.Add(CharacterHasSpecialEffect(Characters.DemiHumanShaman1, 10531))
    OR_2.Add(OR_10)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    End()


@RestartOnRest(1038512500)
def Event_1038512500():
    """Event 1038512500"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1038512500))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(1038500500):
        return
    EnableFlag(1038500500)
    PlaySoundEffect(1038512500, 990000020, sound_type=SoundType.m_Music)


@RestartOnRest(1038512800)
def Event_1038512800():
    """Event 1038512800"""
    if FlagEnabled(1038510800):
        return
    
    MAIN.Await(HealthValue(Characters.DemiHumanQueen) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.DemiHumanQueen, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.DemiHumanQueen))
    
    KillBossAndDisplayBanner(character=Characters.DemiHumanQueen, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG004_970_3000, obj_act_id=1110064)
    EnableFlag(1038510800)


@RestartOnRest(1038512810)
def Event_1038512810():
    """Event 1038512810"""
    GotoIfFlagDisabled(Label.L0, flag=1038510800)
    DisableCharacter(Characters.DemiHumanQueen)
    DisableAnimations(Characters.DemiHumanQueen)
    Kill(Characters.DemiHumanQueen)
    EnableAssetActivation(Assets.AEG004_970_3000, obj_act_id=1110064)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.DemiHumanQueen)
    ForceAnimation(Characters.DemiHumanQueen, 30000, loop=True)
    AND_2.Add(FlagEnabled(1038512805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1038512800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(Characters.DemiHumanQueen, 20000)
    EnableAI(Characters.DemiHumanQueen)
    SetNetworkUpdateRate(Characters.DemiHumanQueen, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DemiHumanQueen, name=904130540)
    DisableAssetActivation(Assets.AEG004_970_3000, obj_act_id=1110064)


@RestartOnRest(1038512849)
def Event_1038512849():
    """Event 1038512849"""
    CommonFunc_9005800(
        0,
        flag=1038510800,
        entity=Assets.AEG099_001_9000,
        region=1038512800,
        flag_1=1038512805,
        character=1038515800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1038510800,
        entity=Assets.AEG099_001_9000,
        region=1038512800,
        flag_1=1038512805,
        flag_2=1038512806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1038510800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1038510800,
        bgm_boss_conv_param_id=931000,
        flag_1=1038512805,
        flag_2=1038512806,
        right=0,
        flag_3=1038512802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005812(0, 1038510800, 1038511801, 3, 0, 0)


@RestartOnRest(1038513700)
def Event_1038513700(_, character: uint, asset: uint):
    """Event 1038513700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3420):
        DisableFlag(1038519203)
    if FlagEnabled(1038519207):
        EnableNetworkFlag(1038512720)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(FlagEnabled(1038519207))
    OR_1.Add(FlagEnabled(1038512720))
    AND_1.Add(FlagEnabled(3426))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(1038519207))
    OR_3.Add(FlagEnabled(1038512720))
    AND_3.Add(FlagEnabled(3426))
    AND_3.Add(OR_3)
    
    MAIN.Await(AND_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableAsset(asset)
    MoveAssetToCharacter(asset, character=character)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    OR_4.Add(FlagEnabled(1038519207))
    OR_4.Add(FlagEnabled(1038512720))
    AND_4.Add(FlagEnabled(3426))
    AND_4.Add(OR_4)
    
    MAIN.Await(not AND_4)
    
    Restart()


@RestartOnRest(1038513701)
def Event_1038513701():
    """Event 1038513701"""
    if PlayerNotInOwnWorld():
        return
    WaitFramesAfterCutscene(frames=1)
    if FlagDisabled(3426):
        return
    OR_1.Add(FlagEnabled(1038519207))
    OR_1.Add(FlagEnabled(1038509205))
    if OR_1:
        return
    OR_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=m60_38_Characters.TalkDummy2, radius=5.0))
    if OR_5:
        return
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1038512700))
    OR_2.Add(FlagEnabled(16000860))
    OR_2.Add(FlagEnabled(76301))
    OR_2.Add(FlagEnabled(76302))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(FlagEnabled(1038519207))
    OR_3.Add(FlagEnabled(1038509205))
    if OR_3:
        return
    EnableFlag(1038519207)
    End()


@RestartOnRest(1038513702)
def Event_1038513702(_, attacked_entity: uint, other_entity: uint):
    """Event 1038513702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3426):
        return
    if FlagEnabled(1038509205):
        return
    if FlagEnabled(1038512704):
        return
    GotoIfFlagDisabled(Label.L1, flag=1038512701)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    
    MAIN.Await(AND_1)
    
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(TimeElapsed(seconds=4.0))
    OR_3.Add(AND_2)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionFalse(Label.L7, input_condition=AND_2)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L5, flag=1038512701)
    GotoIfFlagDisabled(Label.L6, flag=1038512703)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    AND_5.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=10.0))
    SkipLinesIfConditionFalse(2, AND_5)
    EnableFlag(1038512700)
    
    MAIN.Await(FlagEnabled(1038512706))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    AND_6.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=10.0))
    SkipLinesIfConditionFalse(2, AND_6)
    EnableFlag(1038512702)
    
    MAIN.Await(FlagEnabled(1038512707))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(1038512704)
    End()


@RestartOnRest(1038513703)
def Event_1038513703():
    """Event 1038513703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3426):
        return
    if FlagEnabled(1038509205):
        return
    AND_1.Add(FlagEnabled(1038519205))
    AND_1.Add(FlagEnabled(1038519207))
    
    MAIN.Await(AND_1)
    
    EnableFlag(16008540)
    BanishPhantoms(unknown=0)
    WarpToMap(game_map=VOLCANO_MANOR, player_start=16002701)
    End()


@RestartOnRest(1038513705)
def Event_1038513705(_, character: uint):
    """Event 1038513705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    DisableNetworkFlag(1050389265)
    DisableNetworkFlag(1038519255)
    DisableNetworkFlag(4197)
    if FlagEnabled(4180):
        DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(4187))
    AND_1.Add(FlagEnabled(1050389266))
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    if PlayerNotInOwnWorld():
        AND_3.Add(FlagEnabled(4187))
        AND_3.Add(FlagEnabled(4197))
        GotoIfConditionTrue(Label.L6, input_condition=AND_3)
    DisableCharacter(character)
    DisableBackread(character)
    AND_2.Add(FlagEnabled(4187))
    AND_2.Add(FlagEnabled(1050389266))
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableNetworkFlag(1050389265)
    EnableNetworkFlag(1038519255)
    EnableNetworkFlag(4197)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
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
    AND_15.Add(FlagEnabled(4187))
    AND_15.Add(FlagEnabled(1050389266))
    AwaitConditionFalse(AND_15)
    Restart()
