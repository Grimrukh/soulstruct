"""
Liurnia to Altus Plateau (NE) (SW)

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
from .entities.m60_38_50_00_entities import *
from .entities.m60_38_51_00_entities import Characters as m60_38_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038500000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76209,
        flag_1=76209,
        asset=Assets.AEG099_090_9002,
        source_flag=77210,
        value=2,
        flag_2=78210,
        flag_3=78211,
        flag_4=78212,
        flag_5=78213,
        flag_6=78214,
        flag_7=78215,
        flag_8=78216,
        flag_9=78217,
        flag_10=78218,
        flag_11=78219,
    )
    RegisterGrace(grace_flag=1038500001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=76301, asset=Assets.AEG099_060_9002)
    CommonFunc_90005300(0, flag=1038500210, character=Characters.Scarab, item_lot=40256, seconds=0.0, left=0)
    Event_1038502580()
    Event_1038502500()
    Event_1038503700(0, character=Characters.RyatheScout, asset=Assets.AEG099_320_9000)
    CommonFunc_90005752(0, asset=1038501700, vfx_id=200, model_point=120, seconds=3.0)
    Event_1038503701()
    Event_1038503702(0, attacked_entity=1038501700, other_entity=Characters.RyatheScout)
    Event_1038503703()
    CommonFunc_90005740(
        0,
        flag=1038502705,
        flag_1=1038502706,
        left=1038502707,
        character=Characters.RyatheScout,
        model_point=703,
        asset=Assets.AEG099_090_9003,
        model_point_1=703,
        radius=0.20000000298023224,
        animation=90203,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.2000000476837158,
    )
    CommonFunc_90005741(
        0,
        flag=1038502708,
        flag_1=1038502709,
        left=1038502707,
        character=Characters.RyatheScout,
        animation__animation_id=90201,
        left_1=0,
        animation_id=-1,
        special_effect=-1,
        seconds=0.5,
    )
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy0, flag=1038502710)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy2, flag=1038502711)
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930023, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.RyatheScout)
    DisableAsset(Assets.AEG099_320_9000)
    DisableBackread(Characters.WanderingNoble)
    Event_1038502400(
        0,
        character=Characters.GuardianGolem1,
        region=1038502400,
        seconds=0.0,
        animation_id=0,
        attacked_entity=Characters.GuardianGolem0,
    )
    Event_1038502400(
        1,
        character=Characters.GuardianGolem0,
        region=1038502400,
        seconds=0.0,
        animation_id=0,
        attacked_entity=Characters.GuardianGolem1,
    )


@RestartOnRest(1038502400)
def Event_1038502400(_, character: uint, region: uint, seconds: float, animation_id: int, attacked_entity: uint):
    """Event 1038502400"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_15.Add(FlagDisabled(1046367500))
    OR_15.Add(FlagDisabled(1051397900))
    AND_1.Add(OR_15)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1038502500)
def Event_1038502500():
    """Event 1038502500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1038500500):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1038502550))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1038500500)


@RestartOnRest(1038502580)
def Event_1038502580():
    """Event 1038502580"""
    RegisterLadder(start_climbing_flag=1038500580, stop_climbing_flag=1038500581, asset=Assets.AEG027_009_1000)
    RegisterLadder(start_climbing_flag=1038500582, stop_climbing_flag=1038500583, asset=Assets.AEG027_009_1001)
    RegisterLadder(start_climbing_flag=1038500584, stop_climbing_flag=1038500585, asset=Assets.AEG027_047_1000)


@RestartOnRest(1038503700)
def Event_1038503700(_, character: uint, asset: uint):
    """Event 1038503700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3420):
        DisableFlag(1038519203)
    if FlagEnabled(1038509205):
        EnableNetworkFlag(1038502700)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(FlagEnabled(1038509205))
    OR_1.Add(FlagEnabled(1038502700))
    AND_1.Add(FlagEnabled(3426))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(1038509205))
    OR_3.Add(FlagEnabled(1038502700))
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
    OR_4.Add(FlagEnabled(1038509205))
    OR_4.Add(FlagEnabled(1038502700))
    AND_4.Add(FlagEnabled(3426))
    AND_4.Add(OR_4)
    
    MAIN.Await(not AND_4)
    
    Restart()


@RestartOnRest(1038503701)
def Event_1038503701():
    """Event 1038503701"""
    if PlayerNotInOwnWorld():
        return
    WaitFramesAfterCutscene(frames=1)
    if FlagDisabled(3426):
        return
    OR_1.Add(FlagEnabled(1038519207))
    OR_1.Add(FlagEnabled(1038509205))
    if OR_1:
        return
    OR_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=m60_38_Characters.TalkDummy0, radius=5.0))
    if OR_5:
        return
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1038502500))
    OR_2.Add(FlagEnabled(16000860))
    OR_2.Add(FlagEnabled(76301))
    OR_2.Add(FlagEnabled(76302))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(FlagEnabled(1038519207))
    OR_3.Add(FlagEnabled(1038509205))
    if OR_3:
        return
    EnableFlag(1038509205)
    End()


@RestartOnRest(1038503702)
def Event_1038503702(_, attacked_entity: uint, other_entity: uint):
    """Event 1038503702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3426):
        return
    if FlagEnabled(1038519207):
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


@RestartOnRest(1038503703)
def Event_1038503703():
    """Event 1038503703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3426):
        return
    if FlagEnabled(1038519207):
        return
    AND_1.Add(FlagEnabled(1038519205))
    AND_1.Add(FlagEnabled(1038509205))
    
    MAIN.Await(AND_1)
    
    EnableFlag(16008540)
    BanishPhantoms(unknown=0)
    WarpToMap(game_map=VOLCANO_MANOR, player_start=16002701)
    End()
