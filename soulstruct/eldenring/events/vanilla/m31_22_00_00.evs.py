"""
Spiritcaller Cave

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
from .entities.m31_22_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31220000, asset=Assets.AEG099_060_9000)
    Event_31222800()
    Event_31222810()
    Event_31222811()
    Event_31222812()
    Event_31222849()
    Event_31222813(0, character=Characters.Snail5, flag=31222821)
    Event_31222813(1, character=Characters.GodskinNoble, flag=31222820)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    Event_31222500()
    CommonFunc_90005646(
        0,
        flag=31220800,
        left_flag=31222840,
        cancel_flag__right_flag=31222841,
        asset=Assets.AEG099_065_9000,
        player_start=31222840,
        area_id=31,
        block_id=22,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, character=Characters.Wolf4, region=31222304, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Wolf5, region=31222304, seconds=0.0, animation_id=0)
    Event_31222300()
    Event_31222306()
    Event_31222312()
    Event_31222305()
    Event_31222317()
    Event_31222301()
    Event_31222316()
    Event_31222303()
    Event_31222313()
    Event_31222304()
    Event_31222330()
    Event_31222340(0, entity=Characters.InabaDiscipleofOkina0, flag=31222304, seconds=0.10000000149011612)
    Event_31222340(1, entity=Characters.InabaDiscipleofOkina1, flag=31222305, seconds=0.10000000149011612)
    Event_31222340(2, entity=Characters.InabaDiscipleofOkina2, flag=31222306, seconds=0.10000000149011612)


@RestartOnRest(31222300)
def Event_31222300():
    """Event 31222300"""
    OR_5.Add(ThisEventSlotFlagEnabled())
    if OR_5:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31222300))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Snail0, 15007))
    AND_1.Add(CharacterDead(Characters.Snail4))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=31223300)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222301)
def Event_31222301():
    """Event 31222301"""
    if FlagEnabled(31222301):
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31222301))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Snail2, 15007))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=31223301)
    EnableNetworkFlag(31222301)


@RestartOnRest(31222303)
def Event_31222303():
    """Event 31222303"""
    OR_5.Add(ThisEventSlotFlagEnabled())
    if OR_5:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31222303))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Snail1, 15007))
    OR_5.Add(AND_1)
    
    MAIN.Await(OR_5)
    
    EnableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222304)
def Event_31222304():
    """Event 31222304"""
    OR_5.Add(ThisEventSlotFlagEnabled())
    if OR_5:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31222302))
    OR_5.Add(AND_1)
    
    MAIN.Await(OR_5)
    
    ForceAnimation(Characters.Snail3, 3002, wait_for_completion=True)
    EnableSpawner(entity=31223302)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222305)
def Event_31222305():
    """Event 31222305"""
    OR_5.Add(ThisEventSlotFlagEnabled())
    if OR_5:
        return
    OR_1.Add(HasAIStatus(Characters.Snail4, ai_status=AIStatusType.Battle))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Snail4))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(Characters.Snail4, 3002, wait_for_completion=True)
    EnableSpawner(entity=31223304)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222306)
def Event_31222306():
    """Event 31222306"""
    OR_5.Add(ThisEventSlotFlagEnabled())
    if OR_5:
        return
    OR_1.Add(HasAIStatus(Characters.Snail0, ai_status=AIStatusType.Battle))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Snail0))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(Characters.Snail0, 3002, wait_for_completion=True)
    EnableSpawner(entity=31223305)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222311)
def Event_31222311():
    """Event 31222311"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    OR_5.Add(AttackedWithDamageType(attacked_entity=Characters.Snail0))
    OR_5.Add(CharacterDead(Characters.Snail0))
    
    MAIN.Await(OR_5)
    
    DisableSpawner(entity=31223300)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222312)
