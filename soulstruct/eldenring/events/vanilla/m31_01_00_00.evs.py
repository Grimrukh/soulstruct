"""
Earthbore Cave

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
from .entities.m31_01_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31010000, asset=Assets.AEG099_060_9000)
    Event_31012800()
    Event_31012810()
    Event_31012849()
    Event_31012811()
    Event_31012830()
    CommonFunc_90005646(
        0,
        flag=31010800,
        left_flag=31012840,
        cancel_flag__right_flag=31012841,
        asset=Assets.AEG099_065_9000,
        player_start=31012840,
        area_id=31,
        block_id=1,
        cc_id=0,
        dd_id=0,
    )
    Event_31012500()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Rat0, region=31012201, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat1, region=31012201, radius=2.0, seconds=0.0, animation_id=0)
    Event_31012200(0, character=Characters.Rat0, patrol_information_id=31013201)
    Event_31012200(1, character=Characters.Rat1, patrol_information_id=31013202)
    Event_31012230(0, character=Characters.Rat0)
    Event_31012230(1, character=Characters.Rat1)
    Event_31012207(0, character=Characters.Rat2, region=31012207, radius=2.0, seconds=7.0, animation_id=0)
    Event_31012207(1, character=Characters.Rat3, region=31012207, radius=2.0, seconds=10.0, animation_id=0)
    Event_31012207(2, character=Characters.Rat4, region=31012207, radius=2.0, seconds=15.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat5, region=31012221, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat6, region=31012221, radius=2.0, seconds=0.0, animation_id=0)
    Event_31012207(3, character=Characters.GiantRat, region=31012207, radius=3.0, seconds=3.0, animation_id=0)
    Event_31012220(0, character=Characters.Rat2)
    Event_31012220(1, character=Characters.Rat3)
    Event_31012220(2, character=Characters.Rat4)
    Event_31012220(3, character=Characters.GiantRat)


@RestartOnRest(31012500)
def Event_31012500():
    """Event 31012500"""
    GotoIfFlagDisabled(Label.L0, flag=31010500)
    DisableAsset(Assets.AEG020_125_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31012500))
    
    MAIN.Await(AND_1)
    
    DestroyAsset(Assets.AEG020_125_1000)
    EnableFlag(31010500)


@RestartOnRest(31012200)
def Event_31012200(_, character: uint, patrol_information_id: uint):
    """Event 31012200"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(HasAIStatus(Characters.Rat2, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(Characters.Rat3, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(Characters.Rat4, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(Characters.GiantRat, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31012207)
def Event_31012207(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31012207"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(OR_5)
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
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
    OR_6.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(OR_6)
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_5)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31012220)
def Event_31012220(_, character: uint):
    """Event 31012220"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=1.5))
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
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    EnableAI(character)


@RestartOnRest(31012230)
def Event_31012230(_, character: uint):
    """Event 31012230"""
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
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=7.0))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Rat0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Rat1))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31012800)
def Event_31012800():
    """Event 31012800"""
    if FlagEnabled(31010800):
        return
    
    MAIN.Await(HealthValue(Characters.Runebear) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Runebear, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Runebear))
    
    KillBossAndDisplayBanner(character=Characters.Runebear, banner_type=BannerType.EnemyFelled)
    EnableFlag(31010800)
    EnableFlag(9231)
    if PlayerInOwnWorld():
        EnableFlag(61231)


@RestartOnRest(31012810)
def Event_31012810():
    """Event 31012810"""
    GotoIfFlagDisabled(Label.L0, flag=31010800)
    DisableCharacter(Characters.Runebear)
    DisableAnimations(Characters.Runebear)
    Kill(Characters.Runebear)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Runebear)
    ForceAnimation(Characters.Runebear, 30000)
    GotoIfFlagEnabled(Label.L1, flag=31010801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31012801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Runebear, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(31010801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(31012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Runebear)
    ForceAnimation(Characters.Runebear, 20000)
    SetNetworkUpdateRate(Characters.Runebear, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Runebear, name=904630310)


@RestartOnRest(31012811)
def Event_31012811():
    """Event 31012811"""
    if FlagEnabled(31010800):
        return
    AND_1.Add(HealthRatio(Characters.Runebear) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31012802)


@RestartOnRest(31012830)
def Event_31012830():
    """Event 31012830"""
    if FlagEnabled(31010801):
        return
    AddSpecialEffect(Characters.TalkDummy0, 9531)
    AwaitFlagEnabled(flag=31010801)
    AddSpecialEffect(Characters.TalkDummy0, 9532)


@RestartOnRest(31012849)
def Event_31012849():
    """Event 31012849"""
    CommonFunc_9005800(
        0,
        flag=31010800,
        entity=Assets.AEG099_001_9000,
        region=31012800,
        flag_1=31012805,
        character=31015800,
        action_button_id=10000,
        left=31010801,
        region_1=31012801,
    )
    CommonFunc_9005801(
        0,
        flag=31010800,
        entity=Assets.AEG099_001_9000,
        region=31012800,
        flag_1=31012805,
        flag_2=31012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31010800, asset=Assets.AEG099_001_9000, model_point=3, right=31010801)
    CommonFunc_9005822(
        0,
        flag=31010800,
        bgm_boss_conv_param_id=931000,
        flag_1=31012805,
        flag_2=31012806,
        right=0,
        flag_3=31012802,
        left=0,
        left_1=0,
    )