def Event_31222312():
    """Event 31222312"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterDead(Characters.Snail0))
    
    Kill(Characters.Wolf0, award_runes=True)
    Kill(Characters.Wolf4, award_runes=True)
    Kill(Characters.Wolf2, award_runes=True)
    Kill(Characters.Wolf5, award_runes=True)
    Kill(Characters.WolfPackLeader7, award_runes=True)
    Kill(Characters.Wolf6, award_runes=True)
    Kill(Characters.InabaDiscipleofOkina2, award_runes=True)
    Kill(Characters.WolfPackLeader9, award_runes=True)
    DisableSpawner(entity=31223300)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222317)
def Event_31222317():
    """Event 31222317"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterDead(Characters.Snail4))
    
    Kill(Characters.WolfPackLeader6, award_runes=True)
    Kill(Characters.WolfPackLeader5, award_runes=True)
    Kill(31220200, award_runes=True)
    Kill(31220221, award_runes=True)
    Kill(Characters.WolfPackLeader1, award_runes=True)
    Kill(Characters.InabaDiscipleofOkina1, award_runes=True)
    Kill(Characters.WolfPackLeader8, award_runes=True)
    DisableSpawner(entity=31223304)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222314)
def Event_31222314():
    """Event 31222314"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    OR_5.Add(AttackedWithDamageType(attacked_entity=Characters.Snail1))
    OR_5.Add(CharacterDead(Characters.Snail1))
    
    MAIN.Await(OR_5)
    
    DisableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222313)
def Event_31222313():
    """Event 31222313"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterDead(Characters.Snail1))
    
    Kill(Characters.Wolf3, award_runes=True)
    Kill(Characters.Wolf1, award_runes=True)
    Kill(Characters.WolfPackLeader0, award_runes=True)
    DisableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222315)
def Event_31222315():
    """Event 31222315"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    OR_5.Add(AttackedWithDamageType(attacked_entity=Characters.Snail2))
    OR_5.Add(CharacterDead(Characters.Snail2))
    
    MAIN.Await(OR_5)
    
    DisableSpawner(entity=31223303)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222316)
def Event_31222316():
    """Event 31222316"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterDead(Characters.Snail2))
    
    Kill(Characters.WolfPackLeader2, award_runes=True)
    Kill(Characters.WolfPackLeader3, award_runes=True)
    Kill(Characters.WolfPackLeader4, award_runes=True)
    DisableSpawner(entity=31223301)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222330)
def Event_31222330():
    """Event 31222330"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterDead(Characters.Snail3))
    
    Kill(Characters.InabaDiscipleofOkina0, award_runes=True)
    DisableSpawner(entity=31223302)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222340)
def Event_31222340(_, entity: uint, flag: uint, seconds: float):
    """Event 31222340"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(seconds)
    ForceAnimation(entity, 60502)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31222500)
def Event_31222500():
    """Event 31222500"""
    GotoIfFlagDisabled(Label.L0, flag=31220500)
    DisableAsset(Assets.AEG020_125_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31222500))
    
    MAIN.Await(AND_1)
    
    DestroyAsset(Assets.AEG020_125_1000)
    EnableFlag(31220500)


@RestartOnRest(31222520)
def Event_31222520(_, flag: uint, flag_1: uint, asset: uint):
    """Event 31222520"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@RestartOnRest(31222800)
def Event_31222800():
    """Event 31222800"""
    if FlagEnabled(31220800):
        return
    
    MAIN.Await(HealthValue(Characters.Snail5) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Snail5, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Snail5))
    
    KillBossAndDisplayBanner(character=Characters.Snail5, banner_type=BannerType.EnemyFelled)
    Kill(Characters.Human)
    DisableCharacter(Characters.Human)
    DisableAnimations(Characters.Human)
    EnableFlag(31220800)
    EnableFlag(9248)
    if PlayerInOwnWorld():
        EnableFlag(61248)


@RestartOnRest(31222810)
def Event_31222810():
    """Event 31222810"""
    GotoIfFlagDisabled(Label.L0, flag=31220800)
    DisableCharacter(Characters.GodskinApostle)
    DisableAnimations(Characters.GodskinApostle)
    Kill(Characters.GodskinApostle)
    DisableCharacter(Characters.Snail5)
    DisableAnimations(Characters.Snail5)
    Kill(Characters.Snail5)
    DisableCharacter(Characters.GodskinNoble)
    DisableAnimations(Characters.GodskinNoble)
    Kill(Characters.GodskinNoble)
    DisableCharacter(Characters.Human)
    DisableAnimations(Characters.Human)
    Kill(Characters.Human)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Snail5)
    DisableAI(Characters.GodskinApostle)
    AND_1.Add(FlagEnabled(31222805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31222800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Snail5, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableAnimations(Characters.GodskinApostle)
    SetNetworkUpdateRate(Characters.GodskinApostle, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GodskinApostle, name=903560310)
    Wait(1.5)
    EnableAI(Characters.GodskinApostle)
    AddSpecialEffect(Characters.Human, 297810)
    DisableAnimations(Characters.Human)
    SetNetworkUpdateRate(Characters.Human, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(31222811)
def Event_31222811():
    """Event 31222811"""
    if FlagEnabled(31220800):
        return
    
    MAIN.Await(CharacterDead(Characters.GodskinApostle))
    
    DisableBossHealthBar(Characters.GodskinApostle, name=903560310)
    EnableFlag(31222842)
    Wait(5.0)
    EnableSpawner(entity=31223307)
    Wait(0.10000000149011612)
    EnableNetworkFlag(31222820)
    EnableAI(Characters.GodskinNoble)
    EnableAnimations(Characters.GodskinNoble)
    SetNetworkUpdateRate(Characters.GodskinNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GodskinNoble, name=903570310)


@RestartOnRest(31222812)
def Event_31222812():
    """Event 31222812"""
    if FlagEnabled(31220800):
        return
    
    MAIN.Await(CharacterDead(Characters.GodskinNoble))
    
    DisableBossHealthBar(Characters.GodskinNoble, name=903570310)
    Wait(5.0)
    EnableSpawner(entity=31223308)
    Wait(0.10000000149011612)
    EnableNetworkFlag(31222821)
    EnableBossHealthBar(Characters.Snail5, name=904140310)
    EnableAI(Characters.Snail5)
    EnableAnimations(Characters.Snail5)
    ForceAnimation(Characters.Snail5, 3011, wait_for_completion=True)
    SetNetworkUpdateRate(Characters.Snail5, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Snail5, name=904140310)
    Wait(3.0)
    ForceAnimation(Characters.Snail5, 1702)
    AddSpecialEffect(Characters.Snail5, 297811)


@RestartOnRest(31222813)
def Event_31222813(_, character: uint, flag: uint):
    """Event 31222813"""
    if FlagEnabled(31220800):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(AND_1)
    AND_3.Add(Singleplayer())
    AND_2.Add(not AND_3)
    
    MAIN.Await(AND_2)
    
    ActivateMultiplayerBuffs(character)
    Wait(3.0)
    OR_1.Add(CharacterHasSpecialEffect(character, 7820))
    OR_1.Add(CharacterHasSpecialEffect(character, 7821))
    OR_1.Add(CharacterHasSpecialEffect(character, 7822))
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()


@RestartOnRest(31222849)
def Event_31222849():
    """Event 31222849"""
    CommonFunc_9005800(
        0,
        flag=31220800,
        entity=Assets.AEG099_001_9000,
        region=31222800,
        flag_1=31222805,
        character=31225800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31220800,
        entity=Assets.AEG099_001_9000,
        region=31222800,
        flag_1=31222805,
        flag_2=31222806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31220800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=31220800,
        bgm_boss_conv_param_id=356000,
        flag_1=31222805,
        flag_2=31222806,
        right=0,
        flag_3=0,
        left=0,
        left_1=0,
    )
